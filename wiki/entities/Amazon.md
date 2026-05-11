---
type: entity
kind: organization
aliases: ["Amazon", "Amazon.com", "Amazon.com Inc"]
tags: [retail, cloud, ai-infrastructure, hyperscaler-parent, big-tech]
ticker: "AMZN"
website: "https://www.amazon.com"
confidence: 0.78
last_confirmed: "2026-05-11"
source_count: 2
---

# Amazon

**Amazon.com, Inc.** is a US-headquartered retail + cloud + media conglomerate. Founded 1994 by Jeff Bezos. CEO **Andy Jassy** since July 2021 (succeeded Bezos; previously founded and led [[Amazon Web Services]] from 2003).

The wiki holds Amazon as parent of [[Amazon Web Services]] and as one of the **target firms** through which the wiki's enterprise-AI-adoption literature is operationalised. Two angles surface across the ingested sources:

## Role in the wiki

### 1. As a target firm operating-the-trap-escape ([[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025]])

Andy Jassy's May-2025 HBR IdeaCast interview is the wiki's first first-party-CEO source for Amazon. Substantive operational datapoints surfaced:

- **+15% IC-to-manager ratio target** (Q1 2025, already beaten by report date) — Amazon's flatten-management initiative.
- **No-bureaucracy email alias** mechanism — 1,000+ emails received, **375 processes changed** in response.
- **5-day return-to-office mandate** — Jassy's stated rationale: invention works better in-person (collaboration density, ad-hoc whiteboarding, cultural apprenticeship). Acknowledges the measurement difficulty (*"it's very hard to measure how well you're inventing"*).
- **Three-layer AI stack framing**: infrastructure ([[Trainium]] / [[SageMaker]]) → orchestration ([[Bedrock]] with guardrails / RAG / agentic capabilities) → applications ([[Q]] / [[Rufus]] / 1,000+ internal GenAI apps).
- **Rufus** — Amazon's GenAI shopping assistant; designed to reproduce the in-store-salesperson question-narrowing pattern.
- **Foundation model for brand-sizing comparison** — apparel use case.
- **Two-way-door vs one-way-door** decision taxonomy (Bezos-era vocabulary) — Jassy uses it as the rationale for IC-level decision-making.
- **May-2025 vibe-coding prediction**: *"the number of people who are going to be able to be software developers is going to go up exponentially. Because you're going to have these coding apps that allow you to use natural language to describe what you want to go build."* The wiki's earliest vendor-CEO articulation of the floor-raising thesis — ~12 months before [[Andrej Karpathy]] coined [[vibe-coding]].

### 2. As an exemplar in the Octopus-Organization framework ([[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun 2025]])

Amazon is one of the named exemplars in the Werner-Le-Brun *Octopus Organization* framework (Tin Man vs. Octopus org-design contrast). Stephen Brozovich's late-2000s Amazon-internal visual-image-search tool is cited as an organic-utility-spreads-without-mandate example. The Octopus framing reads as AWS-aligned (the authors are AWS Executives in Residence); Amazon-as-exemplar is consistent with Jassy's own *"operate like the world's largest startup"* framing of the parent firm.

## People at Amazon (listed across the wiki)

- **Andy Jassy** — CEO since 2021; founder of [[Amazon Web Services]] (2003 → CEO until 2021). Currently Dangling first-mention (per author-entity-promotion rule); promote on second-source mention.
- **Jeff Bezos** — Founder; CEO until 2021 → Executive Chair. Currently Dangling; coined the two-way-door vocabulary that Jassy continues to use.
- **Stephen Brozovich** — Amazon engineer (~2005) who built an internal visual-image-search tool that spread organically. Dangling first-mention from [[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun]].

## Notable AI products (Amazon-side)

- **[[Amazon Web Services]]** — wholly-owned subsidiary; cloud infrastructure; entity page separately maintained.
- **Trainium** — Amazon's custom AI training chip (Dangling).
- **SageMaker** — Amazon's model-building service (Dangling).
- **Bedrock** — Amazon's frontier-model orchestration platform with guardrails / RAG / agentic capabilities (Dangling).
- **Q** — Amazon's AI coding assistant (Dangling).
- **Rufus** — Amazon's GenAI shopping assistant (Dangling).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "amazon")
SORT file.name ASC
```

## Open questions

- **Updated bureaucracy-reduction numbers** — Jassy's May-2025 *"1,000+ emails / 375 processes changed"* is a snapshot. Any Amazon disclosure or shareholder-letter update would let the wiki track the trap-escape velocity.
- **IC-to-manager ratio actuals** — Jassy named +15% target with Q1 2025 already-beaten; the actual delta is undisclosed.
- **Trainium economics** — Jassy's *"save a lot of money relative to what the cost has been to date"* claim is unquantified. Open primary-source target.
- **Rufus engagement metrics** — first-party data on session-conversion lift or shopping-assistant adoption rate.
