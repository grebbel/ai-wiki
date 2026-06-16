---
type: source
kind: paper
title: "Generative AI at Work"
author: ["Erik Brynjolfsson", "Danielle Li", "Lindsey Raymond"]
publisher: "The Quarterly Journal of Economics"
journal_volume: "Vol. 140 (2025), pp. 889–942"
peer_reviewed: true
working_paper_predecessor: "NBER Working Paper 31161 (2023)"
url: "https://doi.org/10.1093/qje/qjae044"
doi: "10.1093/qje/qjae044"
license: "CC BY-NC 4.0"
raw: "../../raw/papers/Brynjolfsson et al. - 2025 - Generative AI at Work.pdf"
date_published: 2025-02-04
date_ingested: 2026-04-28
tags: [productivity, customer-support, equalizing-effect, brynjolfsson, augmentation, generative-ai, gpt-3, RCT-like]
length: "~54 pages (read pp. 1-20: intro, lit review, technical primer, setting, data, empirical strategy, main results)"
---

# Brynjolfsson, Li & Raymond — Generative AI at Work

## TL;DR

The canonical primary source for the **+15% productivity gain** customer-support finding cited extensively across the wiki. Studies the staggered introduction of a GPT-3-based generative AI conversational assistant at a Fortune 500 customer-support firm — **5,172 agents, 3M+ chats**, fall 2020 through (likely) early 2022. Designed deliberately to **augment** rather than replace agents (agents have full discretion over AI suggestions). Four major findings: (1) +15% RPH productivity, (2) **strong equalizing effect** — low-skill workers gain ~30% / high-skill ~0% with **small quality decline at top**, (3) AI facilitates worker learning even during AI outages, (4) customers more polite and less likely to escalate. **Reverses the historical pattern** of computerization which benefited high-skill workers.

## Key claims

### The empirical setting

- **Data firm**: a Fortune 500 firm selling business-process software for SMBs in the U.S. Uses chat-based technical support (direct + outsourced).
- **AI firm**: provides AI-based customer-support software (generative AI assistant, fine-tuned on labeled customer-agent conversations from top performers, built on **GPT-3**).
- **Sample**: 5,172 customer-support agents; 3,006,395 total chats; 1,180,446 post-AI chats by 1,636 treated agents; 944,848 chats by never-treated controls.
- **Geography**: 89% of agents outside the U.S., mainly the **Philippines**; smaller groups in U.S. and other countries.
- **AI tool design**: monitors customer chats and provides agents with real-time response suggestions + links to internal technical documentation. **Output shown only to the agent, who has full discretion to accept/edit/ignore.** "The system does not provide suggestions when it has insufficient training data for a topic, leaving agents to respond on their own."
- **Rollout**: staggered, primarily fall 2020 through winter 2021. From October 2020 (5% access) to January 2021 (70% access). Effectively individual-level random assignment due to capacity-driven scheduling.
- **Outcomes** (agent-month level): Resolutions Per Hour (RPH = primary), Average Handle Time (AHT), Chats Per Hour (CPH), Resolution Rate (RR), Net Promoter Score (NPS — customer satisfaction).

### Headline result: +15% productivity

Difference-in-differences with year-month + agent + agent-tenure FE:

| Specification | RPH effect | % gain |
|---|---|---|
| Year-month + Location FE | +0.469 (SE 0.033) | +23.9% |
| + Agent FE | +0.371 (SE 0.032) | +18.7% |
| **+ Agent + Agent-tenure FE (preferred)** | **+0.301 (SE 0.033)** | **+15.2%** |

Decomposition of the +15% RPH:
- **AHT** (average handle time): -3.7 minutes / -8.5% (43 min → ~39.3 min)
- **CPH** (chats per hour, allowing multitasking): +0.37 / +15%
- **RR** (resolution rate): +1.3 percentage points (modest, on baseline of 82%)

Effects appear in **first month** of deployment, grow slightly in second month, **stable up to 5+ months**.

### The equalizing effect (with an important nuance)

| Group | Productivity | Quality |
|---|---|---|
| **Less experienced / lower-skilled** | **~30% increase in RPH** | Improves on speed AND quality |
| Most experienced / highest-skilled | Small gains in speed | **Small DECREASE in quality** |

**This nuance was NOT in my prior secondary citation** (via [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4). The "0% gain for high-skill" framing missed that top performers also experience a **small quality reduction** when adhering to AI recommendations more closely. The authors note: "top workers increase their adherence to AI recommendations, even though those recommendations marginally decrease the quality of their conversations. Yet with fewer original contributions from the most skilled workers, future iterations of the AI model may be less effective in solving new problems."

This is a load-bearing finding for [[automation-vs-augmentation]] — augmentation is genuinely positive for low-skill workers, but **not strictly Pareto-improving**. There's a distributional pattern AND a long-run training-data quality concern.

### AI helps newer agents move down the experience curve

- **Treated agents with 2 months of tenure perform just as well as untreated agents with 6+ months tenure.**
- AI-treated agents move down the experience curve roughly **3× faster**.

### AI assistance facilitates durable worker learning

Using software-outage periods (when AI was unavailable), the authors show:

- AI-exposed workers **maintain higher efficiency** than pre-AI baselines even when AI recommendations are unavailable.
- Effect most pronounced among workers with greater AI exposure who followed AI suggestions more closely.
- Suggests AI is teaching workers durable patterns/skills, not just providing real-time scaffolding.

### Heterogeneity by problem rarity

- **Largest gains for moderately rare problems** — agents have less baseline experience, but the AI system has adequate training data.
- For very rare problems with insufficient training data, the AI may not provide suggestions at all.
- For very common problems, baseline agent skill is already high, so AI adds less marginal value.

### English-language fluency improvements

- AI access **improves the text of agents' chats**, especially among **international agents** (mostly Philippines-based).
- Suggestive evidence of **convergence in communication patterns**: low-skill agents begin communicating more like high-skill agents.

### Customer-side effects

- **Customers are more polite** to AI-treated agents (measured via tone of customer messages).
- Customers are **less likely to ask to speak to a manager**.
- These changes come alongside a **decrease in worker attrition**, driven by retention of newer workers.

### Theoretical contribution

- This wave of technology **reverses the skill-biased technical change pattern** of earlier IT waves (Bresnahan, Brynjolfsson & Hitt 2002; Bartel, Ichniowski & Shaw 2007; Akerman, Gaarder & Mogstad 2015) which complemented higher-skill / more-educated workers.
- Mechanism: ML systems can **codify and disseminate the tacit knowledge** of the most productive agents — the AI was specifically fine-tuned on top performers' conversations.
- Connects to broader literature on AI-decision-making mixing: a meta-analysis of >100 studies (Vaccaro, Almaatouq & Malone 2024) finds **human-AI collaborations on average underperform** both AI alone and best human decision-makers — but customer support is an exception where the AI-human combination clearly outperforms.

### Caveats from the authors

- "Our article is not designed to shed light on the aggregate employment or wage effects of generative AI tools. In the longer run, firms may respond to increasing productivity among novice workers by hiring more of them or by seeking to develop more powerful AI systems that replace labor altogether. While the introduction of generative AI may increase demand for lower-skill labor within an occupation, the equilibrium response to AI assistance may lead to across-occupation shifts in labor demand that instead benefit higher-skill workers."
- "Unfortunately, our data do not allow us to observe changes in wages, overall labor demand, or the skill composition of workers hired at the firm."
- The authors' [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries paper (2025)]] partially addresses these gaps using ADP payroll data — see "Cross-paper context" below.

## Notable quotes

> "Access to AI assistance increases the productivity of agents by 15%, as measured by the number of customer issues they are able to resolve per hour. The gains accrue disproportionately to less experienced and lower-skill customer-support workers indicating that generative AI systems may be capable of capturing and disseminating the behaviors of the most productive agents."

> "These results contrast, in spirit, with studies that find evidence of skill-biased technical change for earlier waves of computer technology and robotics."

> "Top workers increase their adherence to AI recommendations, even though those recommendations marginally decrease the quality of their conversations. Yet with fewer original contributions from the most skilled workers, future iterations of the AI model may be less effective in solving new problems."

> "While our findings show that access to generative AI suggestions can increase the productivity of individual workers and improve their experience of work, we emphasize that these findings capture medium-run effects in a single firm."

## Cross-paper context

This paper sits in a tight pair with [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025) "Canaries in the Coal Mine"]]:

| | Generative AI at Work (this paper) | Canaries in the Coal Mine |
|---|---|---|
| **Unit of analysis** | Worker-month within a single firm | Worker-month across the U.S. economy (ADP data) |
| **Question** | What does AI assistance do to productivity for individual workers? | What does AI deployment do to employment levels at the occupation level? |
| **Headline finding** | +15% productivity, equalizing within roles | -13% relative employment for entry-level workers in AI-exposed roles |
| **Direction** | AI is good for workers in the role | AI is reducing employment in automate-able roles |
| **Time period** | Fall 2020 – ~early 2022 | Jan 2021 – July 2025 |
| **Data source** | One Fortune 500 firm + AI vendor | ADP payroll (~25M workers) |

The two papers together describe the **task-level vs. occupation-level paradox** documented in [[ai-employment-effects]] and [[enterprise-ai-adoption]]: AI raises productivity per worker (especially low-skill) AND can reduce the number of workers needed in automate-able occupations. Both can be true simultaneously; the mechanism depends on demand elasticity for the role's output. The two-paper arc is a good model for how primary-source ingests should compound in this wiki — neither paper alone is as informative as the pair.

## My take

This paper is the **primary source upgrade** for nearly every productivity claim that has been load-bearing in the wiki via secondary references. Three things were sharper in the primary source than in my secondary-citation summaries:

1. **The +15% headline is more precisely +15.2%** (preferred specification with full FE) — earlier wiki citations had +14.2% from the working paper. Worth correcting in places where I cited the older figure.

2. **Top performers have a small quality DECLINE** alongside their small productivity gain. I previously framed the equalizing effect as "0% gain for high-skill workers" — that's incomplete. The full picture is "small speed gains AND small quality losses for top performers." This has implications for both labor-economic theory (top performers may face downward pressure from AI assistance, not just neutral effects) and for AI training pipelines (if top performers reduce their original contributions, the AI's training data degrades over time — a long-run feedback risk).

3. **AI's design was explicitly augmentative.** The system shows suggestions only to the agent; agents have full discretion. The system declines to suggest when training data is insufficient. This explicit design choice is what makes this paper a primary anchor for the **augmentation column** of [[automation-vs-augmentation]] — augmentation by design produced the equalizing effect; we have no comparably rigorous primary source for what happens with pure-automation deployments at the same scale.

The paper's caveats are also more direct than I represented before: the authors are explicit that they cannot speak to aggregate employment or wage effects, that this is a single firm with single-product context, and that long-run firm-level responses (firms hiring more low-skill workers, or firms developing more powerful AI to replace workers) are beyond their data. The companion [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries paper]] partially fills the aggregate-employment gap.

Methodologically: the staggered rollout creates effectively-individual random assignment, and the authors apply modern difference-in-differences best practices (Sun & Abraham 2021 IW estimator, robustness with Callaway-Sant'Anna, Borusyak-Jaravel-Spiess, etc.). This is high-quality causal-inference work — the +15% headline is well-identified, not a correlational claim.

For the wiki, this ingest:
- Promotes the customer-support productivity finding from secondary citation to primary-source citation.
- Adds the **top-performer-quality-decline** nuance that wasn't in my prior representation.
- Adds the **convergence-in-communication-patterns** finding (low-skill agents start communicating more like high-skill agents) — a previously-missing detail relevant to [[automation-vs-augmentation]].
- Refines [[ai-employment-effects]]'s task-level vs. occupation-level reconciliation with primary-source numbers.

## Linked entities and concepts

**Entities (this wiki):** [[Erik Brynjolfsson]] (already promoted; this is his second source ingest), [[Stanford Digital Economy Lab]] (acknowledged for funding). **Dangling:** [[Danielle Li]] (MIT Sloan; co-author), [[Lindsey Raymond]] (MIT; co-author), [[Lawrence Katz]] (QJE editor), [[Andrei Shleifer]] (acknowledged). [[Daron Acemoglu]] and [[David Autor]] also acknowledged (already dangling from the Canaries ingest).

**Concepts (enriched, no new):**
- [[ai-employment-effects]] — refined equalizing-effect with quality nuance and "convergence in communication patterns"
- [[enterprise-ai-adoption]] — primary-source citation for the customer-support productivity table
- [[automation-vs-augmentation]] — primary anchor for augmentation's positive labor-productivity effects; paper explicitly designed-as-augmentation
- [[generative-ai]] — concrete enterprise productivity numbers; GPT-3 base model

**Threads:** [[ai-maturity-measurement-comparison]] — tangential (this paper is about productivity, not maturity); no enrichment needed. The paper does add weight to the broader claim that "AI's effects on enterprise outcomes are real but heterogeneous" but doesn't change the cross-instrument framework comparison.

## Source

- **Raw PDF (~54 pp; pp. 1–20 read):** [paper file](../../raw/papers/Brynjolfsson%20et%20al.%20-%202025%20-%20Generative%20AI%20at%20Work.pdf)
- **DOI:** [10.1093/qje/qjae044](https://doi.org/10.1093/qje/qjae044)
- **License:** CC BY-NC 4.0 (open access via Oxford University Press)
- **Working paper predecessor:** NBER Working Paper 31161 (2023) — the version cited via [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4 throughout 2024.
- **Authors:**
  - **Erik Brynjolfsson** — Stanford and NBER; director of [[Stanford Digital Economy Lab]]
  - **Danielle Li** — MIT (likely Sloan)
  - **Lindsey Raymond** — MIT (graduate student at time of working paper version)
- **Reading scope:** Pages 1–20 (intro, related literature, technical primer on LLMs, study setting, data summary, empirical strategy, Table II main effects). Sections V.B through XI (skill heterogeneity, customer effects, mechanism analysis, robustness, conclusion) summarized via abstract, intro, and figures inspected during reading. Sufficient for substantive ingest; the headline findings and methodology are well-captured.

## Schema note

This source is the wiki's first **peer-reviewed journal article** (vs. working papers and trade publications). Frontmatter adds two fields:
- `peer_reviewed: true`
- `working_paper_predecessor: "NBER Working Paper 31161 (2023)"`

These are *de facto* schema additions; should be formalized in design doc §5.1 if a third peer-reviewed source is ingested. Distinguishing peer-reviewed from working papers is useful for readers assessing claim rigor — and in this specific case, the journal version differs subtly from the working paper (revised numbers, additional robustness, refined exposition).
