---
type: source
kind: video
title: "Stanford CS224W: Machine Learning w/ Graphs I 2023 I Knowledge Graph Embeddings"
author: ["Stanford Online"]
url: "https://www.youtube.com/watch?v=isI_TUMoP60"
date_published: 2023-12-07
length: "~70:04 minutes (transcript ~299 grouped segments from 1247 raw manual-track en-US segments)"
raw: "../../raw/videos/leskovec-stanford-cs224w-knowledge-graph-embeddings.md"
tags: [knowledge-graphs, kg-embeddings, transe, transr, distmult, complex, kg-completion, contrastive-loss, freebase, wikidata, stanford-cs224w, academic-foundation]
relationships:
  - type: supports
    target: knowledge-graphs
    via: "academic-foundation source on knowledge graph theory — KG completion task formulation; shallow-embedding methods (TransE, TransR, DistMult, ComplEx); relation pattern taxonomy (symmetric/antisymmetric/inverse/composite/1-to-N); contrastive/triplet loss training; FreeBase / Wikidata as canonical academic benchmarks. The wiki's pre-GenAI-era foundational reference for the construct the LLM-era practitioner sources operate on top of"
---

# Stanford CS224W: Knowledge Graph Embeddings

> To follow along with the course, visit the course website: https://snap.stanford.edu/class/cs224w-2023/
>
> Jure Leskovec — Professor of Computer Science at Stanford University.
>
> Graduate Course: https://online.stanford.edu/courses/cs224w-machine-learning-graphs
> Professional Course: https://online.stanford.edu/courses/xcs224w-machine-learning-graphs

(Channel description, [[Stanford Online]].)

A 70:04 lecture from **Stanford CS224W: Machine Learning with Graphs**, autumn 2023 semester, given by **Jure Leskovec** (Professor of Computer Science at Stanford; SNAP Group lead). Published 7 December 2023 to the Stanford Online YouTube channel — **the wiki's oldest video source by publish date** by more than a year (next-oldest is [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025 (May 2025)]]). Manual caption track at `language_code: en-US` selected for highest fidelity. No chapters (academic lecture). **Pre-GenAI-era foundational academic reference** for the [[knowledge-graphs]] construct the LLM-era practitioner sources ([[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]] / [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza]] / [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic]]) operate on top of.

## TL;DR

Three substantive contributions to the wiki:

1. **The knowledge-graph-completion task formulation** — the canonical academic task that gives the GenAI-era GraphRAG / KG-grounded-agent literature its theoretical foundation. *"Given a head entity and a relation type, predict the missing tail."* Example: *(J.K. Rowling, genre, ?)* → predict *Fantasy / Young-Adult Fiction*. **Link-prediction-with-typed-relations** generalises basic graph link-prediction to the heterogeneous-relation case.

2. **Four shallow KG-embedding methods + the relation-pattern-coverage matrix**:

   | Method | Embedding form | Symmetric | Antisymmetric | Inverse | Composite | 1-to-N |
   |---|---|---|---|---|---|---|
   | **TransE** | `h + r ≈ t` (Euclidean translation) | ✗ | ✓ | ✓ | ✓ | ✗ |
   | **TransR** | Project entities into relation-specific space, then translate | ✓ | ✓ | ✓ | ✗ | ✓ |
   | **DistMult** | Bilinear scoring `<h, r, t>` (Hadamard product) | ✓ | ✗ | ✗ | ✗ | ✓ |
   | **ComplEx** | Complex-valued embeddings; bilinear with conjugate | ✓ | ✓ | ✓ | ✗ | ✓ |

   The method-vs-pattern coverage matrix is **the lecture's central pedagogical artifact**: no single shallow-embedding method covers all relation patterns. *"At the end, basically, this table will be filled in and it will make sense."* The wiki's first **systematic relation-pattern-method tradeoff framing**.

3. **The FreeBase scale-and-incompleteness empirical anchor**: ~80M entities, 38k relation types, 3B edges. **93% of people in FreeBase don't have a place-of-birth**; 80% don't have a nationality. The wiki's first **concrete-numbers anchor for the KG-incompleteness problem** that motivates the entire KG-completion task family. The smaller academic benchmark FB15k (~50k entities, 200–1300 relations, 300–600k edges) is *"what NeurIPS papers tend to use"* — *"very few papers have the guts to use the big data set because it's massive."*

Plus: the word-embedding analogy (King→Queen, China→Beijing, USA→Washington-DC) as the *motivational frame* for translation-based embeddings — *"if you take a name of the country and you look where is the capital embedded, it was the same direction. From China and Beijing, from USA and Washington DC, for Germany and Berlin, it was all these vectors."* TransE's `h + r ≈ t` is the KG generalisation of the same arithmetic.

## What was actually ingested

Full 70:04 lecture transcript. Manual track (high fidelity); speaker labels not present (lecture is monologue with occasional student questions and Leskovec's responses preserved inline). Lecture opens with Leskovec saying *"sorry, sorry, sorry"* and restarting after realising he had the wrong slides up — note this on-record self-correction is preserved in the raw transcript as evidence of the manual track's fidelity. Includes Q&A interactions inline.

## Why this source matters to the wiki

The wiki's recent KG-related ingests ([[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza 2026]] industrial-OT; [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026]] agentic-memory; [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB 2026]] practical-engineering) all operate on the **LLM-era reuse** of knowledge-graph technology — using KGs to ground LLM responses, store agent memory, or power GraphRAG. **None of them re-derive the underlying academic theory** — they assume it.

Leskovec's lecture is the **theoretical baseline** the practitioner literature stands on. Key continuities the wiki should preserve:

- **The KG-completion task** (Leskovec) ≈ **infer-missing-entity-relationship** (SurrealDB ETL: entity-extraction + relationship-extraction with LLM-inferred edges).
- **Word-embedding-analogy motivation** (Leskovec) ≈ **vector embeddings underlying RAG** (SurrealDB hybrid search; Bratanic dream-phase embeddings).
- **The 93%-missing-place-of-birth FreeBase finding** (Leskovec) ≈ **incompleteness problem** that motivates LLM-driven entity-extraction in KG-ETL (SurrealDB Extract stage).
- **Translation-embedding intuition** (TransE) ≈ **graph-traversal-and-hop semantics** (SurrealDB GraphRAG multi-hop navigation).

The lecture is **academic-foundation pre-requisite** for fluently reading the LLM-era practitioner literature.

## Knowledge graphs — Leskovec's working definition

> *"Knowledge graphs allow you to capture in a graph form, in a relational form, knowledge about entities and their relations. So we are going to capture entities, types, and the relationships between them. You can think of nodes as entities. And nodes are labeled with their types. And then edges between two nodes capture the relationship between the entities. Knowledge graph is an example of a heterogeneous graph. But the reason why we call these things knowledge graphs because the idea is that we encode our knowledge about a given domain in this type of graphical form."*

Two structural notes:

- **KG = heterogeneous graph + knowledge interpretation**. The data structure is just a heterogeneous graph (multiple node types + multiple edge types); the *knowledge graph* label is interpretive — *"we encode our knowledge about a given domain in this type of graphical form."*
- **KG enables reasoning + retrieval + ML-integration**: *"we can think of this as a knowledge base over which you can reason, over which you can retrieve, and allows you to bring in the knowledge to your machine learning model."*

## Worked example catalogue from the lecture

Leskovec enumerates pre-GenAI-era industrial KG deployments that anchor the construct historically:

- **Bibliographic networks** — conferences / papers / titles / years / authors / citations. The wiki's standard academic-publishing-data structure.
- **Biomedical KGs** — drugs / diseases / adverse events / proteins / pathways with typed relations (is_a hierarchies / treatments / side-effects).
- **Google search**: *"Google answers a knowledge graph when you type questions into the Google search box."* The KG Leskovec references is the underlying **Google Knowledge Graph** (commercial).
- **Amazon**: *"Amazon has a knowledge graph of all their products, their properties, sellers."*
- **Facebook Graph API**: *"It's not only people and their relationships, but also what schools people went, what locations they attended. That's all nodes in this knowledge graph. It's all resolved to the level of entities."*
- **IBM Watson**, **Microsoft Satori**, **LinkedIn**, **Yandex** — industrial-KG ecosystem circa 2023.
- **Question-answering systems** (Siri / Alexa / Bing): *"What are the latest films by the director of Titanic?"* — multi-hop traversal: parse natural language → look up director → look up films-directed-by edges → return ranked. Direct historical antecedent to the [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]] GraphRAG patterns 30 months later.

## TransE — the canonical translation-embedding intuition

Leskovec's core pedagogical example:

> *"For the triple head-relation-tail, I would like the following in my vector space: I'd like h + r to be equal to t. If the given facts are true, and otherwise I'd like this to be different. The way this would look like is: I take the embedding of h, I have some embedding for r so I move in this direction, and hopefully I end up close to the target t."*

The training method is **contrastive / triplet loss**:

```
For each true triple (h, r, t):
  Sample a corrupted triple (h, r, t') where t' is a wrong tail
  Want: distance(h + r, t) < distance(h + r, t')
  Minimise hinge loss on the violation
```

Subtlety Leskovec flags during Q&A: *"if you will pick a random entity, that will be a too easy tail. So what you usually want to do is you want to pick a tail that is of the same type, but wrong."* **Negative-sample-selection-by-type-matching** is a load-bearing detail.

The relation-pattern coverage matrix (TL;DR table above) reveals TransE's central weakness: **symmetric relations and 1-to-N relations** fall outside the model class. TransR / DistMult / ComplEx are derived to address specific shortcomings.

## Relation pattern taxonomy

The four pattern types Leskovec uses to compare methods:

- **Symmetric**: `r(h, t) ⇒ r(t, h)`. Example: `roommate(A, B) ⇒ roommate(B, A)`.
- **Antisymmetric**: `r(h, t) ⇒ ¬r(t, h)`. Example: `parent(A, B) ⇒ ¬parent(B, A)`.
- **Inverse**: `r1(h, t) ⇒ r2(t, h)`. Example: `advisor(A, B) ⇒ advisee(B, A)`.
- **Composite**: `r1(a, b) ∧ r2(b, c) ⇒ r3(a, c)`. Example: family-relation chains.
- **1-to-N**: a single head has many valid tails for the same relation. Example: `(person, born-in, city)` — Napoleon visited many cities.

The taxonomy is **applicable beyond shallow-embedding methods** — the same pattern types are the discriminators for GNN-based methods (covered in earlier lectures of CS224W not in this ingest) and for LLM-driven entity-extraction in GraphRAG (relevant for [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB's]] LLM-inferred-relationship stage).

## Convergence with existing wiki sources

| Source | Connection |
|---|---|
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB 2026]] | **The KG pair**: Leskovec (academic foundation) + Martin (practical engineering). Two-source threshold met for [[knowledge-graphs]] as a wiki concept page. Leskovec's `h + r ≈ t` intuition is the **mathematical foundation** for the vector embeddings Martin's ETL pipeline produces; Leskovec's KG-completion task is the **theoretical formulation** of the entity-extraction + relationship-extraction Martin's LLM-driven ETL operates on |
| [[2026-02-01-manditereza-ontology-driven-industrial-ai\|Manditereza 2026 (HiveMQ industrial)]] | Manditereza's three-tier semantic data layer (semantic model + domain ontologies + knowledge graph) operates on the KG construct Leskovec defines academically. **Two-source cross-domain convergence** (industrial-OT + academic-foundation) on KG-as-grounding-substrate |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026 (TDS / Neo4j)]] | Bratanic's linked-list-session-graph + dream-phase-distillation operates on the KG data structure. The shallow-embedding approach Leskovec teaches is one option for Bratanic's vector-embedding-of-entities; the typed-relationship taxonomy is one option for Bratanic's hooks-as-edges |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | Karpathy's *Software 3.0* paradigm — where the program is an LLM and the input is a spec — doesn't change the underlying graph-as-knowledge-substrate construct Leskovec teaches. The KG layer is **prompt-agnostic** in a way the LLM layer is not |

### Contradictions

None substantive. Leskovec's framing is academic-canonical; no opposing source in the wiki at this depth.

## Linked entities and concepts

**Concept pages affected**:

- **[[knowledge-graphs]]** — **NEW CONCEPT PAGE created in this ingest** (this source + SurrealDB). Leskovec is the academic-foundation anchor.
- [[agent-harness]] — KG embeddings as the theoretical basis for the harness's persistent-context substrate.

**Dangling** (single-source first-mention, deferred):

- **Jure Leskovec** — Professor of Computer Science at Stanford; SNAP Group lead; co-creator of GraphSAGE, Node2Vec, DeepWalk; CS224W instructor. **Strong promotion candidate** — Leskovec is academically canonical in this space and likely to recur.
- **Jiaxuan** — CS224W TA (transcript-uncertain spelling; *"Jiaxuan covered the topics around graph neural networks over the last few weeks"*).
- **CS224W** — Stanford's *Machine Learning with Graphs* course; foundational for the KG / GNN literature.
- **FreeBase** — large-scale knowledge graph; **~80M entities, 38k relation types, 3B edges**; acquired by Google. Used as canonical academic benchmark.
- **FB15k / FB15k-237** — academic benchmark KG (~50k entities, 200–1300 relations).
- **Wikidata** — Wikipedia's structured-data project; KG of world knowledge.
- **DBpedia** — Wikipedia-derived KG; **Strong promotion candidate** alongside Wikidata for any future KG-data-ecosystem ingest.
- **Stanford SNAP** — Leskovec's research group.
- **Google Knowledge Graph** / **Microsoft Satori** / **IBM Watson** — industrial KG product lines named historically.
- **Node2Vec / DeepWalk** — shallow-embedding methods Leskovec generalises here to KGs.
- **TransE / TransR / DistMult / ComplEx** — KG-embedding method family.

**Concept candidates surfaced (not yet promoted)**:

- *KG completion task* — Leskovec's canonical academic formulation. Single-source-as-a-named-task.
- *Relation pattern taxonomy (symmetric/antisymmetric/inverse/composite/1-to-N)* — the discriminator-set for embedding-method comparison. Single-source.
- *Contrastive / triplet loss with type-matched negative sampling* — training pattern. Single-source as a *named-training-pattern*.

## Open questions raised by this source

- **CS224W later lectures** — this lecture is one of many in the course. Earlier lectures on GNN architectures (relational GCN) and later lectures on graph-aware LLM integration would be useful complementary ingests.
- **Updated FreeBase / Wikidata empirical numbers** — the 93%-missing-place-of-birth statistic is from a Stanford research paper Leskovec cites verbally; primary-source target.
- **Production KG-embedding system case studies** — Leskovec mentions industrial KGs (Google / Amazon / Facebook / IBM / Microsoft / LinkedIn / Yandex) but no primary sources are ingested. Open primary-source target especially for the GraphRAG-vs-classical-KG-embedding question.
- **The CS224W website resources** — slides, assignments, scribed notes — would substantiate the in-lecture claims in primary-source form. Open primary-source target.
