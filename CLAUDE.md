# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not** a software project. It is a personal **LLM wiki** repository following the pattern described in `llm-wiki.md` (Andrej Karpathy's "LLM Wiki" idea). The pattern: Claude incrementally builds and maintains a persistent, interlinked markdown knowledge base from raw sources the user curates. The wiki is a compounding artifact — knowledge is compiled once and kept current, not re-derived per query.

`llm-wiki.md` is the conceptual spec. **This CLAUDE.md is the schema layer** — the disciplined, repo-specific instantiation of that spec. Claude owns the wiki layer entirely; the user owns sourcing, exploration, and direction.

## Current state

The wiki is instantiated. As of v0.2 the repo contains:

- `raw/` — source material under `articles/`, `assets/`, `books/`, `images/`, `lectures/`, `papers/`, `reports/`, `videos/`. Immutable.
- `wiki/` — `sources/`, `entities/`, `concepts/`, `threads/`, `syntheses/` plus the catalogues `index.md` and `log.md`. Wikilinks-only cross-refs.
- Page-type frontmatter: `type: source | entity | concept | thread | synthesis`; `kind:` discriminator on entities and sources.
- Log entries: `## [YYYY-MM-DD] <op> | <title>` where `<op>` ∈ `ingest | query | lint | synthesize | refactor | bulk-refactor`.
- Quartz publishing via `npm run build` / `npm run serve`; custom extensions in `extensions/`.

The implementation roadmap for v2 features lives in [`llm-wiki-v2-plan.md`](llm-wiki-v2-plan.md): six staged versions (v0.2 → v0.7). Each version lands schema before tooling, and bulk migrations are supervised batches.

## The three layers (architecture)

1. **Raw sources** — user-curated, immutable. Claude reads but never modifies. Source of truth.
2. **The wiki** — LLM-generated, LLM-owned markdown. Summaries, entity pages, concept pages, syntheses, an index, a log. Claude creates, updates, cross-references, and keeps consistent.
3. **The schema** — this file. The contract that turns Claude into a disciplined maintainer.

## The four operations

These replace "build / lint / test" for this repo. Apply them whenever the user invokes the corresponding intent. **Synthesize** is the v0.3 addition — see [§Synthesis](#synthesis) for the full operation.

### Ingest
A new source has been added to the raw collection.
0. **Verify the source's identity and completeness before reading further.** See [Verifying sources before ingest](#verifying-sources-before-ingest).
1. Read the source.
2. Discuss key takeaways with the user before writing (default to one source at a time, supervised — unless the user says batch).
3. Write a summary page in the wiki.
4. Update **every** affected entity, concept, and topic page across the wiki — a single ingest may touch 10–15 files. On every touched concept/entity page, bump `last_confirmed` to today's date and recompute `source_count` and `confidence` per [§Lifecycle](#lifecycle).
5. Update `index.md` (catalog of pages, one-line summaries, organized by category).
6. Append an entry to `log.md` using the agreed prefix format.
7. When new data contradicts an older claim, flag it explicitly in the page's `## Debates and supersession` section. If the new source supersedes an older one wholesale, set `supersedes:` on the new source page and `status: stale` + `superseded_by:` on the retired page — never delete the retired page.

### Query
The user asks a question against the wiki.
1. Read `index.md` first to locate relevant pages, then drill into them. Embedding-based RAG is unnecessary at moderate scale.
2. Synthesize an answer **with citations** (link back to wiki pages and, where relevant, raw sources).
3. Output format follows the question — markdown page, comparison table, slide deck (Marp), chart (matplotlib), canvas. Don't default to prose.
4. **File good answers back into the wiki as new pages.** Comparisons, analyses, discovered connections are valuable artifacts — they should not disappear into chat history. Update `index.md` and `log.md` accordingly.

### Lint
Periodic health check of the wiki.
- Detect contradictions between pages.
- Find stale claims superseded by newer sources.
- Flag orphan pages (no inbound links).
- Identify concepts mentioned but lacking their own page.
- Note missing cross-references and data gaps that warrant a web search or new source.
- Suggest new questions to investigate.
Report findings; let the user decide what to act on.

## Verifying sources before ingest

Filenames lie, samples masquerade as full sources, and PDFs get truncated. **Before treating any raw source as authoritative, run these pre-flight checks. Surface mismatches to the user *before* writing wiki pages — bad source data corrupts the wiki and is hard to remove cleanly later.**

### Pre-flight check (videos): rename the raw file before reading further

Video transcripts arrive in `raw/videos/` with non-descriptive filenames (e.g. `video1.md`). The first four lines of the file carry the human-readable identity:

```
title: <video title>
author: <channel or creator name>
url: <source URL>
date published: <YYYY-mon-DD or YYYY-MM-DD>
```

**Before treating the file as a source for ingest:**

1. Read only the first ~6 lines to extract `title:`, `author:`, `url:`, and `date published:`. The four-line metadata block is mandatory; if any line is missing or empty, stop and ask the user.
2. Slugify the title to a filesystem-safe form: lowercase, ASCII, words joined by `-`, drop punctuation. Example: `Rethinking Agents - Harness is All you Need` → `rethinking-agents-harness-is-all-you-need.md`.
3. Rename the raw file in place (`mv raw/videos/video1.md raw/videos/<slug>.md`; use `git mv` once the file is tracked). **The non-descriptive name does not survive into the repo's history-of-record beyond this rename commit.**
4. The source URL goes onto the wiki source page as a top-level frontmatter field: `url: "<youtube-or-other url>"`.
5. The wiki source page filename uses `date published` as its date prefix: `wiki/sources/<YYYY-MM-DD>-<slug>.md`. Normalise month-name forms (`2026-may-04`) to ISO (`2026-05-04`) for the filename and the `date_published:` frontmatter.
6. The raw `author:` line is the canonical attribution. For YouTube videos this is typically the **channel name**; presenter name, when known, can be added later as a body sentence ("Presented by ..."). Use the raw `author:` value verbatim in the source page's `author:` array.
7. Then proceed with Checks 1–3 below (Scope / Identity / Honest scoping) adapted as: *scope* = full transcript? *identity* = does the title at top match what the transcript actually delivers? *honest scoping* = state runtime in mm:ss.

Source-page conventions specific to videos:

- `kind: video`
- `length: "~MM:SS minutes (transcript ~N lines)"` — duration first, line count parenthetical.
- `raw: "../../raw/videos/<slug>.md"` — points to the renamed file.
- `url:` is mandatory (videos are first-class web sources; the file we hold is just a transcript snapshot).
- `date_published:` taken from the raw file's `date published:` line (ISO-normalised).
- `author:` taken verbatim from the raw file's `author:` line (single-element array; channel name).
- **No separate `channel:` field** — the convention is `author = channel` for videos. If a presenter ≠ channel ever needs separate tracking, do that as a body sentence, not a new frontmatter field.

### Check 1 — Scope: is this the whole source?

- Note the **PDF's actual page count** (the Read tool reports it; for very large PDFs the "too many pages" error message gives the count).
- For books and long reports, read the table of contents and note the **highest chapter/section page reference**.
- If the highest TOC page-reference is significantly larger than the actual PDF page count, **the file is a sample, preview, or excerpt — not the full source.** Stop and ask the user before writing wiki pages.
- **Suspect filename patterns** that warrant extra scrutiny:
  - `L-NNNNNNNN-pdf*.pdf` — OverDrive/library checkout previews.
  - `*-sample.pdf`, `*-preview.pdf`, `*-excerpt.pdf`, `*-chapter-N.pdf` — explicit excerpt names.
  - Any "book" file under ~50 pages whose TOC references chapters past page 50.
  - Generic content-management filenames with no author/title (e.g. `download.pdf`, `(1).pdf`).

### Check 2 — Identity: does the filename match the content?

- Read the cover/title page and identify the source from the **content**: authors, title, edition, year, publisher.
- If the filename doesn't match (precedent: `Mitchell and Dino - 2011 ...pdf` actually contained Dell'Acqua et al. 2026), flag the mismatch to the user.
- Convention when the mismatch is real but the user wants to keep the on-disk filename: the source page's slug is named for the actual content; the `raw:` frontmatter preserves the literal filename; note the mismatch in the source page and in the log.

### Check 3 — Honest scoping in the source page

- The `length:` frontmatter field should state **what was actually read**, not the source's nominal full length.
  - Full ingest: `"~12 pages"` (whole article).
  - Partial / front-matter ingest: `"~317 pages (read pp. 1–15: front matter, intro, framework — body chapters deferred)"`.
- The TL;DR and an explicit "What was actually ingested" section should make deferred scope visible.
- Precedents that handle this correctly: [`2026-04-28-ftsg-convergence-outlook-2026`](wiki/sources/2026-04-28-ftsg-convergence-outlook-2026.md) and [`2026-04-30-ai-index-report-2026`](wiki/sources/2026-04-30-ai-index-report-2026.md).

### What to report when a check fails

State: (a) the file as it presents itself (filename, claimed identity from cover), (b) the file as it actually is (page count, identified content, scope), (c) the discrepancy, (d) the proposed next action (ingest as partial / wait for full file / proceed under a different identity). Then ask before proceeding.

## Working principles

- **The wiki is Claude's codebase.** Touching 15 files in one ingest is normal and expected. Don't be timid about cross-cutting updates — that's the point of the pattern.
- **Cross-references are the product.** A page without links is undermaintained. Always check what should link to what when adding or updating a page.
- **Bookkeeping is the job.** Humans abandon wikis because maintenance grows faster than value. Claude's value here is precisely doing the bookkeeping — index updates, log entries, cross-reference repair, consistency sweeps — without being asked twice.
- **Sources are immutable.** Never edit files in the raw collection. Only read.
- **Verify before you trust.** Filenames lie, samples masquerade as full sources, and PDFs get truncated. Run the three pre-flight checks (scope, identity, honest scoping) before any ingest. The cleanup cost of a wiki page written on incomplete or misidentified data is much higher than the verification cost.
- **Co-evolve the schema.** When a workflow turns out to work well (or badly), update this file so future sessions inherit the lesson. The schema is meant to drift toward the user's actual workflow over time.
- **Citations beat assertions.** Wiki claims should be traceable to a source. When synthesizing across sources, say so.

## Tools and environment

- The wiki is intended to be browsed in **Obsidian** alongside the LLM session — graph view, backlinks, and Dataview (if frontmatter is used) are part of the user's reading experience. Prefer Obsidian-friendly conventions (e.g. `[[wikilinks]]`, attachment folder under `raw/assets/`) once that is confirmed with the user.
- **Obsidian Web Clipper** is the expected pipeline for getting web articles into the raw collection as markdown.
- **Marp** (markdown slide decks) and **matplotlib** charts are first-class output formats for query answers, alongside markdown pages.
- The repo is plain markdown in git — version history, branches, and diffs apply normally to wiki edits.

## Frontend / GitHub Pages

The wiki is published as a static site via **[Quartz v4](https://quartz.jzhao.xyz/)**, deployed to GitHub Pages on every push to `main`.

- **Source**: `wiki/` (untouched — Quartz reads it directly via `-d wiki`).
- **Config**: `quartz.config.ts`, `quartz.layout.ts` at repo root.
- **Custom extensions** (in `extensions/`):
  - `inject-type-tags.ts` — auto-adds `type/<type>` and `kind/<kind>` tags from frontmatter so the graph view and tag pages cluster pages by type. Source files stay clean.
  - `inject-aliases.ts` — appends frontmatter `aliases` to the indexed body so FlexSearch finds pages by alias.
  - `backlinks-with-aliases.tsx` — replaces Quartz's stock Backlinks component. The stock one only matches inbound links by canonical slug; this one also matches via the page's frontmatter `aliases`, so wikilinks like `[[Erik Brynjolfsson]]` (which Quartz resolves to the alias slug) correctly produce backlinks on the aliased page.
  - `inject-stale-banner.ts` — when a page's frontmatter has `status: stale`, prepends a warning blockquote at the top of the page linking to `superseded_by`. Source files stay clean; the banner appears only on the published site.
  - `inject-confidence-badge.ts` — when a page carries v0.2 lifecycle fields (`confidence`, `source_count`, `last_confirmed`), renders a one-line italicized metadata strip immediately after the H1: `Confidence 0.85 · 4 sources · last confirmed 2026-04-28`. Skips pages without `confidence` (sources, threads, syntheses).
  - `relationships-panel.tsx` — Quartz Component rendered in `afterBody` (i.e. at the bottom of the article body, just above the footer) so typed relationships read as "related content" the reader sees after finishing the page. Reads the page's `relationships:` frontmatter, groups by relationship type, resolves each `target` slug via `allFiles` lookup, surfaces optional `via` text, hides when empty. Component (not AST injection) so it has access to the slug→file map for proper link resolution.
- **Deploy**: `.github/workflows/deploy.yml`. Pages source must be set to "GitHub Actions" in repo Settings.
- **Local preview**: `npm install` once, then `npm run serve` → `http://localhost:8080`.
- **Build only**: `npm run build` → `public/`.

Practical notes:
- Adding a `type:` or `kind:` value to a page automatically adds a graph filter chip — no extra work.
- `raw/` is excluded via `ignorePatterns` in `quartz.config.ts` (it's source-of-truth, not for publishing).
- When a `[[wikilink]]` target doesn't exist, Quartz renders it as a "broken link" — useful for spotting stub gaps during lint.
- Quartz does not render Dataview blocks. If/when Dataview is introduced for Obsidian-side features, those blocks will appear as plain code on the public site.

## Lifecycle

Knowledge has a lifecycle. A claim from a single source is weaker than one confirmed across four sources. A claim from January is weaker than one confirmed last week. New data sometimes supersedes old data. The wiki captures all three with three frontmatter fields and one supersession protocol.

### Frontmatter contract (concepts and entities)

Every concept and entity page carries:

- `confidence: 0.0–1.0` — how strongly the claim on this page is supported by sources currently in the wiki.
- `last_confirmed: YYYY-MM-DD` — the date of the most recent ingest that reinforced this page.
- `source_count: N` — count of source pages that cite or substantiate this page (matches the page's inbound source links from `wiki/sources/`).

Sources do **not** carry `confidence`. Sources are evidence, not claims. Their reliability is captured implicitly by what cites them.

### Confidence rules

Set `confidence` defensibly when creating or updating a page:

- One supporting source: default `0.7`.
- Each additional supporting source: `+0.05` (cap at `0.95`).
- Any contradicting source flagged in `## Debates and supersession`: `−0.1`.
- Source that is a peer-reviewed paper, large-N empirical study, or government statistical release: `+0.05` over the baseline (counts once, not per source).
- Sources that are vendor-sponsored, anecdotal, or a single case study without replication: do not raise confidence above `0.75` unless multiple independent sources agree.

These are heuristics, not arithmetic. When the values conflict with intuition, write a defensible value and explain in `## Debates and supersession` if needed. Never write `0.0` as a default — that signals "not yet evaluated," which we don't allow on a live page.

### Supersession protocol

When new data fully replaces an older claim (not just adds nuance):

1. The retired page keeps its content. Do not delete or empty it.
2. The retired page gains `status: stale` and `superseded_by: [[new-page]]` in frontmatter.
3. The replacing page (a new source, or a rewritten concept/entity) gains `supersedes: [[retired-page]]` in frontmatter (use list syntax for multiple).
4. The `inject-stale-banner.ts` Quartz extension renders a warning blockquote at the top of stale pages on the published site. In Obsidian the frontmatter is visible; the banner is not.
5. Append a `log.md` entry under `op: refactor` describing what was superseded and why.

When new data only adds nuance or contradiction without retiring the old claim, do **not** mark the old page stale. Add a bullet to its `## Debates and supersession` section instead.

### Debates and supersession section

Concept pages with more than one source must include a `## Debates and supersession` section near the bottom. It records:

- Open contradictions between sources (which source says X, which says ¬X, what the resolution looks like).
- Supersession events (which page was retired, when, why).
- Open questions that the next ingest might answer.

Empty placeholder text is acceptable on early pages; the section's presence is more important than its content.

### Tier vocabulary

The pipeline `raw/` → `wiki/sources/` → `wiki/concepts/` and `wiki/entities/` → `CLAUDE.md` corresponds to four implicit memory tiers from `llm-wiki-v2.md`: working (raw observations), episodic (per-source summaries), semantic (cross-session facts), procedural (workflow patterns encoded in this schema). The wiki does not maintain separate storage for each tier — directories already serve that purpose. Promotion happens when a recurring observation across multiple sources stabilizes into a concept page, or when a recurring lint pattern becomes a CLAUDE.md rule.

### Author-entity promotion

When ingesting a source, every named author goes into the source page's `author:` frontmatter array. Whether to also create an entity page for each author follows a **second-source promotion rule**:

- **First source**: list the author in `author:`. In the source page's "Linked entities and concepts" section, list any not-yet-promoted authors under "**Dangling** (single-source mention, deferred): ...". Do **not** create an entity page yet.
- **Second source citing the same author**: create an entity page on that ingest, and update the first source's "Dangling" line accordingly. Treat this as a normal cross-cutting touch (per [§Working principles](#working-principles)).
- **Aliases**: if the same person's surface form varies across sources (e.g. `Erik Brynjolfsson` / `Brynjolfsson`, or filesystem-canonical diacritic strips like `Jesper B. Sorensen.md` for `Jesper B. Sørensen`), record every form in the entity page's `aliases:` so the audit treats them as equivalent.

The convention exists to reduce sparse single-mention entity pages while ensuring **recurring** authors get tracked. It is enforceable — the silent-skip failure mode (an author named on multiple sources but never given a page because each ingest deferred independently) is auditable via [`scripts/lint-dangling-authors.mjs`](scripts/lint-dangling-authors.mjs):

```bash
node scripts/lint-dangling-authors.mjs
```

The script walks `wiki/sources/` and `wiki/entities/`, reports any name in `author:` on ≥2 source pages without a matching entity (canonical filename or alias), and exits non-zero when dangling authors are found. Run after every ingest that adds source pages, or periodically as a corpus health check. The convention only governs **`author:` frontmatter**; people referenced incidentally in source bodies are out of scope.

## Graph

The wiki is a graph, not a list of pages. Wikilinks in body text already encode relationships, but they're untyped — `[[Erik Brynjolfsson]]` doesn't say *whether* the page mentions Erik because he authored a paper, employs someone, or is being contradicted. v0.3 adds a typed layer in frontmatter so the wiki can be queried as a graph (e.g., "what does this concept contradict?", "what did Brynjolfsson author?").

### Relationships frontmatter

Every concept and entity page may carry a `relationships:` block in its frontmatter:

```yaml
relationships:
  - type: contradicts
    target: ai-employment-effects
    via: "occupation-level vs task-level"
    confidence: 0.7
  - type: authored-by
    target: Erik-Brynjolfsson
```

- **`target`** is the destination page's slug (filename without extension), not a `[[wikilink]]`. Wikilinks-in-frontmatter are not crawled reliably by Quartz; you'd get partial/silent broken links.
- **`type`** must come from the closed vocabulary below.
- **`via`** (optional) is a one-line string explaining the nuance — what the relationship turns on. Particularly valuable on `contradicts`/`supports`.
- **`confidence`** (optional, 0.0–1.0) overrides the default for this edge. If absent, the edge inherits the page's confidence (see [§Lifecycle](#lifecycle)).

### Closed vocabulary

| Type | Direction | Use |
| ---- | --------- | --- |
| `supports` | A supports B | A's claim reinforces B's claim (intra-concept agreement) |
| `contradicts` | A contradicts B | A's claim conflicts with B's; pair with `via` |
| `caused` | A caused B | Causal claim — a phenomenon, decision, or event led to another |
| `fixed` | A fixed B | A resolves or repairs B (rare in knowledge work; common in code wikis) |
| `supersedes` | A supersedes B | A retires B; pair with v0.2 supersession protocol |
| `uses` | A uses B | A makes use of B (e.g., a method uses a tool) |
| `depends-on` | A depends on B | A would not work without B |
| `part-of` | A is part of B | A is a component of B (e.g., person `part-of` lab) |
| `instance-of` | A is an instance of B | A is a specific case of the broader B |
| `authored-by` | A is authored by B | A's content originates with B (person or org) |
| `published-by` | A is published by B | A appeared via B (publisher, journal, venue) |
| `employs` | A employs B | A (organization) employs B (person) |

Use the type that fits. Inverse relationships are not stored explicitly — `scripts/graph-export.mjs` computes them by walking the corpus.

### Body-wikilink rule (load-bearing)

**Every typed relationship in frontmatter must also appear as a body `[[wikilink]]` with at least one sentence of context.**

Frontmatter is the *typed* layer; body is the *navigable* layer; both are required. If a relationship exists only in frontmatter, Quartz's link crawler cannot follow it — you get a relationships panel pointing at links that don't show up in the graph view. If a wikilink exists only in body, the relationship is untyped and the graph export misses it. Lint enforces both directions from v0.4.

A page's `## Related concepts` / `## Related pages` / in-prose mentions usually already satisfy the body side; the migration just adds the frontmatter twin.

### Graph export

`scripts/graph-export.mjs` walks all `wiki/**/*.md`, reads frontmatter, and emits `wiki/.graph.json` (gitignored) with a node list (slug, type, kind, confidence) and an edge list (type, source, target, confidence, via). Re-run after any migration that changes relationships. v0.5 hybrid search uses this file as its third stream.

### Formalized `kind:` enum (entities)

`kind:` on entity pages is now restricted to one of: `person | organization | product | project | place | event | library | dataset | benchmark | venue`. Drift from earlier ingests (e.g. `org` for organization) gets normalized during the v0.3 migration.

## Synthesis

A `wiki/threads/` page is provisional — it gathers questions, candidate sources, and a "How this thread should resolve" plan. When enough sources are in to answer the question, the thread is **synthesized** into a `wiki/syntheses/` page. Threads stay open as long as the wiki is still gathering evidence; syntheses are the durable conclusions.

### Synthesis page contract

A synthesis page (filename usually matches the originating thread's slug) carries `type: synthesis` and the v0.2 lifecycle fields, plus:

```yaml
type: synthesis
derived_from: [thread-slug]   # list; one or more threads this closes
opened: YYYY-MM-DD            # date the originating thread opened
closed: YYYY-MM-DD            # date this synthesis was filed
```

Required body sections, in order:

1. **Question** — what was the thread asking, restated as a single sentence.
2. **Findings** — what the synthesis concludes. The substantive part.
3. **Sources consulted** — bulleted list of every source page that informed the synthesis. Each as a `[[wikilink]]`. This is the citation panel.
4. **Lessons** — short, transferable claims extracted from the synthesis. Each lesson is a single sentence; v0.6 will promote individual lessons to standalone `wiki/lessons/` pages.
5. **Open questions** — what the synthesis did *not* answer; carried forward to a new thread or future ingest.

### `synthesize` operation

When a thread is ready to close:

1. Read the thread page and every source it lists.
2. Draft the synthesis page in `wiki/syntheses/` per the contract above.
3. Update the thread page: `status: closed` in frontmatter; add a "Closed" note pointing to the synthesis.
4. Update `index.md`: drop the thread from the open-threads list; add the synthesis to the (no-longer-empty) Syntheses section.
5. Append a `log.md` entry under `op: synthesize` describing the question and the headline finding.

## Hooks

v0.4 wires Claude Code hooks (configured in [`.claude/settings.json`](.claude/settings.json)) so the bookkeeping that v0.2 and v0.3 added doesn't have to be triggered manually. The harness fires the hooks; the scripts under [`scripts/`](scripts/) are the implementations.

### Non-negotiable rule

**Hooks may write to `wiki/log.md`, to lint reports (stderr/stdout), and to gitignored derived artifacts (`wiki/.graph.json`). Hooks may NOT edit any `wiki/**/*.md` content page** — not concept, not entity, not source, not synthesis, not thread, and not `index.md`. Content edits always require explicit user approval in-session.

This protects the v1 trust contract ("Claude owns the wiki layer, user owns direction") from automation drift. A hook that silently rewrites a concept page when the user wasn't looking is a worse failure than a hook that doesn't fire.

### Hooks in use

| Event | Script | Purpose |
| ----- | ------ | ------- |
| `SessionStart` | [`scripts/session-start.mjs`](scripts/session-start.mjs) | Outputs a short wiki snapshot (catalog counts, last 5 log entries, `status: stale` and `confidence < 0.5` flags) to stdout — Claude Code feeds it back as session context. Read-only. |
| `PostToolUse` (Edit, Write) | [`scripts/lint-page.mjs`](scripts/lint-page.mjs) | If the just-edited file is under `wiki/**/*.md`, validates the v0.2 lifecycle contract (`confidence`, `last_confirmed`, `source_count`), the v0.3 closed relationship vocabulary, and the v0.3 body-wikilink rule (every `relationships.target` must appear as a body `[[wikilink]]`). Warnings to stderr. Always exits 0 — never blocks the tool call. |
| `Stop` | [`scripts/session-end.mjs`](scripts/session-end.mjs) | Per-turn check: if any `wiki/**/*.md` is modified or untracked, re-runs [`scripts/graph-export.mjs`](scripts/graph-export.mjs) so `wiki/.graph.json` stays fresh; otherwise exits silently. No log writes. |

### Auto-prefix log convention

When/if a hook ever does write to `log.md` in a future version, the entry's op must be prefixed `auto-` (e.g. `auto-lint`, `auto-supersession-check`) to distinguish hook-fired writes from human-curated entries. Currently no hook writes log entries; this convention is reserved.

### Cuts vs. v2 plan

- **No on-query hook** — the "file good answers back" decision is human-judgment, not a hook target.
- **No scheduled retention decay** — deferred to v0.5 alongside hybrid search.
- **`session-end.mjs` does not append a log entry** — `Stop` fires per-turn, not per-session, so per-turn entries would be too noisy. Manual log writing remains the convention until a real `SessionEnd` event is wired (or a session-end slash command is built).
- **No auto-fix on lint warnings** — `lint-page.mjs` only reports; the human or Claude decides what to do.

## Reference

`llm-wiki.md` — the upstream conceptual spec.
`llm-wiki-v2.md` — the v2 extension (lifecycle, knowledge graph, hooks, hybrid search, crystallization).
`llm-wiki-v2-plan.md` — the staged release plan that turns v2 into versioned releases for this repo.

Re-read whichever spec applies whenever a workflow question comes up that this file doesn't answer, then consider promoting the resolution into this file.
