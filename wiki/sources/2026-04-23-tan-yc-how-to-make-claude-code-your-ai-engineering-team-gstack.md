---
type: source
kind: video
title: "How to Make Claude Code Your AI Engineering Team"
author: ["Y Combinator"]
url: "https://www.youtube.com/watch?v=wkv2ifxPpF8"
date_published: 2026-04-23
length: "~21:49 minutes (transcript ~103 grouped segments from 521 raw ASR lines)"
raw: "../../raw/videos/tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack.md"
tags: [vibe-coding, agentic-engineering, agent-harness, claude-code, gstack, y-combinator, garry-tan, ai-engineering-team, parallel-sessions, gas-town-stage-7, sub-agents]
relationships:
  - type: supports
    target: agent-harness
    via: "GStack — open-source toolkit by Garry Tan (YC president/CEO) that wraps Claude Code with skills (office hours / design / code review / QA / browser testing); first-party founder-CEO worked example of a packaged harness-of-skills shipping in 3 weeks and outpacing Ruby on Rails stars"
  - type: supports
    target: agentic-engineering
    via: "Garry Tan running 10-15 parallel Claude Code sessions with 400 PRs in review — the AI-founder-type archetype operationalised at YC president scale; Steve Yegge's Gas Town stage 7 invoked explicitly (*'I do think it gets you to level seven'*)"
  - type: supports
    target: vibe-coding
    via: "live demo of going from idea → adversarial review → design mockups → code → QA in a single Claude Code session; *'the barrier to building just collapsed'* peroration; Garry Tan as second YC-partner-vantage on AI-native-company building (after Diana Hu)"
---

# How to Make Claude Code Your AI Engineering Team

> GStack is an open-source toolkit built by YC President & CEO Garry Tan that turns Claude Code into an AI engineering team — with skills for office hours, design, code review, QA, and browser testing.
>
> Use it with Claude Code or Codex or Cursor. It's free and open source: https://github.com/garrytan/gstack
>
> In this video, Garry walks through how GStack works, starting with Office Hours, a skill modeled after real YC partner sessions that pressure-tests your idea before you write a line of code. He demos it live, going from idea through adversarial review, design mockups, and automated QA in a single session.

(Channel description, [[Y Combinator]].)

A 21:49 demo + monologue by **Garry Tan** (YC President & CEO; engineer-by-background — Stanford CS, Palantir employee #10, Posterous co-founder sold-to-Twitter, built first version of YC's Bookface). Published 23 April 2026 to the Y Combinator YouTube channel — **the day before** [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Diana Hu's "How to Build a Company with AI from the Ground Up"]] on the same channel. Two YC-partner-vantage sources on AI-native-engineering in two consecutive days — the **YC-batch-context anchor pair**. ASR caption track; 15 chapters; no manual track.

## TL;DR

Three substantive contributions:

1. **GStack as an open-source harness-of-skills shipping at venture pace**: Tan built GStack in **3 weeks** and reports it *"now has more GitHub stars than Ruby on Rails."* The toolkit wraps [[Claude Code]] (or Codex or Cursor) with named skills — **Office Hours** (16-YC-partners-distilled adversarial-review of startup ideas), **Design Shotgun** (multiple AI design variants in ~60 seconds), **Code Review** (staff-level bug-catching after plan), **QA / Browser Testing** (Playwright+Chromium wrapped as a CLI rather than via Claude-in-Chrome MCP), **Ship** (pre-merge gate). The wiki's **first founder-CEO-vantage open-source-harness anchor** — a YC-president-of-a-Fortune-100-class-accelerator publicly shipping his own harness implementation as a worked example, not just describing one.

2. **The AI-founder-type archetype operationalised at YC-president scale**: Tan reports **10 to 15 parallel Claude Code sessions** running simultaneously, sometimes 3-4 on the same project; *"about 400 PRs to review right now"*; *"10, 15, 20, sometimes 50 PRs in any given day, depending on the number of meetings I have."* Direct operationalisation of [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu's]] *AI founder type* archetype — *"still builds, still coaches and leads by example. If you're the founder, this needs to be you at the forefront."* Tan IS the worked example Hu describes.

3. **Steve Yegge "Gas Town" stage 7 invoked explicitly**: *"There's this idea of trying to get a level 8 software factory and GStack does not get you to level 8, but I do think it gets you to level seven."* The wiki's **second source** explicitly invoking Yegge's eight-stages-of-dev-evolution-to-AI framing (after [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]]). Two-source threshold met on Yegge's framework as a named pattern in the wiki.

Plus: the **ADHD-CEO-vs-autistic-CTO model-allocation framing** — *"by default [Claude Code] uses Claude. And I think Opus 4.6 is sort of ADHD CEO. He's the guy you want to get a beer with and he's got a billion ideas, but when the going gets tough, you got to call in your autistic CTO and that's Codex."* First-party-CEO articulation of model-allocation-by-personality-fit-to-task as a working practice.

## What was actually ingested

Full 21:49 transcript across 15 chapters. ASR transcript with some name-recognition ASR errors flagged below (*"Palunteer"* for **Palantir**; *"Gary"* for **Garry**; *"GSAC"* for **GStack**; *"Gritan"* for **Garry Tan** in the GitHub URL).

## GStack architecture — a harness-of-skills for Claude Code

| GStack Skill | What it does | Anchored against |
|---|---|---|
| **Office Hours** | Adversarial review of startup ideas — distillation of 16 YC partners × thousands of hours × many years; *"10% strength version of what we do at YC every day"*. Asks **the question that determines everything else**: *"What's the strongest evidence that you have that someone actually wants this?"* | Maps onto [[agent-driven-question-narrowing\|agent-driven spec-elicitation]] candidate concept (now visible in: Rufus / Thompson / Böckeler / Tan — four-source convergence) |
| **Plan / CEO Review / Adversarial Review** | Multi-step adversarial review of a design doc; auto-fixes issues; tracks scored improvement (Tan's demo: 6/10 → 8/10 in two rounds; *"automatically caught and fixed 16 issues"*) | Maps onto [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler's]] enhanced-lint-messages-as-good-prompt-injection at the design-doc layer |
| **Design Shotgun** | Generates multiple AI design variants in ~60 seconds and presents them as choices to the developer | Direct operationalisation of [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs\|Thompson's]] *"feel like Steve Jobs picking from nine designs"* developer self-description |
| **Code Review** | Staff-level bug-catching after the plan ships code; *"finding bugs that might not have been in the plan mode"* | Maps onto [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie's]] human-review + eval pattern at the harness-built-in layer |
| **SLQA / SL browse (browser testing)** | Wraps Playwright+Chromium at the CLI level; *"now your Claude Code and any agent can actually just use the browser"* — screenshots, complex interactions, click/fill, download media, regression tests, CSS-bug-assessment. *"Claude in Chrome MCP is one of the worst pieces of software I've ever used"* — Tan's explicit motivation for the rewrite | Direct convergence with [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler's]] CPU-deterministic feedback-harness; **Playwright-as-CLI** as the wiki's first vendor-published browser-control-without-MCP worked example |
| **Ship** | Pre-merge gate; *"the last step before to make sure that your PR is ready to land on main"* | Maps onto [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie's]] evals-as-CI-check |

The collective architecture is the wiki's first **package-everything-in-one-toolkit** worked example — distinct from Anthropic's Skills (modules to load) or Lopopolo's golden-principles GC (in-vendor pattern). GStack ships as a single open-source repo with all skills bundled. Hu's *harness templates* future-prediction (*"pick a workflow topology, instantiate a pre-built harness rather than rebuild"*) is partially realised here at startup-development scope.

## Multi-session orchestration via Conductor

Tan demonstrates GStack inside **Conductor** — a multi-session Claude Code orchestrator (Dangling first-mention; not previously in the wiki). Workflow:

> *"I run 10 to 15 parallel Claude Code sessions all at the same time. I might in one session be running office hours on a brand new idea. ... I have multiple open-source projects with tens of thousands of stars. And I'm probably sitting on about 400 PRs to review right now."*

The **Conductor + GStack + multi-session pattern** is the *worked example of Hu's queryable-organization-with-agents-everywhere* construct, but for a *single-developer-with-many-projects* rather than a *company-with-many-functions*. Same pattern, different scope.

Tan reports the *bottleneck shift* characteristic of multi-session work: *"once the agent was doing all the work of planning and design and coding it, I found myself sitting there doing QA, probably the least fun part of software development. So that made it very, very important for me to try to automate that."* QA → SLQA / SL browse — the harness extends in the direction of the human's remaining bottleneck.

## Tan's worked example — a tax-app idea

Tan demos the full workflow live with a tax-document-aggregator idea:

1. **Office Hours** asks: *"What's the strongest evidence that you have that someone actually wants this?"*; *"How many bank accounts do we have and which one sent a 1099?"* — multi-step pressure-test.
2. **The "this idea just got way bigger" inflection**: Office Hours reframes the idea as *"a funnel — the hook is we'll find all your 1099s for you, the expansion is matchmaking and lead-gen for tax preparers. It's a classic wedge strategy."* Document-aggregation could charge $2-5/year; transaction-percentage of tax-preparer matchmaking is *"10× more"* monetisable. Office Hours surfaces business-model expansion not just feature-list refinement.
3. **Plan mode**: Tan-as-CEO selects among three approaches presented by the agent (A: small Gmail-OAuth-only / B: full-stack Gmail + AI browser + CPA marketplace / C: CPA-first inverse go-to-market). Selects B with a refinement (*"use the browser interaction to skip Google OAuth entirely"*).
4. **Adversarial Review**: catches 16 issues across no-failure-handling / no-privacy-section / 2FA-handoff; auto-fixes most; score improves 6→8 of 10.
5. **Design Shotgun**: generates three design directions; presents as choices.
6. **Code + Code Review + Ship**.

The demo is **fast** — entire idea-to-near-shippable-design in ~10 minutes of video time. Compresses what Thompson 2026's 75-developer survey reports anecdotally into a single-screen worked example at YC-partner scale.

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu / Y Combinator 2026 (24 April)]] | **The YC pair**: Tan (23 April) + Hu (24 April) — two consecutive-day YC-partner-vantage sources on AI-native engineering. Tan IS Hu's *AI founder type* archetype operationalised: still builds, still ships, runs 10-15 parallel sessions at YC-president scale. Hu names the framework (closed-loop / queryable-org / software-factories / 1,000× engineer / token-maxing); Tan ships an open-source instantiation (GStack) of the framework's first principles |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler 2026 (Thoughtworks)]] | **Yegge Gas Town two-source convergence**. Böckeler invokes Yegge's eight-stages-of-dev-evolution-to-AI as audience-orienting framing; Tan invokes the same essay with the specific *"level 7 vs level 8"* terminology Yegge defines. Direct two-source agreement on Yegge as the named-pattern source for the multi-parallel-session practice. Plus: Tan's SLQA/SL-browse-wraps-Playwright is the **specific implementation** of Böckeler's CPU-deterministic-feedback harness, with the *Claude-in-Chrome-MCP-is-terrible* anti-pattern named explicitly |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung 2026 (Anthropic / Claude Code engineering)]] | Fung described what running an agent-native engineering team looks like *inside the vendor*; Tan shows what running an *agent-native-engineering-of-one* looks like at YC-president scale. Same dogfooding principle at different organisational scales |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex 2026]] | Lopopolo: in-vendor at OpenAI Codex (5 months / ~1M LOC / 0 manually-written lines). Tan: open-source-toolkit-shipping-in-3-weeks at YC. Two divergent strategies (in-house vendor harness vs open-source community harness) for the same problem |
| [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs\|Thompson 2026 (NYT The Daily)]] | Thompson's *"feel like Steve Jobs picking from nine designs"* developer self-description is *literally what GStack's Design Shotgun does* — multiple AI design variants in ~60s as choices. Operator-side cultural observation → operator-side toolkit instantiation |
| [[2026-05-09-chase-agent-development-lifecycle\|Chase / LangChain ADLC 2026]] | GStack's skill set maps onto Chase's ADLC: Office Hours/Adversarial Review = Build-phase-spec-elicitation; Code Review = Test; SLQA/Browser = Test simulations; Ship = Deploy gate. GStack is **Chase's ADLC operationalised as a single CLI toolkit** rather than as a vendor product portfolio |
| [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie / Braintrust 2025]] | Both name *evals-as-CI / pre-merge-gate* as a harness pattern; Tan ships it (Ship skill); Guthrie's Braintrust platform offers the eval-platform layer GStack's Ship skill could integrate with |

### Contradictions

None substantive. Tan's framing is enthusiastic but operationally grounded.

## Linked entities and concepts

**Existing wiki entities reinforced**: [[Y Combinator]] (Dangling from Hu 2026; **now two-source — promotion candidate** but defer entity-page creation to the cross-cutting work in this batch).

**Concept pages updated**:

- [[vibe-coding]] — Tan's *"the barrier to building just collapsed ... what are you going to build?"* peroration; live demo as worked example of the floor-raising thesis at solo-founder scale.
- [[agent-harness]] — GStack as the first founder-CEO open-source-toolkit harness instantiation.
- [[agentic-engineering]] — Tan's 10-15-parallel-sessions / 400-PRs-in-review at YC-president scale as the AI-founder-type archetype.

**Dangling** (single-source first-mention, deferred per the author-entity-promotion rule):

- **Garry Tan** — YC President & CEO; engineer (Stanford CS); ex-Palantir #10; Posterous co-founder; built Bookface.
- **GStack** — Garry Tan's open-source toolkit (github.com/garrytan/gstack). **Strong promotion candidate** — likely to recur on future Claude-Code-skill-ecosystem ingests.
- **Conductor** — multi-session Claude Code orchestrator Tan demos GStack inside of.
- **Palantir** — Tan's first decade employer; ASR rendered as *"Palunteer"*.
- **Posterous** — Tan's pre-YC co-founded micro-blogging startup (sold to Twitter).
- **Bookface** — YC's internal social platform; Tan built v1.

**Concept candidates surfaced (not yet promoted)**:

- *Model-allocation-by-personality-fit-to-task* — Tan's *"ADHD CEO Claude Opus 4.6 vs autistic CTO Codex"* framing. Anthropomorphic but operationally meaningful. Single-source.
- *Open-source-toolkit-of-skills-shipping-in-weeks* — GStack as worked example. Single-source as a *pattern-named-as-such*.
- *Bottleneck-shift-to-QA-when-coding-is-automated* — Tan: *"once the agent was doing all the work ... I found myself sitting there doing QA, probably the least fun part."* Single-source as a *named-bottleneck*.

## Open questions raised by this source

- **GStack repository deep-dive** — would substantiate the skill architecture claims. Primary-source target: github.com/garrytan/gstack.
- **Conductor as a separate tool** — Tan uses it as the multi-session shell. First-party documentation on Conductor's architecture and relationship to Claude Code would let the wiki ingest it as a distinct entity.
- **"More GitHub stars than Ruby on Rails in 3 weeks"** — staggering velocity claim. Worth tracking the 3-month / 6-month adoption arc.
- **Whether the GStack architecture transfers to non-individual-developer settings** — Tan operates at YC-president-with-many-side-projects scale; would the same skills work for a 100-developer org? Open empirical question.
