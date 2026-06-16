---
type: source
kind: video
title: "London Executive Forum 2026 — A leader's guide to advanced team structures in an agentic world"
author: ["AWS Events"]
publisher: "Amazon Web Services (AWS Events YouTube channel)"
url: "https://www.youtube.com/watch?v=ECLHOG3uYzk"
date_published: 2026-05-21
date_ingested: 2026-05-25
length: "~43:54 minutes (transcript ~412 ASR lines)"
raw: "../../raw/videos/allen-aws-london-exec-forum-agentic-team-structures.md"
tags: [aws-events, london-executive-forum, jonathan-allen, nick-francis, brooklyn-solutions, agentic-team-structures, pm-bottleneck, project-mantle, use-compose-build, hourglass-organization, embedded-pod-model, builders-to-orchestrators, context-architects, jevons-paradox, schumpeterian-disruption, expert-generalists, renaissance-developer, anti-disposable-applications, moats-erosion, singapore-ai-governance, policy-as-code, agentcore, bedrock-guardrails, 5x-expectation, human-starts-human-ends, momentum-beats-perfection, mit-nanda-95-percent, anthropic-labor-market-impacts, nvidia-slm-paper, junior-hiring-crisis, conference-talk]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/business-model
  - strategic-renewal/organizational-culture
  - contextual/external-triggers
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering
    via: "**Independent confirmation of the PM-bottleneck thesis at AWS-Executive-in-Residence altitude, one day after Ng's talk.** Ng (DeepLearning.AI / AI Dev 26 SF, 20 May): *'AI coding has made [building] 10 or 100 times faster. And so this means that deciding what to build or the product management work becomes the new bottleneck rather than the actual building.'* Allen (AWS / London Exec Forum, 21 May, ~20:23–20:40, drawing on **Project Mantle** — an AWS internal rebuild of the layer under Bedrock that was scheduled for 18 months and shipped in 76 days when AWS put VP-Distinguished-Engineer Anthony Liguori + L7 principal engineers on it with goal-based agents): *'the bottleneck is shifting. It's not execution now. It's decisions. It's product management. And for a long time, for 30 years in my career, it has been the long tail in getting things done. Suddenly, we're seeing that invert.'* Ng named it at the conference altitude; Allen confirms it at AWS vendor altitude with a quantified internal-Amazon delivery datapoint. The 20–21 May 2026 cluster on this thesis is now three sources strong (Ng + Allen + Sinclair/Ivers/Benitez)."
    confidence: 0.85
  - type: supports
    target: 2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers
    via: "**12-month longitudinal AWS-altitude pair on Amazon's agentic-AI doctrine.** Jassy (CEO-of-Amazon, May 2025): three-layer AI stack — *infrastructure (Trainium / SageMaker) → orchestration (Bedrock — frontier-model + guardrails + RAG + agentic capabilities) → applications (Q / Rufus)*. Allen (AWS Executive in Residence, May 2026): the **USE / COMPOSE / BUILD economic decision** — *use* vendor agentic solutions, *compose* with frontier-model APIs (where Allen sees ~80% of his customers landing), *build* only when fine-tuning is justified by inference economics. The frameworks are isomorphic: Jassy's *stack-layer* and Allen's *economic-decision* are the same Amazon-vendor lens at one-year time delta. Both pair the framework with concrete operationalisation of [[micro-productivity-trap]] escape — Jassy via +15% IC-to-manager ratio + 1000+ no-bureaucracy emails; Allen via the embedded-pod model + hourglass-organization shape. The longitudinal evidence: AWS's view of agentic-AI strategy has *stabilised* in the 12 months between the two talks; what's added is **agentic-system-specific economics** (the frontier-model inference cost curve, the 2.1M-token / £45 / 12-Opus-agents personal-system datapoint) and the **non-determinism doctrine** (Allen: *'in agentic AI systems non-determinism is a feature, not a bug'*)."
    confidence: 0.8
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "**Vendor-channel-parity anchor on running AI-native engineering orgs.** Fung (Anthropic / Code with Claude 2026, 8 May): *'when agentic coding goes from individual tool to org-wide default, the tool isn't the hard part... your processes are'* + what broke at Anthropic (review, ownership, hiring) + the norms they had to rewrite. Allen (AWS / London Exec Forum, 21 May): the embedded-pod model (3–5 engineers per pod organised around *workflow*, not product or MVP) + the hourglass-organization shape + Brooklyn Solutions' *'human starts the work, human ends the work'* accountability pattern + Bedrock Guardrails for boundary management. Same problem space — re-architecting engineering org for agentic AI — at two foundation-model vendor altitudes (Anthropic + AWS), 13 days apart. Convergent prescriptions: *processes are the hard part*, *seniors review faster*, *junior learning paths need explicit protection*, *human-in-the-loop survives at the seams* (Allen: P0–P2 + P4–P5 incident response; Brooklyn: humans at the entry and exit of every workflow)."
    confidence: 0.8
  - type: supports
    target: 2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering
    via: "**Role-shift convergence at the vendor-vs-institutional altitudes.** Sinclair / Ivers / Benitez (SEI-CMU, 21 May): *'a coder is someone who just grabs a Jira ticket... software engineers go beyond that... the narrow interpretation of coding might be fading. But those who can bring engineering judgment, point AI in the right direction, connect it to the business, connect it to the users — that's an incredibly valuable skill.'* Allen (AWS, 21 May): *'domain experts are pushing outward. Generalists are deepening their domain expertise. This is leading towards this renaissance developer as Werner Vogels talked about it in his final keynote at re:Invent last year.'* Same-day anchor — *narrow-specialist-roles fade, multi-skilled-judgment-roles thrive* — at SEI/CMU-institutional altitude and AWS-vendor altitude. Allen's **Anthropic-competition exhibit** (1st place lawyer, 2nd place cardiologist from Poland building an AI-agentic patient-care platform, 3rd place cardiologist — *no developer in the top three*) is the *non-developer-domain-expert-wins* operationalisation of the same role-shift Ivers names at the engineering-discipline level."
    confidence: 0.75
  - type: supports
    target: 2026-04-28-warner-wager-dynamic-capabilities-digital-transformation
    via: "**Practitioner-altitude operationalisation of the W&W process-model microfoundations.** Warner & Wäger 2019 specify the dynamic-capability microfoundations for digital transformation across sensing → seizing → transforming → strategic-renewal buckets, derived from 27 senior-executive interviews. Allen's keynote traces the same arc end-to-end at AWS-Executive-in-Residence altitude: *digital-sensing* via the Anthropic labour-market report + MIT NANDA 95%-fail report + the Jevons-paradox / Schumpeterian-disruption framing; *digital-seizing* via the USE/COMPOSE/BUILD economic decision + rapid-prototyping (Brooklyn's 4-phase iteration) + strategic-agility (the pod model itself); *digital-transforming* via the hourglass organization + builders-to-orchestrators + data-engineers-as-context-architects; *strategic-renewal* via the **moats erosion thesis** — the old moats (workflow embeddedness, software scale, integration lock-in, engineering complexity, IP) erode under agentic AI, replaced by *compounding proprietary data*, *network effects*, *regulatory permission*, *capital at scale*, *physical infrastructure*, and the meta-moat *time-that-can't-be-parallelised*. Allen ratifies the theoretical W&W frame with vendor-altitude case material — the wiki's strongest applied example to date."
    confidence: 0.8
  - type: supports
    target: 2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai
    via: "**Anti-disposable-software ethic + quality-over-quantity convergence.** Storoni (HBR IdeaCast, 13 May): the neuroscience-grounded normative reframe on the augmentation pole of [[automation-vs-augmentation]] — *quality of attention beats quantity of output* in the AI age. Allen (AWS, 21 May) names the failure mode the inverse of which Storoni prescribes: *'we are getting to disposable applications. We do not want this as leaders.'* Brooklyn's *'momentum beats perfection'* mantra is explicitly **not** a permission to flood (Francis's 4-phase progression — basic use-cases → Ask Brooklyn conversational → agentic → multi-agent — is iterative *quality compounding*, not disposable-app proliferation). Both anchor on the same anti-Jevons-paradox-for-software ethic at neuroscience and AWS-vendor altitudes respectively."
    confidence: 0.7
  - type: supports
    target: 2026-04-28-anthropic-economic-index-q4-2025
    via: "**Allen cites the lineage** — Allen opens (~1:15–2:00) with *'this report came out from Anthropic just last month: labor market impacts of artificial intelligence... it's really only just started if you actually look at the data in here. The blue on the spider diagram you're seeing is the potential disruption right now of these frontier models. The red is where it's actually started.'* The specific April 2026 Anthropic labour-market report Allen references is **not yet ingested into the wiki**; the [[2026-04-28-anthropic-economic-index-q4-2025|Q4 2025 Index]] (and its [[2026-05-07-anthropic-economic-index-5-learning-curves|5th report follow-on]]) are the closest available anchors for the Anthropic Economic Index lineage on which Allen's labour-market framing rests. Edge type *supports* not because Allen cites the Q4 report directly, but because Allen's evidentiary scaffolding rests on the same Anthropic-Economic-Index methodology + deskilling / automation-vs-augmentation framework the Q4 report established. *Open follow-up:* ingest the April 2026 Anthropic labour-market report Allen references."
    confidence: 0.65
  - type: supports
    target: 2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting
    via: "**Consultant-altitude convergence on enterprise-AI-deployment doctrine.** Sternfels (McKinsey global managing partner, Feb 2026): enterprise-AI transformation prescriptions from the largest-consulting-firm vantage. Allen (AWS Executive in Residence, May 2026): enterprise-AI deployment prescriptions from the largest-cloud-vendor's advisory vantage. Both speak from *advisor-to-enterprise* altitude on the same problem (how do enterprises deploy AI to capture firm-level value, not task-level [[micro-productivity-trap]]); both arrive at the same workflow-centric prescription (Allen: *'AI bolted on is going to fail... ability to focus at a workflow level being the difference between success and failure'*); both name the same observed failure rate band (McKinsey: variants of 70–95% AI-pilot-fail; Allen via MIT NANDA: 95%); both prescribe the same operational pattern (embedded teams, CFO-office partnership for opportunity-cost measurement, no pre-flight ROI model). 7 concept-page overlaps between the two sources (`enterprise-ai-adoption`, `automation-vs-augmentation`, `ai-employment-effects`, `agentic-engineering`, `micro-productivity-trap`, `durable-skills`, `ai-deskilling`)."
    confidence: 0.7
confidence: 0.8
last_confirmed: "2026-05-25"
---

# London Executive Forum 2026 — A leader's guide to advanced team structures in an agentic world

> As AI agents transform the workplace, organizations must adapt their structures and methodologies to harness new opportunities. The probabilistic nature of AI requires continuous iteration and intelligent oversight, creating new ways of working across business functions. To thrive, organizations must combine clear capability assessment with agile planning while leveraging their unique domain expertise and data assets. This keynote explores how leadership is evolving to meet these needs, covering new organizational models and roles that coordinate human-AI hybrid teams. Leaders will learn strategies for balancing rapid decision-making with strategic oversight, finding the optimal mix of centralized guidance and decentralized innovation.
>
> Speaker: Jonathan Allen, AWS Executive in Residence & Nick Francis, Chief Technology & Marketing Officer, Brooklyn Solutions.

(Channel description, AWS Events.)

A 43:54 keynote + customer case study filmed at the **AWS London Executive Forum 2026**, published to the AWS Events YouTube channel on 21 May 2026. Two speakers in series:

- **Jonathan Allen**, [[Amazon Web Services]] **Executive in Residence** (~0:00–33:20), delivering the headline keynote. Allen disclosed (~0:40) that this is a continuation of a deck he first presented at AWS re:Invent in Las Vegas in December 2025, with *400 hours of revision* between then and now — interviews with customers, interviews with Amazon leaders, his own production agentic systems builds, customer go-live work. *Auto-generated transcript, ASR-cleaned at ingest.*
- **Nick Francis**, co-founder and Chief Technology & Marketing Officer of **Brooklyn Solutions** (~33:20–43:45), giving the customer testimony. Brooklyn is a UK scale-up running a supplier-management platform for regulated customers including the Ministry of Defence and Danske Bank.

**Authors / dangling list.** This is the first wiki source by both speakers; per the [[../../CLAUDE|author-entity promotion rule]] (second-source promotion), they go on the dangling list at this ingest and only get entity pages on a second citation:

- **Dangling** (single-source mention, deferred): Jonathan Allen (AWS Executive in Residence), Nick Francis (Brooklyn Solutions co-founder / CTMO), Brooklyn Solutions (UK supplier-management scale-up — *organisation*), Anthony Liguori (AWS VP Distinguished Engineer, Project Mantle lead), Matt Garman (AWS CEO, quoted by Allen on the junior-hiring crisis), Jeff Bezos (named by Allen as having *"eliminated level 9 in Amazon"*), Scott Galloway (quote: *"AI won't take your job. Someone using AI will"*), Rory Sutherland (quote on probabilistic-vs-deterministic business), Martin Fowler (strangler-fig pattern + expert-generalists post), Werner Vogels (re:Invent keynote anchor for *"renaissance developer"*), William Gibson (the *"future is here but not evenly distributed"* quote).

## TL;DR

Five substantive contributions warrant ingest:

1. **The PM-bottleneck thesis, independently confirmed at AWS vendor altitude with a quantified internal-Amazon datapoint.** Allen names *Project Mantle* — an AWS internal rebuild of the layer under Amazon Bedrock that was scheduled for ~18 months and shipped in **76 days** when AWS put VP-Distinguished-Engineer **Anthony Liguori** + L7 principal engineers on it with goal-based agents. The load-bearing claim (~20:23–20:40): *"the bottleneck is shifting. It's not execution now. It's decisions. It's product management. And for a long time, for 30 years in my career, it has been the long tail in getting things done. Suddenly, we're seeing that invert."* This is **independent confirmation** of [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng's PM-bottleneck thesis from one day earlier]] at a different vendor altitude. The 20–21 May 2026 cluster on this thesis is now three sources strong (Ng + Allen + [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Sinclair/Ivers/Benitez SEI-CMU]]).

2. **The USE / COMPOSE / BUILD economic-decision framework** (~9:50–13:30). Allen's headline operational model for enterprise agentic-AI strategy: enterprises choose between *using* third-party agentic solutions (the SaaS vendors knocking on your door), *composing* with frontier-model APIs (Allen sees **~80% of his customers** landing here right now — *"they don't want to train those models. They just want to hit the frontier model... whether they're using Haiku, the small model, or Sonnet or Opus 4.7, available just this last few days"*), or *building* their own fine-tuned model when economics justify it. The framework is the **USE/COMPOSE/BUILD analogue** of [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy's three-layer AI stack from May 2025]] (infrastructure / orchestration / applications) — same Amazon-vendor lens at 12-month delta, with Allen adding agentic-system-specific economics and the **inference-cost-vs-training-cost curve** as the decision driver.

3. **The embedded-pod model + hourglass organization** (~28:18–31:11) as the operational shape that survives the agentic transition. *"Three to five engineers per pod. What is the business outcome? They're solving workflow. Notice I didn't say product. I didn't say MVP. I said workflow."* Past 3–4 pods you need a platform team — *"because without a platform team, you're going to have inconsistency of build. You're not going to have the observability"*. Crucially, the platform team's job is *removing friction from the pods, not controlling them*. Allen pairs the pod model with the **hourglass organization** as the counter to *"seniors 20×-ing productivity and we're cutting back on juniors"* — he argues for keeping the junior pipeline because of the **junior-hiring crisis** he names empirically (73% entry-hiring collapse in European tech per Ravio; 7% new grads → big tech, down from 15%; 7.7% junior headcount decline; 9% senior employment growth). The hourglass is the answer to *"if you stop training the juniors, where on earth do your seniors come from in 5 to 10?"*.

4. **The moats-erosion thesis** (~5:30–6:48). The old moats — *workflow embeddedness, software scale, integration lock-in, engineering complexity, IP locked in software* — erode under *"6 months of seed funding and 30 engineers and an Anthropic frontier model [that] could replace your business entirely"*. The replacement moats: **(1) compounding proprietary data, (2) network effects, (3) regulatory permission, (4) capital at scale, (5) physical infrastructure** — and the meta-moat **"time that can't be parallelised"**. Allen's worked example: *"I have had conversations with banks that are thinking of expanding their branch network again. Who would have thought it? Because that suddenly differentiates their business."* This is the AWS-vendor-altitude framing of [[strategic-renewal/business-model|business-model strategic-renewal]] under agentic AI.

5. **Brooklyn Solutions' phased ingest discipline + 5× expectation + human-starts-human-ends accountability** (~33:20–43:45). The customer testimony is operationally rich: (a) Four-phase progression — *basic use-cases → conversational "Ask Brooklyn" → agentic → multi-agent* — with *"no grand plan. Each phase found its way with the previous one"*; (b) **The "5× expectation"**: *five times the output for as little as 25% increase in opex* (*"you're not going to be able to do that in people"*); (c) **Human-starts-human-ends** accountability — *"we essentially always have a human start the work and a human end the work. But we may have agents of all different sorts in between... what that makes sure is the human themselves are still accountable"* — Brooklyn's regulated-customer (MoD, Danske Bank) compliance shape; (d) **Don't wait for perfect data** — Brooklyn's segmentation-table example (numbers 1–5 mapping to *critical / important / transactional* labels) showed the LLM gave *"weird at best"* responses until they iteratively added context to *what constitutes a critical supplier, what governance a critical supplier is expected to go through*; (e) **Frequency × variability use-case discovery** — workshops with SMEs to find *"things that are mundane, high-frequency, not that variable, that happen day in, day out"*.

## What was actually ingested

Full transcript (~43:54 of dialogue, 412 ASR-cleaned segments). The talk has no chapter markers; speaker switch at ~33:20 (Allen → Francis). Allen's keynote is slide-driven (the talk references *"some of these slides are dense"* and invites the audience to photograph them) but slides are not extracted into the wiki — the substantive claims survive in the transcript verbatim.

## Allen — the keynote (33:20)

### 1. Framing — *"am I the horse?"* (0:07–1:15)

Allen opens with the Scott Galloway quote *"AI won't take your job. Someone using AI will"* and the meta-quote *"am I the horse in what's going on right now? We don't want to be the horse, right? We want to be in charge."* The talk's hidden argument: the [[automation-vs-augmentation|automation-vs-augmentation]] choice is **not** the right framing for leadership — the right framing is *who controls the orchestration*. The disposition of agentic AI is set by the operating model around it, not the model itself.

### 2. The labour-market data (~1:15–2:00) — an external Anthropic citation

Allen anchors with *"this report came out from Anthropic just last month: labor market impacts of artificial intelligence... it's really only just started if you actually look at the data in here."* The April 2026 Anthropic labour-market report Allen references is **not yet in the wiki** — the closest existing anchor is the [[Anthropic Economic Index|Anthropic Economic Index]] series, specifically [[2026-04-28-anthropic-economic-index-q4-2025|Q4 2025]] and [[2026-05-07-anthropic-economic-index-5-learning-curves|the 5th report]] (see this page's `relationships:` block for the typed edge). *Open follow-up*: ingest the April 2026 Anthropic labour-market report Allen references.

### 3. What is an agent? — the spectrum and the working definition (~2:07–3:25)

Allen's spectrum (left to right): **automation** (cron jobs, *"still heavily used in agentic systems"*) → **AI assistants** (ChatGPT, Claude) → **goal-based agents** (the coding assistants — Claude Code, OpenAI Codex, Amazon Kiro — *"which really only started in legitimacy October last year, have fundamentally changed the game"*) → **agentic systems**. Allen's working definition (~3:09): *"an agentic system is fundamentally a prompt with context or the ability to pull tools in that's hitting a language model."* Allen's empirical anchor: *"80% of the use cases that customers are hitting is actually one of the frontier models when they're building these systems."* The wiki's [[agentic-engineering|agentic-engineering]] concept page can take this definition as a clean vendor-altitude restatement (the harness operationalises this; see [[agent-harness]]).

### 4. Jevons paradox for software → "disposable applications" (~3:59–5:24)

Allen's headline framing of the productivity-multiplier question: this is **Jevons paradox**, not *job-threat*. *"5,000 years ago, from the emergence of the bronze chisel... through to electricity... through to silicon... through to cloud, now through to AI"* — every general-purpose-technology epoch has elastic demand for the cheapened output. *"Software is going through the roof and beyond. We are getting to disposable applications."*

The normative move (~5:30): *"We do not want this as leaders, right?"* — Allen frames *disposable applications* as the failure mode of agentic productivity, not a desirable end-state. This anchors the **anti-disposable-software ethic** on the augmentation pole of [[automation-vs-augmentation]] — a normative reframe that aligns with [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni's quality-over-quantity argument]] at neuroscience altitude.

### 5. The moats-erosion thesis (~5:30–6:48)

The talk's first load-bearing strategic argument. The fear conversation Allen has been having for *"the last five or 6 months since these goal-based agents came out"*: *"could 6 months of seed funding and 30 engineers and an Anthropic frontier model replace your business entirely?"*

The eroded moats: **workflow embeddedness, software scale, integration lock-in, engineering complexity, IP-locked-in-software**. *"I have hid behind decades of technology that I've built before going, 'you're not going to be able to come after me. I have a lot of IP locked in the software I've built.' Wow, that just changed, didn't it?"*

The replacement moats: **(1) compounding proprietary data, (2) network effects, (3) regulatory permission, (4) capital at scale, (5) physical infrastructure** — with the meta-moat **"time that can't be parallelised"**. The bank-branch-network example (*"I have had conversations with banks that are thinking of expanding their branch network again"*) is the worked counterexample of *physical infrastructure as moat*.

This is the AWS-vendor-altitude framing of [[dynamic-capabilities|strategic-renewal/business-model]] under agentic AI, and operationalises [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger's]] *strategic-renewal* bucket with vendor-altitude case material.

### 6. The MIT NANDA citation — 95% AI pilots fail (~7:02–8:48)

Allen cites the MIT NANDA enterprise-investment report headline: *"Despite 30 to 40 billion in enterprise investment to GenAI, this report uncovers a surprising result, and that 95% of organizations are getting zero return."* The named failure modes:

- **Lack of workflow alignment** — *"AI bolted on is going to fail"*. Allen's load-bearing prescription is *workflow-level focus* as the success / failure pivot.
- **Wrong targets** — *"companies aiming at sales and marketing high visibility instead of back-office operations where there's higher ROI are going to struggle."*
- **Missing integration** — *"pilots stay as demoed, never connected to actual business decision flows. Pilot purgatory."*

The 5% pattern: *"picking one point and executing well — implementations that adapt, involved, customized, and specialized for critical tasks. Right team composition... and integrated into real business decision flows from day one."* This is the [[micro-productivity-trap|micro-productivity-trap-escape]] prescription at AWS vantage, paralleling [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels/McKinsey's]] consultant-altitude prescription.

### 7. The Nvidia SLM paper — *"economics first"* (~8:53–13:30)

Allen names the Nvidia *"Small Language Models are the future of agentic AI"* paper (mid-2025) and warns it has *"sent some people to an interesting place and not always the right one"*. Allen's counter-doctrine: **the economics is the first decision**, not the model size. He shows the cost curve — transformer-2017 trained for **$900**, frontier models trained for *"that much money"* (multi-millions), inference cost *"dropped, dropped"* — and lays out the **USE / COMPOSE / BUILD** decision:

- **USE** vendor agentic solutions (the SaaS vendors). Legitimate in many scenarios.
- **COMPOSE** with frontier-model APIs (the OpenAIs, Anthropics, AWS). Where Allen sees **~80% of his customers landing right now**. *"They don't want to train those models. They just want to hit the frontier model. And whether they're using Haiku, the small model, or Sonnet or Opus 4.7, available just this last few days, that's what they're choosing to do."*
- **BUILD** your own fine-tuned model. Justified only when *"you've built something where a frontier model can actually give you an inference cost which is cheaper than you maintaining that model."*

Three customer examples (~12:14–13:05): a **recruitment platform** (frontier model for résumé-job matching at 90% pass/fail; built their own only when scale economics demanded it), **customer service** (Connect + frontier model for hard cases, built-their-own sentiment-analysis model at scale), **supply chain optimisation**. The decision is *"an economic decision first and foremost. And the team to go and build is very different to the team to compose, that's very different to the team to use."*

Allen's personal-system datapoint (~13:18–13:31): *"12 Opus agents, did a run, it consumed 2.1 million tokens, cost me 45 quid, one run. That isn't going to scale when you've got millions of customers. So things like batch optimization, caching, really important here."*

The USE/COMPOSE/BUILD framework is isomorphic to [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy's three-layer AI stack from one year earlier]] — same Amazon-vendor lens, with Allen overlaying agentic-system-specific economics. See the `relationships:` block.

### 8. Data engineers → context architects (~13:43–15:23)

The role-shift Allen catalogues across USE / COMPOSE / BUILD:

- **USE**: data engineers move from *building integration pipelines* to *ensuring source systems are clean* — *"if you're not building a Pydantic layer to make sure that data going into the agent's correct, expect problems."*
- **COMPOSE**: data engineers used to build RAG pipelines and vector databases. *"Well, that goal-based agent can now write that better than they can. Now, context is king — or queen, depending on who you are."*
- **BUILD**: data engineers used to create training sets; now composing data to help train automatically.

The talk's tightest data-doctrine line: *"data engineers are becoming context architects... monitor data quality, not just data flow."*

The **ETF / silver-price** worked example (~14:40–14:52) — *"they assumed that an ETF that tracks the price of silver would understand the price of silver. No, not unless you put that into context. The agent won't, and it will get really confused on the two prices."* — is a clean micro-case for the [[agent-harness|harness]] context-management discipline.

### 9. The CFO-office partnership for opportunity-cost measurement (~15:28–16:21)

Allen names *"there is no credible model that I have been able to find right now for monitoring and measuring NPV or ROI prior to going into this"* and prescribes the working alternative: *"embed a financial analyst with that team. Have them understand what the opportunity cost is with time saved, with data sets, with decisions, with outputs."* The decision discipline: *"are we pivoting or persevering an idea really, really quickly?"* — the Eric-Ries lens applied to agentic-AI use-case selection. *Hour-by-hour scope flexibility* replaces *front-end ROI gating*.

### 10. From specialist squads → mixed-skill teams; the renaissance developer (~16:33–19:35)

The talent landscape:

- **Strangler fig + expert generalists** — Martin Fowler's coinage; Allen leans on Fowler's *expert generalist* post explicitly.
- **Domain experts pushing outward** + **generalists deepening domain expertise** → *"renaissance developer"* (Werner Vogels' final re:Invent 2025 keynote framing).
- **Anthropic competition exhibit**: 1st place a lawyer, 2nd place a cardiologist from Poland building an AI-agentic patient-care platform, 3rd place a cardiologist. *"No developer in the top three."*
- The new team shape: software engineers with deep business-outcome understanding + domain experts orchestrating workflows + business-process experts + lawyers dropping into delivery teams. *"Not own — orchestrate alongside business process experts."*

This is the [[durable-skills|durable-skills]] doctrine applied to organisational composition, and the AWS-vendor framing of the role-shift thesis [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Sinclair/Ivers/Benitez name at the SEI-CMU institutional altitude]].

### 11. The PM-bottleneck thesis — Project Mantle (~19:43–24:24)

The talk's load-bearing strategic claim. **Project Mantle**: an AWS internal team that rearchitected the layer under Amazon Bedrock — *"We thought this was going to take us a long time, maybe even a year and a half."* The team was VP-Distinguished-Engineer **Anthony Liguori** (*"we have only a few of these folks in AWS"*) + L7 principal engineers. Delivery: **76 days**.

The inference (~20:23–20:40): *"the bottleneck is shifting. It's not execution now. It's decisions. It's product management. And for a long time, for 30 years in my career, it has been the long tail in getting things done. Suddenly, we're seeing that invert. So our domain experts and our business-leader colleagues aren't ready to make decisions."*

**This is the wiki's first quantified independent confirmation of [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng's PM-bottleneck thesis from one day earlier]]** at AWS-Executive-in-Residence altitude with a named internal-Amazon delivery datapoint (Project Mantle / Liguori / 76 days vs 18 months). The 20–21 May 2026 cluster on this thesis is now three sources strong.

The companion observation: **security agent + DevOps agent** as the *companions* that go into the pods to remove heavy lifting — security-static-and-dynamic code reviews accelerated, pen-testing accelerated, **MTTR** accelerated, log-analysis 50× (Amazon SecOps engineers from 6 hours → 7 minutes on the same log volume; *"we monitor 400 trillion network flows per day"*). The human-in-the-loop survives at the seams: *"P0, P1, P2, P4, P5 — humans are going to be involved in those higher incident limits than they still are right now."*

### 12. The hourglass organization vs the junior-hiring crisis (~22:48–25:54)

The talk's load-bearing organisational-shape claim. Allen rejects the *"seniors 20×-ing their productivity and we're cutting back on the juniors"* default. The empirical anchor of the **junior-hiring crisis**:

- **73% entry-hiring level collapse in European tech** — per Ravio (2025 study).
- **7% of new grads entering big tech, down from 15%**.
- **7.7% junior headcount decline**, **9% employment growth** in senior roles.
- *Fastest-growing US top job title: AI engineer*. *1.3M new AI roles created* (per web sources Allen cites). *67,000 open software-engineer roles vs ~52,000 layoffs*.

The Amazon levelling anchor (~25:08–25:54): L4 (graduate) → L11. *"Jeff Bezos has eliminated L9."* *"If you stop training the juniors, where on earth do your seniors come from in 5 to 10?"*

The **hourglass organization** is the prescription: keep the junior pipeline + accelerate their path to seniority via agentic tooling rather than cutting them. Matt Garman is named as the AWS CEO endorsing the *"first job opportunity"* moral framing.

This is the AWS-vendor anchor on [[ai-employment-effects|ai-employment-effects]] + [[ai-deskilling|ai-deskilling]] (Allen treats *protect the junior learning path* as the active counter to passive deskilling).

### 13. Non-determinism as feature, not bug; toll gates → toil gates (~26:01–28:07)

Allen's load-bearing leadership-shift claim. Traditional enterprise organisations *"have optimized for determinism. But in agentic AI systems, non-determinism is a feature, not a bug."* The path to *high agency* — *"we all understand what managing a high-agency individual looks like"* — requires this leadership inversion. The talk's tightest critique of legacy enterprise discipline:

- *"We've spent years building these toll gates — or should it be toil gates — to help these deterministic systems find their own path."*
- *"An agentic system, much like a river busting its banks, agents do find their own path."*
- Rory Sutherland citation: *"Most business is probabilistic, but everyone in business wants to prove and pretend that it's deterministic. So every spreadsheet is in some ways an act of pretense, because it's past information which you pretend has wonderful predictive value."*

The operating-model corollary: *"If you still have engineering and operations as two different things, you are going to struggle with agentic systems."* *"Runbooks are deterministic. Agents are not. Ticket culture kills the context. No authority over the model. No ability to change anything. No authority over the data — feedback loop of death — leads to that statistic from the MIT NANDA report first of all."*

### 14. The embedded-pod model + platform-team gate (~28:18–31:11)

The talk's load-bearing operational-shape claim. The model that works:

- **3–5 engineers per pod**, organised around a **business outcome / workflow** (not product, not MVP).
- Pod composition strengthened by the **hourglass** — *"seniors already understand production. Agents are absorbing some of that junior work, but we've got to help those juniors now get to that senior level much faster."*
- **Past 3–4 pods → platform team required**. *"Without a platform team, you're going to have inconsistency of build. You're not going to have the observability."*
- The platform team's job: ***removing friction from the pods, not controlling them***. *"Those platform teams have got to have absolutely really good emotional intelligence to empower those pod teams, not hold them back."*

The **SRE caveat** (~30:20–31:00): *"SRE works very well for Google... because their SREs are the most senior developers that exist in Google. If you're just renaming IT ops to SRE, same skills, that is going to fail. And I have seen it fail with customers."*

### 15. Governance — the Singapore model + policy-as-code (~31:19–33:13)

Allen's governance recommendation. The **Singaporean model announced at Davos 2026** is the only government framework Allen rates as adoptable: four principles — *(1) assess and bound risks up front, (2) human accountability, (3) technical controls across lifecycle, (4) end-user responsibility*. Identity management, deskilling prevention, multi-agent risk, five risk categories — *"this is now actionable for our customers to overlay into it."*

The lock-down: **policy-as-code**. *"As much as we've become experts at policy-as-code in CloudFormation and your controls and control objectives, we also see it utterly, utterly crucial in agentic systems."*

### 16. Allen's take-aways (~32:39–33:13)

- *Map your workflows to the [USE/COMPOSE/BUILD] tiers.*
- *Measure the verification tax* — *"you do not want 2.74× more vulnerabilities coming in to you."*
- *Escape Model A* (the deterministic legacy operating model) — *"for those of you that are still running in it, I'm sorry. It won't work for agentic systems."*
- *Implement that governance that's appropriate for you.*
- *Audit your seniority mix. Be prepared to bridge the gap from juniors to seniors, and protect that junior learning path.*

## Francis (Brooklyn Solutions) — the customer testimony (~33:20–43:45)

### 1. Brooklyn's four-phase progression (~34:10–36:14)

- **Phase 1** — basic use cases (document summarisation, formatting, key-point extraction).
- **Phase 2** — *Ask Brooklyn*, a conversational layer of bots over LLMs queryable by users in natural language.
- **Phase 3** — agentic AI: agents that *execute within the software*, not just advise.
- **Phase 4** (current) — multi-agent agentic AI.

*"We never had a grand plan. Each phase found its way with the previous one."* Operating mantra: *advising → acting on behalf of users*.

### 2. The data-context lesson the hard way (~36:49–38:11)

The wiki-relevant micro-case. Brooklyn assumed *"naively out the gate that we could hook up the AI and the large language models of all sorts to our standard SQL database in the application. How wrong we were."* The database was built for the *application* (UX overlay, user-facing); the LLM's responses were *"weird at best."* Worked example:

> *"We have a segmentation system in Brooklyn which essentially just buckets suppliers from critical to non-critical. In that table in the database, it essentially says numbers 1 to 5: critical, important, transactional, etc. What we've had to do now, as we've learned the hard way, is add context to all parts of the database as to what constitutes a critical supplier, what governance a critical supplier is expected to go through. And by doing that on an iterative basis across the database when delivering our use cases, we get much better results from the AI."*

The mantra: *"don't wait for perfect data. Start with what you've got. Start with a use case and iterate on top of your data on those use cases."* The wiki's [[agent-harness|harness]] doctrine on context engineering finds vendor-customer-side ratification here.

### 3. Bedrock Guardrails as boundary layer (~38:57–39:13)

*"We have to tune it. We have to manage that through things like Bedrock Guardrails. We define boundaries which the agents operate in through the prompts as well. We ground our data in reality."* Brooklyn's harness composition: AWS Bedrock + Guardrails + AgentCore (observability).

### 4. Builders → orchestrators; mixed teams (~39:13–40:06)

*"Everyone in Brooklyn that's a developer, and in all other teams, have been asked to work with agents and build their personal team and functions with including AI as a resource in that team."* The task-level decision: *"Does AI genuinely improve the situation, or is it AI for AI's sake?"* The architectural commitment: *"We build for reuse, using the same pattern over and over again."* This mirrors Allen's *"builders to orchestrators"* framing at the customer-implementation altitude.

### 5. Human starts the work; human ends the work (~40:13–40:54)

Brooklyn's regulated-customer (MoD, Danske Bank) accountability pattern. *"We essentially always have a human start the work and a human end the work. But we may have agents of all different sorts in between that taking place doing steps that are now highly automated that weren't to begin with. But what that makes sure is the human themselves are still accountable for the work that gets done. We work with regulated clients. They need that accountability."* This is the wiki's first **vendor-customer-side formalisation** of the *human-at-the-seams* accountability shape — agents in the middle, humans at entry and exit.

### 6. The 5× expectation (~40:54–41:47)

Brooklyn's internal productivity target: **5× output for ≤25% opex increase**. *"You're not going to be able to do that in people. So we're asking them to fundamentally look at the way that they're doing things and increase that output to 5× where possible by using a series of tools and agents, rather than getting in people and personnel and how they'd scale a business."* Quarterly executive reviews keep it honest.

### 7. Use-case discovery via frequency × variability (~41:47–43:00)

Brooklyn's customer workshop format. SMEs surface tasks that are *"mundane, high-frequency, not that variable, that happen day in, day out"* — *known output, known format*. These are the volumetric AI candidates. *"How we do that is we sit down with subject matter experts from all departments and all divisions, and typically within your businesses you'll find these people as well that just through conversation they'll tell you these things."*

### 8. Closing — *momentum beats perfection* (~43:00–43:45)

*"In Brooklyn, we had no grand strategy, just a basic use case that we learned from and we built from there. We've got a backlog of over a hundred now, but each phase revealed itself as the next one closed off. The mantra: momentum beats perfection. Don't over-plan it. Don't wait for perfect data. Don't wait for the technology to settle, otherwise you'll miss the opportunity."*

The closing aphorism's interpretation matters — *momentum beats perfection* is **not** a permission to flood disposable applications (the Brooklyn 4-phase progression is iterative *quality compounding*, not throw-and-see). Read alongside Allen's anti-disposable-applications stance (§4 above), Brooklyn's *momentum* is *small + frequent + iterative*, **not** *abundant + fast + careless*.

## Substantive contributions to the wiki

**To [[enterprise-ai-adoption]]:** the USE/COMPOSE/BUILD framework (~80% of customers landing at COMPOSE); the MIT NANDA 95%-fail / 5%-pattern doctrine; the embedded-pod model (3–5 engineers / pod, past 3–4 pods → platform team); Brooklyn's frequency × variability use-case discovery method.

**To [[automation-vs-augmentation]]:** the anti-disposable-applications normative reframe on the augmentation pole; the *humans on judgment, agents on execution* principle (Allen's *"put humans on judgment work, agents on execution work"*); Brooklyn's *human starts / human ends* operational shape.

**To [[micro-productivity-trap]]:** *AI bolted on is going to fail*; *pilots stay as demoed, never connected to actual business decision flows*; the workflow-level focus prescription as the success/failure pivot. Convergent with [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels/McKinsey]] at a different advisor altitude.

**To [[ai-employment-effects]]:** the **junior-hiring crisis** with Ravio + new-grads-into-big-tech + AI-engineer-fastest-growing-title datapoints; the **hourglass-organization** counter-prescription; *fastest-growing US top job title: AI engineer*; *1.3M new AI roles created*.

**To [[ai-deskilling]]:** the Singapore governance model's *deskilling prevention* category; Allen's *"protect that junior learning path"* as the AWS-vendor anchor on active anti-deskilling discipline; the hourglass-vs-pyramid organisational counter-shape.

**To [[agent-harness]]:** Brooklyn's vendor-customer-side ratification of context-engineering discipline (the critical-supplier segmentation worked example); Bedrock Guardrails + AgentCore as the AWS-vendor harness composition; Allen's *"data engineers are becoming context architects"* as the harness role-shift line.

**To [[agentic-engineering]]:** Allen's working definition (*"an agentic system is fundamentally a prompt with context or the ability to pull tools in that's hitting a language model"*) + the USE/COMPOSE/BUILD economic-decision frame as the strategic-altitude operational corollary of [[agentic-engineering|agentic-engineering]] discipline.

**To [[dynamic-capabilities]]:** the keynote-length practitioner-altitude operationalisation of [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger]] — sensing / seizing / transforming / strategic-renewal traced end-to-end with vendor-altitude case material. See the `relationships:` block.

**To [[software-3.0]]:** Allen's *"non-determinism is a feature, not a bug"* + the *toll gates → toil gates* critique = the operating-model corollary of the [[software-3.0|Software 3.0]] paradigm at AWS-vendor altitude.

**To [[durable-skills]]:** the *renaissance developer* + *expert generalists* + *domain experts pushing outward / generalists deepening domain* prescriptions; the Anthropic-competition exhibit (lawyer + cardiologist + cardiologist; no developer in top 3) as the *non-developer-domain-expert-wins* operationalisation.

## What's *not* in this source

- **No empirical agentic-AI benchmark data.** Allen cites internal Amazon datapoints (Project Mantle 76 days, SecOps 6h→7min on log analysis, 400T network flows / day, 2.1M tokens / £45 personal-system run) but no published agentic benchmarks (no SWE-bench, no GAIA, no harness-vs-no-harness comparisons). For benchmarks, see [[ai-benchmarks]] and the harness-empirical sources cited there.
- **No specific April 2026 Anthropic labour-market report.** Allen cites it but the wiki has not ingested it; the [[2026-04-28-anthropic-economic-index-q4-2025|Q4 2025 Economic Index]] and [[2026-05-07-anthropic-economic-index-5-learning-curves|5th-report follow-on]] are the closest available anchors. *Open follow-up.*
- **No Nvidia SLM paper ingest.** Allen cites it as a fork-in-the-road framing but the paper isn't yet in the wiki. *Open follow-up.*
- **No MIT NANDA report ingest.** The 95%-AI-pilots-fail headline statistic Allen anchors his middle-section critique on lives in this report and would warrant its own source page. *Open follow-up.*

## Open questions for next ingest

- What does the **April 2026 Anthropic labour-market report** actually say — does it confirm or refine the [[Anthropic Economic Index|Economic Index]] series' deskilling + automation/augmentation framework?
- Is the **Project Mantle** ratio (76 days actual / ~18 months estimated) reproducible across AWS services / other vendors? Allen cites it as anecdotal-but-real; what would a corpus of 20–50 such ratios look like?
- Does the **5× expectation** (5× output / ≤25% opex) hold for Brooklyn at a year horizon, or is it a phase-3 forecast that the multi-agent phase-4 will revise? Worth a follow-up ingest if Brooklyn publishes quarterly retrospectives.
- Is the **Singaporean Davos-2026 governance model** the dominant emerging framework, or do the [[eu-ai-act|EU AI Act]] / NIST AI RMF / UK AI assurance frameworks converge with it? Worth comparing once an ingestible source on the Singaporean model lands.
