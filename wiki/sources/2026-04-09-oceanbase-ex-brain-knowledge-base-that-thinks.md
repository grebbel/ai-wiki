---
type: source
kind: article
title: "I Built a Knowledge Base That Thinks — Inspired by Karpathy's LLM Wiki"
author: ["OceanBase Database"]
url: "https://medium.com/@oceanbase/i-built-a-knowledge-base-that-thinks-inspired-by-karpathys-llm-wiki"
date_published: 2026-04-09
length: "~6-min read (11 pages PDF)"
raw: "../../raw/articles/I Built a Knowledge Base That Thinks — Inspired by Karpathy’s LLM Wiki _ by OceanBase Database _ OceanBase Database _ Apr, 2026 _ Medium.pdf"
tags: [llm-wiki, knowledge-base, knowledge-compilation, mcp, hybrid-search, ai-native-database, seekdb, oceanbase, ex-brain, entity-linking, timeline-extraction, vendor-implementation]
relationships:
  - type: supports
    target: llm-wiki
    via: "first-vendor implementation worked example — OceanBase team built `ex-brain` CLI as a direct response to Karpathy's LLM Wiki pattern; demonstrates compiled-truth + timeline-extraction + entity-linking + hybrid-search on seekdb (their AI-native database); MCP server exposes brain_get / brain_put / brain_search / brain_compile / brain_link tools to Claude Code"
  - type: supports
    target: knowledge-graphs
    via: "ex-brain's entity-linking mechanism builds a knowledge graph organically as new information arrives — *'no manual tagging, no predefined ontologies'*; seekdb co-locates vector + full-text + scalar + JSON + GIS in a single embedded database"
  - type: supports
    target: agent-harness
    via: "second seekdb/SurrealDB-class anchor on multi-modal-database-as-harness-substrate after SurrealDB 2026; MCP-integration walkthrough demonstrates the harness-runtime / database-substrate boundary"
---

# I Built a Knowledge Base That Thinks — Inspired by Karpathy's LLM Wiki

> Andrej Karpathy's LLM Wiki dropped a simple idea: store knowledge as plain text, let an LLM understand and update it. Garry Tan's GBrain ran with the same concept. Both projects prove that LLM + local storage is a surprisingly powerful combination for personal knowledge management.

(Article opening, [[OceanBase Database]] Medium publication.)

A 6-minute Medium article by **[[OceanBase Database]]** (publication; written from the engineering team's first-party voice) explaining **ex-brain** — a CLI tool the OceanBase team built as a direct response to [[Andrej Karpathy|Karpathy]]'s LLM Wiki gist. Published 9 April 2026 — **five days after** Karpathy's gist appeared (4 April 2026). The wiki's first **first-vendor implementation worked example** of the LLM Wiki pattern, with the implementation backed by the team's own AI-native database **seekdb**.

## TL;DR

Four substantive contributions:

1. **The compiled-truth principle, named explicitly**: *"knowledge should update itself when new information arrives, not just accumulate."* The article's core thesis distinguishes ex-brain (and the LLM Wiki pattern) from append-only note-taking. Worked example: company Series A in March, new CEO in June, Series B in August — Notion/Obsidian accumulate three notes that the user must mentally reconcile; ex-brain *compiles* them so the page always reflects current truth. The wiki's first **first-vendor articulation of compiled-truth-vs-appended-notes** as a design principle.

2. **Four mechanisms that distinguish ex-brain from standard note-taking**:

   | Mechanism | What it does |
   |---|---|
   | **Smart compilation** | New information updates existing knowledge (status / fact / event detection drives update strategy) rather than just appending |
   | **Automatic timeline extraction** | Events are pulled from text and organised chronologically; date parsing handles ISO + natural language (`last week`, `yesterday`) + localised formats |
   | **Entity linking** | Relationships between people, companies, and concepts are detected and cross-referenced automatically; new entities get auto-created stub pages |
   | **Hybrid search** | Keyword precision (BM25) + semantic understanding (vectors) in a single seekdb query, with optional LLM reranking |

3. **seekdb as the all-in-one storage substrate**: the wiki's second multi-modal-database anchor after [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]]. seekdb is OceanBase's open-source AI-native database (github.com/oceanbase/seekdb): single-file embedded mode (no server, no Docker, 1 CPU + 2 GB RAM); native hybrid search (HNSW / IVF / quantised vectors + BM25 + scalar filtering); built-in AI functions (`AI_EMBED`, `AI_COMPLETE`, `AI_RERANK`) usable in SQL; MySQL-compatible SQL syntax with ACID transactions; multi-model (vector + text + scalar + JSON + GIS coexist in one engine).

4. **MCP integration as the harness/substrate boundary**: ex-brain ships with a built-in MCP server (`ebrain serve`). When connected to Claude (Code) via the `mcpServers` configuration, Claude can use `brain_get` (read pages), `brain_put` (write pages), `brain_search` (query), `brain_compile` (compile new info into existing pages), and `brain_link` (create entity relationships). **The wiki's first MCP-server-as-LLM-Wiki-interface worked example** — explicit demonstration of where the harness (Claude Code as agent runtime) ends and the substrate (seekdb as compiled-knowledge storage) begins.

## What was actually ingested

Full 11-page PDF article including code examples (CLI commands, Python integration, MCP `mcpServers` config). Article tail (pages 10-11) covers seekdb's product specifications + about-the-publication / about-the-author footer; substantive content lives in pages 1-9.

## The four mechanisms — operational detail

### Mechanism 1: Smart compilation (compiled truth)

Single-command CLI surface:

```
ebrain compile companies/river-ai \
  "River AI closed Series A, $50M" \
  --source meeting_notes \
  --date 2024-05-20
```

The LLM behind the CLI analyses **what kind of information** this is and applies the right update strategy:

| Information type | Strategy | Example |
|---|---|---|
| **Status** | Update current value, archive previous | Funding stage, CEO, headcount |
| **Fact** | Append, keep existing | Founded year, industry, HQ |
| **Event** | Add to timeline | Product launch, funding close |

After compilation, the page always reflects current truth. Worked example output:

```markdown
## Status
- **Funding Stage**: Series A (Source: meeting_notes, 2024-05-20)
- **Valuation**: ~$50M

## History
- Previously Seed (until 2024-05-20)

## Facts
- Series A led by Sequoia
- Founded 2020
```

*"No manual reorganization. No stale information buried in a page you'll never re-read."* The compilation pattern is the LLM Wiki idea operationalised — the LLM does the bookkeeping the human would otherwise have to do.

### Mechanism 2: Timeline extraction

```
ebrain timeline extract companies/river-ai
```

Returns chronologically-sorted JSON events. Runs **automatically during compilation** — every `compile` that contains an event adds it to the timeline. Date parsing handles ISO, natural language (`last week`, `yesterday`), and localised formats.

### Mechanism 3: Entity linking

```
ebrain put people/ali-partovi --file notes.md
# Detected:
# - Ali Partovi founder_of Neo
# - Ali Partovi invested_in [other companies]
```

The LLM detects entities and typed relationships from input text. **When a new entity is detected, the system creates a stub page automatically** — convergent with [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]]'s LLM-driven entity-extraction stage of the KG-ETL pipeline. *"No manual tagging, no predefined ontologies."* The knowledge graph emerges organically as information arrives.

### Mechanism 4: Hybrid search

Single-mode search breaks down fast — full-text misses semantics (*"funding"* doesn't find *"financing round"*); vector search can be noisy (*"Sequoia"* might return tree-related results). ex-brain's solution: **seekdb hybrid search with a scoring layer on top** (semantic relevance 85% + freshness 10% + type weight 5%).

```
# Keyword search
ebrain search "River AI Series A"

# Semantic query
ebrain query "Which companies raised funding recently?"
```

Under seekdb: vector and full-text indexes recall candidates independently; results fused via weighted combination or Reciprocal Rank Fusion (RRF); optional LLM reranking for precision.

## seekdb as the all-in-one storage substrate

OceanBase positions seekdb as the right fit for ex-brain because the article enumerates four properties:

- **Embedded mode, zero ops**: single database file; no server process; no Docker container; runs comfortably on 1 CPU + 2 GB RAM. *"For a local-first personal tool, this is the lightest possible deployment."*
- **Native hybrid search**: vector (HNSW, IVF, quantised), full-text (BM25 + phrase + boolean), scalar filtering — all one engine with multi-stage ranking pipelines.
- **Built-in AI functions**: `AI_EMBED` generates vector embeddings in SQL; `AI_COMPLETE` runs text generation; `AI_RERANK` applies reranking models. Works with OpenAI, DashScope, or custom model endpoints. *"Embedding, retrieval, and inference happen inside the database — no external pipeline needed."*
- **SQL-compatible + multi-model**: MySQL syntax; full ACID; vectors + text + scalars + JSON + GIS coexist; ex-brain stores structured metadata (page properties, entity links) + unstructured content (text, embeddings) in one database.

The integration code (truncated in the article):

```javascript
const db = await BrainDb.connect("~/.ebrain/data/ebrain.db");

const pages = await db.getOrCreateCollection({
  name: "ebrain_pages",
  embeddingFunction: createBrainEmbeddingFunction(settings.embed),
});

const hits = await pages.hybridSearch({
  query: { whereDocument: { $contains: "funding" } },
  nResults: 10,
});
```

## MCP integration — the harness/substrate boundary

The article's most architecturally significant section:

```json
{
  "mcpServers": {
    "ebrain": {
      "command": "ebrain",
      "args": ["serve"]
    }
  }
}
```

After this one-line install, **Claude can call ex-brain primitives directly**:

- `brain_get` — read pages
- `brain_put` — write pages
- `brain_search` — query
- `brain_compile` — compile new information into existing pages
- `brain_link` — create entity relationships

This is **the wiki's first first-party-vendor demonstration of where the harness ends (Claude Code) and the substrate begins (seekdb as compiled-knowledge storage)**. Convergent with [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic's]] *hooks-as-portable-primitive across harnesses* — MCP and hooks are two interface styles for the same harness/substrate boundary.

## Cross-source references

- **Karpathy's LLM Wiki** — named as inspiration: *"Andrej Karpathy's LLM Wiki dropped a simple idea: store knowledge as plain text, let an LLM understand and update it."* Direct attribution.
- **Garry Tan's GBrain** — named as parallel concept: *"Garry Tan's GBrain ran with the same concept. Both projects prove that LLM + local storage is a surprisingly powerful combination for personal knowledge management."* The wiki's **second source** referencing GBrain explicitly (first was [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan / GStack 2026]] briefly). Two-source threshold met for GBrain.

## Open issues acknowledged in the article

The "What's Next" section concedes ex-brain is **early-stage**:

- Compilation logic isn't perfect (occasional misclassification of information type)
- Timeline extraction occasionally misses events
- Entity detection produces false positives

Future directions named: conflict detection when new information contradicts existing records; confidence decay for stale data; bidirectional propagation when linked entities change; batch compilation for high-volume ingestion.

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026 (Sequoia AI Ascent)]] | Karpathy is the upstream-spec author for the LLM Wiki pattern this article implements. ex-brain is the **earliest-vendor implementation** in the wiki's ingest corpus |
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB / Martin 2026]] | Both are AI-native multi-modal databases positioning vector + full-text + scalar + graph in a single engine. seekdb (OceanBase) is single-file embedded; SurrealDB is Rust-multi-deployment-modal. The wiki's first **two-vendor convergence on multi-modal-database-as-harness-substrate** |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026 (TDS / Neo4j)]] | Bratanic's *hooks-as-portable-primitive* and ex-brain's *MCP-server-as-LLM-Wiki-interface* are two interface styles for the same harness/substrate boundary. Bratanic uses hooks (system-initiated); ex-brain uses MCP (agent-initiated) |
| [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack\|Tan / GStack 2026]] | Direct reference: ex-brain article names GBrain in its opening paragraph. Two-source-on-GBrain threshold met |
| [[2026-02-01-manditereza-ontology-driven-industrial-ai\|Manditereza 2026 (HiveMQ)]] | ex-brain's *no-predefined-ontologies* entity-linking is the opposite engineering choice from Manditereza's *ontology-as-load-bearing-discipline* — both valid for different contexts (personal-knowledge vs industrial-OT) |

### Contradictions

None substantive. The article is self-aware about ex-brain's early-stage status and names limitations directly.

## Linked entities and concepts

**Concept pages affected**:

- **[[concepts/llm-wiki|llm-wiki]]** — **NEW CONCEPT PAGE created in this batch** — ex-brain is the earliest-vendor implementation worked example.
- [[knowledge-graphs]] — entity-linking mechanism builds a KG organically.
- [[agent-harness]] — MCP-server-as-LLM-Wiki-interface demonstrates the harness/substrate boundary.

**Dangling** (single-source first-mention, deferred):

- **OceanBase Database** — the publication and the engineering team behind ex-brain + seekdb. Multi-mention candidate on future ingest.
- **ex-brain** — the CLI tool itself.
- **seekdb** — OceanBase's open-source AI-native database; github.com/oceanbase/seekdb.
- **Ali Partovi**, **Sarah Chen** — example-data entities (people) in the article's CLI samples.
- **River AI**, **Neo** — example-data entities (companies).

**Other entities mentioned (cross-references promoted by this ingest)**:

- **[[Andrej Karpathy]]** — source_count 1→2 (this article cites him explicitly).
- **Garry Tan** — second-source threshold met (Tan/GStack + this article); promote in this batch.
- **GBrain** — multi-source threshold met; promote alongside Garry Tan.
- **Notion**, **Obsidian** — note-taking tools named as comparison cases.
- **Mem**, **Granola** — AI-powered note-taking alternatives criticised as black-box.
- **DashScope** — embedding/AI provider seekdb supports.

## Open questions raised by this source

- **ex-brain GitHub repo deep-dive** — would substantiate the four-mechanism architecture claims.
- **seekdb vs SurrealDB benchmark** — two AI-native databases positioning identically in the wiki; comparative evaluation an open target.
- **seekdb scalability ceiling** — embedded-mode single-file is great for personal tools; enterprise scaling profile is undisclosed.
- **Conflict detection in compilation** — named as a future direction; first-party design discussion would substantiate.
- **The "compiled truth" pattern at enterprise scale** — ex-brain operates at personal-knowledge-base scale; enterprise extension semantics are an open question (compare [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu 2026]]'s *queryable-organization* framing).
