# Wiki Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the empty-but-correct wiki scaffold described in [`docs/superpowers/specs/2026-04-28-llm-wiki-design.md`](../specs/2026-04-28-llm-wiki-design.md), bringing the repo to a ready-for-first-ingest state.

**Architecture:** Three-layer structure (raw/, wiki/, schema). Wiki is page-type-partitioned with five flat type folders. Index and log files have canonical structure that subsequent ingests append to. `.gitignore` is established first to prevent OS/Obsidian noise from polluting the initial commit.

**Tech Stack:** Plain markdown, YAML frontmatter (for future pages), git, Obsidian (read interface, not required for scaffolding).

---

## Background

The repo currently contains:

- `llm-wiki.md` — upstream Karpathy pattern
- `CLAUDE.md` — runtime contract
- `docs/superpowers/specs/2026-04-28-llm-wiki-design.md` — design doc
- `.vscode/settings.json` — editor colors
- `.git/` — initialized with one commit (`2272749`) on `main`

This plan adds:

- `.gitignore` (root)
- `raw/` skeleton: 6 subdirectories, each with a `.gitkeep`
- `wiki/` skeleton: 5 type subdirectories with `.gitkeep`, plus `wiki/index.md` and `wiki/log.md` with canonical structure

After execution, the next operation should be the first real source ingest (out of scope for this plan).

## File Structure

| Path | Purpose | Created in task |
|---|---|---|
| `.gitignore` | Ignore macOS, Obsidian per-machine state, editor swap files | 1 |
| `raw/articles/.gitkeep` | Placeholder so empty dir is tracked by git | 2 |
| `raw/papers/.gitkeep` | Placeholder | 2 |
| `raw/lectures/.gitkeep` | Placeholder | 2 |
| `raw/books/.gitkeep` | Placeholder | 2 |
| `raw/images/.gitkeep` | Placeholder | 2 |
| `raw/assets/.gitkeep` | Placeholder | 2 |
| `wiki/sources/.gitkeep` | Placeholder | 3 |
| `wiki/entities/.gitkeep` | Placeholder | 3 |
| `wiki/concepts/.gitkeep` | Placeholder | 3 |
| `wiki/syntheses/.gitkeep` | Placeholder | 3 |
| `wiki/threads/.gitkeep` | Placeholder | 3 |
| `wiki/index.md` | Catalog with five canonical sections, all empty | 4 |
| `wiki/log.md` | Format documentation + inaugural `refactor` entry | 5 |

All commits land on `main`. The plan ends with one consolidated commit (Task 6) — six commits for a scaffold would bloat history without aiding revertability, since the scaffold is one logical unit.

---

### Task 1: Create `.gitignore`

**Files:**
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/.gitignore`

- [ ] **Step 1: Write `.gitignore`**

Write file `/Users/witoldtenhove/Projects/karpathy-wiki/.gitignore` with content:

```
# macOS
.DS_Store

# Obsidian — per-machine state (commit the rest of .obsidian/ if/when it appears)
.obsidian/workspace.json
.obsidian/workspaces.json
.obsidian/cache
.obsidian/.trash/

# Editor swap files
*.swp
*~
```

- [ ] **Step 2: Verify the file is staged-clean and matches**

Run:
```bash
test -f /Users/witoldtenhove/Projects/karpathy-wiki/.gitignore && grep -c "^" /Users/witoldtenhove/Projects/karpathy-wiki/.gitignore
```

Expected output:
```
12
```

(12 lines: 3 comment lines + 7 patterns + 2 blank lines.)

---

### Task 2: Create `raw/` skeleton

**Files:**
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/raw/articles/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/raw/papers/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/raw/lectures/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/raw/books/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/raw/images/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/raw/assets/.gitkeep`

- [ ] **Step 1: Create the six raw/ subdirectories**

Run:
```bash
mkdir -p /Users/witoldtenhove/Projects/karpathy-wiki/raw/articles \
         /Users/witoldtenhove/Projects/karpathy-wiki/raw/papers \
         /Users/witoldtenhove/Projects/karpathy-wiki/raw/lectures \
         /Users/witoldtenhove/Projects/karpathy-wiki/raw/books \
         /Users/witoldtenhove/Projects/karpathy-wiki/raw/images \
         /Users/witoldtenhove/Projects/karpathy-wiki/raw/assets
```

Expected: no output, exit code 0.

- [ ] **Step 2: Add `.gitkeep` placeholders so git tracks the empty dirs**

Run:
```bash
touch /Users/witoldtenhove/Projects/karpathy-wiki/raw/articles/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/raw/papers/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/raw/lectures/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/raw/books/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/raw/images/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/raw/assets/.gitkeep
```

Expected: no output, exit code 0.

- [ ] **Step 3: Verify the six subdirectories all exist with `.gitkeep`**

Run:
```bash
find /Users/witoldtenhove/Projects/karpathy-wiki/raw -name '.gitkeep' | sort
```

Expected output:
```
/Users/witoldtenhove/Projects/karpathy-wiki/raw/articles/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/raw/assets/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/raw/books/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/raw/images/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/raw/lectures/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/raw/papers/.gitkeep
```

(6 lines, alphabetical.)

---

### Task 3: Create `wiki/` type-folder skeleton

**Files:**
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/sources/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/entities/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/concepts/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/syntheses/.gitkeep`
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/threads/.gitkeep`

- [ ] **Step 1: Create the five wiki/ type subdirectories**

Run:
```bash
mkdir -p /Users/witoldtenhove/Projects/karpathy-wiki/wiki/sources \
         /Users/witoldtenhove/Projects/karpathy-wiki/wiki/entities \
         /Users/witoldtenhove/Projects/karpathy-wiki/wiki/concepts \
         /Users/witoldtenhove/Projects/karpathy-wiki/wiki/syntheses \
         /Users/witoldtenhove/Projects/karpathy-wiki/wiki/threads
```

Expected: no output, exit code 0.

- [ ] **Step 2: Add `.gitkeep` placeholders**

Run:
```bash
touch /Users/witoldtenhove/Projects/karpathy-wiki/wiki/sources/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/wiki/entities/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/wiki/concepts/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/wiki/syntheses/.gitkeep \
      /Users/witoldtenhove/Projects/karpathy-wiki/wiki/threads/.gitkeep
```

Expected: no output, exit code 0.

- [ ] **Step 3: Verify the five subdirectories all exist with `.gitkeep`**

Run:
```bash
find /Users/witoldtenhove/Projects/karpathy-wiki/wiki -name '.gitkeep' | sort
```

Expected output:
```
/Users/witoldtenhove/Projects/karpathy-wiki/wiki/concepts/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/wiki/entities/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/wiki/sources/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/wiki/syntheses/.gitkeep
/Users/witoldtenhove/Projects/karpathy-wiki/wiki/threads/.gitkeep
```

(5 lines, alphabetical.)

---

### Task 4: Create `wiki/index.md` with canonical structure

**Files:**
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/index.md`

The index has the five page-type sections in the fixed order from spec §9.1: Sources → Entities → Concepts → Syntheses → Threads. Each section is empty until the first ingest populates it.

- [ ] **Step 1: Write `wiki/index.md`**

Write file `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/index.md` with content:

````markdown
# Index

The catalog of every page in this wiki. Updated on every ingest. See [the design doc, §9.1](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#91-wikiindexmd) for format conventions.

Each section is flat-listed alphabetically. Once page counts grow, sections may be supplemented with Dataview blocks that auto-include pages by frontmatter `type:`.

## Sources

_(empty — first source ingest will populate this)_

## Entities

_(empty — first source ingest will populate this)_

## Concepts

_(empty — first source ingest will populate this)_

## Syntheses

_(empty — first synthesis page will populate this)_

## Threads

_(empty — first open question will populate this)_
````

- [ ] **Step 2: Verify all five sections exist in the correct order**

Run:
```bash
grep -E "^## " /Users/witoldtenhove/Projects/karpathy-wiki/wiki/index.md
```

Expected output (exactly, in this order):
```
## Sources
## Entities
## Concepts
## Syntheses
## Threads
```

If the order is wrong, the file is wrong — the five sections must appear in this canonical order so future ingests can rely on it.

---

### Task 5: Create `wiki/log.md` with format documentation and inaugural entry

**Files:**
- Create: `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/log.md`

The log is append-only. The inaugural entry uses operation `refactor` because the scaffold itself is a structural change, not an ingest.

- [ ] **Step 1: Write `wiki/log.md`**

Write file `/Users/witoldtenhove/Projects/karpathy-wiki/wiki/log.md` with content:

`````markdown
# Log

Append-only chronological record of wiki operations. Strict prefix format so `grep "^## \[" wiki/log.md | tail -10` works as a CLI:

```
## [YYYY-MM-DD] <op> | <title>
```

Permitted operations: `ingest`, `query`, `lint`, `synthesize`, `refactor`. See [the design doc, §9.2](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#92-wikilogmd) for details.

---

## [2026-04-28] refactor | scaffold initialized

Initial wiki scaffold built per [the design doc](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md). Created `raw/` (articles, papers, lectures, books, images, assets) and `wiki/` (sources, entities, concepts, syntheses, threads) skeletons with `.gitkeep` placeholders, plus this log and a canonical `index.md`. Ready for first source ingest.
`````

- [ ] **Step 2: Verify the prefix grep works on the inaugural entry**

Run:
```bash
grep "^## \[" /Users/witoldtenhove/Projects/karpathy-wiki/wiki/log.md
```

Expected output (exactly one line):
```
## [2026-04-28] refactor | scaffold initialized
```

If grep returns zero lines or more than one, the format is wrong — every future ingest depends on this prefix being greppable.

---

### Task 6: Verify scaffold and commit

**Files:**
- Modify: git tree (commit the 14 new files)

- [ ] **Step 1: Confirm the full file tree matches the spec**

Run:
```bash
cd /Users/witoldtenhove/Projects/karpathy-wiki && find . -path ./.git -prune -o -path ./.vscode -prune -o -type f -print | sort
```

Expected output (18 lines — 3 visible pre-existing tracked files [`CLAUDE.md`, the spec, `llm-wiki.md`] plus this plan plus 14 new scaffold files; `.vscode/settings.json` is pruned from the listing for clarity):
```
./.gitignore
./CLAUDE.md
./docs/superpowers/plans/2026-04-28-wiki-scaffold.md
./docs/superpowers/specs/2026-04-28-llm-wiki-design.md
./llm-wiki.md
./raw/articles/.gitkeep
./raw/assets/.gitkeep
./raw/books/.gitkeep
./raw/images/.gitkeep
./raw/lectures/.gitkeep
./raw/papers/.gitkeep
./wiki/concepts/.gitkeep
./wiki/entities/.gitkeep
./wiki/index.md
./wiki/log.md
./wiki/sources/.gitkeep
./wiki/syntheses/.gitkeep
./wiki/threads/.gitkeep
```

(That's 18 paths total. If any `.gitkeep` is missing, jump back to Task 2 or 3.)

- [ ] **Step 2: Stage the new files explicitly (no `-A`)**

Run:
```bash
git -C /Users/witoldtenhove/Projects/karpathy-wiki add \
  .gitignore \
  docs/superpowers/plans/2026-04-28-wiki-scaffold.md \
  raw/articles/.gitkeep raw/papers/.gitkeep raw/lectures/.gitkeep \
  raw/books/.gitkeep raw/images/.gitkeep raw/assets/.gitkeep \
  wiki/sources/.gitkeep wiki/entities/.gitkeep wiki/concepts/.gitkeep \
  wiki/syntheses/.gitkeep wiki/threads/.gitkeep \
  wiki/index.md wiki/log.md
```

Expected: no output, exit code 0.

- [ ] **Step 3: Verify the staged tree**

Run:
```bash
git -C /Users/witoldtenhove/Projects/karpathy-wiki status --short
```

Expected output (15 lines, all `A ` for added):
```
A  .gitignore
A  docs/superpowers/plans/2026-04-28-wiki-scaffold.md
A  raw/articles/.gitkeep
A  raw/assets/.gitkeep
A  raw/books/.gitkeep
A  raw/images/.gitkeep
A  raw/lectures/.gitkeep
A  raw/papers/.gitkeep
A  wiki/concepts/.gitkeep
A  wiki/entities/.gitkeep
A  wiki/index.md
A  wiki/log.md
A  wiki/sources/.gitkeep
A  wiki/syntheses/.gitkeep
A  wiki/threads/.gitkeep
```

If any unexpected entries appear (e.g. `.DS_Store`), `.gitignore` was wrong — fix Task 1 before committing.

- [ ] **Step 4: Commit**

Run:
```bash
git -C /Users/witoldtenhove/Projects/karpathy-wiki commit -m "$(cat <<'EOF'
Scaffold wiki: raw/ + wiki/ skeletons, index, log, gitignore

Implements docs/superpowers/specs/2026-04-28-llm-wiki-design.md §16:

- raw/: articles, papers, lectures, books, images, assets (each .gitkeep)
- wiki/: sources, entities, concepts, syntheses, threads (each .gitkeep)
- wiki/index.md: canonical 5-section structure, all empty
- wiki/log.md: format docs + inaugural refactor entry for 2026-04-28
- .gitignore: macOS .DS_Store, Obsidian per-machine state, editor swaps
- docs/superpowers/plans/2026-04-28-wiki-scaffold.md: this plan

Repo is now ready for first source ingest.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Expected output (last line shows commit hash):
```
[main <hash>] Scaffold wiki: raw/ + wiki/ skeletons, index, log, gitignore
 15 files changed, <N> insertions(+)
 ...
```

- [ ] **Step 5: Verify the commit landed and the tree is clean**

Run:
```bash
git -C /Users/witoldtenhove/Projects/karpathy-wiki log --oneline && echo "---" && git -C /Users/witoldtenhove/Projects/karpathy-wiki status
```

Expected output:
```
<new-hash> Scaffold wiki: raw/ + wiki/ skeletons, index, log, gitignore
2272749 Initial commit: LLM wiki design and runtime contract
---
On branch main
nothing to commit, working tree clean
```

If `working tree clean` is missing, something didn't get staged — investigate before declaring done.

---

## Self-review

**Spec coverage:** the spec's §16 (Rollout / build order) lists three artifacts: (a) `raw/` and `wiki/` skeletons with `.gitkeep`, (b) empty `wiki/index.md` and `wiki/log.md` with canonical headings, (c) initial git scaffold commit. All three are covered:
- (a) → Tasks 2 and 3
- (b) → Tasks 4 and 5
- (c) → Task 6

The spec's other sections (page schemas §5, ingest workflow §7, query workflow §8, lint §13, health invariants §14) describe runtime behavior, not scaffold artifacts — correctly out of scope for this plan. They become relevant on the first ingest.

**Placeholder scan:** no `TBD` / `TODO` / vague placeholders. All file contents shown verbatim. All commands shown with expected output.

**Type/name consistency:** the five wiki page types — `sources`, `entities`, `concepts`, `syntheses`, `threads` — are spelled identically in (a) the directory list in §16 of the spec, (b) the `find` listing in Task 6 Step 1, (c) the staged-files listing in Task 6 Step 3, (d) the `index.md` section headings in Task 4, and (e) the `git add` command in Task 6 Step 2. The six raw subdirs (`articles`, `papers`, `lectures`, `books`, `images`, `assets`) are likewise consistent across all tasks.

**Ordering:** `.gitignore` (Task 1) precedes any `git add`. Verification steps follow each creation step. Final commit is gated on tree-correctness check.
