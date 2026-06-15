---
type: source
kind: video
title: "A leader's guide to advanced team structures in an agentic world"
author: ["AWS Events"]
publisher: "Amazon Web Services (AWS Events YouTube channel); AWS Summit Sydney Executive Forum"
url: "https://www.youtube.com/watch?v=O7u6myBRsns"
date_published: 2026-06-12
date_ingested: 2026-06-15
length: "~31:36 minutes (transcript ~294 ASR lines; auto-generated transcript, light cleanup)"
raw: "../../raw/videos/aws-leaders-guide-advanced-team-structures-agentic-world.md"
tags: [aws-events, aws-summit-sydney, steven-brovich, agentic-team-structures, economics-talent-structure-governance, use-compose-build, hourglass-organization, expert-generalist, renaissance-developer, pricing-scissors, model-a-b-c, embedded-pods, platform-team, non-determinism, singapore-ai-governance, agentcore, policy-as-code, anthropic-economic-index, build-with-claude-hackathon, cio-conductor]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
  - strategic-renewal/organizational-culture
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "the Sydney edition of the same AWS Enterprise Strategy 'advanced team structures' talk (~3 weeks later, presenter Steven Brovich vs Jonathan Allen) — identical framework (USE/COMPOSE/BUILD, hourglass, expert-generalist/Renaissance-developer, Singapore governance, non-determinism, Models A/B/C); a near-replication that corroborates the framework and adds quantified specifics"
  - type: supports
    target: 2026-06-12-aws-leaders-guide-data-strategy-agentic-ai
    via: "sibling AWS Summit Sydney executive-forum keynote (same day); team-structures complements the data-strategy talk"
  - type: supports
    target: 2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai
    via: "presents this exact Anthropic 'March study' (Massenkoff & McCrory) — O*NET 800 occupations + Claude usage + Eloundou exposure scores; observed vs theoretical exposure; junior-hiring slowdown ~14%; exposed workers older/educated/better-paid — as the empirical ground for the talk"
---

# A leader's guide to advanced team structures in an agentic world

> As AI agents transform the workplace, organizations must adapt their structures and methodologies… This keynote explores how leadership is evolving to meet these needs, covering new organizational models and roles that coordinate human-AI hybrid teams.
>
> *— [AWS Events YouTube channel](https://www.youtube.com/watch?v=O7u6myBRsns)*

A **~31½-minute executive-forum keynote** from the **AWS Summit Sydney**, delivered by **Steven Brovich** (Amazon since 1999; AWS Enterprise Strategist, working alongside Tom Godden's peer group of former C-level executives). It is the **Sydney edition of the same AWS Enterprise Strategy talk** the wiki already holds as [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Jonathan Allen's London Executive Forum keynote]] (21 May 2026) — same four-question framework (**economics / talent / structure / governance**), same USE/COMPOSE/BUILD, hourglass organisation, expert-generalist/Renaissance-developer, Singapore governance, and *non-determinism-is-a-feature* doctrine. This page records it as a **corroborating second source** and focuses on what Brovich adds; the full framework treatment lives on the Allen page.

## TL;DR — the four-question framework (economics / talent / structure / governance)

- **Framing.** "AI won't take your job. Someone using AI will" (Scott Galloway). The threat is the colleague/competitor who integrated the tools six months earlier. Tractor-on-the-farm and **"the horses who learn how to drive get to stay in the barn"** metaphors (an echo of [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti's]] horse-rider→driver analogy). Grounded in the [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Anthropic "March study" (Massenkoff & McCrory)]]: **observed** exposure ≪ **theoretical** (computer/math ~33% of what's possible; office/admin theoretical ~90%); **no systematic unemployment rise** since ChatGPT; **junior hiring slowed ~14%**; most-exposed workers are "disproportionately older, more educated, and better paid" — a *reshaping*, felt at entry level first.
- **Economics — the pricing scissors.** Training costs rising **2.4× per year**; inference costs falling **10× per year**; the gap "opens by **12–24× per year**." Frontier-model creation approaches billions (a handful of firms); using one collapses toward zero. Hence **USE / COMPOSE / BUILD** as three "worlds": *use* a managed solution (highest leverage, lowest differentiation), *compose* with frontier APIs (medium/medium), *build* only where you truly differentiate (highest control/cost, lowest speed). Workflows cut across worlds and migrate over time; the unhealthy path is "we're a build shop on day one." (Same framework as Allen; Brovich adds the precise cost-curve numbers.)
- **Talent — orchestrators, not builders.** The craft shifts from *building fastest* to *orchestrating fastest* — point an agent at a problem, evaluate output, steer the next iteration, know when to overrule. **Martin Fowler**/ThoughtWorks **"expert generalist"** (July 2025; seven characteristics — curiosity, collaborativeness, customer focus, first-principles thinking) is what agentic AI **amplifies**: "an agent multiplies a curious person… rewards deep fundamentals, not surface-level certification collecting." Specialists broaden, generalists deepen → they meet as **Werner Vogels' "Renaissance developer."** Evidence: Anthropic's **Build-with-Claude hackathon** (Feb 2026) — 13,000 applications, 500 accepted, 277 shipped production code, 21M lines generated; **the top three finishers were not professional developers** (1st a lawyer's California permitting tool "Crossbeam"; 3rd an interventional cardiologist's post-appointment patient-care platform built in 7 days).
- **Structure — Model A is dead; choose B or C.** The CIO shifts "from owner of the stack to conductor of the stack." Operating models must become **tolerant of variance in execution, strict about variance in outcome** ("set the outcome, give the means, resist the urge to manage the how"; agents "find their own path like a river — your job is to define the riverbank"). Three organisational models:
  - **Model A (traditional IT ops)** — engineering builds, throws over the wall to ops. **Now the anti-pattern.** Six stacked failure modes (runbooks are deterministic / ticket culture kills context / operators have no authority over the model / nor over the data / 91% of ML models degrade over time / ITIL can't keep up) → "why **95% of AI pilots fail** to achieve meaningful impact." *"Model A is dead. Full stop."*
  - **Model B (embedded)** — "you build it, you run it"; same 3–5 senior engineers build and operate the pod. Results: multiple deployments/day, sub-hour recovery, 0–15% change-failure rate ("DORA Elite territory"). Breaks past ~10 pods (duplicated auth/observability layers).
  - **Model C (B + platform)** — a shared platform provides agent infrastructure (runtime, memory, identity, observability), consistent and governed, but **enables rather than constrains**: "pods choose what to build… full autonomy, full accountability, but the road they build on is the platform." B at small scale; B+C at medium/large.
- **Governance — Singapore + policy-as-code.** Singapore IMDA's **Model AI Governance Framework for Agentic AI v1** (launched Jan 2026 at Davos by Minister **Josephine Teo**) — the first state-backed framework specifically for autonomous agents. Four dimensions: upfront risk assessment / **human accountability chains** (every agent action traced to a named human) / technical guardrails across the lifecycle / end-user transparency. Five distinguishing features: mandatory **agent identity management**, concrete testing across five risk categories, explicit **multi-agent coordination risk**, voluntary-but-directional (de facto standard for regulated/government work), and addressing the **deskilling trap** head-on. Convergence: **Amazon Bedrock AgentCore** launched on the *same four questions* — who's the agent? who authorised it? what is it allowed to do? can we audit what it did? — enforced **outside the LLM loop** ("you stop it at the gateway before the LLM ever sees the request… policy-as-code is the riverbank").

## What this source adds beyond the Allen page

The framework is the same; the **incremental value** of the Sydney edition is: (a) a *second presenter* (Brovich) independently delivering it → corroboration that this is settled AWS Enterprise Strategy doctrine, not one strategist's view; (b) **quantified economics** — the 2.4×/10×/12–24× pricing-scissors numbers; (c) the **Model A/B/C** taxonomy with six concrete Model-A failure stats and the *95%-pilots-fail* / *91%-models-degrade* / *DORA-Elite* anchors; (d) a **deeper Singapore-governance treatment** (four dimensions + five distinguishing features + the AgentCore four-questions convergence + policy-as-code-outside-the-LLM-loop); (e) the **Anthropic Economic Index** presented as the talk's empirical spine (observed-vs-theoretical exposure, junior −14%).

### The moats slide (~6:55–7:30) — full taxonomy from the deck

The talk is slide-backed; the deck begins around **6:55**, and the pivotal exhibit is a **two-row "waterline" moats slide** titled **"The Only Moats That Matter."** Slide imagery supplied by the user adds detail the ASR transcript does *not* capture (the transcript only said "the top row… moats we spent 20 years building… the bottom row… hard to get"):

- **Above the waterline — "HARD TO DO" ("AI is making these worthless as moats")**: **Workflow embeddedness · Software scale · Integration lock-in · Engineering complexity.** The buildable moats — the ones AI's time-compression erodes.
- **Below the waterline — "HARD TO GET" ("Bottlenecked by years, physics, human behaviour, political will, capital")**, each tagged with its binding constraint: **Compounding Proprietary Data** (*years of operations*) · **Network Effects** (*years of adoption*) · **Regulatory Permission** (*years of process*) · **Capital at Scale** (*decades of trust*) · **Physical Infrastructure** (*years of building*). The durable moats — the ones AI *cannot* speed up.

The slide's load-bearing aphorism (slide-only, not in the ASR): **"AI compresses the time it takes to do things. It does not compress the time it takes for things to happen."** That is the sharpest single formulation in either AWS talk of *why* the bottom-row moats appreciate while the top-row erode — the constraint on the durable moats is **elapsed time / trust / physics**, which no amount of capability gain shortens. (Spoken echo at ~30:44: "the things AI can't compress.")

This is the same **moats-erosion thesis** the wiki documents on the [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen page]] (which names the same two lists), now with the precise slide taxonomy + the time-compression aphorism — feeding [[foundation-models]]' commodity framing and [[strategy]]'s durable-advantage question. *(Moat names, per-moat time labels, and the aphorism are transcribed from the slide images the user supplied; the surrounding argument is in the transcript.)*

## Why this matters to the wiki

As a near-replication of the Allen talk three weeks later, this source's main contribution is **confidence** — it lifts the framework from single-source to a two-source AWS-vendor consensus. Concretely it strengthens: [[automation-vs-augmentation]] (orchestrator-not-builder), [[ai-employment-effects]] (the Anthropic-index reshaping + junior slowdown), [[foundation-models]] (the pricing-scissors / USE-COMPOSE-BUILD economics), [[agent-harness]] (Models A/B/C, non-determinism doctrine, policy-as-code/AgentCore), [[enterprise-ai-adoption]] (CIO-as-conductor, the Monday-morning six steps), and [[responsible-ai]] (the Singapore agentic-governance framework in operational detail).

## Dynamic-capabilities (W&W) reading

- `digital-sensing/digital-scenario-planning` — the pricing-scissors trajectory + the Anthropic labour study as forward-looking sensing.
- `digital-seizing/strategic-agility` + `balancing-digital-portfolios` — USE/COMPOSE/BUILD as a portfolio decision migrating over time.
- `digital-transforming/redesigning-internal-structures` — Models A/B/C, embedded pods, platform team, CIO-as-conductor.
- `strategic-renewal/business-model` + `organizational-culture` — moats erosion; orchestrator culture; the deskilling-prevention governance duty.
- `contextual/external-triggers` — the Singapore framework + the competitive-timeline-compression pressure.

## Linked entities and concepts

- Channel: [[Amazon Web Services]] (AWS Events).
- **Dangling** (single-source mentions, deferred): **Steven Brovich** (AWS Enterprise Strategist, presenter), Tom Godden (AWS Enterprise Strategy), **Martin Fowler** (expert-generalist; also on the Allen page), Werner Vogels (Renaissance developer; also Allen), Scott Galloway (also Allen), Josephine Teo (Singapore Minister), Mikkel Nettoko (hackathon 3rd place).
- Concepts: [[automation-vs-augmentation]], [[ai-employment-effects]], [[foundation-models]], [[agent-harness]], [[enterprise-ai-adoption]], [[responsible-ai]].

## Relationships

- *supports* [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]] — the same talk, Sydney edition; corroboration + quantified specifics.
- *supports* [[2026-06-12-aws-leaders-guide-data-strategy-agentic-ai]] — sibling same-day AWS Sydney keynote.
- *supports* [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai]] — presents this Anthropic "March study" as its empirical spine.
