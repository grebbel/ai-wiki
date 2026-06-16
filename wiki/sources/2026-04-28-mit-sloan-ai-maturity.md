---
type: source
kind: article
title: "How to boost your organization's AI maturity level"
author: ["Kristin Burnham"]
research_by: ["Stephanie Woerner", "Peter Weill", "Ina Sebastian", "Evgeny Káganer"]
publisher: "MIT Sloan / Ideas Made to Matter"
section: "Artificial Intelligence"
url: "https://mitsloan.mit.edu/ideas-made-to-matter/how-to-boost-your-organizations-ai-maturity-level"
raw: "../../raw/articles/How to boost your organization’s AI maturity level _ MIT Sloan.pdf"
date_published: 2025-10-07
date_ingested: 2026-04-28
tags: [mit-sloan, mit-cisr, ai-adoption, ai-maturity, four-s-framework, organizational-change]
length: "3 pages"
---

# MIT Sloan — How to boost your organization's AI maturity level

## TL;DR

A summary of an [[MIT CISR]] research briefing by [[Stephanie Woerner]], [[Peter Weill]], Ina Sebastian, and Evgeny Káganer. Introduces a **four-stage enterprise AI maturity framework** and four organizational challenges ("Four S": Strategy, Systems, Synchronization, Stewardship) for moving from Stage 2 (pilots) to Stage 3 (scaled AI ways of working) — the **financial inflection point**. Backed by MIT CISR's 2022 Future Ready Survey (N=721) plus 2024 interviews with 16 executives at 9 enterprises.

## Key claims

### The four stages of enterprise AI maturity

| Stage | Name | % of firms | Attributes | Focus |
|---|---|---|---|---|
| 1 | Experiment and prepare | **28%** | Educating workforce; setting acceptable-use policies; making data accessible; ensuring decision-making uses data; identifying where humans need to be in the loop | Exploration and education |
| 2 | Build pilots and capabilities | **34%** | Beginning to simplify and automate processes; creating use cases; sharing data via APIs; coach-and-communicate management style; using LLMs (out-of-box traditional and GenAI) to augment work | Business cases and pilots |
| 3 | Develop AI ways of working | **31%** | Expanding process automation; test-and-learn; architecting for reuse; incorporating pretrained models; investigating proprietary models; exploring autonomous agents | Scaling AI platforms and dashboards |
| 4 | Become AI future-ready | **7%** | Embedding AI into decision-making and processes; creating and selling AI-augmented business services; combining traditional, generative, agentic, and robotic AI | Continuous innovation and new revenue streams |

### The financial inflection is at Stage 2 → Stage 3

- **Organizations see the greatest financial impact moving from Stage 2 to Stage 3.**
- Enterprises in Stages 1–2 had financial performance **below industry average**.
- Enterprises in Stages 3–4 had financial performance **well above industry average**.
- Maturity score is constructed as the equally-weighted combination of three measures: effectiveness of AI to (i) improve operations, (ii) improve customer experience, (iii) support and develop the ecosystem. On a 0–100% scale: Stage 1 = 0%–49%; Stage 2 = 50%–74%; Stage 3 = 75%–99%; Stage 4 = 100%.

### Four challenges to move Stage 2 → Stage 3 (the "Four S")

1. **Strategy** — Align AI investments with strategic goals, and offer measurable, scalable value.
2. **Systems** — Architect modular, interoperable platforms and data ecosystems to enable enterprise-wide intelligence.
3. **Synchronization** — Create AI-ready people, roles, and teams while redesigning work around AI capabilities.
4. **Stewardship** — Embed and monitor compliant, human-centered, and transparent AI practices by design.

### Case study 1: [[Guardian Life Insurance]]

Three areas of AI use: customer experience, operating efficiency, employee productivity.

- **Strategy** — Data and AI team owns AI strategy and prioritization; value-tracking framework runs initiatives from hypothesis → pilot → scale, kept tied to measurable impact. **Concrete outcome: automated RFP and quoting process — turnaround cut from ~1 week to 24 hours.** Plans to scale in 2026.
- **Systems** — CTO reorganized around products and platforms with small cross-functional teams, microservices, and APIs enabling reuse and faster delivery. Modernized legacy systems and data architecture.
- **Synchronization** — Reskilling the workforce by reorganizing employees into AI-focused roles and emphasizing solving end-to-end business problems. Longer-term plans include rotations and training programs to build hybrid business-technical skills.
- **Stewardship** — Given its regulated environment, embedded governance with risk, legal, and compliance teams. Architecture reviews via both formal and fast-track boards, ensuring privacy, security, and regulatory requirements built into new solutions.

### Case study 2: [[Italgas]]

Europe's largest natural gas distributor. Three areas of AI use: managing infrastructure, boosting efficiency, improving safety. **Digital Factory** is the innovation hub anchoring this work, supported by executive sponsorship and cross-functional teams.

- **Strategy** — Prioritized AI projects:
  - **WorkOnSite** — accelerated construction projects by **40%** and reduced inspections by **80%**
  - **DANA** — a generative AI-based network control system
  - Each MVP sprint backed by a C-level sponsor for strategic alignment
- **Systems** — Italgas has digitized assets and processes since 2017: cloud-based platform, IoT infrastructure, **300-terabyte data platform**, **23 AI models**. Business translators embedded in units to drive adoption and modular component application.
- **Synchronization** — Engaged **>1,000 employees** in innovation initiatives; delivered **30,000 hours of AI/data training in 2024**. Italgas Academy supports a new digital leadership model — building an agile, AI-ready workforce while maintaining continuity.
- **Stewardship** — Governance via a chief people, innovation, and transformation officer + an AI officer + a group AI office overseeing integration and monitoring. Initiatives balance efficiency gains with new business opportunities — e.g., **commercializing WorkOnSite generated €3M revenue in 2024**.

### AI maturity = major organizational change

The researchers emphasize that transitioning through stages of AI maturity represents a **major organizational change**, requiring overcoming both human resistance and technological complexity. Driving change requires **a united front among the CEO, CIO, chief strategy officer, and the head of human resources**.

## Notable quotes

> "Now is the time for executive teams to align, commit, and lead the charge toward enterprise-scale AI by developing a playbook for strategy, systems, synchronization, and stewardship." — Woerner, Weill, Sebastian, Káganer

> "Organizations that are AI mature outperform early-stage AI implementers — but many companies struggle to advance from AI pilots to AI at scale."

## My take

This is a **clean conceptual companion to the [[2026-04-28-ai-index-report-2025|AI Index 2025]]**. Where AI Index gives the macro-empirical landscape (what % of orgs use AI, by how much, with what financial impact), this MIT CISR briefing gives the **micro-organizational mechanism** — the stage transitions and the four kinds of change required to move between stages.

Two specific things worth flagging:

1. **The 7% Stage 4 number rhymes with the AI Index's "1% mature" finding** (different instrument, different sample, different definition — see [[ai-maturity-measurement-comparison]]). Multiple measurements are converging on a thesis: *most organizations using AI are not yet capturing meaningful value at scale.*

2. **The Stewardship pillar is doing more work than it gets credit for.** The Guardian case study shows architecture review boards as the operationalization of [[responsible-ai]] — RAI as a procurement-and-design discipline, not a separate ethics function. This is a more practical framing than the typical "RAI principles" framing in policy literature.

The case studies are valuable as **concrete numbers** I can cite from this point forward:
- Guardian: RFP turnaround **1 week → 24 hours** (28× speedup)
- Italgas: WorkOnSite +40% construction speed, -80% inspections; **300TB data platform, 23 AI models**; 30,000 training hours in 2024; **€3M revenue** from commercializing WorkOnSite

The methodological caveat: the MIT CISR Future Ready Survey is from **2022** (N=721), supplemented by **2024 interviews** at only 9 enterprises. The 2022 survey predates the GenAI explosion. The 28%/34%/31%/7% stage breakdown should be treated as the *2022 baseline* — current distributions may have shifted, especially given how rapidly enterprise GenAI use grew in 2024 ([[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4: GenAI use 33% → 71% in one year).

## Linked entities and concepts

**Entities (this wiki):** [[MIT CISR]], [[Stephanie Woerner]], [[Peter Weill]]. **Dangling (not yet promoted):** [[Ina Sebastian]], [[Evgeny Káganer]], [[Kristin Burnham]] (journalist), [[Guardian Life Insurance]], [[Italgas]], [[IESE Business School]], [[MIT Sloan]].

**Concepts:** [[enterprise-ai-adoption]] (substantially enriched by this source), [[responsible-ai]] (stewardship operationalized), [[generative-ai]] (agentic AI in Stage 4).

**Threads:** [[ai-maturity-measurement-comparison]] (opened by this ingest).

## Source

- **Raw PDF:** [article file](../../raw/articles/How%20to%20boost%20your%20organization%E2%80%99s%20AI%20maturity%20level%20_%20MIT%20Sloan.pdf)
- **Public URL:** mitsloan.mit.edu/ideas-made-to-matter/how-to-boost-your-organizations-ai-maturity-level
- **Underlying research:** MIT CISR 2022 Future Ready Survey (N=721) + 2024 interviews at 9 enterprises
