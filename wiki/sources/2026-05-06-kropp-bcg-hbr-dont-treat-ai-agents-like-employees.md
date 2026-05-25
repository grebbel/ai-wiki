---
type: source
kind: article
title: "Research: Why You Shouldn't Treat AI Agents Like Employees"
author: ["Matthew Kropp", "Julie Bedard", "Emma Wiles", "Megan Hsu", "Lisa Krayer"]
publisher: "Harvard Business Review (Generative AI section, BCG Henderson Institute research)"
url: "https://hbr.org/2026/05/research-why-you-shouldnt-treat-ai-agents-like-employees"
date_published: 2026-05-06
date_ingested: 2026-05-25
length: "~12 pages, full ingest"
raw: "../../raw/articles/Research_ Why You Shouldn’t Treat AI Agents Like Employees.pdf"
tags: [bcg, bcg-henderson-institute, hbr, ai-employee-framing, anthropomorphizing-ai, accountability, ai-governance, randomized-experiment, agentic-ai, redesign-workflows, human-in-the-loop, ai-brain-fry, professional-identity, kropp-bedard, generative-ai]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/strategic-agility
  - strategic-renewal/organizational-culture
  - contextual/internal-enablers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "**Independent empirical confirmation of the *managers-in-charge-of-agents* failure mode Allen names.** Allen (~22:48–23:10): *'we've gone from this pyramid... through to people trying to put managers or people in charge of agents. I haven't seen this working really well, because those domain experts need to understand that orchestration flow of what's going on.'* Kropp et al. supply the **RCT-grade empirical evidence** for *why* it doesn't work: in their N=1,261 randomized experiment, the *AI-employee framing* (vs *AI-tool framing*, holding everything else constant) caused — among managers in orgs that already have AI on their org charts — a **9pp drop in personal accountability** (with 8pp shift to the AI), **44% more escalation requests**, **18% fewer errors caught**, and (whole-sample) **13% higher uncertainty about professional identity**. Allen's named prescription (*'put humans on judgment work, agents on execution work'* + Brooklyn's *'human starts the work, human ends the work'*) and Kropp et al.'s five-point redesign recommendation converge on the same operational shape from independent vantages 15 days apart (May 6 → May 21). The convergence pattern: both reject the *AI-as-employee* framing AND prescribe *AI-as-software-with-clear-human-accountability + workflow-redesign* instead."
    confidence: 0.85
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "**Same redesign-the-process-not-the-org-chart prescription at HR/finance-manager altitude vs Anthropic-engineering-org altitude.** Fung (Anthropic): *'when agentic coding goes from individual tool to org-wide default, the tool isn't the hard part... your processes are.'* Kropp et al.: *'organizations cannot simply layer [AI] onto workflows built for human pace... CEOs need to redesign the work of both AI and humans.'* Five-point redesign list (workflows + role expectations; explicit personal accountability; capability-building plan; don't constrain agents to 1-for-1 roles; deliberate choices about human-work evolution) is the BCG/advisory-altitude version of Fung's *five norms rebuilt* list at Anthropic. Convergent at *processes / workflows are load-bearing*; complementary at the org-altitude — Fung at engineering-org level, Kropp et al. at HR/finance-management level."
    confidence: 0.8
  - type: contradicts
    target: 2026-04-25-masad-replit-ceo-only-two-jobs-left
    via: "**Productive tension on the *AI-as-employee-substitute* framing.** Masad (Replit CEO, April 2026): the *only-two-jobs-left* framing — AI agents will substitute for most current jobs, leaving only managers-of-agents and infrastructure-of-agents roles. Kropp et al. (May 2026): empirically test the *AI-as-employee* framing in a randomized experiment and find it **causes the failure modes that would prevent Masad's prediction from being a productive end-state** — accountability shifts to the (non-accountable) AI; escalation balloons; error-catching drops; professional-identity crisis. The disagreement turns on what the *agentic future* operating model looks like: Masad's framing implicitly accepts the AI-employee construct as the destination, while Kropp et al. argue the construct itself is the failure mode and prescribe AI-as-software-with-human-accountability instead. Both sources may be right at different time horizons — Masad's prediction at 5–10 year horizon; Kropp et al.'s findings at the present operational-redesign horizon. The wiki holds both, with this edge naming the productive tension at the operating-model layer."
    confidence: 0.7
  - type: contradicts
    target: 2026-05-19-garg-yc-internal-ai-agent-evolves-itself
    via: "**Productive tension on the *one-agent-per-role* design pattern.** Garg (AnswerThis CEO, May 19): a 2-FTE startup running >$2M ARR via an *internal AI agent that processes >100 emails/day, closes support tickets, updates the CRM, and builds its own tools when needed*. Kropp et al. recommendation #4 explicitly: *'Don't constrain agents into 1-for-1 roles. The concept of “employee” assumes bounded roles, finite human capacity, and a hierarchy in which work is delegated to someone less experienced or knowledgeable. AI does not share these limits. A single agent can operate across many workflows; multiple agents can reshape one job.'* Garg's design is paradigmatically *one agent reshaping multiple traditional jobs* — which is *what Kropp recommend* — but Garg also describes the agent in *employee-style* language (*'a non-technical co-founder trains the agent by giving it feedback in Slack'* — feedback-loop language drawn from people management). The productive contradiction is at the *language layer*: same operational shape (one agent → many roles), opposite framings (Garg uses employee-style framing in his pitch; Kropp et al. recommend explicitly against it). Worth surfacing — both founder-altitude pragmatism (Garg) and advisory-altitude prescription (Kropp et al.) are operational, and the gap between them is *what the wiki cluster has been waving at* as the open question of agentic-AI organisational design."
    confidence: 0.65
  - type: supports
    target: 2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting
    via: "**Consultant-altitude pair on enterprise AI transformation doctrine** (BCG + McKinsey). Sternfels (McKinsey, Feb 2026): McKinsey-altitude prescriptions for enterprise AI consulting transformation. Kropp et al. (BCG Henderson Institute, May 2026): BCG-altitude prescriptions for enterprise agentic-AI rollout. Both emphasise *workflow redesign over technology layering*, *explicit accountability mechanisms*, and *capability-building plans for humans managing agents*. The two top-of-market consulting firms' research arms converging on the same prescription set is the wiki's strongest two-firm anchor on enterprise-AI-transformation governance to date."
    confidence: 0.75
  - type: supports
    target: 2026-05-02-dutt-chatterji-ai-experimentation-to-transformation
    via: "**Same micro-productivity-trap diagnosis, different lever named.** Dutt et al. (Bain/OpenAI, May 2026): *micro-productivity-trap* mechanism — task-level AI gains failing to translate to firm-level value; named sub-modes *offering lock-in* and *process lock-in*. Kropp et al. (BCG Henderson Institute, May 2026): same firm-level-value-gap, with a third named sub-mode — **anthropomorphizing lock-in**: organisations that frame AI as employees end up with diffused accountability, more escalation, lower review quality, and identity disruption *without* meaningfully increasing adoption intent. The named mechanism is structurally a third sub-mode in the Dutt et al. taxonomy at the same advisor-altitude — BCG + Bain converging at near-identical timing."
    confidence: 0.75
  - type: supports
    target: 2026-04-28-warner-wager-dynamic-capabilities-digital-transformation
    via: "**Empirical operationalisation of the W&W *redesigning-internal-structures* + *organizational-culture* microfoundations.** Where W&W frame structural redesign and cultural renewal as theoretical microfoundations of digital-transforming + strategic-renewal capabilities, Kropp et al. add a **specific RCT-grade empirical hazard**: the apparently-cultural choice of *how to frame AI in the org* (tool vs employee) materially changes accountability and quality outcomes. The framing is not merely symbolic — it is a load-bearing microfoundation in the W&W sense."
    confidence: 0.65
confidence: 0.85
last_confirmed: "2026-05-25"
---

# Research: Why You Shouldn't Treat AI Agents Like Employees

> As organizations experiment with placing AI agents on org charts as "employees," new research shows this framing has unintended consequences. In a large-scale experiment, anthropomorphizing AI reduced individual accountability, increased unnecessary escalation, lowered review quality, and heightened employee uncertainty about their roles — without improving adoption. The findings suggest the core challenge is not whether to deploy agentic AI, but how to redesign workflows, roles, and governance so humans remain clearly accountable while effectively supervising increasingly capable systems.

(Article summary, [[Harvard Business Review|HBR]] Generative AI section.)

A **Harvard Business Review** research-feature article published 6 May 2026, co-authored by five researchers at [[Boston Consulting Group]] and BCG Henderson Institute (plus one Boston University academic). The lead author is **Matthew Kropp** (BCG managing director and senior partner; CAIO of BCG X; BCG Henderson Institute Fellow). Co-authors: **Julie Bedard** (BCG managing director and partner, global People & Organization and AI leadership teams; BCG Henderson Institute Fellow), **Emma Wiles** (Boston University Questrom School of Business; MIT Initiative on the Digital Economy digital fellow), **Megan Hsu** (BCG project leader; BCG Henderson Institute Ambassador), and [[Lisa Krayer]] (BCG principal; People & Organization, Technology and AI teams; BCG Henderson Institute Ambassador — second wiki appearance after [[2026-04-28-dellacqua-jagged-technological-frontier|the Jagged Frontier paper]], so promoted from Dangling to entity page in this ingest).

The article reports a randomized experiment (N=1,261 HR and finance managers / directors / executives across US, Canada, and EU) designed to test whether **the framing of an AI system — as a tool, as a human teammate ("Alex"), or as an AI teammate ("ALEX-3") — causes downstream behavioural and organisational consequences when everything else is held constant.**

**Headline finding:** the *AI-employee framing* (vs *AI-tool framing*) caused — among managers in organisations that *already have AI agents on their org charts* — a **9pp drop in personal accountability** (with 8pp shift to the AI itself), **44% more escalation requests**, **18% fewer errors caught**, and (whole-sample) **13% higher uncertainty about professional identity**, **7% higher concern about job security**, **10% lower trust in how AI would be used**, and **no meaningful increase in adoption intent**. The article closes with five prescriptions for redesigning work for *responsible human-AI collaboration*.

**Authors / dangling list.** First wiki source by four of the five co-authors; per the [[../../CLAUDE|author-entity promotion rule]] (second-source promotion), they stay on the dangling list at this ingest:

- **Promoted from Dangling to entity page** in this ingest: [[Lisa Krayer]] (BCG principal; second wiki appearance via the [[2026-04-28-dellacqua-jagged-technological-frontier|Jagged Frontier paper]]).
- **Dangling** (single-source mention, deferred): Matthew Kropp (BCG managing director / senior partner; CAIO of BCG X), Julie Bedard (BCG managing director / partner; People & Org + AI leadership teams), Emma Wiles (BU Questrom; MIT IDE digital fellow), Megan Hsu (BCG project leader; BCG Henderson Institute Ambassador).

## TL;DR

Five substantive contributions warrant ingest:

1. **The first RCT-grade empirical evidence in the wiki on the *AI-as-employee framing*** — a 1,261-manager randomized experiment with three conditions (AI-tool / human-teammate / AI-teammate). Holds everything else constant; only manipulates the *named author* of the documents under review. **The framing alone moves accountability, escalation, quality, and identity outcomes** when subset to managers whose organisations already have AI on their org charts.

2. **The four named failure modes of anthropomorphizing AI** — *accountability becomes blurred* (9pp personal-accountability drop + 8pp shift to AI; *"the blame isn't on a person, it's on the technology"*), *escalation and burden on others increase* (44% more requests for additional review under AI-employee framing), *quality control declines* (18% fewer errors caught; budget-with-inconsistent-totals and entry-level-role-requires-10-years-experience examples), *professional identity and trust take a hit* (13% higher identity uncertainty, 7% higher job-security concern, 10% lower trust). All four operate as **organisational hazards introduced by a framing choice** that is *cheap to make and hard to reverse*.

3. **The 5-point redesign prescription** for *responsible human-AI collaboration*: (1) explicitly redefine workflows + name new (human) role expectations + redesign spans of control + reset performance management to reward quality of oversight and effective orchestration of AI; (2) make accountability explicit and personal for employees and agents (define decision rights, escalation triggers, consequences); (3) design and implement a capability-building plan for employees managing agents; (4) **don't constrain agents into 1-for-1 roles** (*"A single agent can operate across many workflows; multiple agents can reshape one job"*); (5) make deliberate choices about how human work evolves toward *judgment, creativity, and ownership*.

4. **The *AI brain fry* concept named in passing** (referencing a prior BCG study) — *mental fatigue from excessive use or oversight of AI tools beyond one's cognitive capacity*. Workers experiencing brain fry score 11% / 39% higher on minor / major error frequency. The article's contribution: *AI-employee framing may introduce a related risk* — when managers feel less need to fully engage in cognitive review (because *"Kevin"* drafted it, not their colleague), scrutiny drops further. This is a vendor-customer-side empirical correlate of [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni's]] *gear-3 reactive work* neurological mechanism on the augmentation pole of [[automation-vs-augmentation]].

5. **The *Scout* and *Kevin* exhibits** — two real-world anecdotes from study participants' organisations. *Scout* is an AI agent formally listed on the HR team org chart at one participant's company, *"functioning like a junior employee, acting autonomously with a defined scope, outputs, and boundaries — embedded directly into the company's hiring process workflow"*; the HR leader notes *"it's technically an equivalent peer on your team. That's how it acts and behaves."* *Kevin* is an AI agent on another company's org chart whom colleagues joke *"he's a little dry"* and to whom they redirect blame when errors occur: *"Hey, Kevin's making a mistake. Why is he making that mistake?"* The two exhibits are the wiki's first explicit *worked exemplars* of the AI-on-org-chart practice the article studies.

## What was actually ingested

Full 12-page article including the abstract, introduction, *AI Employees Enter the Workforce* section, the four-failure-mode section, the five-point *Redesigning Work for Responsible Human-AI Collaboration* section, and the author bios. Two BCG Henderson Institute prior studies are cited in-text: the *AI brain fry* study (not separately ingested) and *the recent BCG study on AI and workforce transformation* (3.5× managerial role-modelling claim — also not separately ingested).

## The experiment design

- **N=1,261** managers, directors, and executives from HR and finance functions across US, Canada, and EU.
- **Three randomised conditions** (between-subjects): document drafted by (1) *an AI tool*, (2) *a human employee on their team named "Alex"*, (3) *an AI employee on their team named "ALEX-3"*. Documents and errors held constant across conditions.
- **Pre-registered subset analysis**: participants whose organisations already have AI agents on org or work charts (23% of the sample). This is the population most likely to internalise the framing as real rather than hypothetical.
- **Outcome measures**: (a) allocation of accountability for the documents (self / team / AI / leadership); (b) escalation choices (with incentives reflecting confidence-vs-cost-of-passing-work-on tradeoffs); (c) errors caught (with performance-based incentives encouraging careful review); (d) professional identity uncertainty; (e) job-security concern; (f) AI-use trust; (g) adoption intent.
- **Population baseline**: 31% of participants said their company's leadership already frames AI as a teammate / employee; 23% said their organisation has AI agents listed on org / work charts. The practice extends beyond tech sector — healthcare, financial services, retail, professional services.

## The four failure modes (with quoted operative anecdotes)

### Accountability becomes blurred

- **9pp drop in personal accountability**; **8pp increase in accountability attributed to AI**.
- Operative quote: *"The blame isn't on a person; it's on the technology."*
- Mechanism: *"Today's AI systems cannot be held accountable and require clear human ownership"* — the framing redirects responsibility to an entity that cannot bear it, diffusing the accountability that organizations need to keep on humans.

### Escalation and the burden on others increase

- **44% more requests for additional review** under AI-employee framing vs AI-tool framing.
- Mechanism: lower self-perception of judgment quality when reviewing AI-employee output; *"questioning their own skills, doubting whether they had identified all issues, or feeling the need to re-verify work they would typically accept at face value."*
- Cost: extra review cycles charged back to the organisation.

### Quality control declines

- **18% fewer errors caught** under AI-employee framing.
- Worked examples in the document set: a budget showing contract *"reduces costs"* but accompanying spreadsheet showing total expenses *increased*; an entry-level job description requiring *"more than 10 years of experience."*
- Mechanism (the article's *AI brain fry* extension): *"When managers review AI as a tool, they still experience the cognitive burden of oversight. When the same output is framed as coming from an 'employee,' managers may feel less need to fully engage in the cognitive burden of review — effectively absolving some of that burden — and apply less scrutiny to catching errors."*

### Professional identity and trust take a hit

- Whole-sample: **13% higher uncertainty about professional identity**, **7% higher concern about job security**, **10% lower trust in how AI would be used**.
- Operative quotes: *"If you want people to feel like they will lose their job to AI, or can be easily replaced by AI, then put it on the org chart."* / *"Makes you wonder what your role is supposed to be when AI is treated like a colleague."*
- The article's leadership-issue framing: *"In companies that push AI without addressing their human employees' go-forward role, managers may assume human roles are universally becoming less relevant. Yet AI transformations are not monolithic. Some roles are substitutable; many others are augmentable... When companies fail to distinguish between the two, employees are left to interpret AI solely as a substitute rather than a support, undermining trust and culture for all adopting populations."*

### Adoption does not meaningfully increase

- The implicit *upside* of anthropomorphizing — that it would make AI feel more familiar / approachable and therefore drive adoption — *did not materialise* in the experiment.
- Adoption follows **managerial encouragement and expectations**, not framing. Operative anecdote: *"At the point that I saw it was becoming tied to employee success — when somebody used an LLM, they got featured at a town hall — I started telling everybody on my team, 'You've got to use this as much as you can.'"*
- BCG cross-reference: *"Companies leading in AI maturity are 3.5 times more likely to have managers who actively role-model AI use in daily operations, underscoring that visible managerial signaling drives adoption."*

## The five-point redesign prescription

1. **Explicitly redefine workflows and then name new (human) role expectations.** Redesign roles at scale; clarify expectations; explicitly state oversight responsibility over AI systems in job descriptions; set realistic expectations for velocity and volume; name the persistent human skills that remain critical. Reset performance management to reward *quality of oversight and effective orchestration of AI systems*, not just speed and output.
2. **Make accountability explicit and personal for employees and agents.** AI agents should be treated as *what they are — software automation that requires clear human accountability for the output and operation*. Define decision rights (what is the agent allowed to do autonomously vs. what requires explicit human approval); escalation triggers (what triggers review, who intervenes, who bears the cost of delay or error); consequences (when the agent fails, what happens next; how accountability is carried forward over time).
3. **Design and implement a capability-building plan for employees managing agents.** New managerial toolkit and training curriculum for the *delegation-vs-control balance* with AI. Employees must understand the full range of tasks AI can perform, *use it as a source of intelligence rather than just task execution*, and know when to rely on AI / when to challenge / where its limitations differ from those of human workers.
4. **Don't constrain agents into 1-for-1 roles.** *"The concept of 'employee' assumes bounded roles, finite human capacity, and a hierarchy in which work is delegated to someone less experienced or knowledgeable. AI does not share these limits. A single agent can operate across many workflows; multiple agents can reshape one job."* Design the right *agentic unit* for the workflow — *may be a broader functional capability used across a team or process, rather than defaulting to one agent per human role.*
5. **Make deliberate choices about how human work evolves.** *"How work is divided between humans and AI is a design choice."* As AI improves productivity, it creates the opportunity to *redeploy human effort toward higher-value activities where demand is growing* — work requiring *judgment, creativity, and ownership*. Cites prior BCG Henderson Institute research on the *executive-vs-individual-contributor perception gap*: 76% of executives believe employees are enthusiastic about AI adoption; only 31% of individual contributors report the same.

## Substantive contributions to the wiki

**To [[automation-vs-augmentation]]:** the article's *augmentable vs substitutable* roles distinction is the [[Boston Consulting Group|BCG]]/HBR-altitude restatement of the wiki's central conceptual cut. Adds a new normative-prescription dimension: *organisations failing to distinguish augmentable from substitutable roles cause employees to interpret AI solely as a substitute*, undermining trust and culture even where the deployment is augmentative. The cultural-misclassification cost is structural, not merely communicative.

**To [[enterprise-ai-adoption]]:** the article's headline finding is that the *framing choice* (tool vs employee) is a load-bearing variable in enterprise-AI adoption outcomes. The BCG 3.5× managerial-role-modelling statistic + the 76% / 31% executive-vs-IC perception gap add empirical anchors to the *adoption-via-managerial-signalling* channel.

**To [[micro-productivity-trap]]:** the *anthropomorphizing lock-in* failure mode is structurally a third sub-mode in the [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al. taxonomy]] (alongside *offering lock-in* and *process lock-in*) — organisations that frame AI as employees end up with diffused accountability, more escalation, lower review quality, and identity disruption *without* meaningfully increasing adoption.

**To [[ai-deskilling]]:** the *AI brain fry* cross-reference (with the 11% / 39% minor / major error frequency increases) is the wiki's first empirical anchor on *over-use-of-AI-causes-deskilling-through-cognitive-load* — distinct from the [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] *task-composition-shift* mechanism. Adds a second causal pathway to the same outcome.

**To [[agent-harness]]:** the *decision rights / escalation / consequences* triad in recommendation #2 maps onto the harness's *permission/guardrails*, *human-in-the-loop*, and *observability* layers. The article gives the *vendor-customer-side governance-design framing* of harness primitives the wiki has otherwise treated from the vendor-engineering side.

**To [[ai-agents]]:** the named *"don't constrain agents into 1-for-1 roles"* prescription is the wiki's first explicit *design-for-multi-role-agents* recommendation at consultant altitude — a structural anti-pattern named.

## Open questions for next ingest

- What does the **prior BCG *AI brain fry* study** (named in passing in this article) actually measure, and is the 11%/39% error-frequency increase robust to other samples? Worth ingesting on its own.
- The **3.5× managerial-role-modelling figure** comes from a separate BCG study on *AI and workforce transformation* — also worth ingesting separately.
- The **76% / 31% executive-vs-IC enthusiasm gap** is from prior BCG Henderson Institute research — same.
- Does the *AI-employee-framing penalty* survive across cultures? The experiment is US / Canada / EU; effects in Asia-Pacific or LatAm enterprises may differ.
- Does the framing penalty attenuate over time as managers gain experience with AI agents on org charts? The current evidence is from the early-adoption period; longitudinal data is the next question.
