#!/usr/bin/env python3
"""process_stubs_batch.py — Assist ZOT_003 processing for NBRA raw stubs.

Usage examples:
    uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=dry-run
    uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=template
    uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=provenance-refresh
    uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=finalize

Default behavior is intentionally narrow:
    - template/dry-run only consider raw stubs changed in the working tree
    - only raw stubs not yet represented in wiki/sources/ are templated
    - provenance refresh is a separate mode for zotero_item_key churn
    - finalize auto-updates wiki/index.md and wiki/log.md only for small, clean batches
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")


KEYWORD_CONCEPT_MAP = {
    "pathogen": "pathogen-inventory-systems",
    "inventory": "pathogen-inventory-systems",
    "biosecurity": "biosecurity-capacity-building",
    "capacity": "biosecurity-capacity-building",
    "training": "biosecurity-capacity-building",
    "one health": "one-health-operationalization",
    "operational": "one-health-operationalization",
    "cross-sector": "one-health-operationalization",
    "coordination": "one-health-operationalization",
}

KEYWORD_ENTITY_MAP = {
    "rivm": "rivm",
    "bwc": "biological-weapons-convention",
    "weapons convention": "biological-weapons-convention",
    "who": "who",
    "world health organization": "who",
}

PLACEHOLDER_MARKERS = (
    "TO-BE-ASSIGNED",
    "_[",
    "(suggest concepts)",
    "(suggest entities)",
)


def find_repo_root() -> Path:
    cwd = Path.cwd().resolve()
    for parent in (cwd, *cwd.parents):
        if (parent / "CLAUDE.md").exists() and (parent / "wiki").exists() and (parent / "raw").exists():
            return parent
        if (parent / "ghs-wiki" / "CLAUDE.md").exists() and (parent / "ghs-wiki" / "wiki").exists():
            return parent / "ghs-wiki"
    return cwd


def run_git(repo_root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def parse_frontmatter_text(content: str, label: str = "content") -> dict:
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
        body = parts[2].strip()
        return {"frontmatter": frontmatter, "body": body, "content": content}
    except Exception as exc:
        print(f"Warning: Failed to parse {label}: {exc}", file=sys.stderr)
        return {}


def parse_frontmatter_file(filepath: Path) -> dict:
    return parse_frontmatter_text(filepath.read_text(encoding="utf-8"), filepath.name)


def raw_rel_key(raw_path: Path, repo_root: Path) -> str:
    return raw_path.resolve().relative_to((repo_root / "raw").resolve()).as_posix()


def extract_raw_ref_key(raw_ref: str) -> Optional[str]:
    parts = Path(raw_ref).parts
    if "raw" not in parts:
        return None
    idx = parts.index("raw")
    tail = parts[idx + 1 :]
    if len(tail) < 2:
        return None
    return "/".join(tail)


def get_source_records(sources_dir: Path) -> list[dict]:
    records = []
    for source_file in sorted(sources_dir.glob("*.md")):
        parsed = parse_frontmatter_file(source_file)
        if not parsed:
            continue
        frontmatter = parsed["frontmatter"]
        raw_ref = frontmatter.get("raw", "")
        raw_key = extract_raw_ref_key(raw_ref) if raw_ref else None
        records.append(
            {
                "path": source_file,
                "frontmatter": frontmatter,
                "body": parsed["body"],
                "content": parsed["content"],
                "raw_key": raw_key,
            }
        )
    return records


def get_processed_maps(sources_dir: Path) -> tuple[set[str], dict[str, dict]]:
    processed = set()
    source_map = {}
    for record in get_source_records(sources_dir):
        if record["raw_key"]:
            processed.add(record["raw_key"])
            source_map[record["raw_key"]] = record
    return processed, source_map


def get_changed_paths(repo_root: Path, scope: str) -> list[Path]:
    output = run_git(repo_root, "status", "--porcelain", "--untracked-files=all", "--", scope)
    changed = []
    for line in output.splitlines():
        if len(line) < 4:
            continue
        path_text = line[3:]
        if " -> " in path_text:
            path_text = path_text.split(" -> ", 1)[1]
        path = repo_root / path_text.strip()
        if path.suffix == ".md":
            changed.append(path)
    return changed


def suggest_concepts(title: str, abstract: str) -> list[str]:
    text = (title + " " + abstract).lower()
    concepts = set()
    for keyword, concept in KEYWORD_CONCEPT_MAP.items():
        if keyword in text:
            concepts.add(concept)
    return sorted(concepts)


def suggest_entities(title: str, abstract: str) -> list[str]:
    text = (title + " " + abstract).lower()
    entities = set()
    for keyword, entity in KEYWORD_ENTITY_MAP.items():
        if keyword in text:
            entities.add(entity)
    return sorted(entities)


def normalize_date(raw_date: str) -> str:
    raw_date = str(raw_date or "").strip()
    return raw_date.split()[0] if raw_date else "2026-01-01"


def derive_kind(item_type: str) -> str:
    kind_map = {
        "journalArticle": "paper",
        "conferencePaper": "paper",
        "book": "book",
        "report": "report",
        "webpage": "article",
        "blogPost": "article",
        "document": "article",
    }
    return kind_map.get(item_type, "article")


def derive_length(fulltext_source: str, item_type: str) -> str:
    if fulltext_source == "none":
        return "abstract-only ingest (no attachment/full text in Zotero)"
    if item_type in {"webpage", "blogPost", "document"}:
        return f"web page ({fulltext_source or 'zotero-extracted'} text)"
    if fulltext_source == "zotero-extracted":
        return "~N pages (zotero-extracted full text)"
    return "~N pages (full-text synthesis from source)"


def derive_fulltext_quality(fulltext_source: str, item_type: str, raw_folder: str) -> str:
    source = fulltext_source or "unknown"
    if source == "none":
        return "abstract-only (`fulltext_source: none`)."
    if item_type in {"webpage", "blogPost", "document"}:
        return f"{source} website text."
    if source == "zotero-extracted":
        return "zotero-extracted full text."
    return f"{source} content routed through raw/{raw_folder}/."


def generate_source_page(raw_file: Path, stub_data: dict, repo_root: Path) -> Optional[str]:
    frontmatter = stub_data.get("frontmatter", {})
    body = stub_data.get("body", "")
    if not frontmatter:
        return None

    title = frontmatter.get("title", "Untitled")
    authors = frontmatter.get("authors", []) or []
    date_published = normalize_date(frontmatter.get("date_published", ""))
    doi = frontmatter.get("doi", "")
    url = frontmatter.get("url", "")
    item_type = frontmatter.get("item_type", "article")
    abstract = frontmatter.get("abstract", "") or body
    fulltext_source = frontmatter.get("fulltext_source", "pdf")
    kind = derive_kind(item_type)
    raw_key = raw_rel_key(raw_file, repo_root)
    author_yaml = ""
    if authors:
        author_yaml = "  - " + "\n  - ".join(authors)

    concepts = suggest_concepts(title, abstract)
    entities = suggest_entities(title, abstract)
    concept_links = "\n- ".join(f"[[concepts/{item}|{item}]]" for item in concepts) if concepts else "(suggest concepts)"
    entity_links = "\n- ".join(f"[[entities/{item}|{item}]]" for item in entities) if entities else "(suggest entities)"

    fm_text = f"""---
type: source
kind: {kind}
title: "{title}"
author:
{author_yaml}
date_published: {date_published}
url: "{url}"
doi: "{doi}"
length: "{derive_length(fulltext_source, item_type)}"
raw: "../../raw/{raw_key}"
zotero_item_key: {frontmatter.get('zotero_item_key', '')}
zotero_collection: {frontmatter.get('zotero_collection', 'NBRA')}
fulltext_source: {fulltext_source}
tags:
  - TO-BE-ASSIGNED
---"""

    page_body = f"""
# {title}

## TL;DR

_[One to two sentence summary of the key contribution]_

## What was actually ingested

- Source channel: Zotero acquire from collection {frontmatter.get('zotero_collection', 'NBRA')}.
- Raw type: {item_type} routed to raw/{raw_file.parent.name}/.
- Full-text quality: {derive_fulltext_quality(fulltext_source, item_type, raw_file.parent.name)}

## Key findings

- _[Finding 1]_
- _[Finding 2]_
- _[Finding 3]_

## Implementation implications

- _[Implication 1]_
- _[Implication 2]_

## Related concepts

- {concept_links}

## Related entities

- {entity_links}
"""
    return fm_text + "\n\n" + page_body.strip() + "\n"


def determine_template_output_name(frontmatter: dict) -> str:
    date_str = normalize_date(frontmatter.get("date_published", ""))
    title_slug = re.sub(r"[^\w\s-]", "", frontmatter.get("title", "untitled").lower())
    title_slug = re.sub(r"[\s_-]+", "-", title_slug).strip("-")[:60]
    return f"{date_str}-{title_slug}.md"


def replace_line(content: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)


def update_source_key_content(content: str, new_key: str) -> str:
    updated = replace_line(content, r"^zotero_item_key:\s*.*$", f"zotero_item_key: {new_key}")
    updated = re.sub(r"^- Zotero item key: .*$", f"- Zotero item key: {new_key}", updated, flags=re.MULTILINE)
    return updated


def extract_tldr(body: str) -> str:
    match = re.search(r"## TL;DR\n(.*?)(?:\n## |\Z)", body, flags=re.S)
    if not match:
        return ""
    lines = [line.strip() for line in match.group(1).splitlines() if line.strip()]
    if not lines:
        return ""
    text = lines[0].strip()
    text = text.strip("_").strip()
    return re.sub(r"\s+", " ", text)


def build_sources_section(source_records: list[dict]) -> list[str]:
    entries = []
    for record in source_records:
        fm = record["frontmatter"]
        title = fm.get("title", record["path"].stem)
        summary = extract_tldr(record["body"]) or "Summary pending."
        date_key = str(fm.get("date_published", "9999-99-99"))
        entries.append((date_key, title.lower(), record["path"].stem, title, summary))
    entries.sort(key=lambda item: (item[0], item[1]))
    return [f"- [[sources/{stem}|{title}]] - {summary}" for _, _, stem, title, summary in entries]


def update_index(index_path: Path, source_records: list[dict]) -> None:
    lines = index_path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index("## Sources")
    except ValueError:
        raise RuntimeError("Could not locate '## Sources' section in wiki/index.md")

    end = len(lines)
    for idx in range(start + 1, len(lines)):
        if lines[idx].startswith("## "):
            end = idx
            break

    replacement = ["## Sources", ""] + build_sources_section(source_records) + [""]
    new_lines = lines[:start] + replacement + lines[end:]
    index_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def build_log_entry(args: argparse.Namespace, source_records: list[dict]) -> str:
    today = date.today().isoformat()
    label = args.log_slug or f"zot-003-{args.collection.lower()}-update"
    lines = [
        f"## [{today}] ingest | {label}",
        "",
        f"- Executed trigger: \"Update ghs-wiki from {args.collection} collection using ZOT_003 workflow\".",
        f"- Auto-finalize checks passed: {len(source_records)} source page(s), max allowed without force = {args.max_finalize_count}.",
        f"- Processed {len(source_records)} reviewed source page(s) into wiki index/log:",
    ]
    for record in source_records:
        title = record["frontmatter"].get("title", record["path"].stem)
        lines.append(f"  - [[sources/{record['path'].stem}|{title}]]")
    lines.append("- Updated [[index|wiki index]] with the current Sources section ordering.")
    return "\n".join(lines)


def prepend_log_entry(log_path: Path, entry: str) -> None:
    content = log_path.read_text(encoding="utf-8")
    frontmatter_end = content.find("---", 3)
    if frontmatter_end == -1:
        raise RuntimeError("Could not locate frontmatter end in wiki/log.md")
    insert_at = frontmatter_end + 3
    while insert_at < len(content) and content[insert_at] in "\r\n":
        insert_at += 1
    prefix = content[:insert_at]
    remainder = content[insert_at:].lstrip("\r\n")
    log_path.write_text(prefix + "\n\n" + entry + "\n\n" + remainder, encoding="utf-8")


def file_has_placeholders(record: dict) -> bool:
    haystack = record["content"]
    return any(marker in haystack for marker in PLACEHOLDER_MARKERS)


def filter_collection(records: list[dict], collection: str) -> list[dict]:
    wanted = collection.strip().lower()
    filtered = []
    for record in records:
        record_collection = str(record["frontmatter"].get("zotero_collection", "")).strip().lower()
        if not wanted or not record_collection or record_collection == wanted:
            filtered.append(record)
    return filtered


def resolve_raw_candidates(args: argparse.Namespace, repo_root: Path, raw_dir: Path) -> list[Path]:
    if args.new_stubs:
        stub_files = []
        for pattern in args.new_stubs.split():
            stub_files.extend(repo_root.glob(pattern))
        return sorted({path.resolve() for path in stub_files if path.suffix == ".md" and path.exists()})

    if args.all_stubs:
        return sorted(path.resolve() for path in raw_dir.rglob("*.md"))

    return sorted(path.resolve() for path in get_changed_paths(repo_root, "raw") if path.exists())


def resolve_source_candidates(args: argparse.Namespace, repo_root: Path, sources_dir: Path) -> list[dict]:
    if args.source_files:
        selected = []
        for pattern in args.source_files.split():
            selected.extend(repo_root.glob(pattern))
        candidate_paths = sorted({path.resolve() for path in selected if path.suffix == ".md" and path.exists()})
    elif args.all_stubs:
        candidate_paths = sorted(path.resolve() for path in sources_dir.glob("*.md"))
    else:
        candidate_paths = sorted(path.resolve() for path in get_changed_paths(repo_root, "wiki/sources") if path.exists())

    records = []
    for path in candidate_paths:
        parsed = parse_frontmatter_file(path)
        if not parsed:
            continue
        records.append(
            {
                "path": path,
                "frontmatter": parsed["frontmatter"],
                "body": parsed["body"],
                "content": parsed["content"],
                "raw_key": extract_raw_ref_key(parsed["frontmatter"].get("raw", "")),
            }
        )
    return filter_collection(records, args.collection)


def handle_template_mode(args: argparse.Namespace, repo_root: Path, raw_dir: Path, sources_dir: Path) -> int:
    processed_raws, _ = get_processed_maps(sources_dir)
    stub_files = resolve_raw_candidates(args, repo_root, raw_dir)
    if not stub_files:
        print("No changed raw stubs found.")
        return 0

    candidates = []
    for stub_file in stub_files:
        if raw_dir.resolve() not in stub_file.parents:
            continue
        parsed = parse_frontmatter_file(stub_file)
        if not parsed:
            print(f"  ⊘ {stub_file.name} (failed to parse)")
            continue
        collection = str(parsed["frontmatter"].get("zotero_collection", "")).strip().lower()
        if args.collection and collection and collection != args.collection.strip().lower():
            continue
        key = raw_rel_key(stub_file, repo_root)
        if key in processed_raws:
            continue
        candidates.append((stub_file, parsed))

    if not candidates:
        print("No new unprocessed stubs found in the changed raw set.")
        return 0

    print(f"Found {len(candidates)} new stub(s) to process:")
    generated = []
    for stub_file, parsed in candidates:
        output_name = determine_template_output_name(parsed["frontmatter"])
        output_path = sources_dir / output_name
        content = generate_source_page(stub_file, parsed, repo_root)
        if not content:
            print(f"  ⊘ {stub_file.name} (could not generate content)")
            continue
        if args.mode == "dry-run":
            print(f"  ✓ {output_name} (preview)")
            print(f"    Title: {parsed['frontmatter'].get('title', 'Untitled')}")
            print(f"    Authors: {', '.join(parsed['frontmatter'].get('authors', []))}")
            print()
            continue

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(f"  ✓ {output_name}")
        generated.append(output_name)

    if args.mode == "template" and generated:
        print(f"\nGenerated {len(generated)} wiki source page(s) in {sources_dir}/")
        print("Next: review content, remove placeholders, then run finalize mode once the delta is small and clean.")
    return 0


def handle_provenance_refresh(args: argparse.Namespace, repo_root: Path, raw_dir: Path, sources_dir: Path) -> int:
    _, source_map = get_processed_maps(sources_dir)
    raw_candidates = resolve_raw_candidates(args, repo_root, raw_dir)
    if not raw_candidates:
        print("No changed raw stubs found for provenance refresh.")
        return 0

    updates = []
    for raw_path in raw_candidates:
        if raw_dir.resolve() not in raw_path.parents:
            continue
        raw_parsed = parse_frontmatter_file(raw_path)
        if not raw_parsed:
            continue
        collection = str(raw_parsed["frontmatter"].get("zotero_collection", "")).strip().lower()
        if args.collection and collection and collection != args.collection.strip().lower():
            continue
        raw_key = raw_rel_key(raw_path, repo_root)
        source_record = source_map.get(raw_key)
        if not source_record:
            continue
        raw_item_key = str(raw_parsed["frontmatter"].get("zotero_item_key", "")).strip()
        source_item_key = str(source_record["frontmatter"].get("zotero_item_key", "")).strip()
        if raw_item_key and raw_item_key != source_item_key:
            updates.append((raw_path, source_record["path"], raw_item_key, source_item_key))

    if not updates:
        print("No zotero_item_key drift found between changed raw stubs and source pages.")
        return 0

    print(f"Found {len(updates)} provenance update(s):")
    for raw_path, source_path, new_key, old_key in updates:
        print(f"  ✓ {source_path.name}: {old_key} -> {new_key} (from {raw_path.name})")
        content = source_path.read_text(encoding="utf-8")
        source_path.write_text(update_source_key_content(content, new_key), encoding="utf-8")
    return 0


def handle_finalize(args: argparse.Namespace, repo_root: Path, sources_dir: Path) -> int:
    source_records = resolve_source_candidates(args, repo_root, sources_dir)
    if not source_records:
        print("No changed source pages found to finalize.")
        return 0

    if len(source_records) > args.max_finalize_count and not args.force:
        print(
            f"Refusing to auto-finalize {len(source_records)} source pages. "
            f"Limit is {args.max_finalize_count}; rerun with --force if intentional."
        )
        return 1

    dirty = [record for record in source_records if file_has_placeholders(record)]
    if dirty and not args.force:
        print("Refusing to auto-finalize because placeholder content remains in:")
        for record in dirty:
            print(f"  - {record['path'].name}")
        return 1

    all_source_records = get_source_records(sources_dir)
    index_path = repo_root / "wiki" / "index.md"
    log_path = repo_root / "wiki" / "log.md"
    update_index(index_path, all_source_records)
    prepend_log_entry(log_path, build_log_entry(args, source_records))
    print(f"Updated {index_path} and {log_path} for {len(source_records)} source page(s).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collection", type=str, default="NBRA", help="Zotero collection name")
    parser.add_argument(
        "--mode",
        choices=["template", "dry-run", "provenance-refresh", "finalize"],
        default="template",
        help="Workflow slice to run",
    )
    parser.add_argument("--new-stubs", type=str, default=None, help="Explicit raw stub glob(s) to process")
    parser.add_argument("--source-files", type=str, default=None, help="Explicit source page glob(s) to finalize")
    parser.add_argument("--all-stubs", action="store_true", help="Ignore changed-only defaults and scan full directories")
    parser.add_argument("--max-finalize-count", type=int, default=8, help="Maximum auto-finalize batch size without --force")
    parser.add_argument("--log-slug", type=str, default=None, help="Override log entry slug for finalize mode")
    parser.add_argument("--force", action="store_true", help="Bypass finalize safety checks")
    args = parser.parse_args()

    repo_root = find_repo_root()
    raw_dir = repo_root / "raw"
    sources_dir = repo_root / "wiki" / "sources"
    if not raw_dir.exists() or not sources_dir.exists():
        print(f"Error: expected raw/ and wiki/sources/ under {repo_root}", file=sys.stderr)
        return 1

    if args.mode in {"template", "dry-run"}:
        return handle_template_mode(args, repo_root, raw_dir, sources_dir)
    if args.mode == "provenance-refresh":
        return handle_provenance_refresh(args, repo_root, raw_dir, sources_dir)
    return handle_finalize(args, repo_root, sources_dir)


if __name__ == "__main__":
    sys.exit(main())
