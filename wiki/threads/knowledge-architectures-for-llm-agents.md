---
type: thread
status: closed
opened: 2026-04-27
closed: 2026-05-12
tags: [rag, llm-wiki, fat-skills, gbrain, agent-memory, knowledge-architectures, decision-framework, three-architectures, hybrid-convergence]
---

# Thread: Which knowledge architecture fits which agent's job?

## The question

By late April 2026 the wiki had ingested **three increasingly distinct knowledge architectures** for LLM-based agents:

1. **RAG** — embed sources into vectors; retrieve top-k chunks per query; inject into context; generate.
2. **LLM Wiki** — LLM pre-compiles raw sources into a persistent interlinked markdown wiki; query reads the index + drills into compiled pages; *"file good answers back as new pages."* (Karpathy's pattern; the foundational architecture for this repo.)
3. **Fat Skills / GBrain** — autonomous skills with cron triggers operating on a backing store; LLM-routed via skill-descriptions; the agent doesn't just remember — it acts. (Garry Tan's pattern.)

The thread tracks the question: **which architecture fits which class of agent task, and how do they hybridise?**

Sub-questions:

- What is each architecture's core verb (retrieve / compile / act)?
- Where does each scale well and where does each break?
- What is the decision criterion for choosing between them?
- How does the *hybrid convergence* work in practice — what does a production system that combines retrieval + wiki + skills actually look like?
- What evidence is there that Claude Code (or any other shipping system) is already partial-implementing the convergence?

## What we know so far

### From [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026 (AI Advances)]]

**The canonical three-architecture comparison matrix**:

| Architecture | Core verb | Scale | Compounds? | Proactive? | Context | Setup cost | Best for |
|---|---|---|---|---|---|---|---|
| **RAG** | Retrieve | 200K+ docs | No | No — waits | Chunks (lossy) | Low (a weekend) | Search at scale |
| **LLM Wiki** | Compile | ~1K sources | Yes — wiki refines | No — waits | Full pages | Medium (weeks) | Deep expertise |
| **Fat Skills (GBrain)** | Act | 17K+ pages | Partial — logs | Yes — 21 crons | Skill-scoped | High (months) | Autonomous ops |

**Decision tree**: *"what is your agent's job?"* — retrieve from large corpus → RAG; build deep expertise → LLM Wiki; act autonomously → Fat Skills. Most production agents need **2 of 3**.

**Hybrid reality**: *"The most capable architectures will combine all three: RAG for the retrieval layer (finding relevant content at scale), Wiki for the synthesis layer (compiling retrieved content into persistent knowledge), and skills for the action layer (operationalizing that knowledge into autonomous workflows)."*

**Convergence prediction**: 2023 RAG era → 2025 Wiki + Skills emerge → 2026+ hybrid.

### From [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026 (Medium)]]

The LLM Wiki explainer. **Three-layer architecture** (raw sources / wiki / schema=CLAUDE.md). **Three operations** (ingest / query / lint). **Ten-dimension RAG-vs-LLM-Wiki tradeoff matrix**.

**Verdict**: *"The honest architecture for most serious knowledge systems is a hybrid. Use the LLM Wiki pattern for what it genuinely does better: compiling and maintaining synthesised knowledge ... Use vector retrieval as the substrate underneath the wiki once it outgrows context."*

### From [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber 2026 (Chroma)]]

**Vendor-of-the-substrate vantage**. *"RAG is dead — the term, not the technique."* **Context Rot 45-page report** — empirical anchor for the LLM Wiki scale ceiling.

**Bitter lesson**: context engineering will be folded back into models. **File-systems-are-bad-databases** critique of the current Codex/Claude-Code default; **virtualized-bash-on-real-database** (Mintlify on Chroma) as the cleaner alternative.

### From [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan / GStack 2026]] + [[Garry Tan]] entity

**The Fat Skills / GBrain operator vantage**. GBrain: 24 autonomous skills + 21 cron jobs + 17,888-page brain on Postgres + pgvector. **Thin harness, fat skills**: ~200 lines harness code; intelligence in skill files. **RESOLVER.md + skill-description-as-routing-table**. Always-on signal-detector skill. Deterministic-vs-latent work split.

### From [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]

**The upstream spec author** for the LLM Wiki pattern. Continues to use it personally: *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles."* **Software 3.0** framing positions the LLM Wiki within the broader programs-migrate-into-model-weights direction.

### From [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain 2026]] + [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]]

**Substrate-layer worked examples**. ex-brain implements LLM Wiki with MCP server integration on seekdb (multi-modal AI-native database). SurrealDB's GraphRAG provides vector + graph + full-text in a single SurrealQL query. Both demonstrate the substrate-LLM-Wiki-application boundary in production.

## Cross-source convergence

The sources converge on:

1. **Three distinct architectures with different core verbs** (retrieve / compile / act) — Liu's framework is canonical.
2. **No single architecture wins everywhere** — choice depends on agent's job.
3. **Hybrid is the production reality** — the most capable systems combine all three.
4. **Claude Code already partial-implements the convergence** — CLAUDE.md = mini-wiki; auto-memory = compounding; skills = action.
5. **Vector retrieval becomes substrate** — at LLM Wiki scale, retrieval sits underneath; not the application layer.

## How this thread should resolve

**Resolution**: synthesis page in `wiki/syntheses/` capturing Liu's three-architecture decision framework + the hybrid-convergence prediction + the per-architecture failure-mode summary + the Claude-Code-as-partial-convergence-example. Closed when the convergence is reflected across 5+ sources from distinct vantages (threshold met as of 12 May 2026).

**Closed 2026-05-12**: see [[syntheses/knowledge-architectures-for-llm-agents|synthesis: Knowledge architectures for LLM agents]].
