---
type: source
kind: article
title: "RAG Isn't Dead. But Something Is. Karpathy's LLM Wiki Explained"
author: ["Sathish Raju"]
url: "https://medium.com/@sathishraju/rag-isnt-dead-but-something-is-karpathys-llm-wiki-explained"
date_published: 2026-04-16
length: "~10-min read (15 pages PDF)"
raw: "../../raw/articles/RAG Isn’t Dead. But Something Is. Karpathy’s LLM Wiki Explained _ by Sathish Raju _ Apr, 2026 _ Medium.pdf"
tags: [llm-wiki, karpathy-gist, rag, agent-memory, knowledge-compilation, three-layer-architecture, hybrid-architecture, claude-md, ingest-query-lint]
relationships:
  - type: supports
    target: llm-wiki
    via: "the wiki's clearest single-article explainer of Karpathy's LLM Wiki pattern — three-layer architecture (raw sources / wiki / schema=CLAUDE.md); three core operations (ingest / query / lint); working Python implementation; honest-comparison table vs RAG with specific failure modes Karpathy glossed over (scale ceiling, hallucination baking, ingest cost)"
  - type: supports
    target: agent-harness
    via: "the schema (CLAUDE.md/AGENTS.md) framed as the configuration file telling the LLM how to maintain the wiki — direct articulation of the harness-config/persistent-context layer"
---

# RAG Isn't Dead. But Something Is. Karpathy's LLM Wiki Explained

> A GitHub Gist with 17 million views set the developer internet on fire. Karpathy described an LLM that builds and maintains a persistent wiki instead of re-searching documents on every query. Here's what he actually proposed — and why the "RAG is dead" framing misses the point.
>
> On April 4, 2026, Andrej Karpathy posted a GitHub Gist. Not a paper. Not a product launch. An "idea file" — a markdown document designed to be copy-pasted into an LLM agent. Within days it had 17 million views, 5,000 stars, and 4,282 forks. The developer internet declared RAG dead. Both sides of that debate have a point. Neither side is fully right.

(Article opening, [[Sathish Raju]] on Medium.)

A 10-minute Medium article by **[[Sathish Raju]]** (Senior AI Architect at Lenovo; previously co-founder/CTO at kloud.io acquired by Alation) explaining [[Andrej Karpathy|Karpathy]]'s LLM Wiki gist with a working Python implementation and honest comparison vs RAG. Published 16 April 2026 — **12 days after** Karpathy's gist. **The wiki's clearest single-article explainer** of the LLM Wiki pattern; substantively descriptive of the very architecture this repo implements.

## TL;DR

Four substantive contributions:

1. **The Karpathy gist statistics as a wiki-event anchor**: posted 4 April 2026; **17 million views**, 5,000 stars, 4,282 forks **within days**. Karpathy framed it as *"an idea file — a markdown document designed to be copy-pasted into an LLM agent"* — not a paper, not a product. The wiki's first **concrete-numbers anchor for the LLM Wiki gist as a developer-internet event**.

2. **The three-layer LLM Wiki architecture, named with explicit ownership semantics**:

   | Layer | Contents | Ownership |
   |---|---|---|
   | **Raw sources** | Articles, papers, images, data files | **Immutable.** LLM reads but never modifies. Human source of truth |
   | **The wiki** | LLM-generated markdown: summaries, entity pages, concept pages, comparisons, synthesis | **LLM owns this layer entirely.** Human reads; LLM writes and maintains |
   | **The schema** | Configuration file (CLAUDE.md, AGENTS.md) telling the LLM how to maintain the wiki: naming conventions, cross-referencing rules, what counts as a contradiction | **Co-evolved** by human and LLM as you figure out what works |

   The three-layer split with ownership-by-layer is **the wiki's first explicit articulation** of CLAUDE.md as the schema layer that closes the loop (rather than as just a project-instructions file).

3. **The three core operations — ingest / query / lint**:

   - **Ingest** (*compiling new knowledge*): drop a new source in raw/; LLM reads, discusses takeaways, writes summary, updates index, touches every relevant entity + concept page. *"A single article about a new Tesla model might update the Tesla page, the battery technology page, the EV market overview, and the manufacturing process page — all in one pass."* The cross-references are maintained automatically.
   - **Query** (*navigating compiled knowledge*): LLM reads index, selects relevant pages, synthesises an answer with citations. **Good answers get filed back into the wiki as new pages.** *"Your explorations compound in the knowledge base."*
   - **Lint** (*health-checking the wiki*): scan for contradictions / stale claims / orphan pages / concepts mentioned but lacking own page / missing cross-references / data gaps. *"This is the maintenance operation that humans consistently fail to do at scale. LLMs don't get bored. They will update fifteen cross-references without complaint."*

4. **The honest-comparison table — LLM Wiki vs RAG**: ten dimensions of comparison, the wiki's first **systematic feature-by-feature contrast** of the two patterns:

   | Dimension | RAG | LLM Wiki |
   |---|---|---|
   | Knowledge accumulation | ✗ Stateless — nothing compounds | ✓ Stateful — grows richer over time |
   | Cross-document synthesis | ✗ Rediscovered on every query | ✓ Pre-compiled at ingest time |
   | Contradiction detection | ✗ Not tracked across documents | ✓ Flagged during ingest and lint |
   | Retrieval explainability | △ "Close in embedding space" | ✓ Specific page citations, readable by humans |
   | Infrastructure required | Embedding model + vector DB + re-indexing | ✓ Just a filesystem and an LLM API |
   | Scale (large corpora) | ✓ Scales to millions of documents | ✗ Practical up to ~hundreds of sources |
   | Query latency | ✓ Fast — vector search | △ Depends on wiki size and context |
   | Real-time / streaming data | ✓ Re-index on update | ✗ Requires re-ingest with LLM passes |
   | Human readability | ✗ Vector database not human-readable | ✓ Plain markdown, browsable in any editor |
   | Multi-user / enterprise | ✓ Battle-tested at scale | ✗ No RBAC, no ACID, no concurrency controls |
   | Hallucination risk | △ Isolated to query time | ✗ Errors baked in at ingest can propagate |

   The table is **the wiki's first source for the systematic tradeoff matrix** — useful for citation when explaining the LLM-Wiki-vs-RAG decision.

## What was actually ingested

Full 15-page PDF article. Pages 13-15 are publication-footer / author-bio; substantive content lives in pages 1-12.

## What Karpathy quietly glossed over (Raju's honest treatment)

The article's most useful section for the wiki's self-awareness — three limitations Karpathy's gist understates:

### 1. The scale ceiling is real

Karpathy runs his wiki at *"roughly 100 articles and 400,000 words."* At that size, the **index.md file fits in a context window**; navigation by index is essentially a directory listing — *"fast, transparent, completely auditable."* But: *"The 'bye-bye RAG' framing quietly assumes that what works at 100 pages works at 10,000. It does not. Once the wiki outgrows what fits in context, you need a real retrieval substrate underneath it — and the cheapest way to build that substrate is, ironically, vector embeddings."*

The wiki's first **named scale-ceiling caveat on the LLM Wiki pattern**. For the wiki itself (currently ~50 sources / ~75 entities / ~25 concepts), this is comfortably under the ceiling; future-growth planning would benefit from explicit awareness.

### 2. Hallucination baking

> *"With RAG, the model goes back to original documents on every query. Even if it makes a mistake in one answer, the next query has a chance to correct it because the source is still the ground truth. The wiki changes this fundamentally. The LLM reads documents, creates pages, links them — and stores that synthesis as authoritative knowledge. LLMs sometimes fill gaps or make assumptions. In RAG, that's a wrong answer. **In the wiki, that's a wrong page that every future query trusts.** Organized, persistent mistakes are harder to spot than individual errors."*

The wiki's first **named risk: persistent-mistake-amplification**. Implications for the lint operation: lint should specifically look for *plausible-but-wrong* claims, not just orphans and contradictions.

### 3. Ingest is not free

> *"The wiki feels efficient at query time because the heavy work is already done. But that work doesn't disappear — it moves to ingest. Every new document requires multiple LLM passes to process, summarize, link, and merge into the existing structure. If your data changes frequently, re-ingesting to keep the wiki current is expensive. RAG handles fresh data better because it always retrieves from the latest source directly."*

The wiki's first **named cost-curve caveat**: ingest cost scales with corpus + LLM passes; LLM Wiki is the wrong choice for fast-moving / streaming-data scenarios.

## The verdict — complement, not replace

Raju's resolution of the "RAG is dead" framing:

> *"What Karpathy actually proposed is a different job for the LLM in a knowledge pipeline — not the elimination of retrieval, but the elevation of it. The honest architecture for most serious knowledge systems is a hybrid. Use the LLM Wiki pattern for what it genuinely does better: compiling and maintaining synthesised knowledge, preserving cross-document connections, enabling the kind of 'what do I know about this topic overall?' queries that RAG struggles with. Use vector retrieval as the substrate underneath the wiki once it outgrows context."*

The article's closing thesis:

> *"Karpathy hasn't killed RAG. He's articulated something more important: that knowledge should compound, not evaporate. Every answer, every synthesis, every cross-document connection should persist and grow richer over time."*

The wiki's first **named convergence-prediction** for the LLM Wiki / RAG / hybrid space — convergent with [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]]'s longer convergence treatment.

## The Python implementation Raju ships

Three functions span the entire LLM Wiki pattern in <200 lines (truncated in the PDF; full version on Raju's blog):

```python
def ingest_source(source_path: str) -> None:
    """Compile a new source document into the wiki."""
    # 1. Load source + schema (CLAUDE.md) + current index
    # 2. Prompt: 'You are a disciplined wiki maintainer.'
    # 3. LLM writes updated wiki pages; human applies to filesystem

def query_wiki(question: str) -> str:
    """Answer a question using the compiled wiki."""
    # Load all wiki pages into context (works at <few-hundred-page scale)
    # LLM answers with citations

def lint_wiki() -> str:
    """Run a health check across the entire wiki."""
    # Find contradictions / stale claims / orphan pages / missing cross-refs
```

The implementation **is essentially what this repository's CLAUDE.md describes operationally** — the three-operation contract (ingest / query / lint) matches CLAUDE.md's §"The four operations" exactly minus *synthesize* (the v0.3 addition). Strong evidence that the LLM Wiki pattern has stabilised at the operation-vocabulary level across multiple implementations.

## Practical tip Raju quotes from Karpathy

> *"Use `grep '^## \[' wiki/log.md | tail -5` to see the last 5 operations at a glance. If each log entry starts with `## [DATE] operation | title`, your entire wiki history becomes queryable with basic Unix tools — no database required."*

This repository's `wiki/log.md` follows exactly this convention (per CLAUDE.md's *"Append an entry to log.md using the agreed prefix format"*).

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026 (Sequoia AI Ascent)]] | Karpathy is the upstream-spec author. Raju's article is the **clearest explainer-of-Karpathy**. The Sequoia interview substantiates that Karpathy continues to use the pattern personally: *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles."* |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase / ex-brain 2026]] | ex-brain is the **vendor implementation**; Raju is the **conceptual explainer**. Together they form a *concept + implementation* pair on the LLM Wiki pattern |
| [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers\|Liu 2026 (AI Advances)]] | Raju and Liu are **two independent explainers** of the LLM Wiki pattern published 11 days apart. Both treat the three-layer architecture explicitly; both compare to RAG; both predict hybrid convergence. Two-explainer consensus on the pattern's structure |
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB / Martin 2026]] | Raju's *"a real retrieval substrate underneath it — and the cheapest way to build that substrate is, ironically, vector embeddings"* converges with Martin's GraphRAG mechanic (vector + graph in one query). The LLM Wiki + retrieval-substrate hybrid Raju proposes is operationally close to SurrealDB's KG-RAG architecture |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex 2026]] | Lopopolo's *AGENTS.md as table-of-contents* + *golden-principles GC* is the harness-engineering analog of Raju's *CLAUDE.md as schema* + *lint operation*. Same maintenance pattern at different scales (personal LLM Wiki vs vendor codebase) |
| **CLAUDE.md (this repo)** | Raju's three-layer architecture + three-operation contract (ingest / query / lint) **matches this repo's CLAUDE.md §"The four operations" exactly minus the v0.3 *synthesize* addition**. Strong cross-source convergence evidence that the pattern has stabilised at the operation-vocabulary level |

### Contradictions

None substantive. Raju is descriptive and balanced.

## Linked entities and concepts

**Concept pages affected**:

- **[[concepts/llm-wiki|llm-wiki]]** — Raju is one of the four anchor sources for the new concept page (alongside ex-brain, Liu, and the upstream Karpathy gist).
- [[agent-harness]] — schema-as-CLAUDE.md framing operationalises the harness-config / persistent-context layer.

**Dangling** (single-source first-mention, deferred):

- **Sathish Raju** — Senior AI Architect at Lenovo; previously co-founder/CTO of kloud.io (acquired by Alation).
- **kloud.io**, **Alation**, **Lenovo** — Raju's career affiliations.

**Other entities cross-referenced**:

- **[[Andrej Karpathy]]** — explicitly cited; source_count bump warranted.
- **Tesla** — used as example-data entity in the Python pseudocode.
- **Obsidian** — named in Karpathy's analogy: *"Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase. You are the architect."*

## Open questions raised by this source

- **Karpathy's actual GitHub Gist URL** — Raju cites "17 million views" but the gist URL itself is not in the wiki yet. Open primary-source target.
- **Lint-for-plausible-mistakes** — Raju names *hallucination baking* as the LLM Wiki's persistent-mistake risk; lint operation enhancement to specifically check *plausible-but-wrong* claims is an open design question for this repository's own lint implementation.
- **The "good answers filed back as new pages" pattern** — Raju and CLAUDE.md both describe this; the operational details of *which* answers warrant filing-back are an open design question.
- **Enterprise-scale LLM Wiki** — Raju notes *"different infrastructure, same principle"* but doesn't detail the enterprise architecture. Open future-source target.
