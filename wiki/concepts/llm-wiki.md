---
type: concept
aliases: ["LLM Wiki", "LLM-Wiki", "llm wiki", "Karpathy's LLM Wiki", "LLM-maintained wiki", "compounding wiki"]
tags: [llm-wiki, knowledge-compilation, three-layer-architecture, ingest-query-lint, agent-memory, claude-md, knowledge-compounding, agentic-knowledge-base]
confidence: 0.91
last_confirmed: "2026-05-17"
accessed_at: "2026-05-17"
source_count: 7
relationships:
  - type: part-of
    target: agent-harness
    via: "the LLM Wiki is one of several persistent-context substrates an agent harness reads from — distinguished from vector-RAG (no compounding) and fat-skills (action-oriented) by its compile-and-maintain semantics"
  - type: instance-of
    target: software-3.0
    via: "Karpathy positions the LLM Wiki within his Software 3.0 framing — the wiki is an artifact the LLM (as programmer) writes and maintains; the human (as architect) sets schema and curates sources"
  - type: authored-by
    target: Andrej Karpathy
    via: "Karpathy is the upstream-spec author — the LLM Wiki gist (April 4, 2026) is the foundational artifact; 17 million views, 5,000 stars, 4,282 forks within days"
quality_score: 1
---

# LLM Wiki

The **LLM Wiki** is a knowledge-management pattern named by **[[Andrej Karpathy]]** in a GitHub Gist published 4 April 2026 (which hit 17 million views, 5,000 stars, and 4,282 forks within days). In the pattern, an LLM compiles raw source materials into a persistent, interlinked markdown wiki that the LLM owns and maintains — *"knowledge compounds; the synthesis, the cross-references, the identified contradictions are built once and kept current, not re-derived on every query."* The pattern is **the foundational architecture for this very repository** (see [`llm-wiki.md`](../../llm-wiki.md), [`llm-wiki-v2.md`](../../llm-wiki-v2.md), and [`CLAUDE.md`](../../CLAUDE.md) at the repo root).

The wiki holds five sources engaging this concept substantively, from five distinct vantages:

- **The upstream spec**: [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026 (Sequoia AI Ascent)]] — *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles ... anytime I see a different projection onto information, I always feel like I gain insight."* Karpathy's first-person continued use of the pattern, plus the gist itself (cited via the explainer articles below) is the upstream spec.
- **The clearest explainer**: [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026 (Medium)]] — three-layer architecture (raw / wiki / schema); three operations (ingest / query / lint); working Python implementation; honest comparison vs RAG with limitations named explicitly (scale ceiling, hallucination baking, ingest cost).
- **The comparative-architecture treatment**: [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026 (AI Advances)]] — places LLM Wiki alongside RAG and GBrain in a unified decision framework; predicts hybrid convergence (2023 RAG → 2025 Wiki+Skills emerge → 2026+ convergence); notes Claude Code already implements partial-convergence.
- **The vendor implementation (server-side / durable end of the spectrum)**: [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase / ex-brain 2026]] — first-vendor implementation worked example using seekdb (AI-native database); demonstrates compiled-truth + timeline-extraction + entity-linking + hybrid-search; MCP-server-as-LLM-Wiki-interface for Claude Code integration.
- **The single-author extension (browser-only / session-scoped end of the spectrum)**: [[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki|Mysore 2026 (Medium)]] — proposes a **5W1H Wiki Frame** (Who / What / When / Where / Why / How) the LLM auto-populates from each document before any query, plus three UI patterns: *Autonomous Scaffolding* (LLM-as-Architect not user-as-Clerk), *Contrast Engine* (side-by-side Plain-vs-WikiZZ output), *LLM Jury* (evaluator LLM judges the delta). Live demo at [vishalmysore.github.io/lllmwikiZZ](https://vishalmysore.github.io/lllmwikiZZ/); zero-server / static-first / `FileReader` parsing / Cloudflare Worker CORS proxy to NVIDIA NIM + Anthropic + Gemini providers. **Source-quality flags**: single-author experiment (anecdotal per [§Lifecycle](#lifecycle)); engagement = 1 clap at fetch time; "persistent" is session-scoped not durable. Coins **"Context Debt"** and **"transient RAG"** as vocabulary candidates — both deferred to second-source mention.
- **The knowledge-graph augmentation (KG-as-attention-direction)**: [[2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus|Nodus Labs 2026 (YouTube tutorial, 11 April 2026)]] — *published 7 days after Karpathy's gist*, the wiki's **earliest third-party "fix" / extension proposal**. Diagnosis: *"The LLM Wiki has structure, but is not aware of itself"* — flat-prompt queries still produce generic outputs because the LLM extracts concepts then completes with most-probable continuation. Fix: layer an **InfraNodus** knowledge graph on top of the wiki's `concepts/` folder, with three integration depths (external tool / MCP-server-callable from Claude / KG-integrated into wiki workflow with `infranodus/` folder of per-session ontology graphs as **"living memory"**). The novel mechanism — **gap-analysis as attention-direction**: identify cluster pairs with low betweenness, paste the gap-prompt back to Claude with the underlying source extracts, ask for cluster-bridging insights. *"I point the LLM's attention to the gap that exists. I provide the underlying structure."* **First wiki source on KG-as-attention-direction primitive** (distinct from KG-as-retrieval-substrate — see [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]]). Ships a **Claude skill** (`infranodus/skills/skill-llm-wiki`) as a packaged operational form. Vendor-sponsored (cap 0.75 confidence per Lifecycle rule).

The six sources now span **the full architectural spectrum** of LLM-Wiki implementations: from **privacy-maximalist / browser-only / session-scoped** (Mysore's WikiZZ) through **KG-attention-augmented** (Nodus Labs InfraNodus) and **MCP-server-with-seekdb** (OceanBase ex-brain) to **durability-maximalist / Postgres-pgvector / 21-cron-jobs / 17,888-page** (Liu's GBrain, which Liu positions as a distinct architecture but which shares the LLM-compiles-knowledge premise with the LLM-Wiki pattern).

## Working definition

Composite from the four wiki sources plus the upstream repo specs:

> A knowledge management system where an LLM (not the human) compiles raw source documents into a persistent, interlinked markdown wiki; maintains cross-references across pages; flags contradictions; and periodically lints for orphans, stale claims, and missing concepts. The human curates sources and sets the schema (a configuration file like CLAUDE.md). The LLM owns the wiki layer entirely.

Karpathy's canonical analogy ([[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]):

> *"Your files are raw ingredients. The LLM Wiki is the cooked meal. With RAG, you cook every time you are hungry."*

## The three-layer architecture

The wiki sources converge on a three-layer split with explicit ownership semantics:

| Layer | Contents | Ownership |
|---|---|---|
| **Layer 1 — Raw sources** | Articles, papers, transcripts, bookmarks. PDFs, images, data files. | **Immutable.** LLM reads; never modifies. Human source of truth. |
| **Layer 2 — The wiki** | LLM-generated markdown: summaries, entity pages, concept pages, comparisons, synthesis | **LLM-owned entirely.** Human reads; LLM writes and maintains. |
| **Layer 3 — The schema** | Configuration file (CLAUDE.md, AGENTS.md) telling the LLM how to maintain the wiki: naming conventions, cross-referencing rules, what counts as a contradiction | **Co-evolved** by human and LLM as workflow stabilises. |

The three-layer architecture is **named consistently across all three explainer articles** ([[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]], [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]], [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase 2026]]) — strong evidence that the pattern has stabilised at the architectural-vocabulary level.

## The three core operations

The LLM Wiki pattern has three named operations, repeated across all wiki sources:

### Ingest — compiling new knowledge

Drop a new source into raw/. The LLM:
- Reads the source.
- Discusses key takeaways with the user.
- Writes a summary page.
- Updates every relevant entity, concept, and topic page across the wiki — *"a single article about a new Tesla model might update the Tesla page, the battery technology page, the EV market overview, and the manufacturing process page — all in one pass"* ([[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]).
- Updates `index.md` with the new page entry.
- Appends to `log.md`.

[[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]]'s observation: *"A single ingest typically touches 10–15 wiki pages — adding cross-references, flagging contradictions, updating entity profiles."* Convergent with this repo's CLAUDE.md (*"Touching 15 files in one ingest is normal and expected"*).

### Query — navigating compiled knowledge

When you ask a question:
- LLM reads `index.md` first to locate relevant pages.
- Drills into the relevant pages.
- Synthesises an answer with citations to specific wiki pages.
- **Good answers get filed back into the wiki as new pages** — *"your explorations compound in the knowledge base"* ([[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]).

### Lint — health-checking the wiki

Periodically, the LLM scans for:
- Contradictions between pages.
- Stale claims superseded by newer sources.
- Orphan pages (no inbound links).
- Concepts mentioned but lacking their own page.
- Missing cross-references and data gaps.

[[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] on why this works: *"This is the maintenance operation that humans consistently fail to do at scale. LLMs don't get bored. They will update fifteen cross-references without complaint."*

The wiki's own `wiki/log.md` follows Karpathy's *"prefix entries with `## [DATE] operation | title`"* convention — making the entire operation history queryable with `grep '^## \[' wiki/log.md | tail -5`.

## Why it compounds — the compounding mechanism

The compounding effect distinguishes LLM Wiki from RAG ([[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]]):

| Mode | What happens when a new document arrives |
|---|---|
| **RAG** | Retrieves 3 chunks per query; fragments of the paper; no connections preserved; *"never compounds"* |
| **LLM Wiki** | Updates 15 pages per ingest; each richer than before; *"relationships strengthened"* |

The mechanism is **synthesis-at-ingest-time vs synthesis-at-query-time**. RAG defers synthesis to query time (each query rediscovers cross-document relationships). LLM Wiki front-loads synthesis to ingest time (relationships are computed once, persisted, and re-read by every future query). [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]: *"This is the 'compilation' step — the heavy cognitive lift happens once at ingest, not on every query."*

## Honest comparison vs RAG — the systematic tradeoff matrix

[[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]'s ten-dimension comparison:

| Dimension | RAG | LLM Wiki |
|---|---|---|
| Knowledge accumulation | ✗ Stateless | ✓ Stateful |
| Cross-document synthesis | ✗ Rediscovered every query | ✓ Pre-compiled at ingest |
| Contradiction detection | ✗ Not tracked | ✓ Flagged at ingest + lint |
| Retrieval explainability | △ "Close in embedding space" | ✓ Specific page citations |
| Infrastructure required | Embedding model + vector DB + re-indexing | ✓ Filesystem + LLM API |
| Scale (large corpora) | ✓ Millions of documents | ✗ ~Hundreds of sources |
| Query latency | ✓ Fast vector search | △ Depends on wiki size + context |
| Real-time / streaming | ✓ Re-index on update | ✗ Re-ingest with LLM passes |
| Human readability | ✗ Vector DB not human-readable | ✓ Plain markdown |
| Multi-user / enterprise | ✓ Battle-tested | ✗ No RBAC / ACID / concurrency |
| Hallucination risk | △ Isolated to query time | ✗ Errors baked at ingest can propagate |

The systematic feature-by-feature contrast is the wiki's load-bearing reference for when-to-use-which.

## What Karpathy quietly glossed over — the named limitations

[[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]'s honest treatment of three limitations:

### The scale ceiling

Karpathy runs his wiki at *"roughly 100 articles and 400,000 words."* At that size, the index file fits in context; navigation is essentially a directory listing. *"The 'bye bye RAG' framing quietly assumes that what works at 100 pages works at 10,000. It does not. Once the wiki outgrows what fits in context, you need a real retrieval substrate underneath it — and the cheapest way to build that substrate is, ironically, vector embeddings."*

The wiki's first **named scale-ceiling caveat**. For this repository (currently ~50 sources / ~78 entities / ~25 concepts), the ceiling is approached but not reached. Future-growth planning would benefit from explicit awareness.

### Hallucination baking

> *"With RAG, the model goes back to original documents on every query. Even if it makes a mistake in one answer, the next query has a chance to correct it because the source is still the ground truth. The wiki changes this fundamentally. The LLM reads documents, creates pages, links them — and stores that synthesis as authoritative knowledge. LLMs sometimes fill gaps or make assumptions. In RAG, that's a wrong answer. In the wiki, that's a wrong page that every future query trusts. Organized, persistent mistakes are harder to spot than individual errors."*

The wiki's first **named risk: persistent-mistake-amplification**. Design implication for lint: scan for plausible-but-wrong claims specifically, not just orphans and contradictions.

### Ingest is not free

> *"The wiki feels efficient at query time because the heavy work is already done. But that work doesn't disappear — it moves to ingest. Every new document requires multiple LLM passes to process, summarize, link, and merge into the existing structure. If your data changes frequently, re-ingesting to keep the wiki current is expensive. RAG handles fresh data better because it always retrieves from the latest source directly."*

The cost-curve caveat: LLM Wiki is the wrong choice for fast-moving / streaming-data scenarios.

## Convergence prediction — the hybrid architecture

Both [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] and [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] independently predict convergence:

> *"The honest architecture for most serious knowledge systems is a hybrid. Use the LLM Wiki pattern for what it genuinely does better: compiling and maintaining synthesised knowledge ... Use vector retrieval as the substrate underneath the wiki once it outgrows context."* — Raju 2026

> *"The most capable architectures will combine all three: RAG for the retrieval layer (finding relevant content at scale), Wiki for the synthesis layer (compiling retrieved content into persistent knowledge), and skills for the action layer (operationalizing that knowledge into autonomous workflows)."* — Liu 2026

Liu's phase-timeline: **2023 RAG era → 2025 Wiki + Skills emerge → 2026+ convergence**. Three converging streams that may dissolve the three-way split.

## Claude Code as the partial-convergence-example

Liu notes ([[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]]):

> *"Claude Code already hints at this convergence. CLAUDE.md files function as a mini-wiki (persistent context that compounds across sessions). Auto-memory learns from interactions (compounding). Skills trigger workflows (action). It's not a deliberate implementation of all three patterns — but the same pressures produced the same solutions."*

This is **meta-relevant to this repository**: this very wiki operates inside Claude Code, instantiates CLAUDE.md as the schema layer, uses session-start hooks as auto-memory, and integrates Skills via the skill API. The convergence Liu predicts is partially-realised in the runtime this repo runs on.

## LLM Wiki vs GBrain (Fat Skills) — different jobs

[[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] distinguishes LLM Wiki from [[Garry Tan]]'s GBrain (which she also calls *"Fat Skills"*):

- **LLM Wiki (compile)**: knowledge compounds; *"the LLM as knowledge engineer"*. Best for deep expertise on ~1K sources.
- **Fat Skills / GBrain (act)**: knowledge acts; *"24 autonomous skills, 21 cron jobs, brain spanning 17,888 pages ... it acts on them. Autonomously."* Best for power-user autonomous-ops on ~17K pages.

GBrain is **the operational/action layer**; LLM Wiki is **the synthesis/expertise layer**. Different jobs; complementary.

## Open questions

- **The Karpathy gist itself** — referenced in three sources but not directly ingested. Primary-source target: the GitHub gist URL.
- **The scale ceiling crossing strategy** — Raju proposes vector embeddings as the substrate when the wiki outgrows context. The operational details (when to add the substrate, what kind of vector index, how to integrate it with the markdown layer) are open implementation questions for this repo's own future v0.5+ versions.
- **The 2024 RAG-failure-points paper** — Liu cites *"seven distinct failure points"*. Primary-source target.
- **Karpathy's own answer to scale and hallucination concerns** — Karpathy's gist is *"an idea file,"* not a production spec. A primary-source ingest of the gist + community-extension Q&A would substantiate.
- **LLM Wiki v2 community extensions adding retrieval layers** — Liu names this as the convergence direction. Primary-source target.
- **Enterprise LLM Wiki implementations** — Liu notes *"the implementation at enterprise scale is a semantic graph with RBAC, ACID transactions, and an LLM agent maintaining it. Different infrastructure. Same principle."* No enterprise-scale implementation source ingested yet.

## Debates and supersession

None substantive. The four wiki sources are convergent on the architecture, the operations, and the limitations. The internet's *"RAG is dead"* meta-debate is dismissed by both Raju and Liu as missing-the-point; they argue for **complement, not replace**.

## Related concepts

- [[agent-harness]] — the LLM Wiki is one of several persistent-context substrates an agent harness reads from.
- [[agentic-engineering]] — the LLM Wiki pattern operates within the agentic-engineering discipline (the LLM-as-knowledge-engineer maintains the artifact the human curates).
- [[knowledge-graphs]] — entity-linking + cross-references in the LLM Wiki are a markdown-form knowledge graph; SurrealDB / OceanBase / Neo4j convergence direction.
- [[software-3.0]] — Karpathy positions the LLM Wiki within his Software 3.0 framing.
- [[vibe-coding]] — vibe-coding raises the floor; the LLM Wiki extends the same floor-raising principle to knowledge work.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "llm-wiki")
SORT file.name ASC
```
