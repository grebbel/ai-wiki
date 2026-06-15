---
type: source
kind: video
title: "A leader's guide to data strategy in the era of agentic AI"
author: ["AWS Events"]
publisher: "Amazon Web Services (AWS Events YouTube channel); AWS Summit Sydney Executive Forum"
url: "https://www.youtube.com/watch?v=3XyNPfWWxiQ"
date_published: 2026-06-12
date_ingested: 2026-06-15
length: "~33:42 minutes (transcript ~319 ASR lines; auto-generated transcript, light cleanup)"
raw: "../../raw/videos/aws-leaders-guide-data-strategy-agentic-ai.md"
tags: [aws-events, aws-summit-sydney, data-strategy, agentic-ai, data-products, machines-as-data-consumers, context-engineering, metadata, data-governance, minimum-viable-governance, open-by-default, formula-1, real-time-data, data-ownership, markdown-for-agents, reimagine-rewire-remember, knowledge-graphs, enterprise-data]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - digital-seizing/strategic-agility
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "same AWS Enterprise Strategy executive-forum series; the data-layer complement to Allen's team-structures talk — Allen's 'context is king' + data-engineers-as-context-architects is the same thesis from the data-strategy angle"
  - type: supports
    target: 2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset
    via: "operationalises Argenti's *'AI transformation follows data transformation, not the other way around'* — both argue data-readiness is the gate on agentic adoption, and both name the garbage-in/garbage-out amplification"
  - type: supports
    target: 2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications
    via: "data-as-machine-consumable (markdown conversion, embedded quality/trust signals, metadata for agent reasoning) is the data-strategy face of the harness Context-optimization layer"
---

# A leader's guide to data strategy in the era of agentic AI

> In Formula 1, victories depend on turning millions of data points into winning decisions. Organizations can apply this same precision to unlock value from underutilized data assets. Drawing from F1's model, we present a three-part framework for data excellence: customer-focused decisions, dynamic people-powered strategies, and market-responsive structures.
>
> *— [AWS Events YouTube channel](https://www.youtube.com/watch?v=3XyNPfWWxiQ)*

A **~34-minute executive-forum keynote** from the **AWS Summit Sydney**, delivered by an **AWS Enterprise Strategist** (a self-described "former CIO"; not named in the transcript), using **Formula 1** as the running analogy for data excellence. It is the **data-strategy companion** to the wiki's AWS team-structures sources ([[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen]] / [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Brovich]]), and the wiki's most focused single source on **re-architecting enterprise data for machine consumers**.

## TL;DR

- **The data consumer has changed: machines, not humans.** Four eras of data strategy: BI (reports) → big data (lakes) → generative AI (content) → **agentic (machines are the primary consumer)**. "Agents need metadata to reason. They need memory to learn. They need context to act." Data formatted for humans — bold, italics, indentation, PDFs — is **overhead to a machine** (more tokens, no signal). **Stripe** is cited converting human docs to **markdown** so agents can reason (headers→hierarchy, lists→arrays, links→navigable).
- **The sobering stats.** **Gartner**: **80% of data-governance initiatives will fail by 2027.** HBR: **99% of organisations invest in data but only 29% see meaningful value.** **92% of agentic-AI users worry about data quality/governance**; half of data leaders say poor data quality blocks AI implementation completely. Diagnosis: organisations "prioritised data volume over data value" — celebrating petabytes collected instead of value delivered.
- **The framework: Reimagine → Rewire → Remember.**
  - **Reimagine** — challenge every assumption about what data is worth. Have a business strategy *informed by* AI, not an "AI initiative" chasing technology. **Four questions every data investment must pass or be rejected**: (1) How will it create value? (2) Is this the most direct path? (3) How quickly can we deliver? (4) **Can an agent consume this without a human translating?** "If a human needs to interpret the data, you have failed the test."
  - **Rewire** — restructure teams and ownership. **Data products** must be *purpose-built, agent-ready, metadata-enriched*, with **clear ownership at the most granular level** ("shared responsibility = shared neglect"; the CDO is "a terrible place to put ownership"). Decentralise teams by default, centralise only what speeds you up; **move data engineers into the business units** where decisions happen. F1 analogy: the driver gets 8 numbers, the pit wall gets 200, the factory gets 2,000 — all purpose-built from the same source.
  - **Remember (value)** — strategy is "what you do every day," not a document. Don't gather-clean-store-then-lake ("$50M, 5 years, one fired CIO, no value"); instead **identify a business problem → get the data that solves it right → lather, rinse, repeat**. Audit decision delays, pick 2–3 high-impact decisions, make them real-time. [[McKinsey]]: across 200+ managers, **fast + high-quality decisions outweighed almost anything else** in value creation.
- **What agents need from data — three things**: (1) **machine-readable structure** (parse without guessing), (2) **semantics** (relationships between entities — extract people/places/time, then their associations; a knowledge-graph framing), (3) **memory** across agents and interactions (so agents learn). Traditional data gives the *what*; agentic AI demands the **why** — "the more why we can give it, the more autonomous we can permit these agents to be."
- **Minimum viable governance — guardrails, not roadblocks.** Strict lockdown "creates the problems it was meant to prevent" — people go underground and build *without* safeguards. Instead: **open by default** (vast majority open within the org; a limited slice protected; only a small slice restricted), real-time policy enforcement and audit trails **built-in not bolted-on**, eight data tenets (customer-value-drives-investment, minimise decision distance, default-open access, clear ownership, trust-through-monitoring, automation — "if it's not automated, it is not done" — and real-time everything). "You can't audit your way to trust; agents need trust at speed." Governance should **accelerate** value like an F1 safety car manages risk without stopping the race.

## What was actually ingested

The full ~34-minute keynote (ASR transcript, ~319 lines, light proper-noun cleanup). The presenter is an AWS Enterprise Strategist / former CIO; the ASR did not capture a self-introduction, so attribution is to the **AWS Events** channel with the presenter named generically in body. F1 is a rhetorical scaffold throughout (AWS is the F1 title sponsor); the load-bearing content is the data-for-machines thesis, the four-question test, data products, and minimum-viable-governance.

## Why this matters to the wiki

This is the **data/context substrate** beneath the wiki's agent cluster. It operationalises, from the data-engineering angle, claims the wiki holds elsewhere: [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti's]] *"AI transformation follows data transformation"*; the [[agent-harness|harness]] **Context** layer (data products as the agent-consumable, metadata/trust-signal-enriched input — the same problem [[2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications|Chopra's Headroom]] solves at the compression/routing layer); the [[knowledge-graphs|knowledge-graph]] construction story (LLM entity-extraction → associations → context). The *"can an agent consume this without a human translating?"* test is a crisp, quotable addition to [[enterprise-ai-adoption]].

## Dynamic-capabilities (W&W) reading

- `digital-transforming/redesigning-internal-structures` — decentralise data teams by default, move data engineers into business units, granular data-product ownership.
- `digital-transforming/improving-digital-maturity` — the Reimagine→Rewire→Remember maturity path; data products with contracts/metadata/quality signals.
- `digital-seizing/strategic-agility` — real-time-data over batch, "evolution not revolution," continuous testing and learning over annual planning.
- `contextual/internal-enablers` — minimum-viable-governance, the eight data tenets, and metadata/lineage as the infrastructure that enables agentic value.

## Linked entities and concepts

- Channel: [[Amazon Web Services]] (AWS Events). Presenter: unnamed AWS Enterprise Strategist / former CIO (body mention only).
- **Dangling** (single-source mentions, deferred): **Stripe** (markdown-for-agents example), **Gartner** (80%-governance-failure stat), [[McKinsey]] (200-managers decision-speed study).
- Concepts: [[enterprise-ai-adoption]], [[agent-harness]], [[knowledge-graphs]], [[document-intelligence]].

## Relationships

- *supports* [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]] — same AWS Enterprise Strategy series; data-layer complement.
- *supports* [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset]] — operationalises *"AI transformation follows data transformation."*
- *supports* [[2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications]] — data-as-machine-consumable is the data-strategy face of the harness Context layer.
