---
type: thread
status: closed
opened: 2026-04-09
closed: 2026-05-12
tags: [rag, llm-wiki, retrieval, knowledge-architectures, term-vs-technique, hybrid-architecture, complement-not-replace]
---

# Thread: Is RAG dead?

## The question

When Andrej Karpathy posted his **LLM Wiki gist on 4 April 2026** (17M views / 5K stars / 4.3K forks within days — per [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]), the developer internet declared *"RAG is dead."* The wiki then ingested a stream of explainer articles, vendor pieces, and conference talks that all touched on the claim. The question this thread tracks: **is RAG actually dead — and if not, what exactly did Karpathy retire?**

Sub-questions:

- Is *retrieval-augmented generation* (the technique) being replaced, or is *RAG* (the term) being retired?
- If RAG persists, what is it complementary to?
- What are the named failure modes of RAG that motivate the rejection?
- What is the proposed replacement vocabulary (context engineering / LLM Wiki / agentic search)?
- Which corpus sizes / use cases still call for RAG, and which call for alternatives?

## What we know so far

### From [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026 (Medium)]]

The clearest single-article explainer of Karpathy's gist. **Verdict**: *"The 'RAG is dead' framing is both wrong and unhelpful. What Karpathy actually proposed is a different job for the LLM in a knowledge pipeline — not the elimination of retrieval, but the elevation of it."*

Ten-dimension RAG-vs-LLM-Wiki comparison matrix surfaces explicit tradeoffs:

- RAG scales to millions of documents; LLM Wiki practical only to ~hundreds.
- RAG is stateless; LLM Wiki is stateful (knowledge compounds).
- RAG handles fresh / streaming data better; LLM Wiki re-ingest is expensive.
- RAG hallucinations are isolated to query time; LLM Wiki errors are *baked in* and *propagate* (persistent-mistake-amplification).

Three named limitations Karpathy glossed over: scale ceiling, hallucination baking, ingest cost.

### From [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026 (AI Advances)]]

**The most-substantive comparative-architecture treatment**. Frames the question as a three-way choice — RAG / LLM Wiki / Fat Skills (GBrain). Verdict: *"these architectures aren't competing. They're solving different versions of the same problem. Picking between them is a design decision, not a loyalty test."*

RAG's three named failure points (cites a 2024 paper with 7 total):

- **Chunking problem** — 30-page spec fragmented; relationships destroyed.
- **Re-derivation problem** — every query starts from scratch; *"RAG rereads the same books for every exam, never actually learning the material"* (Karpathy via Liu).
- **Passivity problem** — RAG waits for queries; never notices contradictions; never acts.

**Convergence prediction**: 2023 RAG era → 2025 Wiki + Skills emerge → 2026+ hybrid.

### From [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber 2026 (Chroma CEO on Mastra)]]

**The vendor-of-the-substrate vantage**. Headline framing: *"RAG is dead — the term, not the technique."* *"If you ask 25 people to define RAG, they'll all define it a slightly different way. Rag is banned. Vector database is also banned."* Reframe: **context engineering**.

**Context Rot** — Chroma's 45-page 2025 research report demonstrating LM performance is **not invariant to context length**. Dumb zone starts somewhere **20K-120K tokens** depending on use case. *"I've not found anybody who really trusts a million tokens to do anything that's any kind of good."*

Three-axis context-failure taxonomy: **too much / too little / confusing**. Strict superset of SurrealDB's three failure modes.

**File systems are bad databases** structural critique — current Codex/Claude-Code default (file-system + bash) has poor concurrency / no indexing / grep-only search / sandbox heavyweight. Cites [[Swyx]]'s *"Oops, You Wrote a Database"* article.

**The bitter-lesson direction**: context engineering will be folded back into the models themselves. Chroma just released a model trained to edit its own context. *"If you want to bet on the future, you should bet that will be the case."*

### From [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain 2026]]

**Earliest-vendor implementation worked example** (5 days after Karpathy's gist). ex-brain CLI tool using seekdb (OceanBase's AI-native database). **MCP server integration** demonstrates the harness/substrate boundary explicitly. No direct comment on the *RAG is dead* claim but implements the *complement-not-replace* hybrid via *hybrid search* (BM25 + vector + scoring layer).

### From [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]]

**Practical-engineering vantage on the failure modes**. Three named vector-only-RAG failure modes: **context clash / context confusion / dense neighbourhood degradation**. **GraphRAG** mechanic — vector + graph in single SurrealQL query — as the *technical* implementation of the *complement-not-replace* hybrid.

## Cross-source convergence

The five sources independently converge on:

1. **Term-vs-technique distinction**: *RAG* the term should be retired (or at least clarified); the technique (vector retrieval) persists as a substrate primitive.
2. **Complement, not replace**: hybrid architecture is the right answer for serious knowledge systems.
3. **Named failure modes**: chunking / re-derivation / passivity (Liu) ⊆ too-much / too-little / confusing (Huber) ⊆ context clash / context confusion / dense neighbourhood degradation (SurrealDB; only addresses the *too-much* axis).
4. **Context engineering as the rebranding** (Huber explicit; Raju implicit via the LLM Wiki *compile* operation).
5. **Bitter-lesson direction**: context engineering moves from hand-crafted pipelines into the models themselves (Huber explicit; Karpathy compatible).

## How this thread should resolve

**Resolution**: synthesis page in `wiki/syntheses/` capturing the *complement-not-replace* consensus + the *what-RAG-is-and-isn't* clarification + the named failure modes + the convergence prediction. Closed when 4+ sources have converged on the answer (threshold met as of 12 May 2026).

**Closed 2026-05-12**: see [[syntheses/is-rag-dead|synthesis: Is RAG dead?]].
