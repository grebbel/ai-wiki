---
type: source
kind: video
title: "RAG is Dead: Jeff Huber (Chroma) on Building Agentic Search"
author: ["Mastra"]
url: "https://www.youtube.com/watch?v=RvkbPPZbPgc"
date_published: 2026-05-11
length: "~13:45 minutes (transcript ~63 grouped segments from 413 raw ASR lines)"
raw: "../../raw/videos/huber-chroma-rag-is-dead-agentic-search.md"
tags: [llm-wiki, knowledge-graphs, agent-harness, context-engineering, context-rot, agentic-search, chroma, rag-is-dead, vector-database, bitter-lesson, file-system-as-database, hybrid-search]
relationships:
  - type: supports
    target: llm-wiki
    via: "convergent with Liu/Raju/OceanBase explainers — *RAG is dead the term, not the technique*; context engineering as the rebranding; Chroma's *Context Rot* 45-page research report substantiates the LLM-Wiki scale-ceiling caveat with empirical data on context-length performance degradation"
  - type: supports
    target: knowledge-graphs
    via: "first-party vendor anchor — Chroma's *Context One* specialised search sub-agent (10x faster, 25x cheaper than gigabrain models for search); agentic search with hybrid search under the hood as the default recommendation"
  - type: supports
    target: agent-harness
    via: "*'file systems are bad databases'* claim — concurrency, indexing, search-via-grep-only limitations; the harness's persistent-context substrate should be a real database not a sandboxed filesystem; convergent with SurrealDB/seekdb multi-modal-database-as-substrate framing"
---

# RAG is Dead: Jeff Huber (Chroma) on Building Agentic Search

> Jeff Huber, co-founder and CEO of Chroma, presents the case for retiring RAG as a term and embracing the bitter lesson for context engineering.
>
> RAG is dead, Jeff says. The term, not the technique. Ask 25 builders to define RAG, and get 25 different answers. The same goes for "vector database." Both should be banned.
>
> What is real, Jeff argues, is that most agent failures are context failures rather than reasoning failures. Context is too much, too little, or confusing. Last year, Chroma published a 45-page research report called Context Rot showing that language model performance is not invariant to context length. The "dumb zone" starts somewhere between 20,000 and 120,000 tokens, depending on the use case.

(Channel description, [[Mastra]].)

A 13:45 conference talk by **Jeff Huber** (Chroma co-founder & CEO) hosted on the [[Mastra]] YouTube channel. Published 11 May 2026 — **today**, by the wiki's working date. ASR caption track; no chapters. **The wiki's first-party-Chroma-CEO source** on context engineering as the rebranding of RAG and the case for agentic search.

## TL;DR

Six substantive contributions:

1. **"RAG is dead — the term, not the technique"**. Huber's headline framing: *"if you ask 25 people to define RAG, they'll all define it a slightly different way. Rag is banned. Oh by the way, vector database is also banned."* Convergent with [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] and [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] but from the *vendor's-vendor* vantage (Chroma is the underlying retrieval substrate for many of the LLM-Wiki implementations the wiki has ingested). The reframe: **context engineering**.

2. **The Context Rot empirical anchor**: Chroma's **45-page research report from 2025** demonstrating that *"language model performance is **not invariant** to the number of tokens you use in the context window."* The "dumb zone" starts somewhere **between 20,000 and 120,000 tokens** depending on use case — *"I've not found anybody who really trusts a million tokens to do anything that's any kind of good."* The wiki's first **empirical anchor** for the scale-ceiling caveat [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju]] named on the LLM Wiki pattern.

3. **Three named context-failure modes**: *"the context is either too much (gets into the dumb zone, gets into context-rot territory), too little (missing critical information even a human couldn't reason about), or confusing (language models still aren't great at handling conflicting information and understanding which information has priority)."* The wiki's first **three-axis context-failure taxonomy** — strict superset of [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB's]] *context clash / context confusion / dense neighbourhood degradation* (which only address the *too-much* axis).

4. **"Embrace the bitter lesson" for context engineering**: *"Stop hand engineering and as much as possible embrace the bitter lesson. Give agents great tools and good guidance on how to use those tools and when to use those tools, and then just let the agents figure it out."* Huber's claim is that **context engineering itself will be folded back into the models** — Chroma just released a model trained to edit its own context. *"If you want to bet on the future, you should bet that will be the case."*

5. **"File systems are bad databases" — Huber's structural critique**: four named limitations of the file-system-plus-bash pattern (Codex / Claude Code's current default):
   - Poor concurrency (last-write-wins for two agents/humans editing same thing).
   - Files easily corruptable in pathological cases.
   - No indexing over the data.
   - Limited search (only `grep` — strict pattern match; no semantic expansion).
   - Sandbox is heavyweight tool when you only need read/write.
   Cites [[Swyx]]'s recent article *"Oops, You Wrote a Database"* as the canonical statement of this anti-pattern. Names **Mintlify's virtualized-bash-on-Chroma** as the cleaner alternative — *"to the agent it looks the exact same"* (bash commands: glob / grep / cat / ls just work).

6. **Chroma Context One — the open-source specialised search sub-agent**: *"an auto-regressive language model. You input the query and Context One outputs the documents."* Trained-with-pretty-small-budget claim: *"10× faster, 25× cheaper, and actually better at searching or on par with gigabrain models like Opus 4.5/4.6 and GPT-5 4."* 50-page research report. The wiki's first **named search-specialised-LM-vs-gigabrain-LM tradeoff** with measurable cost-and-speed numbers.

## What was actually ingested

Full 13:45 transcript including audience Q&A (memory-vs-context-compaction question; agentic-search-vs-RAG-cutover question referencing Anthropic's Boris Cherny). ASR caption track; minor transcription errors (e.g. *"Cherny"* may be rendered as *"Chen"* — the speaker said *"Boris Chen's some of his talks on the design of cloud code"* which is almost certainly [[Boris Cherny]] of Claude Code based on context).

## The Context Rot report — empirical anchor

Chroma published *Context Rot* in 2025 as a 45-page technical report. Huber's framing of the headline finding:

> *"We demonstrated definitively that language models and their performance are not invariant to the number of tokens you use in the context window. And then actually the ability for the language model to perform extremely well — to reason at a high degree and pay attention to large portions of the context — goes down quite precipitously."*

> *"Lots of builders now have their own intuition about kind of where that dumb zone starts for their use case. For some people they say it's below 20,000 tokens, 40, 60, 80, 120. I've not found anybody who really trusts a million tokens to do anything that's any kind of good. At the time we published this technical report, the language model labs were sort of claiming that you have 10 million tokens — 'look, it's perfect on needle in the haystack. Just trust us, it works well.' Of course, all the builders were saying this is nonsense."*

Direct substantiation of [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]'s scale-ceiling caveat with measurable empirical data. The wiki's first **empirical-numbers anchor for the context-window scale ceiling**.

## File systems as databases — the anti-pattern critique

Huber's four-point structural critique of the file-system-plus-bash pattern (currently dominant in Codex / Claude Code workflows):

| Problem | Mechanism |
|---|---|
| **Poor concurrency** | Two agents or humans editing the same thing → last-write-wins; no atomicity |
| **Corruption risk** | Files easily corrupted in pathological cases |
| **No indexing** | Linear scan only |
| **Search-via-grep-only** | Strict pattern match; no semantic expansion |
| **Sandbox heavyweight** | Spinning up a full sandbox is overkill if you only need read/write to files |

The anti-pattern is named with citation to **[[Swyx]]'s** article *"Oops, You Wrote a Database"* — the canonical statement of the file-system-as-incidental-database problem.

The cleaner alternative Huber names: **virtualized bash + virtualized file system over a real database**. Mintlify's documentation-assistant pattern is the worked example — *"yes, plug, they used Chroma as the backing database and put a virtual file system in front of Chroma."* From the agent's perspective, identical bash commands work; from the substrate's perspective, the database provides concurrency / indexing / hybrid search / re-ranking that the file system can't.

The wiki connection: convergent with [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]] and [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain]] — all three are vendor framings of *multi-modal-database-as-harness-substrate*. Huber adds the **anti-pattern-call-out** to the cluster: the file-system-plus-bash pattern is the *wrong* default; a real database is the *right* default.

Huber's note on the meta: *"the people that are really bitter-lesson-pilled and are kind of an AGI maximalist — the whole meta around 'you should use file systems because agents are trained on file system APIs and they're really good at them' — is a bit of a passing fad. It's a meme. It's not wrong, but it's short-sighted; agents will become very good at using whatever tools you give them in the fullness of time."*

## Embrace the bitter lesson — context engineering folded back into models

Huber's prediction:

> *"Context engineering itself will just be folded back into the models. You're already seeing some evidence for this. In a few slides I'll talk about a model that Chroma just released ourselves. And actually this model was taught to edit its own context — to do its own kind of lightweight context engineering."*

The wiki implication: the **context-engineering-as-handcraft** discipline is being subsumed into LM-side capabilities. Hand-engineering chunks / retrieval pipelines / re-ranking will be displaced by models that **manage their own context window**. This is convergent with Karpathy's *Software 3.0* prediction direction — programs migrate into model weights over time.

## Chroma Context One — search-specialised LM

The wiki's first **named search-specialised-LM-vs-gigabrain-LM tradeoff** with measurable numbers:

| Dimension | Gigabrain (Opus 4.5/4.6, GPT-5 4) | Chroma Context One |
|---|---|---|
| Speed | Baseline | **10× faster** |
| Cost | Baseline | **25× cheaper** |
| Search quality | Baseline | *"Actually better at searching or on par"* |
| Architecture | Auto-regressive LM that outputs *text* generation | Auto-regressive LM that outputs *documents* directly |
| Training budget | (vendor) | *"Pretty small budget and small team"* |
| Distribution | (vendor-hosted) | Open-source on Hugging Face |
| Backing report | — | 50-page research report |

Huber's argument: *"We find the task of search actually does not lend itself particularly well to being gigabrained, and maybe you're paying too much, you're waiting too long, and you're actually getting worse search results."*

The pattern (specialised-small-model-for-narrow-task > general-large-model-for-narrow-task) is convergent with the *thin-harness/fat-skills* framing in [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] — different decompositions of the same insight that intelligence-per-token can be optimised per task class.

## Chroma Sync — automatic indexing

Huber announces a complementary product: **Chroma Sync**. *"This allows just dropping files into a bucket and then Chroma picks up all those files and automatically handles the indexing, so that you don't have to handle those pipelines yourself."* The wiki's first **named automatic-indexing-as-a-service product** for the LLM-Wiki / knowledge-graph cluster.

## Agentic search with hybrid search — Huber's default recommendation

For *"almost all use cases"* Huber recommends: *"agentic search with hybrid search under the hood ... if you need a default magic button, just go type that into Claude Code and tell it you want it to do that, and it will."*

The recommendation maps onto [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB's]] *hybrid search in a single query* claim and [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain's]] *hybrid search via seekdb* — three-vendor convergence on **hybrid search as the default substrate primitive**.

## Memory ≈ context compaction — Huber's structural collapse

Q&A insight Huber surfaces:

> *"Memory is actually in some sense a task of context distillation. If you have a million tokens of memory, and you need to inject a couple hundred tokens into this new generation, that is in some sense still a search process of 'what should I remember in this moment?' So memory, context compaction, distillation — they're actually all the same thing once you unpack it."*

The wiki's first **structural collapse of memory / context compaction / distillation as the same underlying task** — relevant to [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026]]'s dream-phase memory framing and to GBrain's signal-detector skill (which performs context compaction at every-message granularity).

## Agentic search vs RAG cutover — the [[Boris Cherny]] reference

An audience member references Boris Cherny's design talks for Claude Code: *"They tried RAG and then they tried agentic search and it just worked much, much better. It seems like agentic search is able to do more and more of what you needed RAG for previously."*

Huber's response distinguishes corpus-size regimes:
- **Small corpuses (30-50 files)**: grep-based agentic search probably finds the right thing eventually. *"It may not be fast, it may not be cheap, but it will eventually find the right thing."*
- **Larger corpuses**: grep breaks. *"And then also, if you need any level of semantic expansion, you do want some semantic expansion."*
- **Forthcoming Chroma research** (Huber promises *"next week"*): empirical numbers on *more-expressive-search-tools-vs-grep-with-more-generations*.

Huber's bias-flag: *"Number one, somebody tells you something, question their incentives — who wants you to spend more money on tokens?"* — pointed reframe of the *"agentic search beats RAG"* claim from vendors (like Anthropic) with token-revenue interests.

The wiki connection: convergent with [[2026-05-08-running-an-ai-native-engineering-org|Fung 2026 (Anthropic / Boris Cherny / Claude Code engineering)]] — Cherny is named in both sources. Two-source mention of Cherny strengthens his existing entity page.

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju 2026]] | **The "RAG is dead but only as a term" framing converges**. Raju treats it from the LLM-Wiki-explainer vantage; Huber from the vendor-of-the-substrate vantage. Two-source convergence on the rebranding-vs-elimination distinction. Huber's *Context Rot* report empirically substantiates Raju's *scale-ceiling caveat* (scale ceiling = the dumb zone Huber names) |
| [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers\|Liu 2026]] | Liu's *three architectures: RAG / LLM Wiki / Fat Skills* is the *system-design-decision-framework*; Huber's *RAG-is-dead-the-term* is the *vendor's-vendor reframe*. Both reject the term *RAG*; both advocate for hybrid/convergence. The wiki now holds **three independent sources rejecting RAG-as-a-useful-term** while preserving its underlying technique |
| [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide\|SurrealDB / Martin 2026]] | Both name *vector-only-RAG failure modes*; SurrealDB enumerates *context clash / context confusion / dense neighbourhood*; Huber generalises to *too-much / too-little / confusing*. The two taxonomies are **strict subset / superset** — Huber's framing is broader |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase ex-brain 2026]] | Three-vendor convergence on multi-modal-database-as-substrate: SurrealDB / seekdb / Chroma. Huber adds the **anti-pattern call-out** (*file systems are bad databases*) the prior two sources didn't articulate explicitly |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026 (TDS / Neo4j)]] | Huber's *memory ≈ context compaction ≈ distillation* structural collapse is the **conceptual frame** for what Bratanic implements operationally (hooks-driven persistent memory + dream-phase distillation) |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung 2026 (Anthropic / Claude Code engineering)]] | Both name [[Boris Cherny]]. Huber's audience-Q references Cherny's design talks for Claude Code on agentic-search-beats-RAG. Huber pushes back with *"question their incentives — who wants you to spend more money on tokens?"* The wiki's first **substantive cross-source disagreement** (rather than just convergence) between Anthropic's framing and an independent-vendor framing |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | Huber's *embrace the bitter lesson — context engineering will be folded back into models* is direct convergence with Karpathy's *Software 3.0* prediction that programs migrate into model weights over time |
| [[concepts/llm-wiki\|llm-wiki]] | Huber is the **vendor-of-the-substrate vantage** on the LLM Wiki cluster. Where Karpathy authored the pattern and Raju/Liu/OceanBase explain/implement it, Huber sells the underlying retrieval database used in most LLM-Wiki implementations |

### Contradictions

The **agentic-search-vs-RAG cutover** is the wiki's first substantive vendor-disagreement. Cherny (per Fung 2026 / Claude Code engineering) advocates agentic search as broadly better than RAG. Huber pushes back: *"on larger corpuses [grep-based agentic search] breaks ... and if you need semantic expansion, you do want some semantic expansion."* Huber promises empirical data *"next week"* (mid-May 2026 publication target). **Open primary-source ingest target**.

## Linked entities and concepts

**Existing wiki entities reinforced**:

- [[Boris Cherny]] — Huber's audience-Q references Cherny's Claude Code design talks. Second source mention.
- [[Anthropic]] — implicit via Claude Code reference; substrate-vs-agent debate.

**Concept pages affected**:

- [[concepts/llm-wiki|llm-wiki]] — Huber is the vendor-of-the-substrate vantage.
- [[knowledge-graphs]] — third-vendor convergence on multi-modal-database-as-substrate.
- [[agent-harness]] — *file-systems-are-bad-databases* critique of the current Codex/Claude-Code-default-pattern.

**Dangling** (single-source first-mention, deferred):

- **Jeff Huber** — Chroma co-founder & CEO.
- **Chroma** — vector database / retrieval substrate (multi-mention candidate — already referenced in [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] briefly).
- **Mastra** — channel (single-source).
- **Swyx** — tech influencer; *"Oops, You Wrote a Database"* article author.
- **Mintlify** — documentation-assistant vendor; virtualized-bash-on-Chroma worked example.
- **Chroma Context One** — open-source specialised search sub-agent.
- **Chroma Sync** — automatic-indexing-as-a-service product.
- **Context Rot** — Chroma's 45-page 2025 research report.

**Concept candidates surfaced**:

- *Context Rot* — Chroma's named phenomenon with empirical 45-page substantiation. Likely promotion-candidate on second-source mention.
- *Embrace the bitter lesson for context engineering* — Huber's framing. Single-source.
- *File systems are bad databases* — Huber's structural critique. Single-source.
- *Search-specialised LM vs gigabrain LM* — Huber's named cost/speed/quality tradeoff. Single-source.
- *Memory ≈ context compaction ≈ distillation* — Huber's structural collapse. Single-source.

## Open questions raised by this source

- **The Context Rot 45-page report itself** — primary-source ingest target. Chroma blog / research site.
- **Forthcoming Chroma research on agentic-search-vs-grep numbers** — Huber promises *"next week"* (mid-May 2026 publication).
- **Mintlify's virtualized-bash-on-Chroma article** — primary-source ingest target on the worked example.
- **Swyx's "Oops, You Wrote a Database" article** — primary-source ingest target on the file-system-as-incidental-database anti-pattern.
- **Chroma Context One on Hugging Face** — primary-source ingest target on the search-specialised-LM model release.
- **The agentic-search-vs-RAG empirical disagreement** — would benefit from a controlled comparison Cherny's Anthropic team and Huber's Chroma team agree on. Open empirical question.
