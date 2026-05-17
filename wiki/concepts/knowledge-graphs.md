---
type: concept
aliases: ["knowledge graph", "KG", "knowledge graphs", "knowledge-graph", "kg"]
tags: [knowledge-graphs, kg, graph-rag, ai-grounding, ontology, relational-data, agent-harness, agentic-memory, etl, entity-extraction, relationship-extraction]
confidence: 0.88
last_confirmed: "2026-05-17"
accessed_at: "2026-05-17"
source_count: 6
relationships:
  - type: part-of
    target: agent-harness
    via: "knowledge graphs are one of the persistent-context substrates the harness reads from — Chatterjee's Context layer; Bratanic's dream-phase memory; SurrealDB's GraphRAG retrieval"
  - type: uses
    target: foundation-models
    via: "LLM-driven entity-extraction and relationship-extraction populate the KG; LLMs read graph-traversal results as part of grounded-RAG generation"
quality_score: 1
---

# Knowledge Graphs

**Knowledge graphs** — heterogeneous graphs with typed nodes (entities) and typed edges (relationships) used as deterministic, queryable, updatable substrates for machine reasoning and AI-agent grounding. The data structure is not new — knowledge graphs were popular in industrial search (Google Knowledge Graph, Amazon's product graph, Facebook Graph API) and academic research (FreeBase, Wikidata, DBpedia) for decades before the LLM era. What changed in 2024–2026 is the **role** they play: from *standalone-search-result-enrichment* to *deterministic-grounding-layer-for-LLM-agents*.

The wiki holds four sources engaging this concept substantively, from four distinct vantages:

- **Academic-foundation vantage**: [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec's Stanford CS224W lecture (December 2023)]] — the wiki's pre-GenAI-era theoretical reference. KG-completion task formulation; shallow-embedding methods (TransE / TransR / DistMult / ComplEx); relation-pattern taxonomy (symmetric / antisymmetric / inverse / composite / 1-to-N); FreeBase scale-and-incompleteness empirical anchor.
- **Industrial-OT vantage**: [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza 2026 (HiveMQ)]] — knowledge graphs as the **semantic foundation** for industrial AI agents. Three-tier semantic data layer (semantic model + domain ontologies + knowledge graph); four structural pillars (object types / properties / link types / action types).
- **Agentic-memory vantage**: [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026 (TDS / Neo4j)]] — knowledge graphs as the **persistent-memory substrate** across agent sessions. Linked-list session graph; dream-phase distillation into durable Markdown memories; hooks-as-portable-primitive across harnesses.
- **Practical-engineering vantage**: [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB / Martin 2026]] — knowledge graphs as the **GraphRAG retrieval substrate** for production AI agents. Full ETL pipeline (parsing / chunking / embedding / entity-extraction / relationship-extraction / deduplication / ontology); chunking-strategy taxonomy; SurrealQL hybrid-query mechanics.

## Working definition

Composite from the four wiki sources:

- **Heterogeneous graph**: typed nodes (entities — Leskovec) + typed edges (relationships — Leskovec). The data structure is a heterogeneous graph; *knowledge graph* is the interpretive label.
- **Encodes domain knowledge**: *"we encode our knowledge about a given domain in this type of graphical form"* (Leskovec). Distinguishes a KG from a generic graph by *intent*, not *structure*.
- **Supports reasoning + retrieval + ML integration**: *"a knowledge base over which you can reason, over which you can retrieve, and allows you to bring in the knowledge to your machine learning model"* (Leskovec).
- **In the LLM era — adds deterministic structure on top of vectors** (Martin): *"LLMs are very good storytellers ... but if they don't have factual data or context, they are just going to hallucinate. ... The idea is to put them together — a very good storyteller generating answers, but a very good knowledge graph that as deterministic as possible generates good contexts."*

## Why vector-only RAG breaks — what KGs add ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]])

Martin's three named failure modes for vector-only RAG at scale:

| Failure mode | Mechanism | KG remediation |
|---|---|---|
| **Context clash** | Too many similar-score chunks compete for inclusion; all could be correct but the LLM gets overloaded | Graph relationships trim retrieval to *typed-relevant-subgraph* only |
| **Context confusion** | Retrieved chunks contradict each other; LLM picks the wrong one | Deterministic graph traversal returns the *authoritative* fact, not a similarity-score nearest neighbour |
| **Dense neighbourhood degradation** | Vector space saturated near common topics; many candidates within distance threshold | Graph-trimmed vector search reduces candidate-set size while preserving topical fit |

Martin's structural framing: *"adding graph to that helps you trim down the results."* The KG isn't a replacement for vector search — it's a **constraint on the vector-search-space** that adds deterministic-structure-on-top-of-similarity-score-retrieval.

## GraphRAG — the unified-query mechanic

[[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]]'s GraphRAG demonstration:

1. Embed the user prompt as a query vector.
2. Vector-search for nearest chunk(s) in the KG (chunks are vector-embedded nodes).
3. **Multi-hop graph traversal** from nearest chunks to related entities (typed edges).
4. Combine vector + graph results into the LLM's context window.
5. (Optional) full-text search overlay for additional precision.
6. LLM generates grounded response.

In SurrealQL, all six steps can be expressed as a **single query** — *"the beauty of having our own SQL-like query language is that we can have all those modalities in a single query."* The wiki's first single-query-language-for-hybrid-search worked example.

## The KG-ETL pipeline as a named discipline ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]])

| Stage | Sub-steps | Strategy choices |
|---|---|---|
| **Extract** | Parsing → Chunking → Embedding → Entity extraction → Relationship extraction | PDF parsing strategies; **chunking taxonomy** (recursive / structural / semantic / agentic / no-chunking — accuracy vs cost); LLM-driven entity + relationship extraction |
| **Transform** | Deduplication → Ontology mapping → Canonicalisation | Merge LLM-extracted entities referring to the same real-world thing; canonical typed-vocabulary for entities and relationships |
| **Load** | Insert into the database | Co-locate vector + graph + full-text to avoid stitching-stores operational cost |

The pipeline is **the practical engineering form of Leskovec's academic KG-construction question**. Leskovec: *"how do you bring any structure to this 38,000 different relationships"* — ontology design is hard. Martin: chunking, entity-extraction, and relationship-extraction are all LLM-assisted now, lowering the marginal cost of KG construction below the pre-GenAI-era hand-curation cost.

## Chunking strategy taxonomy ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]])

| Strategy | Mechanism | Cost | Accuracy |
|---|---|---|---|
| **Recursive** | Count ~1000 tokens, split, repeat | Cheapest | Lowest — may split mid-concept |
| **Structural** | Split at paragraph / heading / page boundaries within token windows | Very cheap | Better than recursive |
| **Semantic** | Embed adjacent paragraphs; high similarity → keep together; low similarity → split | Moderate (embedding LLM only) | High — *"really really cool, very well balanced"* |
| **Agentic** | Big-LLM decides chunk boundaries per document | Expensive | Highest potentially; research frontier |
| **No-chunking** | Don't chunk at extraction; let the LLM read the whole doc and chunk on-the-fly during RAG | Very expensive | Highest theoretically; limited by context window |

Martin's production recommendation: *"For now, I would suggest you just chunk your data in this extraction step."* Semantic chunking is the practical sweet spot; agentic and no-chunking remain research-frontier as of April 2026.

## Decision criteria — when to use a KG (vs vector-only)

Martin's rule of thumb ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]]):

- **Manual-driven Q&A on a single product line** → vector-only may suffice.
- **Multiple products / domains / use-cases in the same store** → graph trimming becomes valuable.
- **Decisions / policy-following / complex workflow** → KG required.
- **Explainability / traceability needed** → KG required.
- **Dynamic knowledge where future retrievals depend on past decisions** → KG required (decisions stored back into the graph for future retrieval).

## KG completion task — the canonical academic formulation ([[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec 2023]])

> *"Given a head and a relation type, predict the missing tails."*

Example: `(J.K. Rowling, genre, ?) → Fantasy / Young-Adult Fiction`.

The task **generalises link-prediction to heterogeneous-relation graphs**. The wiki's GraphRAG-era practitioner sources don't operate directly on KG completion — they treat the KG as a *given* and focus on retrieval. But the **incompleteness problem** the task addresses motivates the LLM-driven entity-extraction stage of the SurrealDB ETL pipeline: real-world KGs are sparse, and LLMs help fill in missing edges at lower cost than human curation.

## Shallow-embedding methods and relation-pattern coverage ([[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec 2023]])

| Method | Embedding form | Symmetric | Antisymmetric | Inverse | Composite | 1-to-N |
|---|---|---|---|---|---|---|
| **TransE** | `h + r ≈ t` (Euclidean translation) | ✗ | ✓ | ✓ | ✓ | ✗ |
| **TransR** | Project entities into relation-specific space, then translate | ✓ | ✓ | ✓ | ✗ | ✓ |
| **DistMult** | Bilinear scoring (Hadamard product) | ✓ | ✗ | ✗ | ✗ | ✓ |
| **ComplEx** | Complex-valued embeddings; bilinear with conjugate | ✓ | ✓ | ✓ | ✗ | ✓ |

The matrix is **the canonical pedagogical artifact** of the shallow-embedding KG literature: no single method covers all relation patterns. **The pattern taxonomy is wiki-load-bearing** — it transfers to other contexts where typed-relationship reasoning matters (LLM-driven relationship-extraction in GraphRAG ETL; multi-hop traversal semantics in agentic RAG).

## Knowledge graphs in the LLM-era agentic stack

The four wiki sources address KGs at different layers of the agentic stack:

| Layer | Source | KG role |
|---|---|---|
| **Foundation theory** | Leskovec 2023 | Mathematical formulation of the construct (heterogeneous graph; KG completion; shallow embeddings) |
| **Industrial reasoning substrate** | Manditereza 2026 | Three-tier semantic data layer underlying industrial AI agents (OT/IT convergence) |
| **Agentic memory** | Bratanic 2026 | Persistent memory across agent sessions (linked-list session graph + dream-phase distillation into Markdown) |
| **GraphRAG retrieval** | SurrealDB 2026 | Deterministic-grounding-substrate for production RAG (vector + graph in one query) |

The KG construct is **maximally polymorphic**: same data structure, four distinct uses across the agentic stack. This is **structurally analogous to how MQTT became a polymorphic primitive across industrial protocols** ([[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza 2026]]'s unified namespace) — the right data structure adopted in multiple layers compounds organisational leverage.

## Cross-source positioning

- **Knowledge graphs are not new**. Both Leskovec (academic, 2023) and Martin (practical, 2026) explicitly anchor the construct historically — *"this became very popular a couple of decades ago already and was very popular in the Google search engine"* (Martin). The GenAI-era story is **adoption-curve compression**, not *invention*.
- **Convergence with [[agent-harness]]**: KGs are one of the persistent-context substrates the harness reads from. Specifically, they sit in Chatterjee's *Context* layer (assembling the right context per request) and feed Chatterjee's *Compounding* layer (telemetry-feeds-learning) when used as agent memory.
- **Convergence with [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu 2026]]'s queryable-organization**: Hu's *"the whole organization should be legible to AI"* operates on the same *make-the-substrate-legible-and-queryable* principle as Martin's *"the graph is a representation of your knowledge."* At company scale (Hu) and at application scale (Martin) the same architectural choice repeats.
- **The LLM-driven entity-extraction inversion**: pre-GenAI-era, KGs were expensive to build (hand-curation; ontology engineers). LLMs invert that economics — *"chunks, concepts, and probably companies are things that are going to be inferred by an LLM"* (Martin). The KG-construction-cost-curve drops by ~1-2 orders of magnitude.

### KG-as-attention-direction (Nodus Labs / InfraNodus, April 2026)

The wiki's prior KG sources ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]], [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza]], [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec]], [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic]]) frame KGs as **retrieval substrates** (graph-traversal supplements or replaces vector similarity). [[2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus|Nodus Labs / InfraNodus]] introduces a **second use mode** for KGs in agent workflows: **attention direction**.

The mechanism: compute clusters and cluster-pair gaps from concept-page co-occurrence; emit a **gap-prompt** (structured representation of two disconnected clusters + the densest source extracts from each); paste the gap-prompt back to the LLM and ask it to generate cluster-bridging insights using the underlying source documents. *"I point the LLM's attention to the gap that exists. I provide the underlying structure. I give it some context."* The KG is not retrieving anything; it is **telling the LLM where in its existing context to look harder**.

This complements rather than replaces KG-as-retrieval. A mature stack carries both: graph-traversal for deterministic retrieval (Martin) + gap-analysis for non-generic ideation (Paranyushkin / InfraNodus).

## Related concepts

- [[agent-harness]] — KGs are one of the persistent-context substrates the harness reads. The Context + Compounding layers in Chatterjee's 4-layer model are where KG retrieval lives.
- [[agentic-engineering]] — knowledge-graph-aware retrieval is one of the operational disciplines an agentic engineer needs.
- [[industrial-ai-agents]] — KGs are load-bearing in industrial-OT settings (Manditereza); see that page for the OT-specific framing.
- [[generative-ai]] — the LLM-era is what gave KGs their second life as agent-grounding substrates.
- [[foundation-models]] — LLMs drive KG entity-extraction and relationship-extraction in the modern ETL pipeline.

## Open questions

- **GraphRAG benchmarks** — Martin claims qualitative improvements over vector-only RAG; empirical benchmarks (which KG-RAG architectures, on which corpora, with which retrieval metrics) would substantiate. Open primary-source target.
- **Ontology design as a discipline** — both Leskovec and Martin name ontology design as load-bearing but neither details the *how*. Worth tracking primary sources on ontology-as-engineering-discipline.
- **The chunking-strategy decision frontier** — Martin's recommendation is *"semantic chunking is the practical sweet spot."* As LLM costs drop, when does agentic or no-chunking become production-ready? Open empirical question.
- **KG-embedding methods in the LLM era** — TransE / TransR / DistMult / ComplEx (Leskovec) were designed for static KGs. Do they transfer to dynamic LLM-populated KGs, or does the LLM era favour different embedding architectures? Open primary-source target.
- **The KG vs vector-only decision** — Martin's rule of thumb is practitioner-prescriptive. A controlled comparison (same corpus, same questions, both architectures, measured outcome) would let the wiki engage the tradeoff empirically.
- **GraphRAG-vs-classical-KG-embedding** — production deployments of GraphRAG (SurrealDB / Neo4j / others) vs classical KG-embedding completion (TransE family). Different paradigms; comparative evaluation an open question.

## Debates and supersession

None substantive yet — the four wiki sources are aligned in framing. The construct itself is decades old (Leskovec) and well-established; the LLM-era re-adoption is what's recent (Martin / Manditereza / Bratanic) and the four sources converge rather than contradict.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "knowledge-graphs") OR contains(tags, "kg") OR contains(tags, "graph-rag")
SORT file.name ASC
```
