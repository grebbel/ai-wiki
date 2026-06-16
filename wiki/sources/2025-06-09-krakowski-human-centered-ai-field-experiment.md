---
type: source
kind: paper
title: "Human-Centered Artificial Intelligence: A Field Experiment"
author: ["Sebastian Krakowski", "Darek Haftor", "Johannes Luger", "Natallia Pashkevich", "Sebastian Raisch"]
publisher: "INFORMS"
journal_volume: "Management Science 72(1):57-72"
peer_reviewed: true
doi: "10.1287/mnsc.2022.03849"
url: "https://doi.org/10.1287/mnsc.2022.03849"
date_published: 2025-06-09
date_ingested: 2026-05-25
length: "~17 pages, full ingest"
raw: "../../raw/papers/krakowski-et-al-2025-human-centered-artificial-intelligence-a-field-experiment.pdf"
tags: [krakowski, raisch, management-science, field-experiment, dif-in-dif, did, augmentation, untailored-augmentation-negative-effect, kirton-kai, adaptive-innovative-cognitive-style, pharmaceutical-sales, nordic-pharma, work-procedure, decision-authority, training, incentives, cognitive-styles, human-centered-ai, augmentation-as-contingent, learning-effects-in-ai-interaction, prison-quote]
dynamic_capabilities:
  - digital-seizing/strategic-agility
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/organizational-culture
  - contextual/internal-enablers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work
    via: "**Two-field-experiment pair on the augmentation pole — one shows the success case, one shows the failure case.** Brynjolfsson-Li-Raymond (QJE 2025, customer-support AI deployed in a real call center): augmentation under deliberate human-in-the-loop design produces **+15% productivity** with strong equalizing effect (low-skill +30%, high-skill ~0% with small quality decline). Krakowski et al. (Management Science 2025, AI sales-support system in Nordic pharma): **untailored augmentation produces NEGATIVE performance effects vs the legacy IT control**, while tailored interaction (aligned to sales experts' cognitive styles per Kirton 1976) produces positive effects vs both untailored and control. The two papers together complete the augmentation-pole evidence base: *augmentation can produce +15% or it can produce negative outcomes, depending on the interaction-design discipline applied*. Brynjolfsson-Li-Raymond's deployment was *explicitly designed to augment* (agents have full discretion to accept/edit/ignore suggestions; system declines to suggest when training is insufficient) — i.e. *tailored* in Krakowski's vocabulary. Krakowski supplies the empirical evidence that *without that design discipline, the same augmentation technology turns negative*. The two-source convergence sharpens the [[automation-vs-augmentation]] cut: **augmentation is contingent on interaction-design, not guaranteed by deployment choice**."
    confidence: 0.85
  - type: supports
    target: 2026-04-28-dellacqua-jagged-technological-frontier
    via: "**Same-journal-family + same-method + same outside-the-frontier-loses pattern.** Dell'Acqua et al. (Organization Science / INFORMS, 758-BCG-consultant RCT): within-the-frontier +12% tasks / +25% speed / +40% quality; outside-the-frontier ~19pp accuracy loss with subjective coherence persisting through it. Krakowski et al. (Management Science / INFORMS, 72-sales-experts DiD): tailored interaction = positive; untailored interaction = negative vs control. Both papers operate on the *bounded/contingent-positivity-of-augmentation* thesis: when AI is deployed within its zone of fit (within-the-frontier / tailored-to-cognitive-style), positive effects materialise; when deployed outside (outside-the-frontier / untailored), the *same technology* produces *worse outcomes than the legacy baseline*. The Dell'Acqua bounded-region is task-shape; the Krakowski bounded-region is interaction-design — two different *dimensions* of the same underlying contingency phenomenon. Both papers also document **subjective experience that diverges from objective performance** (Dell'Acqua: confidence persists through accuracy loss; Krakowski: the Finnish adaptor's *'felt like in prison'* quote despite the system being *'great'*)."
    confidence: 0.8
  - type: supports
    target: 2026-04-28-anand-wu-genai-playbook
    via: "**Deployment-quadrant frame + interaction-design frame as complementary layers.** Anand-Wu (HBR 2025): the 2×2 task-quadrant deployment framework (cost-of-errors × type-of-knowledge → no-regrets / creative-catalyst / quality-control / human-first zones) prescribes **WHERE** to deploy AI. Krakowski et al.: within a chosen deployment, the **HOW** of human-AI interaction design (work procedure / decision authority / training / incentives, tailored to cognitive style) determines whether the deployment produces positive or negative outcomes. The two frames stack: Anand-Wu's quadrant chooses the deployment zone; Krakowski's parameters tune the interaction within that zone. *Without* Krakowski's interaction tuning, even a correctly-zoned Anand-Wu deployment can produce negative outcomes — pharmaceutical sales is a *quality-control quadrant* task (high cost of errors, partly tacit knowledge) where Anand-Wu would prescribe augmentation; Krakowski shows that augmentation alone is insufficient without interaction tailoring."
    confidence: 0.7
  - type: supports
    target: 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees
    via: "**Two 2026 RCT-grade empirical sources on the *organisational-design dimension* of AI deployment outcomes — published 11 months apart.** Krakowski et al. (Management Science, online June 2025): N=72 Nordic pharma sales experts DiD, four interaction parameters (work procedure / decision authority / training / incentives) × two cognitive styles (adaptor / innovator) → tailored = positive, untailored = negative vs legacy IT. Kropp et al. (HBR / BCG Henderson Institute, May 2026): N=1,261 HR/finance managers randomised experiment, AI-tool vs AI-employee framing → AI-employee framing causes 9pp accountability drop, 44% more escalation, 18% fewer errors caught. Both papers test **organisational design choices** as causal variables in AI-deployment outcomes (Krakowski: interaction-context parameters; Kropp et al.: framing/anthropomorphizing) and find that **apparently-administrative choices materially change performance and accountability outcomes**. Both papers prescribe explicit interaction-design over default deployment as the operative lever. Two-source convergence at advisor-altitude (BCG Henderson Institute) and academic-altitude (Management Science) on the same underlying claim."
    confidence: 0.8
  - type: supports
    target: 2026-04-28-warner-wager-dynamic-capabilities-digital-transformation
    via: "**Empirical operationalisation of *redesigning-internal-structures* + *improving-digital-maturity* microfoundations in a regulated industry.** Where Warner & Wäger frame structural redesign and digital-maturity-improvement as theoretical microfoundations of *digital-transforming* capability, Krakowski et al. supply a concrete RCT-grade empirical instance: untailored structural redesign (D2 — imposed work procedures, constrained decision authority, mandatory training, extrinsic incentives) produces *negative performance* vs the legacy IT control; tailored structural redesign (D3 — parameters aligned to sales experts' cognitive styles) produces positive performance vs both. **The structural redesign microfoundation is the lever** — but it is contingent on tailoring, not deployment alone. The case study sits in the regulated pharmaceutical-sales context — a complement to the W&W 27-senior-executive-interview methodology with a DiD field experiment in a similarly high-regulation setting."
    confidence: 0.7
  - type: supports
    target: 2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer
    via: "**Productive-struggle + cognitive-style-tailoring convergence at developer + sales-expert altitudes.** Forsgren & Macvean (Google DORA 2026): *productive struggle* — engineering-leadership countermeasure where humans deliberately work through complexity rather than offloading it to AI. Krakowski et al.: *tailored human-AI interaction* — sales experts whose interaction context aligns with their cognitive style increase utilization, learning, and performance over time. Both prescribe **interaction-design rather than tool-deployment as the operative lever**, at developer-tool altitude (DORA) and sales-rep altitude (Krakowski). The cross-domain convergence: *AI augmentation is a design discipline, not a deployment decision*."
    confidence: 0.65
confidence: 0.85
last_confirmed: "2026-05-25"
---

# Human-Centered Artificial Intelligence: A Field Experiment

> Humans and artificial intelligence (AI) algorithms increasingly interact on unstructured managerial tasks. We propose that tailoring this human-AI interaction to align with individuals' cognitive preferences is essential for enhancing performance. This hypothesis is examined through a field experiment in a multinational pharmaceutical firm. In the experiment, we manipulated four contextual parameters of human-AI interaction — work procedures, decision-making authority, training, and incentives — to align with sales experts' cognitive styles, categorized as either adaptors or innovators. Our results show that tailored interaction significantly improves sales performance, whereas untailored interaction results in negative treatment effects compared with both the tailored and control conditions. Qualitative evidence suggests that this negative outcome arises from role conflicts and ambiguities in untailored interaction. Exploring the mechanisms underlying these outcomes further, a mediation analysis of AI login data reveals that human-AI interaction tailoring leads sales experts to adjust their AI utilization, which contributes to the observed performance outcomes. These findings support a human-centered approach to AI that prioritizes individuals' information-processing needs and tailors their interaction with AI accordingly.

(Abstract.)

A peer-reviewed academic field experiment published in **Management Science 72(1):57-72** (the INFORMS flagship operations-research / management-science journal, accepted in the *Special Issue on the Human-Algorithm Connection* edited by Catherine Tucker). **Online first 9 June 2025; print volume 72(1) appearing in the 2026 issue.** Submitted Dec 8 2022; revised three times across 2024–early 2025; accepted March 13 2025; CC BY-NC-ND open access.

**Authors**: **Sebastian Krakowski** (Stockholm School of Economics, House of Innovation; corresponding author), **Darek Haftor** (Uppsala University, Department of Informatics and Media), **Johannes Luger** (University of Zurich, Department of Business Administration), **Natallia Pashkevich** (Södertörn University, School of Social Sciences), **Sebastian Raisch** (University of Geneva, Geneva School of Economics and Management). Funded by Erling Persson Family Foundation, Schweizerischer Nationalfonds, and the Jan Wallanders och Tom Hedelius Stiftelse.

**Authors / dangling list.** First wiki source by all five authors; per the [[../../CLAUDE|author-entity promotion rule]] (second-source promotion), they all go on the dangling list at this ingest:

- **Dangling** (single-source mention, deferred): Sebastian Krakowski (Stockholm School of Economics, corresponding author; co-author of *Raisch & Krakowski 2021* on AI augmentation — cited self-referentially in the paper as the theoretical prior), Darek Haftor (Uppsala), Johannes Luger (University of Zurich), Natallia Pashkevich (Södertörn University), Sebastian Raisch (University of Geneva).

## TL;DR

Six substantive contributions warrant ingest:

1. **The wiki's first RCT-grade DiD field experiment showing that *untailored* augmentation produces *negative* performance vs the legacy IT control.** N=72 sales experts across 12 business units in the four Nordic subsidiaries (Denmark / Finland / Norway / Sweden) of a multinational pharmaceutical firm. Three conditions: D1 (control, legacy IT), D2 (untailored AI), D3 (tailored AI per the sales expert's cognitive style). 9 quarters pre-intervention + post-intervention period. **The headline finding is unintuitive and important: deploying the AI system *without* tailoring the interaction to individual cognitive style produces a *gradual decline in market share* relative to a stable legacy-IT baseline.** This is the wiki's strongest single-paper empirical anchor for the claim that **augmentation is contingent on interaction-design, not guaranteed by deployment choice**.

2. **The four parameters of human-AI interaction design** that the study manipulates: **(1) work procedure** (imposed, predefined process vs flexible self-management); **(2) decision-making authority** (constrained vs high); **(3) training** (mandatory vs on-demand); **(4) incentives** (extrinsic / monetary vs intrinsic). These four parameters are tailored to adaptors (well-defined procedures + constrained authority + mandatory training + extrinsic incentives) or to innovators (flexible procedures + high authority + on-demand training + intrinsic incentives) in the D3 condition. The wiki's first **operational vocabulary for interaction-design parameters** in enterprise AI deployment.

3. **The empirical anchor for the Kirton 1976 *adaptive-innovative* cognitive-style framework** (KAI Index, 32-item Likert) in human-AI interaction. Sample distribution: **47 adaptors, 25 innovators** — innovators underrepresented vs theoretical population mean (sample mean KAI = 91.92, theoretical mean = 96). The under-representation aligns with the highly technical and regulated pharmaceutical industry favouring precision over creativity. The KAI cut allows the study to examine *interaction-style heterogeneity* as a moderator of AI-deployment outcomes — a moderator the wiki has not previously had a concrete empirical handle on.

4. **The *work procedure* parameter as the single most impactful lever** — the paper's most actionable finding. Although only one parameter was misaligned for adaptors in D2 (work procedure) while three of four were misaligned for innovators in D2, *most of the negative treatment effect in D2 originates from adaptors* (Table 4). The paper's interpretation: *"Work procedure emerged as the most critical parameter, shaping daily operational interactions."* For practitioners, this elevates **work-process redesign over training, authority, or incentive redesign** as the lever to get right first when designing human-AI interaction.

5. **The *prison quote* — qualitative evidence on the mechanism of untailored augmentation.** A Danish innovator in D2 described it as: *"The whole work situation was in a way paradoxical. We got this super tool, and at the same time, I felt like in prison. There was no freedom to work the way I wanted to work. (…) I wanted to work more spontaneously and in an improvised way to deal with each situation. This level of controlling killed my internal drive!"* A Norwegian innovator: *"The IT system was great, it had much more valuable information. However, I wanted to use it in my own way. The whole change made me lose my belief that I could reach the high sales objectives set for me. In a way, after the change, I felt like a less good sales representative, because of that prison-like context."* The Swedish adaptor in D3 contrasts: *"I think I did more than double as much relevant work after the change."* The qualitative evidence reveals the *role-conflict + ambiguity* mechanism behind the negative quantitative outcome — an internal-motivation collapse rather than a tool-quality problem.

6. **The login-data mediation analysis** as the operational mechanism. AI-system utilization in D2 *decreased gradually* post-intervention as sales experts withdrew from the system; utilization in D3 *gradually increased*, indicating learning. The paper's argument: *"AI system utilization — rather than the work parameters, which remained constant throughout the post-intervention period — is the primary driver of our results."* Tailored interaction → higher utilization → higher learning → higher performance. The mechanism is *not* algorithm aversion (Dietvorst et al. 2018) but rational adaptation to a system that doesn't suit the user's cognitive style.

## What was actually ingested

Full 17-page paper including abstract, theoretical framing (cognitive styles + four-parameter prior work), empirical context (Nordic pharma, sales meetings as performance proxy), model specification (DiD with individual / year / quarter fixed effects, post-intervention indicator, D2/D3 dummies, observable controls including KAI score), results (with the headline tailored-vs-untailored-vs-control comparison), qualitative interview evidence, login-data mediation analysis, discussion, and contributions to the literature. Online Appendix sub-analyses (by country, by product, by KAI quartile, with lagged units-sold outcomes) are cited but not extracted — the main paper's claims rest on the central DiD analysis.

## The empirical design

| Element | Detail |
|---|---|
| **Setting** | Four Nordic subsidiaries (Denmark, Finland, Norway, Sweden) of a multinational pharmaceutical company. Sales experts visit prescribers (medical doctors) with drug information; meetings are highly idiosyncratic and the proxy for anticipated sales. |
| **Sample** | **N = 72 sales experts across 12 business units**. Balanced on gender, age, education, work experience; KAI cognitive-style measured pre-intervention. |
| **Cognitive-style measurement** | Kirton 1976 KAI Index — 32-item Likert questionnaire. Cutoff at the theoretical mean (96): below = adaptor (47 experts); above = innovator (25 experts). |
| **Treatment design** | D1 = control (legacy IT system, basic information repository). D2 = untailored AI interaction. D3 = tailored AI interaction (four parameters aligned to each sales expert's cognitive style). **The AI system itself is identical across D2 and D3** — only the four interaction-design parameters differ. |
| **Tailored parameters (D3)** | For adaptors: imposed work procedure + constrained decision authority + mandatory training + extrinsic incentives. For innovators: flexible work procedure + high decision authority + on-demand training + intrinsic incentives. |
| **Performance outcomes** | Primary: average daily number of client meetings per quarter (successful-meetings proxy). Secondary: average daily product units sold (lagged 2/4/6/8 quarters for the public-sector procurement delay). |
| **Identification** | DiD with individual / year / quarter fixed effects. 9 quarters of pre-intervention data confirm common-trends assumption (Online Appendix F1). Random allocation of business units to conditions. Multiple sensitivity analyses confirm robustness; authors caution against strong causal interpretation due to small-cluster power constraints. |

## The headline results

1. **D2 (untailored AI) negatively impacts performance vs D1 (legacy IT control)** — *contrary to expectations*. Market share gradually *declines* post-intervention in D2.
2. **D3 (tailored AI) yields positive performance effects vs both D2 and D1.** Market share gradually *increases* in D3.
3. **Most of the D2 negative effect originates from adaptors** — surprising because only one parameter (work procedure) was misaligned for adaptors in D2 (the other three were aligned with adaptor preferences). The paper concludes work procedure is the most critical parameter shaping daily interactions.
4. **Learning effects in D3**: sales experts gradually increased AI utilization and improved performance over time, with mediation evidence that utilization is the primary driver of the performance result.
5. **No evidence of algorithm aversion in D3** — the disengagement in D2 reflects rational adaptation to a poor-fit interaction context, not systematic anti-AI bias. This adds to the debate between [algorithm aversion (Dietvorst et al. 2018)](Dietvorst) vs [algorithm appreciation (Logg et al. 2019)](Logg) by *resolving it via the interaction-design contingency*: aversion happens when interaction is misfit; appreciation happens when interaction is fit.

## Substantive contributions to the wiki

**To [[automation-vs-augmentation]]:** the paper supplies the wiki's strongest single empirical anchor for **the contingent-positivity-of-augmentation claim**. Augmentation does not automatically produce positive outcomes — the *same technology* deployed with untailored interaction produces *worse outcomes than the legacy baseline*. Pairs with [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson-Li-Raymond]]'s success case (+15% productivity under deliberately augmentative design) and [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua's]] frontier-bounded case (within = positive, outside = negative) to complete the wiki's augmentation-pole evidence base.

**To [[enterprise-ai-adoption]]:** adds the **four-parameter interaction-design vocabulary** (work procedure / decision authority / training / incentives) as a complement to deployment-side frameworks like [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's 2×2]] and stage-side frameworks like [[2026-04-28-mit-sloan-ai-maturity|MIT CISR Four Stages]]. Adds the **negative-market-share-trajectory worked example** under untailored deployment.

**To [[micro-productivity-trap]]:** the *untailored augmentation produces negative market-share* finding is the wiki's first **strictly-academic empirical anchor** on the trap. The mechanism named by qualitative interview evidence — role conflicts and ambiguities collapsing internal motivation, leading sales experts to withdraw from the system — is structurally a fourth named sub-mode alongside [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al.'s]] *offering-lock-in* / *process-lock-in* and [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al.'s]] *anthropomorphizing-lock-in*: **interaction-design-misfit lock-in**.

**To [[ai-employment-effects]]:** the paper's mechanism is *worker withdrawal* rather than *worker displacement*. The Finnish/Norwegian innovator quotes (*"made me lose my belief that I could reach the high sales objectives"* / *"felt like a less good sales representative"*) name a labour-market consequence not directly captured by employment-statistics analyses — *self-perception decay under poor-fit augmentation*. Open empirical question: does interaction-design-misfit drive voluntary exit from augmented roles? Worth tracking.

**To [[dynamic-capabilities]]:** the four-parameter framework operationalises two W&W microfoundations — *digital-transforming/redesigning-internal-structures* (work procedure, decision authority) and *digital-transforming/improving-digital-maturity* (training, incentives). Adds an empirical anchor that *structural redesign without cognitive-style tailoring is worse than no redesign at all* — a strong claim against default-deployment approaches.

## What's *not* in this source

- **No LLM / generative-AI deployment.** The AI system in the study is a (mid-2010s-era) predictive system providing target lists, customer-interaction plans, and summary reports — *not* a frontier-LLM-based agentic system. Authors explicitly note in §6.2 *Future Research*: *"It would also be relevant to explore how our findings apply to newer AI technologies, such as generative AI, including large language models."* The wiki should treat the four-parameter framework as a *vocabulary that likely generalises* but not as a tested-on-LLMs finding.
- **No multi-industry replication.** Single-firm, single-industry (Nordic pharma sales). Whether the cognitive-style-interaction-fit moderator generalises to engineering, customer support, finance, healthcare, or creative knowledge work is an open question.
- **Power constraints noted by authors.** With only 12 clusters and 72 individuals, the paper cautions against strong causal interpretation. Treat as strong correlational evidence with credible identification rather than as a clean causal claim.

## Open questions for next ingest

- Does the **four-parameter interaction-design framework** apply at LLM-agent / agentic-AI scale, or is it tied to predictive-AI deployment?
- Does **work-procedure as the most-critical-parameter** finding survive in newer LLM-based deployments where work procedures are inherently more flexible?
- Are there other **cognitive-style or interaction-style moderators** the framework would benefit from incorporating (e.g. Wang et al. 2024 on experience-tailoring, cited in §6.2)?
- The paper's prior theoretical anchor — **Raisch & Krakowski 2021 *Artificial Intelligence and Management: The Automation-Augmentation Paradox*** — is cited self-referentially and is *not* in the wiki. Worth ingesting as the theoretical companion.
