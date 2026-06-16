---
type: source
kind: video
title: "Knowledge Graphs for AI Agents (A Practical Guide)"
author: ["SurrealDB"]
url: "https://www.youtube.com/watch?v=clhZES0M7no"
date_published: 2026-04-27
length: "~60:04 minutes (transcript ~244 grouped segments from 728 raw manual-track segments)"
raw: "../../raw/videos/surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md"
tags: [knowledge-graphs, graphrag, rag, vector-search, hybrid-search, etl, chunking-strategies, entity-extraction, surrealdb, surrealql, agentic-rag, ai-agents, agent-harness]
relationships:
  - type: supports
    target: knowledge-graphs
    via: "first wiki source specifically focused on knowledge graphs as the deterministic-grounding-substrate for LLM-based agents; full ETL pipeline (parsing/chunking/embedding/entity-extraction/relationship-extraction/deduplication/ontology); chunking-strategy taxonomy (recursive/structural/semantic/agentic); SurrealQL as single-language for vector + graph + full-text in one query"
  - type: supports
    target: agent-harness
    via: "knowledge graph as the persistent-context substrate the harness reads — extends the wiki's existing harness vocabulary from application-context (Chatterjee) and company-context (Hu) to relational-knowledge-context"
  - type: supports
    target: industrial-ai-agents
    via: "second-vendor anchor on knowledge-graph-as-agentic-substrate after Manditereza 2026 industrial vantage; SurrealDB provides the general-purpose-developer vantage on the same construct"
---

# Knowledge Graphs for AI Agents (A Practical Guide)

> RAG systems hit a wall as they scale: dense vector neighbourhoods produce context clash, hallucinations creep into answers, and high-dimensional embeddings stop being enough on their own. This session uses real-world examples — e-commerce search, customer support, agentic chatbots — to analyse where vector-only RAG breaks down, and the operational cost of stitching together separate vector, graph, and full-text stores. Martin (Solutions Engineer at SurrealDB) demonstrates how knowledge graphs ground LLM responses by adding deterministic structure on top of vectors, walking through the full ETL pipeline — parsing, chunking, embedding, entity and relationship extraction, deduplication, ontology.

(Channel description, [[SurrealDB]].)

A 60:04 webinar by **Martin** (Solutions Engineer at SurrealDB) on knowledge-graph-grounded RAG for AI agents. Published 27 April 2026 to the SurrealDB YouTube channel. **The wiki's first dedicated knowledge-graph-architecture source** with substantive vendor-practitioner depth on the full ETL pipeline. Manual caption track (`kind: manual`) selected for highest fidelity. 9 chapters.

## TL;DR

Four substantive contributions to the wiki:

1. **Why vector-only RAG breaks at scale — the named failure modes**: **context clash** (multiple chunks compete, all correct, but the LLM gets overloaded); **context confusion** (chunks contradict each other); **dense neighbourhood degradation** (high-dimensional space gets saturated near common topics; vector search returns too many similar-looking results). Martin: *"LLMs are very good storytellers ... but if they don't have factual data or context, they are just going to hallucinate."* The wiki's first **first-party-vendor articulation** of vector-only-RAG's breakdown modes as named failure patterns rather than handwaving.

2. **GraphRAG mechanics — vector + graph hops in a single query**: structural pattern Martin demonstrates with worked customer-support example. Embedded node (vector-searchable) connected via graph relationships to typed-other-nodes (product, troubleshooting-guide-domain, etc.). Query: *"my mouse Bluetooth isn't working"* → infer product+issue from prompt → vector-search-within-graph-subset reduces dense neighbourhood by trimming to product-related and troubleshooting-related nodes only. *"Adding graph to that helps you trim down the results."* The wiki's first **mechanistic walk-through** of GraphRAG (as opposed to handwaving the concept).

3. **The KG-ETL pipeline as a discipline**: **E**xtract (parsing + chunking + embedding + entity-extraction + relationship-extraction) → **T**ransform (deduplication + ontology + canonicalisation) → **L**oad (into the database). Each stage has named-strategy choices with explicit accuracy-vs-cost tradeoffs.

4. **Chunking-strategy taxonomy** — the wiki's first explicit framing of chunking as a *choose-by-tradeoff* discipline rather than a one-size-fits-all default:

   | Strategy | Mechanism | Cost | Accuracy |
   |---|---|---|---|
   | **Recursive** | Count ~1000 tokens, split, repeat | Cheapest | Lowest — may split mid-concept |
   | **Structural** | Split at paragraph/heading/page boundaries within token windows | Very cheap | Better than recursive |
   | **Semantic** | Embed paragraph N + paragraph N+1; if semantic similarity high → same chunk, else → split | Moderate (embedding LLM only) | High — *"really really cool, very well balanced"* |
   | **Agentic** | Big-LLM decides chunk boundaries per document | Expensive | Highest potentially |
   | **No-chunking** (emerging) | Don't chunk at extraction; let the LLM read the whole doc and chunk on-the-fly during RAG | Very expensive | Highest theoretically, limited by context window |

   Martin's recommendation: *"For now, I would suggest you just chunk your data in this extraction step"* — agentic and no-chunking are flagged as research-frontier rather than production-ready.

## What was actually ingested

Full 60:04 transcript including audience Q&A (Sebastian's GraphRAG question at 21:48). Manual caption track preserves dialogue cleanly; Martin is the only sustained speaker (chat-Q&A interjections rendered inline). Demo portion (43:23 onwards in Surrealist UI) is described verbally but visual content not captured.

## Knowledge graph — Martin's working definition

> *"The graph is a representation of your knowledge where you have concepts related to other concepts or entities related to entities using different types of relationships. But, of course, it not only stores data, but it also is used to navigate your knowledge graph. When we talk about doing multi-hop graphs, it's basically you're navigating the graph hopping from one entity to another to a specific relationship and can do many hops, depending on your use case."*

Two structural notes:

- **KGs are not new** — *"knowledge graphs is actually not a new thing now in the AI use cases. This became very popular a couple of decades ago already and was very popular in the Google search engine."* Martin grounds the construct historically; convergent with [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec's Stanford CS224W lecture]] from December 2023.
- **KGs vs vector stores — the easy-update property**: *"Knowledge graph is very easy to update, especially if you take decisions based on some knowledge you have in your graph. Then you can actually reflect that back. And in the future, you can have a bit of traceability."* The persistent-context property that distinguishes graphs from embeddings: deterministic, updatable, traceable.

## Two specimen KG examples — explicit vs inferred

Martin contrasts two KG-architecture styles:

| Style | Source data | Entity / relationship origin |
|---|---|---|
| **Explicit / transactional-mapped** | E-commerce database (relational tables: products → categories; products → reviews; products → orders; orders → customers) | Direct map from relational schema; entities = rows, relationships = foreign keys |
| **Hybrid / LLM-inferred** | Articles + documents | Some entities explicit (author, year) from headers; **chunks / concepts / companies / relationships** inferred by LLM from document body. E.g. *"leader-in"* relationship between company and industry-concept, where the industry-concept itself is LLM-inferred from chunks |

The choice depends on **dataset nature** + **use-case nature** (what questions will the chatbot answer?). Martin: *"sometimes a knowledge graph is not the ideal solution. It's sometimes not enough and sometimes just an overkill."* The wiki's first **principled-when-not-to-use-a-KG** framing.

## Why vector-only RAG breaks — the named failure modes

Martin's enumeration:

- **Context clash**: *"sometimes you have context clash or even context confusion where the LLM just gets a lot of chunks to generate an answer, but maybe there are too many chunks. All can be correct, but there are maybe too many chunks. And sometimes LLMs don't like big context and things that look like can contradict themselves."*
- **Dense neighbourhood degradation**: *"if you have a very big vector space, you may have very dense neighbourhoods. Imagine you get a lot of documents or chunks inserted in the same very specific neighbourhood in your vector store probably because they're talking about the same topic ... when there is a query that is also positioned in that specific point in the vector space, it's going to start having issues by picking which is the best chunk to use to generate an answer."*
- **Hallucination as the residual symptom**: *"LLMs are very good storytellers. They're very good at generating an answer. But if they don't have factual data or context from your RAG system, they are just going to hallucinate an answer."*

The **best-seller-product** worked example illustrates the failure mode at scale: vector-only RAG over a corpus including marketing slides, internal Slack messages, and Notion pages might *"hallucinate what the most popular products in your store are"* because there's no deterministic relational query into transaction data — only semantic similarity. *"It also would require some human to actually have presented about the best-seller products of this month so that information goes somewhere and gets ingested in your vector store."* The KG path: simple relational query into the transactional graph returns deterministic ground truth.

## When to use which — Martin's rule of thumb

> *"If your agent just needs to answer questions based on the manual, like troubleshooting or customer support, vector store could be enough. ... But if your agent needs to make decisions, follow policies, or manage complex workflows, then definitely you would need a knowledge graph, especially if you need explainability or traceability."*

Decision criteria:

- **Knowledge dynamism**: if knowledge is dynamic and you want future retrievals to be related to previous retrievals, KG is required.
- **Explainability / traceability**: KG required.
- **Decision-making with policies**: KG required.
- **Manual-driven Q&A only**: vector-only may suffice.
- **Scale of corpus heterogeneity**: more domains/products in same store → harder for vector-only.

## The KG-ETL pipeline as a named discipline

### Extraction

- **Parsing**: PDF → readable text. Multi-modal PDFs (images / tables / figures) are *"the worst case"*. Three image-handling strategies: caption-the-image and inline the caption; pass the image to a multimodal LLM; drop the image entirely.
- **Chunking**: five strategies (recursive / structural / semantic / agentic / no-chunking) with explicit accuracy-vs-cost tradeoffs detailed in the TL;DR.
- **Embedding**: vector embeddings for each chunk; **also** for entities (named in Martin's KG diagrams as *"blue nodes"* are vector-embedded; e.g. review + product + category in e-commerce KG).
- **Entity extraction**: LLM-driven extraction of named entities from chunks.
- **Relationship extraction**: LLM-driven extraction of typed relationships between entities.

Martin's insight on the *smaller-chunks-better* finding: *"there are research papers that have demonstrated that the smaller the context you give to an LLM, the better the result. Of course, it has to be small, very accurate, and precise, and contain all the information required to actually generate the answer."* Open primary-source target — Martin cites this verbally but doesn't name the paper.

### Transformation

- **Deduplication**: merge LLM-extracted entities that refer to the same real-world thing under different surface forms.
- **Ontology**: a canonical vocabulary of entity types and relationship types the LLM extracts against.
- **Canonicalisation**: normalise extracted entity properties.

### Loading

- Load the graph into the database (SurrealDB or equivalent).
- Martin emphasises co-locating vector + graph + full-text in **one database** to avoid stitching-together-stores operational cost.

## SurrealQL — vector + graph + full-text in one query

Martin demonstrates a unified query language where the same SurrealQL statement can:

- Vector-search to find nearest chunks to the prompt embedding;
- Graph-hop from chunks to related entities (multi-hop where useful);
- Full-text-search across selected nodes;
- Re-rank and deduplicate in the same query;
- Output JSON-shaped results via array/object functions.

The architectural claim: *"the beauty of having our own SQL-like query language is that we can have all those modalities in a single query."* The wiki's first **single-query-language-for-hybrid-search** worked example.

## Agentic RAG + tool calling (chapter 46:49)

Martin extends the discussion to agentic RAG where the LLM **chooses among retrieval tools** at runtime:

- Tool 1: vector search.
- Tool 2: graph traversal (multi-hop).
- Tool 3: full-text search.
- Tool 4: hybrid (combinations above).

The agent decides per-query which tool fits. *"The agent itself decides what information it needs."* Convergent with [[2026-05-09-chase-agent-development-lifecycle|Chase's]] *retrieval-as-Build-phase-decision* and with [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler's]] feed-forward harness elements.

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings\|Leskovec / Stanford CS224W (December 2023)]] | **The KG pair**: SurrealDB (practical-engineering vantage) + Leskovec (academic-foundation vantage). Two-source convergence threshold met for **[[knowledge-graphs]]** as a concept page (alongside earlier industrial mention in [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza]] + agentic-memory in [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic]]) |
| [[2026-02-01-manditereza-ontology-driven-industrial-ai\|Manditereza 2026 (HiveMQ industrial)]] | Both name knowledge-graphs as the deterministic-grounding-substrate for LLM agents. Manditereza: industrial-OT vantage with three-tier semantic data layer; SurrealDB: general-purpose-developer vantage with KG-ETL pipeline. **Two-vendor convergence** on KG as harness-substrate |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026 (TDS / Neo4j)]] | Bratanic uses KG as **agentic memory** (linked-list session graph; dream-phase distillation). SurrealDB uses KG as **agentic retrieval** (vector + graph hops for RAG). Same data structure, two distinct uses in the agent runtime |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | Chatterjee's Context layer (assembling the right context for each request) is *where the KG retrieval lives* in the harness; the KG itself is the **persistent-context substrate** the Context-layer reads from |
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu / Y Combinator 2026]] | Hu's *queryable organization / legibility-to-AI* is **the company-scale analog** of Martin's KG-as-retrieval-substrate. The intelligence layer Hu describes at the company scale operates on the same kind of artifact-rich queryable-structure as Martin's KG at the application scale |
| [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie / Braintrust 2025]] | Guthrie's eval discipline applies *to* the GraphRAG retrieval results — score the relevance of each retrieved subgraph; offline-online-flywheel applies identically. KG-RAG and eval discipline compose |
| [[2026-05-09-chase-agent-development-lifecycle\|Chase / LangChain ADLC 2026]] | Chase's Build-phase *retrieval / context engineering* component is where the KG-ETL discipline lives in the ADLC; Martin supplies the operational mechanics Chase's framework references |

### Contradictions

None substantive. Martin's framing is operator-prescriptive; no opposing source in the wiki.

## Linked entities and concepts

**Concept pages affected**:

- **[[knowledge-graphs]]** — **NEW CONCEPT PAGE created in this ingest** (this source + Leskovec). Anchors KG as a wiki concept distinct from but related to agent-harness, RAG, and agentic-memory.
- [[agent-harness]] — KG as persistent-context substrate for the Context layer.
- [[industrial-ai-agents]] — cross-link to the new knowledge-graphs page.

**Dangling** (single-source first-mention, deferred):

- **Martin** — SurrealDB Solutions Engineer; presenter. Surname not given in transcript.
- **SurrealDB** — multimodal database (relational + document + time-series + geospatial + vector + full-text + graph + key-value); ~31k GitHub stars; Rust-based; multi-deployment-modal (browser-WASM / edge / distributed). **Strong promotion candidate** as a vendor entity given the substantive ingest.
- **SurrealQL** — SurrealDB's SQL-like query language for the multi-modal queries.
- **Surrealist** — the SurrealDB browser-based UI demoed at 43:23.
- **Sebastian** — audience-Q-asker (chat). First-name only.
- **Santi** — audience member (chat greeting); first-name only.

**Concept candidates surfaced (not yet promoted)**:

- *Context clash / context confusion* — Martin's named vector-only-RAG failure modes. Single-source as named-failure-mode. Promotion candidate on second-source mention.
- *Dense neighbourhood degradation* — Martin's framing. Single-source.
- *Chunking-strategy taxonomy (recursive/structural/semantic/agentic/no-chunking)* — Martin's explicit framing of chunking-as-a-discipline. Single-source.
- *Hybrid search in a single query (vector + graph + full-text)* — Martin's architectural claim. Single-source.
- *Agentic RAG with retrieval-tool-selection* — Martin's framing. Single-source; convergent-but-distinct from Chase's *retrieval as Build-phase decision*.

## Open questions raised by this source

- **The "smaller chunks better" research finding** — Martin cites verbally; primary-source target.
- **SurrealQL hybrid-query syntax** — primary-source target: SurrealDB documentation.
- **The agentic-chunking research frontier** — *"already some papers"* per Martin; primary-source target.
- **Multi-modal PDF parsing tooling** — Martin describes the problem extensively; primary-source target on best-in-class parsers.
- **Ontology design as a discipline** — Martin names ontology as an ETL stage; the *how* of ontology design is not detailed. Primary-source target.
- **SurrealDB vs Neo4j vs PostgreSQL+pgvector vs Pinecone for KG-RAG workloads** — comparative vendor benchmarks would let the wiki triangulate Martin's single-vendor framing.
