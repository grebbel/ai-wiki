---
type: source
kind: article
title: "RAG, LLM Wiki, or Gbrain? How Your Agent Remembers Changes Everything"
author: ["Yanli Liu"]
url: "https://aiadvances.medium.com/rag-llm-wiki-or-gbrain-how-your-agent-remembers-changes-everything"
date_published: 2026-04-27
length: "~15-min read (22 pages PDF)"
raw: "../../raw/articles/RAG, LLM Wiki, or Gbrain_ How Your Agent Remembers Changes Everything _ by Yanli Liu _ Apr, 2026 _ AI Advances.pdf"
tags: [llm-wiki, gbrain, rag, agent-memory, knowledge-architecture, fat-skills, thin-harness, decision-framework, convergence, claude-md, context-engineering]
relationships:
  - type: supports
    target: llm-wiki
    via: "the wiki's most-substantive comparative-architecture article — places LLM Wiki alongside RAG and GBrain in a unified decision framework; three-architectures × three-tradeoffs table; convergence prediction (2023 RAG → 2025 Wiki+Skills emerge → 2026+ hybrid); detailed GBrain architecture description (24 skills, 21 cron jobs, 17,888 pages, Postgres+pgvector, thin-harness/fat-skills)"
  - type: supports
    target: agent-harness
    via: "explicit thin-harness/fat-skills framing — GBrain keeps the harness to ~200 lines while the skills carry all intelligence as full-workflow markdown documents; CLAUDE.md + RESOLVER.md routing pattern named; convergent with Karpathy's harness-engineering and Bockeler's fat-context-thin-runtime"
  - type: supports
    target: knowledge-graphs
    via: "names Neo4j building knowledge layers (graph + vector + semantic) as enterprise platforms moving toward the convergence; Postgres+pgvector as GBrain's deterministic-plus-latent split substrate"
---

# RAG, LLM Wiki, or GBrain? How Your Agent Remembers Changes Everything

> Karpathy's compounding wiki, Garry Tan's autonomous brain, and the decision framework most teams skip.
>
> Three weeks ago, Andrej Karpathy posted a GitHub gist that hit 5,000 stars in days. His argument: stop using LLMs as search engines over your documents. Use them as knowledge engineers who compile, cross-reference, and maintain a living wiki. The system learns. The knowledge compounds.
>
> Later on, Garry Tan shipped GBrain — 24 autonomous skills, 21 cron jobs, and a brain spanning 17,888 pages. His system doesn't just remember things. It acts on them. Autonomously.

(Article opening, [[Yanli Liu]] on AI Advances Medium publication.)

A 15-minute Medium article by **[[Yanli Liu]]** (finance practitioner in Luxembourg; AI Advances contributor with 4.5K followers). Published 27 April 2026 — **23 days after** Karpathy's gist. **The wiki's most-substantive comparative-architecture article** on knowledge-memory patterns for AI agents, with a unified decision framework placing LLM Wiki alongside RAG and GBrain.

## TL;DR

Six substantive contributions:

1. **The three-architecture framing — RAG / LLM Wiki / GBrain — as solving different versions of the same problem**:

   | Architecture | Core verb | Scale | Compounds? | Proactive? | Context | Setup cost | Best for |
   |---|---|---|---|---|---|---|---|
   | **RAG** | Retrieve | 200K+ docs | No | No — waits | Chunks (lossy) | Low (a weekend) | Search at scale |
   | **LLM Wiki** | Compile | ~1K sources | Yes — wiki refines | No — waits | Full pages | Medium (weeks) | Deep expertise |
   | **Fat Skills (GBrain)** | Act | 17K+ pages | Partial — logs | Yes — 21 crons | Skill-scoped | High (months) | Autonomous ops |

   The wiki's **first three-architecture decision matrix** with explicit dimensions. Liu's framing: *"these architectures aren't competing. They're solving different versions of the same problem. Picking between them is a design decision, not a loyalty test."*

2. **RAG's three critical failure points — the wiki's most-systematic enumeration**:
   - **The chunking problem**: 30-page spec gets fragmented; relationships destroyed; *"the chunk that mentions a compliance requirement lands in one vector. The chunk that explains why that requirement exists lands in another."*
   - **The re-derivation problem**: every query starts from scratch. *"Karpathy put it sharply: 'RAG rereads the same books for every exam, never actually learning the material.'"*
   - **The passivity problem**: *"RAG waits for you to ask. It never notices that the document it indexed last Tuesday contradicts the one it indexed today."*

   Cites a 2024 research paper mapping *seven distinct failure points* in production RAG. The wiki's first **citation of an academic-paper failure-point taxonomy for RAG**. Open primary-source target.

3. **The LLM Wiki three-layer architecture, named explicitly**:
   - **Layer 1 — Raw sources**: PDFs, articles, transcripts, bookmarks. Immutable. *"The LLM reads them but never modifies them."*
   - **Layer 2 — Wiki pages**: human-readable markdown, cross-linked, continuously refined. *"The LLM owns this layer entirely."*
   - **Layer 3 — Schema**: a configuration file (CLAUDE.md). *"Tells the LLM how to maintain the wiki: naming conventions, cross-referencing rules, what counts as a contradiction."*

   *"A single ingest typically touches 10-15 wiki pages — adding cross-references, flagging contradictions, updating entity profiles."* This is the wiki's first **systematic statement of the cross-cutting-touch property** of LLM Wiki ingest — convergent with this repo's own CLAUDE.md (*"Touching 15 files in one ingest is normal and expected"*).

   *"And there's a maintenance loop most people miss: the lint workflow. Periodically, the LLM audits the entire wiki — finding orphan pages with no incoming links, flagging stale claims, identifying concepts mentioned but never given their own page. The wiki stays healthy because the machine does the maintenance humans always abandon."*

4. **GBrain detailed architecture — the wiki's deepest first-party-class description**:

   - **24 autonomous skills + 21 cron jobs + 17,888-page brain repo** (vs Karpathy's ~100 pages).
   - **Postgres + pgvector** backend — deterministic data (SQL) + latent knowledge (embeddings).
   - **Built for personal AI agents** — specifically OpenClaw, Hermes, and Claude Code. README: *"Your AI agent is smart but forgetful. GBrain gives it a brain."*
   - **"Thin harness, fat skills" architecture**: harness is ~200 lines of code (model execution + read/write files + safety). All intelligence in the skills.
   - **CLAUDE.md + RESOLVER.md as routing**: RESOLVER.md dispatches user intent to skills across six categories (always-on / brain ops / content ingestion / thinking / operational / setup). **Key insight Liu names**: *"the skill descriptions themselves function as the resolver. The model reads the descriptions and matches intent automatically. No explicit routing code needed."*
   - **Fat skill = workflow contract**: each skill is *"not a prompt template, but an entire workflow: when to fire, what to check, how to chain with other skills, what quality bar to enforce."* Frontmatter includes `name`, `version`, `description` (with triggers), `tools`, `mutating`, `writes_to`.
   - **The enrich skill** (worked example): builds and maintains person/company dossiers; *"seven-step enrichment protocol that runs across three tiers — full research for inner-circle contacts, moderate effort for industry figures, light touch for entities worth tracking but not critical. Every claim requires inline [Source: ...] citations following a strict precedent hierarchy: user statements > compiled truth > timeline entries > external APIs."*
   - **Always-on layer**: `signal-detector` skill *"fires on every inbound message, running as a cheap sub-agent in parallel with the main response. It captures two things: original ideas (preserved in the user's exact phrasing, never paraphrased) and entity mentions ... Every entity it detects gets cross-linked to existing brain pages or spawns a new one. The operating principle: 'An unlinked mention is a broken brain.'"*
   - **Cron — skills that run themselves**: *"each job is deliberately thin — the prompt is literally 'Read skills/{name}/SKILL.md and run it.' All the intelligence stays in the skill file ... Jobs run on 5-minute staggered slots ... respect quiet hours (11 PM–8 AM by default) ... enforce idempotency."* Reports filed to `reports/{job-name}/{YYYY-MM-DD-HHMM}.md`.
   - **The deterministic split**: *"GBrain separates latent work (reading, synthesis, pattern recognition) from deterministic work (database writes, calculations, reproducible outputs). Mixing them is how agents hallucinate."*

5. **The convergence prediction — "where this is heading"**:

   - 2023: **RAG era**
   - 2025: **Wiki + Skills emerge**
   - 2026+: **Convergence**

   *"The three-way split won't last. The same way databases evolved from 'pick SQL or NoSQL' to hybrid systems that handle both, knowledge architectures are converging. Karpathy's LLM Wiki v2 community extensions are adding retrieval layers on top of compiled wikis — compounding meets scale. GBrain's skills already query a Postgres + pgvector backend — action meets retrieval. And enterprise platforms like Neo4j are building knowledge layers that combine graph databases, vector search, and semantic reasoning in a single access point."*

   Closing thesis: *"The question for 2026 isn't 'which architecture wins.' It's how quickly the boundaries between retrieve, compile, and act dissolve into a single knowledge operating system that does all three."*

6. **Claude Code as the working-convergence-example**:

   > *"Claude Code already hints at this convergence. CLAUDE.md files function as a mini-wiki (persistent context that compounds across sessions). Auto-memory learns from interactions (compounding). Skills trigger workflows (action). It's not a deliberate implementation of all three patterns — but the same pressures produced the same solutions."*

   The wiki's first **first-party-from-an-explainer claim that Claude Code is a partial-implementation of the converged architecture**. This is meta-relevant: this very repository operates inside Claude Code, instantiates CLAUDE.md as the schema, uses session-start hooks as auto-memory, and integrates Skills via the skill API.

## What was actually ingested

Full 22-page PDF article. Pages 18-22 are publication-footer / author-bio / related-articles; substantive content lives in pages 1-17.

## The decision framework — "what is your agent's job?"

Liu's decision tree (the article's most operationally useful artifact):

> *"Your agent retrieves answers from a large corpus. You have thousands of documents. They change regularly. ... Use RAG. It's not glamorous, but it's the architecture that scales to the corpus sizes most organizations actually have. Pair it with a reranker and you'll cover 80% of knowledge assistant use cases."*

> *"Your agent builds expertise that should compound over time. You have hundreds of sources — research papers, regulatory filings, competitor analyses, technical specs. The value isn't in any single document but in the connections between them. ... Use the LLM Wiki. Feed it your sources, let it build the cross-references, and query the compiled wiki instead of raw chunks. Your hundredth query will be significantly better than your first — something RAG can never promise."*

> *"Your agent needs to act on what it knows without being asked. You don't just want answers. You want your agent to monitor, flag, enrich, and execute. You want it running while you sleep, filing insights back into the system, triggering workflows when conditions change. ... Use fat skills. But budget for the engineering."*

The wiki's first **explicit decision-tree-by-agent-job framework** for the three-way memory-architecture choice. Liu's hybrid framing: *"The most capable architectures will combine all three: RAG for the retrieval layer (finding relevant content at scale), Wiki for the synthesis layer (compiling retrieved content into persistent knowledge), and skills for the action layer (operationalizing that knowledge into autonomous workflows)."*

## GBrain — Liu's first-party-class detailed treatment

Liu's GBrain treatment is **the wiki's deepest first-party-class description** of [[Garry Tan]]'s second open-source project (after GStack). Key details:

- **Origin**: *"GBrain wasn't designed as an enterprise product. It was built to run on personal AI agents — specifically OpenClaw, Hermes, and Claude Code. ... This is infrastructure built by the Y Combinator CEO to run his own agents, then open-sourced. That origin shapes everything about the architecture — it optimizes for one power user's workflows, not organizational deployment."*
- **Three-tier enrichment protocol** (from the `enrich` skill): full research for inner-circle / moderate for industry figures / light touch for entities-worth-tracking-not-critical.
- **Source precedence hierarchy**: user statements > compiled truth > timeline entries > external APIs.
- **Always-on signal-detector**: parallel-sub-agent on every inbound message; preserves user-exact-phrasing; *"An unlinked mention is a broken brain."*
- **Garry Tan's latest iteration**: *"Fewer fatter skills makes the resolver shorter, which itself is less context bloat. Short resolvers are better than long ones."* The trend is toward **fewer, more comprehensive skills with branching parameters** rather than many narrow ones — directly relevant to harness-design choices.

The **enterprise reality** Liu names:

> *"This architecture maps well to a specific enterprise pattern: the power user who serves as a force multiplier for their team. A senior analyst running autonomous research workflows. A product lead who needs competitive intelligence updated daily without asking for it. An engineering manager whose agent monitors deployment health and escalates autonomously. But it doesn't map to the typical enterprise deployment of 'give everyone access to a knowledge assistant.' The engineering overhead per user is too high."*

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026 (Sequoia AI Ascent)]] | Karpathy is the upstream-spec author. Liu's article is the **most comparative-architecture treatment** of the LLM Wiki idea. Karpathy quote Liu cites: *"RAG rereads the same books for every exam, never actually learning the material."* |
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju 2026 (Medium)]] | Two independent **explainer-articles** of the LLM Wiki pattern, published 11 days apart. Both treat the three-layer architecture; both compare to RAG; both predict hybrid convergence. **Strongest two-explainer cross-source convergence** on the LLM Wiki construct |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase / ex-brain 2026]] | ex-brain implements the LLM Wiki pattern at personal-knowledge-base scale; GBrain implements *all three patterns* (RAG + Wiki + Skills). Different scopes, same architectural family |
| [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack\|Tan / GStack 2026]] | GStack and GBrain are Tan's two open-source toolkits. GStack wraps Claude Code with skills *for individual sessions*; GBrain wraps it with autonomous skills *running on schedules*. The wiki's **first cross-source connection between Tan's two projects** |
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB / Martin 2026]] | Same-date publication (27 April 2026); convergent on the multi-modal-substrate question. SurrealDB at the database layer; Liu at the architecture layer above it |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler 2026 (Thoughtworks)]] | Liu's *thin harness, fat skills* (200 lines of harness, intelligence in skill files) is structurally identical to Böckeler's *Skills as the modularised feed-forward layer* in her harness vocabulary. Two-source convergence on the *fat-context-thin-runtime* harness pattern |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex 2026]] | GBrain's skill-file-as-workflow-contract is the personal-agent analog of Lopopolo's AGENTS.md table-of-contents pattern. Same architecture at different scopes |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026 (TDS / Neo4j)]] | Liu mentions Neo4j is *"building knowledge layers"* combining graph + vector + semantic. Bratanic's Neo4j-backed agent-memory is the vendor implementation of what Liu describes as the convergence direction |

### Contradictions

None substantive. Liu's framing is descriptive and balanced; the three-way decision framework explicitly avoids positioning any one architecture as superior.

## Linked entities and concepts

**Concept pages affected**:

- **[[concepts/llm-wiki|llm-wiki]]** — Liu is one of the four anchor sources for the new concept page (alongside ex-brain, Raju, and the upstream Karpathy gist).
- [[agent-harness]] — thin-harness/fat-skills framing.
- [[knowledge-graphs]] — Neo4j knowledge-layers convergence direction.

**Dangling** (single-source first-mention, deferred):

- **Yanli Liu** — finance practitioner in Luxembourg; AI Advances contributor.
- **AI Advances** — Medium publication (78K followers).
- **OpenClaw**, **Hermes** — personal AI agents Liu names alongside Claude Code as GBrain's intended runtime environments.

**Other entities cross-referenced**:

- **[[Andrej Karpathy]]** — explicitly cited multiple times.
- **Garry Tan** — third-source threshold for entity promotion now reached (Tan/GStack + ex-brain + this article).
- **GBrain** — multi-source threshold met.
- **Neo4j**, **Pinecone**, **Chroma**, **LangChain**, **LlamaIndex** — named as RAG/KG ecosystem entities.
- **Postgres + pgvector** — GBrain's backend.

## Open questions raised by this source

- **The 2024 RAG-failure-points paper** — Liu cites *"a 2024 research paper mapped into seven distinct failure points"*; primary-source target.
- **GBrain GitHub repo** — Liu describes the architecture in detail; primary-source ingest of RESOLVER.md, THIN_HARNESS_FAT_SKILLS.md, and the SKILL.md schema would substantiate the *thin-harness/fat-skills* framing.
- **OpenClaw and Hermes** — Liu names these as personal AI agents GBrain is built for. Both are Dangling first-mention; primary-source ingest targets.
- **Neo4j knowledge layers** — Liu references *"enterprise platforms like Neo4j are building knowledge layers that combine graph databases, vector search, and semantic reasoning"*; primary-source target on the specific Neo4j product or initiative.
- **The "RAG era / Wiki + Skills emerge / Convergence" timeline** — Liu's three-phase prediction is high-level; specific milestones / vendor announcements that mark phase transitions would substantiate.
- **Liu's other-articles cluster** — the article references *"The 9 Sections Every DESIGN.md Needs"*, *"The 4 Lines Every CLAUDE.md Needs"*, *"Harness Engineering: What Every AI Engineer Needs to Know in 2026"*. All convergent with the wiki's existing clusters; potential future-ingest targets.
