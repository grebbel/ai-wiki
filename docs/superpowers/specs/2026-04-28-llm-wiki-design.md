# LLM Wiki — Technical Design

**Date:** 2026-04-28
**Status:** Approved (initial design)
**Upstream:** [`llm-wiki.md`](../../../llm-wiki.md) (Karpathy's pattern)
**Runtime contract:** [`CLAUDE.md`](../../../CLAUDE.md)

This document captures the concrete instantiation of the LLM-wiki pattern for this repository. It is the frozen record of the design decisions made on 2026-04-28. `CLAUDE.md` is the day-to-day runtime contract; this doc explains *why* `CLAUDE.md` says what it says.

---

## 1. Goals

Build a personal, outward-facing, wide-open knowledge base where Claude maintains a hybrid wiki — both per-source summary pages and per-entity/concept pages as fully fleshed peers — fed primarily by web articles and academic papers, with secondary support for YouTube lectures, books, and standalone images.

The wiki must:

- Compound over time. Adding a source enriches existing pages, not just appends a new one.
- Stay navigable as it grows from tens to hundreds of sources, without forcing a topical hierarchy that will rot.
- Survive without bespoke infrastructure. Plain markdown + Obsidian + git is the floor; tooling (search, PDF extraction) is added only when the index alone stops scaling.
- Make Claude's bookkeeping work load-bearing. A single ingest is expected to touch ~10–15 files; the design leans into this rather than minimizing it.

## 2. Non-goals

- No embedding-based RAG infrastructure at the start. The index file is the retrieval mechanism. (Re-evaluate at ~hundreds of sources.)
- No team/collaboration features. Single-user, single-machine.
- No automated ingest from feeds. Sources are deliberately curated; Web Clipper / manual download is the only intake.
- No web UI. Obsidian is the read interface.
- No domain-specific schemas (e.g. medical, legal). The wiki is general-purpose.

## 3. Architecture

Three layers, exactly as in the upstream pattern:

| Layer | Owner | Mutability |
|---|---|---|
| **Raw sources** (`raw/`) | User curates | Immutable — Claude reads, never writes |
| **Wiki** (`wiki/`) | Claude owns entirely | Claude creates, updates, refactors |
| **Schema** (`CLAUDE.md` + this doc) | User + Claude co-evolve | Updated when workflows stabilize or shift |

The architectural choice that distinguishes this design from a flat note collection: **the wiki layer is partitioned by page *type*, not by topic.** Topical clustering happens via frontmatter tags + the index. See §6 for the rationale.

## 4. Directory layout

```
karpathy-wiki/
├── raw/                  # IMMUTABLE — user-curated sources
│   ├── articles/         # Web clips (Obsidian Web Clipper → .md)
│   ├── papers/           # Academic PDFs + extracted .md alongside (e.g. attention.pdf + attention.md)
│   ├── reports/          # Industry reports, gov't white papers, consultancy decks, sell-side research (PDF + extracted .md)
│   ├── lectures/         # YouTube transcripts
│   ├── books/            # Per-chapter notes you write yourself; one folder per book
│   ├── images/           # Standalone images that are themselves a source
│   └── assets/           # Inline images downloaded from articles (referenced by source pages, not standalone sources)
├── wiki/                 # CLAUDE-OWNED
│   ├── sources/          # One summary page per source — rich, not stub
│   ├── entities/         # People, orgs, products, places, events
│   ├── concepts/         # Ideas, frameworks, terms, methods
│   ├── syntheses/        # Cross-cutting essays, comparisons, query answers worth keeping
│   ├── threads/          # Open questions you're tracking — resolve into syntheses
│   ├── index.md          # Catalog, partitioned by page-type
│   └── log.md            # Append-only chronological record
├── docs/
│   └── superpowers/specs/  # This file and future design docs
├── CLAUDE.md             # Runtime contract for Claude
└── llm-wiki.md           # Upstream conceptual pattern
```

### Why type-partitioned and not topic-partitioned

For a wide-open KB, topic folders (`wiki/ml/`, `wiki/economics/`) are a trap:

- Cross-domain pages have to pick a folder arbitrarily.
- The folder set has to be invented up front, before the user's actual interests emerge.
- Folders rot. Five years in, half are stale and half don't fit anything new.

Type folders are stable: a page's *type* doesn't change, but its *topic* might (an "AI safety" page can drift toward "AI governance" with no file move). Topical navigation is delegated to tags + index — both first-class Obsidian/Dataview features.

## 5. Page schemas

All pages are Obsidian-flavored markdown with YAML frontmatter. Frontmatter is non-optional — Dataview depends on it.

### 5.1 Source page

Path: `wiki/sources/YYYY-MM-DD-<slug>.md` (date = ingestion date, for chronological ordering on disk).

```yaml
---
type: source
kind: article | paper | report | lecture | book | image
title: "Attention Is All You Need"
author: ["Ashish Vaswani", "Noam Shazeer", "..."]
url: "https://arxiv.org/abs/1706.03762"
raw: "../../raw/papers/attention-is-all-you-need.pdf"
date_published: 2017-06-12
date_ingested: 2026-04-28
tags: [transformer, attention, deep-learning]
---
```

Body:

1. **TL;DR** — 3 lines max.
2. **Key claims** — bullet list, each claim is a candidate citation for an entity/concept page.
3. **Notable quotes** — for articles/papers; timestamps for lectures.
4. **My take** — your reactions, criticisms, things to follow up.
5. **Linked entities and concepts** — a curated wikilink list (also auto-linked inline in body).
6. **Source** — backlink to `raw/`.

### 5.2 Entity page

Path: `wiki/entities/<Canonical Name>.md`. Title-case; aliases live in frontmatter.

```yaml
---
type: entity
kind: person | org | project | product | place | event
aliases: ["AV", "Vaswani"]
tags: [ml-researcher, google-brain]
---
```

Body:

1. **Definition** — one paragraph.
2. **Structured sections** — grow over time. For a person: roles, key works, affiliations. For an org: focus areas, notable products. Sections are added as needed; not enforced up front.
3. **Mentioned in** — a Dataview block listing all source pages that link here.
4. **Contradictions / open questions** — explicit, not buried in prose.

### 5.3 Concept page

Path: `wiki/concepts/<term>.md`. Lowercase-kebab title; aliases in frontmatter.

```yaml
---
type: concept
aliases: ["self-attention", "scaled dot-product attention"]
tags: [transformer, deep-learning]
---
```

Body:

1. **Working definition** — your best current synthesis.
2. **Key claims** — each followed by a wikilink citation to the source page.
3. **Debates / contradictions** — where sources disagree.
4. **Related concepts** — wikilinks.
5. **Mentioned in** — Dataview block.

### 5.4 Synthesis page

Path: `wiki/syntheses/<slug>.md`.

```yaml
---
type: synthesis
status: draft | stable
last_revised: 2026-04-28
tags: [transformer, history-of-ml]
---
```

Body: free-form essay or comparison table. Always cites entity/concept/source pages. Born either from a query whose answer is worth keeping, or from a thread that resolved.

### 5.5 Thread page

Path: `wiki/threads/<slug>.md`.

```yaml
---
type: thread
status: open | resolved | dormant
opened: 2026-04-28
tags: [open-question]
---
```

Body:

1. **The question** — sharp, one paragraph.
2. **What we know so far** — citations to existing wiki pages.
3. **What's missing** — gaps that warrant new sources.
4. **Candidate sources to find** — concrete leads.

When `status: resolved`, write a synthesis page and link to it; keep the thread file as a record of the inquiry.

## 6. Linking conventions

- **Internal links: Obsidian wikilinks `[[Page Title]]`.** Enables backlinks, graph view, Dataview. Display text: `[[Page|alt text]]`.
- **Citations on entity/concept pages:** each claim followed by `([[2026-04-15-attention-is-all-you-need|Vaswani et al.]])` — wikilink whose display text is a short attribution.
- **Pointers to raw/:** standard relative markdown links from a source page back to the raw file: `[(pdf)](../../raw/papers/attention.pdf)`. This is *not* a wikilink because raw files aren't part of the Obsidian graph.
- **Tags:** YAML array in frontmatter. Inline `#tags` in body are allowed but frontmatter is canonical (Dataview-queryable).

## 7. Ingest workflow

Default mode: **one source at a time, supervised.** Batch mode is a deliberate override, not the default.

1. **Read** the raw source.
2. **Discuss** key takeaways with the user — what's worth emphasizing, what to skip.
3. **Source page** — create `wiki/sources/YYYY-MM-DD-<slug>.md` with full schema (§5.1).
4. **Identify entities and concepts** mentioned. For each:
   - Existing page → update with what this source adds (new claims, contradictions, links).
   - Missing page → create stub: definition + this source as first citation.
5. **Contradiction check** — does this source disagree with existing claims? If yes, add an entry under "Contradictions" on the affected page; do *not* silently overwrite the older claim.
6. **Index update** — `wiki/index.md` gets one new line per new page, and any one-line summaries that need refreshing.
7. **Log entry** — append to `wiki/log.md` (§9).

Expected file touch count: ~10–15 files for a moderately rich source. This is the design working as intended, not a smell.

## 8. Query workflow

1. Read `wiki/index.md` first to identify candidate pages.
2. Drill into the relevant entity/concept/synthesis pages.
3. Synthesize an answer with citations:
   - Wiki claims cite the wiki page that holds them.
   - Wiki pages in turn cite source pages.
   - Source pages cite raw/ for primary verification.
4. **Output format follows the question** — markdown, table, Marp slides, matplotlib chart, Obsidian canvas. Prose is not the default; it's one option among several.
5. **If the answer has lasting value, file it as a synthesis page** and append a `query` entry to the log. This is how exploration compounds rather than evaporating into chat history.

## 9. Index and log formats

### 9.1 `wiki/index.md`

Partitioned by page type, in this fixed order:

```markdown
# Index

## Sources
- [[2026-04-28-attention-is-all-you-need]] — Vaswani et al. introduce the Transformer.

## Entities
- [[Vaswani, Ashish]] — ML researcher; Transformer co-author.

## Concepts
- [[self-attention]] — Mechanism for sequence modeling without recurrence.

## Syntheses
- [[history-of-attention-mechanisms]] — How attention evolved 2014–2017.

## Threads
- [[open: scaling laws vs architecture]] — When do architectural improvements beat scale?
```

Each section is flat-listed alphabetically with a one-line summary. Sections may be supplemented with a Dataview block that auto-includes pages by frontmatter `type:` — this is encouraged once page counts grow.

### 9.2 `wiki/log.md`

Append-only. Strict prefix so `grep "^## \[" wiki/log.md | tail -10` works as a CLI:

```markdown
## [2026-04-28] ingest | Attention Is All You Need
- Source page created. New concept: [[self-attention]]. Updated: [[Transformer]], [[Vaswani, Ashish]].
- Contradiction noted on [[Recurrent Neural Networks]] re: long-range dependencies.
```

Permitted operations: `ingest`, `query`, `lint`, `synthesize`, `refactor`.

**Gotcha — docstring at the top of `log.md`.** If `log.md` itself documents the format with a fenced code block like ```` ``` `` ## [YYYY-MM-DD]…`` `` ```` , `grep "^## \["` will match the example line as a phantom entry, polluting every query. Always use a 4-space-indented code block (or inline backticks) for the format example inside `log.md` itself — fenced code blocks are fine in this spec because nobody greps the spec for log entries.

## 10. Source-format pipelines

| Source kind | Intake | Storage | Notes |
|---|---|---|---|
| **A. Web articles** (dominant) | Obsidian Web Clipper → `.md` | `raw/articles/` | Inline images downloaded to `raw/assets/` via Web Clipper hotkey. |
| **B. Papers** (dominant) | PDF download | `raw/papers/<slug>.pdf` + `<slug>.md` | Extraction tool: `marker` recommended (preserves equations); LLM-driven fallback for shorter papers. |
| **B′. Reports** | PDF download (sometimes web-clipped) | `raw/reports/<slug>.pdf` + `<slug>.md` | Industry / consultancy / government / sell-side. Same PDF-extraction pipeline as papers. Distinguish via tags (`consultancy`, `government`, `equity-research`, `ngo`). Executive summary often worth quoting verbatim on the source page. |
| **C. Lectures** | YouTube transcript | `raw/lectures/<video-id>.md` | Use `yt-dlp --write-auto-sub` or equivalent; preserve timestamps. |
| **E. Books** | User-written notes | `raw/books/<book-slug>/<NN-chapter>.md` | One folder per book; one file per chapter. Chapter ingest is its own log entry. |
| **I. Images** | Manual save | `raw/images/<slug>.<ext>` | A source page (`kind: image`) describes context, source URL, what's in it. |

Other formats (podcasts, tweets, newsletters) can be added later by extending `raw/` with a new folder and adding a `kind:` value — no schema rewrite needed.

## 11. Search infrastructure

- **Phase 1 (now):** `index.md` is the search. Sufficient at the scale of tens to low hundreds of pages, given the index is updated on every ingest.
- **Phase 2 (trigger: index becomes hard to scan, or queries miss relevant pages):** add [`qmd`](https://github.com/tobi/qmd) — local BM25 + vector search + LLM rerank, with both a CLI and an MCP server. Claude can shell out to it during query.
- **Phase 3 (probably never):** custom infrastructure. Avoid unless a specific limitation forces it.

## 12. Output formats for queries

- **Markdown** — default for narrative answers, comparisons, summaries.
- **Marp** — for presentations (Obsidian has a Marp plugin).
- **matplotlib** — for charts based on extracted data (e.g. timeline of source publication dates).
- **Obsidian Canvas** — for visual / spatial layouts (mind maps, comparison boards).
- **Tables** — for structured comparisons; render in markdown.

Whichever format is chosen, if the answer is worth keeping it gets filed as a synthesis page (which can embed Marp/canvas/etc).

## 13. Lint workflow

Run on demand; reasonable cadence is weekly. Output is a report — no destructive edits without user confirmation.

Checks:

- **Orphan pages** — no inbound wikilinks. Either link them up, mark them dormant, or delete.
- **Contradictions** — claims that disagree across pages without being marked.
- **Missing concept pages** — concepts mentioned in ≥ N sources (default N=3) that lack their own page.
- **Lazy ingests** — source pages with zero entity/concept links.
- **Stale claims** — older claims contradicted by newer sources but not yet flagged.
- **Broken wikilinks** — typo'd or renamed targets.
- **Suggestions** — queries to investigate, sources to find, threads worth opening.

## 14. Health invariants (Claude must enforce on every ingest)

These are non-negotiable. If any are violated, the ingest is incomplete.

1. **Index is updated.** Every new or renamed page reflected in `wiki/index.md`.
2. **Log entry written.** Every ingest produces a log entry with the fixed prefix.
3. **No isolated source pages.** A source page must have ≥ 1 wikilink to an entity *or* concept page.
4. **Frontmatter present.** Every wiki page has a `type:` field at minimum.
5. **Contradictions explicit.** New claims that disagree with existing claims are flagged on the affected page, never silently merged or overwritten.
6. **Citations real.** Every claim on an entity/concept page links to a source page that actually contains the claim.

## 15. Tooling and environment

- **Obsidian** — read interface. Graph view, backlinks, and Dataview are part of the user experience. Wikilinks, frontmatter, and tags are all chosen to be Obsidian-native.
- **Obsidian Web Clipper** — primary intake for articles.
- **Obsidian Dataview plugin** — for "Mentioned in" blocks and dynamic index sections.
- **`marker` (or LLM extraction)** — for PDF → markdown.
- **`yt-dlp`** — for lecture transcripts.
- **git** — version history. Every ingest is a candidate commit. (Repo is currently *not* git-initialized; this is a setup gap to resolve before first ingest.)

## 16. Rollout / build order

The wiki itself is built by Claude on the user's command. The directory scaffold is the only thing built up front:

1. Create `raw/` and `wiki/` skeletons (empty subdirectories with `.gitkeep`).
2. Create empty `wiki/index.md` and `wiki/log.md` with the canonical headings.
3. Initialize git, commit the scaffold.
4. First real ingest follows the workflow in §7.

## 17. Open questions / future considerations

- **PDF extraction tool choice.** `marker` is the current recommendation but unconfirmed. First paper ingest will pick a tool and the result gets recorded in `CLAUDE.md`.
- **Search Phase 2 trigger.** "Index becomes hard to scan" is fuzzy. Concrete trigger TBD (probably: more than ~3 page types per index section make scanning slow).
- **Multi-source ingest.** Right now batch is an override; if it becomes the norm, the workflow needs explicit batching rules (e.g. defer index update until batch completes).
- **Web search during ingest.** Should Claude proactively search for additional context on a new entity? Currently no — keep ingest grounded in the source. Revisit if entity pages feel thin.
- **Page archival.** No retirement workflow for genuinely obsolete pages. Add when needed.

## 18. Decision log

Each decision below was settled during the brainstorming session on 2026-04-28. Reversal is possible — the entry exists so future-you knows which choices were deliberate and which were inherited.

| # | Decision | Rationale | Reversible? |
|---|---|---|---|
| 1 | Personal knowledge base (not Karpathy-content-specific despite repo name) | User chose option C in brainstorm | Easy |
| 2 | Outward-facing (consumed material, not journal) | User chose option A | Hard — schema would shift |
| 3 | Wide-open / general-curiosity scope | User chose option C | Hard — folder layout would shift |
| 4 | Hybrid: source + entity/concept pages as peers | User chose option D | Medium — would change ingest workload |
| 5 | Source mix: web articles + papers dominant; lectures, books, images secondary | User-stated | Easy — extend `raw/` |
| 6 | Type-partitioned wiki/ folders, not topic-partitioned | Approach 3, recommended | Medium — bulk file moves |
| 7 | Obsidian wikilinks (not standard markdown links) | Backlinks, graph view, Dataview | Hard — repo-wide rewrite |
| 8 | YAML frontmatter required on all wiki pages | Dataview, machine-readable types | Easy to add; hard to remove |
| 9 | Index-only search at start | YAGNI; Karpathy spec confirms scale | Easy — add `qmd` later |
| 10 | Supervised one-at-a-time ingest as default | Karpathy's recommendation; matches "discuss takeaways" step | Easy — add batch mode |
| 11 | Log prefix `## [YYYY-MM-DD] <op> \| <title>` | Karpathy spec; greppable | Hard — log-wide rewrite |
| 12 | Reports get their own folder + `kind: report`, not folded into `papers/` | Reports differ from peer-reviewed papers in tone, audience, and use (exec summaries quoted verbatim, citations less rigorous). Tags handle sub-type (consultancy / government / equity-research / ngo). Added 2026-04-28 in response to first real-use question. | Easy — folder rename, frontmatter sweep |
| 13 | Entity `kind:` enum extended to include `project` | The [[AI Index]] is a project/initiative within [[Stanford HAI]], not an org per se. `kind: org` would have been a forced fit. Surfaced during first real ingest. | Easy — frontmatter sweep |
| 14 | Defer wikilinks to dangling for entities not yet given pages | First-ingest principle: avoid stub-spam by linking to entities that don't yet have pages, letting Obsidian's "create from link" be the trigger when the user wants to flesh them out. Better than 30 stub pages with one sentence each. Confirmed during AI Index ingest where ~30 candidates (OpenAI, Anthropic, individual benchmarks, etc.) were deferred. | Soft policy — no migration cost |

---

## Appendix A: glossary

- **Source page** — wiki page summarizing one raw source.
- **Entity page** — wiki page about a thing (person, org, etc.).
- **Concept page** — wiki page about an idea or term.
- **Synthesis page** — wiki page that's a cross-source essay or comparison; often born from a query answer or resolved thread.
- **Thread page** — wiki page tracking an open question.
- **Ingest** — workflow for adding a new raw source and propagating its content into the wiki.
- **Lint** — wiki health check; produces a report.
- **Raw source** — the original document in `raw/`. Immutable.
