---
type: query-trace
question: "Is RAG dead according to the wiki?"
date: 2026-06-05
language: en
trace: 2026-06-05-is-rag-dead-query-trace.json
pages_used: 5
pages_ignored: 49
---

# Query trace — Is RAG dead?

## 1. Question

- **Original:** Is RAG dead according to the wiki?
- **Restated:** Does the wiki conclude that retrieval-augmented generation is obsolete, or does it survive in some form?
- **Facets:** 1) the headline verdict · 2) what specifically died vs. persists · 3) what replaced / rebranded it.

## 2. Paths explored

Retrieval ran via `node scripts/wiki-retrieve.mjs --json -n 12` (qmd ∪ graph, RRF-fused, decay-ranked). `graph_available: true`; 11 qmd hits + 43 graph neighbours = 54 candidates.

**qmd hits** (relevance stream)

| # | Page | type | qmd score | fused | effConf | verdict |
|---|------|------|-----------|-------|---------|---------|
| 1 | `wiki/syntheses/is-rag-dead.md` | synthesis | 0.93 | 0.93 | 0.83 | **USE** |
| 2 | `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | source | 0.93 | 0.93 | — | IGNORE |
| 3 | `wiki/threads/is-rag-dead.md` | thread | 0.81 | 0.81 | — | **USE** |
| 4 | `wiki/sources/2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained.md` | source | 0.90 | 0.90 | — | **USE** |
| 5 | `wiki/concepts/llm-wiki.md` | concept | 0.84 | 0.84 | 0.74 | **USE** |
| 6 | `wiki/sources/2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker.md` | source | 0.81 | 0.81 | 0.70 | **USE** |
| 7 | `wiki/syntheses/knowledge-architectures-for-llm-agents.md` | synthesis | 0.85 | 0.85 | 0.83 | IGNORE |
| 8 | `wiki/sources/2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers.md` | source | 0.84 | 0.84 | — | IGNORE |
| 9 | `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | source | — | 0.81 | 0.80 | IGNORE |
| 10 | `wiki/sources/2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings.md` | source | — | 0.82 | — | IGNORE |
| 11 | `wiki/concepts/agent-harness.md` | concept | — | 0.84 | 0.95 | IGNORE |

**graph neighbours** (`--hops 1`, typed-edge stream — top of a 43-page tail)

| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus.md` | llm-wiki / synthesis edges | 1 | 0.46 | IGNORE |
| `wiki/concepts/knowledge-graphs.md` | is-rag-dead --supports--> this | 1 | 0.44 | IGNORE |
| `wiki/sources/2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks.md` | llm-wiki edges | 1 | 0.43 | IGNORE |
| …40 further graph-only neighbours | — | 1 | <0.46 | IGNORE (`below-threshold`) |

**index.md / gap-expansion (Step 5):** none — all three facets were answered by the USE set, so no expansion round was run.

## 3. Ignore policy applied

Reason-classes that actually fired this run (`references/ignore-policy.md`):

- `redundant` — a stronger USE page already covers the same claim (the broad knowledge-architectures synthesis and the Liu comparative piece are both subsumed by `is-rag-dead`).
- `off-facet` — semantically adjacent (qmd/graph pulled them in) but addressing none of the three facets: GraphRAG mechanics, KG-embeddings technique, agentic team structures, and the agent-harness concept (high confidence ≠ relevance).
- `below-threshold` — the 40-page graph-only tail below fused 0.46; no facet needs them.

## 4. Information ignored

| Page | reason-class | reason |
|------|--------------|--------|
| `wiki/syntheses/knowledge-architectures-for-llm-agents.md` | redundant | broader 3-way (RAG/Wiki/Skills) synthesis; `is-rag-dead` is the direct answer for this question |
| `wiki/sources/2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers.md` | redundant | its verdict is already captured in W1/W5 |
| `wiki/concepts/agent-harness.md` | off-facet | fused 0.84 / effConf 0.95, but about runtime scaffolding, not RAG's death |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | off-facet | GraphRAG substrate detail, not the verdict |
| `wiki/sources/2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings.md` | off-facet | KG-embeddings lecture; a technique, not the question |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | off-facet | team structures; unrelated to retrieval |
| 43 graph-only neighbours (fused < 0.46) | below-threshold | long tail reached only by 1-hop traversal; no facet needs them |

## 5. Information used

| Page | type | effConf | contribution |
|------|------|---------|--------------|
| [[syntheses/is-rag-dead\|is-rag-dead synthesis]] | synthesis | 0.83 | the headline verdict, what's retired vs. what persists, the rebrand, the failure-mode union |
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju 2026]] | source | — | the "elevation not elimination" thesis + 10-dimension RAG-vs-LLM-Wiki tradeoff table |
| [[2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker\|Ebbelaar 2026]] | source | 0.70 | concrete proof the technique persists: BM25 + dense + RRF + reranker production stack |
| [[concepts/llm-wiki\|llm-wiki]] | concept | 0.74 | the complementary synthesis-layer architecture; vector retrieval as substrate-below-the-wiki |
| [[threads/is-rag-dead\|is-rag-dead thread]] | thread | — | five-source convergence + the sub-question structure |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page(s) | Section / span |
|--------|------------------------|--------------|----------------|
| [W1] | RAG the technique is not dead; the *term* is being retired; vector retrieval persists as a substrate primitive | [[syntheses/is-rag-dead\|is-rag-dead]] | ## Findings |
| [W2] | "Not the elimination of retrieval, but the elevation of it" — complement, not replace | [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju 2026]] | ## The verdict — complement, not replace |
| [W3] | The technique persists as hybrid search: BM25 + dense + RRF + cross-encoder reranker — "the production stack that … wins in 2026" | [[2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker\|Ebbelaar 2026]] | ## TL;DR |
| [W4] | The LLM Wiki sits at the synthesis layer above retrieval; vector embeddings are the cheapest substrate once a wiki outgrows its context window | [[concepts/llm-wiki\|llm-wiki]] | ## Convergence prediction — the hybrid architecture |
| [W5] | Five independent sources converge: term-vs-technique, complement-not-replace, named failure modes, context-engineering rebrand, bitter-lesson direction | [[threads/is-rag-dead\|is-rag-dead thread]] | ## Cross-source convergence |

## 7. Final answer

**No — the wiki's verdict is that RAG is not dead; the *term* is dying while the *technique* survives as a substrate.** The `is-rag-dead` synthesis closed (filed 2026-05-12) with five sources converging on one resolution: *"RAG (retrieval-augmented generation) is not dead. The term RAG is being retired in favour of context engineering. The technique persists as a substrate primitive underneath higher-level architectures, not as the application architecture itself."* [W1]

**What actually died** is the framing, not the retrieval: the developer-internet "RAG is dead" reaction to Karpathy's LLM Wiki gist (17M views in days) over-read it. As Raju put it, Karpathy proposed *"a different job for the LLM in a knowledge pipeline — not the elimination of retrieval, but the elevation of it."* [W2] What gets retired specifically is (a) the ambiguous *term*, (b) the conflation of RAG with the whole application architecture, and (c) the naive embed→store→top-k→inject→generate pipeline, which fails at scale through chunking, re-derivation, and passivity. [W1][W5]

**What persists** is vector retrieval as one substrate primitive among several — and concretely, *hybrid search*: BM25 (sparse) ∪ dense embeddings → Reciprocal Rank Fusion → cross-encoder reranker, which Ebbelaar calls *"the production stack that works and wins in 2026."* [W3] Above that substrate sit higher-level architectures: the [[concepts/llm-wiki|LLM Wiki]] for the synthesis layer, GraphRAG for graph-aware retrieval, and agentic search for orchestration — with vector embeddings as the cheapest substrate once a wiki outgrows its context window. [W4]

**The rebrand** the field is converging on is *context engineering* — the umbrella construct, with RAG / vector retrieval / hybrid search as implementation primitives beneath it; the wiki also notes the "bitter-lesson" direction that context engineering will fold back into the models themselves. [W1][W5]

*Caveat on currency:* the load-bearing pages are fresh (synthesis `effConf 0.83`, last confirmed 2026-05-29), so no decay discount applies. This trace reflects the wiki as of 2026-06-05.

## 8. Trace artifact

Machine-readable provenance: [`2026-06-05-is-rag-dead-query-trace.json`](2026-06-05-is-rag-dead-query-trace.json) — full 54-candidate ledger with verdicts, scores, and the answer-element map.
