---
type: source
kind: video
title: "Architecting AI-Native Organizations: How to Redesign Work at Scale — Joe Beutler"
author: ["IT Revolution"]
publisher: "IT Revolution (Enterprise AI Summit: Spring 2026, 9–10 April 2026)"
url: "https://www.youtube.com/watch?v=fFOLWoHyWLE"
date_published: 2026-06-02
date_ingested: 2026-06-06
length: "~25:25 minutes (transcript ~360 lines; auto-generated ASR transcript, light cleanup applied for proper nouns — Joe Beutler, ChatGPT, Codex, PwC, BBVA — and obvious stutters/fillers)"
raw: "../../raw/videos/2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler.md"
tags: [enterprise-ai, ai-native-organization, org-design, agentic-ai, openai, ask-assist-automate, embedded-engineering, team-agents, governance-vs-transformation, joe-beutler, gene-kim, it-revolution, enterprise-ai-summit-2026, financial-services-ai]
confidence: 0.75
last_confirmed: "2026-06-06"
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "both: embed engineering inside the business, business owns outcomes, org design is the binding constraint — Anthropic engineering-internal view vs OpenAI cross-customer deployment view"
    confidence: 0.75
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "embedded teams + workflow-level focus; Ask-Assist-Automate maturity ladder complements Allen's USE/COMPOSE/BUILD economic-decision frame"
    confidence: 0.7
  - type: supports
    target: 2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships
    via: "workflow-not-task as the unit of value capture; Beutler's team agents fill MGI's middle layer between workforce tools and top-down initiatives"
    confidence: 0.7
  - type: supports
    target: 2026-05-02-dutt-chatterji-ai-experimentation-to-transformation
    via: "same OpenAI vendor vantage; foundation-and-evals before automation; process redesign over task automation"
    confidence: 0.75
---

# Architecting AI-Native Organizations: How to Redesign Work at Scale — Joe Beutler

> Joe Beutler, Head of Solutions Engineering for Strategics at OpenAI, draws on firsthand experience inside OpenAI and across its largest enterprise customers to explain what structural changes actually enable AI-native organizations. He examines why most companies are stuck between broad workforce tools and a handful of top-down strategic initiatives—and what it takes to unlock automation at the team and department level. In this talk, you'll learn how to separate governance from transformation, why embedding engineering directly inside business functions is the key to scaling AI adoption, and how to use the Ask-Assist-Automate framework to move from early experiments to production-grade agentic workflows responsibly.
>
> *— [IT Revolution YouTube channel description](https://www.youtube.com/watch?v=fFOLWoHyWLE)*

A **~25-minute conference talk** by **Joe Beutler** (Head of Solutions Engineering, Strategics, at [[OpenAI]]; previously across all strategic accounts, now focused on financial services), introduced by **Gene Kim**, at the **IT Revolution Enterprise AI Summit: Spring 2026** (9–10 April 2026). It is the wiki's **first first-party [[OpenAI]] source** — answering the standing open question on the OpenAI entity page that "no first-party OpenAI source has been ingested yet." The vantage is **vendor-of-deployment, cross-customer**: Beutler sits across OpenAI's largest enterprise accounts and reports the structural patterns he sees working, plus how OpenAI is restructuring *itself*.

This source's structural value: it pairs the **inside-engineering** vantage of [[2026-05-08-running-an-ai-native-engineering-org|Fung / Anthropic]] (how *one lab* runs its own AI-native engineering org) with the **cross-customer deployment** vantage (the structural patterns a frontier-lab solutions team sees succeed across dozens of large enterprises). Where Fung names the team-norms rewrite *inside* Anthropic, Beutler names the **org-design prescription he watches land or fail across his customer base** — and introduces the **Ask → Assist → Automate** deployment-maturity ladder, a named framework new to the wiki.

## TL;DR

- **The enterprise AI adoption gap is a *middle-layer* gap.** Two approaches dominate today: **bottoms-up** (workforce tools like ChatGPT given to all employees) and **top-down** (one-to-three large strategic initiatives, e.g. call-center automation). What's missing is the middle — **team agents**: automation at the team and department level. Closing that middle layer is, in Beutler's framing, how you close "the big enterprise value gap that everyone keeps talking about." Maps directly onto the [[micro-productivity-trap]] and the [[enterprise-ai-adoption|adoption-depth gradient]].
- **Three things to architect an AI-native organization**: (1) **business leaders own the outcomes** (not central IT); (2) **engineering sits inside the business function**, close enough to the work to automate it; (3) use the **Ask-Assist-Automate** framework to start and scale responsibly.
- **Separate governance from transformation.** "You can't have the same person own transformation and governance, because one or the other tends to win out." Central IT owns foundations, firmwide governance, tooling, and the biggest cross-company initiatives; **business units own transformation in their own domain.** *"If the head of a business unit is not accountable for the result, you probably don't have an agent. You have a demo."*
- **The embedded-innovation evolution** ("moving centers of excellence to embedded innovation"): the path is *organic*, not a hire-an-eng-leader edict. A domain expert obsessed with AI builds tooling → colleagues adopt it → the role goes full-time → pair with an engineer → bring in a head of innovation. Three roles are load-bearing: **domain expert** (requirements / quality / edge cases), **AI expert** (project selection / evals / system behavior), **software engineer** (connects context, identity, telemetry). OpenAI's engineering org insisted embedded engineers be **interviewed by engineering and put on the same comp ladder.**
- **Ask → Assist → Automate** (deployment-maturity ladder): **Ask** = read-only (pull data, answer questions, validate sources before any write actions); **Assist** = agent recommends, human-in-the-loop validates; **Automate** = the things the agent always gets right stop going to humans, exceptions route to people. You cannot go zero-to-full-automation, especially in regulated environments. **The biggest value is at Automate, but it also demands the most integration, the highest quality bar, the strongest evals, and the most operational ownership.**
- **OpenAI's own wins**: finance team uses the API to extract/structure contract data → "millions of dollars of impact"; finance built a GPT that answered "thousands" of investor due-diligence questions during the fundraise; **PwC benchmarked OpenAI's finance team at only 20% of the size it should be** (vs both legacy and digitally-native comps). Go-to-market automated top-of-funnel (lead qualification, quote prep) for the SMB self-service segment.
- **Worked customer cases**, all on the same Ask→Assist→Automate pattern: a **large insurer** auto-claims agent; a **wealth-management** adviser agent; **T-Mobile** (wanted to automate its whole call center — a $3B cost center already 60% automated; OpenAI walked them back to start with Ask); **BBVA** building across customer service, an "AI banker," risk, and operations in parallel.
- **The next prize is no-code agent builders** — productizing agent creation (continuous evals + governance + connectors + shareable skills) so individuals build their own agents, explicitly *contra* a "massive professional-services business … lucrative contracts that will last 10 years."
- **Where to start**: a **workflow inventory** (map every workflow, track AI usage / frequency / time spent / opportunity), **pick your bets**, start with the experts already building, then elevate the winners from individuals to a centralized team that owns getting them to production.
- **Emerging role: the AI agent manager.** Agents need ongoing management (new products, new security concerns) the way people need training and enablement — Beutler expects this to become a full-time job.
- **Closing**: "If the last decade was about digitizing workflows, the next one will be about building and managing agentic workflows. And this is the real architecture question that is in front of all enterprises right now."

## What was actually ingested

Full ~25:25 transcript (cleaned from auto-generated English captions; ASR fixes for product/people names — *Joe Butler→Beutler*, *chatbt/chachib/chatt/chatg→ChatGPT*, *codeex→Codex*, *PWC→PwC*; section headings follow the eight YouTube chapter markers). No slides were captured (the talk references a self-made "eyesore" workflow-inventory slide and an org-evolution diagram, described in prose). The talk is a single conference session; the only hard numbers are the anecdotal benchmarks above ($3B / 60% / 20%-finance-team) — no systematic dataset is presented.

## Key claims, with quotes

### The middle-layer gap: team agents

> *"There's been this bottoms-up approach where people are providing workforce tools like ChatGPT to their employees … and then from the top down there are these large strategic initiatives … But what's been missing is what's in the middle, which is this concept of team agents … how can you have more automation at the team and department level."*

This is Beutler's framing of the [[enterprise-ai-adoption|enterprise value gap]]: breadth (everyone has a chatbot) and a few marquee initiatives, but a hollow middle. It is the vendor-of-deployment restatement of the [[micro-productivity-trap]] — task-level tools and a couple of top-down projects don't aggregate to firm value; the team/department layer is where workflow-level automation actually compounds. Converges with [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|MGI's]] workflow-as-unit-of-value-capture and [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS's]] "AI bolted on is going to fail … focus at a workflow level."

### Business owns the outcomes; governance ≠ transformation

> *"You can't have the same person own transformation and governance, because one or the other tends to win out … if the head of a business unit is not accountable for the result, you probably don't have an agent. You have a demo. Central IT should own the foundations … but the business units need to own the transformation in their own domain."*

The sharpest single articulation in the wiki of the **governance/transformation split**. It complements [[2026-05-03-rewired-second-edition-sample|McKinsey Rewired's]] "operating model: business, tech, and operations closer together" and "we don't have a single success story where senior business leaders were not in the driver's seat," and operationalizes the *accountability-must-be-personal* prescription from [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al.]].

### Embedded engineering and the three-role team

> *"You need a domain expert who defines the requirements, the quality and the edge cases … an AI expert who advises on project selection, sets up the evals, and establishes system behavior … and a software engineer who can connect the context, the identity, and the telemetry."*

The embedding is **organic and HR-load-bearing**: a seller "obsessed with AI" built tooling, colleagues adopted it, the role went full-time, then was paired with an engineer (interviewed by engineering, on the same comp ladder), then a head of innovation was hired. This is the worked mechanism behind Gene Kim's introduction claim that OpenAI has "embedded engineering managers throughout the company" reporting to the CFO and CRO. It is the cross-customer-deployment twin of [[2026-05-08-running-an-ai-native-engineering-org|Fung's]] inside-Anthropic team-shape rewrite — both land on *engineering moves to where the domain work is*.

### Ask → Assist → Automate (the deployment-maturity ladder)

> *"It's really hard to go from zero to full automation … you have to start with a strong foundation with evals and governance. You start with **Ask** — read-only operations … then **Assist** … the agent recommends … the human in the loop to validate … then you naturally end up at the **Automate** phase."*

A clean three-rung ladder that maps onto the wiki's [[automation-vs-augmentation]] axis: **Ask** and **Assist** are *augmentation* (human does the work, agent reads / recommends), **Automate** is *automation* (agent acts, exceptions route to humans). The **T-Mobile** case anchors it: a $3B call-center cost center, already 60% automated, with ambitions to automate 75% — OpenAI "got them to come back a little bit" and start at Ask. The **flywheel** claim: start by building tools that *help people do their job*; once they see value they give feedback; value grows quickly then "exponentially as you unlock each new level."

### The biggest value, and its cost, live at Automate

> *"The biggest value is obviously at Automate. But that is also where you have the most integration, the highest quality bar, the strongest evaluations, and the most operational ownership from the people doing the job today."*

This is the responsible-scaling caveat that distinguishes Beutler's framing from a naive "automate everything" reading — and it is why the [[agent-harness|harness layer]] (evals, governance, connectors, skills) is the binding constraint, not model capability: *"the bottleneck is rarely the model capability … it is org design, ownership, and workflow clarity."*

### No-code agent builders as the next prize

> *"One of the biggest prizes I see right now in enterprise AI is these no-code agent builders … We don't have a massive professional services business … We're trying to enable each individual to figure out how to use AI on their own and build these things for themselves … an agent-building platform that's no-code, has continuous evaluation, has all the governance you need to get through your IT security, connectors that tie into the different data sources that matter, and provides skills."*

The wiki's first vendor-side statement of **harness-as-a-service from OpenAI specifically** — the productization move the [[2026-05-05-loukides-radar-trends-may-2026|May 2026 Radar Trends digest]] tracked across five vendors in a single month ("AI is becoming operational"). The explicit *anti-professional-services* stance is a notable contrast with the services-company thesis in [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren / YC]] — OpenAI wants to sell the *builder*, not the *outcome-as-a-service*.

### Workflow inventory + the emerging AI-agent-manager role

> *"We identified all of the different workflows that make up the job we do today … how often … how much time … where there's an opportunity to get to more assisted AI functions or full automation … you can't build all of these at once, so you have to pick your bets."*

> *"We're starting to move toward a world where part of someone's job is as an AI agent manager … we could see this becoming a full-time job."*

The workflow-inventory method is the operational complement to [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Brooklyn Solutions' frequency × variability]] use-case discovery. The **AI-agent-manager** role is a forward-looking labor-market signal for the [[ai-employment-effects]] cluster: agents, like employees, need ongoing enablement and quality management.

## Dynamic-capabilities reading (Warner & Wäger)

This source sits squarely in the digital-transformation lens; it touches five cells of the [[concepts/warner-wager-process-model|Warner & Wäger process model]]:

- **`digital-transforming/redesigning-internal-structures`** *(core)* — the entire talk is about **designing team-based structures**: "moving centers of excellence to embedded innovation," embedding engineering inside finance / go-to-market, hiring a head of innovation. This is the cell's canonical "designing team-based structures" activity at AI-native altitude.
- **`digital-transforming/improving-digital-maturity`** — the **enablement problem** ("people need to know how to use the tools so they can recognize how to automate their own workflows"), shifting domain experts into AI-builder roles, recruiting engineers onto the same comp ladder, and the emerging **AI-agent-manager** role all instantiate "identifying digital workforce maturity" and "leveraging digital knowledge inside the firm."
- **`digital-seizing/balancing-digital-portfolios`** — "you can't build all of these at once, so you have to pick your bets," elevating winners from individuals to a centralized team, and **setting an appropriate speed of execution** (walking T-Mobile back from straight-to-Automate) are textbook portfolio-balancing and pacing decisions across dozens of candidate use cases.
- **`digital-seizing/rapid-prototyping`** — the domain expert "tinkering and building tools for the team," dedicated **innovation teams**, and the no-code agent-builder vision map onto "creating minimum viable products" / "using a digital innovation lab."
- **`contextual/internal-enablers`** — **executive support** (CFO/CRO sponsoring embedded engineering) and **cross-functional teams** are named as the enablers that make the embedded-innovation pattern work; "business leaders own the outcomes" is the executive-support enabler made into a structural rule.

(Roles inherited from the cell defaults — no override. The union spans `ceo, cfo, cso, cdo, cio, chro, cto, product-manager, tech-lead, innovation-lab-lead, transformation-lead`, consistent with the talk's explicit address to CFOs, CROs, central IT, and the new embedded-engineering / head-of-innovation roles.)

## Cross-source positioning

| Source | Construct | What this Beutler talk adds |
|---|---|---|
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung / Anthropic 2026]] | AI-native org: team-norms rewrite *inside one lab* | The **cross-customer deployment twin** — the org-design prescription a frontier-lab solutions team watches succeed or fail across dozens of large enterprises; both converge on *embed engineering, business owns outcomes*. |
| [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures\|Allen / AWS 2026]] | USE / COMPOSE / BUILD economic-decision frame; workflow-level focus | **Ask → Assist → Automate** is the *deployment-maturity* complement to Allen's *economic-decision* frame; both name workflow-level focus and right-team-composition as the 5%-that-succeed pattern. |
| [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships\|Yee et al. / MGI 2025]] | Workflow-as-unit-of-value-capture; 190+ workflows across 16 functions | Beutler's **team-agents middle layer** is the org-altitude name for the gap MGI quantifies; "dozens of use cases per department" is the workflow-redesign mandate in vendor-of-deployment voice. |
| [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|Dutt, Chatterji et al. 2026 (Bain/OpenAI)]] | Micro-productivity-trap; 4-step transformation; evals | **Same OpenAI vendor vantage**; *foundation-and-evals before automation* is the Ask-phase restatement of "reimagine workflows" + "measure with evals." |
| [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company\|Warren / YC 2026]] | Outcome-as-a-service vendor playbook | **Contrast**: Warren sells the *outcome*; Beutler explicitly *rejects* the professional-services/outcome model in favor of selling the **no-code builder** so customers build their own agents. |
| [[micro-productivity-trap\|micro-productivity-trap]] | Task gains don't aggregate to firm value | Names the *structural* remedy (team agents + embedded engineering + business-owned outcomes) rather than the diagnostic. |

## Linked entities and concepts

**Existing pages (touched or referenced):**

- [[OpenAI]] — heavy: first first-party OpenAI source; adds the internal finance/go-to-market wins, the PwC 20%-finance-team benchmark, the embedded-engineering-managers structural claim, and the no-code-agent-builder direction. Answers the entity's standing open question.
- [[enterprise-ai-adoption]] — heavy: the team-agents middle layer, governance-vs-transformation split, embedded engineering, Ask-Assist-Automate, workflow inventory, AI-agent-manager role.
- [[automation-vs-augmentation]] — moderate: Ask/Assist = augmentation, Automate = automation; the ladder is a deployment-maturity progression along the axis.
- [[micro-productivity-trap]] — moderate: the middle-layer gap is the structural cause of task-gains-without-firm-value.
- [[agent-harness]] — light/moderate: evals + governance + connectors + skills = harness-as-a-service; "the bottleneck is rarely the model."
- [[ai-agents]] — light: team agents, agentic systems, the Ask/Assist/Automate operating modes.
- [[concepts/warner-wager-process-model|warner-wager-process-model]] — the five tagged cells above.

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):**

- *Joe Beutler* — speaker (Head of Solutions Engineering, Strategics, OpenAI; financial-services focus). Promote on second-source mention.
- *Gene Kim* — introducer (IT Revolution / DevOps Enterprise founder, author). Promote on second-source mention.
- *IT Revolution* — channel / publisher (Enterprise AI Summit host). Promote on second-source mention.
- *T-Mobile*, *BBVA*, *PwC* — organizations named in case studies / benchmarks (not authors). Candidate future entities if they recur; out of scope for author-promotion.
- *Enterprise AI Summit: Spring 2026* — the event/venue. Promote if a second source from the same event lands.

## Source-quality flag

- **Strengths**: the wiki's **first first-party OpenAI source** and first cross-enterprise vendor-of-deployment vantage from OpenAI's solutions side; high operational density (every section names a concrete structural practice); introduces a named framework (Ask-Assist-Automate) absent from the wiki; resonates with multiple independent 2026 sources at different altitudes (Fung engineering-internal; Allen/AWS economic-decision; MGI workflow-quant; Bain/OpenAI transformation) without re-citing them.
- **Caveats**: vendor talk by an interested party (OpenAI sells the API, GPTs, and the future no-code builder Beutler is promoting); auto-generated transcript (ASR-cleaned); hard numbers are anecdotal ($3B / 60% / 20%-finance-team, "millions of dollars," "thousands of questions") with no systematic dataset; customer cases are described without independent verification.
- **Per CLAUDE.md §Lifecycle**: baseline 0.70 (single supporting source for the embedded-engineering + Ask-Assist-Automate specifics) + 0.05 for strong cross-source resonance with already-ingested 2026 sources at multiple altitudes. Vendor-sponsored single case-talk → held at/below the 0.75 ceiling for non-replicated single sources. **Confidence: 0.75.**

## Open questions for the wiki

- **Ask-Assist-Automate as a candidate concept page.** If a second source names the same (or a structurally equivalent) deployment-maturity ladder, promote it from a body section to its own concept page and add it to the [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks synthesis]] as a standalone framework.
- **Second OpenAI first-party source.** This is the first; a second would let the wiki triangulate OpenAI's vendor framing (and would promote Joe Beutler / IT Revolution / Gene Kim from dangling to entity).
- **The AI-agent-manager role.** A forward-looking labor-market claim; worth tracking whether a job-market or survey source confirms it materializing.
- **No-code-builder vs outcome-as-a-service.** Beutler (OpenAI) bets on selling the builder; [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren / YC]] and [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria]] bet on outcome-as-a-service. Which vendor model dominates which market is an open strategic question the wiki can track.
