---
type: source
kind: article
title: "How to Move from AI Experimentation to AI Transformation"
author: ["Arjun Dutt", "Gene Rapoport", "Aaron \"Ronnie\" Chatterji", "Gawesha Weeratunga", "Harrison Satcher"]
publisher: "Harvard Business Review"
journal_volume: "HBR.org Digital, 30 April 2026"
url: "https://hbr.org/2026/04/how-to-move-from-ai-experimentation-to-ai-transformation"
date_published: 2026-04-30
date_ingested: 2026-05-02
tags: [generative-ai, AI-transformation, micro-productivity-trap, EBITDA, lowes, openai, bain, chatterji, dutt, process-redesign, evals]
length: "~10 pages"
raw: "../../raw/articles/How to Move from AI Experimentation to AI Transformation.pdf"
---

# Dutt, Rapoport, Chatterji, Weeratunga & Satcher — How to Move from AI Experimentation to AI Transformation

## TL;DR

A practitioner-oriented HBR article (30 April 2026) co-authored by [[Bain & Company]] partners ([[Arjun Dutt]], [[Gene Rapoport]]) and [[OpenAI]]'s Economic Research team ([[Aaron Chatterji]] — Chief Economist; [[Gawesha Weeratunga]]; [[Harrison Satcher]]). Combines Bain's enterprise-AI-deployment book with OpenAI's vantage point as a provider to "over one million businesses."

**Core diagnostic**: most firms get stuck in a **"micro-productivity trap"** — treating AI as plug-and-play SaaS with isolated use cases. Individual task gains do not translate to firm-level results because the surrounding workflow still depends on tacit knowledge, manual handoffs, or legacy systems.

**Two failure modes**:
- **Offering lock-in** — using AI to optimize *existing* offerings.
- **Process lock-in** — using AI to automate *current* processes without rethinking them.

**Successful firms instead "reinvent the business"**: organization-wide, future-focused, outcome-oriented. **Bain client EBITDA gains: 10–25%** for transformation-mindset deployments.

**Four-step framework** (with worked cases at **[[Lowe's]]** + OpenAI partnership and a Fortune-1000 manufacturer the authors call **FabricationCo**):
1. Narrow possibilities strategically (4–5 critical domains)
2. Reimagine workflows across the organization
3. Engage those closest to today's process
4. Measure what matters (concrete business outcomes, not "efficiency" — and continuous **evals** for AI behaviour)

## Key claims

### The micro-productivity trap

> "Individuals often realize productivity gains on key tasks, but those gains often stall at the firm level when the surrounding workflow still depends on tacit knowledge, manual handoffs, or legacy systems not built for AI. AI can accelerate a task, but unless companies address workflow bottlenecks, productivity gains may not translate into business value."

Two named lock-ins, often co-occurring:

| Lock-in | What it looks like |
|---|---|
| **Offering lock-in** | AI applied to optimize the *existing* product/service rather than reframe what value the firm provides |
| **Process lock-in** | AI applied to automate *current* processes step-by-step rather than rebuild around an outcome |

The opposite posture — what the article calls the AI-transformation mindset — explicitly assumes "we live in a world in which powerful AI tools exist" and rebuilds workflows on that premise.

### Four steps

#### 1. Narrow possibilities strategically

- Resist the urge to deploy AI everywhere; identify **4 or 5 critical domains**.
- Top-4 domains across Bain's client work and decision-maker feedback: **software development, customer support, knowledge worker efficiency, marketing**. (Industry-specific selection still required.)
- Diagnostic questions:
  - Which parts of the business will benefit most today *and* tomorrow (assuming continued capability progress)?
  - Where is the highest concentration of resources doing repeatable work?
  - What are high-value, low-effort use cases (often where workers are bottlenecked)?
  - Buy vs build? In-house vs partner?

**FabricationCo case**: week-long cross-functional workshop with frontline operators + managers across divisions. Mapped end-to-end workflows for both customer and internal roles. Surfaced **14 discrete AI use cases** with tens of millions in aggregate potential value. Now on track to realize **~$30M in additional profit**.

**Lowe's case**: prioritization framework based on technology maturity, use-case size, readiness for change, and **dimensional risk** (including brand risk). Vision settled on as "democratizing expertise across the organization" — operationalized as two AI interfaces launched March 2025: **Mylow** (online customers) and **Mylow Companion** (in-store associates).

> "How customers shop with us, how we sell, how we work" — Lowe's broader framework, per [[Chandhu Nair]] (SVP of stores, data, AI, and innovation).

#### 2. Reimagine workflows across the organization

> "It's the process redesign — not the technology — that is the most challenging part of AI deployment for firms, and also creates most of the value."

Key argument: many seemingly department-specific work products are actually cross-functional. At FabricationCo, "even seemingly straightforward activities like quoting customer jobs required coordination across sales, design, and operational teams" — making them **prime candidates for reinvention rather than incremental automation**.

Selection questions:
- Where is the highest value (time, effort, usage)?
- Which processes are most ready (repeatability, data quality, technology)?
- Where is variation across business units highest?

**FabricationCo quoting workflow** (worked example):
- Old: design engineers spent several hours producing initial designs as input for *every* bid quote — including bids unlikely to convert (>50% in some segments).
- New: 20-minute cost estimates by *non-designers* for early-stage bids; full engineered designs reserved for higher-probability opportunities.
- Result: **~15× faster quote generation**; reduced wasted effort; improved win rates.

#### 3. Engage those closest to today's process

- Successful transformations engage **both top-down and bottom-up** perspectives.
- Cross-seniority collaboration between leaders close to the work *and* outstanding individual contributors who can re-envision the process.
- **Prototyping culture** in *all* areas (not just the tech team) — hackathons, micro-sprints. Even simple wireframes can convert sceptical/anxious team members.

**FabricationCo**: pilot regions chosen for strategic importance + first-mover willingness; visible successes in pilots generated confidence in not-yet-deployed regions; demos and feedback sessions extended to non-pilot regions to enable **fast cross-region scaling**.

**Lowe's Mylow Companion**: targeted store pilots starting in 1–2 departments per store (e.g. plumbing or electrical) with in-app and on-floor feedback loops to refine prompts, AI guardrails, UX. Iterative expansion across departments and stores. **Now fully deployed across 1,700+ Lowe's stores.**

#### 4. Measure what matters

> "'Efficiency' or 'productivity' are too vague; instead, those benefits should be tied to key business outcomes, with metrics that allow for comparisons with non-AI methods."

Two measurement layers:

1. **Business-outcome metrics** — comparable to non-AI baselines.
2. **Evals** (continuous evaluation suites) — AI systems "like humans, can produce different results from the same request"; require sustained measurement against a tolerance range.

**FabricationCo metrics**:
- Win rates (AI-generated quotes vs non-AI)
- Quote turnaround time
- Margins on downstream material/factory costs
- Volume + accuracy of priced bids
- Result: **+10 percentage-point increase in win rate within 3 months** of deployment.

**Lowe's evals approach**:
- SMEs created prompt + expert-validated response sets ("how Mylow Companion *should* reply").
- Evaluated multiple models against the validated set; iterated prompting.
- Associates regularly audit both outputs *and* the system's intermediate steps.

**Lowe's outcome metrics**:
- Drivers of business results: basket size, conversion rate, incremental sales.
- Drivers of success: associate knowledge, customer satisfaction, ease of check-out.
- Result: **conversion rate more than doubles** when customers engage Mylow online; **customer satisfaction +200 basis points** when associates use Mylow Companion.

### The boardroom imperative

> "AI transformation must be prioritized at the very top levels of the company, with all executives and functions participating, because leaders who have an organization-wide view are critical to transformative deployments."

Failure pattern in lagging firms: leaders recognize AI as important but **delegate** it to technology groups/divisions without specific goals or metrics, just vague "improve productivity" or "focus on high-potential sources of value." From that delegation, initiatives often fail.

## Headline numbers

| Metric | Value |
|---|---|
| Bain client EBITDA gains (transformation mindset) | **10–25%** |
| FabricationCo additional profit (on track) | **~$30M** |
| FabricationCo quote-generation speedup | **~15×** |
| FabricationCo win-rate increase (3 months) | **+10 pp** |
| Lowe's Mylow Companion deployment | **1,700+ stores** |
| Lowe's Mylow online conversion rate | **>2× (more than doubles)** |
| Lowe's Mylow Companion CSAT lift | **+200 basis points** |

## Methodology notes

- Practitioner-oriented HBR Generative AI piece; not an empirical study.
- Author vantages: Bain enterprise-AI-deployment work + OpenAI's view as a provider to >1M businesses + Duke business / public-policy academic perspective ([[Aaron Chatterji]]).
- Two case studies: **Lowe's** (named, with public OpenAI partnership) and **FabricationCo** (anonymized Fortune 1000 manufacturer, Bain client).
- Acknowledgements: Bain's Mike Coxon and Daan Kakebeeke contributed to writing.

## Quotes worth saving

> "AI can accelerate a task, but unless companies address workflow bottlenecks, productivity gains may not translate into business value."

> "It's the process redesign — not the technology — that is the most challenging part of AI deployment for firms, and also creates most of the value."

> "[Successful firms] take an outcome-oriented approach, centering on what outcomes those processes serve and rebuilding their workflows starting from the premise that we live in a world in which powerful AI tools exist."

> "Going from lagging to leading requires that companies avoid siloed initiatives and enable instead a more wholesale transformation of their business."

## Related in this wiki

- [[micro-productivity-trap]] — concept page anchored on this source
- [[Arjun Dutt]], [[Gene Rapoport]], [[Aaron Chatterji]], [[Gawesha Weeratunga]], [[Harrison Satcher]] — author entities
- [[Bain & Company]] — co-publishing partner
- [[OpenAI]] — co-publishing partner; vantage as provider to >1M businesses
- [[Lowe's]] — case study (Mylow / Mylow Companion); OpenAI partnership
- [[automation-vs-augmentation]] — "process lock-in" maps to automation-without-redesign; "reinvent the business" maps to outcome-oriented augmentation
- [[enterprise-ai-adoption]] — adds a 4-step framework alongside Anand-Wu's 2×2, MIT CISR's Four Stages, MITTRI/Cisco's 5 Foundations, and Werner-Le-Brun's Octopus/Tin-Man
- [[generative-ai]] — adds field evidence (Bain client EBITDA 10–25%; Lowe's 2× conversion; FabricationCo +10pp win rate)
- [[ai-employment-effects]] — process-redesign framing has implications for what stays / changes within retained jobs
- [[2026-04-28-anand-wu-genai-playbook]] — adjacent strategy framework (cost-of-errors × type-of-knowledge 2×2)
- [[2026-04-28-werner-lebrun-octopus-organization]] — adjacent: octopus orgs ≈ "reinvent the business"; tin-man orgs ≈ stuck in offering/process lock-in
- [[2026-04-28-mit-sloan-ai-maturity]] — adjacent: Stage 4 firms have moved past the micro-productivity trap; Four S challenges (Strategy, Systems, Synchronization, Stewardship) overlap the boardroom-imperative argument
- [[2026-04-28-mittri-cisco-ai-enabled-enterprise]] — adjacent: chatbot → agent → multi-agent progression sits within the workflow-reimagination step
- [[2026-04-28-bansal-birkinshaw-systems-thinking]] — adjacent: cross-functional workflow redesign is systems-thinking applied to AI
- [[2026-04-28-anthropic-economic-index-q4-2025]] — Anthropic's parallel measurement initiative; OpenAI Economic Research team here is a counterpart vantage
- [[2026-04-30-ai-index-report-2026]] — context: 88% organizational AI adoption but AI agent deployment in single digits per function — the gap this article tries to address
