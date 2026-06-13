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
- Log entries: `## [YYYY-MM-DD] <op> | <title>` where `<op>` ∈ `ingest | acquire | query | lint | synthesize | refactor | bulk-refactor`. (`acquire` is the v0.9 addition — used only when raw files land without same-session processing; the umbrella op for the typical case remains `ingest`.)
- Quartz publishing via `npm run build` / `npm run serve`; custom extensions in `extensions/`.
- **v0.5 is fully landed (2026-05-17).** All three slices: **retention** (`accessed_at` on concepts + entities + syntheses; §Retention decay curve as lint signal), **search** ([qmd](https://github.com/tobi/qmd) / `@tobilu/qmd` registered as collection `ai-wiki`; 205 docs / 1466 chunks; BM25 + vector + query-expansion local models in `~/.cache/qmd/`), **quality** (`quality_score` + `quality_notes` on concepts and syntheses via [`scripts/quality-score.mjs`](scripts/quality-score.mjs); mechanical rubric across structure / citations / cross-consistency). Manual `accessed_at` bumps via [`scripts/bump-accessed.mjs`](scripts/bump-accessed.mjs) pending MCP integration. See [§Lifecycle](#lifecycle), [§Retention](#retention), [§Quality](#quality), [§Search](#search). LLM-as-judge quality scoring deferred to v0.6.

The implementation roadmap for v2 features lives in [`llm-wiki-v2-plan.md`](llm-wiki-v2-plan.md): eight staged versions (v0.2 → v0.9). Each version lands schema before tooling, and bulk migrations are supervised batches.

## The three layers (architecture)

1. **Raw sources** — user-curated, immutable. Claude reads but never modifies. Source of truth.
2. **The wiki** — LLM-generated, LLM-owned markdown. Summaries, entity pages, concept pages, syntheses, an index, a log. Claude creates, updates, cross-references, and keeps consistent.
3. **The schema** — this file. The contract that turns Claude into a disciplined maintainer.

## The four operations

These replace "build / lint / test" for this repo. Apply them whenever the user invokes the corresponding intent. **Synthesize** is the v0.3 addition — see [§Synthesis](#synthesis) for the full operation. **Ingest** was split into two re-runnable phases — Acquire and Process — in v0.9; the operation count stays at four (Ingest / Query / Lint / Synthesize), but Ingest now has explicit named sub-phases. See §Acquire and §Process below.

### Ingest = Acquire + Process

A new source enters the wiki in two phases. **Acquire** lands a raw file (fetch / convert / place into a typed `raw/` subfolder) and stops. **Process** reads `raw/` and writes `wiki/`. They fail differently and run on different cadences — often in the same session, but skipping either is common (e.g. landing several PDFs today, processing over the week). See §Acquire and §Process below.

### Acquire

A new raw file lands in `raw/`. Acquire **only touches `raw/`** — the wiki source page is not written until §Process runs.

1. **Determine source type → typed `raw/` subfolder.** Organise by source *type*, not topic — different formats have different processing rules. Current typed subfolders: `articles/`, `assets/`, `books/`, `images/`, `lectures/`, `papers/`, `reports/`, `videos/`. Create new typed subfolders on the fly when a genuinely new source category appears (e.g. `raw/patents/`, `raw/interviews/`); don't ask permission for every new type.
2. **Convert before landing.** Source formats that the LLM cannot read in one pass must be converted to markdown *before* landing in `raw/`:
   - PDFs → markdown (`marker`, `pdftotext`, MarkItDown, or a Zotero markdown export) → `raw/papers/<slug>.md`. Keep the original PDF in `raw/assets/` for reference.
   - YouTube / podcast URLs → transcript markdown → `raw/videos/<slug>.md`. The [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) is the canonical acquire-time skill — auto-triggered by any YouTube URL request that mentions transcript / captions / subtitles, or invoked explicitly with `-o raw/videos/<slug>.md`.
   - `.docx` / `.epub` / `.html` → markdown (`pandoc`, `readability`).
3. **Acquire-time skill contract.** A skill that lands a raw file emits the file at `raw/<type>/<slug>.md` with a canonical YAML frontmatter as its first block. The frontmatter is the *contract* between Acquire and Process — Process reads it during pre-flight checks. The video-format contract is specified in detail at [§Pre-flight check (videos): the YAML frontmatter contract](#pre-flight-check-videos-the-yaml-frontmatter-contract); new acquire-time skills (PDF→markdown, web clipper integration, podcast transcription) follow the same pattern: produce a raw file at the canonical path with the canonical frontmatter for its type.
4. **Re-runnable.** Re-acquiring the same source from a better channel (higher-quality transcript, full text replacing a sample) **replaces the raw file**. The wiki source page is not touched until §Process re-runs. This is why Acquire is named as a distinct phase — re-acquisition without re-processing is common and benign.
5. **Log entry.** When Acquire runs without Process in the same session, log as `acquire | <slug or batch description>` (reverse-chronological, top of [`log.md`](wiki/log.md)). When Acquire and Process run together (the typical case), use `ingest | ...` as the umbrella op — no separate `acquire` entry needed.

### Process
A source in `raw/` has not yet been turned into a wiki page. (When invoked under the §Ingest umbrella, Acquire produced this file moments ago; when invoked standalone, the file has been sitting in `raw/` since an earlier session.)
0. **Verify the source's identity and completeness before reading further.** See [§Verifying sources before ingest](#verifying-sources-before-ingest).
1. Read the source.
2. Discuss key takeaways with the user before writing (default to one source at a time, supervised — unless the user says batch).
3. Write a summary page in the wiki.
4. **Tag the source's `dynamic_capabilities:` frontmatter** with the Warner & Wäger microfoundation(s) / strategic-renewal outcome(s) / contextual factors it touches, per [§Dynamic-capabilities tagging](#dynamic-capabilities-tagging). Tagging is encouraged, not forced — skip when the source genuinely sits outside the W&W lens (e.g. pure LLM-internals papers).
5. **Run a neighbour-source scan.** Query `wiki/sources/` for sources that share at least one `dynamic_capabilities:` cell with the new source, **or** that already cite any of the concept pages you intend to update in step 6 (the fallback path catches pre-GH #4 sources that don't carry W&W tags yet). For each candidate, decide on a typed `relationships:` edge — typically `supports` if both sources address the same phenomenon from compatible angles, `contradicts` if findings or framings conflict (pair with `via:`), or `supersedes` if the new source replaces a prior claim wholesale (per [§Supersession protocol](#supersession-protocol)). Add the edge to the **new source's** frontmatter `relationships:` block. Reverse-linking from the neighbour is encouraged but not required — the graph export computes inverses, and the body-wikilink rule applies in both directions. Skip neighbours where no defensible edge type fits — *not every co-occurrence is a relationship*. **At ≥3 candidate neighbours, surface the list in your response so the user can spot omissions before commit.** See [§Source-to-source relationships](#source-to-source-relationships) for vocabulary guidance.
6. Update **every** affected entity, concept, and topic page across the wiki — a single ingest may touch 10–15 files. On every touched concept/entity page, bump `last_confirmed` to today's date and recompute `source_count` and `confidence` per [§Lifecycle](#lifecycle).
7. Update `index.md` (catalog of pages, one-line summaries, organized by category).
8. Prepend an entry to `log.md` using the agreed prefix format — new entries go directly under the `---` separator at the top of the file (reverse-chronological convention since 2026-05-12, GH #3), so the most recent entry is the first one in the file. Use `ingest | ...` as the umbrella op regardless of whether Acquire ran in this session or a previous one — only the standalone-Acquire case (no Process) gets the separate `acquire | ...` op (see §Acquire step 5).
9. When new data contradicts an older claim, flag it explicitly in the page's `## Debates and supersession` section. If the new source supersedes an older one wholesale, set `supersedes:` on the new source page and `status: stale` + `superseded_by:` on the retired page — never delete the retired page.

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

### Pre-flight check (videos): the YAML frontmatter contract

For new YouTube sources, invoke the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) first — it produces this format directly. The skill is auto-triggered by any YouTube URL request that mentions transcript / captions / subtitles, or can be invoked explicitly with `-o raw/videos/<slug>.md` to land at the canonical path.

Video transcripts in `raw/videos/` carry their human-readable identity in YAML frontmatter at the top of the file:

```yaml
---
title: <video title>
video_id: <youtube id>
url: <source URL>
channel: <channel name>
channel_id: <youtube channel id>
channel_url: <channel URL>
publish_date: '<ISO-8601 with timezone, e.g. 2026-05-08T11:50:11-07:00'>
upload_date: '<ISO-8601 with timezone>'
category: <youtube category>
duration: '<MM:SS>'
length_seconds: <integer>
view_count: <integer>
caption_tracks:
  - language_code: <iso>
    name: <track name>
    kind: <asr | manual>
    is_translatable: <bool>
description: |
  <youtube description text, multi-line>
notes: |
  <ingest-time provenance: ASR cleanups applied, section headings inferred, etc.>
---
```

The skill emits all of the above plus optional fields (`thumbnails:`, `keywords:`, `chapters:`, `is_live:`, `is_family_safe:`, `default_language:`, `available_countries:`); they're useful but not load-bearing for pre-flight identity.

**Canonical pre-flight fields the wiki cares about:** `title`, `url`, `channel`, `publish_date`. If any of these four is missing or empty, stop and ask the user.

**Before treating the file as a source for ingest:**

1. Read the YAML frontmatter (everything between the opening and closing `---`). Extract the four canonical fields plus `description:` and `caption_tracks[].kind` (used downstream during source-page creation, see [§Source-page conventions specific to videos](#source-page-conventions-specific-to-videos)).
2. Slugify the title to a filesystem-safe form: lowercase, ASCII, words joined by `-`, drop punctuation. Example: `Rethinking Agents - Harness is All you Need` → `rethinking-agents-harness-is-all-you-need.md`.
3. The raw file should already be at `raw/videos/<slug>.md` if the skill was invoked with `-o`; otherwise rename in place (`mv raw/videos/<file>.md raw/videos/<slug>.md`; use `git mv` once the file is tracked). **The non-descriptive name does not survive into the repo's history-of-record beyond this rename commit.**
4. The source URL goes onto the wiki source page as a top-level frontmatter field: `url: "<youtube-or-other url>"` (verbatim from the raw file).
5. The wiki source page filename uses the **date component** of `publish_date:` as its prefix: `wiki/sources/<YYYY-MM-DD>-<slug>.md`. Strip any time/timezone component (`'2026-05-08T11:50:11-07:00'` → `2026-05-08`).
6. The raw `channel:` line is the canonical attribution. Use it verbatim in the source page's `author:` array as a single-element list. Presenter name (when ≠ channel) is named in body prose, never in separate frontmatter.
7. Then proceed with Checks 1–3 below (Scope / Identity / Honest scoping) adapted as: *scope* = full transcript? *identity* = does the title at top match what the transcript actually delivers? *honest scoping* = state runtime in mm:ss using `duration:` and `length_seconds:`.

**Legacy-format compatibility (transition).** Files written before 2026-05-09 may use a four-line plain-text header (`title:` / `author:` / `url:` / `date published:`) without `---` delimiters and without the rich fields. Both formats are readable; YAML is canonical for new ingests. Map legacy `author:` → new `channel:` and legacy `date published:` → new `publish_date:` mentally when reading. The two legacy raw files in this repo (Karpathy at Sequoia AI Ascent; Prompt Engineering YouTube) were backfilled to YAML on 2026-05-09.

#### Source-page conventions specific to videos

The wiki source-page schema is **unchanged**. Only the source field names from the raw file change. Use this field-mapping table when drafting a video source page:

| Raw (skill output) | Wiki source page | Transformation |
| --- | --- | --- |
| `title:` | `title:` | quote-wrap if it contains `:`; otherwise verbatim |
| `channel:` | `author:` | single-element list: `["<channel>"]` |
| `url:` | `url:` | verbatim, quoted |
| `publish_date:` | `date_published:` | strip time component → ISO date only |
| `duration:` + transcript line count | `length:` | format `"~MM:SS minutes (transcript ~N lines)"`; line count computed at ingest time |
| `caption_tracks:[].kind` | source-quality flag in body (not confidence) | `kind: asr` → "auto-generated transcript, ASR-cleaned"; `kind: manual` → "human-curated transcript". *Sources do not carry confidence per [§Lifecycle](#lifecycle); transcript provenance does not feed into confidence math.* |
| `description:` | **leading blockquote in body**, before TL;DR | renders the channel's own framing of the video before the wiki's interpretation. Mandatory for video source pages. |
| `chapters:` (if present) | optional: mirror as body section headings | not load-bearing — body structure follows the source page's own rhetorical needs |
| `keywords:` | seed for `tags:` | merge with hand-curated tags |
| `category:` | optional `tags:` entry | e.g. `Science & Technology` → `science-technology` if useful |

Fixed schema fields on the source page:

- `kind: video`
- `length: "~MM:SS minutes (transcript ~N lines)"` — duration first, line count parenthetical.
- `raw: "../../raw/videos/<slug>.md"` — points to the canonical raw file.
- `url:` is mandatory (videos are first-class web sources; the file we hold is just a transcript snapshot).
- `date_published:` taken from the raw file's `publish_date:` (legacy: `date published:`), ISO-normalised to date only.
- `author:` taken from the raw file's `channel:` (legacy: `author:`) as a single-element array.
- **No separate `channel:` field on the source page** — the convention is `author = channel` for videos. The skill's `channel_id:` and `channel_url:` are not promoted into source-page frontmatter; capture them in body if substantively useful.

**Body opening for video source pages.** The body begins with the YouTube `description:` rendered as a blockquote (after the H1, before the wiki's own framing). This makes the channel's stated framing of the video legible to readers before the wiki's interpretation overlays it.

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
- `accessed_at: YYYY-MM-DD` — the date the page was last *read into context* (as opposed to written to). Added in v0.5 as the reinforcement signal for the [§Retention](#retention) curve. Seeded at v0.5 migration time to equal `last_confirmed`; bumped manually via `node scripts/bump-accessed.mjs <slugs>` after a query-time read, or procedurally during ingest (Process step 6 bumps `accessed_at` alongside `last_confirmed`). **Syntheses also carry `accessed_at`** (added after the v0.5 quality scorer flagged the omission — syntheses are claim-bearing pages, not evidence, so they decay like concepts). Sources do not carry `accessed_at` — sources don't decay; their reliability is governed by what cites them.

**Concepts and syntheses additionally carry** (added v0.5 quality slice):

- `quality_score: 0.0–1.0` — a mechanical health score combining structure, citation density, and cross-consistency. Computed by `node scripts/quality-score.mjs`; lives in frontmatter as a *derived* field (the only frontmatter value written by tooling rather than by hand). See [§Quality](#quality) for the rubric. Not on entities (which are catalogue pages, not knowledge claims) or sources (which are evidence).
- `quality_notes:` — optional list of specific issues the scorer flagged. Empty when score is at ceiling. Read by humans to know what to fix.

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
5. Prepend a `log.md` entry under `op: refactor` describing what was superseded and why (reverse-chronological convention since 2026-05-12, GH #3).

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

## Retention

Knowledge has a half-life. A concept reinforced last week sits at full strength; a concept that hasn't been read or cited in 18 months has likely drifted from the rest of the wiki around it. v2's "forgetting" idea (the Ebbinghaus-style retention curve) is captured here as a **lint signal, never an auto-edit** — decay only changes what surfaces in lint output and what the SessionStart hook highlights; it never deletes, archives, or rewrites a page.

### The decay curve

For concept and entity pages, an *effective* confidence is derived at lint time:

```
effective_confidence = stored_confidence × exp(-days_since_access / tau)
```

Where:

- `stored_confidence` is the `confidence:` value written by the most recent ingest that touched the page.
- `days_since_access` is `(today − accessed_at)`.
- `tau` is the decay time-constant: **90 days for concepts and syntheses, 365 days for entities, ∞ for sources** (sources don't decay; they are immutable evidence). Concepts and syntheses decay roughly four times faster than entities because conceptual framings and durable conclusions shift faster than the people, organisations, and products they describe — a 2024 framing of "agent harness" is less recognisable today than the 2024 identity of OpenAI.

This is read-only — the stored `confidence:` is never overwritten by decay math. `effective_confidence` is computed each time lint runs (and, from v0.5's search slice, each time the search ranker assembles a result list).

### What decay does and does not do

**Does:**

- Surface decay candidates in lint output: any page where `effective_confidence < 0.5` gets listed under "decay candidates" with the suggestion to either re-confirm (bump `accessed_at` via a normal ingest/query touch) or, if the page is genuinely stale, run the [§Supersession protocol](#supersession-protocol).
- Influence search rank from v0.5's search slice onward: low-effective-confidence pages drop in result lists.
- Influence the SessionStart hook's surfacing of "needs attention" pages.

**Does not:**

- Delete pages. Ever.
- Auto-write to `status: stale`. Stale-marking is always a human-approved supersession decision per [§Supersession protocol](#supersession-protocol).
- Overwrite `confidence:`. `confidence:` is the value the last *active* ingest wrote; `effective_confidence` is a derived view, computed on demand.
- Decay sources. Source pages have no `accessed_at:` and no decay; they are the evidence layer.

### The reinforcement signal

`accessed_at:` is bumped to today's date whenever:

1. A new ingest touches the page (this is the same trigger as `last_confirmed`, so for ingest-time touches the two fields move together).
2. A query operation reads the page into context (lands with v0.5's search slice — a scheduled hook bumps `accessed_at` on pages the search ranker returned).
3. A user manually re-confirms the page during a lint pass ("yes, this is still current" → `accessed_at` bumps).

Pages whose `accessed_at:` falls behind `last_confirmed:` are *read-aged*: they're still factually current but haven't been actively engaged with. The decay curve uses `accessed_at`, so read-engagement matters as much as ingest-time freshness.

### Cuts vs. `llm-wiki-v2.md`

- **No auto-deletion.** v2's "moved to a bottom drawer" is implemented here as "drops off the homepage and into lint output." Nothing is ever silently archived.
- **No per-page tau override.** Tau is fixed by page type (concept / entity). Personalised decay (e.g. "this concept decays slower because it's foundational") is deferred — if a concept genuinely should resist decay, set its `confidence:` to a higher value, don't introduce a per-page knob.
- **No scheduled retention sweep that auto-marks pages stale.** v2 suggests automation; this repo's hook contract ([§Hooks](#hooks)) forbids content edits from automation. Lint reports are the only output of the daily retention check.

## Quality

Not every wiki page is equally well-written. A concept with three sources but no `## Debates and supersession` section, no inbound wikilinks, and a 50-word body is structurally weak even if its `confidence:` is high. **v0.5 adds a mechanical quality score** that flags those structural weaknesses without trying to judge content correctness (LLM-as-judge is deferred to v0.6).

### What gets scored

- **Concepts** (`wiki/concepts/*.md`) — they make knowledge claims; their structural shape predicts readability and re-use.
- **Syntheses** (`wiki/syntheses/*.md`) — they are durable conclusions and bear the strictest schema (Question / Findings / Sources consulted / Lessons / Open questions).
- **Not entities** — entity pages are catalogue cards (who/what/where); the quality model doesn't fit. Their health is governed by `confidence`, `source_count`, and `relationships` only.
- **Not sources** — sources are evidence, immutable, never scored.
- **Not threads** — threads are provisional by design; quality scoring would be premature.

### The rubric

`quality_score` is a weighted sum on `[0.0, 1.0]`. Three dimensions:

| Dimension | Weight | What's checked |
| --- | ---: | --- |
| **Structure** | 0.40 | H1 present; required sections present per page type (`## Debates and supersession` for concepts with `source_count > 1`; the five mandatory sections for syntheses per [§Synthesis](#synthesis)); frontmatter contract complete (`confidence`, `last_confirmed`, `source_count`, `accessed_at`); body length ≥200 words (i.e. not a stub). |
| **Citation density** | 0.30 | Number of wikilinks to source pages (`[[2026-…-…]]`) per 1000 body words. Target: ≥3.0 source links per 1000 words. Scored linearly up to that ceiling. The wiki's central convention is *citations beat assertions* — this dimension enforces it numerically. |
| **Cross-consistency** | 0.30 | Every `relationships:` target slug exists as a real page; every typed relationship has a body wikilink (the v0.3 body-wikilink rule) at least mentioning the target; no broken `[[wikilink]]`s; concepts with `source_count > 1` have a `## Debates and supersession` section (overlaps Structure but counted again because it's the load-bearing claim about epistemic honesty). |

The 0.40 / 0.30 / 0.30 weighting reflects the schema's priorities: structure is the most-tractable lever the wiki controls; citation density and cross-consistency together encode the *citation discipline + relationship discipline* that the v0.2 and v0.3 layers established.

### Thresholds

- **`quality_score ≥ 0.85`** — page is at or near ceiling. No action needed.
- **`0.65 ≤ quality_score < 0.85`** — workable; specific issues listed in `quality_notes`. Address opportunistically.
- **`quality_score < 0.65`** — needs work. Surfaced by lint and SessionStart hook; address before adding new sources to the page.

### How and when it runs

- **Manual batch** — `node scripts/quality-score.mjs` walks `wiki/concepts/` and `wiki/syntheses/`, recomputes scores, writes `quality_score` and `quality_notes` back to frontmatter. Idempotent — if the score and notes haven't changed, no write happens (git stays clean).
- **Dry-run** — `node scripts/quality-score.mjs --dry-run` prints the score table without writing.
- **Single page** — `node scripts/quality-score.mjs --page <slug>` scores one page (e.g. just after editing a concept).
- **Not hook-fired** — quality scoring runs cross-page consistency checks; running it on every PostToolUse would walk the entire wiki on every keystroke. Run it manually after each ingest batch, or weekly as a corpus health check.

### The auto-write exception

`quality_score` and `quality_notes` are **the only frontmatter fields the schema permits tooling to write to.** The hooks contract ([§Hooks](#hooks)) forbids content-page edits from automation — but `quality_score` is a *derived* value, not editorial content, and the script is explicit + idempotent + user-invoked (not hook-fired). The exception is narrow on purpose: any future "auto-write" temptation must clear the same bar — derived, deterministic, user-triggered.

### Cuts vs. `llm-wiki-v2.md`

- **No LLM-as-judge yet.** v2 suggests "a second pass with a different prompt" for quality evaluation. That's the v0.6 quality slice — `scripts/judge-quality.mjs` will overlay an LLM rubric on top of the mechanical score for concepts and syntheses.
- **No auto-rewrite of low-quality pages.** Even when a page scores below 0.65, the script never edits its content — it only writes the score and the notes. The notes tell a human (or Claude in a future session) what to fix; the fix is editorial.
- **No quality score on entities or sources.** v2 implies scoring "everything" — this repo restricts the rubric to pages where structural shape predicts re-use value (concepts and syntheses). Extending to entities is plausible but adds noise more than signal at current scale.

## Search

At ~200 pages the wiki has outgrown `index.md` as a primary discovery surface. v2's "hybrid search past 100–200 pages" warning has cashed in. v0.5 adds **[qmd](https://github.com/tobi/qmd)** (`@tobilu/qmd` on npm) as the local search engine — BM25 keyword + vector semantic + LLM re-ranking, all on-device via `node-llama-cpp` with GGUF models. No external API; no embedding service.

### What lives where

- **qmd's index** (BM25 inverted index + 768-d embeddings per page) lives outside the repo, in qmd's own data directory (typically `~/.qmd/`). It is not committed.
- **The collection mapping** is registered with qmd as the named collection `ai-wiki`, rooted at `./wiki` with the glob `**/*.md` (so the 205-page corpus of concepts, entities, sources, threads, syntheses, plus `index.md` and `log.md` is indexable).
- **The collection context-string** (registered via `qmd context add qmd://ai-wiki "..."`) carries the schema summary so qmd's LLM re-ranker has framing when surfacing results.
- The wiki's typed graph (`wiki/.graph.json` from v0.3) remains the third retrieval stream; it is **not** indexed by qmd. Graph traversal is invoked separately (see §Graph) and merged with qmd's hits via Reciprocal Rank Fusion at the query-answering layer.

### When to use qmd vs `index.md`

| Query shape | Strategy |
| --- | --- |
| Looking up a known page by exact title or alias | `index.md` — direct lookup, fastest |
| Question that obviously hits ≤5 wiki pages by name | `index.md` — open them directly |
| Question that touches >5 pages, or whose answer requires synthesis across several | **qmd first** to narrow to top 10, then read those |
| Open-ended exploration ("what does the wiki say about X-ish topics") | **qmd `query`** (hybrid + rerank) — it surfaces semantic neighbours `index.md` won't catch |
| Looking for *structural* context ("what is `agent-harness` `part-of`?") | Graph traversal via `wiki/.graph.json` — qmd doesn't know about typed edges |
| Answer that must be **auditable** ("show your work" / fact-check / defensible briefing) | **`/wqa`** ([§Auditable answers](#auditable-answers-wqa)) — fuses qmd + graph, then records what was used vs. ignored and maps every answer element back to its page |

The 5-page threshold is a heuristic. The real test is whether the query would force you to scan >50% of `index.md` to find candidates — if yes, qmd is cheaper.

### qmd command cheat-sheet

Run via `npx @tobilu/qmd <command>` (no global install needed) or `qmd <command>` after `npm install -g @tobilu/qmd`.

- **`qmd query "<question>"`** — **default for complex queries.** Hybrid retrieval (BM25 ∪ vector) followed by LLM re-ranking. Slower per call but most robust to phrasing variation.
- **`qmd search "<terms>"`** — fast BM25 keyword search. Use when the terms are specific and you expect literal matches.
- **`qmd vsearch "<question>"`** — pure vector semantic search. **Warning:** unreliable on lexically ambiguous paraphrases — without a BM25 leg, vector can resolve to the wrong semantic cluster on a single misleading word (the v0.5 acceptance test caught this: a Dutch paraphrase with the ambiguous *"in productie"* sent vsearch to the labor/employment cluster instead of harness/runtime; `query` got it right). Treat `vsearch` as a diagnostic tool, not a primary discovery surface.
- **`qmd get "<path>"`** — fetch a specific document by path, or `qmd get "#<docid>"` by qmd's internal id (shown in search results).
- **`qmd multi-get "<glob>"`** — fetch multiple documents by glob (e.g. `"sources/2026-05*.md"`).

The **collection name** (`ai-wiki`) becomes a URI prefix in qmd's output: results are reported as `qmd://ai-wiki/<path>`. Treat that as the wiki source-of-truth path.

### Re-embedding after writes

qmd's index does not auto-refresh. After ingest sessions that add or substantially edit pages, refresh in **two steps**:

```sh
npx @tobilu/qmd update   # re-index: discover NEW files + detect edited ones
npx @tobilu/qmd embed    # compute embeddings for changed/added content hashes
```

**`update` before `embed` is load-bearing for *added* files.** `qmd embed` only embeds documents qmd already knows about — on a session that creates new pages, running `embed` alone reports *"all content hashes already have embeddings"* and silently skips the new files (they never enter the index). `qmd update` re-scans the collection root, picks up new files and edits, and *then* `embed` vectorises them. For sessions that only *edit* existing pages, `embed` alone suffices, but running both is always safe and idempotent. (Precedent: the 2026-06-12 ReAct ingest hit the silent-skip; the 2026-06-13 GDPval ingest confirmed `update` picks up the new files — "Indexed: 3 new, 13 updated".)

`embed` computes embeddings only for pages whose content hash changed (qmd tracks hashes per document). On a typical post-ingest run (5–10 pages touched), this is seconds. A full rebuild is rare.

### Re-ranking by `effective_confidence`

When qmd returns its top-N, the query-answering layer should re-rank by §Retention's `effective_confidence`. A high-BM25 hit on a concept that has decayed (e.g. `effective_confidence < 0.5` because `accessed_at` is 18 months old) is downgraded relative to a fresher concept on the same topic. This is the integration point between §Search and §Retention — qmd returns relevance, the wiki's lifecycle math returns currency, and both matter. The re-ranking is computed at read-time; qmd's stored scores are not modified.

### Bumping `accessed_at` after a query

When a query consumes pages from qmd's results, **bump those pages' `accessed_at` to today** — that's the reinforcement signal §Retention's decay curve uses. There are three routes, from most integrated to most manual:

**Route 1 — `/wq` slash command** (most ergonomic, the default for interactive use):

```
/wq wat zegt de wiki over dynamische capaciteiten van organisaties
```

The command dispatches to [`scripts/wiki-query.mjs`](scripts/wiki-query.mjs) which runs `qmd query --json`, prints the top-N results, **and automatically bumps `accessed_at`** on every concept / entity / synthesis page returned. Sources in the result list are skipped (they don't decay). Language-agnostic — the slash command answers in the query's language.

**Route 2 — wiki-query wrapper directly** (for shell, scripts, other agents):

```sh
node scripts/wiki-query.mjs -n 8 "your question"          # 8 results + bump
node scripts/wiki-query.mjs --no-bump -n 3 "quick lookup" # skip the bump
node scripts/wiki-query.mjs --json "your question"        # raw qmd JSON
```

Same auto-bump semantics as `/wq`. The `--json` flag passes qmd's structured output through unchanged — useful for other agents or pipelines.

**Route 3 — qmd MCP server** (for agents that want a direct tool):

Register the qmd MCP server by adding a `.mcp.json` at the repo root (one-time, user-authorised):

```json
{
  "mcpServers": {
    "qmd": {
      "command": "npx",
      "args": ["--yes", "@tobilu/qmd", "mcp"]
    }
  }
}
```

After reload, agents in this repo have direct `query`, `get`, `multi_get`, `status` tools from qmd's MCP server. **Important caveat:** qmd's MCP server does *not* know about the wiki's `accessed_at` reinforcement rule — it only retrieves. Agents using MCP directly should still call `node scripts/bump-accessed.mjs <slugs>` afterwards to honour §Retention. The `/wq` slash command and `wiki-query.mjs` wrapper are the only paths that bundle both operations.

**Manual fallback** for ad-hoc bumps unrelated to a query:

```sh
node scripts/bump-accessed.mjs <slug> [<slug> ...]
```

Idempotent — a slug already at today's date is a no-op. Slugs resolve against `wiki/concepts/`, `wiki/entities/`, `wiki/syntheses/`. Sources are rejected (they don't decay).

### Auditable answers (`/wqa`)

`/wq` is the quick-lookup surface: it retrieves, you read, you answer. When the answer must be **traceable** — fact-checking a claim, a defensible briefing, a "show me exactly where this comes from" request — use the **`traceable-wiki-answer`** skill via **`/wqa <question>`** instead. It produces not just an answer but a full provenance trace: the question, every wiki path explored, what was used vs. **ignored (with a reason-class for each)**, where each fact lives, and a mapping from every answer element back to its wiki page.

The skill is the operational home of two pieces of §Search and §Retention machinery that `/wq` leaves to the agent:

- **Multi-strategy fusion.** [`scripts/wiki-retrieve.mjs`](scripts/wiki-retrieve.mjs) is the skill's retrieval entry point. It runs `qmd query --json` (relevance) **and** walks `wiki/.graph.json` typed edges from each qmd seed (structure), fuses the two streams with Reciprocal Rank Fusion (graph stream down-weighted so a structural neighbour can't tie a genuine search hit), then re-ranks by §Retention's `effective_confidence` as a *dampener* (relevance sets the order; decay demotes). It emits a JSON **candidate ledger** — the script scores, the agent verdicts. Degrades to qmd-only with a logged `graph_warning` if `wiki/.graph.json` is missing.

  ```sh
  node scripts/wiki-retrieve.mjs --json -n 12 "your question"   # ledger (skill default)
  node scripts/wiki-retrieve.mjs --hops 2 "your question"       # widen graph traversal
  node scripts/wiki-retrieve.mjs --no-bump --json "question"    # don't touch accessed_at
  ```

  Same auto-bump semantics as `wiki-query.mjs` — it bumps `accessed_at` on the qmd-returned concept/entity/synthesis pages as its last step (bump output to stderr so `--json` stdout stays clean). Pages promoted from the graph stream during gap-expansion need a manual `bump-accessed.mjs` per the skill's Step 8.

- **The ignore decision as a recorded artifact.** Triage (use/ignore, one reason-class per ignore) lives in the trace, not the script — see `.claude/skills/traceable-wiki-answer/references/ignore-policy.md`. Outputs land in `inspiration/<date>-<slug>-query-trace.{md,json}` (the 8-section audit report + machine-readable trace), mirroring how `iterative-wiki-query` saves research logs. The artifacts sit outside `wiki/**`, so the PostToolUse lint hook does not fire on them.

Use `/wq` for speed, `/wqa` when provenance matters; both honour the §Retention bump.

### Cuts vs. `llm-wiki-v2.md`

- **No external API embeddings.** v2 mentions "vector search via embeddings"; qmd's local GGUF route honours that without OpenAI/Anthropic API exposure.
- **No graph-aware retrieval inside qmd.** Graph traversal stays in `wiki/.graph.json` + `scripts/`; merging happens at the answer-synthesis layer, not inside the retrieval engine. v2 envisions a unified store; this split is pragmatic and revisable.
- **No MCP integration yet.** qmd ships an MCP server; wiring it into Claude Code as a native tool is deferred to the v0.5 quality slice (or whenever it becomes friction). Until then the CLI route works.
- **No auto-refresh hook on edit.** The PostToolUse lint hook ([§Hooks](#hooks)) deliberately does not call `qmd embed` after every wiki edit — re-embedding on every keystroke would thrash. Re-embed runs as part of the manual ingest-completion checklist, not as automation.

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

### Source-to-source relationships

The closed vocabulary works for source pages too. A source page may declare typed `relationships:` pointing to other source pages — the most common types in practice are **`supports`** (e.g., a research-frontier paper supports an applied practitioner workshop on the same topic; an empirical dataset supports the framework a prior conceptual paper named), **`contradicts`** (e.g., a study disconfirms a prior empirical claim — always pair with `via:` describing what the disagreement turns on), and **`supersedes`** (per [§Supersession protocol](#supersession-protocol) — pair with `status: stale` + `superseded_by:` on the retired source).

Source-to-source edges are how the wiki encodes its **thematic cluster index** — two sources on the same topic with no typed edge between them is a graph-quality smell, not a neutral state. The [§Ingest](#ingest) workflow's step 5 (Neighbour-source scan) is the disciplined way to keep this layer consistent.

### Body-wikilink rule (load-bearing)

**Every typed relationship in frontmatter must also appear as a body `[[wikilink]]` with at least one sentence of context.**

Frontmatter is the *typed* layer; body is the *navigable* layer; both are required. If a relationship exists only in frontmatter, Quartz's link crawler cannot follow it — you get a relationships panel pointing at links that don't show up in the graph view. If a wikilink exists only in body, the relationship is untyped and the graph export misses it. Lint enforces both directions from v0.4.

A page's `## Related concepts` / `## Related pages` / in-prose mentions usually already satisfy the body side; the migration just adds the frontmatter twin.

### Wikilink-rendering rule (Quartz compatibility)

**Never put markdown formatting inside the alias portion of a wikilink.** Quartz's default forward-link parser expects a literal string between `|` and `]]`; emphasis (`*…*`), bold (`**…**`), or other markdown inside the alias either leaks the raw characters into the rendered link text or silently breaks the link on the published site. Obsidian renders these fine because it processes the alias as full markdown — so the breakage is invisible in authoring and only shows up after deploy.

Two safe patterns:

- **Full-alias italics**: move the asterisks outside the wikilink — `*[[target|alias]]*`, not `[[target|*alias*]]`.
- **Partial italics inside an alias** (e.g. a publication title within a longer descriptive alias): drop the inner asterisks — `[[target|Author 2026 — Title of Paper (Journal)]]`, not `[[target|Author 2026 — *Title of Paper* (Journal)]]`. The `[[…]]` rendering already signals the link is to a publication; the visual loss is minor and the link stays clickable.

This rule applies to body text, table cells, and any other markdown context where a wikilink renders. Frontmatter wikilinks (e.g. `relationships.target:`) are a separate matter — those should be slugs only, never wikilinks at all.

### Graph export

`scripts/graph-export.mjs` walks all `wiki/**/*.md`, reads frontmatter, and emits `wiki/.graph.json` (gitignored) with a node list (slug, type, kind, confidence) and an edge list (type, source, target, confidence, via). Re-run after any migration that changes relationships. v0.5 hybrid search uses this file as its third stream.

### Formalized `kind:` enum (entities)

`kind:` on entity pages is now restricted to one of: `person | organization | product | project | place | event | library | dataset | benchmark | venue`. Drift from earlier ingests (e.g. `org` for organization) gets normalized during the v0.3 migration.

## Dynamic-capabilities tagging

Source pages may carry a `dynamic_capabilities:` frontmatter field declaring which **Warner & Wäger (2019) process-model cells** the source touches. This adds a queryable meta layer parallel to v0.3's typed `relationships:`, but specialised to the digital-transformation lens: rather than "this source supports/contradicts another wiki page," the tag answers "what kind of digital-transformation work is this source about?"

The closed vocabulary, the operational definitions for each slug, and the `role_defaults:` matrix that drives role-relevance inheritance all live in one place: [[concepts/warner-wager-process-model|warner-wager-process-model]]. That concept page is the single source of truth; CLAUDE.md only documents the *contract* between source pages and the lint.

### Frontmatter contract (source pages)

```yaml
dynamic_capabilities:
  - <bucket>/<element>
  - ...
roles: [<role-slug>, ...]   # optional override, see §Role-relevance
```

- `dynamic_capabilities:` is **optional**. Pre-2026-05-14 source pages do not need backfill; new ingests should tag when the W&W lens applies.
- Each entry must be drawn from the closed vocabulary published on [[concepts/warner-wager-process-model|warner-wager-process-model]] (15 cells across 5 buckets: `digital-sensing/*`, `digital-seizing/*`, `digital-transforming/*`, `strategic-renewal/*`, `contextual/*`).
- Multiple entries allowed when a source genuinely speaks to multiple cells.
- **Tagging is encouraged, not forced.** When a source sits outside the W&W lens (e.g. pure LLM-internals papers, model-quantization mechanics), omit the field rather than stretching the vocabulary.
- `dynamic_capabilities:` tags do **not** carry per-entry `confidence:` — the tag is a binary "touches / doesn't touch" classification, not a graded claim.

**Tags as discovery index.** Beyond classification, `dynamic_capabilities:` cells are the corpus's **thematic adjacency index**. Two source pages sharing a cell are conceptually adjacent — they are the first candidates for source-to-source typed `relationships:` per [§Source-to-source relationships](#source-to-source-relationships). The [§Ingest](#ingest) workflow uses this affordance in its step 5 (Neighbour-source scan), with a fallback path through shared concept-page citations for pre-GH #4 sources that don't carry W&W tags yet. A future lint rule can flag sources with ≥2 overlapping cells but no typed relationship between them; until then the discipline is the ingestor's, and the *"≥3 candidate neighbours, surface the list"* rule in Ingest step 5 is the accountability mechanism.

### Body twin rule (load-bearing)

**Every `dynamic_capabilities:` entry in frontmatter must be reflected in the body** — at minimum one sentence in the page summary saying *how* the source touches that cell, ideally naming which of the bullet-level activities listed on [[concepts/warner-wager-process-model|warner-wager-process-model]] are in play. Frontmatter is the typed layer; body is the navigable layer. Both required.

This mirrors v0.3's [§Body-wikilink rule](#body-wikilink-rule-load-bearing) for typed relationships — same architectural pattern, same enforcement mechanism. Lint matches on the cell slug or its trailing element (e.g. either `digital-seizing/balancing-digital-portfolios` or `balancing-digital-portfolios` in body prose satisfies the rule).

### Role-relevance inheritance

Each cell carries a **default role profile** — the business roles that would typically care about a source in that cell. The matrix lives on [[concepts/warner-wager-process-model|warner-wager-process-model]] as a `role_defaults:` block, with 15 role slugs across nine C-suite (`ceo`, `coo`, `cfo`, `cso`, `cdo`, `cto`, `cio`, `chro`, `cmo`) and six functional roles (`product-manager`, `tech-lead`, `rd-director`, `innovation-lab-lead`, `transformation-lead`, `strategy-consultant`).

Role-relevance is **derived** from `dynamic_capabilities:` by default — no per-source `roles:` needed. A source page may add an explicit `roles:` list when its emphasis diverges from the cell defaults; when present, `roles:` **replaces** the inherited defaults for that source (half-overrides are not supported in v1).

`roles:` is a list of role slugs from the closed vocabulary on the concept page. Lint validates the vocabulary on source pages. (On person-entity pages, `roles:` — if used — remains a free-text job-title field, not a slug list. Lint distinguishes by `type:`.)

The body-twin rule does **not** extend to `roles:` — role-relevance is a derived view, not an independent claim.

### When not to tag

- Sources purely about LLM internals (training dynamics, quantization, attention mechanics) where the W&W lens does not apply.
- Sources where the only plausible cell is `contextual/external-triggers` and even that feels forced — leave the field off rather than over-fit.
- Sources whose contribution is purely methodological (analysis tools, vocabularies, benchmarks) without a digital-transformation use case attached.

The point of the tagging layer is to make the *digital-transformation reading* of the corpus queryable. A source that does not contribute to that reading should not be forced into the vocabulary just to have a tag.

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
5. Prepend a `log.md` entry under `op: synthesize` describing the question and the headline finding (reverse-chronological convention since 2026-05-12, GH #3).

## Hooks

v0.4 wires Claude Code hooks (configured in [`.claude/settings.json`](.claude/settings.json)) so the bookkeeping that v0.2 and v0.3 added doesn't have to be triggered manually. The harness fires the hooks; the scripts under [`scripts/`](scripts/) are the implementations.

### Non-negotiable rule

**Hooks may write to `wiki/log.md`, to lint reports (stderr/stdout), and to gitignored derived artifacts (`wiki/.graph.json`). Hooks may NOT edit any `wiki/**/*.md` content page** — not concept, not entity, not source, not synthesis, not thread, and not `index.md`. Content edits always require explicit user approval in-session.

This protects the v1 trust contract ("Claude owns the wiki layer, user owns direction") from automation drift. A hook that silently rewrites a concept page when the user wasn't looking is a worse failure than a hook that doesn't fire.

### Hooks in use

| Event | Script | Purpose |
| ----- | ------ | ------- |
| `SessionStart` | [`scripts/session-start.mjs`](scripts/session-start.mjs) | Outputs a short wiki snapshot (catalog counts, 5 most recent log entries — the *first* 5 since the 2026-05-12 reverse-chronological flip, `status: stale` and `confidence < 0.5` flags) to stdout — Claude Code feeds it back as session context. Read-only. |
| `PostToolUse` (Edit, Write) | [`scripts/lint-page.mjs`](scripts/lint-page.mjs) | If the just-edited file is under `wiki/**/*.md`, validates the v0.2 lifecycle contract (`confidence`, `last_confirmed`, `source_count`), the v0.3 closed relationship vocabulary, and the v0.3 body-wikilink rule (every `relationships.target` must appear as a body `[[wikilink]]`). Warnings to stderr. Always exits 0 — never blocks the tool call. |
| `Stop` | [`scripts/session-end.mjs`](scripts/session-end.mjs) | Per-turn check: if any `wiki/**/*.md` is modified or untracked, re-runs [`scripts/graph-export.mjs`](scripts/graph-export.mjs) so `wiki/.graph.json` stays fresh; otherwise exits silently. No log writes. |

### Auto-prefix log convention

When/if a hook ever does write to `log.md` in a future version, the entry's op must be prefixed `auto-` (e.g. `auto-lint`, `auto-supersession-check`) to distinguish hook-fired writes from human-curated entries. Currently no hook writes log entries; this convention is reserved.

### Cuts vs. v2 plan

- **No on-query hook** — the "file good answers back" decision is human-judgment, not a hook target.
- **No scheduled retention decay** — deferred to v0.5 alongside hybrid search.
- **`session-end.mjs` does not write a log entry** — `Stop` fires per-turn, not per-session, so per-turn entries would be too noisy. Manual log writing (now prepending) remains the convention until a real `SessionEnd` event is wired (or a session-end slash command is built).
- **No auto-fix on lint warnings** — `lint-page.mjs` only reports; the human or Claude decides what to do.

## Reference

`llm-wiki.md` — the upstream conceptual spec.
`llm-wiki-v2.md` — the v2 extension (lifecycle, knowledge graph, hooks, hybrid search, crystallization).
`llm-wiki-v2-plan.md` — the staged release plan that turns v2 into versioned releases for this repo.

Re-read whichever spec applies whenever a workflow question comes up that this file doesn't answer, then consider promoting the resolution into this file.
