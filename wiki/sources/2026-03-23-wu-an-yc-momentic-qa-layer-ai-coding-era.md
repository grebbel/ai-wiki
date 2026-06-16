---
type: source
kind: video
title: "The Q/A Layer for the AI Coding Era"
author: ["YC Root Access"]
publisher: "Y Combinator (YC Root Access channel — Founder Firesides episode with Harj Taggar interviewing Weiwei Wu & Jeff An / Momentic)"
url: "https://www.youtube.com/watch?v=UpWNdSVWA7M"
date_published: 2026-03-23
date_ingested: 2026-05-22
length: "~33:54 minutes (auto-generated English captions; ASR-cleaned, 328 segments)"
raw: "../../raw/videos/2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era.md"
tags: [momentic, weiwei-wu, jeff-an, harj-taggar, notion, simon-last, quora, robinhood, qa-vertical-ai, functional-testing, verification-layer, truth-driven-development, spec-driven-development, code-as-implementation-detail, mcp-integration, claude-code, cursor, codex, playwright, selenium, ten-x-engineer-counter, sapphire-or-standard-capital, founder-firesides, yc-root-access, y-combinator, founder-vantage]
dynamic_capabilities:
  - digital-sensing/identifying-needs
  - digital-seizing/strategic-agility
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "Momentic's *closing-the-feedback-loop-for-the-coding-agents* framing operationalises Chase's three-layer continual-learning model (model/harness/context) at the **external-validator vendor-product altitude**. Wu: *'In a sense, it's like we're closing the loop for feedback for the coding agents... I can't really trust Claude Code or Cursor to tell me themselves. I need a third external source of truth.'* This is Chase's *evals-as-gradient* claim restated as a vendor-product wedge — Momentic sells the eval-substrate that lives outside the coding agent's own self-report, integrated as an MCP-tool that Cursor and Claude Code can call to verify before merge. Wiki's first founder-vantage worked example of *evals-as-gradient* as a *standalone-vendor* product shape, complementing Chase's vendor-CEO-stage articulation."
    confidence: 0.85
  - type: contradicts
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "**Productive tension on the *1,000× engineer* thesis.** Tan & Hu (CS153, 20 May 2026): *the 1,000× engineer* prescription — one founder with Claude Max plan replicates 10 people / $4M / 2 years of legacy work in 5 days. Wu (Momentic, 23 March 2026): *'Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with'* — a direct counter-claim that the multiplier is **conditional on the engineer's pre-AI baseline**, not unconditionally available. Wu's claim came two months before Tan & Hu's CS153 framing, but the rhetorical inversion is exact. The wiki now carries paired founder-vantage anchors on **whether AI is a force-multiplier on existing skill or a leveller across skill levels** — productive contradiction filed for the [[concepts/agentic-engineering|agentic-engineering]] page's debates-and-supersession section."
    confidence: 0.7
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "Wu's *truth-driven / spec-driven development* framing — *'code is just an implementation of that source of truth... your code is just an implementation detail. They're just implementation details to me. All I care about is the end user journey, the end success criteria that I've spec'd out'* — is the **vendor-product instantiation** of Chase's [[concepts/agent-development-lifecycle|ADLC]] *evals* phase as load-bearing primary artifact. Both Chase and Wu converge on: the spec / eval set, not the code, is the durable system-of-record. Momentic operationalises this by making the spec the source-of-truth and *automatically maintaining that source of truth over time* including suggesting changes when new UI components appear."
    confidence: 0.75
  - type: supports
    target: 2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals
    via: "Twin **YC Root Access enterprise-vertical-AI Founder Firesides** with parallel pivot-and-vertical-wedge templates. Both founders pivoted from horizontal developer-adjacent tooling (Momentic: started in 2023 as Cursor-for-unit-tests-style tools / Luminai: started as documentation-for-engineers) to vertical-specific applications (Momentic: QA-as-vertical / Luminai: healthcare-admin-as-vertical). Both anchor on a marquee enterprise customer (Momentic: Notion → ~500K test runs/day / Luminai: Cleveland Clinic). Both founders narrate **founder-led customer-acquisition through a single high-trust contact** (Momentic: Simon Last's Twitter post → 10pm DM → onboarded that night / Luminai: warm-intro discipline + LinkedIn-contact-scraping script). The YC-Root-Access founder-fireside cluster now spans healthcare-ops + sales-enablement + QA across three published episodes."
    confidence: 0.7
  - type: supports
    target: 2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack
    via: "Momentic's MCP-integration design — Cursor / Claude Code call Momentic as a tool-call during development to verify functional correctness, with *'the average step for us runs in under 300 milliseconds'* — is the **vendor-side complement** to Tan's GStack *Office Hours / Adversarial Review / Code Review / SLQA / Ship* skill pipeline. Where GStack composes skills inside the agent harness, Momentic provides an external skill-shaped tool-call (start a real browser, verify the user flow works) that those harnesses can use. Wiki's emerging picture: the AI-coding-era dev loop has both **internal skills** (GStack-style harness primitives) and **external verifiers** (Momentic-style MCP tools) — both composable via MCP, both improving the harness layer in Chase's three-layer model."
    confidence: 0.65
  - type: supports
    target: 2026-02-19-trivedy-langchain-anatomy-of-an-agent-harness
    via: "Wu's *'I can't really trust Claude Code or Cursor to tell me themselves. I need a third external source of truth'* is a founder-vantage application of Trivedy's *harness-is-load-bearing* thesis at the **verification-substrate** layer. The harness inside the coding agent is necessary but not sufficient for confidence; an external harness (Momentic's functional-testing harness) provides the independent eval gradient that the coding agent's self-report cannot. The wiki's pattern is now: **multi-harness-stack** — coding-agent harness (writes the code) + verification harness (validates it) — with MCP as the inter-harness protocol."
    confidence: 0.7
---

> *In this episode of Founder Firesides, YC Managing Partner Harj Taggar talks to Weiwei Wu and Jeff An, co-founders of Momentic (W24), who just raised a $15M Series A. Momentic is the verification layer for software — an AI-powered testing platform that impersonates end users to catch bugs before they ship. Powering companies like Notion, Quora, and Built with over a million test runs a day, they discuss why the explosion of AI-generated code makes testing more critical than ever and their vision for a future where engineers write specs, not code.*

# Wu & An / YC — Momentic as the verification layer for the AI coding era

[[Harj Taggar]] (YC Managing Partner) interviews [[Weiwei Wu]] and [[Jeff An]], co-founders of [[Momentic]] (YC W24), on YC Root Access — Founder Firesides episode, published 23 March 2026, ~34 minutes. Frames a $15M Series A announcement led by *Standard Capital*; Momentic is positioned as the **verification layer for software** — an AI-powered functional-testing platform that impersonates end users, powering Notion, Quora, Built, Zero, and others at *over a million test runs a day*.

## TL;DR

- **Verification-layer-for-software wedge**: Momentic does **functional testing** — *"acting, impersonating one of your users actually going through your app and clicking through and making sure all of the user flows that I can achieve are actually working."* Wedge against legacy tools (Selenium, Cypress, Playwright) on flakiness and maintenance cost; differentiator vs. raw browser-control LLM agents on speed (~300ms per step) and debuggability.
- **MCP-integration as the dev-loop product surface**: customers have Cursor / Claude Code call Momentic during development as a tool-call. *"Their change is going to impact production in some way. We just make sure that everything that they care about doesn't break."* Wiki's clearest founder-vantage worked example of *third-party verification harness as an MCP-callable from inside a coding agent.*
- **The truth-driven / spec-driven development thesis as load-bearing rhetorical claim**: Wu's two-schools-of-thought articulation — *"your code is the source of truth"* (status quo) vs. *"truth-driven development / spec-driven development... the spec is the source of truth. Your code is just an implementation of that source of truth."* In Wu's near-future, the engineer *"would actually just be writing specs and detailing edge cases, success criteria, that's for these AI agents to build. I don't really care if they're using TypeScript or Rust or anything like that. They're just implementation details to me."*
- **Productive contradiction with the 1,000×-engineer thesis**: *"Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with."* Counter to Tan & Hu's CS153 (May 2026) framing of unconditional multiplier; Wu argues the multiplier is **conditional on the engineer's pre-AI baseline skill** — adaptability, ambiguity-navigation, curiosity, passion.
- **Notion onboarding via Twitter-DM-at-10pm anchor anecdote**: *"Simon from Notion actually was posting on Twitter... 'It'd be great if I could just describe this and test it for me.' A lot of people recommended Momentic. I was in San Francisco actually that evening at 10pm. I DM'd Simon — Simon Last — and I was like, 'I think we've built exactly what you want. I can onboard you tonight.'"* Now Notion runs *"almost half a million test runs a day"* on Momentic and *"Momentic tests must pass before one of Notion's engineers can merge their PR."*
- **The closing-the-loop-for-coding-agents framing**: *"In a sense, it's like we're closing the loop for feedback for the coding agents... I can't really trust Claude Code or Cursor to tell me themselves. I need a third external source of truth."* The wiki's clearest founder-vantage articulation of **independent-eval-as-a-product** rather than as a tool the customer assembles internally.

## What was actually ingested

The full ~34-minute transcript (auto-generated English captions, ASR-cleaned). Light cleanup: ASR mis-transliterations of names ("Mantic"→"Momentic", "Weiwayi"→"Weiwei", "Kora"→"Quora", "claw MD"→"CLAUDE.md", "codeex"→"Codex", "playright"→"Playwright"); minor terms ("llinters"→"linters", "customerf facing"→"customer-facing", "PC process"→"POC process", "SES"→"SEVs", "agentto agent"→"agent-to-agent"). Stage cues retained.

**Discrepancy note on the round size**: the channel description states *"$15M Series A"*; on-stage the speakers say *"$50 million Series A"*. The wiki uses the description figure ($15M) as canonical — the channel description is the author-authoritative artefact and a *fifteen / fifty* ASR mistranscription is plausible. Lead investor named on-stage as *"Standard Capital"* (preserved verbatim from ASR; not externally verified at ingest time).

Full raw at [`raw/videos/2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era.md`](../../raw/videos/2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era.md).

## Substantive content

### 1. The verification-layer wedge (1:31–7:24)

The category framing. Wu opens with a primer on testing: *"if I'm shipping code, how do I make sure my app isn't broken?"* Existing options are inefficient (manual click-through) or expensive (engineering time on automation). Momentic specifically does **functional testing** — impersonating an end user clicking through user flows — and slots between linters/code-review (which only check the code) and production deployment.

The differentiator against **legacy tools** (Selenium, Cypress, Playwright): flakiness from selector-fragility, especially in flexible products like Notion (*"a rich text editor, everything's a database — but all of those things are also very difficult to test with Selenium"*). Maintenance cost: *"100,000 lines of Playwright code, and whenever you change your feature in a meaningful way, now you have 50K lines that you have to find and update."* Momentic encapsulates that maintenance — automatically maintaining the source-of-truth tests over time, *"suggesting changes to what your source of truth should be"* when new UI components appear.

The differentiator against **raw browser-control LLM agents** (the Chrome extensions that let Claude Code drive a browser): *"the average step for us runs in under 300 milliseconds"* + specialised debuggability UX (*"it's really hard to know what went wrong if you use a traditional browser agent... we have agents that automatically diagnose these issues for you"*). Complex UIs (rich-text editors, drag-and-drop, canvases) are *"relatively difficult to verify"* for generic agents; Momentic's agents are specialised for those affordances.

The doctrinal claim that frames the whole product: as AI-generated code volume grows exponentially (Cursor, Claude Code, Codex churning out lines), the verification bottleneck dominates. *"As the amount of code output is increasing, we see massive bottlenecks where there may not be before in terms of just: how do I actually verify the work?"*

### 2. The MCP-integration product surface (6:51–9:24)

Where Momentic slots in the AI-coding dev loop. *"A lot of customers actually use our MCP integration to have Cursor or Claude Code write and run Momentic tests while they're developing. So actually while they're creating a new feature or editing an existing feature, they'll make sure that these coding agents also verify that that change is functionally correct by calling out to Momentic — starting a real browser, verifying that the flow actually works — like a tool. It's basically a tool-call for one of the agents."*

Why this is better than the coding agent writing its own tests: (a) the agent *"often thinks that it doesn't have to do that or whatever it's done is just correct, even though it's not"* — self-report failure mode; (b) coding agents *"aren't optimized for browser use, especially in a testing capacity"* — affordance gap on complex UIs.

Taggar's confirmation from inside YC's own engineering team: *"as Claude Code usage has ramped up, we've now set up sort of a pipeline (it's in the CLAUDE.md file actually) to just like make sure you run your own tests and make sure they all pass before you submit any PRs or MRs."*

The user-facing simplification: *"any user flow you can describe — whether it's to a manual tester or to an AI or to Cursor or Claude Code when you're building it — just give it to Momentic and we'll validate it."*

### 3. The truth-driven / spec-driven development thesis (9:53–22:04)

The most rhetorically load-bearing claim in the episode. Wu's two-schools-of-thought framing (18:43–20:48):

| School | Source of truth | Implication |
|---|---|---|
| **Code-as-truth** (status quo) | *"Whatever is in prod is what you've specified it to be. A direct reflection of your codebase."* | But code has bugs — *"are these bugs also part of your source?"* |
| **Truth-driven / spec-driven** (Wu's bet) | A human-in-collaboration-with-AI spec detailing *"user journeys, user flows, success criteria, edge cases within your application"* | *"Your code is just an implementation of that source of truth"* — engineers humans + AI both make mistakes, so the codebase shouldn't be the source-of-record for *how the product is supposed to work* |

The role-shift prediction (11:00–11:48): *"engineers are still very much focused on what code is being generated. But I think as these models get better, that will be less and less of the focus. And humans will be more like **requirements-gatherers**, or they'll be sort of like **truth-finders**... their goal is basically to figure out: what should be written, what should be built in the first place?"* The engineer becomes *"the input to the code generator black box,"* with Momentic as *"this sort of step that actually validates that whatever the black box generates is functional."*

Wu's stronger near-future claim (10:08): *"I would be disappointed in three to six months if I'm still reviewing TypeScript or React code... I see code as an implementation detail. It's a commodity. Some frontier model out there is going to be incredibly good at generating code. It's just the implementation detail."*

Counter-tension acknowledged: An's response on whether engineering expertise still matters (21:05–21:51) — *"there are still many technical aspects of being a software engineer that are not based in the code... thinking about how this integrates with other systems or third-party dependencies, or the scalability aspects, or even just thinking about taste. Models are not particularly good right now at producing tasteful UX. That's the difference between ChatGPT generating a Figma lookalike and actual Figma."* Engineer-as-PM-with-product-intuition remains load-bearing even if code-writing gets commodified.

### 4. The closing-the-loop-for-coding-agents framing (12:41–15:34)

The product positioning relative to the coding agents themselves. Wu: *"In a sense, it's like we're closing the loop for feedback for the coding agents."* Why a standalone product rather than something the coding-agent vendor would absorb:

1. **External source of truth**: *"I can't really trust Claude Code or Cursor to tell me themselves. I need a third external source of truth for verifying that. This is why I have unit tests, I have integration tests at different parts of the stack."*
2. **Responsibility cannot be delegated to the agent**: *"if something breaks, I can't really tell our customer, 'Hey, we vibe-coded this with Claude Code, our SLA got breached because of that, sorry about that, we're going to revert their pull request.' I think that doesn't really work, because the responsibility ultimately is on the product owner — on the human who was delegating to these different AI agents."*
3. **Source-of-truth maintenance over time**: *"these coding agents aren't maintaining your source of truth over time... we've built a mechanism for automatically maintaining that source of truth over time for you — and even going as far as suggesting changes to what your source of truth should be."*

This is the wiki's clearest founder-vantage articulation of **the multi-harness stack** — the coding-agent harness (writes the code) + the verification harness (validates it, owns the source-of-truth) as **structurally separate**, connected by MCP.

### 5. The Notion onboarding anchor (15:41–17:53)

The marquee customer-acquisition story. Simon Last (Notion) posted on Twitter that *"it'd be great if I could just describe this and test it for me."* Comments recommended Momentic. Wu was in San Francisco that evening; DM'd Simon at 10pm with *"I think we've built exactly what you want. I can onboard you tonight."* Sent a Loom of Wu testing on his own Notion workspace; onboarded Simon that night. Escalated to formal POC with the broader Notion team.

Notion's prior stack: a mix of manual testing + *"a really big suite of Selenium that the team was maintaining."* Selenium pain: *"notoriously prone to flakiness — whether it's XPaths or selectors which is how you target elements on the page, it would frequently break. Especially since Notion is such a very flexible product."* Migration to Momentic happened via *"just like plain-English instructions."*

The 2026 state (at the time of the fireside):

- Notion runs *"almost half a million test runs a day"* on Momentic.
- *"Momentic tests must pass before one of Notion's engineers can merge their PR."* — Momentic is in the critical-path of Notion's merge gate.
- Aggregate platform-level: *"we're processing over a million test runs a day"* across all customers.

The mirror-image of Dinakaran's LinkedIn-script-warm-intro pattern at [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Luminai]] — Wu went straight to public-post-DM-at-10pm rather than to network traversal, but the **founder-led-customer-acquisition-through-a-single-high-trust-contact** template is the same.

### 6. The 10× engineer counter-claim (23:19–23:45)

Wu's contrarian observation: *"to be honest, a good engineer is still a really good engineer. I actually wrote a LinkedIn post about this — but, like, Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with."*

Direct rhetorical inversion of the unconditional *1,000× engineer* framing [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu]] articulate at CS153. Wu's hiring criteria pre-AI and post-AI: *"if you're adaptable, if you can navigate ambiguity, if you're curious and passionate, then that continues to be an asset. And that's still what we're looking for."* The multiplier exists, but it amplifies existing skill rather than substituting for it.

The supporting claim: *"now that the industry is moving at this incredibly fast pace, it's even more important to be able to adapt to new trends, to be able to take in that there's a new level of tooling that you can adopt that dramatically accelerates your code output."* The AI-era engineer's load-bearing skills are **meta-skills** (adaptability, curiosity), not coding fluency in any specific stack.

This is filed as a productive `contradicts` edge on the *1,000× engineer* concept. Both founders are right at different conditionalities — Tan & Hu are describing what the *best* engineer can now do unconditionally; Wu is describing what *Codex deployed on the average engineer* produces. The wiki's [[concepts/agentic-engineering|agentic-engineering]] page should carry both.

### 7. Founder-origin pair (25:16–27:50)

Wu was on a PharmD track at the University of Minnesota; switched to CS after a *"most boring experience of my life"* pharmacy camp. An was on a chemistry track at Cambridge; switched to founding software products after a chemistry summer internship felt *"incredibly grueling"* and isolated. Both name the pivot toward software as motivated by *desire for interpersonal / product-building work* over isolated technical work.

Pairing was via Dan Robinson (ex-CTO of Heap), who introduced An (in San Francisco) to Wu (in Seattle), at end of 2023. Wu flew down and stayed on An's couch for a week before deciding to merge into Momentic. Both had been building *"Cursor-for-unit-tests"-style* tools independently when they met.

Applied to YC for **W24** (winter 2024). Wu was unconvinced they would get in — *"AI agents were really bad at that point. Models still had like 16K in token limits — which meant that most websites wouldn't actually fit within the context window — and we barely had any market traction."* An convinced him to apply. They had *"six or seven pilot customers"* at application time.

### 8. The Standard-Capital / peer-group-board model (0:55–1:31)

Atypical Series A structure named on-stage: *"instead of having a board member on our board, we have a peer group of other similar-stage Series A companies to do our board meetings with."* Wu frames this as a fit-with-stage product feature of *Standard Capital*'s offering — application was *"online... not too unlike the application for YC."* Not load-bearing for the wiki's analysis but worth flagging as a 2026-era **peer-cohort-replacing-traditional-board-seat** capital structure.

### 9. The 13-person culture and the *radical-candor / don't-be-a-dick* explicit norm (24:14–25:16)

*"We're a team of 13... I think one of the things that we care a lot about is radical candor — clear direct feedback... don't be a dick to your co-workers."* Hiring discipline: *"we would talk to people multiple times before they ever did a single interview... a sort of rather unique one-day work-trial process."* Investment in *"in-depth team retros and discussions, retreats as well"* post-join.

### 10. Operational scale and capital signals

- **Latest round**: $15M Series A (per channel description) announced 23 March 2026. Lead: *"Standard Capital"* (ASR-preserved; not externally verified).
- **YC batch**: W24.
- **Customers named on stage**: Notion, Built, Quora, Zero.
- **Platform throughput**: *"over a million test runs a day"* aggregate.
- **Notion-specific throughput**: *"almost half a million test runs a day."*
- **Team size**: 13 (at fireside).

## Linked entities and concepts

**Entities directly named or substantively discussed in the source:**

- **[[Y Combinator]]** — accelerator; Momentic is W24. Source-count bumps 9→10.
- **[[Harj Taggar]]** — interviewing Managing Partner. Dangling first mention (his first-source appearance in the wiki).
- **[[Momentic]]** — Dangling first mention (the company).
- **[[Weiwei Wu]]** — Dangling first mention (co-founder).
- **[[Jeff An]]** — Dangling first mention (co-founder).
- **[[Notion]]** — substantive mention (anchor customer; ~500K test runs/day). Existing entity (referenced from prior sources).
- **[[Simon Last]]** — Dangling first mention (Notion CTO; the Twitter-DM-onboarding anecdote).
- **[[Robinhood]]** — Dangling first mention (Wu's prior employer; testing-team experience anchor).
- **[[Dan Robinson]]** — Dangling first mention (ex-CTO of Heap; introducer to An).
- **[[Anthropic]]** — substantive cross-reference (Claude Code as customer-facing dev-loop substrate). Existing entity. Source-count: increment.

**Concepts touched substantively:**

- **[[concepts/agent-harness|agent-harness]]** — verification harness as structurally separate from coding-agent harness; MCP as the inter-harness protocol. Source-count: +1.
- **[[concepts/agentic-engineering|agentic-engineering]]** — truth-driven / spec-driven development as the central rhetorical claim; the 10× counter-thesis as productive contradiction with [[concepts/durable-skills|the 1,000× thesis]]. Source-count: +1.
- **[[concepts/agent-development-lifecycle|agent-development-lifecycle]]** — evals/specs as load-bearing artifacts; vendor-product instantiation. Source-count: +1.
- **[[concepts/enterprise-ai-adoption|enterprise-ai-adoption]]** — Notion at ~500K tests/day as anchor customer; Cursor-and-Claude-Code as the customer dev-loop surface. Source-count: +1.
- **[[concepts/vibe-coding|vibe-coding]]** — explicit on-stage reference (*"we vibe-coded this with Claude Code"*) as the negative case for why external verification is needed. Source-count: +1.
- **[[concepts/durable-skills|durable-skills]]** — the *"adaptable, navigate ambiguity, curious, passionate"* meta-skill anchor for the AI-era engineer. Source-count: +1.

**Dangling** (single-source mentions, deferred): Momentic, Weiwei Wu, Jeff An, Harj Taggar, Simon Last, Robinhood, Dan Robinson, Heap, Cypress, BugBot, Greptile.

## Caveats

- 34-minute YC Root Access Founder Fireside with overt Series A announcement framing; financial, throughput, and impact claims are founder/host self-reports, unaudited.
- The **$15M vs $50M Series A discrepancy** (description vs on-stage) is noted explicitly; the wiki uses $15M per the description. If the true figure is later disclosed elsewhere, this page should be updated.
- *"Standard Capital"* as lead investor is ASR-preserved and not externally verified at ingest time.
- The *over-a-million-test-runs-a-day* aggregate and *~half-a-million-test-runs-a-day* Notion-specific figures are founder claims without disclosed measurement methodology.
- The *"Momentic tests must pass before one of Notion's engineers can merge their PR"* claim is unverified against Notion's actual engineering policy; treat as the founder's representation, not a Notion confirmation.
- The 10× counter-thesis (*"Codex only makes you 10x if you were 10x to begin with"*) is filed as productive contradiction with Tan & Hu's CS153 1,000× framing; the contradiction may be more apparent than real if the two founders are talking about different baselines (best-engineer-now vs average-engineer-deployed-Codex).
- Simon Last as Notion's CTO is a public fact but not stated on-stage; the Twitter-DM anecdote names *"Simon from Notion, Simon Last"* without role.
- The spec-driven-development prediction (*"engineers will just write specs in three to nine months"*) is a forecasting claim Wu makes on-stage; treat as forecast, not status quo.
