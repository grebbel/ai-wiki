---
type: entity
kind: person
aliases: ["Harrison Chase"]
tags: [harrison-chase, langchain, langgraph, langsmith, langchain-labs, deep-agents, agent-development-lifecycle, continual-learning, agentic-engineering, ceo-founder]
affiliation: "[[LangChain]]"
role: "Co-founder and CEO, LangChain (since 2022)"
confidence: 0.8
last_confirmed: "2026-05-21"
accessed_at: "2026-05-21"
source_count: 2
---

# Harrison Chase

**Harrison Chase** is the co-founder and CEO of [[LangChain]] — the company he started in 2022 around the open-source [`langchain`](https://github.com/langchain-ai/langchain) Python framework, which expanded over 2023–26 into a layered product stack ([[LangChain|LangChain framework]] / **LangGraph** runtime / **Deep Agents** harness pattern / **LangSmith** observability & evaluation / **LangSmith Fleet** no-code agent builder / **LangChain Labs** research group). The wiki's **canonical vendor-CEO voice on agent-engineering infrastructure** — Chase coins the *frameworks / runtimes / harnesses / no-code* four-layer Build vocabulary and the *model / harness / context* three-layer continual-learning model that anchor the wiki's [[agent-development-lifecycle]] and [[agent-harness]] concepts.

Promoted from Dangling to an entity page on 21 May 2026 after the second substantive source mention:

1. [[2026-05-09-chase-agent-development-lifecycle|Chase / LangChain blog — *The Agent Development Lifecycle* (9 May 2026)]] — Chase's foundational ADLC essay; named *the wiki's second formalization of the ADLC and the source most influential on the concept page's current shape* (per the [[LangChain]] entity page). Establishes the four-layer Build split (frameworks / runtimes / harnesses / no-code) that the wiki now uses as its working taxonomy.
2. [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase, Sproul & di Vittorio — Interrupt 26 Day 2 keynote (21 May 2026)]] — 12 days later, Chase headlines the Interrupt 26 keynote with the **two-types-of-agents typology** (long-horizon vs customer-experience) and the **three-layer continual-learning model** (model / harness / context) — extending the ADLC vocabulary along two new structural axes. Announces **LangChain Labs** as a research group inside LangChain *"aimed in particular at continual learning."*

## Role in the wiki

Chase operates at the **vendor-CEO-of-agent-engineering-infrastructure altitude** — articulating the operating vocabulary for *what is being built* while shipping the product stack that instantiates each layer. Three distinct contributions surface across the two ingested sources:

### 1. The four-layer Build vocabulary ([[2026-05-09-chase-agent-development-lifecycle|ADLC, 9 May]])

Chase's foundational structural decomposition of the *Build* phase of the agent lifecycle:

| Layer | What it is | LangChain product |
|---|---|---|
| **Frameworks** | Abstractions for model calls, tools, prompts, retrieval, structured outputs, agent loops | LangChain (the framework) |
| **Runtimes** | Stateful agent runtime; control flow / branching / looping / persistence / pause-resume | LangGraph |
| **Harnesses** | Prompts, skills, MCP servers, hooks, middleware, memory, virtual filesystem | Deep Agents |
| **No-code** | Domain-expert-facing UI to create and configure agents without code | LangSmith Fleet |

This taxonomy is now the wiki's canonical Build-phase vocabulary on [[concepts/agent-development-lifecycle]], with LangChain serving as the **vendor whose product taxonomy *is* the wiki's vocabulary** — both because Chase coined the four-layer split and because LangChain ships at all four layers.

### 2. The two-types-of-agents typology ([[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Interrupt 26, 21 May]])

A parallel-vertical typology *orthogonal to the four-layer Build split*: Chase predicts (and observes already emerging) a divergence in agent **product surfaces**:

- **Long-horizon agents** — run for minutes / hours / days; code execution, planning, sub-agents, multi-agent, skills; *outcomes and goals* as horizon-extension mechanisms; knowledge work.
- **Customer-experience agents** — latency-critical; voice (and maybe video) as modality; brand-sensitive; sales / customer support / end-user-facing.

*"There is a shared stack underneath. There are also differences in terms of the technology. And I think one of the big questions that we'll be thinking about over the next year is how common is this shared stack versus how particular are the technology pieces that you need for each?"*

### 3. The three-layer continual-learning model ([[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Interrupt 26, 21 May]])

The Interrupt 26 keynote's conceptual centerpiece: every agentic system has **three independently improvable layers**, each with its own continual-learning loop:

| Layer | What it is | Improvement mechanism |
|---|---|---|
| **Model** | The base foundation model (Sonnet, GLM4, GPT-4) | Fine-tuning on traces (Chase cites **Ramp + Prime Intellect fine-tuning Qwen 3.5 for Ramp sheets** as the worked example) |
| **Harness** | *"The code surrounding the model that connects it to the environment"* (Deep Agents, Claude Code, pi) | Agent-edits-harness with evals as forcing function — Chase cites [[2026-03-30-lee-meta-harness-end-to-end-optimization|MetaHarness]] (MIT + Stanford) as the canonical paper |
| **Context** | *"What we provide to the harness as ways to guide it on particular tasks"* (`agent.md`, skills) | Agent.md / skill files iterated against eval suites |

**The evals-as-gradient framing** (Chase's own articulation): *"In classical machine learning, you have the model, you have the training data, you do some gradient descent, and that updates the weights of the model. When you're updating the agent in general, depending on the layer you're at, if you're working at the harness or context layer, it's not exactly gradient descent, but the evals that you write act as a forcing function... So evals and traces are incredibly important for this learning."*

### 4. The on-stage confirmation of the LangChain Top 30 → Top 5 claim

Chase asserts at Interrupt 26: *"we moved from top 30 on terminal bench two to top five just by changing the harness itself. So no changes to the model, only changes to the harness, and we saw a big increase in performance."* This is the **third primary-source confirmation** of the same numerical claim — first asserted in [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain Engineering blog (10 March 2026)]], and the strongest single-claim convergence in the wiki's *harness > model* corpus.

## Notable framings Chase has contributed

- **"Frameworks / Runtimes / Harnesses / No-code"** — the four-layer Build vocabulary now used as the wiki's working taxonomy.
- **"Model / Harness / Context"** — the three-layer continual-learning model.
- **"Evals act as a forcing function"** — the gradient analogy for non-model-layer learning.
- **"Two types of agents: long-horizon and customer experience"** — the product-surface typology orthogonal to the build-layer split.
- **"Everyone will be involved in building agents — domain experts most of all"** — the *org-side corollary* of layered-agent thinking, paired with [[Diana Hu]]'s *AI founder / IC / DRI* org structure prescription.

## Career timeline

- **Pre-LangChain** — *"My background's in classical machine learning"* (Chase, Interrupt 26, ~9:20).
- **2022** — Founded LangChain as an open-source Python framework for working with LLMs.
- **2023–2024** — LangGraph (stateful agent runtime) and LangSmith (observability + eval) launched as the product stack grows out of the open-source base.
- **2025–2026** — Deep Agents pattern, LangSmith Fleet (no-code), LangChain Academy, LangSmith Sandboxes shipped. Company organises Interrupt 2026 (this source) as its first major industry conference.
- **2026** — Announces **LangChain Labs** as a research group inside LangChain aimed in particular at continual learning ([[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Interrupt 26]]).

## Convergence with wiki sources

| Source | Connection |
|---|---|
| [[2026-05-09-chase-agent-development-lifecycle\|Chase / ADLC (9 May 2026)]] | The foundational four-layer Build vocabulary; wiki's primary Chase source for the ADLC concept page. |
| [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents\|Chase, Sproul & di Vittorio / Interrupt 26 (21 May 2026)]] | The continual-learning extension; two-types-of-agents typology; LangChain Labs announcement; vendor-CEO confirmation of Top 30 → Top 5. |
| [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness\|Trivedy / LangChain Engineering (10 March 2026)]] | LangChain colleague's first articulation of the *Agent = Model + Harness* coinage that Chase's Interrupt 26 three-layer model extends. |
| [[2026-02-17-langchain-improving-deep-agents-harness-engineering\|LangChain Engineering — Improving Deep Agents with Harness Engineering (17 Feb 2026)]] | The deep-agents-as-harness pattern that became the substrate for LangSmith Fleet (per Brace Sproul, Interrupt 26 ~17:23). |
| [[2026-03-30-lee-meta-harness-end-to-end-optimization\|Lee et al. / MetaHarness (30 March 2026)]] | The academic paper Chase cites by name on stage at Interrupt 26 as the canonical *learn at the harness layer* worked example. |
| [[2026-05-11-karten-zhang-continual-harness-online-adaptation\|Karten & Zhang / Continual Harness (11 May 2026)]] | The academic formalisation of continual-harness adaptation — Chase's Interrupt 26 three-layer model is the vendor-CEO operationalisation 10 days later. |
| [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer\|Tan & Hu / Stanford CS153 (20 May 2026)]] | Paired *founder/CEO articulations of layered-agent-system thinking* landing within 24 hours. Tan/Hu maps *agentic-primitives → company-structure*; Chase maps *learning-systems → agentic-system-layers*. Same architectural decompose-and-map move applied to different domains. |

## Open questions

- **Chase's pre-LangChain career** — *"My background's in classical machine learning"* is a one-line autobiographical aside; the wiki has no further detail on where Chase worked before founding LangChain in 2022.
- **LangChain Labs's first publications** — Labs is announced at Interrupt 26 as the *continual-learning research group inside LangChain*; the first Labs outputs (papers, blog posts, open-source releases) are an open ingest target for late 2026 / 2027.
- **LangSmith Fleet customer adoption** — the internal-LangChain GTM-agent metrics (84% weekly usage / 240% lead-to-qualified / 40h saved per rep / month) are the only quantified Fleet outcomes the wiki holds. Customer-side adoption metrics (any LangChain customers using Fleet at scale with published numbers) would substantiate or refine the *no-code-builder-for-domain-experts* thesis.
- **LangSmith Engine** — referenced in the Interrupt 26 description as a separate Interrupt-week announcement (*"Meet LangSmith Engine"* blog link); not substantively discussed in the talk body. Open ingest target.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "harrison-chase") OR contains(tags, "langchain")
SORT file.name ASC
```
