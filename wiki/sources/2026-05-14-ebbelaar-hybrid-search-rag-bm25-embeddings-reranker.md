---
type: source
kind: video
title: "The Complete Guide to Hybrid Search in RAG (BM25 + Embeddings + Reranker)"
author: ["Dave Ebbelaar"]
publisher: "Dave Ebbelaar (Datalumina) YouTube channel"
url: "https://www.youtube.com/watch?v=XvKiTfd6Xvo"
date_published: 2026-05-14
date_ingested: 2026-05-25
length: "~59:17 minutes (transcript ~640 ASR lines across 19 chapters)"
raw: "../../raw/videos/the-complete-guide-to-hybrid-search-in-rag-bm25-embeddings-reranker.md"
tags: [rag, hybrid-search, bm25, dense-embeddings, reciprocal-rank-fusion, rrf, reranker, beir-benchmark, financeqa, eval-driven-retrieval-design, knowledge-architectures, sparse-vs-dense, dave-ebbelaar, datalumina, retrieval-engineering, code-walkthrough]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers
    via: "**Practitioner-altitude operationalisation of the *RAG is complementary, not dead* thesis.** Liu (medium-altitude trade-press, April 2026): RAG persists as the *substrate-of-retrieval* under the LLM-Wiki / Gbrain conceptual frames; not replaced, recomposed. Ebbelaar (YouTube practitioner tutorial, May 2026) gives the **concrete code-walkthrough operationalisation** of what *hybrid retrieval* looks like in production in mid-2026: **BM25 (sparse keyword) ∪ dense embeddings → Reciprocal Rank Fusion → cross-encoder reranker on the union top-K**, with the BEIR/FinanceQA dataset as the evaluation benchmark. *'This is really the production stack that works and wins in 2026 when you want to build serious production-ready systems.'* The framing is *anti-monolithic retrieval* — hybrid is the working pattern — which is the operational form of Liu's *RAG-as-substrate-of-many-architectures* claim."
    confidence: 0.7
  - type: supports
    target: 2026-05-11-huber-chroma-rag-is-dead-agentic-search
    via: "**Productive complement on the *what kind of retrieval pattern matters in 2026* question.** Huber (Chroma, May 11): *agentic search* as the emerging replacement for static RAG pipelines — the agent issues queries iteratively, conditions later queries on earlier results, and selects what to retain. Ebbelaar (May 14, three days later): the *retrieval primitives the agentic-search agent calls under the hood* — hybrid (BM25 + dense + RRF + rerank) is the production-grade primitive. The two sources stack: Huber names the orchestration layer; Ebbelaar names the retrieval-primitive layer the orchestration calls. Both reject the *naive-vector-search RAG* default of 2024."
    confidence: 0.6
  - type: supports
    target: 2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair
    via: "**Eval-driven retrieval design as a sub-genre of eval-driven AI engineering.** Guthrie (Braintrust 2025) names the *eval-as-engineering-discipline* doctrine. Ebbelaar operationalises it specifically for *retrieval system design*: the closing chapter (*Evaluating Retrieval Quality* / *Tuning for Your Own Data*) walks through running the assembled hybrid stack on the BEIR FinanceQA queries-and-corpus pairs and comparing top-K hit rates across (BM25 alone / dense alone / hybrid / hybrid+rerank), then **prescribes finding the right combination for your corpus** rather than defaulting to the full stack. *'Do you always need this entire stack? And the answer is no. So you should figure out for your corpus what the best combination of this is.'* The retrieval-engineering analog of Wolfe/Khan's *eval-driven AI engineering* doctrine."
    confidence: 0.6
  - type: supports
    target: 2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide
    via: "**Two 2026 *production-retrieval-stack practical guide* anchors at different infrastructure altitudes.** SurrealDB (April 27): *single-query-language-for-hybrid-search* + knowledge-graphs for agentic RAG; multi-modality (graph + vector + text) in one query. Ebbelaar (May 14): the *components-from-scratch* version — BM25 + dense embeddings + RRF + reranker in Python with HuggingFace BEIR datasets. SurrealDB shows what a *production-database-vendor-side* hybrid stack looks like; Ebbelaar shows what a *roll-your-own-components* hybrid stack looks like. Both papers anchor the *hybrid-retrieval-as-the-production-pattern* claim from different vantages."
    confidence: 0.55
confidence: 0.7
last_confirmed: "2026-05-25"
---

# The Complete Guide to Hybrid Search in RAG (BM25 + Embeddings + Reranker)

> Want to learn real AI Engineering? Go here: https://go.datalumina.com/QpP01LX

(Channel description, [[Dave Ebbelaar]] / [[Datalumina]].)

A 59:17 YouTube practitioner tutorial published 14 May 2026 to the [[Dave Ebbelaar]] channel (Datalumina founder; AI engineering consultancy). 5,803 views (small audience — practitioner-targeted technical tutorial, not viral content). Auto-generated ASR transcript with 19 chapter markers; chapter list runs *Hybrid Retrieval Overview → Meet the Finance QA Data → Exploring Queries and Corpus → Mapping Questions to Documents → Retrieval Pipeline Roadmap → BM25 Keyword Retrieval → Tokenizing the Corpus → Building the BM25 Index → Querying with BM25 → Why Dense Embeddings Help → Creating Dense Embeddings → Dense Search in Python → Dense Retrieval Compared → Reciprocal Rank Fusion → Fusing Search Results → Adding the Re-Ranker → Re-Ranking Hybrid Candidates → Evaluating Retrieval Quality → Tuning for Your Own Data.*

**Companion artifact**: the [GitHub repository](https://github.com/daveebbelaar/ai-cookbook/tree/main/knowledge/hybrid-retrieval) (under `ai-cookbook`) ships the full Python codebase walked through in the video. Each retrieval technique has an accompanying `docs/` markdown with formulas + math + original-paper references for deeper study.

**Authors / dangling list.** First wiki source by [[Dave Ebbelaar]] and first wiki appearance of [[Datalumina]]; per the [[../../CLAUDE|author-entity promotion rule]] (second-source promotion), both stay on the dangling list at this ingest:

- **Dangling** (single-source mention, deferred): Dave Ebbelaar (founder of Datalumina; AI-engineering YouTuber + freelancer-track educator), Datalumina (AI development consultancy + GenAI Accelerator six-week training).

## TL;DR

Four substantive contributions warrant ingest:

1. **The hybrid-retrieval production stack assembled from scratch in code** — **BM25 (sparse keyword)** ∪ **dense embeddings (semantic similarity)** → **Reciprocal Rank Fusion** (combines the two ranked lists into a single fused ranking) → **cross-encoder reranker** (re-scores the top-K fused candidates with a high-precision but high-latency model). Ebbelaar's framing claim: *"This is really the production stack that works and wins in 2026 when you want to build serious production-ready systems."* The wiki's first **complete-components-from-scratch operationalisation** of hybrid retrieval at practitioner altitude.

2. **The BEIR / FinanceQA dataset as the evaluation harness** — the BEIR benchmark family (Benchmarks for Information Retrieval) supplies *(query, relevant-corpus-document-ids, corpus)* triples that turn retrieval into a measurable engineering problem. Ebbelaar uses the FinanceQA subset (financial questions paired with answer documents) as a stand-in for *"company documents, your sales playbook, customer support questions, pretty much anything that you want to put in your corpus."* The wiki's first source explicitly using BEIR for retrieval evaluation in a practitioner tutorial.

3. **The eval-driven retrieval-design discipline** — the closing chapters (*Evaluating Retrieval Quality* and *Tuning for Your Own Data*) operationalise the principle that *the right combination of (BM25 / dense / RRF / rerank) depends on your corpus*. Ebbelaar's final framing claim: *"Do you always need this entire stack? And the answer is no. So you should figure out for your corpus what the best combination of this is. And I've now showed you an experimental setup that you can use to do this."* The wiki's *retrieval-engineering*-altitude analog of [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie's eval-driven AI engineering doctrine]] and [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|the Anthropic eval-as-engineering-discipline cluster]].

4. **The anti-naive-vector-search stance** — the tutorial's hidden argument is structurally anti-*"just embed everything and use cosine similarity"*. Each component is justified individually: BM25 catches exact terms / identifiers / rare words but misses paraphrases; dense embeddings catch semantic similarity but miss exact matches; RRF fuses their complementary strengths; reranker provides high-precision final scoring on top-K candidates. *"This is rather naive way of searching and retrieving information but in some scenarios can work highly effective"* (Ebbelaar on BM25 alone). The framing extends the *RAG-isn't-dead-but-naive-RAG-is* thesis the wiki has been building since the [[is-rag-dead|is-rag-dead synthesis]] closed (May 12).

## What was actually ingested

Full transcript across 19 chapters. The video is unusually code-dense — the substantive material is the *progression of techniques* (BM25 → dense → RRF → rerank) and the *evaluation-driven tuning rationale*, both of which survive in the transcript text alongside the (unavailable in transcript) Jupyter / Python code being walked through. The companion GitHub repo provides the executable artifact for anyone re-implementing.

## The hybrid-retrieval stack — chapter-by-chapter

### Why hybrid: complementary strengths of BM25 and dense embeddings

**BM25** (chapter 10:05–23:55) is the wiki's first detailed practitioner treatment of *sparse retrieval* (sometimes called *lexical retrieval*). The Ebbelaar framing: *"BM25 also known as sparse retrieval. We'll do keyword overlaps and then there is a weighting mechanism that is applied to it to actually perform the math to see what we need to retrieve. This is really good for catching exact terms, identifiers, rare words, but it will miss paraphrases."* The implementation walks through tokenisation, index construction (`rank_bm25`), and querying.

**Dense embeddings** (chapter 23:56–36:44) is the more-familiar 2023-era *semantic-similarity-via-embedding-distance* technique. Ebbelaar's framing of why it matters: paraphrase and synonym retrieval that BM25 fundamentally cannot do — *"BM25 will not help me retrieve this"* on a paraphrase query.

### Reciprocal Rank Fusion (RRF) — the fusion operator

Chapter 37:12–43:55. **RRF** combines two (or more) ranked lists from independent retrievers into a single ranking. The formula: for each document, summed across retrievers, *1 / (k + rank)* where *k* is typically 60 and *rank* is the document's position in that retriever's results. Documents that appear high in *either* list get a high fused score; documents that appear in *both* lists get a higher score. The wiki's first explicit treatment of RRF as the operational fusion mechanism for hybrid retrieval. *"The beauty of RRF is it doesn't need calibrated scores — only ranks — so it works across heterogeneous retrieval methods."*

### The cross-encoder reranker

Chapters 43:56–49:35. The **reranker** is a (small, fast) transformer trained specifically to score *(query, document)* pairs with high precision. Ebbelaar's implementation uses the `sentence-transformers` cross-encoder family. The reranker runs only on the top-K candidates from the fused retriever (typical K = 50–100), since its per-pair inference cost is much higher than the retriever's per-document indexing cost. This is the *third-stage precision lift* on top of the retrieval-recall foundation.

### Evaluation and the *tuning-for-your-corpus* discipline

Chapters 49:36–end. Ebbelaar runs the assembled stack on the BEIR FinanceQA queries-and-corpus pairs and computes top-K hit-rate metrics across configurations (BM25 alone / dense alone / RRF-hybrid / RRF-hybrid + reranker). Final empirical claim: the reranker step alone *"is literally all that we add to it and because of that we jump to this particular score."* But the closing message is the *tuning discipline*: *"You should figure out for your corpus what the best combination of this is. And I've now showed you an experimental setup that you can use to do this."* — explicitly disclaiming the *full-stack-is-always-best* default.

## Substantive contributions to the wiki

**To the [[is-rag-dead|is-rag-dead synthesis]]:** the source instantiates the synthesis's closing claim — *"naive vector-only RAG is dead; hybrid + reranking + eval-driven tuning is the production replacement"* — at a practitioner code-walkthrough altitude. Pairs with [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber/Chroma's *agentic search* framing]] (the orchestration layer above) and [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB's single-query-language hybrid stack]] (the database-side framing).

**To the [[knowledge-architectures-for-llm-agents|knowledge-architectures synthesis]]:** the wiki's first complete-from-scratch operationalisation of the *RAG-as-hybrid-retrieval-substrate* architecture. The four-component stack (BM25 + dense + RRF + rerank) is the operational refinement of the *RAG substrate* the synthesis names as one of three knowledge architectures alongside LLM-Wiki and Gbrain.

**To [[agent-harness]]:** the source instantiates the harness's *retrieval / context-gathering* layer with a concrete production-stack walkthrough. The chapter sequence (build → measure → tune) mirrors the harness's eval-driven-engineering discipline at the retrieval-component scale.

## What's *not* in this source

- **No agentic-RAG orchestration.** Ebbelaar's stack is *static-pipeline* hybrid retrieval — the queries are pre-defined and the retrieval pipeline runs once per query. He does not cover [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber's *agentic search*]] (where an agent decides which queries to run, conditions later queries on earlier results, etc.). The two sources are complementary, not redundant.
- **No knowledge-graph or graph-RAG.** Pure text-document retrieval. Graph-aware retrieval is covered by [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]] and [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase Ex-Brain]] at different altitudes.
- **No latency / throughput / cost numbers** beyond the implicit *"reranker is more expensive per-pair, so run on top-K only."* For production cost numbers, the wiki has [[2026-05-05-google-gemini-file-search-multimodal|Gemini File Search]] vendor-side anchors.
- **No multi-modal retrieval.** Text-only. Multimodal retrieval is named explicitly by [[2026-05-05-google-gemini-file-search-multimodal|Gemini File Search]] as a 2026 production pattern.

## Open questions for next ingest

- Does the **(BM25 + dense + RRF + rerank) stack** survive the move to *agentic search* orchestration patterns, or does it get supplanted by **iterative-query-and-condition** retrieval?
- What is the **right K** for the rerank stage in production — Ebbelaar uses 50–100 in the tutorial; production-cost-vs-recall tradeoffs are not measured here.
- Does **RRF still win** when the retrievers produce *calibrated scores* (e.g. logistic-regression-fused) rather than ranks? The 2026 literature on score-fusion vs rank-fusion is not covered here.
