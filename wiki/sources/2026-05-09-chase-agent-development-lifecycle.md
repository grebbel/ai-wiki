---
type: source
kind: article
title: "The Agent Development Lifecycle"
author: ["Harrison Chase"]
publisher: "LangChain — Blog"
url: "https://www.langchain.com/blog/the-agent-development-lifecycle"
date_published: 2026-05-09
date_ingested: 2026-05-10
length: "~10-page article (~3,000 words; 12-page PDF including diagrams + footer)"
raw: "../../raw/articles/langchain.com_blog_the-agent-development-lifecycle.pdf"
tags: [langchain, agent-development-lifecycle, adlc, build-test-deploy-monitor, governance, langgraph, langsmith, deep-agents, agent-runtime, agent-harness, evaluation, tracing, simulation, sandboxes, prompt-hub]
---

# The Agent Development Lifecycle

A thesis-piece on the LangChain blog by **Harrison Chase** (LangChain co-founder/CEO) formalizing what the wiki has been calling the [[agent-development-lifecycle|Agent Development Lifecycle (ADLC)]] as a **four-phase loop wrapped by governance**: *Build → Test → Deploy → Monitor → (Iterate)*, with *Govern* surrounding the whole loop. *"That is what makes agent development repeatable."*

This is the wiki's **second formalization** of the ADLC construct — and the first non-Google source for it. Where [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google's Agents CLI announcement]] presented a 9-stage wheel grounded in the Google Cloud substrate, Chase presents a more abstract 4+1-phase model that maps cleanly across vendors, with explicit named primitives at each phase that draw from LangChain's own product line (LangChain, LangGraph, Deep Agents, LangSmith) but generalize to alternatives (CrewAI, Claude Agents SDK, AWS AgentCore, Daytona, E2B, Temporal, n8n).

## TL;DR

- **The lifecycle**: Build → Test → Deploy → Monitor — with Iterate as the integrating loop and Govern wrapping the whole.
- **Build** has *four layers of tooling*: **Frameworks** (abstractions for model calls / tools / prompts / retrieval / agent loops — LangChain, CrewAI), **Runtimes** (state, control flow, durability, persistence, human intervention — LangGraph), **Harnesses** (prompts, skills, MCP servers, hooks, middleware, memory — Deep Agents, Claude Agent SDK), and **No-code** (domain experts configure agents directly — LangSmith Fleet, Claude Cowork, n8n). *"These distinctions matter because 'building an agent' can mean different things."*
- **Test** mostly precedes deployment and combines: **datasets** (built from manual testing, dogfooding, support tickets, prior traces, known edge cases), **metrics** (correctness for ground-truth tasks; criteria-based evaluation for open-ended ones — was the response grounded? did the agent follow policy? did it ask for clarification? did it complete the task efficiently without unnecessary tool calls?), **experiments** (compare prompts, models, retrieval strategies, tool schemas, orchestration patterns against the same eval set; over time, show whether the agent is improving or regressing), and **simulations** (multi-turn evaluation; voice agents are an obvious case but applies to any multi-turn agent — support, coding, internal-ops).
- **Deploy** is *more than hosting*: a production agent runtime needs **durable execution + human-in-the-loop** (LangSmith Deployment, AWS AgentCore, Temporal-based custom runtimes), **sandboxes** for isolated code execution (LangSmith Sandboxes, Daytona, E2B), a **virtual filesystem** when full sandbox isn't needed (Deep Agents pattern; Postgres/S3-backed), and a **prompt / context hub** so non-engineers can edit prompts, skills, and task instructions without a full deploy.
- **Monitor** is fundamentally different from monitoring traditional software: latency / cost / error rates / uptime are necessary but only part of the picture. *"An agent can return a technically successful response and still fail the task itself."* Required components: **traces** (full trajectory: inputs / model calls / tools invoked / outputs / final response — *"if you cannot see the trajectory, you cannot reliably debug the behavior or turn those failures into future evals"*), **signals** (LLM-as-judge + simpler regex-based signals; double as product analytics), **feedback** (LLM-judge + regex + human review + direct user feedback, attached to the underlying run), **dashboards** (usage / feedback / latency / cost / tool calls / evaluator scores / recurring failure patterns + alerts on rising latency / increasing costs / failing tools / declining feedback / policy violations).
- **Iterate** is hill-climbing over the loop: *"They do not wait for a perfect agent before shipping. Instead, they build something useful, test it enough to understand its behavior, deploy it in a controlled way, monitor how it performs in production, and feed those learnings back into the next version."* Datasets get stronger over time as production traces backfill them. *"This is how teams hill-climb."*
- **Govern** wraps the whole lifecycle:
  - **Cost** — agents become expensive (multiple model calls, long context, repeated tool use, retries); orgs need budgets, usage monitoring, alerts, visibility.
  - **Tool access** — clear controls on which tools an agent can access, under what conditions, on whose behalf.
  - **Audit trails** — for every tool call: inspect which agent made the call, what inputs/outputs, which user or policy authorized it.
  - **Human-in-the-loop** — designed in from the start; not every tool call should be fully automated.
  - **Discoverability / reuse** — orgs accumulate prompts, skills, tools, retrieval sources, policies, agents — without good discovery, teams recreate them, leading to inconsistency. *"Shared context and shared agents need to be findable, reusable, and governed."* Especially important for *skills*.
  - **Repeatable infrastructure across teams** — the most effective orgs invest in shared infrastructure so every team isn't building its own evaluation framework / deployment / tracing / feedback / dashboards from scratch.
  - *"Good governance is not about slowing teams down. It is about making fast iteration possible without losing visibility, control, or consistency as agent systems scale."*

## What was actually ingested

Full 12-page PDF read end-to-end — body text, all six included diagrams ("The Agent Development Lifecycle" wheel, "Build choices sit at different layers," "No-code expands who can build," "Testing starts before production," "Deployment is more than hosting," "A trace shows the full trajectory," "Governance wraps the lifecycle"), the Conclusion, and the full footer (Related content, "See what your agent is really doing" callout). The article structure is named via section headers (Build, Test, Deploy, Monitor, Iterate, Govern, Conclusion) — no appendix.

## Key claims and contrasts

### The four Build layers — frameworks vs. runtimes vs. harnesses vs. no-code

> *"There is a wide range of tooling here. Some tools are code-first, while others are no-code or low-code. Some focus on abstractions, while others focus on giving agents a working environment with prompts, tools, skills, and state."*

The diagram lists four layers, with example tools at each:

| Layer | Focus | LangChain ecosystem | Outside LangChain |
|---|---|---|---|
| **Frameworks** | Abstractions for model calls, tools, prompts, retrieval, structured outputs, agent loops | **LangChain** | CrewAI |
| **Runtimes** | State, control flow, durability, persistence, human intervention | **LangGraph** | (named: Temporal-based custom runtimes) |
| **Harnesses** | Prompts, skills, MCP servers, hooks, middleware, memory, sometimes filesystem | **Deep Agents** | **Claude Agent SDK** |
| **No-code** | Domain experts configure agents directly | **LangSmith Fleet** | Claude Cowork, n8n |

This is **load-bearing for the wiki's harness vocabulary**. Until this source, the wiki had treated "harness" and "framework" as adjacent layers in [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane's]] 4-layer stack (Layer 2 = harness frameworks; Layer 3 = harness runtime). Chase's distinction is sharper:

- **Frameworks** are pure abstractions — *what you write code against*.
- **Runtimes** are execution-layer concerns — state, durability, control flow.
- **Harnesses** are the *environment* the agent runs in — prompts, skills, MCP servers, hooks, middleware, memory.
- **No-code** is the configuration UI for non-engineers.

This refines the wiki's harness vocabulary considerably. Worth feeding back into [[agent-harness|`agent-harness.md`]] in this ingest batch. Notably, Chase's *harness* sits at a *more specific* place in the stack than Kokane's — for Chase, the harness is the *runtime + content* (skills, prompts, MCP, hooks) the agent operates within, not the entire abstraction stack from foundation model up. This is more compatible with [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic 2026]]'s framing of hooks as a harness-component primitive.

### Testing starts before production

> *"That does not mean building a perfect eval suite before anyone uses the agent. In practice, that is rarely realistic. It does mean having enough evals in place to catch obvious failures, compare versions, and avoid shipping changes blindly."*

The "Testing starts before production" diagram traces a four-step pipeline: **Inputs** (expected tasks, known edge cases, dogfooding traces, simulations) → **Datasets** (examples, hard cases, regression coverage) → **Metrics** (correctness, criteria checks, policy compliance) → **Experiments** (compare versions, catch regressions, decide readiness — *"Ready to deploy?"*).

The metric-typology distinction between **ground-truth metrics** (extraction, classification, field updates — measurable for correctness) and **criteria-based evaluation** (write-a-response / summarize / decide-whether-to-escalate / multi-valid-path tasks — was the response grounded? did the agent follow policy? did it ask for clarification?) is the cleanest articulation in the wiki of *why agent evaluation is harder than software-test evaluation*: many tasks have no single ground truth, so evaluation moves to behaviour-criteria scoring. This complements [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]]'s scalable measurement of durable skills: criteria-scored evaluation is the same shape, applied to a different task population (agents vs. workers).

### Simulations as the multi-turn-eval primitive

> *"Many agents are multi-turn systems. They do not just answer one question; they have a conversation, gather information, call tools, update state, and recover from ambiguity. For those agents, single-turn evals are not enough."*

Voice agents are the obvious example. Pattern broader: support agents (frustrated customer, follow-up, order-status check, escalation decision); coding agents (inspect repo, make changes, run tests, respond to feedback); internal-ops agents (gather missing information before action). This is the wiki's first source making **simulation as a first-class evaluation primitive** explicit.

### Deployment is more than hosting

> *"A production agent runtime typically needs to support durable execution and human-in-the-loop patterns. Durable execution means the agent can checkpoint progress and resume instead of losing work when something fails."*

Named primitives:

- **Durable runtime** — LangSmith Deployment, AWS AgentCore, Temporal-based custom solutions.
- **Sandboxes** — isolated execution environments with filesystem access; reduce blast radius of mistakes / unsafe behavior. LangSmith Sandboxes, Daytona, E2B.
- **Virtual filesystem** — when sandbox is overkill. Deep Agents pattern: file-as-working-memory, Postgres/S3-backed.
- **Prompt / context hub** — *"Some of the most important parts of an agent are not traditional application code. Prompts, retrieval context, skills, and task instructions may need to change more often than the application itself. They may also need to be edited by people who are not engineers."* The hub separates *agent code* from *agent configuration* in deployment terms.

### Monitoring needs traces, not just metrics

> *"This is where monitoring agents differs from monitoring traditional software. Metrics like latency, cost, error rates, and uptime still matter, but they are only part of the picture. An agent can return a technically successful response and still fail the task itself. It may call the wrong tool, rely on the wrong context, skip a required approval step, or produce an answer that sounds plausible but is wrong."*

The four required components — *traces / signals / feedback / dashboards* — are operationally identical to [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] **Compounding** layer extended into production. Chase makes the loop explicit: *"The strongest monitoring systems feed directly back into evaluation. Important traces become dataset examples, recurring failures become metrics, and production behavior becomes the foundation for the next round of improvement."*

This **cleanly extends** [[2026-05-07-kiron-schrage-compound-benefits|Kiron & Schrage 2026]]'s *verification → evaluation → learning capture* loop — same architecture, applied at the agent-engineering layer rather than the workflow-quality layer.

### Governance as a precondition for scale

> *"For a single agent, lightweight controls may be enough. As organizations deploy more agents, governance becomes necessary. Without it, teams quickly end up with agents that are difficult to discover, difficult to monitor, expensive to run, and unclear in what they are allowed to do."*

The six governance axes (cost / tool access / audit trails / HITL / discoverability / shared infrastructure) are the wiki's first systematic treatment of *agent governance* — a concept that has been adjacent in [[2026-04-28-anand-wu-genai-playbook|Anand & Wu]], [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan AI maturity]], [[responsible-ai|responsible-ai]], etc., but not previously named with this taxonomy.

Particularly load-bearing: the *discoverability of skills* problem. *"This is especially important for skills. A skill can encode a workflow, a writing style, a domain-specific procedure, or instructions for using a tool. If one team has already built a good skill, another team should be able to find it rather than write a new version from scratch."* This is the same problem [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's Codex team]] solved internally with the AGENTS.md / DESIGN.md / docs/ hierarchy + doc-gardening agent. Different scope, same mechanic.

## Cross-source resonance

| Source | Connection |
|---|---|
| [[2026-04-22-cheung-ippolito-secchi-google-agents-cli\|Cheung, Ippolito & Secchi 2026]] (Google Agents CLI) | The wiki's *first* ADLC formalization. Chase is the *second*, abstracting the lifecycle to vendor-agnostic phases. The two are **complementary**: Google's 9-stage wheel sequences the work that happens at each of Chase's 4 phases (capability+design+tools+context+evaluate inside Build/Test; deploy+CI/CD inside Deploy; UAT inside Test/Govern). Major upgrade for [[agent-development-lifecycle\|`agent-development-lifecycle.md`]] — bumping `source_count` from 1 to 2 and confidence from 0.70 to 0.80. |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | The four-layer harness (Context / Constraints / Contracts / Compounding) maps to the *Build* phase of Chase's lifecycle — they describe *what* gets built; Chase describes *the lifecycle wrapping the building of it*. The Compounding layer specifically maps to Chase's Monitor + Iterate phases. Complementary, not overlapping. |
| [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] | Kokane's 4-layer stack (App / Frameworks / Harness / Model) gets refined here. Chase splits Kokane's "Frameworks" into *frameworks (abstractions)* + *runtimes (execution)* + *harnesses (environment)* — three distinct layers. This is a substantive vocabulary refinement; capture in the [[agent-harness\|harness concept page]]. |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo 2026]] (OpenAI Codex) | Lopopolo's Codex team has *built* a complete instance of Chase's lifecycle inside a single repo: Build (ARCHITECTURE.md / Providers interface / custom linters); Test (per-worktree observability stack + Chrome DevTools Protocol validation); Deploy (gh + repository-as-system-of-record); Monitor (taste-invariant scans + golden-principle GC + doc-gardening agent); Iterate (review feedback → doc updates → linter rules); Govern (mechanical layer enforcement + restricted Providers interface). The two posts together substantiate the lifecycle as a *real engineering practice* not just a marketing taxonomy. |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic 2026]] | Bratanic's hooks + dream-phase architecture is operationally inside Chase's *harness* layer (Build) and *monitoring/iteration* loop (Monitor → Iterate) — events flow into the dream phase, distilled memories flow back into the harness via hook injection. Chase's ADLC and Bratanic's hooks/dream-phase are different vantages on the same continuous-improvement loop. |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron & Schrage 2026]] | The *verification → evaluation → learning capture* loop is operationally identical to Chase's Test → Monitor → Iterate. Different scopes (Kiron-Schrage at workflow-quality level; Chase at agent-engineering level), same mechanic. |
| [[2026-04-30-ai-index-report-2026\|AI Index 2026]] | Documents the broader move toward agentic AI as production practice; Chase's lifecycle is the operational scaffold. |
| [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills\|Globerson et al. 2026]] | Criteria-based evaluation (Chase's metric typology) is operationally the same shape as Globerson et al.'s LLM-judge measurement of durable skills. |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | Karpathy's *agentic engineering* discipline finds its lifecycle scaffold here; the discipline is what fills out each phase of the lifecycle. |

## Linked entities and concepts

- **Author**: Harrison Chase — *first wiki source mention by name*. He is co-founder/CEO of LangChain. Per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion), do **not** create an entity page on a single source; list as **Dangling**. Promote on second-source mention. (LangChain itself, however, has been substantively named across [[agent-harness]], [[ai-agents]], and [[generative-ai]] — it is a candidate for *organization-entity promotion in this same ingest batch*. Decision: promote LangChain to a proper entity page given the cumulative second-source threshold; defer Harrison Chase pending second-source mention by name.)
- **Organization**: **LangChain** — entity promotion candidate, see above.
- **Products / projects mentioned (LangChain ecosystem)**: **LangChain** (framework), **LangGraph** (runtime), **Deep Agents** (harness), **LangSmith** (eval/observability/deployment platform; LangSmith Deployment, LangSmith Sandboxes, LangSmith Fleet, LangSmith Observability, LangSmith Evaluation, LangSmith Platform, LangChain Academy).
- **Outside-LangChain products mentioned**: **CrewAI**, **Claude Agent SDK** (== Claude Cowork in the no-code framing), **AWS AgentCore**, **Temporal**, **Daytona**, **E2B**, **n8n**, **Postgres**, **S3**.
- **Concepts touched**:
  - [[agent-development-lifecycle]] — **major upgrade**: this is the second formalization. Source count 1 → 2; confidence 0.70 → 0.80. Concept page extension warranted.
  - [[agent-harness]] — refinement: Chase's frameworks/runtimes/harnesses split sharpens the wiki's vocabulary. Minor concept page update.
  - [[ai-agents]] — minor extension.
  - **Agent governance** — candidate concept. Six axes named here (cost, tool access, audit trails, HITL, discoverability, shared infrastructure). Single-source for now; defer concept-page promotion to second-source mention. Worth flagging in [[ai-agents]] and [[agent-harness]] until promoted.
  - **Simulation as agent eval** — candidate concept. Single-source for now.

## Notes on confidence and lifecycle

- **Source quality**: founder/CEO essay on the company's owned blog. Authoritative on what LangChain ships and how its co-founder thinks about the lifecycle. Vendor-tilted on tooling examples (LangChain ecosystem prominent at every layer), but the *abstract lifecycle structure* (Build/Test/Deploy/Monitor/Govern) generalizes cleanly and is corroborated by the multi-vendor product list (CrewAI, Claude SDK, AWS, Temporal, Daytona, E2B, n8n).
- **Page does not carry `confidence:`** — sources are evidence, not claims.
- **Date and freshness**: published **9 May 2026**; ingested **10 May 2026** — same-week. The freshest source in this ingest batch.

## What this source does *not* do

- It does **not** quantify costs, throughput, or success rates. Every architectural claim is qualitative.
- It does **not** include a worked end-to-end example (one team going through the full Build → Test → Deploy → Monitor → Iterate → Govern loop on a real agent). The taxonomy is asserted abstractly; concrete instantiation is left to the reader. (This complements [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's]] post, which *is* an end-to-end worked example for one team / one product, but at OpenAI rather than at LangChain customers.)
- It does **not** name failure modes or anti-patterns at any phase. *What goes wrong inside Test if you only chase ground-truth metrics? What fails in Deploy if you skip the prompt hub? What governance failures look like when missing?* — none specifically named.
- It does **not** contrast its 4-phase ADLC with Google's 9-stage ADLC explicitly. The earlier formalization is not cited; the wiki is responsible for the comparative work.
- It does **not** address how agents differ from chatbots / RPA / workflow automation in lifecycle terms. The argument assumes you've already decided you're building an agent.
- It does **not** address build-vs-buy or framework-vs-roll-your-own at any phase — implicit assumption is that the team is using LangChain ecosystem tools (or comparable).

These are reasonable scope choices for a thesis-piece blog post; flag as gaps a follow-up source (case study / playbook / academic survey) would need to fill.
