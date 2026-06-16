---
type: source
kind: article
title: "The End of One-Size-Fits-All Enterprise Software"
author: ["Deep Nishar", "Nitin Nohria"]
publisher: "Harvard Business Review"
journal_volume: "HBR.org Digital, 23 April 2026"
url: "https://hbr.org/2026/04/the-end-of-one-size-fits-all-enterprise-software"
date_published: 2026-04-23
date_ingested: 2026-05-05
tags: [generative-ai, enterprise-software, SaaS, build-vs-buy, vibe-coding, firm-boundary, make-or-buy, foundation-models, agentic-ai]
length: "~8 pages"
raw: "../../raw/articles/The End of One-Size-Fits-All Enterprise Software.pdf"
---

# Nishar & Nohria — The End of One-Size-Fits-All Enterprise Software

## TL;DR

A practitioner HBR.org Digital article (23 April 2026) co-authored by [[Deep Nishar]] (technologist/investor; ex-Google senior product, ex-LinkedIn CPO) and [[Nitin Nohria]] (HBS professor; 10th Dean of Harvard Business School 2010–2020). Argues that [[generative-ai]] is **dissolving the economic logic that made standardized [[enterprise-ai-adoption|enterprise software]] the default** — and at a much faster pace than the authors themselves predicted in their May 2025 piece (the prior thesis they explicitly correct: "We were wrong — not about the direction, but about the pace").

**Central claim:** the build-vs-buy question is no longer a cost decision. It is a strategic question about **which workflows the firm should own**. Custom software is accessible again because vibe coding plus [[foundation-models]] compress months-of-engineering into days.

**The four-model framework** for the firm-boundary decision under GenAI:

1. **Build** — directly on foundation models, for distinctive jobs (logistics-optimization example).
2. **Compose** — vendor scaffolding configured by business users (Salesforce Headless 360 example).
3. **Collaborate** — forward-deployed engineers from providers build bespoke systems in weeks.
4. **Buy outcomes** — procure the outcome itself, not the tool (Adobe outcome-based pricing for CX Enterprise + agentic AI).

These are **not mutually exclusive** — most organizations will use a combination. The strategic question is which model fits which workflow, given where the firm wants its boundary.

## Empirical anchors

- **Enterprise GenAI app spending: $1.7B (2023) → $37B (2025)** — more than 20× in two years; SaaS took ~10 years for comparable penetration. Source: cited in the article (linked in original).
- **Public SaaS valuations 30–60% below 2021 peaks**.
- **~40% of code is now AI-generated**; vast majority of developers use AI coding tools daily.
- **>1/3 of companies report replacing at least one SaaS tool with a custom-built GenAI alternative**; majority expect to build more in the coming year.
- Some early-adopting mid-market companies report material declines in spending on categories such as project management software even as AI investment surges.
- **Caveat from the article**: most organizations are still experimenting; many AI initiatives fall short of expected returns. Direction is clear; uniform execution is not.

## The four models in detail

### 1. Build

Construct systems directly on top of foundation models, organized around the specific jobs the organization is trying to perform — not around a vendor's workflow conventions.

- **Worked example (article):** a logistics company building a system to continuously optimize delivery time and cost based on its own data; over time becomes a repository of institutional knowledge that's hard to replicate.
- **Tradeoff:** greater control and differentiation in exchange for ongoing technical complexity.
- **Useful check:** does the system encode truly distinctive data or decision logic? If not, *building* is overreaching — *composing* or *collaborating* would deliver similar value with far less complexity.

### 2. Compose

Vendor provides scaffolding, templates, and primitives that business users configure to their needs.

- **Worked example (article):** a sales organization using **Salesforce Headless 360** to tailor lead scoring, outreach sequencing, and pipeline reviews to its own motion — without building a CRM from scratch.
- **Direction reverses:** software adapts to the company, rather than the company adapting to the software.
- **Tradeoff:** lower burden than building from scratch; some constraints remain on how far customization can extend into core functions.
- **Watch for:** signs that critical differentiation is being constrained by the platform's boundaries; when customization "feels forced or cumbersome," consider building or collaborating more deeply.

### 3. Collaborate

Shift from buying enterprise software to collaborating with providers to build tailored solutions. Providers use **forward-deployed engineers** to define the job clearly, then build bespoke systems around the desired outcome.

- **Worked example (article):** specialized team helping a manufacturer redesign procurement and build a system around it in weeks vs. the months/years a traditional ERP deployment plus consulting configuration would require.
- **Tradeoff:** speed and alignment vs. dependence on external expertise.
- **Watch for:** repeated reliance on external partners may mask an opportunity to internalize a strategically important capability — or conversely, the work being done lacks uniqueness and could be bought as an outcome.

### 4. Buy outcomes

The most radical model — purchase the outcome, not the tool. The vendor takes responsibility for results, not for delivering software.

- **Worked example (article):** instead of licensing accounting software and operating it internally, contract for "accurate financials, compliance, and reporting as a service."
- **Industry example named:** **Adobe** announced **outcome-based pricing** for its CX Enterprise suite and agentic AI tools — Adobe deploys its AI agents directly with the customer and charges for outcomes (e.g., number of successful ad campaigns completed by its AI agents) rather than per seat or per AI token.
- **Tradeoff:** simplifies operations but shifts control and requires high trust in the provider.
- **When it works best:** when the outcome is **non-differentiating**. If performance in that domain begins to shape competitive advantage, firms should reclaim control by building, composing, or collaborating.

## The strategic question this forces

> "When any function can be deeply customized, or handed to an external provider to deliver as an outcome, every organization faces a strategic choice it has not had to confront in a generation: Which jobs do we truly want to own?"

Under the prior bargain (custom software prohibitively expensive), the make-or-buy question was effectively settled by default — companies ran their own payroll, customer support, demand forecasting because the available tools required them to, not because these were sources of differentiation. **Standardized systems made one company's implementation look much like another's.**

The article's reframing: **the boundary of the firm becomes a variable rather than a given.**

This also changes the nature of advantage:

> "In a world where systems can be replicated quickly, advantages built solely on process or embedded logic are more contestable. What remains defensible is a clear understanding of which jobs are truly distinctive to how a company creates value, and the discipline to build depth in those areas rather than spreading effort across everything."

## Practical constraint: speed vs. discipline

A subtle but important warning the article flags from early adopters:

> "Moving quickly is not the same as moving effectively. Organizations that rush to automate without re-architecting their data and processes often find that quality suffers, edge cases accumulate, and systems become difficult to manage. The lesson is not to slow down, but to pair ambition with discipline: to treat data architecture, governance, and ownership as integral to the transformation rather than afterthoughts."

This directly **reinforces the [[micro-productivity-trap]] framing** from [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt, Chatterji et al.]] — both pieces converge on "process redesign / data architecture is the load-bearing decision, not the technology."

## Four practical decisions for leaders

The article closes with four leader-level practices:

1. **Treat data architecture as the foundation.** Fragmented, vendor-managed data limits what AI systems can do.
2. **Revisit the build-vs-buy decision per function.** The relevant question shifts from "can it be built?" to "*should* it be built? Where does building create meaningful differentiation?"
3. **Establish clear governance for internally developed systems.** As more software is created outside traditional IT structures, security, maintainability, and accountability move from peripheral to central — see [[responsible-ai]].
4. **Recognize software choices are workforce choices.** When AI performs work previously done by teams, technology decisions are organizational-design decisions — see [[automation-vs-augmentation]] and [[ai-employment-effects]].

## What's NOT being claimed

The article carefully *doesn't* declare the end of SaaS:

> "It would be a mistake to declare the end of SaaS. Many applications will persist, and some vendors will adapt successfully by moving toward more flexible, outcome-oriented models. The transition will unfold unevenly across industries and functions."

The underlying logic, not the SaaS market, is what's changed.

## Cross-source positioning (descriptive only)

This article enters the wiki's [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] cluster as a **7th named framework**, operating at a **decision layer not previously surfaced** by the synthesis page's six frameworks: the **firm-boundary / make-or-buy layer**. The synthesis (filed 2026-05-05) maps six frameworks onto seven layers (org-design / readiness / capability progression / transformation playbook / trap escape / task deployment / diagnostic). Nishar-Nohria adds an 8th layer.

Direct support relationships:
- **Reinforces [[micro-productivity-trap]]** — both Nishar-Nohria and Dutt-Chatterji name "process redesign first, technology second" as load-bearing.
- **Reinforces the McKinsey *Rewired* and Bain/OpenAI insistence on senior-leader ownership** — Nishar-Nohria's "data architecture as foundation" maps onto Rewired's data capability and Bain/OpenAI's "boardroom imperative."
- **Empirically supports [[generative-ai]]** — the $37B / 40%-AI-code / SaaS-valuation-compression numbers add data points to the GenAI-as-substrate story.

## Authorial vantage and source-quality flag

- **Deep Nishar** is an investor with positions in **Anthropic, Figma, Glean, and Slack** (per his author bio). His investments include companies that benefit from the framework he's prescribing (e.g., [[Anthropic]] sells foundation-model API access that "Build" relies on; Slack is a SaaS the article implicitly says is *not* threatened). Read with that vantage in mind: the article is *prescriptive* and *practitioner-oriented*, not empirical research. Its data points (>1/3 of companies replacing SaaS, etc.) are cited via embedded links in the original — those links should be followed if the data points become load-bearing for any wiki claim.
- **Nitin Nohria** is the academic anchor — long-tenured HBS dean and professor. His co-authorship lends gravitas and reduces (without eliminating) the vendor-of-deployment slant.
- **Treat as: HBR.org Digital practitioner article**, not peer-reviewed research. Confidence boost from this source is +0.05 per the [§Lifecycle](../../CLAUDE.md#lifecycle) "additional supporting source" rule, with no peer-review bonus.

## Linked entities and concepts

**Entities (this wiki):** [[Deep Nishar]] *(new)*, [[Nitin Nohria]] *(new)*, [[Harvard Business Review]] (publisher), [[Anthropic]] (Nishar investment), [[Harvard Business School]] *(dangling — Nohria's institutional home)*. **Dangling** (single-source mentions, deferred): Salesforce / Salesforce Headless 360, SAP, Workday, Epic, Cursor, Replit Agent, OpenAI Codex, Adobe.

**Concepts:** [[enterprise-ai-adoption]] (firm-boundary lens enrichment — heavy), [[micro-productivity-trap]] (data-architecture-as-foundation reinforcement), [[generative-ai]] ($37B / 40% AI code / vibe coding), [[automation-vs-augmentation]] (Buy Outcomes as the most automative model), [[foundation-models]] (substrate for the Build model).

**Threads/syntheses:** [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] (this article is a 7th framework at a new firm-boundary layer; flagged as an open question in the synthesis's "post-closure" set).

## Source

- **Raw PDF (~8 pages):** [article file](../../raw/articles/The%20End%20of%20One-Size-Fits-All%20Enterprise%20Software.pdf)
- **Publisher:** Harvard Business Review
- **Section:** Enterprise Computing
- **Date:** April 23, 2026
- **Authors:** Deep Nishar, Nitin Nohria
