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

**Issue**: Steps 3-5 are repetitive and error-prone. Sources need metadata extraction, metadata formatting, and careful frontmatter assembly.

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
# Proposed command (helper script not yet implemented):
python process_stubs_batch.py --collection NBRA --mode=template
```

This would:
1. Scan `raw/papers/` for NEW markdown files (tracking against git history)
2. Extract YAML frontmatter
3. Generate wiki source page templates in `wiki/sources/`
4. Pre-fill Related Concepts with keyword matching
5. Output summary of generated files

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

#### Automated Index Generation (Helper Script Needed)
```bash
python regenerate_wiki_index.py --source-dir wiki/sources/ --index-file wiki/index.md
```

This would:
1. Scan `wiki/sources/` for all source pages
2. Extract `title`, `date_published`, `tags` from frontmatter
3. Sort chronologically
4. Regenerate wiki/index.md sources section
5. Preserve other sections (Entities, Concepts, Threads, Syntheses)

**Advantage**: Eliminates manual index updates

#### Log Entry Generation
Each batch ingest automatically prepends to `wiki/log.md`:
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

    # 2. Identify NEW stubs (compare timestamps to last run)
    ls -lt ghs-wiki/raw/papers/*.md | head

    # 3. Process each new stub into wiki/sources/
    # [Instructions for manual processing follow]

    # 4. Update index
    # [Index update command]

    # 5. Build and verify
    cd ghs-wiki && npm run build && git status
```

**Option 2: Conversational Comment in Copilot Chat**
Simply ask: "Execute ZOT_003 update for NBRA collection"

This triggers:
1. Fetch of new items
2. Identification of new stubs
3. Processing via chosen method (A, B, or C)
4. Index/log updates
5. Build verification

---

## Proposed Helper Scripts (Implementation Plan)

### Script 1: `process_stubs_batch.py` 
**Purpose**: Generate wiki source page templates from raw stubs

```python
# Usage:
# python process_stubs_batch.py --collection NBRA --mode=template
#
# Reads: raw/papers/*.md (new files from recent fetch)
# Writes: wiki/sources/*.md (generated template pages)
# Features:
# - Extracts YAML frontmatter from stubs
# - Identifies new vs. already-processed
# - Generates wiki source page skeleton
# - Suggests concept/entity links via keyword matching
# - Outputs summary + list of files for review
```

### Script 2: `regenerate_wiki_index.py`
**Purpose**: Auto-maintain wiki/index.md sources section

```python
# Usage:
# python regenerate_wiki_index.py --source-dir wiki/sources/ --index-file wiki/index.md
#
# Reads: wiki/sources/*.md (all source pages)
# Writes: wiki/index.md (updated sources section only)
# Features:
# - Chronological sorting by date_published
# - Preserves other index sections (Entities, Concepts, etc.)
# - Generates source list with summaries from TL;DR sections
```

### Script 3: `prep_log_entry.py`
**Purpose**: Generate formatted log entries for ingest batches

```python
# Usage:
# python prep_log_entry.py --new-sources wiki/sources/2024-*.md
#
# Reads: New source pages (by pattern or file list)
# Outputs: Markdown log entry formatted for prepending to wiki/log.md
# Features:
# - Extracts titles and dates
# - Formats as wiki links
# - Counts and summarizes batch
```

---

## Recommended Update Cadence

| Trigger | Frequency | Method | Time Cost |
|---------|-----------|--------|-----------|
| Ad-hoc check | Weekly | Fetch + Manual A | 20-40 min |
| Batch ingest | Bi-weekly | Batch B + Manual | 30-50 min (5-10 items) |
| Urgent priority | As needed | Fetch + Single A | 10-15 min per item |

---

## Workflow Checklist for Next Update

When executing the next NBRA update, follow this checklist:

- [ ] **Acquire**: Run fetch_zotero.py from correct directory
- [ ] **Identify**: List new stubs (timestamps vs. last run)
- [ ] **Review**: Read raw stub YAML and content
- [ ] **Create**: Generate wiki/sources/ pages (manual or template-assisted)
  - [ ] Frontmatter: Copy/verify key fields
  - [ ] Tags: Add 2-4 relevant tags
  - [ ] TL;DR: Write 1-2 sentence summary
  - [ ] Key Findings: Extract 3-5 main points
  - [ ] Implementation Implications: Add practical insights
  - [ ] Related Concepts: Link to existing wiki concepts
- [ ] **Index**: Update wiki/index.md (manual or auto-regenerate)
- [ ] **Log**: Prepend entry to wiki/log.md
- [ ] **Verify**: `npm run build` and `git status`
- [ ] **Commit**: Stage and commit with clear message

---

## Next Steps

### Immediate (No script needed yet)
1. Document the current manual workflow in this file ✓
2. Use **Method A** (inline processing) for 1-2 more batches
3. Track time and pain points
4. Identify which steps would benefit most from automation

### Short-term (1-2 weeks)
1. Implement `process_stubs_batch.py` (Priority: HIGH)
2. Implement `regenerate_wiki_index.py` (Priority: HIGH)
3. Test hybrid workflow (Method C) with next batch
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
| Fully manual (Method A) | ~60 minutes | – |
| Template-assisted (Method B) | ~35 minutes | 42% reduction |
| Hybrid (Method C) | ~40 minutes | 33% reduction with better quality |

**Recommendation**: Implement Method C (Hybrid) with Scripts 1-2 to achieve 33% time savings while maintaining quality oversight.

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
2. Process using chosen method
3. Update index/log
4. Build and verify
5. Report results
