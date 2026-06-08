# AI-Wiki

A persistent, LLM-maintained knowledge base on AI, software engineering, and organisational strategy — built as a [digital garden](https://maggieappleton.com/garden-history) and published with [Quartz v4](https://quartz.jzhao.xyz/).

Browse the site: **[businessdatasolutions.github.io/ai-wiki](https://businessdatasolutions.github.io/ai-wiki)**

> *Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.*
> — Andrej Karpathy, [LLM Wiki](llm-wiki.md)

---

## Why

Most people's experience with LLMs and documents looks like RAG: upload some files, the model retrieves chunks at query time, and synthesises an answer. It works, but the LLM is **rediscovering knowledge from scratch on every question**. Nothing accumulates. Ask the same subtle cross-source question twice and you get two independently-derived answers, with no compounding investment.

This repository is a different pattern, originally articulated by Andrej Karpathy in [`llm-wiki.md`](llm-wiki.md). Instead of retrieving from raw documents at query time, an LLM **incrementally builds and maintains a structured, interlinked markdown wiki** that sits between you and the raw sources. Every new source is read, summarised, cross-referenced, and woven into the existing graph — updating concept pages, entity cards, and syntheses, flagging contradictions, retiring superseded claims.

**The wiki is a persistent, compounding artifact.** The cross-references are already drawn. The contradictions are already flagged. The synthesis already reflects everything that has been read. Each new source makes the wiki incrementally richer, rather than just adding another item to a search index.

The pattern recovers something close to Vannevar Bush's 1945 [Memex](https://en.wikipedia.org/wiki/Memex): a personal, curated knowledge store where the associative trails between documents matter as much as the documents themselves. The part Bush couldn't solve was *who maintains the trails*. LLMs handle that — they don't get bored, don't forget to update a cross-reference, and can touch 15 files in one ingest without complaint. **Maintenance, not reading, is the bottleneck for personal knowledge bases. This pattern collapses the maintenance cost.**

This particular instance focuses on:

- **AI strategy and adoption** — how organisations are deploying generative AI and agents, what works, what fails.
- **Software engineering with agents** — Karpathy, Ng, Anthropic, AWS, and others on the changing shape of developer work.
- **Dynamic capabilities and digital transformation** — the wiki uses the [Warner & Wäger (2019) process model](https://businessdatasolutions.github.io/ai-wiki/concepts/warner-wager-process-model) as a meta-tagging layer on top of the corpus.

---

## How

### Three layers

```
┌─────────────────────────────────────────────────┐
│  raw/        Immutable source material          │  ← user curates
│              (articles, papers, transcripts)    │
├─────────────────────────────────────────────────┤
│  wiki/       LLM-generated markdown             │  ← LLM owns
│              (sources, entities, concepts,      │
│               threads, syntheses, index, log)   │
├─────────────────────────────────────────────────┤
│  CLAUDE.md   The schema / contract              │  ← co-evolved
│              (page types, ops, discipline)      │
└─────────────────────────────────────────────────┘
```

- **`raw/`** is the source of truth. Articles, papers, transcripts, slide decks. **Immutable** — the LLM reads but never modifies. Typed subfolders (`articles/`, `books/`, `papers/`, `podcasts/`, `videos/`, …) because different formats have different ingest rules.
- **`wiki/`** is the structured knowledge layer. Every page carries YAML frontmatter (`type`, `kind`, `confidence`, `last_confirmed`, `source_count`, `accessed_at`, optional `quality_score`, optional typed `relationships`). Wikilinks (`[[…]]`) are the navigation primitive. The LLM owns this layer entirely — humans browse it but rarely edit it directly.
- **[`CLAUDE.md`](CLAUDE.md)** is the schema. It's the contract that turns a generic LLM into a *disciplined wiki maintainer*: it specifies the page types, the four operations, the lifecycle metadata, the supersession protocol, the typed-relationship vocabulary, and the lint rules. It co-evolves with the wiki — when a workflow proves out, the schema absorbs the lesson.

### Four operations

| Op | What happens |
| --- | --- |
| **Ingest** | A new source enters via [`raw/`](raw/) (the *Acquire* phase) and is then turned into a `wiki/sources/<date>-<slug>.md` page that updates every affected concept and entity — typically 10–15 files in one pass (the *Process* phase). |
| **Query** | Ask a question against the wiki. The model reads [`wiki/index.md`](wiki/index.md) or runs `/wq …` (hybrid search via [qmd](https://github.com/tobi/qmd)) to locate pages, drills in, and answers with citations. Good answers can be filed back as new pages — explorations compound. |
| **Lint** | Health check. Detect contradictions, stale claims, orphan pages, missing cross-references, dangling authors, decay candidates. Reports only — never edits. |
| **Synthesize** | Close an open thread (`wiki/threads/`) by collapsing its candidate sources into a durable `wiki/syntheses/` page with Findings / Sources consulted / Lessons / Open questions. |

### Division of labour

> *The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.*

- **You curate** sources, ask questions, set direction, sanity-check the output.
- **The LLM writes** every wiki page, maintains cross-references, applies the supersession protocol, recomputes confidence, runs neighbour-source scans, drafts syntheses, and keeps [`wiki/log.md`](wiki/log.md) and [`wiki/index.md`](wiki/index.md) current.

The author of any wiki page (concept, entity, synthesis) is Claude, by design.

### Lifecycle discipline

Knowledge has a half-life. The schema captures that with three frontmatter signals plus a [retention curve](CLAUDE.md#retention):

- **`confidence`** (0.0–1.0) — how strongly the page's claims are supported by sources currently in the wiki. Starts at 0.7 for a single supporting source, climbs by `+0.05` per additional source, drops by `-0.1` for any flagged contradiction (capped at 0.95).
- **`last_confirmed`** — date of the most recent ingest that reinforced the page.
- **`source_count`** — inbound source-page citations.
- **`accessed_at`** — date the page was last *read into context* (bumped on ingest or by `/wq`). Feeds the retention curve:

  `effective_confidence = stored_confidence × exp(−days_since_access / τ)`

  with τ = 90 days for concepts/syntheses, 365 days for entities, ∞ for sources. Lint surfaces decay candidates; **nothing is ever auto-deleted or auto-marked stale**. Supersession is always a human-approved decision.

- **`quality_score`** — a mechanical structure/citation-density/cross-consistency rubric (concepts and syntheses only), computed by [`scripts/quality-score.mjs`](scripts/quality-score.mjs).

### Typed knowledge graph

Beyond wikilinks, every concept/entity/source page may declare typed `relationships:` in frontmatter, drawn from a closed vocabulary (`supports`, `contradicts`, `supersedes`, `caused`, `uses`, `depends-on`, `part-of`, `instance-of`, `authored-by`, `published-by`, `employs`, `fixed`). [`scripts/graph-export.mjs`](scripts/graph-export.mjs) compiles all of these into `wiki/.graph.json` for downstream graph queries. A typed `contradicts` edge always pairs with a `via:` string naming what the disagreement turns on — relationships are nuanced or they don't exist.

Source pages additionally carry [`dynamic_capabilities:`](CLAUDE.md#dynamic-capabilities-tagging) tags from the Warner & Wäger 2019 process model, which doubles as the corpus's **thematic adjacency index** (two sources sharing a cell are the first candidates for a typed source-to-source edge).

### Hooks (light-touch automation)

Three Claude Code hooks ([`.claude/settings.json`](.claude/settings.json)) keep the bookkeeping alive without touching content:

- **`SessionStart`** prints a snapshot of catalog counts and the last 5 log entries so the model has context immediately.
- **`PostToolUse`** lints any just-edited wiki page against the lifecycle and relationship contracts. Warnings only — never blocks.
- **`Stop`** refreshes `wiki/.graph.json` when any wiki file changed.

**Non-negotiable rule**: hooks may write to `log.md`, lint reports, and gitignored derived artifacts. **Hooks may NOT edit any `wiki/**/*.md` content page.** Content edits require explicit user approval in-session. This protects the trust contract — the LLM owns the wiki layer, but the *user* owns when it changes.

---

## What

### Current corpus (as of 2026-05-26)

| Page type | Count | Purpose |
| --- | ---: | --- |
| [Sources](wiki/sources/) | **132** | One page per ingested article, paper, transcript, podcast, report. |
| [Entities](wiki/entities/) | **91** | People, organisations, products, places, projects, events, libraries, datasets, benchmarks, venues. |
| [Concepts](wiki/concepts/) | **32** | Cross-source abstractions (e.g. `automation-vs-augmentation`, `enterprise-ai-adoption`, `agent-harness`). |
| [Threads](wiki/threads/) | **5** | Open investigations awaiting more sources. |
| [Syntheses](wiki/syntheses/) | **4** | Closed threads — durable conclusions. |

Plus the catalogue files [`wiki/index.md`](wiki/index.md) (content-oriented) and [`wiki/log.md`](wiki/log.md) (chronological, reverse-order).

### Repository layout

```
ai-wiki/
├── CLAUDE.md                  The schema — the contract for how the wiki is maintained
├── llm-wiki.md                Karpathy's original pattern spec
├── llm-wiki-v2.md             v2 extensions (lifecycle, graph, hooks, search, crystallization)
├── llm-wiki-v2-plan.md        Staged release plan (v0.2 → v0.9)
│
├── raw/                       Source material (immutable)
│   ├── articles/  books/  papers/  podcasts/  videos/  reports/  …
│
├── wiki/                      LLM-generated knowledge layer (the published content)
│   ├── sources/   entities/   concepts/   threads/   syntheses/
│   ├── index.md   log.md
│
├── quartz/  quartz.config.ts  quartz.layout.ts   Static-site generator
├── extensions/                Custom Quartz plugins (see below)
├── scripts/                   Lifecycle / lint / graph / search tooling
├── inspiration/               Working notes, drafts, ideation
└── public/                    Generated site output (gitignored)
```

### Custom Quartz extensions ([`extensions/`](extensions/))

Quartz publishes the wiki to GitHub Pages. The schema-aware affordances are added by local plugins:

- `inject-type-tags.ts` — auto-adds `type/<type>` and `kind/<kind>` tags so the graph view and tag pages cluster by page type.
- `inject-aliases.ts` — appends frontmatter aliases to the indexed body so search finds pages by alternate names.
- `backlinks-with-aliases.tsx` — replaces Quartz's stock Backlinks component to also resolve via `aliases:`.
- `inject-stale-banner.ts` — renders a warning blockquote at the top of any page with `status: stale`, linking to `superseded_by`.
- `inject-confidence-badge.ts` — renders a one-line metadata strip (`Confidence 0.85 · 4 sources · last confirmed 2026-04-28`) under the H1.
- `relationships-panel.tsx` — renders typed `relationships:` as a grouped "related content" panel at the bottom of each article, with `via:` annotations.

### Tooling ([`scripts/`](scripts/))

All scripts are Node ESM (`.mjs`), invoked as `node scripts/<name>.mjs …`.

| Script | Purpose |
| --- | --- |
| [`session-start.mjs`](scripts/session-start.mjs) | Hook: prints session-context snapshot. |
| [`session-end.mjs`](scripts/session-end.mjs) | Hook: refreshes `wiki/.graph.json` per turn when wiki changed. |
| [`lint-page.mjs`](scripts/lint-page.mjs) | Hook: validates lifecycle + relationships on edited wiki pages. |
| [`lint-confidence.mjs`](scripts/lint-confidence.mjs) | Standalone: report on `confidence` / `source_count` / `last_confirmed` health. |
| [`lint-dangling-authors.mjs`](scripts/lint-dangling-authors.mjs) | Standalone: flag authors named on ≥2 sources without an entity page. |
| [`graph-export.mjs`](scripts/graph-export.mjs) | Compile typed `relationships:` into `wiki/.graph.json`. |
| [`quality-score.mjs`](scripts/quality-score.mjs) | Mechanical quality rubric for concepts + syntheses. |
| [`bump-accessed.mjs`](scripts/bump-accessed.mjs) | Bump `accessed_at:` (retention reinforcement signal). |
| [`seed-accessed-at.mjs`](scripts/seed-accessed-at.mjs) | One-shot migration: seed `accessed_at` to `last_confirmed` on legacy pages. |
| [`wiki-query.mjs`](scripts/wiki-query.mjs) | Hybrid search wrapper around qmd; auto-bumps `accessed_at` on returned concept/entity/synthesis pages. |

### Search

For the AI agent, hybrid search runs through [qmd](https://github.com/tobi/qmd) (BM25 + vector + LLM re-ranking, fully local via `node-llama-cpp`). The wiki is registered as the qmd collection `ai-wiki`. Use:

```bash
# Bundled wrapper that also bumps accessed_at on returned pages:
node scripts/wiki-query.mjs "your question"

# Or, inside Claude Code, the slash command:
/wq your question
```

Browsing the published site uses Quartz's built-in FlexSearch.

### Quick start (local development)

Requires **Node ≥ 22** and **npm ≥ 10.9.2**.

```bash
npm install                    # one-time, install Quartz dependencies
npm run serve                  # build + serve at http://localhost:8080 with live reload
npm run build                  # build the static site into public/
npm run check                  # TypeScript type-check (extensions/)
```

GitHub Pages deploys automatically from `main` via [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

### Reading the source documents

- **[`llm-wiki.md`](llm-wiki.md)** — the upstream conceptual spec (Karpathy). Start here if you've never seen the pattern.
- **[`llm-wiki-v2.md`](llm-wiki-v2.md)** — the v2 extension (lifecycle, knowledge graph, hooks, hybrid search, crystallization).
- **[`llm-wiki-v2-plan.md`](llm-wiki-v2-plan.md)** — how v2 is rolled out in eight staged versions (v0.2 → v0.9).
- **[`CLAUDE.md`](CLAUDE.md)** — the operational schema. The single source of truth for *how this particular wiki is maintained*. Read this if you want to fork the repository and run your own instance.

---

## Licence

MIT — see [`package.json`](package.json). The wiki content and the `CLAUDE.md` schema are part of the repository and follow the same licence; the raw source material under `raw/` retains its original copyright and is included for personal scholarly use.
