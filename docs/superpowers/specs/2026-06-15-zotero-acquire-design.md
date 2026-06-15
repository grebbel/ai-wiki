# Design — `zotero-acquire` skill

**Date:** 2026-06-15
**Status:** approved (pending spec review)
**Source notes:** [`inspiration/2026-06-15-zotero-stack-integratie.md`](../../../inspiration/2026-06-15-zotero-stack-integratie.md)
**Prior PRD:** [`inspiration/2026-05-14-prd-zotero-stack-integratie.md`](../../../inspiration/2026-05-14-prd-zotero-stack-integratie.md)

## Problem

Adding a source to the wiki means hand-copying a file into `raw/<type>/`, converting it to
markdown, and hand-writing frontmatter. The user already curates sources in a **local Zotero 7
library** (397 stored items, no cloud account). Zotero 7 ships a read-only local HTTP API at
`http://localhost:23119/api/` (no key, `users/0`) that exposes item metadata, collections, tags,
and attachment files on disk. We want a repeatable **Acquire** path that pulls user-chosen Zotero
items into `raw/` *without* giving up the immutable-`raw/` provenance discipline.

## Decisions (locked during brainstorming, 2026-06-15)

1. **Acquire mechanism = `pyzotero` against the local API** (`Zotero(local=True)`), in a
   self-contained Python script run via `uv`. Mirrors `youtube-transcript-skill`. **No MCP
   dependency.** The `zotero-mcp` server (live interactive querying) is explicitly **out of scope**
   for this build — it can be added later as a separate optional tool.
2. **Selection gate = a dedicated Zotero collection** (working name `ai-wiki`). The script pulls
   that collection by name. The wider library never enters the wiki. *(No `ai-wiki` collection
   exists yet — the user creates it and drags items in. The script takes `--collection <name>`, so
   the exact name is not load-bearing.)*
3. **Full-text policy = copy the real PDF, then convert as usual.** For each item, resolve its PDF
   attachment from Zotero storage; if present, **copy the PDF into `raw/<type>/<slug>.pdf`**
   (gitignored) and convert it to markdown via the repo's existing PDF pipeline
   (`marker` → `markitdown` → `pdftotext`, whichever is installed). Zotero's extracted plain text is
   only a **fallback** for items with no PDF attachment (webpages, notes).
4. **No binary committed to git.** `.gitignore` already excludes `raw/**/*.pdf` (and `.docx/.epub/…`).
   The copied PDF lives locally, co-located by type; the public repo holds only the markdown stub +
   provenance fields (`zotero_item_key`, `doi`/`url`) to re-fetch.
5. **Acquire only.** The skill stops at `raw/`. The existing human-supervised **Process** step turns
   the stub into a `wiki/sources/` page.

## Architecture

New skill directory `.claude/skills/zotero-acquire/`, structured like `youtube-transcript-skill`:

```
.claude/skills/zotero-acquire/
  SKILL.md            # trigger + usage + the Acquire→Process contract
  fetch_zotero.py     # pyzotero local-API client + PDF copy + convert
  requirements.txt    # pyzotero, PyYAML
  .python-version
```

Run pattern (via `uv`, like the youtube skill):

```sh
uv run --with-requirements .claude/skills/zotero-acquire/requirements.txt \
  .claude/skills/zotero-acquire/fetch_zotero.py --collection ai-wiki
```

### Data flow (per item in the named collection)

1. **List top-level items** of the collection: `GET /users/0/collections/<key>/items/top`.
   Skip standalone top-level `attachment` items (no parent metadata).
2. **Extract metadata** from `data`: `title`, `creators` → `authors`, `date` → `date_published`
   (normalized to ISO date), `DOI`, `ISBN`, `url`, `abstractNote` → `abstract`, `itemType`, `tags`.
   Better-BibTeX `citekey` captured if the extra field / BBT exposes it (best-effort; optional).
3. **Compute `<slug>`** by slugifying the title (lowercase, ASCII, `-`-joined, punctuation dropped) —
   same rule as the videos contract.
4. **Route to `raw/<type>/`** via the `itemType → type` map below. This is a *first guess*; Process
   corrects it (e.g. a report typed `webpage` in Zotero).
5. **Resolve PDF attachment:** `GET /users/0/items/<itemKey>/children`, filter
   `itemType == attachment && contentType == application/pdf`. Path =
   `<zotero-data-dir>/storage/<attachmentKey>/<filename>` (data dir default `~/Zotero`, overridable
   via `--data-dir`). If multiple PDFs, pick the first.
   - **PDF exists** → copy to `raw/<type>/<slug>.pdf`; convert to `raw/<type>/<slug>.md` via the
     first available of `marker` / `markitdown` / `pdftotext`. Record `fulltext_source: pdf-converted`
     and `converter: <tool>`.
   - **No PDF** → fetch Zotero extracted text from the *attachment* key
     (`GET /items/<attachmentKey>/fulltext`) if any attachment exists; else leave body empty with a
     pointer to `url`. Record `fulltext_source: zotero-extracted | none`; no PDF copied.
6. **Dedup on `zotero_item_key`:** before writing, scan `raw/**/*.md` frontmatter for an existing
   `zotero_item_key`. If found, **skip** (log `skip: already acquired`). `--force` overwrites.
7. **Write** `raw/<type>/<slug>.md` with the contract frontmatter (below) + body.

The script is **Acquire-only**: it never touches `wiki/`.

### `itemType → raw/<type>/` map

| Zotero `itemType` | `raw/` folder |
| --- | --- |
| `journalArticle`, `conferencePaper`, `preprint`, `thesis` | `papers/` |
| `report` | `reports/` |
| `book`, `bookSection` | `books/` |
| `magazineArticle`, `newspaperArticle`, `blogPost`, `webpage`, `document` | `articles/` |
| `presentation` | `lectures/` |
| `videoRecording`, `podcast` | `videos/` (note: audio/video not transcribed by this skill) |
| *(anything else)* | `articles/` (fallback) |

Map lives at the top of `fetch_zotero.py` for easy editing.

### Acquire→Process contract (frontmatter the script writes)

Parallels the videos YAML frontmatter contract in CLAUDE.md. The first block of each
`raw/<type>/<slug>.md`:

```yaml
---
zotero_item_key: CAJBMNHG          # dedup key + provenance (required)
zotero_collection: ai-wiki
item_type: webpage                 # raw Zotero itemType (routing hint only)
title: "The 2026 AI Index Report | Stanford HAI"
authors: ["Stanford HAI"]
date_published: 2026-04           # ISO, best-effort from Zotero `date`
doi: ""
isbn: ""
url: "https://hai.stanford.edu/ai-index/2026-ai-index-report"
citekey: ""                        # Better BibTeX if available
abstract: |
  ...
pdf: ai-index-report-2026.pdf      # filename only; omitted when no PDF copied
fulltext_source: pdf-converted     # pdf-converted | zotero-extracted | none
converter: pdftotext               # marker | markitdown | pdftotext | null
notes: |
  Acquired 2026-06-15 from Zotero collection `ai-wiki`.
  itemType `webpage` but content is a report — confirm raw/ routing at Process.
---

<converted markdown or extracted text body>
```

The four canonical pre-flight fields Process must check: `title`, `url` (or `doi`),
`date_published`, `zotero_item_key`. If `title` or both `url`+`doi` are missing → stop and ask.

## CLAUDE.md changes (in-scope)

1. **§Verifying sources before ingest → new subsection "Pre-flight check (Zotero stubs)":** the
   Zotero→source-page field-mapping table (mirrors the videos table), the dedup-on-`zotero_item_key`
   rule, the "PDF co-located in `raw/<type>/` and gitignored" convention, and honest-scoping guidance
   (`fulltext_source` tells Process whether the body is clean-converted, lossy-extracted, or empty).
2. **§Acquire:** name `zotero-acquire` as a canonical acquire-time skill alongside
   `youtube-transcript-skill`; document the dedicated-collection scoping and that Acquire-only batches
   log as `acquire | zotero-batch <collection> (<n> items)`.
3. **Drift fix:** change the existing "keep the original PDF in `raw/assets/`" prose to the actual
   **co-locate-by-type** practice (`raw/<type>/<slug>.pdf` next to its markdown), which the Zotero
   path depends on. (Flagged in the inspiration notes.)

## Out of scope / deferred

- `zotero-mcp` server + repo-root `.mcp.json` (optional live-query tool).
- Installing `marker` (script degrades to `pdftotext`, which is present).
- Zotero write-back (the native local API is read-only; not needed — we only read sources in).
- Auto-Process (Process stays human-supervised by design).

## Risks / wrinkles (confirmed against the live library)

- **`itemType` ≠ true source kind** (AI Index report typed `webpage`). Mitigated: routing is a guess,
  `notes:` flags it, Process corrects.
- **Multiple attachments per item** (PDF + HTML snapshot). Mitigated: prefer `application/pdf`.
- **Custom Zotero data dir.** Default `~/Zotero` (confirmed on this machine); `--data-dir` override.
- **`pdftotext` is unstructured** (no headings/tables). Acceptable per decision 3; a marquee paper can
  be re-acquired with `marker` later, or `marker` installed to upgrade all future runs automatically.
- **Local-API checkbox must be ON** (*Settings → Advanced → Allow other applications…*). Confirmed ON.

## Verification plan

1. Create a small test collection (or reuse one, e.g. `State of AI`, 3 items) with ≥1 PDF item.
2. `--dry-run` against it: assert correct slugs, type-routing, PDF detection, dedup — no files written.
3. Live run on the test collection: assert `raw/<type>/<slug>.{md,pdf}` written, frontmatter valid,
   PDF gitignored, dedup skips on a second run.
4. End-to-end: Process ≥3 acquired items into `wiki/sources/` pages (the inspiration notes'
   Definition-of-done).

## Definition of done

- `.claude/skills/zotero-acquire/` skill builds and dry-runs cleanly against the live API.
- CLAUDE.md carries the Zotero pre-flight subsection + §Acquire update + the `raw/assets/` drift fix.
- ≥3 collection items acquired and processed end-to-end.
