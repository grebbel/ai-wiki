# Quick Reference: NBRA Collection Update

## Default Update Flow

### Step 1: Fetch new items from Zotero
```bash
cd /Users/rtenhove/Documents/01_WORKSPACE/02_ghs_wiki/ghs-wiki/.claude/skills/zotero-acquire
uv run --python 3.12 --with-requirements requirements.txt python fetch_zotero.py --collection NBRA
```
**Output**: New or refreshed raw stubs written under `../../raw/`

### Step 2: Preview only the changed, unprocessed NBRA stubs
```bash
cd /Users/rtenhove/Documents/01_WORKSPACE/02_ghs_wiki/ghs-wiki
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=dry-run
```
**Output**: Only changed raw stubs that are not yet represented in `wiki/sources/`

### Step 3: Generate templates for that same small delta
```bash
cd /Users/rtenhove/Documents/01_WORKSPACE/02_ghs_wiki/ghs-wiki
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=template
```
**Output**: Generated pages in `wiki/sources/` with templates to fill in

### Step 4: Enhance generated content
1. Open each new file in `wiki/sources/`
2. Replace placeholders:
   - `_[One to two sentence summary...]_` → Write actual TL;DR
   - `- _[Finding 1]_` → Fill in key findings
   - `- _[Implication 1]_` → Add implementation implications
3. Verify suggested concepts/entities, adjust as needed

### Step 5: Auto-update index/log only when the batch is small and clean
```bash
cd /Users/rtenhove/Documents/01_WORKSPACE/02_ghs_wiki/ghs-wiki
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=finalize --log-slug zot-003-nbra-update
```
**Guardrails**:
- only changed `wiki/sources/` pages are considered
- placeholder content blocks auto-finalize
- batches larger than 8 files require `--force`

### Step 6: Verify and commit
```bash
cd /Users/rtenhove/Documents/01_WORKSPACE/02_ghs_wiki/ghs-wiki
npm run build
git status
git add -A
git commit -m "ZOT_003: Add N new NBRA sources (date-published dates)"
git push origin main
```

### Separate Repair Path: provenance refresh only
If the fetch step refreshed existing raw stubs and only `zotero_item_key` values changed, do not re-template pages. Run:

```bash
cd /Users/rtenhove/Documents/01_WORKSPACE/02_ghs_wiki/ghs-wiki
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=provenance-refresh
```

This updates matching `wiki/sources/` pages so raw/source provenance stays aligned.

---

## When to Use Each Method

| Scenario | Method | Time | Quality |
|----------|--------|------|---------|
| Regular weekly check | Changed-only template + finalize | 10-20 min for small delta | High |
| Manual deep review | Manual (full read) | 60-80 min/5 items | Very High |
| Quick urgent update | Dry-run + template only | 10-15 min per item | Medium |
| Provenance-only refresh | `provenance-refresh` | 2-5 min | High |
| Batch mode testing | Dry-run | ~2 min | N/A |

---

## Troubleshooting

### No new stubs found
- Check Zotero is running and API is accessible
- Verify: `curl -i http://localhost:23119/api/users/0/collections`
- Should return HTTP 200
- If the repo is clean, `dry-run` should now return `No changed raw stubs found.` instead of scanning the full backlog

### I want to process older backlog raw stubs on purpose
- Use: `uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=dry-run --all-stubs`
- Then rerun with `--mode=template --all-stubs` only when that backlog processing is intentional

### Existing source pages have stale Zotero keys
- Use: `uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=provenance-refresh`
- This is the repair path for refreshed raw stubs that already have wiki pages

### Finalize refuses to update index/log
- The batch is either too large, still contains placeholders, or includes source pages outside the requested collection
- Fix the pages first, or rerun intentionally with `--force`

### Script not finding raw directory
- Ensure you're running from `ghs-wiki/` directory
- Or specify explicit patterns, e.g. `--new-stubs 'raw/papers/*.md'`

### Generated concept/entity links are wrong
- Edit them manually in the generated page
- Or update `KEYWORD_CONCEPT_MAP` in process_stubs_batch.py

### Build fails after new sources
- Check markdown syntax in new files
- Verify frontmatter YAML is valid
- Run: `npm run check` for details

---

## File Locations

- **Fetch script**: `.claude/skills/zotero-acquire/fetch_zotero.py`
- **Batch processor**: `.claude/skills/process_stubs_batch.py`
- **Workflow guide**: `.claude/skills/zotero-update-workflow.md`
- **Raw stubs**: `raw/papers/` (temporary, not committed)
- **Wiki sources**: `wiki/sources/` (permanent, committed)
- **Index**: `wiki/index.md` (auto-updated only in finalize mode)
- **Log**: `wiki/log.md` (prepended only in finalize mode)

---

## Manual Trigger Commands

To trigger an update in Claude chat/annotation:

```
Update ghs-wiki from NBRA collection using ZOT_003 workflow
(fetch → dry-run changed delta → template → enhance → finalize → build → commit)
```

Or for provenance-only repair:

```
Repair refreshed Zotero item keys: process_stubs_batch.py --mode=provenance-refresh
```
