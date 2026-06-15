#!/usr/bin/env python3
"""zotero-acquire — pull items from a local Zotero collection into raw/<type>/ stubs.

Acquire-phase tool for the LLM wiki (see CLAUDE.md §Ingest / §Acquire). Reads the
local Zotero 7 HTTP API via pyzotero (no cloud account, no API key), and for each
top-level item in a chosen collection:

  1. copies the item's primary binary attachment (PDF/DOCX/EPUB) into the matching
     raw/<type>/ folder — gitignored, co-located by type;
  2. converts it to markdown with the repo's normal pipeline
     (marker -> markitdown -> pdftotext, whichever is installed);
  3. writes a markdown stub carrying the Acquire->Process frontmatter contract.

It NEVER touches wiki/. The human-supervised Process step turns each stub into a
wiki/sources/ page.

Usage:
    python fetch_zotero.py --collection ai-wiki
    python fetch_zotero.py --collection "State of AI" --dry-run
    python fetch_zotero.py -c ai-wiki --limit 3 --json

Requires the Zotero desktop app running with its local API enabled
(Settings -> Advanced -> "Allow other applications on this computer to
communicate with Zotero").
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml  (or run via uv with requirements.txt)")
try:
    from pyzotero import zotero
except ImportError:
    sys.exit("pyzotero required: pip install pyzotero  (or run via uv with requirements.txt)")


# Zotero itemType -> raw/<type>/ folder. A first guess only; Process corrects it
# (e.g. a report typed `webpage` in Zotero). Edit freely.
ITEM_TYPE_MAP = {
    "journalArticle": "papers",
    "conferencePaper": "papers",
    "preprint": "papers",
    "thesis": "papers",
    "report": "reports",
    "book": "books",
    "bookSection": "books",
    "magazineArticle": "articles",
    "newspaperArticle": "articles",
    "blogPost": "articles",
    "webpage": "articles",
    "document": "articles",
    "presentation": "lectures",
    "videoRecording": "videos",
    "podcast": "videos",
}
DEFAULT_TYPE = "articles"

# Attachment contentType -> short kind, in preference order (PDF first).
CONVERTIBLE_CT = [
    ("application/pdf", "pdf"),
    ("application/vnd.openxmlformats-officedocument.wordprocessingml.document", "docx"),
    ("application/epub+zip", "epub"),
    ("text/html", "html"),
]
# Only these extensions get copied into raw/ (they are gitignored binaries).
# Text formats (html) are converted from the Zotero source path without copying,
# so we never commit a scraped page into the repo.
BINARY_EXT = {"pdf", "docx", "epub", "mobi"}


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def slugify(text: str, maxlen: int = 80) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:maxlen].rstrip("-") or "untitled"


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "CLAUDE.md").exists() and (parent / "raw").exists():
            return parent
    return p.parents[3]


def creators_to_authors(creators) -> list[str]:
    out = []
    for c in creators or []:
        if c.get("name"):
            out.append(c["name"])
        else:
            nm = " ".join(x for x in (c.get("firstName"), c.get("lastName")) if x).strip()
            if nm:
                out.append(nm)
    return out


def norm_date(raw: str) -> str:
    """Best-effort ISO date from Zotero's freeform `date` field."""
    if not raw:
        return ""
    m = re.search(r"(\d{4})(?:[-/](\d{1,2}))?(?:[-/](\d{1,2}))?", raw)
    if not m:
        return raw.strip()
    y, mo, d = m.group(1), m.group(2), m.group(3)
    if mo and d:
        return f"{y}-{int(mo):02d}-{int(d):02d}"
    if mo:
        return f"{y}-{int(mo):02d}"
    return y


def extract_citekey(data: dict) -> str:
    """Better BibTeX writes 'Citation Key: xyz' into the Zotero `extra` field."""
    m = re.search(r"(?:Citation Key|citekey)\s*:\s*(\S+)", data.get("extra", "") or "", re.I)
    return m.group(1) if m else ""


# --------------------------------------------------------------------------- #
# converters (priority order; each returns markdown text or None)
# --------------------------------------------------------------------------- #
def _conv_marker(src: Path):
    if not shutil.which("marker_single"):
        return None
    with tempfile.TemporaryDirectory() as td:
        r = subprocess.run(
            ["marker_single", str(src), "--output_dir", td],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            return None
        mds = sorted(Path(td).rglob("*.md"))
        if mds:
            return mds[0].read_text(encoding="utf-8", errors="replace")
    return None


def _conv_markitdown(src: Path):
    if not shutil.which("markitdown"):
        return None
    r = subprocess.run(["markitdown", str(src)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 and r.stdout.strip() else None


def _conv_pdftotext(src: Path):
    if src.suffix.lower() != ".pdf" or not shutil.which("pdftotext"):
        return None
    r = subprocess.run(["pdftotext", "-layout", str(src), "-"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 and r.stdout.strip() else None


CONVERTERS = [
    ("marker", _conv_marker),
    ("markitdown", _conv_markitdown),
    ("pdftotext", _conv_pdftotext),
]


def convert(src: Path):
    """Return (markdown_text, converter_name) or (None, None)."""
    for name, fn in CONVERTERS:
        try:
            out = fn(src)
        except Exception:
            out = None
        if out:
            return out, name
    return None, None


# --------------------------------------------------------------------------- #
# Zotero access
# --------------------------------------------------------------------------- #
def pick_attachment(children):
    """Return (attachment_item, kind) preferring PDF, then docx/epub/html, then any file."""
    atts = [c for c in children if c["data"].get("itemType") == "attachment"]
    for ct, kind in CONVERTIBLE_CT:
        for c in atts:
            if c["data"].get("contentType") == ct:
                return c, kind
    for c in atts:
        if c["data"].get("filename"):
            return c, None
    return None, None


def attachment_path(data_dir: Path, att) -> Path | None:
    data = att["data"]
    if data.get("linkMode") == "linked_file" and data.get("path"):
        return Path(data["path"]).expanduser()
    fn = data.get("filename")
    if not fn:
        return None
    return data_dir / "storage" / att["key"] / fn


def zotero_fulltext(zot, attachment_key: str):
    try:
        content = (zot.fulltext_item(attachment_key) or {}).get("content", "")
        if content.strip():
            return content, "zotero-extracted"
    except Exception:
        pass
    return "", "none"


def existing_keys(raw_dir: Path) -> set[str]:
    keys: set[str] = set()
    for md in raw_dir.rglob("*.md"):
        try:
            head = md.read_text(encoding="utf-8", errors="replace")[:2000]
        except Exception:
            continue
        m = re.search(r"^zotero_item_key:\s*(\S+)", head, re.MULTILINE)
        if m:
            keys.add(m.group(1).strip().strip("\"'"))
    return keys


# --------------------------------------------------------------------------- #
# per-item processing
# --------------------------------------------------------------------------- #
def build_stub(meta: dict, body: str) -> str:
    fm = yaml.dump(
        meta, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100
    ).rstrip()
    return f"---\n{fm}\n---\n\n{body.rstrip()}\n"


def process_item(zot, item, collection, data_dir, raw_dir, seen, force, dry_run) -> dict:
    data = item["data"]
    key = item["key"]
    itype = data.get("itemType", "")
    title = data.get("title") or "(untitled)"
    slug = slugify(title)
    folder = ITEM_TYPE_MAP.get(itype, DEFAULT_TYPE)

    if key in seen and not force:
        return {"key": key, "type": itype, "slug": slug, "action": "skip (already acquired)"}

    attachment_name, converter, body = "", "", ""
    fulltext_source = "none"

    att, _kind = pick_attachment(zot.children(key))
    if att:
        src = attachment_path(data_dir, att)
        if src and src.exists():
            ext = src.suffix.lower().lstrip(".")
            if ext in BINARY_EXT:
                dest = raw_dir / folder / f"{slug}.{ext}"
                if not dry_run:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest)
                attachment_name = dest.name
            md, converter = convert(src)
            if md:
                body = md
                fulltext_source = "pdf-converted" if ext == "pdf" else "doc-converted"
            else:
                body, fulltext_source = zotero_fulltext(zot, att["key"])
        else:
            body, fulltext_source = zotero_fulltext(zot, att["key"])

    if not body:
        body = data.get("abstractNote") or "_(no extractable full text — see source URL)_"

    meta = {
        "zotero_item_key": key,
        "zotero_collection": collection,
        "item_type": itype,
        "title": title,
        "authors": creators_to_authors(data.get("creators")),
        "date_published": norm_date(data.get("date")),
        "doi": data.get("DOI", ""),
        "isbn": data.get("ISBN", ""),
        "url": data.get("url", ""),
        "citekey": extract_citekey(data),
        "abstract": data.get("abstractNote", ""),
    }
    if attachment_name:
        meta["attachment"] = attachment_name
    meta["fulltext_source"] = fulltext_source
    meta["converter"] = converter or ""
    meta["notes"] = (
        f"Acquired from Zotero collection `{collection}`. "
        f"itemType `{itype}` routed to raw/{folder}/ — confirm routing + identity at Process."
    )

    target = raw_dir / folder / f"{slug}.md"
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build_stub(meta, body), encoding="utf-8")
    seen.add(key)

    verb = "would write" if dry_run else "wrote"
    return {
        "key": key, "type": itype, "slug": slug,
        "action": f"{verb} {folder}/{slug}.md",
        "attachment": attachment_name or "-",
        "converter": converter or "-",
        "fulltext": fulltext_source,
    }


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Acquire a local Zotero collection into raw/ stubs.")
    ap.add_argument("-c", "--collection", default="ai-wiki", help="Zotero collection name (default: ai-wiki)")
    ap.add_argument("--data-dir", default=str(Path.home() / "Zotero"), help="Zotero data dir (default: ~/Zotero)")
    ap.add_argument("--raw-dir", default=None, help="raw/ dir (default: repo raw/)")
    ap.add_argument("--limit", type=int, default=0, help="Max items to process (0 = all)")
    ap.add_argument("--dry-run", action="store_true", help="Plan only; write/copy nothing")
    ap.add_argument("--force", action="store_true", help="Re-acquire even if zotero_item_key already present")
    ap.add_argument("--json", action="store_true", help="Emit per-item results as JSON to stdout")
    args = ap.parse_args()

    data_dir = Path(args.data_dir).expanduser()
    raw_dir = Path(args.raw_dir).expanduser() if args.raw_dir else repo_root() / "raw"

    zot = zotero.Zotero(0, "user", local=True)
    cols = zot.collections()
    target = args.collection.strip().lower()
    key = next((c["key"] for c in cols if c["data"]["name"].strip().lower() == target), None)
    if not key:
        names = ", ".join(sorted(c["data"]["name"] for c in cols))
        sys.exit(f"collection not found: {args.collection!r}\navailable: {names}")

    items = [it for it in zot.everything(zot.collection_items_top(key))
             if it["data"].get("itemType") not in ("attachment", "note")]
    if args.limit:
        items = items[: args.limit]

    seen = existing_keys(raw_dir)
    results = [process_item(zot, it, args.collection, data_dir, raw_dir, seen, args.force, args.dry_run)
               for it in items]

    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        mode = "DRY RUN" if args.dry_run else "ACQUIRE"
        print(f"[{mode}] collection {args.collection!r} ({key}) — {len(items)} item(s); raw -> {raw_dir}")
        for r in results:
            extra = "" if r["action"].startswith("skip") else \
                f"  [type={r.get('type','')} att={r.get('attachment','-')} conv={r.get('converter','-')} ft={r.get('fulltext','-')}]"
            print(f"  - {r['action']}{extra}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
