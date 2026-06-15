---
type: entity
kind: org
aliases: ["Amazon Web Services", "AWS", "AWS Events"]
tags: [tech-vendor, cloud, ai-infrastructure, hyperscaler, aws-enterprise-strategy]
parent: "[[Amazon]]"
ticker: "AMZN (Amazon)"
website: "https://aws.amazon.com"
confidence: 0.85
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 6
---

# Amazon Web Services

**Amazon Web Services** (AWS) is the cloud-computing subsidiary of Amazon. Launched 2006. The dominant public-cloud provider by revenue alongside Microsoft Azure and Google Cloud — a major hyperscaler hosting much of the world's enterprise AI workload.

## Role in the wiki

Two distinct angles on AWS surface across the ingested sources:

### 1. As an AI infrastructure provider

[[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.1 timeline: Anthropic's partnership with AWS expanded by an additional **$4 billion investment from Amazon** in November 2024, bringing the total to **$8 billion**. Significant signal of AWS's commitment to frontier model partnerships.

### 2. As a thought-leadership platform

AWS runs an "Executives in Residence" program advising Fortune 500 leadership teams. [[Jana Werner]] and [[Phil Le-Brun]] (authors of [[2026-04-28-werner-lebrun-octopus-organization|"Become an Octopus Organization"]] in HBR Nov–Dec 2025) hold these positions. The Octopus framework is implicitly AWS-aligned: customer-centricity, distributed systems, microservices, decoupling — all align with AWS's core selling points (cloud microservices, serverless, decoupled architectures).

### The AWS Events keynote series ("AWS Events" YouTube channel)

The **AWS Enterprise Strategy** team (former C-level executives — Jonathan Allen, **Steven Brovich**, Tom Godden, et al.) delivers a recurring executive-forum keynote on agentic-AI leadership, published on the **AWS Events** channel (an alias of this entity). Three are in the wiki, all sharing the same four-question framework (economics / talent / structure / governance) and USE/COMPOSE/BUILD doctrine:

- [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|London Exec Forum — advanced team structures]] (Jonathan Allen, 21 May 2026).
- [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Sydney — advanced team structures]] (Steven Brovich, 12 June 2026) — the near-replication that corroborates the framework + adds quantified specifics (pricing scissors, Models A/B/C, deeper Singapore governance).
- [[2026-06-12-aws-leaders-guide-data-strategy-agentic-ai|Sydney — data strategy in the era of agentic AI]] (former-CIO Enterprise Strategist, 12 June 2026) — the data-layer companion (data-products, markdown-for-agents, minimum-viable-governance).

Discount the Octopus framing slightly for AWS's commercial interest, but the underlying argument is well-supported by examples external to AWS (Netflix, Google, Coca-Cola, U.S. Army).

### 3. As an AI-stack vendor — Jassy's three-layer framing ([[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025]])

[[Andy Jassy]] (Amazon CEO, AWS founder) named the wiki's earliest first-party three-layer AI-stack framing in May 2025:

| Layer | AWS product | Purpose |
|---|---|---|
| Bottom (infrastructure) | **Trainium** | Custom AI training chip — *"going to help people save a lot of money relative to what the cost has been to date"* |
| Bottom (infrastructure) | **SageMaker** | *"The standard way for people building their own models — to get the data in, build a model, experiment, deploy into production"* |
| Middle (orchestration) | **Bedrock** | Frontier-model marketplace + guardrails / RAG / **agentic capabilities** features — *"take a bunch of automated actions in succession"* |
| Top (applications) | **Q** | Amazon's AI coding assistant — *"the best AI-powered coding assistant"* (Jassy's framing) |

Jassy's complaint in this section: *"there was a lot of attention early on on ChatGPT … I think people have slept a little bit on the other layers of the stack"* — direct marketing message positioning AWS as the stack-vendor versus OpenAI / Anthropic as application-vendors. The structural decomposition is compatible with [[2026-05-09-chase-agent-development-lifecycle|Chase's]] later (April 2026) four-sub-layer Build split (Frameworks / Runtimes / Harnesses / No-code) at a coarser granularity. **Bedrock's agentic-capabilities feature** is the wiki's earliest first-party-CEO mention of a productised harness primitive — eight months before [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's]] Managed Agents announcement.

### 4. As an AI-stack vendor 12 months on — the USE / COMPOSE / BUILD frame ([[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London Exec Forum 2026]])

A year after Jassy's three-layer framing, **[[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Jonathan Allen]]** (AWS *Executive in Residence*, the third holder of that title to appear in the wiki after Werner and Le-Brun) gives the agentic-AI-era restatement. The **USE / COMPOSE / BUILD** economic-decision framework is the agentic-system-economics overlay on Jassy's stack:

- **USE** = third-party agentic vendor solutions (the SaaS layer Jassy's *top-of-stack* applications).
- **COMPOSE** = frontier-model APIs (Haiku / Sonnet / Opus 4.7 from Anthropic on Bedrock + cross-vendor models). **Allen reports ~80% of his AWS customers currently land here.**
- **BUILD** = train your own model. SageMaker / Amazon Nova / *the Forge* are the tooling; justified only when fine-tuning improves inference economics over the frontier model.

Allen's keynote also names the **Amazon Bedrock AgentCore** productised harness/runtime layer (announced at AWS Summit by Francesca Vasquez earlier the same day) — the AWS agentic-runtime equivalent of [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]], for *containment, simplicity, security, observability*. Brooklyn Solutions' customer testimony ratifies **AgentCore + Bedrock Guardrails** as the AWS-vendor harness composition in regulated-customer contexts (MoD, Danske Bank).

The wiki's longitudinal-AWS-doctrine reading: **the three-layer stack has stabilised at 12-month delta; what's new in May 2026 is the explicit USE/COMPOSE/BUILD economic-decision overlay on the middle (orchestration) layer.** The middle layer is where 80% of customer activity lives.

## Notable people (mentioned in this wiki)

- [[Jana Werner]] — Executive in Residence, AWS; co-author of the Octopus Org book and HBR article.
- [[Phil Le-Brun]] — Executive in Residence, AWS; co-author of the Octopus Org book and HBR article.
- **Jonathan Allen** — Executive in Residence, AWS; headline speaker at the 2026 London Executive Forum (*Dangling* — single-source so far, deferred entity-page promotion per [[../../CLAUDE.md#author-entity-promotion|second-source rule]]).
- **Anthony Liguori** — VP Distinguished Engineer, AWS; Project Mantle lead in Allen's keynote (76-day Bedrock-substrate-rebuild case) (*Dangling*).
- **Matt Garman** — AWS CEO (since June 2024); quoted by Allen on the junior-hiring-crisis moral framing (*Dangling*).
- **Francesca Vasquez** — AWS executive who introduced AgentCore / security-agent / DevOps-agent at the London Forum earlier the same day (*Dangling*; first-name-only in the transcript, presumed Francesca Vasquez).

## AWS's positioning vs. competitors (note for future ingests)

In the AI infrastructure layer:
- **AWS** — cloud + Anthropic partnership ($8B); SageMaker; Bedrock for foundation-model access
- **Microsoft Azure** — OpenAI partnership; Copilot integration
- **Google Cloud** — Gemini family; deep ML expertise via Google DeepMind

The wiki's [[foundation-models]] page lists notable models from each parent company. The AWS-Anthropic partnership likely deepens further; future ingests should track.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "aws")
SORT file.name ASC
```

## Open questions

- AWS's strategic AI roadmap beyond the Anthropic partnership — Bedrock model selection, Q business agent, Trainium/Inferentia silicon.
- The AWS Executives in Residence program — how many residents, how selected, what outputs.
- Conflict-of-interest framing: how to evaluate AWS-affiliated authors writing about org design / customer-centricity / distributed systems.
