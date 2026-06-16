---
type: source
kind: article
title: "Signals for 2026"
subtitle: "The tech trends we're watching in the new year"
author: ["Julie Baron"]
publisher: "[[O'Reilly Media]]"
section: "O'Reilly Radar"
url: "https://www.oreilly.com/radar/signals-for-2026/"
date_published: 2026-01-09
date_ingested: 2026-05-16
length: "~13 minute read (12-page PDF print)"
raw: "../../raw/articles/Signals for 2026 – O'Reilly.pdf"
tags: [annual-trends, agents, harness, context-engineering, mcp, agentic-ai, ai-product-strategy, oreilly-radar, ai-not-taking-jobs]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
  - digital-seizing/balancing-digital-portfolios
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-04-28-ftsg-convergence-outlook-2026
    via: "both are New-Year tech-outlook pieces for 2026; Signals is O'Reilly's editor-anchored shortlist of trends to watch, FTSG is the multi-author convergence atlas — complementary scopes"
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "Signals' 'increased accountability / proof of value' headline framing tracks the AI-Index empirical record of moving from experimentation to measurable adoption"
  - type: supports
    target: 2026-05-02-dutt-chatterji-ai-experimentation-to-transformation
    via: "Signals' 'shift from experimentation to measurable business outcomes' bullet directly tracks Dutt et al.'s micro-productivity-trap framing"
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "Signals names *context engineering*, *agentic development*, *eval- and spec-driven development*, and *vibe coding* as the new vocabulary for software development in 2026 — same paradigm vocabulary as Karpathy's Sequoia keynote, written for an audience of practitioners"
---

# Baron — Signals for 2026

The **O'Reilly Radar annual-outlook essay** for 2026, by **[[Julie Baron]]** (O'Reilly editor). Published **9 January 2026**. ~13 minute read. **Frames 2026 as "the year of increased accountability"** — *Expect enterprises to shift focus from experimentation to measurable business outcomes and sustainable AI costs.*

The essay's tone is editorial-curatorial rather than predictive. The opening quotes [[Tim O'Reilly]] (*"AI is not taking jobs: The decisions of people deploying it are"*) and [[Mike Loukides]] (*"At O'Reilly, we don't believe in predicting the future. But we do believe you can see signs of the future in the present"*). Six sections, each with a short framing block and 2–3 bulleted **Takeaways** that name the trends Baron expects to matter.

## TL;DR

- **2026 = accountability year.** *"Three years into a post-ChatGPT world, AI remains the focal point of the tech industry. In 2025, several ongoing trends intensified: AI investment accelerated; enterprises integrated agents and workflow automation at a faster pace; and the toolscape for professionals seeking a career edge is now overwhelmingly expansive. But the jury's still out on the ROI from the vast sums that have saturated the industry."*
- **The vocabulary shift in software development.** The new operating concepts for 2026 are **vibe coding**, **agentic development**, **context engineering**, **eval- and spec-driven development**, and **multi-agent / agent-swarm orchestration**. Coding-agent **protocols** (MCP) are named as the load-bearing standard.
- **The framing line.** *"AI isn't just a pair programmer; it's an entire team of developers."* The fundamentals — code review, design patterns, debugging, testing, documentation — *stay the same and will be what elevates purposeful AI-assisted code above the crowd*.
- **AI as infrastructure operator.** **AIOps platforms**, **agentic SRE**, **self-healing systems and predictive observability** are positioned as 2026's InfraOps frontier — AI shifts from being a workload to being *an active participant in managing infrastructure itself*. **Neoclouds** (CoreWeave, Lambda, Vultr) named as the hyperscaler alternatives gaining traction for AI workloads. **Ray on Kubernetes** as the distributed-compute framework worth tracking.
- **Data-side reorganization for agents.** AgentDB, Databricks **Lakebase**, Tiger Data's **Agentic Postgres** named as new database categories *"designed from the ground up to support agents."* Vector databases (Pinecone, Milvus, Qdrant, Weaviate) named as the agentic-RAG primitives. **DuckDB** and **ClickHouse** named as the analytical-database growth stories.
- **Security as broader attack surface.** **59% of tech professionals cite AI-driven cyberthreats as their biggest concern** (named statistic). The SOC is shifting to **agentic SOC** — specialised coordinated AI agents for triage and response; SOC-analyst role shifting from reactive alert triage to **proactive threat hunting, complex analysis, and AI-system oversight**. **Zero trust for machine identities** named as the smart opening move against agent sprawl. **Prompt injection and model manipulation** named as the new attack primitives.
- **Product management's strategic crisis.** Companies have moved past simple AI experiments but **existing product playbooks (sizing markets, roadmapping, UX) weren't designed for AI-native products**. *"Most companies have moved past simple AI experiments but are now facing a strategic crisis."* The **product builder** role — *"a full stack generalist in product, design, and engineering who can rapidly build, validate, and launch new products"* — named as the role companies are hiring for *"although few people actually possess the full skill set at the moment."*
- **AI product evaluation = mission-critical.** *"As AI becomes a core product component and strategy matures, rigorous evaluation is the key to turning products that are good on paper into those that are great in production. Teams should start by defining what 'good' means for their specific context, then build reliable evals for models, agents, and conversational UIs to ensure they're hitting that target."*
- **Design's new frontier**. Generative AI has pushed user experience beyond static screens into probabilistic new multimodal territory. **AI conversational designers** and **AI interaction designers** named as 2026 hiring categories *to devise conversation flows for chatbots and even design a model's behavior and personality*.
- **Closing line.** *"While big questions about AI remain unanswered, the best way to plan for uncertainty is to consider the real value you can create for your users and for your teams themselves right now. The tools will improve, as they always do, and the strategies to use them will grow more complex. Being deeply versed in the core knowledge of your area of expertise gives you the foundation you'll need to take advantage of these quickly evolving technologies — and ensure that whatever you create will be built on bedrock, not shaky ground."*

## Six-section structure

1. **Software Development** — vibe coding, agentic development, context engineering, eval-/spec-driven development, code review fundamentals, multi-agent / agent-swarm orchestration. Programming languages named: TypeScript / Java / C# (type safety as AI guardrail); Rust / Zig (memory safety adopted by Google, Microsoft, Amazon, Meta; Zig behind Anthropic's Bun acquisition); Python (AI/ML and edge-compute centrality).
2. **Software Architecture** — AI-enhanced and AI-native architectures; event-driven models for agentic triggers; LLMs + RAG into existing architectures; **emerging architecture patterns and antipatterns specifically for AI systems**; API and data integrations elevated by MCP.
3. **Infrastructure and Operations** — AI as primary driver of infrastructure architecture; GPU orchestration at scale; specialised networking; **Ray on Kubernetes** as distributed-compute framework; **neoclouds** (CoreWeave, Lambda, Vultr); **AIOps platforms**; **agentic SRE**.
4. **Data** — agent-supporting database categories (AgentDB, Lakebase, Agentic Postgres); vector databases; real-time analytics (DuckDB, ClickHouse); ESG/carbon-aware tooling; democratisation via low-code/no-code.
5. **Security** — broader attack surface; governance/compliance challenges; **agentic SOC**; zero trust for machine identities; prompt injection and model manipulation as new threat primitives.
6. **Product Management and Design** — proof-of-concept → proof-of-value; product builder role; AI conversational/interaction designer roles; eval-driven product development.

## What was actually ingested

Full 12-page PDF print of the O'Reilly Radar article — 13-minute reading time confirmed by length. Six sections × short framing + 2–3 takeaways each. No appendix.

## Cross-positioning with the wiki

- **Annual-outlook companion to [[2026-04-28-ftsg-convergence-outlook-2026|FTSG Convergence Outlook 2026]].** Different genres (curated trend-shortlist vs multi-author convergence atlas), same publication window, complementary scopes — together they form the wiki's **2026 New-Year outlook pair**.
- **Adoption-curve confirmation for [[2026-04-30-ai-index-report-2026|AI Index 2026]].** Baron's "accountability year / proof of value / strategic crisis" framing maps to the empirical record AI Index 2026 carries (88% org adoption, but only ~7% Stage-4 maturity per [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan AI maturity]]).
- **Vocabulary alignment with [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy at Sequoia]].** Same paradigm-vocabulary moves (vibe coding, agentic development, context engineering, multi-agent orchestration). Baron is the trade-press flagship version of the vocabulary; Karpathy is the academic-keynote version.
- **Micro-productivity-trap echo of [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al.]]**. "Existing product playbooks weren't designed for AI-native products" is Baron's compressed version of the offering-lock-in / process-lock-in framing.
- **Quotable headline for the [[concepts/ai-employment-effects]] cluster.** Tim O'Reilly's *"AI is not taking jobs: The decisions of people deploying it are"* belongs on the concept page alongside [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson's canary-in-the-coal-mine]] empirical anchor — Baron-via-O'Reilly is the **deployment-decision attribution** framing.

## Named entities (this ingest)

- [[Julie Baron]] — O'Reilly editor. **First mention.** *Dangling.*
- [[Tim O'Reilly]] — Founder of O'Reilly Media. **First mention.** *Dangling.*
- [[Mike Loukides]] — O'Reilly Radar editor; author of the monthly *Radar Trends to Watch* series. **First mention here, but second-source promotion eligible immediately given the parallel January-2026 Radar Trends ingest in this batch.** *Promoted to entity in this batch.*
- [[O'Reilly Media]] — Publisher of all eight sources in this 16 May 2026 batch. *Promoted to entity in this batch.*

Plus dangling first-mentions of: neocloud vendors (CoreWeave, Lambda, Vultr); database vendors (AgentDB, Lakebase, Tiger Data, Pinecone, Milvus, Qdrant, Weaviate, DuckDB, ClickHouse, MongoDB-derived DocumentDB); language ecosystems (Rust, Zig, Bun, TypeScript, Python).

## Source-quality notes

- **Genre**: editorial annual-outlook by an O'Reilly editor — high-credibility within trade-press; **not peer-reviewed; not empirical**. Names a single statistic (*59% of tech professionals cite AI-driven cyberthreats…*); other claims are framing-level.
- **Confidence: 0.75.** Per Lifecycle heuristic: single source, +0.05 for recognised publisher, capped at 0.80; no contradictions yet detected against existing wiki claims.
