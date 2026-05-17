# LLM Wiki v2 — Staged Release Plan

## Context

`llm-wiki-v2.md` extends Karpathy's original LLM Wiki pattern with patterns proven by the agentmemory engine. It introduces nine feature clusters (lifecycle, knowledge graph, hybrid search, automation hooks, quality/self-correction, multi-agent collaboration, privacy/governance, crystallization, output formats) and explicitly says you don't need everything on day one — pick an entry point on its "implementation spectrum."

The current `ai-wiki/` repo is the v1 instantiation: 93 pages (54 entities, 17 concepts, 20 sources, 2 open threads, 0 syntheses), strict log conventions, alias-aware Quartz publishing, and a CLAUDE.md that already encodes ingest/query/lint operations and source-verification preflight. Several v2 ideas are *partly* present in disguise: `kind:` is proto-entity-typing, `log.md` is proto-audit-trail, "Debates / contradictions" prose sections are proto-supersession, the open `wiki/threads/` are proto-crystallization-targets.

The user has chosen "all v2 features, full build, staged release plan." The work below originally staged the spec into six small versions (v0.2 → v0.7) plus an optional v0.8+; the 2026-05-17 update (see below) added v0.8 and v0.9 from a third upstream, with deferred work renumbered to v0.10+. Each version is small enough to absorb in days-to-weeks of single-user evolution, lands schema before tooling, and either ends with a clean migration of existing pages or doesn't touch them at all. The scale-down from "all features" comes from two honest cuts: (a) multi-agent / mesh-sync infrastructure is YAGNI for a single user — only the `scope: shared|private` flag is kept; (b) the four consolidation tiers from v2 are reduced to *naming the tiers in CLAUDE.md prose* rather than building separate storage layers, because raw → source → concept/entity → CLAUDE.md already maps onto them.

### Update 2026-05-17 — third upstream + repo contributions beyond v2

The plan was originally drafted against two upstreams (Karpathy's `llm-wiki.md` + agentmemory's `llm-wiki-v2.md`). On 2026-05-17 a comparative synthesis added a **third upstream**: the InfraNodus `skill-llm-wiki/SKILL.md` (10-phase scaffolding skill). InfraNodus contributes two ideas neither Karpathy nor v2 has:

1. **Acquire ≠ Process.** The skill splits ingest into two re-runnable operations: *acquire* (touch `raw/`, convert PDF → markdown, place into typed subfolders) and *process* (read `raw/`, write `wiki/`). They fail differently, run on different cadences, and skipping either is common. This repo half-does it already — the `youtube-transcript-skill` is an acquire-time tool — but the schema never names the split. Lands as **v0.9** below.
2. **Plan as a fifth operation.** Gap-driven todo generation: read the wiki + the graph + (optionally) InfraNodus's gap-analysis output, produce a prioritised `todos/` folder of next-research workstreams. No analogue in v1 or v2. Lands as **v0.8** below.

The synthesis also surfaced **this repo's own contributions** that the upstream specs don't have, worth naming so they don't get lost:
- **Body-wikilink rule** (v0.3) — every typed `relationships:` entry in frontmatter must appear as a body `[[wikilink]]` with a sentence of context. Lint-enforced. Closes a v2 hole where typed-graph edges and Quartz's wikilink crawler can diverge silently.
- **Dynamic-capabilities tagging** (v0.5 schema, GH #4) — the Warner & Wäger process-model overlay on source pages, with role-relevance inheritance. A domain-specific tagging layer that v2 doesn't anticipate but its closed-vocabulary frontmatter pattern naturally accommodates.
- **Neighbour-source scan** (v0.5 ingest checklist) — step 5 of ingest asks "what existing sources share a `dynamic_capabilities:` cell, or cite the same concept pages I'm about to update?" Produces typed source-to-source `relationships:` (`supports` / `contradicts` / `supersedes`). This is an applied lint built into the ingest path itself — no upstream describes it.
- **YAML frontmatter contract for raw video sources** (v0.5) — the `youtube-transcript-skill`'s output is the canonical pre-flight format. Names the four load-bearing identity fields and the legacy-format compatibility rule.

Two synthesis takeaways feed the rest of this document: (a) the **Plan operation** is genuinely new and merits its own version, not a v0.8+ footnote; (b) the **acquire-vs-process split** is a schema clarification, not a tooling effort — it slots cleanly between v0.7 and v0.10+.

## Approach at a glance

| Version | Theme | Schema lands | Tooling lands | Migration |
| ------- | ----- | ------------ | ------------- | --------- |
| v0.2    | Lifecycle metadata | confidence, last_confirmed, source_count, supersedes/superseded_by, status: stale | `inject-stale-banner.tsx`, `lint-confidence.mjs` | 71 pages bulk-edited (concepts + entities) |
| v0.3    | Typed entity graph + synthesis contract | relationships block (YAML object), formalized `kind:` enum, `type: synthesis` page contract, derived_from | `inject-relationships.tsx`, `graph-export.mjs`, `synthesize` operation | 54 entities gain relationships; 2 open threads close into syntheses |
| v0.4    | Automation hooks | `§Hooks` in CLAUDE.md, `auto-` log prefix | `.claude/settings.json` hooks (SessionStart, Stop, PostToolUse), `session-start.mjs`, `session-end.mjs`, `lint-page.mjs`, `lint-orphans.mjs`, `repair-xrefs.mjs` | None (additive) |
| v0.5    | Hybrid search + retention | `accessed_at`, `quality_score`, `§Retention` curve | qmd install + index, scheduled lint hook, `quality-score.mjs` | Seed accessed_at; score concepts |
| v0.6    | Crystallization + LLM-as-judge | `crystallize` operation, `type: lesson` pages, `§Quality review` | `/crystallize` slash command, `judge-quality.mjs`, thread-aging hook | Crystallize 2 existing threads |
| v0.7    | Output formats + scoping | `scope: shared\|private`, `sensitive: true`, bulk-ops governance | `exclude-private.ts`, `/compare`, `/timeline`, `/marp-deck`, `/export-csv`, `ingest-filter.mjs` | None unless private flagged |
| v0.8    | **Plan operation** (5th op, gap-driven todos) — InfraNodus contribution | `§Plan` operation, `todos/` folder contract, `op: plan` log prefix | `/plan` slash command, `scripts/detect-gaps.mjs`, `scripts/seed-todos.mjs` | Generate first `todos/` from current wiki state |
| v0.9    | **Acquire/Process refactor** — make ingest's two phases explicit (InfraNodus contribution) | §Ingest split into §Acquire + §Process; typed `raw/` subfolder enum; skill-as-acquire-step pattern formalised | None new — youtube-transcript-skill already fits the pattern; document the contract | None (schema-only) |
| v0.10+  | Deferred (mesh sync, external graph DB, on-query hook, consolidation infra, retention auto-deletion) | — | — | only if forced |

Three principles run through every version:
1. **Schema-first.** CLAUDE.md sections + frontmatter contracts land before any tooling that depends on them.
2. **Hooks may not silently edit content.** They write to `log.md` and lint reports; content edits to `wiki/**/*.md` always require explicit user approval. This protects the "Claude owns the wiki, user owns direction" contract.
3. **Migrations are supervised.** Bulk edits to existing pages happen in batches of ~10, with Claude reading each page and writing defensible values — never via blind script.

---

## v0.2 — Lifecycle metadata: confidence, supersession, dates

**Goal.** Give every wiki claim a vocabulary for "how sure" and "what replaced what." Schema only, no automation, no decay math.

**Lands.** Cluster 1 (lifecycle) partial: confidence + supersession schema. Cluster 7 (privacy/governance) partial: codify `log.md` as the audit trail (already true — just declare it).

**Schema changes — `CLAUDE.md` adds new section §Lifecycle.**
- New frontmatter on **concepts and entities**:
  - `confidence: 0.0–1.0` (default 0.7 for one-source pages; rules: +0.05 per additional source, −0.1 if any contradicting source).
  - `last_confirmed: YYYY-MM-DD` (most recent ingest that reinforced the page).
  - `source_count: N` (computed from inbound source links).
- New frontmatter on **source pages**: `supersedes: [[old-source]]` (optional list).
- New frontmatter on **any page**: `status: stale` + `superseded_by: [[new-page]]` for retired-but-preserved pages.
- Promote in-prose "Debates" pattern to a **required `## Debates and supersession` section** on concept pages with >1 source.
- Update §Ingest to require setting/bumping `last_confirmed` and `source_count` on every touched concept/entity page.

**Tooling.**
- New extension `extensions/inject-stale-banner.tsx`: when frontmatter has `status: stale`, render a yellow callout at top of page linking to `superseded_by`. Mirrors the simple frontmatter-reading pattern of [`extensions/inject-type-tags.ts`](/Users/witoldtenhove/Projects/ai-wiki/extensions/inject-type-tags.ts).
- Optional: graph-view filter chip via the existing `inject-type-tags.ts` (`status/stale` already auto-emerges if status is added to tags).
- New script `scripts/lint-confidence.mjs` — read-only walker that prints distribution of confidence values and flags concepts >30 days old without a `last_confirmed` bump.

**Migration.**
- 71 pages (17 concepts + 54 entities) gain three new fields each. Done in supervised batches of ~10 per session. Claude reads page, counts inbound sources from `wiki/index.md` and `log.md`, sets defensible values. Highest-risk step in v0.2 — script-based defaults would be wrong half the time.
- Sources don't get `confidence` (sources are evidence, not claims).
- One-time scan of `log.md` for "supersedes / contradicts / replaces" wording; back-fill `supersedes:` on the few sources where it applies (Brynjolfsson Canaries vs the equalizing-effect framing is the obvious one).

**Prereqs.** None — this is the foundation.

**Cuts vs. v2 spec.**
- No retention/forgetting curve (deferred to v0.5).
- No four-tier consolidation pipeline. CLAUDE.md prose names the implicit tiers: `raw/` → sources → concepts/entities → CLAUDE.md. No directories or scripts for them.
- No quality_score (deferred to v0.5).

**Verification.**
- `npm run build` green.
- All 71 pages have all three new fields, no defaults left at 0.0.
- `lint-confidence.mjs` runs, prints distribution.
- Stale banner renders on a hand-picked test page (e.g. a sample-only source like `2026-05-03-rewired-second-edition-sample.md` once superseded by a full ingest).
- A `log.md` entry documents the bulk migration as `bulk-refactor | v0.2 lifecycle migration`.

---

## v0.3 — Typed entity graph + synthesis contract

**Goal.** Make relationships first-class and queryable, without breaking Quartz's wikilink resolver.

**Lands.** Cluster 2 (knowledge graph) most of it — typed relationships in frontmatter, formalized entity types, derived graph JSON. Cluster 8 (crystallization) schema slice — define what a synthesis page looks like; first synthesis is the v0.3 acceptance test.

**Schema changes — `CLAUDE.md` adds §Graph and §Synthesis.**
- Formalize `kind:` enum on entities: `person | organization | product | project | place | event | library | dataset | benchmark | venue`. Migrate any drift.
- New frontmatter on entities + concepts: `relationships:` as a YAML object list — **NOT** wikilinks-in-frontmatter (Quartz's link resolver doesn't traverse those reliably; you'd get partial/silent broken links).
  ```yaml
  relationships:
    - type: contradicts
      target: ai-employment-effects
      via: "occupation-level vs task-level"
      confidence: 0.7
    - type: authored-by
      target: Erik-Brynjolfsson
  ```
- Closed relationship vocabulary: `uses, depends-on, contradicts, supports, caused, fixed, supersedes, part-of, instance-of, authored-by, published-by, employs`.
- **Hard rule (load-bearing).** Every typed relationship in frontmatter must also appear as a body `[[wikilink]]` with a sentence of context. Frontmatter is the *typed* layer; body is the *navigable* layer; both are required. Lint enforces this from v0.4.
- New page type `type: synthesis`. Required sections: Question / Findings / Sources consulted / Lessons / Open questions. Required frontmatter: `derived_from: [[thread-A]], [[thread-B]]`, plus the standard lifecycle fields from v0.2.
- New CLAUDE.md operation **synthesize** (already in `log.md`'s permitted-ops enum but undefined): close a thread → produce a synthesis page → file under `wiki/syntheses/`.

**Tooling.**
- New extension `extensions/inject-relationships.tsx`: render the typed relationships as a structured panel on the page (separate from backlinks); group by relationship type.
- New script `scripts/graph-export.mjs`: walks all pages, emits `wiki/.graph.json` (gitignored) with nodes (slug, type, kind, confidence) and edges (type, source, target, confidence, via). This is the input format for any future hybrid search, agent traversal, or external visualization. Don't skip it — v0.5/v0.6 depend on it existing.

**Migration.**
- 54 entities gain a `relationships:` block (most small: org X `employs` person Y, person Y `authored` source Z, source Z `published-by` venue W). Batches of ~10 per session, supervised.
- 17 concepts gain relationships where they exist (mostly `supports` / `contradicts` between concepts; `authored-by` doesn't apply).
- The two open threads — [`organizational-frameworks-for-ai-adoption`](/Users/witoldtenhove/Projects/ai-wiki/wiki/threads/organizational-frameworks-for-ai-adoption.md) and [`ai-maturity-measurement-comparison`](/Users/witoldtenhove/Projects/ai-wiki/wiki/threads/ai-maturity-measurement-comparison.md) — close into the first two synthesis pages. The "How this thread should resolve" section in the threads is already a written-out crystallization plan; v0.3 just executes them.

**Prereqs.** v0.2 (relationships carry their own `confidence`).

**Cuts vs. v2 spec.**
- No external graph DB. Graph lives in frontmatter + `.graph.json`. Revisit only if the wiki crosses ~1000 pages.
- No automatic entity extraction beyond what Claude does manually during ingest.

**Verification.**
- `wiki/.graph.json` builds cleanly; ~54 entity nodes, ~17 concept nodes, 2-5 edges per node.
- Quartz build green; relationship panel renders; no broken links.
- `wiki/syntheses/` is no longer empty — at least one synthesis page closes one of the open threads, citing the thread + 5+ source pages.
- `index.md` Syntheses section drops the "(empty)" placeholder.

---

## v0.4 — Automation hooks (the bookkeeping cliff drops)

**Goal.** Move from "user remembers to ask for lint" to "lint runs on session-end automatically." This is where v2's promise of near-zero maintenance actually lands.

**Lands.** Cluster 4 (automation hooks) most of it — on-new-source / on-session-start / on-session-end / on-edit. Defer scheduled jobs to v0.5. Cluster 5 (quality / self-correction) partial — hook-driven self-healing for cheap cases (orphan detection, broken xref repair).

**Schema changes — `CLAUDE.md` adds §Hooks.**
- Hard rule: hooks may write to `log.md` and lint reports; hooks may NOT edit any `wiki/**/*.md` content page without explicit user approval in-session. Encoded in CLAUDE.md as a non-negotiable.
- New log entry convention: prefix `auto-` for hook-fired operations (`auto-lint`, `auto-supersession-check`).

**Tooling.**
- `.claude/settings.json` gains a `hooks` block:
  - `SessionStart` → `scripts/session-start.mjs`: load `wiki/index.md` head, last 10 `log.md` entries, list of `status: stale` pages, list of `confidence < 0.5` pages, into the conversation context.
  - `Stop` → `scripts/session-end.mjs`: diff staged wiki changes, append a single `log.md` entry summarizing the session.
  - `PostToolUse` filter on `Edit|Write` matching `wiki/**/*.md` → `scripts/lint-page.mjs <file>`: checks frontmatter contract, broken wikilinks, missing required sections, the v0.3 frontmatter-relationship-must-have-body-wikilink rule.
- New scripts under `scripts/`:
  - `session-start.mjs`, `session-end.mjs`
  - `lint-page.mjs` (single-file lint, fast)
  - `lint-orphans.mjs` (whole-wiki orphan scan)
  - `repair-xrefs.mjs` (read-only proposer; outputs diffs to stdout, doesn't apply)
- The session-end hook also calls `scripts/graph-export.mjs` from v0.3 so `.graph.json` stays current.

**Migration.** Minimal — one-time pass to make sure every page already passes `lint-page.mjs` so the hook doesn't fire warnings on unrelated edits.

**Prereqs.** v0.2 (so session-start can highlight low-confidence pages), v0.3 (so hooks have a current graph).

**Cuts vs. v2 spec.**
- No on-query hook yet (file-back-as-page is human-judgment, not a hook target).
- No scheduled retention decay (deferred to v0.5).
- Hooks remain read-mostly + log writes only.

**Verification.**
- Stop a session mid-edit; reopen Claude; SessionStart injects staged-changes summary and last log entries.
- Save a page with a deliberately broken `[[wikilink]]`; PostToolUse lint surfaces it pre-commit.
- `log.md` contains `auto-lint` entries with timestamps.

---

## v0.5 — Hybrid search + retention/forgetting

**Goal.** At ~93 pages and growing, `index.md` is starting to creak (v2 says scale features kick in past 100-200 pages). Add real search before flat index actually breaks. Land the long-promised retention curve, now that hooks can run it on schedule.

**Lands.** Cluster 3 (hybrid search) full — qmd or equivalent (BM25 + vector + RRF), with graph traversal as the third stream from v0.3. Cluster 1 remainder — Ebbinghaus retention, scheduled lint, decay surfaces. Cluster 4 remainder — scheduled hooks. Cluster 5 down-payment — mechanical quality_score (LLM-judged version comes in v0.6).

**Schema changes — `CLAUDE.md` adds §Retention and updates §Lifecycle.**
- New frontmatter on concepts/entities: `accessed_at: YYYY-MM-DD` — bumped by SessionStart hook when the page is read into context. This is the reinforcement signal.
- New CLAUDE.md §Retention: simple curve `effective_confidence = stored_confidence * exp(-days_since_access / tau)` with tau ≈ 90 days for concepts, 365 for entities, never decays sources. Surfaced via lint — never auto-deletes, never auto-rewrites.
- New `quality_score: 0.0–1.0` field on concepts + syntheses. Lint computes mechanically: structure (required sections present?) + citation density (each major claim near a `[[source]]`?) + cross-consistency (no contradictions with linked pages without a Debates section?).
- CLAUDE.md gains §Search: rule "for any query that would touch >5 pages from `index.md`, run qmd first to narrow to top 10."

**Tooling.**
- Install qmd; configure index over `wiki/`. Either CLI shell-out or MCP server (MCP is cleaner — pick that if available).
- Scheduled hook (cron-style or `/loop` invocation if no cron in environment): daily run that touches `accessed_at` on referenced pages, surfaces decay candidates, **proposes** stale-marking via log entry but doesn't apply.
- New script `scripts/quality-score.mjs`: structure check, citation check, consistency check. Writes `quality_score` and `quality_notes` to frontmatter (this is the only auto-write from a hook in the whole rollout — and it's a derived field, not editorial content).

**Migration.**
- One-time qmd index build (minutes).
- Seed `accessed_at` from each page's `last_confirmed`.
- Compute `quality_score` for all 17 concepts; expect 2-3 below threshold needing structural cleanup. Cleanup happens in v0.5 itself.

**Prereqs.** v0.4 (hooks fire the schedule).

**Cuts vs. v2 spec.**
- Quality scoring stays mechanical here. LLM-as-judge defers to v0.6.
- Retention is read-only — no auto-deletion, ever. v2's "moved to a bottom drawer" = "appears in lint output, not on the homepage."

**Verification.**
- qmd `query "jagged frontier"` returns the Dell'Acqua source + jagged-frontier concept + relevant entities, fused-rank.
- Daily lint produces a "decay candidates" list as a log entry; nothing changes on those pages.
- All concept pages have `quality_score`; bottom 3 cleaned up.

---

## v0.6 — Crystallization + LLM-as-judge quality

**Goal.** Make exploration itself a first-class source. Every closed thread becomes a synthesis. Every query worth filing back is filed back. Quality is now scored by reasoning, not just structure.

**Lands.** Cluster 8 (crystallization) full — thread → synthesis is a named, hooked, instrumented operation, plus extracted lessons. Cluster 5 remainder — LLM-as-judge quality scoring + contradiction-resolver-as-proposer.

**Schema changes — `CLAUDE.md` adds §Crystallization and §Quality review.**
- New named operation **crystallize**: closed thread → synthesis page → extracted lessons under `wiki/lessons/`. Each lesson is `type: lesson`, ≤200 words, one canonical claim, source list, inherits lifecycle fields from v0.2. Lessons decay aggressively (tau ≈ 60 days).
- §Quality review: a second-pass Claude API call with reviewer prompt evaluates each new/edited concept/synthesis against rubric; score lands in `quality_score`, notes in `quality_notes`. Replaces the mechanical scorer from v0.5 for these page types (entities still use mechanical).
- Contradiction resolver: when supersession-check finds a candidate, it produces a **proposed diff** in `log.md` (not an edit). Human approves before any page change.

**Tooling.**
- New `/crystallize <thread-slug>` slash command in `.claude/commands/`.
- `scripts/judge-quality.mjs` — Claude API call with reviewer prompt; writes back `quality_score` and `quality_notes`.
- Hook addition (extends v0.4 set): on session-end, if a `type: thread, status: open` page hasn't been edited in 14 days but its referenced sources have grown, propose closing/crystallizing in the session-end log entry.

**Migration.**
- Crystallize the two threads closed in v0.3 *again* under the new operation if needed (the v0.3 syntheses become the baseline; v0.6 adds the lessons extraction).
- LLM-judge pass over all 17 concepts and any syntheses; expect 3-5 needing rewrites.

**Prereqs.** v0.3 (synthesis schema), v0.4 (hooks), v0.5 (quality_score field exists).

**Cuts vs. v2 spec.**
- LLM-judge runs on edits + on-demand, not nightly over the whole wiki (cost).

**Verification.**
- `wiki/lessons/` directory exists with at least 3-5 lessons extracted from the two crystallized threads.
- A lesson page is reachable via graph view from its parent concept.
- `quality_score` distribution is plausible (most pages 0.7-0.9, outliers <0.5 with cleanup tickets).

---

## v0.7 — Output formats + privacy/scoping

**Goal.** Stop forcing every answer into a markdown page. Land the small bits of governance that actually matter for a single user.

**Lands.** Cluster 9 (output formats) full — comparison tables, timelines, dep graphs, Marp decks, JSON/CSV exports — as **slash-command templates**, not auto-generated artifacts. Cluster 7 remainder — filter-on-ingest stub, shared/private scoping, bulk-ops governance via `log.md`. Cluster 6 partial — only `scope: shared|private` is kept; mesh-sync is deferred indefinitely.

**Schema changes.**
- New frontmatter `scope: shared | private` (default `shared`; private pages excluded from `npm run build`, still visible in Obsidian).
- New frontmatter on sources `sensitive: true` → triggers ingest-time filter.
- Bulk ops governance: any operation touching >10 pages must log as `bulk-refactor | <intent>` with affected slug list and reversibility note. Codify the precedent established in the v0.2 migration.

**Tooling.**
- New extension `extensions/exclude-private.ts`: drops `scope: private` pages from the Quartz build.
- New slash commands in `.claude/commands/`:
  - `/compare <a> <b>` — comparison table.
  - `/timeline <concept>` — markdown or Mermaid timeline.
  - `/marp-deck <synthesis>` — generate Marp slides from a synthesis page.
  - `/export-csv <query>` — JSON/CSV export from the graph + qmd.
  Each is a templated output recipe Claude follows, not infrastructure.
- `scripts/ingest-filter.mjs` — regex-based PII/secret strip on raw markdown before Claude reads it. Conservative defaults; configurable in CLAUDE.md.

**Migration.** Minimal — `scope: shared` is default; nothing changes for existing pages until something is marked private.

**Prereqs.** v0.4 (hooks fire ingest-filter), v0.6 (synthesis pages give Marp something to render).

**Cuts vs. v2 spec.**
- No mesh sync, no work coordination, no shared/private *promotion* workflow. Revisit only if a second user appears.
- No JSON/CSV export "infrastructure" — slash commands ask Claude to write the right shape and stop.

**Verification.**
- A test page marked `scope: private` is invisible on the published Quartz site, visible in Obsidian, queryable by Claude.
- One Marp deck builds from a synthesis page.
- `ingest-filter.mjs` passes on a planted-secret fixture.

---

## v0.8 — Plan operation: gap-driven research direction

**Goal.** Promote *what to research next* from an ad-hoc human question to a first-class operation alongside ingest / query / lint / synthesize. Reads the wiki + the graph and produces a prioritised `todos/` folder of next-research workstreams. Sourced from the InfraNodus skill (Phase 10 PLAN), which is the only upstream that has it; closes a real gap none of v1 / v2 address.

**Lands.** The fifth operation. Nothing from the original v2 cluster list — this is the synthesis-driven addition.

**Schema changes — `CLAUDE.md` adds §Plan and updates §Operations.**
- New named operation **plan**: read `wiki/index.md`, `wiki/.graph.json`, the most recent N log entries, optionally any InfraNodus gap-analysis exports under `output/`; produce a prioritised todo list.
- `wiki/log.md` permitted-ops enum gains `plan` (alongside existing `ingest | query | lint | synthesize | refactor | bulk-refactor`).
- New top-level folder `todos/` (sibling of `wiki/`, `raw/`, `extensions/`). One markdown file per workstream. Schema:
  ```yaml
  ---
  title: <workstream title>
  status: open | in-progress | done | abandoned
  priority_type: content-gap | weak-coverage | empty-section | naming-gap | source-to-find | synthesis-needed
  created: YYYY-MM-DD
  deadline: YYYY-MM-DD     # optional
  derived_from: lint | gap-analysis | thread-aging | manual
  ---
  # <title>
  ## Why this matters
  <one paragraph; cite the gap or analysis output that flagged it>
  ## Tasks
  - [ ] <task>
    - <sub-detail; reference wiki pages via [[wikilinks]]>
  ```
- §Plan prose names six priority types, taken from InfraNodus's Phase 10 matrix (content-gap, weak-coverage, empty-section, naming-gap, source-to-find, synthesis-needed). Closed vocabulary so lint can validate it.
- Each completed todo file gets `status: done` and a body-bottom "Outcome" note linking to the wiki page(s) that closed it. Don't delete — `todos/` is a record of intent, not a kanban.

**Tooling.**
- New slash command `/plan` in `.claude/commands/`: invokes the plan operation, asks the user which gaps to convert into todos (multi-select), writes the files.
- New script `scripts/detect-gaps.mjs` — walks `wiki/.graph.json` for disconnected clusters (modularity-based heuristic), low-`source_count` concepts, empty subfolders, threads that have been open >30 days. Outputs a ranked candidate list to stdout. Read-only.
- Optional integration: if InfraNodus MCP server is configured, plug its `generate_knowledge_graph` output into `detect-gaps.mjs` as an additional stream (RRF over local + InfraNodus signals).
- `scripts/seed-todos.mjs` — supervised migration helper: take the candidate list from `detect-gaps.mjs`, prompt for keep/discard per candidate, scaffold one todo file per kept item. Never auto-writes.

**Migration.** One-time: generate the first `todos/` set from current wiki state. Expected output at 93 pages: 5–10 candidate workstreams, of which 3–5 survive triage.

**Prereqs.** v0.3 (the graph exists), v0.5 (low-confidence and decay candidates are surfaceable), v0.6 (lessons exist as targets for synthesis-needed gaps).

**Cuts vs. InfraNodus skill.**
- No `.plan/` reminder/Telegram tracking layer — keep todos in markdown, lean on git for tracking. The InfraNodus skill suggests `/actionize` for Telegram; defer indefinitely.
- No InfraNodus `ontology-creator` integration. This repo's typed `relationships:` + `.graph.json` already serve the role InfraNodus's append-only ontology files do; adding a second source of truth would introduce drift.
- Deadlines are optional, not enforced.

**Verification.**
- `/plan` runs end-to-end on the current wiki, producing ≥3 todo files in `todos/`.
- One todo file is closed (`status: done` + Outcome note linking to the page that addressed it) and the closure is logged in `log.md` as `plan | closed <todo-slug>`.
- A new `op: plan` entry in `log.md` records the planning session itself.

---

## v0.9 — Acquire/Process refactor: name the two phases of ingest

**Goal.** Make explicit what the repo already half-does: ingest is two operations, not one. *Acquire* touches `raw/` only (fetch / convert / place into typed subfolders); *Process* reads `raw/` and writes `wiki/`. Schema-only refactor — no new tooling beyond formalising the contract that the `youtube-transcript-skill` already satisfies.

**Lands.** A schema clarification sourced from the InfraNodus skill (Phases 8 + 9). Lets future skills (PDF→markdown, web-clipper integration, podcast transcription) slot into a named pattern instead of inventing a new convention each time.

**Schema changes — `CLAUDE.md` splits §Ingest into §Acquire and §Process.**
- §Acquire codifies:
  - Typed `raw/` subfolders (already de-facto in this repo): `articles/`, `assets/`, `books/`, `images/`, `lectures/`, `papers/`, `reports/`, `videos/`. The contract: organise by source **type**, not topic — different formats have different ingest rules.
  - Convert-before-land: PDFs → markdown before landing in `raw/papers/` (originals preserved in `raw/assets/`).
  - The acquire-time skill contract: a skill emits a raw file with a canonical YAML frontmatter at `raw/<type>/<slug>.md`. The `youtube-transcript-skill` is the reference implementation; the existing §"Source-page conventions specific to videos" already specifies the field-mapping table.
  - Acquire is **re-runnable** — re-acquiring the same source from a better channel (e.g. higher-quality transcript) replaces the raw file; the wiki source page is not touched until §Process re-runs.
- §Process is the existing §Ingest steps 1–9, unchanged in substance — just renamed and now starting "After §Acquire has landed a raw file…". The four pre-flight checks (scope, identity, honest scoping) remain at the head of §Process.
- §Ingest becomes a one-liner pointer: "Ingest = Acquire + Process. See §Acquire and §Process."
- `log.md` permitted-ops gains `acquire` as an op (distinct from `ingest`, which stays as the umbrella for sessions that do both). Most sessions stay `ingest`; `acquire` is used only when the session lands raw files but defers processing.

**Tooling.** None new. This is a documentation refactor — every existing tool and skill already fits one side of the split.

**Migration.**
- One pass over `CLAUDE.md`: split §Ingest, move the four pre-flight checks under §Process, lift the video-frontmatter contract under §Acquire as the canonical "what an acquire-time skill produces."
- Log entry: `refactor | v0.9 — split §Ingest into §Acquire + §Process`.
- No wiki content changes.

**Prereqs.** None — this is paper-only.

**Cuts vs. InfraNodus skill.**
- No 10-phase guided scaffolding (Discover / Scope / Structure / Schema / Workflows / Tooling / Scaffold). That's an onboarding skill for *new* wikis. This repo is already instantiated.
- No `infranodus/` folder of append-only ontology files. Typed `relationships:` + `.graph.json` cover the same job from a single source of truth.

**Verification.**
- `CLAUDE.md` reads cleanly with §Acquire + §Process replacing §Ingest.
- The `youtube-transcript-skill` documentation (`.claude/skills/youtube-transcript-skill/SKILL.md`) references §Acquire as the contract it satisfies.
- A new acquire-only session (e.g. land a paper as `raw/papers/<slug>.md` without processing) leaves the wiki untouched and logs as `acquire | <slug>`.

---

## v0.10+ — Deferred

Revisit only if forced.
- **Mesh sync** (cluster 6 remainder): if a coauthor or second machine appears.
- **Consolidation tier infrastructure** (cluster 1 deferred piece): if the wiki crosses ~500 pages and the four-tier model starts paying its weight.
- **External graph DB**: if `.graph.json` exceeds a few MB and traversal queries get slow.
- **On-query hook** (cluster 4 remainder): if the user finds they're forgetting to file good answers back.
- **Retention auto-deletion** (v2 forgetting curve, harder form): v0.5 lands decay-as-lint-signal; auto-deletion or auto-archiving is deferred indefinitely. Knowledge that has decayed off the homepage and is invisible to lint is already "in the bottom drawer" in v2's framing.
- **InfraNodus MCP integration for richer gap analysis**: v0.8 names a stub hook; promote only if the user is running InfraNodus alongside Obsidian anyway and the local detector misses obvious gaps.
- **Telegram / external reminder integration for `todos/`**: InfraNodus's `/actionize` companion. Defer; git + markdown todos with deadlines is sufficient at single-user scale.

---

## Cross-version risks

1. **Bulk migration consistency (v0.2, v0.3).** Adding confidence to 71 pages or relationships to 54 entities is the single most likely place to introduce silent drift — half rich, half rubber-stamped 0.7. Mitigation: supervised batches of ~10, treat the migration itself as multi-session work, never a single-shot script.
2. **Quartz link resolver vs. typed-relationships frontmatter (v0.3).** Quartz crawls body wikilinks; YAML object relationships are invisible to it. If relationships are ever encoded as `[[...]]` strings inside frontmatter, partial resolution + silent broken links result. The split-layer rule ("typed in frontmatter, navigable in body, both required") is load-bearing — `lint-page.mjs` (v0.4) enforces it.
3. **Hook-driven auto-edits (v0.4-v0.6).** Strong temptation to let session-end auto-mark stale or auto-rewrite low-quality pages — exactly the wrong move. A hook that silently changes content destroys the "Claude owns the wiki, user owns direction" contract. Mitigation: hard CLAUDE.md rule, encoded from v0.4 onward — hooks may write to `log.md` and lint reports only; the only frontmatter-write exception is the derived `quality_score` field in v0.5/v0.6.

## Critical files to touch

Each version edits these (in order of frequency):
- [/Users/witoldtenhove/Projects/ai-wiki/CLAUDE.md](/Users/witoldtenhove/Projects/ai-wiki/CLAUDE.md) — every version adds a section before its tooling lands.
- [/Users/witoldtenhove/Projects/ai-wiki/wiki/log.md](/Users/witoldtenhove/Projects/ai-wiki/wiki/log.md) — every migration and bulk-op logs here.
- [/Users/witoldtenhove/Projects/ai-wiki/wiki/index.md](/Users/witoldtenhove/Projects/ai-wiki/wiki/index.md) — synthesis section (v0.3), lesson section (v0.6), private-scope handling (v0.7).
- [/Users/witoldtenhove/Projects/ai-wiki/quartz.config.ts](/Users/witoldtenhove/Projects/ai-wiki/quartz.config.ts) — register new extensions in v0.2, v0.3, v0.7.
- [/Users/witoldtenhove/Projects/ai-wiki/extensions/](/Users/witoldtenhove/Projects/ai-wiki/extensions/) — new files added in v0.2, v0.3, v0.7. Pattern follows [`inject-type-tags.ts`](/Users/witoldtenhove/Projects/ai-wiki/extensions/inject-type-tags.ts).
- [/Users/witoldtenhove/Projects/ai-wiki/.claude/settings.json](/Users/witoldtenhove/Projects/ai-wiki/.claude/settings.json) — hooks block in v0.4, scheduled hook in v0.5.
- New `/Users/witoldtenhove/Projects/ai-wiki/scripts/` directory created in v0.2 (`lint-confidence.mjs`); each subsequent version adds scripts to it.

Per-version migration targets:
- v0.2: 17 concepts under `wiki/concepts/` + 54 entities under `wiki/entities/` (71 pages).
- v0.3: same 71 pages gain relationships; both threads in `wiki/threads/` close into new files in `wiki/syntheses/`.
- v0.6: new `wiki/lessons/` directory.
- v0.8: new top-level `todos/` directory (sibling of `wiki/`, not inside it); 3–5 seeded workstreams.
- v0.9: schema-only refactor of `CLAUDE.md` §Ingest → §Acquire + §Process; zero content pages touched.

## Verification strategy across versions

After each version lands:
1. `npm run build` succeeds with no warnings.
2. `npm run serve` shows the new behavior on a representative page (e.g. stale banner in v0.2; relationship panel in v0.3; rendered Marp deck in v0.7).
3. `lint-confidence.mjs` (v0.2) / `lint-page.mjs` (v0.4+) passes on all `wiki/**/*.md`.
4. The version's acceptance test runs (e.g. v0.3 closes a thread into a synthesis; v0.6 produces lessons; v0.7 hides a private page).
5. A `log.md` entry records the version landing as `bulk-refactor | v0.X <theme>`.

## Sequencing recommendation

Treat each version as one or two focused sessions, not one big push. Suggested cadence: v0.2 over 2-3 sessions (because of the bulk migration), v0.3 over 2 sessions, v0.4 in 1 session, v0.5 in 2 sessions (qmd install + retention), v0.6 in 2 sessions, v0.7 in 1 session, v0.8 in 1-2 sessions (gap-detector + first todos seeding), v0.9 in 1 session (CLAUDE.md refactor only). Each version is independently shippable — pause between any two and the wiki keeps working.

Note on v0.8 vs v0.9 ordering. v0.9 is paper-only and could land at any point — it has zero prerequisites. Put it after v0.8 because the Plan operation is a natural place to flush out which raw sources are *acquired but not processed* (a gap type v0.8's detector should surface), and that gap is more legible once §Acquire is named as a distinct step. If a future skill is being authored that needs the contract before v0.8 ships, swap them — no other version cares about the order.
