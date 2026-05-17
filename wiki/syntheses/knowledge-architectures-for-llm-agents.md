---
type: synthesis
aliases: ["knowledge architectures for LLM agents", "RAG vs LLM Wiki vs Fat Skills", "three architectures synthesis"]
tags: [rag, llm-wiki, fat-skills, gbrain, agent-memory, knowledge-architectures, decision-framework, hybrid-convergence, three-architectures, synthesis, cross-source-comparison]
derived_from: [knowledge-architectures-for-llm-agents]
opened: 2026-04-27
closed: 2026-05-12
confidence: 0.90
last_confirmed: "2026-05-12"
accessed_at: "2026-05-12"
source_count: 7
relationships:
  - type: supports
    target: llm-wiki
    via: "places the LLM Wiki construct in the broader three-architecture decision framework; clarifies what it's good at (deep expertise on ~1K sources) and what it's not (search at scale; autonomous action)"
  - type: supports
    target: knowledge-graphs
    via: "GraphRAG (vector + graph in single query) is one technical instantiation of the RAG layer in the hybrid; KG-as-substrate is convergent across SurrealDB / seekdb / Neo4j vendors"
  - type: supports
    target: agent-harness
    via: "the harness reads from one or more of the three architectures depending on the agent's job; the Context layer + Compounding layer in Chatterjee's 4-layer model are where this decision lives"
  - type: instance-of
    target: agent-development-lifecycle
    via: "Liu's three-architecture decision framework is the Build-phase choice over which storage/retrieval pattern fits the agent's job"
quality_score: 1
---

# Synthesis: Knowledge architectures for LLM agents — RAG / LLM Wiki / Fat Skills

Closes [[threads/knowledge-architectures-for-llm-agents|knowledge-architectures-for-llm-agents]]. Filed 2026-05-12 with **7 sources** converging on the three-architecture decision framework and the hybrid-convergence prediction.

## Question

**Which knowledge architecture fits which class of agent task, and how do they hybridise?** The wiki ingested three increasingly distinct architectures across April-May 2026 — RAG (retrieve), LLM Wiki (compile), Fat Skills / GBrain (act) — plus several substrate-layer worked examples. What is the decision framework, and what does the production hybrid actually look like?

## Findings

**No single architecture wins everywhere.** Picking among RAG / LLM Wiki / Fat Skills is a **design decision driven by the agent's job**, not a loyalty test. The most capable production systems combine all three at different layers:

- **RAG** at the **retrieval layer** — finding relevant content at scale (10K+ documents).
- **LLM Wiki** at the **synthesis layer** — compiling retrieved content into persistent, interlinked, compounding knowledge.
- **Fat Skills** at the **action layer** — operationalising compiled knowledge into autonomous workflows triggered by crons / signals / events.

### The three-architecture comparison matrix (per [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]])

| Dimension | RAG | LLM Wiki | Fat Skills (GBrain) |
|---|---|---|---|
| **Core verb** | Retrieve | Compile | Act |
| **Scale** | 200K+ docs | ~1K sources | 17K+ pages |
| **Compounds?** | No | Yes — wiki refines | Partial — logs |
| **Proactive?** | No — waits | No — waits | Yes — 21 crons |
| **Context** | Chunks (lossy) | Full pages | Skill-scoped |
| **Setup cost** | Low (a weekend) | Medium (weeks) | High (months) |
| **Best for** | Search at scale | Deep expertise | Autonomous ops |

### The decision tree — *"what is your agent's job?"*

- **Retrieve answers from a large corpus** (10K+ docs, change regularly, users need fast answers, ship production-ready with known cost model) → **RAG**. Pair with a reranker; covers 80% of knowledge-assistant use cases.
- **Build expertise that should compound over time** (hundreds of sources, value in the connections, your hundredth query should be smarter than your first) → **LLM Wiki**.
- **Act on what you know without being asked** (monitor, flag, enrich, execute; run while you sleep; trigger workflows when conditions change) → **Fat Skills**. Budget for engineering — codebase with tests, evaluations, maintenance overhead.

*"Most production agents need 2 of 3. Pick your primary, then layer the second when it hurts."*

### Per-architecture failure modes (the wiki's load-bearing summary)

#### RAG (per [[syntheses/is-rag-dead|companion synthesis: Is RAG dead?]] and [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] + [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber 2026]])

| Failure | Mechanism |
|---|---|
| **Chunking problem** | 30-page spec fragmented into 500-token chunks; relationships destroyed |
| **Re-derivation problem** | Every query starts from scratch; *"RAG rereads the same books for every exam, never actually learning the material"* (Karpathy via Liu) |
| **Passivity problem** | Waits for queries; never notices contradictions between indexed docs; never acts |
| **Context Rot** | LM performance not invariant to context length; dumb zone at 20K-120K tokens (Chroma empirical anchor) |
| **Latency** | Embed + search + rerank + package compounds across 40-tool-call loops |

#### LLM Wiki (per [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]])

| Failure | Mechanism |
|---|---|
| **Scale ceiling** | Index file must fit in context; ~100 pages works (Karpathy's scale); 10K pages doesn't |
| **Hallucination baking** | LLM-synthesised pages stored as authoritative knowledge; *"that's a wrong page that every future query trusts"* |
| **Ingest cost** | Every new source requires multiple LLM passes to summarise + link + merge; expensive at high re-ingest velocity |
| **Real-time / streaming** | Re-ingest can't keep up with high-velocity data |
| **Multi-user / enterprise** | No RBAC, no ACID transactions, no concurrency controls |

#### Fat Skills / GBrain (per [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] + [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan 2026]])

| Failure | Mechanism |
|---|---|
| **Engineering investment** | 24 skills + 21 cron jobs + end-to-end tests + evaluations + unit tests — *"that's not a weekend project. It's a codebase"* |
| **Deep personalisation** | Built around the operator's specific workflows; not drag-and-drop transferable |
| **Single-power-user scale** | Architecture assumes one operator who understands the full system; *"you can't npm install someone else's brain"* |
| **Doesn't map to typical enterprise deployment** | Engineering overhead per user too high for *"give everyone access to a knowledge assistant"* |

### The hybrid architecture — what production combines actually look like

**Liu's hybrid pattern** (the synthesis canonical):

> *"RAG for the retrieval layer (finding relevant content at scale), Wiki for the synthesis layer (compiling retrieved content into persistent knowledge), and skills for the action layer (operationalizing that knowledge into autonomous workflows)."*

**Operational instantiations the wiki holds**:

| Layer | Implementation | Source |
|---|---|---|
| **Retrieval substrate** | Hybrid search (BM25 + vector + scalar) in single query; SurrealQL multi-modal queries; seekdb embedded-mode with AI_EMBED/AI_RERANK | [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB]] / [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase ex-brain]] |
| **GraphRAG** | Vector-search trimmed by graph-relationship subset; multi-hop traversal — *"adding graph to that helps you trim down the results"* | [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB]] |
| **Synthesis layer (LLM Wiki)** | Three-layer architecture (raw / wiki / schema); three operations (ingest / query / lint); CLAUDE.md as schema | [[concepts/llm-wiki\|llm-wiki]] concept page + [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju]] + [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers\|Liu]] |
| **Action layer (Fat Skills)** | RESOLVER.md routing + 24-skill workflow markdown files + 21 cron jobs + Postgres+pgvector | [[Garry Tan\|GBrain]] |
| **Specialised retrieval LMs** | Auto-regressive LM that outputs documents directly; 10× faster, 25× cheaper than gigabrain models | Chroma Context One (Huber) |
| **MCP-server-as-substrate-interface** | `brain_get` / `brain_put` / `brain_search` / `brain_compile` / `brain_link` exposed to Claude Code | [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|ex-brain]] |

### Claude Code as the partial-convergence-example

Liu's load-bearing observation:

> *"Claude Code already hints at this convergence. CLAUDE.md files function as a mini-wiki (persistent context that compounds across sessions). Auto-memory learns from interactions (compounding). Skills trigger workflows (action). It's not a deliberate implementation of all three patterns — but the same pressures produced the same solutions."*

**Meta-relevant**: this wiki operates inside Claude Code, instantiates CLAUDE.md as the schema layer, uses session-start hooks as auto-memory, and integrates Skills via the skill API. The convergence is partially realised in the runtime this repo runs on.

### Convergence prediction — Liu's three-phase timeline

| Phase | Timing | Characterisation |
|---|---|---|
| **1. RAG era** | 2023 | Embed-store-retrieve-generate pipeline as the default; LangChain / LlamaIndex / Pinecone / Chroma ecosystem |
| **2. Wiki + Skills emerge** | 2025 | Karpathy's LLM Wiki gist (April 2026; the wiki dates this construct's emergence to late-2025 / early-2026); Tan's GStack (3-week build, Apr 2026); Tan's GBrain (Apr 2026) |
| **3. Convergence** | 2026+ | Hybrid systems combining all three; *"the same way databases evolved from 'pick SQL or NoSQL' to hybrid systems that handle both, knowledge architectures are converging"* (Liu) |

**Signals the convergence is happening**:

- Karpathy's LLM Wiki v2 community extensions adding retrieval layers on top of compiled wikis (Liu cites; primary-source target).
- GBrain's skills already query a Postgres + pgvector backend (Liu).
- Enterprise platforms like Neo4j building knowledge layers that combine graph + vector + semantic in a single access point (Liu).
- Mintlify's virtualized-bash-on-Chroma (Huber).
- Chroma Context One — specialised search-LM that outputs documents directly to a generation-LM (Huber).
- Claude Code's CLAUDE.md + auto-memory + skills (Liu).

## Sources consulted

- [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026 (Sequoia AI Ascent)]] — upstream spec author; first-person continued use of the LLM Wiki pattern.
- [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain 2026]] — earliest-vendor implementation worked example; substrate-layer (seekdb) + MCP interface.
- [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] — clearest single-article explainer of Karpathy's gist; three-layer architecture + three operations + working Python.
- [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan / GStack 2026]] — Fat-Skills-adjacent operator vantage (GStack as toolkit) + reference to GBrain.
- [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] — **the canonical three-architecture comparison + decision framework + convergence prediction**.
- [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]] — practical-engineering vantage; GraphRAG; KG-ETL pipeline; chunking-strategy taxonomy.
- [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber 2026]] — vendor-of-the-substrate vantage; Context Rot; bitter lesson; file-systems-are-bad-databases.

## Lessons

Each a single transferable claim:

1. **Choose by job, not loyalty**: agent's task class (retrieve / compile / act) determines architecture; production systems hybrid 2-of-3.
2. **RAG scales to corpus size where LLM Wiki cannot**, but LLM Wiki compounds where RAG cannot. Different jobs.
3. **Fat Skills are codebase-level investment**, not weekend hacks — budget for tests, evals, maintenance.
4. **GBrain's *thin harness, fat skills* pattern inverts typical agent design** — ~200 lines of harness; intelligence in skill-file markdown.
5. **Vector retrieval becomes a substrate primitive** at the synthesis-layer scale, not the application architecture itself.
6. **Hybrid search (vector + graph + full-text + scalar) in a single query** is the substrate-layer pattern emerging across vendors (SurrealDB / seekdb / Chroma).
7. **The convergence is empirically observable** in Claude Code's CLAUDE.md + auto-memory + skills — *"the same pressures produced the same solutions"* (Liu).
8. **Specialised small models** for retrieval beat gigabrain models on cost + speed + sometimes quality (Chroma Context One pattern).
9. **GBrain's RESOLVER.md routing-via-skill-descriptions** is the *thin-harness* pattern's load-bearing primitive — skill descriptions function as the resolver; no explicit routing code needed.
10. **The boundary between LLM Wiki and Fat Skills is the *act* axis** — both compile, but Fat Skills also trigger workflows autonomously.

## Open questions

- **The 2024 RAG-failure-points academic paper** Liu cites — primary-source target.
- **Karpathy's LLM Wiki v2 community extensions** adding retrieval layers — primary-source target on the specific extension projects.
- **The GBrain GitHub repo** — primary-source target for RESOLVER.md, THIN_HARNESS_FAT_SKILLS.md, the 24 SKILL.md files.
- **Enterprise-scale LLM Wiki** — Liu and Raju both flag this as a different infrastructure-shaped problem (RBAC, ACID, semantic graph + LLM agent maintaining it). No enterprise-scale implementation source ingested.
- **The agentic-search-vs-RAG empirical disagreement** between [[Boris Cherny]] (Anthropic / Claude Code) and Huber (Chroma). Huber promised data *"next week"* (mid-May 2026). Open primary-source target.
- **Neo4j knowledge layers** — Liu references *"enterprise platforms like Neo4j are building knowledge layers that combine graph databases, vector search, and semantic reasoning"*. Primary-source target on the specific Neo4j product or initiative.
- **OpenClaw and Hermes** — Liu names these as personal AI agents GBrain is built for. Both currently Dangling first-mention; primary-source targets.
- **The point of role-convergence between IC/DRRI/AI-founder-type (Hu) and product-builder (Singhal)** — both predict role-collapse via Claude Code's emergence as a general builder substrate. Worth tracking whether *knowledge architecture choice* and *organisational role choice* end up making the same kinds of decisions.

## Related syntheses

- **Companion synthesis**: [[syntheses/is-rag-dead|is-rag-dead]] — narrow synthesis on the RAG-specific question (*RAG is dead — the term, not the technique*). This page extends to the full three-architecture treatment.
- **Concept anchors**: [[concepts/llm-wiki|llm-wiki]] (the second-architecture concept page; same pattern this repo implements), [[knowledge-graphs]] (substrate primitive), [[agent-harness]] (the runtime that reads from the substrate), [[agent-development-lifecycle]] (the Build-phase choice over which storage/retrieval pattern fits the agent's job).

## Debates and supersession

None substantive. The seven wiki sources converge on the three-architecture decision framework and the hybrid-convergence prediction.

The one substantive disagreement is at the **substrate level, not the architecture level**: [[Boris Cherny]] (Anthropic / Claude Code) advocates agentic-search-with-grep over RAG; Huber pushes back on incentives. This disagreement lives downstream of the *which-architecture* choice — both interlocutors agree on the architecture (something like LLM Wiki + Fat Skills); they disagree on the substrate-primitive default.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
