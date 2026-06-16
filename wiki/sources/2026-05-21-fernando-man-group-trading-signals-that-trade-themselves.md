---
type: source
kind: video
title: "Trading signals that trade themselves"
author: ["Claude"]
publisher: "Anthropic (Claude YouTube channel — Code with Claude conference talk; Tushara Fernando / Man Group head of data and AI)"
url: "https://www.youtube.com/watch?v=EOg4gY0Yln0"
date_published: 2026-05-21
date_ingested: 2026-05-21
length: "~20:45 minutes (auto-generated English captions; ASR-cleaned, 157 segments)"
raw: "../../raw/videos/trading-signals-that-trade-themselves.md"
tags: [man-group, tushara-fernando, anthropic, claude-code, code-with-claude, systematic-trading, signals, backtesting, skills-governance, skills-marketplace, knowledge-context-as-moat, regulated-financial-services, hedge-fund, ai-native-vendor, organizational-context, enterprise-scale, expense-report-failure-mode, customer-story]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "**The enterprise-scale empirical worked example of Tan's skills/skillify/check-resolvable framework.** Tan / CS153 names skills as employees, resolvers as the org chart, skillify as the 10-step compliance protocol, check-resolvable as audit; Fernando / Man Group is the **1,700-person regulated-financial-services worked example** showing what each of those primitives is for when adopted at enterprise scale. The **expense-report failure-mode story** (~9:32–10:42) — a power user wrote a skill for himself, hardcoded his cost-center code, shared with team; expense approver in sales suddenly got everyone's reports because nobody had reviewed that skill — is the wiki's clearest empirical worked example of *what goes wrong without check-resolvable / trigger-eval / skillify discipline.* Fernando's distinction between **power users vs process owners** writing skills, and her solve (knowledge marketplace; every skill visible, tagged, tested with evals, owned by workflow owner, lifecycle-managed) is the **operational instantiation** of what Tan asserts is structurally identical to a company's org chart + audit + performance reviews."
  - type: supports
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "**The vendor-CEO three-layer continual-learning model (Chase) operationalised in regulated finance (Fernando).** Chase / Interrupt 26 names model / harness / context as three independently improvable layers; Fernando's *'organizational context is your IP, it's your moat, it's one of the few safe spaces left in AI — the frontier labs are not going to solve context for you'* is the wiki's strongest enterprise-vantage articulation of why **context is the value layer Chase asserts**, with explicit *'decades of institutional knowledge'* as the underlying substrate. Same shared assertion (skills = how decades of institutional knowledge become leverage) from independent vantages: Chase as the vendor-CEO building the platform, Fernando as the enterprise customer running it on production financial workflows."
  - type: supports
    target: 2026-05-19-garg-yc-internal-ai-agent-evolves-itself
    via: "**Two-FTE-startup-micro-scale (Garg) ↔ 1,700-employee-enterprise-scale (Fernando) endpoints of the same self-extending-skills-platform thesis.** Garg builds the self-extending Claude Code harness with agent-editable instructions.md and 45+ self-authored CLIs at 2-FTE / $2M ARR; Fernando builds the governed skills marketplace with 100+ governed skills + lifecycle management at 750-of-1,700-people regulated-financial-services scale. **Both arrive at the same conclusion**: the connective layer is what the frontier labs cannot give you — your workflows, your data, your institutional knowledge. Different scales, different governance demands (compliance-driven for Fernando, founder-led for Garg), same architectural pattern."
  - type: supports
    target: 2026-05-13-jha-emergent-democratizing-app-building-with-claude
    via: "**Claude-channel customer-story cluster extension** at the regulated-enterprise vantage. Jha (Emergent, 13 May) lands the *adoption-velocity-asymmetry-favouring-the-long-tail* on the Claude channel from the SMB / non-coder vantage ($100M ARR / 8 months / 7M users / 70-80% never wrote a line of code); Fernando (Man Group, 21 May) lands the *organizational-context-is-the-moat* claim from the opposite enterprise vantage ($200B AUM regulated investment manager / 750-of-1,700-people on Claude Code / production trading signals proposed by AI). **Same Claude-channel customer-story cluster, opposite ends of the customer-size + regulatory-burden spectrum** — both ratify the *skills/context as the layer where the value sits* thesis from different operational conditions."
---

# Fernando — Trading signals that trade themselves (Code with Claude)

> There are trading signals in production at Man Group right now — running real capital — that were researched, backtested, and proposed by AI. Tushara Fernando shares what made that possible inside a regulated investment firm: a governed skills framework and core data layer that taught Claude Code how Man Group's quants have worked for decades, now scaled across ~750 developers and quants and 100+ skills. Walk away with the governance model that lets compliance say yes to AI on your most load-bearing workflows.
>
> — channel description, Claude

## TL;DR

A ~20:45 [[Anthropic]] *Code with Claude* conference talk (published 2026-05-21 on the Claude YouTube channel). Speaker: **Tushara Fernando**, head of data and AI at **Man Group** — an alternative investment manager managing over **$200 billion of assets** for pension funds, sovereign wealth funds, and large institutions. *"Our clients are real people — teachers in Canada, metal workers in Japan. So we really need to get AI right. If we get this wrong, we could lose real money."*

**The headline empirical claim** (~4:38–5:13): *"There are trading signals running right now in production at Man Group, a regulated investment firm running real capital, that were researched, backtested, and proposed by AI. AI came up with the idea. AI got the data. AI ran the backtest. AI then wrote up the strategy proposal and AI productionised the signal. Humans of course reviewed all of the output to make sure that it was sensible. But AI was at the center of that process."*

**The substantive contributions are four.**

**1. The expense-report failure-mode story (~9:32–10:42)** — the wiki's clearest empirical worked example of *what goes wrong with ungoverned skills*. After Anthropic-led skills workshops, hackathons, blog posts, and show-and-tell sessions drove enthusiastic adoption, *"we started to see cracks in our approach. It was really the power users that were building the skills. It wasn't the process owners."* The vignette:

> *"There was a guy who used to travel a lot at Man Group and he had loads of expenses to do and he spent loads of time doing this. So he wrote a skill for it. He gave lots of pictures of receipts to Claude and it would do the expense report for him and he brought this to the show-and-tell session and he even shared it with a few people in his team and it was working really well. And then a few days later, the expense approver came to us and was like, 'Why is Claude creating so many expense reports for my cost center? People from technology, people from the people team. Why do I have to approve all of them? I'm in sales. I don't want to approve everybody else's expense reports.' And we dug into it and it was just because the cost center code was hardcoded... Nobody had reviewed that skill. It worked for him. It worked for his team, so it was going to work for everybody. But that's not the case. And he wasn't accountable for that. He kind of thought it was quite funny. And I mean, so did I, to be honest."*

This is the most concretely-described instance in the wiki of why [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan's]] *skillify* 10-step protocol exists — unit tests + LLM evals + integration test + resolver entry + trigger eval + **check-resolvable** + smoke test + schema. *"People were just codifying their ways of doing things. They weren't the organizational ways of doing things. And in many cases, they weren't actually the workflow owner."*

**2. Knowledge marketplace as the governance solve (~11:36–13:14).** Fernando's solution to the *"power-users vs process-owners writing skills"* problem:

- **Every skill visible, tagged, tested with evals.**
- **The skill is owned by the workflow owner** (not the power user who wrote it).
- **Usage is tracked. They're all reviewed. They have a lifecycle. And they're all visible to everybody to install.**
- **Plugins as useful groups of skills** — e.g., a *data plugin* gives access to Man Group's datasets.
- **Knowledge marketplace UI**: *"This is My Knowledge. It's where you'll find our collection of skills and Man Group's context store. The skill suggestions are tailored to each business unit. They have clear ownership and are organized into managed and community skills."*

The **organisational-library framing**: *"Imagine a library. It captures decades of institutional knowledge. There are sections for the finance department, the people department, the research department. We care for every item. We care for every skill in those departments... It's really that care that makes this work."*

**3. The systematic-trading worked example (~13:20–16:01).** A 4-skill workflow that Fernando demos:

- **Alternative datasets skill** — search for relevant data sources (e.g., credit card data).
- Claude identifies a dataset of US consumer transactions.
- Plot Amazon's monthly credit card spend against stock price returns; spikes at Black Friday and Christmas.
- **Backtest skill** — *"investing $1,000 in 2021 using this signal would now be worth around $2,500"* — better than buy-and-hold for Amazon.
- **Distributed compute skill** — run on a broader universe of retail companies; each company as an individual worker; findings collected.

Fernando notes the production version is much more nuanced (seasonality, inflation, broader securities), and *"we do this with agents as well as humans exploring these ideas. The key takeaway is that the governance of these skills is key."*

**4. Organisational context as IP / moat (~16:47–17:21) — the load-bearing rhetorical claim.**

> *"Focus on that organizational context. **That is your IP. It's your moat. It's one of the few safe spaces left in AI.** The frontier labs are not going to solve context for you. It's not on the internet. They don't know your workflows. And you already have that context. You have decades of it. The work is on exposing it, not reinventing it. And skills are how those decades of institutional knowledge become leverage."*

This is the wiki's most-direct statement that the value layer in 2026 AI is **enterprise-specific context** (not the model, not the harness, but the workflows-and-data substrate the harness operates over). It maps directly onto [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase's]] *model / harness / context* three-layer continual-learning model — Fernando is asserting that the **context layer is where the moat sits** at enterprise scale.

**The scale of adoption** (~18:20–18:53): Man Group has roughly **1,700–1,800 people**; **750 of them use Claude Code** across developers, quants, the people team, the finance team. *"Everybody across all of the departments is using Claude Code."* **100+ governed skills + at least as many community skills.**

**Closing lessons** Fernando would tell past-me:

- *Focus on organisational context — that is your IP, your moat.*
- *Treat skills like production code, because that's what they will become.*
- *Plan your approach before you plan the rollout — who owns the skill? who reviews? how does it get retired? how does it get tested? Decide this before shipping the first skill, not after the hundredth like us.*
- *Adoption is not a licensing problem. It's a people problem.*

**Caveats.** Vendor-marketing channel (Anthropic's Claude YouTube). Every metric is vendor-cited by an Anthropic customer speaking at Anthropic's own conference; the production-trading-signal claim is the most consequential and unfalsifiable from outside (Man Group's IP not disclosed). The *750-of-1,700 / 100+ governed skills* numbers are concrete-enough to be checkable against Man Group internal reporting if it ever surfaces. The Anthropic-led workshops + hackathons + blog + show-and-tell are explicitly named as the adoption-driving mechanism, but also as the cause of the *power-user-not-process-owner* anti-pattern — the lesson is *governance has to come before adoption*, not after.

## Why this matters in the corpus

This source is the wiki's **strongest enterprise-scale empirical anchor on the skills-governance thesis**. The wiki already holds the framework at three altitudes:

| Altitude | Source | Contribution |
|---|---|---|
| **Founder-CEO altitude** | [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]] | Skills as employees, resolvers as org chart, skillify as 10-step compliance protocol, check-resolvable as audit, trigger evals as performance reviews — the rhetorical decomposition |
| **Vendor-CEO altitude** | [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] | Model / harness / context three-layer continual-learning model with evals-as-gradient — the product framing |
| **Startup-micro-scale** | [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / AnswerThis]] | $2M-ARR / 2-FTE self-extending Claude Code harness with agent-editable instructions.md — the smallest scale where the pattern works |
| **Enterprise-scale** (this source) | **Fernando / Man Group** | **750-of-1,700 regulated-financial-services scale with 100+ governed skills and production trading signals** — the largest scale where the pattern has been operationalised in the wiki's corpus |

The Fernando ingest **closes the scale-ladder** for the skills-as-the-enterprise-context-layer thesis. The four sources together let the wiki name *skills governance as a 2026 vendor + customer-side cluster*: the rhetoric is from YC's leadership; the framework is from LangChain's CEO; the smallest worked example is YC portfolio at 2-FTE scale; the largest is a regulated-financial-services hedge fund at 1,700-person scale.

**The expense-report story is the wiki's clearest empirical anchor on the failure-mode.** Tan's CS153 framework predicts that check-resolvable + skillify exist *because* skills written by power-users go wrong; Fernando provides the specific scenario. Future ingests citing *why skills governance matters* should anchor here.

## What was actually ingested

The full ~20:45 transcript was read end-to-end. The transcript renders **Man Group** consistently as *"Mang Group"* / *"Mangroup"* and **Tushara** as *"Tashara"* — both ASR artefacts, corrected against the channel description in attribution.

The talk is delivered at the [[Anthropic]] *Code with Claude* conference (the same conference that hosts the [[2026-05-08-running-an-ai-native-engineering-org|Fung]] keynote on AI-native engineering org structure). Fernando's slide deck includes a knowledge-marketplace UI screenshot and a systematic-trading demo video; both are described in voice but the visual content is not captured.

## Linked entities and concepts

**Entities promoted by this source:**

- [[Anthropic]] — channel; already entity. Bumps source-count.

**Dangling — single-source mention, deferred:**

- **Man Group** — $200B AUM alternative investment manager; ~1,700–1,800 people; 750 use Claude Code; 100+ governed skills. First wiki mention; promote on second substantive source.
- **Tushara Fernando** — head of data and AI at Man Group. First wiki mention.
- **Code with Claude** — Anthropic's annual conference; the wiki has now received two ingests from this conference ([[2026-05-08-running-an-ai-native-engineering-org|Fung]] and this Fernando talk), but they were filed on different operational vantages so the conference itself remains a Dangling-as-a-venue first-mention.

**Concept pages touched:**

- [[concepts/agent-harness]] — adds the **enterprise-skills-governance worked example** at 1,700-person regulated-financial-services scale; the *expense-report failure-mode* as the empirical anchor on why check-resolvable / trigger-eval / skillify protocols exist; the *power-users vs process-owners* distinction in skill ownership.
- [[concepts/enterprise-ai-adoption]] — adds the **750-of-1,700 / 100+ governed skills / production trading signals** Man Group operational metrics; the *adoption-is-a-people-problem-not-a-licensing-problem* lesson; the *organisational-context-is-your-IP* moat thesis at enterprise scale.
- [[concepts/agentic-engineering]] — adds Fernando's *treat skills like production code* lesson — agent-tooling-as-software-engineering-discipline at enterprise scale.
- [[concepts/foundation-models]] — Fernando's *"the frontier labs are not going to solve context for you"* is a vendor-customer-side articulation of the foundation-model-as-substrate framing: models are commodity, context is moat.

## Source quality

- **Channel**: [[Anthropic]] Claude YouTube — official Anthropic vendor channel.
- **Format**: ~20-minute conference talk with slides; manual ASR-cleaned captions.
- **Empirical anchors**: $200B AUM (verifiable from Man Group public disclosures); 1,700–1,800 employees (rough self-report); 750 Claude Code users; 100+ governed skills + similar number of community skills (vendor-customer self-report). **The production-trading-signal claim** is the most consequential and least verifiable — Man Group's IP is intentionally undisclosed.
- **Bias / motive**: Anthropic customer speaking at Anthropic's annual conference; treat the *"we trust Claude Code with production trading signals"* claim as motivated but consistent with the rest of the talk's operational detail.
- **Transcript provenance**: youtube-transcript-skill (Playwright path); ASR-only auto-captions used (no manual captions available). Standard rolling-caption dedupe was a no-op on this transcript shape.
