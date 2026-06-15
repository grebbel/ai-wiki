---
name: zotero-acquire
description: Acquire sources from a local Zotero 7 library into the wiki's raw/ folder. Trigger when the user wants to pull items from Zotero into the wiki, ingest from a Zotero collection, or stop hand-copying PDFs into raw/. Reads the local Zotero HTTP API (no cloud, no key), copies each item's PDF into raw/<type>/, converts it to markdown, and writes an Acquire→Process stub. Acquire-phase only — never writes to wiki/.
---

# zotero-acquire

The canonical **Acquire-time** skill for getting sources out of a local Zotero 7 library and into
`raw/`, paralleling [`youtube-transcript-skill`](../youtube-transcript-skill/SKILL.md) for videos.
It reads Zotero's local HTTP API via `pyzotero` (`Zotero(0, "user", local=True)` →
`http://localhost:23119/api`, no account, no key), and for each top-level item in a chosen
collection:

1. **copies the primary binary attachment** (PDF/DOCX/EPUB) into `raw/<type>/<slug>.<ext>` —
   gitignored, co-located by type;
2. **converts it to markdown** with the repo's normal pipeline (`marker` → `markitdown` →
   `pdftotext`, whichever is installed);
3. **writes a markdown stub** `raw/<type>/<slug>.md` carrying the Acquire→Process frontmatter
   contract (below).

It is **Acquire-only**: it never touches `wiki/`. The human-supervised **Process** step (CLAUDE.md
§Process) turns each stub into a `wiki/sources/` page.

## When to use

- The user says "pull these from Zotero", "ingest my Zotero collection", "acquire from Zotero", or
  wants to stop hand-copying PDFs into `raw/`.
- After the user has dragged the sources they want into the dedicated **`ai-wiki`** Zotero collection
  (the scoping gate — the wider library never enters the wiki).

## Prerequisites (one time, on the user's machine)

1. Zotero 7 desktop app **running**.
2. Local API enabled: *Settings → Advanced → "Allow other applications on this computer to
   communicate with Zotero"*. Verify: `curl -s -o /dev/null -w "%{http_code}" http://localhost:23119/api/users/0/collections` returns `200`.
3. A dedicated collection (default name **`ai-wiki`**) holding the items to acquire.

No `pip install` needed if you run via `uv` (below); the deps (`pyzotero`, `PyYAML`) are declared in
`requirements.txt`.

## How to invoke

Run via `uv` (recommended — ephemeral, cached, no global installs):

```bash
cd .claude/skills/zotero-acquire

# Plan first — write/copy nothing, just show routing:
uv run --with-requirements requirements.txt python fetch_zotero.py --collection ai-wiki --dry-run

# Acquire for real:
uv run --with-requirements requirements.txt python fetch_zotero.py --collection ai-wiki
```

Flags:

| Flag | Default | Purpose |
| --- | --- | --- |
| `-c`, `--collection` | `ai-wiki` | Zotero collection name (case-insensitive) |
| `--dry-run` | off | Plan only — print routing, write/copy nothing |
| `--limit N` | `0` (all) | Cap items processed (handy for a test slice) |
| `--force` | off | Re-acquire even if `zotero_item_key` already present in `raw/` |
| `--json` | off | Emit per-item results as JSON to stdout |
| `--data-dir` | `~/Zotero` | Zotero data dir (where `storage/` lives) |
| `--raw-dir` | repo `raw/` | Override target (e.g. a temp dir for testing) |

**Always `--dry-run` first** to eyeball the `itemType → raw/<type>/` routing before writing.

## Workflow (Acquire → Process)

1. User drags sources into the `ai-wiki` Zotero collection.
2. Run `--dry-run`, review routing, then run for real. This is **Acquire** — log it as
   `acquire | zotero-batch ai-wiki (<n> items)` only if you stop here (per CLAUDE.md §Acquire).
3. For each new stub, run normal **Process** (CLAUDE.md §Process): verify identity/scope, fix the
   `raw/<type>/` routing if `item_type` mislabelled it (e.g. a report typed `webpage`), then write the
   `wiki/sources/` page and update concepts/entities/index/log. When Acquire + Process happen in the
   same session, the umbrella log op is `ingest | …` (no separate `acquire` entry).
4. Re-embed qmd after the batch (CLAUDE.md §Search): `npx @tobilu/qmd update && npx @tobilu/qmd embed`.

## The Acquire→Process contract (frontmatter the stub carries)

```yaml
---
zotero_item_key: CAJBMNHG          # dedup key + provenance (required)
zotero_collection: ai-wiki
item_type: webpage                 # raw Zotero itemType — a ROUTING HINT ONLY
title: "The 2026 AI Index Report | Stanford HAI"
authors: ["..."]                   # from Zotero creators (may be empty — fill at Process)
date_published: 2026-04            # best-effort ISO from Zotero's freeform `date`
doi: ""
isbn: ""
url: "https://hai.stanford.edu/ai-index/2026-ai-index-report"
citekey: ""                        # Better BibTeX "Citation Key:" from the Zotero `extra` field
abstract: "..."
attachment: <slug>.pdf             # copied filename (omitted when nothing copied)
fulltext_source: pdf-converted     # pdf-converted | doc-converted | zotero-extracted | none
converter: pdftotext               # marker | markitdown | pdftotext | "" (none)
notes: |
  Acquired from Zotero collection `ai-wiki`. itemType ... routed to raw/<type>/ — confirm at Process.
---

<converted markdown / extracted text / abstract>
```

**Canonical pre-flight fields Process must check:** `title`, `url` (or `doi`), `date_published`,
`zotero_item_key`. `fulltext_source` tells Process how trustworthy the body is:
`pdf-converted`/`doc-converted` = clean-ish; `zotero-extracted` = lossy plain text; `none` = body is
just the abstract or a URL pointer (fetch the real source before writing the wiki page).

## `itemType → raw/<type>/` map

| Zotero `itemType` | `raw/` folder |
| --- | --- |
| `journalArticle`, `conferencePaper`, `preprint`, `thesis` | `papers/` |
| `report` | `reports/` |
| `book`, `bookSection` | `books/` |
| `magazineArticle`, `newspaperArticle`, `blogPost`, `webpage`, `document` | `articles/` |
| `presentation` | `lectures/` |
| `videoRecording`, `podcast` | `videos/` (audio/video **not** transcribed here — use youtube-transcript-skill) |
| *(anything else)* | `articles/` (fallback) |

The map lives at the top of `fetch_zotero.py`; routing is a **first guess** that Process corrects.

## Attachment & full-text rules

- **Prefers a PDF attachment**; falls back to DOCX/EPUB, then HTML, then any stored file.
- **Only gitignored binaries** (`pdf`/`docx`/`epub`/`mobi`) are copied into `raw/`. HTML snapshots are
  converted from Zotero's stored copy **without** committing the page into the repo.
- **Conversion order:** `marker` → `markitdown` → `pdftotext`. On this machine only `pdftotext` is
  installed, so PDFs convert to layout-preserving plain text (no table structure). Install `marker`
  to upgrade all future runs automatically; or re-acquire a marquee paper by hand with `marker`.
- **No attachment / conversion fails** → uses Zotero's own extracted full text
  (`fulltext_source: zotero-extracted`); if none, the body is the abstract (`fulltext_source: none`).

## Dedup

Before writing, the script scans `raw/**/*.md` frontmatter for an existing `zotero_item_key`. Matches
are **skipped** (`skip (already acquired)`). `--force` overwrites — use when an item's attachment or
metadata changed in Zotero and you want to re-pull.

## Failure modes

- **`collection not found: 'ai-wiki'`** — name typo, or the collection doesn't exist yet. The error
  prints the available collection names. Create the collection in Zotero and drag items in.
- **HTTP connection refused / empty results** — Zotero app not running, or the local-API checkbox is
  off. Re-check the prerequisite `curl` returns `200`.
- **`converter: -` and `fulltext_source: zotero-extracted` or `none`** — no installed converter could
  read the file (e.g. an HTML-only item with no `markitdown`). Body is lossy/abstract-only; treat as a
  partial Acquire and fetch the real source at Process.
- **Garbled cover pages in pdftotext output** — `pdftotext -layout` mangles stylized cover art into
  spaced letters. Harmless; the body text is intact. Use `marker` if a clean render matters.

## Why pyzotero + local API (not the cloud Web API, not an MCP server)

The local API needs no account and no key, and it exposes attachment **file paths on disk**, which is
what lets us copy the real PDF into `raw/` for provenance. The cloud Web API would require per-account
keys and wouldn't give local file paths. A Zotero MCP server (e.g. `54yyyu/zotero-mcp`) is a fine
*interactive* read surface but is out of scope here — Acquire needs a deterministic, scriptable,
copy-the-binary path, which a self-contained script delivers. See
[`inspiration/2026-06-15-zotero-stack-integratie.md`](../../../inspiration/2026-06-15-zotero-stack-integratie.md)
and [`docs/superpowers/specs/2026-06-15-zotero-acquire-design.md`](../../../docs/superpowers/specs/2026-06-15-zotero-acquire-design.md).
