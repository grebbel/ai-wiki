---
type: synthesis
aliases: ["RAG is dead synthesis", "RAG synthesis", "is RAG dead"]
tags: [rag, retrieval, llm-wiki, knowledge-architectures, term-vs-technique, hybrid, complement-not-replace, synthesis, cross-source-comparison]
derived_from: [is-rag-dead]
opened: 2026-04-09
closed: 2026-05-12
confidence: 0.90
last_confirmed: "2026-05-29"
accessed_at: "2026-06-05"
source_count: 8
relationships:
  - type: supports
    target: llm-wiki
    via: "the RAG-as-substrate-not-application reframe is precisely what makes the LLM Wiki pattern coherent at scale — LLM Wiki at the synthesis layer, vector retrieval underneath as the substrate"
  - type: supports
    target: knowledge-graphs
    via: "GraphRAG (SurrealDB) and hybrid-search (Chroma / OceanBase) are operational instances of the *complement-not-replace* hybrid; the KG construct is one of the substrate primitives the hybrid layers over"
  - type: supports
    target: agent-harness
    via: "the harness's Context layer reads from a hybrid substrate (vector + graph + structured + filesystem) rather than from a single source-of-truth retrieval type; the *file-systems-are-bad-databases* critique is harness-design guidance"
quality_score: 1
---

# Synthesis: Is RAG dead?

Closes [[threads/is-rag-dead|is-rag-dead]]. Filed 2026-05-12 with **5 sources** converging on the same answer.

## Question

**Is RAG dead, or just the term?** When Karpathy's LLM Wiki gist went viral (4 April 2026; 17M views in days), the developer internet declared *"RAG is dead."* The wiki ingested five sources in the following five weeks. What did they actually conclude?

## Findings

**RAG (retrieval-augmented generation) is not dead. The term *RAG* is being retired in favour of *context engineering*. The technique persists as a substrate primitive underneath higher-level architectures, not as the application architecture itself.**

The five wiki sources converge on this resolution from five distinct vantages:

| Source | Vantage | Headline |
|---|---|---|
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju 2026]] | LLM-Wiki explainer | *"The 'RAG is dead' framing is both wrong and unhelpful... not the elimination of retrieval, but the elevation of it."* |
| [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers\|Liu 2026]] | Comparative-architecture | *"These architectures aren't competing. They're solving different versions of the same problem."* |
| [[2026-05-11-huber-chroma-rag-is-dead-agentic-search\|Huber 2026]] | Vendor-of-the-substrate (Chroma CEO) | *"RAG is dead — the term, not the technique. Rag is banned. Vector database is also banned."* |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase ex-brain 2026]] | Earliest-vendor implementation | Implements hybrid search (BM25 + vector + scoring) as the substrate primitive without commenting on the *RAG is dead* claim |
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB 2026]] | Practical-engineering | GraphRAG = vector + graph in single query; *"adding graph to that helps you trim down the results"* |

### What's actually being retired

**The term, the conflation, and the application-architecture framing.** Specifically:

- **The term *RAG* is ambiguous**: *"If you ask 25 people to define RAG, they'll all define it a slightly different way"* (Huber). The same applies to *vector database* (Huber bans both).
- **The conflation of *RAG* with *application architecture***: the *"the entire system is a RAG pipeline"* framing is what dies. The *"vector retrieval is one substrate primitive among several"* framing is what survives.
- **The naive-RAG pipeline** (embed → store → retrieve top-k → inject → generate) doesn't survive contact with large heterogeneous corpora; the three named failure modes (below) explain why.

### What persists as substrate

- **Vector retrieval** as a substrate primitive (embedded as bytes in a multi-modal database alongside graph, full-text, scalar, JSON).
- **Hybrid search** (vector + full-text + scalar filtering, often combined with graph traversal and re-ranking) as the default retrieval pattern.
- **Re-ranking + the substrate-LLM split**: small specialised search-LMs (e.g. Chroma Context One) feed retrieved documents to large generation-LMs.

### Named failure modes (the union across sources)

The three sources that enumerate failure modes converge on **three classes** with overlapping subsets:

| Failure class | Mechanism | Named in |
|---|---|---|
| **Too much** (chunking + dense neighbourhood) | Over-retrieval; chunks fragment relationships; vector space saturated near common topics | Liu (chunking) + Huber (too much) + SurrealDB (dense neighbourhood + context clash) |
| **Too little** (passivity + missing context) | RAG waits for queries; never notices what's missing; can't detect contradictions across documents | Liu (passivity) + Huber (too little) |
| **Confusing** (contradictory chunks) | LLMs handle conflicting information poorly; retrieved chunks may contradict each other | Huber (confusing) + SurrealDB (context confusion) |

Plus two failure modes that emerge structurally rather than at the retrieval layer:

| Failure mode | Mechanism | Named in |
|---|---|---|
| **Re-derivation** | Every query starts from scratch; no compounding; *"RAG rereads the same books for every exam, never actually learning the material"* (Karpathy via Liu) | Liu (re-derivation) — the *what-LLM-Wiki-solves-that-RAG-cannot* failure mode |
| **Latency** | Embed + vector-search + re-rank + context-package compounds across tool-call loops | Liu (*"for an agent making 40 tool calls in a loop, those milliseconds compound into seconds"*) |

### The rebranding — context engineering

Two sources explicitly propose **context engineering** as the post-RAG vocabulary:

- **Huber**: *"Context engineering is important. Let's not call it RAG. We can call it context engineering. Ensuring that your agents have the right level of context at the right time is the name of the game."*
- **Karpathy** (via the LLM Wiki pattern): the *compile* operation is context engineering at ingest time; the *query* operation is context engineering at retrieval time.

The wiki's [[concepts/llm-wiki|llm-wiki]] concept page is the load-bearing anchor for this rebranding at the *application-level* layer; this synthesis anchors it at the *substrate* layer.

### The bitter-lesson direction

Huber's prediction: **context engineering itself will be folded back into the models.** *"Chroma just released a model trained to edit its own context."* Karpathy-compatible (Software 3.0: programs migrate into model weights over time). Convergence direction:

- Today (mid-2026): hand-crafted retrieval pipelines + hand-engineered chunking + hand-tuned re-ranking.
- Soon: models that **manage their own context window** — self-editing context; specialised retrieval sub-models (Chroma Context One pattern); the *bitter lesson* applied to context as it has been applied to features.

## Sources consulted

- [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] — "RAG Isn't Dead. But Something Is. Karpathy's LLM Wiki Explained"
- [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] — "RAG, LLM Wiki, or Gbrain? How Your Agent Remembers Changes Everything"
- [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber 2026]] — "RAG is Dead: Jeff Huber (Chroma) on Building Agentic Search"
- [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain 2026]] — "I Built a Knowledge Base That Thinks — Inspired by Karpathy's LLM Wiki"
- [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]] — "Knowledge Graphs for AI Agents (A Practical Guide)"
- [[2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker|Ebbelaar 2026]] — *"The Complete Guide to Hybrid Search in RAG (BM25 + Embeddings + Reranker)"* — practitioner code-walkthrough of the hybrid stack (BM25 + dense + RRF + reranker) on the BEIR FinanceQA dataset, with the closing prescription *"figure out for your corpus what the best combination of this is"*; the wiki's first complete-components-from-scratch operationalisation of the synthesis's *hybrid-architecture-is-the-right-answer* lesson #2.

Plus upstream:
- [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026 (Sequoia AI Ascent)]] — first-person confirmation of continued LLM-Wiki use; the upstream spec author.

## Lessons

Each a single transferable claim:

1. *"RAG is dead"* in the developer-internet sense means the **term** is dead; the **technique** persists as a substrate primitive.
2. **Hybrid architecture** is the right answer for any serious knowledge system — vector retrieval as substrate, with LLM Wiki / GraphRAG / agentic search layered above per the agent's job.
3. **Context engineering** is the rebranding the field is converging on; treat it as the umbrella construct, with RAG / vector retrieval / hybrid search as implementation primitives.
4. The naive-RAG pipeline (embed → store → retrieve → inject → generate) has **three named failure modes** that scale with corpus size: chunking destroys relationships, re-derivation prevents compounding, passivity prevents flagging contradictions.
5. **Specialised small models for retrieval beat gigabrain models for retrieval** on cost + speed + sometimes quality (Chroma Context One: 10× faster, 25× cheaper, on-par-or-better at search).
6. **File systems are bad databases** when used as agent substrates — concurrency, indexing, and search limitations make virtualized-file-systems-over-real-databases the cleaner pattern.
7. **Context engineering will fold back into models** (the bitter-lesson direction) — bet that hand-crafted retrieval pipelines are a transitional artifact.
8. **The cutover point between agentic-search and vector-RAG is corpus-size dependent**: small corpuses (30-50 files) work with grep-based agentic search; larger corpuses break grep and need semantic expansion.

## Open questions

- **The agentic-search-vs-RAG empirical disagreement.** [[Boris Cherny]] (per [[2026-05-08-running-an-ai-native-engineering-org|Fung 2026]]) advocates agentic search at Claude Code; Huber pushes back: *"question their incentives — who wants you to spend more money on tokens?"* Huber promised empirical data *"next week"* (mid-May 2026). The wiki's first substantive vendor disagreement on an empirical claim. **Open primary-source target**.
- **The Context Rot 45-page report itself** — Chroma's empirical underbidding of the *dumb zone* boundary (20K-120K tokens depending on use case). Primary-source ingest target.
- **The 2024 RAG-failure-points academic paper** Liu cites — primary-source target.
- **Swyx's "Oops, You Wrote a Database" article** — primary-source target on the file-system-as-incidental-database anti-pattern.
- **The hybrid-architecture-at-enterprise-scale implementation pattern** — Liu and Raju both flag that personal-LLM-Wiki at ~100 sources and enterprise-LLM-Wiki at 10K+ sources are different infrastructure-shaped problems. No enterprise-scale implementation source ingested yet.
- **GPT-5's jailbreak-resistance generalisation** — Blank ([[2026-05-11-blank-mit-6s191-three-laws-of-ai|MIT 6.S191]]) reports GPT-5 scores 100% on the six-bears benchmark vs GPT-4o 94% / GPT-4o-mini 78% / Gemini 2.5 Flash worst. Single-benchmark observation; open empirical question whether GPT-5 maintains 100% across other adversarial benchmarks.

## Related concepts and syntheses

- See [[syntheses/knowledge-architectures-for-llm-agents|knowledge-architectures-for-llm-agents]] for the broader synthesis on the RAG / LLM Wiki / Fat Skills three-way choice and the convergence prediction. This synthesis is the narrow-on-RAG companion to that broader treatment.
- [[concepts/llm-wiki|llm-wiki]] — the concept page on Karpathy's pattern; the *complement-not-replace* resolution makes the LLM Wiki coherent at scale by placing vector retrieval as substrate.
- [[knowledge-graphs]] — substrate primitive; GraphRAG (vector + graph in single query) is one operational instance of the hybrid resolution.
- [[agent-harness]] — the harness reads from a hybrid substrate (vector + graph + structured + filesystem); Huber's *file-systems-are-bad-databases* critique is direct harness-design guidance.

## Debates and supersession

None substantive. The five wiki sources are convergent on the *complement-not-replace* resolution. The internet's *"RAG is dead"* framing is dismissed by all five sources as missing the point.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "rag")
SORT file.name ASC
```
