---
type: source
kind: article
title: "What Is Andrej Karpathy's LLM Wiki — And How Can You Extend It?"
subtitle: "Karpathy's LLM Wiki compiles documents into a persistent, compounding knowledge base. This article explains the pattern and extends it with 5W1H context framing (LLM WikiZZ) — with a live demo and open-source code"
author: ["Vishal Mysore"]
publisher: "Medium (@visrow / personal Medium account)"
url: "https://medium.com/@visrow/what-is-andrej-karpathys-llm-wiki-and-how-can-you-extend-it-08e967d25321"
date_published: 2026-04-18
date_ingested: 2026-05-14
length: "~5-min read (5 substantive pages + author bio)"
raw: "../../raw/articles/What Is Andrej Karpathy’s LLM Wiki — And How Can You Extend It_ _ by Vishal Mysore _ Apr, 2026 _ Medium.pdf"
tags: [llm-wiki, karpathy-llm-wiki, 5w1h, wikizz, context-debt, knowledge-graphs, rag-vs-wiki, autonomous-scaffolding, contrast-engine, llm-as-judge, anthropic-api, nvidia-nim, gemini, cloudflare-worker, single-author-extension, vishal-mysore]
---

# Mysore — What Is Andrej Karpathy's LLM Wiki — And How Can You Extend It?

A 5-minute Medium article by **Vishal Mysore** (2.3K followers; *"Holder of multiple patents in AI and software engineering"* per author bio) published **18 April 2026** on his personal Medium account ([@visrow](https://medium.com/@visrow)). The piece slots chronologically between [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] (16 April) and [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] (27 April) in the wiki's [[concepts/llm-wiki|LLM Wiki]] cluster — but its scope and intent differ from both. Raju and Liu position themselves as explainers / comparative analyses; **Mysore's piece is a self-promotion vehicle** for his own open-source extension, **LLM WikiZZ**. The structure: short Karpathy-explainer front-door → longer extension pitch → live-demo CTA. The closing disclaimer makes the framing explicit: *"This article builds on Andrej Karpathy's LLM Wiki pattern. All extensions and implementations are original work by the author."*

## Source-quality flags

Two flags worth surfacing up front because they shape how the wiki should weight this source's claims:

1. **Engagement = 1 clap, 0 responses** (visible at fetch time, 14 May 2026; 26 days after publication). Despite the author's 2.3K follower count, the piece is essentially unread. Compare to **[[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]** which surfaces in the wiki specifically as *"the wiki's clearest single-article explainer"* — published two days before Mysore, on the same platform, on essentially the same topic, and (per its surface engagement metrics) substantially more widely read. The platform's collective judgment is one observable data-point.

2. **WikiZZ is a single-developer experiment, not a community-validated pattern.** Per CLAUDE.md [§Lifecycle](../../CLAUDE.md#lifecycle) — *"Sources that are vendor-sponsored, anecdotal, or a single case study without replication: do not raise confidence above 0.75 unless multiple independent sources agree."* This source is anecdotal in that sense: one author proposing his own extension framework, with a live demo as the only evidence of feasibility. The wiki should treat the **5W1H frame** and **Contrast Engine / LLM Jury patterns** as *concept candidates* (deferred until second source) rather than as validated patterns.

These flags do not invalidate the article. Mysore's framings ("Context Debt", "Architect vs Clerk", the 5W1H frame as a context-scaffolding template) are coherent and pedagogically clear; the live demo *is* an existence proof that the workflow runs. The flags are about **how much weight to give the article's claims** in the wiki's confidence accounting, not about whether to ingest it.

## TL;DR

Five substantive contributions:

1. **The Karpathy-explainer portion is duplicative.** Mysore re-states the key Karpathy facts (gist published 4 April 2026, 5,000+ stars and 4,400+ forks within two weeks; *"incrementally build and maintain a persistent, interlinked wiki"*; *"curate sources, direct the analysis, ask good questions"*) all of which are already in the wiki via [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]], [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]], [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase 2026]], and [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]. The new wiki value of this source is **not** in this portion.

2. **"Context Debt" coinage.** Mysore names *"the cost that builds up when an LLM doesn't truly understand the fundamental frame of the data"* as Context Debt. Adjacent to but distinct from "technical debt"; positioned as the diagnosis that *"transient RAG"* (his term for query-time RAG: NotebookLM, ChatGPT file uploads) produces. Concept candidate — defer to second-source mention.

3. **The 5W1H Wiki Frame as a context-structuring template.** Six-axis template the LLM auto-populates *before any user query*:

   | Axis | Mysore's definition |
   |---|---|
   | **Who** | The target audience / persona context |
   | **What** | The core mission objective |
   | **When** | The temporal and urgency context |
   | **Where** | The situational and environmental context |
   | **Why** | The underlying motivation / value |
   | **How** | The structural and formatting requirement |

   The wiki's first explicit named *six-axis context-scaffolding template*. Convergent in spirit with the wiki's existing CLAUDE.md frontmatter schema (type / kind / aliases / tags / confidence / source_count / last_confirmed / relationships) but applied at the *query-context* layer rather than the *page-metadata* layer.

4. **Three UX patterns for showing context-value.** Mysore proposes three concrete UI patterns, each new to the wiki:
   - **Autonomous Scaffolding** — *"In traditional workflows, the user is the 'Clerk,' manually specifying the context for every query. In WikiZZ, the LLM becomes the 'Architect.'"* The "Generate Wiki" button auto-populates the 5W1H frame from the document.
   - **Contrast Engine** — side-by-side **Plain Mode** (context-less RAG) vs **WikiZZ Mode** (query refined through persistent 5W1H window). See §[The global-warming comparison](#the-global-warming-comparison-empirical-anchor) below for the concrete numbers.
   - **LLM Jury** — a *"high-intelligence Evaluator LLM"* judges the semantic delta between the two answers, calling out improvements in *"situational relevance, concision, or technical depth."* LLM-as-judge applied to A/B-comparison of RAG-quality.

5. **Implementation architecture.** WikiZZ runs **entirely in the browser** (zero-server / static-first); documents are parsed locally via `FileReader` and never stored; API requests are routed through a **Cloudflare Worker** CORS proxy to **NVIDIA NIM, Anthropic, and Gemini**. The wiki's first **browser-only LLM-wiki implementation pattern** — distinct from OceanBase's seekdb-backed implementation and from Liu's GBrain (24-skill / 21-cron / Postgres-pgvector) implementation. Privacy-first by design; trade-off is that the wiki state does not persist across sessions (the *"persistent"* in 5W1H Frame is session-scoped, not durable).

## The Star Wars 5W1H example (pedagogical anchor)

The article's lead visual (page 1) is a hand-drawn diagram applying the 5W1H frame to **Star Wars** — four interconnected nodes with each node's 5W1H axes populated. This is the article's clearest pedagogical anchor for *what 5W1H produces in practice*, so the wiki captures it verbatim:

| Node | What | Who | When | Where | Why | How |
|---|---|---|---|---|---|---|
| **STAR WARS: EPISODE IV** (Film) | A classic space opera film | Directed by George Lucas | 1977 | *(not populated)* | *(not populated — implied via Franchise edge)* | Released on film |
| **LUKE SKYWALKER** (Character) | A young farmboy from Tatooine | Played by Mark Hamill | Introduced in 1977 | *(not populated)* | *(not populated)* | Through action and dialogue |
| **DARTH VADER** (Character) | A dark lord of the Sith | Played physically by David Prowse; voiced by James Earl Jones | Introduced in 1977 | *(visualised as central in the diagram)* | Powerful, intimidating screen presence | Powerful, intimidating screen presence |
| **STAR WARS FRANCHISE** (Legacy) | A global pop culture phenomenon | Created by George Lucas | 1977 – Present | *(not populated)* | *(implied via expanded universe)* | Through a massive expanded universe of films, shows, books, etc. |

The diagram's substantive point — and the reason it's the article's pedagogical lead — is that **the 5W1H axes cross-link across nodes**:
- The *Who* of *Episode IV* (George Lucas) = the *Who* of *Star Wars Franchise* (George Lucas) → automatic cross-reference
- The *When* of *Episode IV* (1977) = the *When* of *Luke Skywalker introduction* (1977) = the *When* of *Darth Vader introduction* (1977) = the start of *Star Wars Franchise When* (1977 – Present) → automatic cross-reference
- *Luke Skywalker* and *Darth Vader* are both *Characters* in *Episode IV*; the diagram draws arrows from Episode IV to each → automatic *part-of* edge

Each node has its own 5W1H **lens**; the lenses are **the cross-reference substrate**. This is the most concrete operationalisation in the wiki of *how* the 5W1H frame is supposed to produce a knowledge graph — and the underlying claim is convergent with the wiki's existing [[knowledge-graphs]] concept page (specifically, with the *typed-relationships-as-graph-substrate* idea from CLAUDE.md §Graph).

**Wiki-internal note**: not every 5W1H axis is populated for every node in Mysore's example (Episode IV has no *Why*; Luke Skywalker has no *Where* or *Why*). This is **honest** of the diagram — the 5W1H frame is a *scaffold*, not a *requirement*; not every axis applies to every node. The wiki's own CLAUDE.md frontmatter schema permits similar sparsity (optional fields like `via:` and `confidence:` on relationships).

## The global-warming comparison (empirical anchor)

The article's second key visual (page 4) is a screenshot of the WikiZZ UI showing a **side-by-side Plain-vs-WikiZZ comparison** of a global-warming query. **This is the article's core empirical claim**: that the 5W1H-framed output *better captures the essence of the source document* than plain query-time RAG. The two outputs are reproduced **verbatim from the page-4 screenshot** so future readers of this wiki can judge the claim for themselves:

### Verbatim outputs from the page-4 screenshot

> **WITHOUT WIKIZZ (Plain Mode)** — 604 tokens, 6.1s:
>
> *"According to the document, global warming is primarily caused by human activity, specifically the expansion of the greenhouse effect through the release of certain gases such as carbon dioxide, methane, and nitrous oxide. These gases are released through various human activities, including:*
>
> *1. Deforestation and land use changes*
> *2. Burning fossil fuels*
> *3. Decomposition of wastes in landfills*
> *4. Agriculture, especially rice cultivation*
> *5. Soil cultivation practices, including the use of commercial and organic fertilizers*
> *6. Fossil fuel combustion*
> *7. Nitric acid production*
> *8. Biomass burning"*

> **WITH WIKIZZ (5W1H Mode)** — 729 tokens, 8.9s:
>
> *"According to the provided document, global warming is primarily caused by human activities. These activities include:*
>
> *1. Deforestation and land use changes, which release carbon dioxide (CO2) into the atmosphere.*
> *2. Burning fossil fuels, which also releases CO2.*
> *3. Agriculture, especially rice cultivation, which produces methane.*
> *4. The decomposition of wastes in landfills, which also produces methane.*
> *5. The use of commercial and organic fertilizers in soil cultivation practices, which produces nitrous oxide.*
> *6. Fossil fuel combustion and biomass burning, which also produce nitrous oxide.*
>
> *Overall, human activities are expanding the greenhouse effect, leading to the long-term rise in the average temperature of the Earth's climate system."*

> **LLM JURY verdict** (the WikiZZ UI's "What Changed?" panel):
>
> *"The WikiZZ answer with 5W1H framing provides more specific details about the greenhouse gases released by human activities and offers a clearer explanation of how these activities contribute to global warming. The framing also helps to reorganize the information in a more logical and concise manner."*
>
> Three highlighted callout tags: *"More specific details about greenhouse gases released by human activities"* · *"Clearer explanation of how human activities contribute to global warming"* · *"Improved organization and concision of the answer"*

### What the comparison demonstrates

**The WikiZZ output better captures the essence of the document than the plain RAG output.** Concretely:

- **Each cause now names its emitted gas** — CO₂, methane, or nitrous oxide. The plain output mentions the three gases once in the opening sentence and then produces an unrelated list of activities; the WikiZZ output threads the gas → activity link through every item. **A reader scanning either output for *"which activities produce methane?"* can answer from the WikiZZ version in seconds; the plain version requires reading the document.**
- **The list is reorganised around the regulatory-relevant taxonomy** (gas type) rather than the document's surface taxonomy (activity type). The plain output has 8 items in document-order; the WikiZZ output has 6 items grouped by emitted gas. Items 3 + 4 are both *methane*; items 5 + 6 are both *nitrous oxide* — the regrouping is the structural payoff of having recognised the audience.
- **The output ends with a synthesis sentence** — *"Overall, human activities are expanding the greenhouse effect, leading to the long-term rise in the average temperature of the Earth's climate system."* The plain output ends with the last bullet ("Biomass burning"). The WikiZZ output frames the bullets as evidence for a thesis rather than as a flat list.

Mysore's framing of *why* this happens: *"the LLM recognizes [the document's] 'Why' and 'What' as providing a technical guide for policymakers"* — i.e. the 5W1H frame populates *audience = policymakers* and *purpose = technical guide*, which causes the model to restructure the output around the regulatory-relevant taxonomy. **The 5W1H frame is what tells the LLM how to project the document onto the audience's mental model**; the plain output projects the document onto the model's default flat-list response shape.

### Cost trade-off and one observable LLM-Jury quirk

The WikiZZ output is **longer (+21%, 604→729 tokens) and slower (+46%, 6.1s→8.9s)**. This is a real trade-off: the audience-aware re-projection costs latency and tokens. For policy-document use the cost is plausibly worth it; for high-volume agent-loops it may not be. The wiki notes this as a trade-off, not a knock.

One observable small quirk: the LLM Jury's callout includes *"Improved organization and concision of the answer"*, but the WikiZZ output is *longer* than the plain output. The improvement is in **specificity** (gas-named per item) and **organisation** (regrouped by gas) — not in concision. This is a small evidence-point that **LLM-as-judge of its own context-pipeline output may not always cleanly identify what improved**. *Not load-bearing on Mysore's main claim* (the WikiZZ output is genuinely better at capturing the document's essence); flagged for the wiki's downstream LLM-as-judge sources.

## The 3-phase compounding diagram (theoretical-claim visual)

The article's closing visual (page 5) is a three-phase diagram showing how WikiZZ-ingested documents accrete into a knowledge graph over time:

| Phase | Visualisation | Mysore's claim |
|---|---|---|
| **Phase 1: Small Web** | ~3 nodes (one What, one Who, one Why), loosely clustered, single small dashed circle around the cluster | *"The 'Who' of one document connects to the 'Who' of another"* — the seed phase |
| **Phase 2: Growing Web of Two Topics** | Two distinct clusters (each labelled with multiple 5W1H axes) with thin edges starting to bridge them; *"Topic A"* is named in the diagram | *"The 'Why' of a medical paper links to the 'Why' of a policy document"* — cross-topic linking begins |
| **Phase 3: Living Knowledge Graph** | ~20+ nodes densely interconnected; all six 5W1H axes visible; multiple Who / Why / Where / How edges crossing the network | *"The LLM stops seeing documents as separate silos and starts seeing a structured semantic network — where a surgeon, a patient, and a policymaker are all connected nodes with different lenses on the same underlying knowledge"* |

Mysore's strongest theoretical claim — the article's closing bullet — is on this diagram: *"The wiki doesn't just grow — it gets smarter with every document added, every query asked, and every 5W1H frame generated."* The wiki notes this is an **assertion**, not a demonstration. The article's actual evidence is a single-query Plain-vs-WikiZZ comparison (Phase 1 at most). Whether Phase 3 actually emerges from WikiZZ's stateless-browser-session architecture is an open empirical question — WikiZZ's *"persistence"* is session-scoped (per Mysore's own Technical Architecture section: *"the WikiZZ Frame persists for the session"*), which structurally limits how much compounding can accrue without a durable storage layer. **This is the source's biggest open question** — see §[Open questions](#open-questions-raised-by-this-source).

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained\|Raju 2026 (Medium)]] | **Same platform, same topic, two days apart, very different reception** (Raju is the wiki's *clearest single-article explainer* of Karpathy's pattern; Mysore is the wiki's *single-author-extension-pitch* on the same pattern). Raju gives the architecture; Mysore gives a vocabulary extension (5W1H) + UX patterns (Autonomous Scaffolding / Contrast Engine / LLM Jury) + a live demo. **Complementary in role; Raju is the canonical reference, Mysore is the variation.** |
| [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers\|Liu 2026 (AI Advances)]] | Liu's comparative-architecture article places **LLM Wiki** between RAG and GBrain in a unified decision framework. **Mysore's WikiZZ sits inside the LLM Wiki cell** of Liu's framework — specifically as a *browser-only / session-scoped* sub-variant, distinct from GBrain's Postgres+pgvector / 21-cron-jobs / 17,888-page durable implementation. Mysore's architecture is **a thin-client implementation of Karpathy's pattern**; Liu's framework predicts hybrid convergence will dominate, which Mysore's stateless approach may or may not survive |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase / ex-brain 2026]] | OceanBase's ex-brain is the **opposite extreme** of Mysore's WikiZZ on the durability axis: ex-brain is server-side, seekdb-backed, MCP-server-integrated (Claude calls `brain_get`, `brain_put`, etc.); WikiZZ is browser-side, `FileReader`-based, session-scoped. **Same Karpathy pattern; opposite architectural choices on persistence-vs-privacy.** The wiki now spans **the full spectrum** of LLM-Wiki implementations from privacy-maximalist (Mysore) to durability-maximalist (Liu's GBrain) with the seekdb path (OceanBase) in between. |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026 (Sequoia AI Ascent)]] | Karpathy's own continued use of the pattern as a first-person testimonial (the upstream-spec author) is the **counter-argument to Mysore's session-scoped architecture**: Karpathy describes the wiki as something *"that's being built up from these articles"* — i.e. accreting over many sessions, not refreshed per browser tab. Karpathy implicitly endorses *durable* over *session-scoped*. The wiki notes this as a **soft tension**, not a contradiction (Mysore's privacy-first browser-only approach is one valid sub-variant) |
| [[knowledge-graphs]] (concept page) | Mysore's "Living Knowledge Graph" closing claim — *"a structured semantic network where a surgeon, a patient, and a policymaker are all connected nodes with different lenses on the same underlying knowledge"* — is the wiki's first explicit *5W1H-as-typed-edges* framing applied to the LLM-Wiki pattern. Adjacent to the wiki's existing knowledge-graph treatment ([[knowledge-graphs]] is anchored on [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings\|Leskovec 2023]] and the SurrealDB / Bratanic / Manditereza vendor sources). Mysore's 5W1H scheme could be viewed as a **fixed-vocabulary typed-edges schema** specifically for the LLM-Wiki context — a sub-variant of the open-vocabulary [[knowledge-graphs]] approach |
| [[Anthropic]] entity page | **Anthropic's API is named as one of WikiZZ's three LLM providers** (alongside NVIDIA NIM and Gemini). The wiki's first **third-party-developer-tool-uses-Anthropic-API** mention in the LLM-Wiki cluster. Surfaces in the Anthropic entity page as a single-line *Mentioned as API provider* note |
| [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Harness is All You Need 2026]] | The *Harness* literature names the LLM-as-judge pattern as the eval-discipline substrate. Mysore's **LLM Jury** is a specific UI instance of this — applied not to agent-eval but to A/B-comparison of RAG-quality with-and-without context-scaffolding. Convergent on the *LLM-as-judge is a valid signal* premise; orthogonal on the target of judgment |

### Contradictions

None substantive. The article makes coherent claims; the wiki's main pushback is on **engagement (1 clap) and architectural durability (session-scoped vs Karpathy's implied durable model)** as flagged in §Source-quality. The empirical-anchor screenshot's LLM Jury claim of *"improved concision"* despite a +21% token increase is a small internal inconsistency Mysore does not address but the wiki notes as observable.

## Linked entities and concepts

**Existing entity pages affected**:

- [[Anthropic]] — Anthropic API named as one of WikiZZ's three LLM providers (alongside NVIDIA NIM and Gemini). Source-quality cap applies (single-author tool); this is a one-line *Mentioned as API provider* surfacing, not a structural addition. `source_count` 7→8; `confidence` 0.92 unchanged (anecdotal single-tool mention does not raise above current 0.92, especially when adjacent OceanBase ex-brain already provides a much more substantive Anthropic-API integration claim via MCP).

**Concept pages affected**:

- [[concepts/llm-wiki|llm-wiki]] — `source_count` 5→6; `confidence` 0.91 → 0.91 (no change — Mysore is the *single-author-extension* variant which per [§Lifecycle](../../CLAUDE.md#lifecycle) does not raise above 0.75 except via *multiple independent sources agreeing*; the existing 0.91 is from rigorous sources and Mysore is unable to lift it further). New body bullet under §*Implementations and variants* (or equivalent) flagging Mysore's WikiZZ as the **browser-only / session-scoped** sub-variant. `last_confirmed` 2026-05-14.

**Dangling** (single-source first-mentions, deferred per the [author-entity promotion rule](../../CLAUDE.md#author-entity-promotion)):

- **Vishal Mysore** — author of this source. AI/software-patents background; 2.3K Medium followers; Medium handle [@visrow](https://medium.com/@visrow). First time as `author:`. Strong promotion candidate **only if a second Mysore source is ingested** — the 1-clap engagement on this piece would suggest deferring promotion even on second-source.
- **WikiZZ / LLM WikiZZ** — Mysore's open-source tool. Live demo at https://vishalmysore.github.io/lllmwikiZZ/. Browser-only / static-first / `FileReader` / Cloudflare Worker proxy / NVIDIA NIM + Anthropic + Gemini providers. Single-source.
- **NVIDIA NIM** — Nvidia's inference microservice product. **Second wiki mention of Nvidia broadly** (after [[2025-05-17-turc-llms-low-precision-quantization-fundamentals|Turc 2025]] which named **Nvidia H100** and **TensorRT** — but Turc is the principal-subject source on Nvidia infrastructure, Mysore mentions NIM only as a third-party API option). The wiki's first **NVIDIA NIM** mention specifically. Defer entity promotion until a source narrates NIM in operator detail.
- **Gemini** (Google's model family) — named only as a third-party API option for WikiZZ. The wiki already has substantive Gemini coverage via [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] (Flow / Veo / Sora cameos comparison) and [[2026-05-11-blank-mit-6s191-three-laws-of-ai|Blank 2026]] (Gemini 2.5 Flash scored *"worst"* on six-bears jailbreak). Mysore's reference is incidental.
- **Cloudflare Worker** — Cloudflare's edge-compute serverless platform; named here as the CORS-proxy infrastructure for WikiZZ. **Cloudflare itself is mentioned in [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]]** as the pro-democracy-protesters mission-emergence case study — making Mysore the **second wiki mention of Cloudflare** but in a completely orthogonal context (governance case study vs CORS-proxy infrastructure). Per the second-source rule the wiki would normally promote Cloudflare to an entity page — but neither mention treats Cloudflare as a principal subject, so the wiki **defers entity promotion** with this explicit two-orthogonal-contexts justification. Reconsider on a third source.
- **NotebookLM** — named in passing as an example of *"transient RAG"* (alongside *"ChatGPT file uploads"*). The wiki already mentions NotebookLM in [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] as the *AI-as-judge for demo days* tool. Mysore's reference is critical (RAG-substrate-not-application) rather than instrumental. Cross-source surfacing not warranted.
- **George Lucas**, **Mark Hamill**, **David Prowse**, **James Earl Jones** — cultural-reference names in the Star Wars pedagogical example (page 1). Cultural-context flags, not promotion candidates. Mysore is using Star Wars as an *intuition pump* (the same way [[2025-05-17-turc-llms-low-precision-quantization-fundamentals|Turc 2025]] uses Severance / MDR).
- **OpenAI** — named in the opening line as *"Andrej Karpathy — co-founder of OpenAI"* — incidental author-credentialing reference, not a substantive claim about OpenAI itself. The wiki's [[OpenAI]] entity page already covers Karpathy's co-founder status.
- **Tesla** — named in the opening line as *"former AI Director at Tesla"* — incidental author-credentialing reference. The wiki does not currently have a Tesla entity page; defer.

**Concept candidates surfaced (deferred until second-source mention)**:

- *5W1H Wiki Frame* — six-axis context-structuring template. Strong promotion candidate on a second source surfacing the same template (or substantial variants).
- *Context Debt* — Mysore's coinage. Single-source vocabulary; defer.
- *Autonomous Scaffolding* (LLM as Architect vs user as Clerk) — context-population pattern. Defer.
- *Contrast Engine* (Plain vs WikiZZ UI pattern for showing context value-add) — UX pattern; defer.
- *LLM Jury / Evaluator LLM as judge of A/B-RAG-quality delta* — specific instance of the general LLM-as-judge pattern. Defer.
- *Browser-only / session-scoped LLM Wiki* — architectural sub-variant of Karpathy's LLM Wiki pattern. Defer.
- *Transient RAG* (Mysore's term for query-time-only RAG with no persistent compilation layer) — vocabulary candidate; convergent with [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]'s framing but Raju does not use the exact phrase. Two-source convergence threshold for *transient-vs-compounding RAG* distinction is met in spirit; defer formal concept-page promotion until a third source uses the same vocabulary.

## Open questions raised by this source

- **Does Mysore's session-scoped persistence actually produce the Phase-3 Living Knowledge Graph the article claims?** The architecture (browser-only, `FileReader`, no durable storage layer described) appears to limit how much compounding can accrue across sessions. The article's evidence (a single-query Plain-vs-WikiZZ comparison) is *Phase-1 at most*. Phase 3 requires longitudinal evidence that the architecture as described does not provide. An empirical investigation — running WikiZZ across many documents over multiple sessions and observing whether the 5W1H cross-references actually compound — would resolve this.
- **Does the 5W1H frame's *fixed* axis vocabulary scale beyond the demo-quality examples?** Mysore's Star Wars and global-warming examples both populate the 5W1H axes naturally. But edge-cases (technical papers without a clear *Who*; legal documents without a clear *Why*; codebases where *Where* might be a file path) are not addressed. The frame may need extension or relaxation for general documents.
- **The LLM-Jury concision claim does not match the token count.** *"Improved organization and concision of the answer"* is in the LLM Jury verdict on the global-warming demo, but the WikiZZ output is +21% longer than the plain output. Is this a labelling artefact, a model-specific quirk, or evidence that LLM-as-judge of its own context-pipeline output is unreliable? Worth checking against the [[2026-05-11-blank-mit-6s191-three-laws-of-ai|Blank 2026 eval-discipline]] literature.
- **Cloudflare Worker as the CORS proxy** is a *commodity infrastructure choice*, but it is the wiki's first explicit named CORS-proxy implementation in an LLM-Wiki source. Open question: is CORS-proxying the right boundary for privacy-first LLM-Wiki implementations, or does it introduce a *de facto* server-side trust relationship that Mysore's "zero-server" framing obscures? Worth ingesting a security-side source on Cloudflare-Worker-as-API-proxy if one arises.
- **WikiZZ codebase ingest** — Mysore claims *"open-source code"* in the subtitle but the article does not link to the source repository (only the live demo). Primary-source ingest of the GitHub repository (likely at https://github.com/vishalmysore/lllmwikiZZ or similar) would substantiate the architecture claims.
- **The 5W1H frame applied to *this* wiki** — open thought-experiment: would auto-populating a 5W1H frame on the wiki's existing 60 sources produce a usefully richer cross-reference graph than the wiki's current typed-relationships approach? Or would it produce a parallel scaffold that doesn't compose with the existing schema? Worth a small experimental ingest cycle if/when the wiki has time for it.
