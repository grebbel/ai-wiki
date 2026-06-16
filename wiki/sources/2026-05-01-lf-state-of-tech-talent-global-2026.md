---
type: source
kind: report
title: "2026 State of Tech Talent Report: Not a jobs crisis, but a skills crisis with an upskilling answer"
author: ["Marco Gerosa", "Adrienn Lawson", "Anna Hermansen"]
publisher: "The Linux Foundation (Linux Foundation Research), foreword by Clyde Seepersad (Linux Foundation Education)"
url: "https://www.linuxfoundation.org/research/state-of-tech-talent-2026"
date_published: 2026-05-01
date_ingested: 2026-06-08
length: "~38 pages (full report incl. executive summary, methodology, demographics, appendix)"
raw: "../../raw/reports/LFTraining_Tech_Talent_Report_Global_2026_webversion_052626.pdf"
tags: [ai-employment-effects, durable-skills, upskilling, tech-talent, skills-gap, net-hiring-effect, certifications, agentic-ai-security, park-stack, institutional-knowledge, linux-foundation, survey, enterprise-ai-adoption]
confidence: 0.75
last_confirmed: "2026-06-08"
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "survey-side complement to the ADP-payroll finding: AI is not reducing aggregate IT demand (net hiring +26%/+31%); only the largest orgs report negative net hiring (-4%)"
    confidence: 0.72
  - type: supports
    target: 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs
    via: "both: AI redefines/expands technical roles rather than eliminating them; redesign entry-level roles + upskilling as the executive response"
    confidence: 0.72
  - type: supports
    target: 2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer
    via: "upskilling existing staff + durable core skills as the answer to the AI-era skills gap"
    confidence: 0.7
---

# 2026 State of Tech Talent Report: Not a jobs crisis, but a skills crisis with an upskilling answer

A **38-page annual survey report** from **Linux Foundation Research** (authors Marco Gerosa of Northern Arizona University; Adrienn Lawson and Anna Hermansen of The Linux Foundation; foreword by Clyde Seepersad, SVP & GM Education). Based on an online survey fielded **February 2026 with 400 participants worldwide** responsible for hiring, training, and managing technical talent. It is the wiki's first **tech-talent-market survey** anchor — a workforce-side complement to the firm-side and economy-side AI-adoption sources, and an empirical counterweight to the "AI is eating IT jobs" narrative.

## TL;DR

- **The headline thesis**: *"Not a jobs crisis, but a skills crisis with an upskilling answer."* AI is **not reducing demand for technical talent** — it is **raising the bar** for what that talent must do. The binding constraint is *operationalising* AI, not accessing it.
- **AI is not eating all IT jobs**: aggregated **net hiring effect +26% (2025), +31% (2026)**; only the **largest organisations** report a negative net effect (**−4%**). 97% plan to implement AI; 55% expect significant value in software development.
- **The skills gap is full-stack, not just AI**: understaffing in **AI (47%), cybersecurity (40%), cost optimization (36%), platform engineering (34%)**; **AI security and AI operations each affect 57%** of organisations. Most orgs lag on **PARK-stack** (foundational AI-infrastructure) implementation.
- **Agentic AI raises serious security risks** and most organisations are not ready; **security concerns (48%) and budget constraints (47%)** are the leading barriers to getting value from new technologies (security/privacy is now the *top* barrier).
- **Upskilling is the answer**: upskilling existing staff (**57%**) is the primary response to talent gaps, ahead of external hiring (49%); rated important by **94%** for closing AI gaps *and preserving institutional knowledge*. Upskilling is favoured over hiring by **7.9× (business context), 7.7× (retention), 7.3× (team cohesion), 5× (lower total cost)**; orgs are **3.5× more likely to upskill than hire** across strategic domains.
- **Talent signals are shifting**: **technical training (93%) ranks above compensation (91%)** as a retention strategy; **76% of hiring managers consider certifications important**; degrees/titles/years-of-experience are "proving insufficient" as roles change faster than those signals.

## What was actually ingested

Full 38-page report (executive summary, four findings sections, conclusion, methodology + demographics, appendix; converted via `pdftotext`). Identity verified against the cover and citation block. Survey: online, Feb 2026, n=400 worldwide. The report's own external anchors include McKinsey *State of AI 2025*, BCG *Where's the Value in AI? Only 5% Are Getting It at Scale*, Deloitte *State of GenAI in the Enterprise*, Bain *Widening Talent Gap*, BCG *AI Transformation Is a Workforce Transformation*, and LinkedIn skills-based-hiring trends.

## Key findings, with detail

### "Not a jobs crisis, but a skills crisis"

The foreword (Seepersad) states the thesis bluntly: *"AI does not appear to be reducing demand for technical talent. It is raising expectations for what that talent must be able to do … The issue is not simply a lack of people. It is a lack of capability — specifically, the ability to apply skills across systems, workflows, and real-world environments."* This is the **workforce-side mirror** of the firm-side [[micro-productivity-trap]] finding (the constraint is operationalisation, not technology) and of [[enterprise-ai-adoption|BCG's 5%-get-value-at-scale]] anchor — the report cites both directly.

### AI is not eating all IT jobs (net hiring is positive)

The +26%/+31% aggregated net hiring effect, with only the largest orgs negative (−4%), is the **survey-side complement** to [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen's]] ADP-payroll evidence. The two are *not* identical: Brynjolfsson et al. find a **compositional** twist (entry-level decline in the most AI-exposed occupations) that the Global report's aggregate doesn't surface — but the Europe sibling report *does* (see [[2026-06-01-lf-state-of-tech-talent-europe-2026|Europe report]], −3% entry-level). Together they qualify the headline: aggregate IT demand rises *and* the junior tier is where the pressure concentrates.

### Upskilling over hiring — and why

The report's distinctive contribution is the **quantified upskilling-vs-hiring preference** (7.9×/7.7×/7.3×/5× across business context, retention, team cohesion, cost) and the framing of upskilling as **institutional-knowledge preservation**, not just gap-closing ("upskilled talent doesn't take wing and fly, they grow roots"). This is the strongest workforce-side evidence in the wiki for the [[durable-skills]] thesis and complements [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean]] on durable core skills.

### Skills-based signals over credentials-of-record

Certifications (important to 76% of hiring managers) and demonstrated, job-relevant skills are displacing degrees/titles/tenure as trust signals — a shift with an obvious interest-alignment caveat (the publisher sells certifications; see source-quality flag).

## Dynamic-capabilities reading (Warner & Wäger)

- **`digital-transforming/improving-digital-maturity`** *(core)* — the entire report is about "identifying digital workforce maturity," "external recruiting of digital natives," and "leveraging digital knowledge inside the firm" (upskilling + institutional-knowledge preservation).
- **`digital-transforming/redesigning-internal-structures`** — organisations "redefining roles in real time and expanding the scope of responsibilities" across software, infrastructure, data, and security.
- **`contextual/internal-barriers`** — skills/capability gaps, security concerns, and budget constraints named as the barriers to getting value from AI.

(Roles inherited from cell defaults: `chro, cdo, cio, ceo`.)

## Linked entities and concepts

**Existing pages (touched or referenced):**

- [[ai-employment-effects]] — heavy: net-hiring evidence; "AI not eating IT jobs"; role redefinition.
- [[durable-skills]] — heavy: upskilling, institutional knowledge, skills-over-credentials.
- [[enterprise-ai-adoption]] — moderate: 97% AI adoption, value-at-scale gap, security as the binding barrier.
- [[automation-vs-augmentation]] — light: roles redefined/expanded (augmentation), not eliminated.
- [[responsible-ai]] — light: agentic-AI security risks and readiness gap.

**New pages created with this ingest:**

- [[The Linux Foundation]] — entity (organization): promoted on cross-source presence (this report + the Europe report + the [[2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications|Headroom talk]] channel).
- [[Marco Gerosa]] — entity (person): lead author of both 2026 State-of-Tech-Talent reports.
- [[Adrienn Lawson]] — entity (person): co-author of both reports (Linux Foundation Research).

**Dangling (single-source mention, deferred):** *Anna Hermansen* (Global-report co-author only), *Clyde Seepersad* (foreword).

## Source-quality flag

- **Strengths**: a real survey (n=400, methodology + demographics disclosed, Data.World access); cross-referenced against independent anchors (McKinsey, BCG, Deloitte, Bain); the wiki's first workforce-side empirical anchor on the AI-and-jobs question; directly corroborates the Brynjolfsson-canaries reading at the aggregate level.
- **Caveats**: **interest alignment** — Linux Foundation *Education* sells training and certifications, so the report's central prescription (upskilling + certifications) aligns with the publisher's commercial interest; self-reported survey (intentions like "97% plan to implement AI" overstate realised deployment); n=400 global is modest for fine-grained breakdowns. Per CLAUDE.md, a vendor-interested survey is held at **≤0.75** unless independent sources agree — several do (Brynjolfsson, BCG, Bain), supporting 0.75.
- **Confidence: 0.75.**

## Open questions for the wiki

- **The PARK stack** (foundational AI infrastructure; Ray/Distributed Computing the lowest-deployed component) is named but not defined here — worth pinning down if a second source uses it.
- **Aggregate-positive but entry-level-negative**: the reconciliation with [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson]] lives in the [[2026-06-01-lf-state-of-tech-talent-europe-2026|Europe report's]] −3% entry-level finding — track whether future LF reports surface the entry-level cut globally.
