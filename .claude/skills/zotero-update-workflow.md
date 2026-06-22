# ZOT_003: Efficient NBRA Collection Update Workflow



## Overview
This document proposes an efficient method for updating ghs-wiki when new items are added to the Zotero NBRA collection. The workflow balances automation with human oversight and is triggered via manual comment.

---

## Current State (as of 2026-06-18)
- **NBRA collection**: 15 total items
- **Previously acquired**: 13 items (with 8 initial + 2 new from ZOT_002)
- **Manual workflow steps**: 
  1. Run fetch script
  2. Identify new raw stubs
  3. Create wiki source pages (manual metadata extraction)
  4. Update wiki/index.md
  5. Update wiki/log.md
  6. Build and verify

**Issue**: Steps 3-5 are repetitive and error-prone. A second issue surfaced during execution: the old helper script scanned the full `raw/` tree and mixed together three different cases that should be treated separately:
- genuinely new raw stubs that do not yet have source pages;
- already-processed stubs whose `zotero_item_key` changed after a refresh;
- reviewed source pages that are ready for index/log finalize.

---

## Proposed Efficient Workflow

### Phase 1: Automated Acquisition (Fetch)
```bash
cd ghs-wiki/.claude/skills/zotero-acquire
uv run --python 3.12 --with-requirements requirements.txt python fetch_zotero.py --collection NBRA
```
**Output**: New raw stubs written to `ghs-wiki/raw/papers/` (or other type folders)
**Time**: ~10 seconds

### Phase 2: Assisted Processing (Semi-Automated)

#### Option A: Manual Inline Processing (Recommended for oversight)
1. Review new stubs in `ghs-wiki/raw/papers/`
2. For each stub, extract frontmatter and create wiki source page manually
   - **Frontmatter contract**: Copy `zotero_item_key`, `title`, `authors`, `date_published`, `doi`, `url` from stub YAML
   - **Tags**: Derive from title, abstract, and topic relevance (e.g., health-security, disaster-response)
   - **Related concepts/entities**: Review stub for keywords matching existing concepts and entities
3. Add TL;DR, Key Findings, Implementation Implications sections
4. Add Related Concepts section with wiki links

**Advantages**: 
- Full human review of content quality
- Opportunity to add contextual insights
- Ensures semantic consistency across wiki
- Best for maintaining knowledge quality

**Time per source**: ~8-12 minutes

#### Option B: Template-Driven Batch Processing
Use a helper script to generate source page stubs with:
- Pre-populated frontmatter from raw stubs
- Placeholder sections (TL;DR, Key Findings, etc.)
- Suggested concept/entity links based on title keywords

```bash
# Changed-only preview
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=dry-run

# Changed-only template generation
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=template
```

This would:
1. Scan only changed raw markdown files by default
2. Keep only raw stubs that are not yet represented in `wiki/sources/`
3. Extract YAML frontmatter
4. Generate wiki source page templates in `wiki/sources/`
5. Pre-fill Related Concepts with keyword matching
6. Output summary + list of files for review

Backlog processing remains available, but only when explicitly requested with `--all-stubs`.

#### New Repair Slice: Provenance Refresh
When a fetch refreshes existing raw stubs and only `zotero_item_key` values change, that should not be treated as a new ingest batch.

```bash
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=provenance-refresh
```

This mode:
1. Scans only changed raw markdown files
2. Keeps only raw stubs that already map to `wiki/sources/`
3. Aligns `zotero_item_key` in the corresponding source pages
4. Leaves `wiki/index.md` and `wiki/log.md` untouched

#### New Finalize Slice: gated index/log automation
Once the generated source pages are reviewed and placeholder-free, finalize is allowed to update `wiki/index.md` and `wiki/log.md`.

```bash
uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=finalize --log-slug zot-003-nbra-update
```

This mode:
1. Scans only changed source pages by default
2. Refuses to proceed when placeholders remain
3. Refuses to auto-finalize batches above a small threshold unless `--force` is supplied
4. Rebuilds the Sources section in `wiki/index.md`
5. Prepends a matching ingest entry to `wiki/log.md`

These guards prevent the old failure mode where a broad repo scan created an unexpectedly large ingest surface.

**Advantages**: 
- 70% time savings for routine processing
- Consistent frontmatter handling
- Less manual typing

**Time per source**: ~3-5 minutes (filling in content sections)

#### Option C: Hybrid Approach (Recommended for production)
1. Run batch template generator (Option B) to create stubs
2. Manually review and enhance generated content
3. Add unique insights, fix auto-generated tags, link to new concepts if needed
4. Commit

**Effective Time**: ~5-7 minutes per source with best of both worlds

---

### Phase 3: Index & Log Updates

#### Automated Index Generation
Index regeneration is now bundled into `process_stubs_batch.py --mode=finalize` rather than a separate helper script.

This mode:
1. Scans only the changed reviewed source pages by default
2. Rebuilds the Sources section from all existing `wiki/sources/` pages
3. Preserves other sections (Entities, Concepts, Threads, Syntheses)
4. Refuses large or placeholder-heavy batches unless explicitly forced

#### Log Entry Generation
Each clean finalize batch prepends to `wiki/log.md`:
```markdown
## [YYYY-MM-DD] ingest | zot-nnn-batch-update-nb-ra

- Fetched from NBRA collection; new items: N
- Acquired N raw stubs → `raw/papers/`
- Processed N into wiki sources:
  - [[sources/YYYY-MM-DD-title-slug|Title]]
  - [[sources/YYYY-MM-DD-title-slug|Title]]
  - (...)
- Updated wiki/index.md with new sources
```

---

## Manual Comment-Based Triggering

### Recommended Trigger Mechanism

**Option 1: Inline Command in Terminal**
Keep a `.instructions.md` at repo root with:
```markdown
## Manual Update Trigger

When new items are added to NBRA in Zotero, execute:

    # 1. Fetch and verify
    cd ghs-wiki/.claude/skills/zotero-acquire
    uv run --python 3.12 --with-requirements requirements.txt python fetch_zotero.py --collection NBRA

  # 2. Preview only changed unprocessed stubs
  cd ghs-wiki
  uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=dry-run

  # 3. Generate templates for that same small delta
  uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=template

  # 4. If the change is only key churn on existing stubs instead, run:
  uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=provenance-refresh

  # 5. After reviewing generated pages, finalize the small clean batch
  uv run --with pyyaml python .claude/skills/process_stubs_batch.py --collection NBRA --mode=finalize --log-slug zot-003-nbra-update

  # 6. Build and verify
  npm run build && git status
```

**Option 2: Conversational Comment in Copilot Chat**
Simply ask: "Execute ZOT_003 update for NBRA collection"

This triggers:
1. Fetch of new items
2. Identification of changed unprocessed stubs only
3. Processing via chosen method (A, B, or C)
4. Optional provenance refresh if only keys changed
5. Gated index/log finalize
6. Build verification

---

## Proposed Helper Scripts (Implementation Plan)

### Script 1: `process_stubs_batch.py` 
**Purpose**: Handle the three small workflow slices explicitly

```python
# Modes:
# - dry-run: changed raw stubs not yet represented in wiki/sources/
# - template: generate source page skeletons for that same small delta
# - provenance-refresh: repair zotero_item_key drift for already-processed stubs
# - finalize: auto-update wiki/index.md and wiki/log.md only for small clean reviewed batches
```
The index/log responsibilities previously described as separate helper scripts are now folded into `finalize`.

---

## Recommended Update Cadence

| Trigger | Frequency | Method | Time Cost |
|---------|-----------|--------|-----------|
| Ad-hoc check | Weekly | Fetch + changed-only dry-run | 2-5 min |
| Small ingest | As needed | Template + finalize | 10-25 min |
| Provenance-only repair | As needed | provenance-refresh | 2-5 min |
| Large backlog | Rare | `--all-stubs` + manual review | Explicitly slower by design |

---

## Workflow Checklist for Next Update

When executing the next NBRA update, follow this checklist:

- [ ] **Acquire**: Run fetch_zotero.py from correct directory
- [ ] **Identify**: Run changed-only dry-run first
- [ ] **Decide**: Is this a new-stub batch or only provenance refresh?
- [ ] **Review**: Read raw stub YAML and content
- [ ] **Create**: Generate wiki/sources/ pages (manual or template-assisted)
  - [ ] Frontmatter: Copy/verify key fields
  - [ ] Tags: Add 2-4 relevant tags
  - [ ] TL;DR: Write 1-2 sentence summary
  - [ ] Key Findings: Extract 3-5 main points
  - [ ] Implementation Implications: Add practical insights
  - [ ] Related Concepts: Link to existing wiki concepts
- [ ] **Finalize**: Auto-update wiki/index.md and wiki/log.md only after the batch is reviewed and small
- [ ] **Verify**: `npm run build` and `git status`
- [ ] **Commit**: Stage and commit with clear message

---

## Next Steps

### Immediate (No script needed yet)
1. Document the current manual workflow in this file ✓
2. Use changed-only dry-run before every ingest
3. Reserve `--all-stubs` for intentional backlog work only
4. Keep provenance refresh separate from content ingest

### Short-term (1-2 weeks)
1. Validate the new split workflow on the next real NBRA delta
2. Refine finalize thresholds if typical batches are larger than expected
3. Optionally add an explicit `--since-ref` mode if changed-only based on working tree becomes too narrow
4. Refine based on experience

### Long-term (Future)
1. GitHub Actions workflow to auto-fetch weekly (optional)
2. Integration with VS Code task system for convenient triggering
3. Enhanced keyword-concept matching for better suggestions
4. Contribution workflow for collaborative enrichment

---

## Efficiency Summary

| Current Workflow | Time per 5-item batch | Automation Potential |
|---|---|---|
| Old broad-scan workflow | Unpredictable | Mixed new items, backlog, and provenance drift |
| Changed-only hybrid | Predictable small batches | Default path for routine updates |
| Provenance-refresh slice | Minimal | Keeps raw/source keys aligned without fake ingest work |

**Recommendation**: Use the split workflow by default: changed-only dry-run, template only for truly new stubs, provenance-refresh only for key churn, and finalize only for reviewed small clean batches.

---

## Manual Comment Trigger

**How to trigger**: In any context (chat, Claude annotations, etc.), simply provide a comment like:

```
# @claude Execute ZOT_003 update for NBRA
# Method: Hybrid (template + manual review)
# Expected items: Check and update as needed
```

This will:
1. Fetch new items from NBRA
2. Preview only the changed unprocessed delta
3. Process using chosen method
4. Run provenance refresh only if needed
5. Finalize index/log only when the reviewed batch is small and clean
6. Build and verify
