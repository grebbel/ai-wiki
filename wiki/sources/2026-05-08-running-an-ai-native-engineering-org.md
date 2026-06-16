---
type: source
kind: video
title: "Running an AI-native engineering org"
author: ["Claude"]
publisher: "Anthropic (Claude YouTube channel — Code with Claude 2026)"
url: "https://www.youtube.com/watch?v=igO8iyca2_g"
date_published: 2026-05-08
date_ingested: 2026-05-09
length: "~28:38 minutes (transcript ~163 lines + 12 presentation slides captured as screenshots)"
raw: "../../raw/videos/running-an-ai-native-engineering-org.md"
slides: "../../raw/images/fung-slide-01-…-12-*.png (12 substantive slides)"
tags: [agentic-engineering, claude-code, anthropic, code-review, dogfooding, jit-planning, claudify-everything, octopus-organization, process-pruning, fiona-fung, code-with-claude-2026, presentation-slides]
confidence: 0.80
last_confirmed: "2026-05-09"
---

# Running an AI-native engineering org

> When agentic coding goes from individual tool to org-wide default, the tool isn't the hard part...your processes are. Fiona Fung, Director of Engineering for Claude Code, walks through what broke at Anthropic (review, ownership, hiring) and the norms we had to rewrite to keep shipping.
>
> *— [Claude YouTube channel description](https://www.youtube.com/watch?v=igO8iyca2_g)*

A **~29-minute conference talk** by **Fiona Fung** (Director of Engineering for Claude Code at [[Anthropic]]; previously led teams at Meta and Microsoft) at *Code with Claude 2026* (a Claude-channel-published session). The wiki's first **inside-engineering** source on what running an AI-native engineering organisation actually looks like day-to-day — distinct from prior 2026 sources that argued the *case* for AI-native engineering rhetorically (Karpathy, Chatterjee, Kokane) or measured it ablation-by-ablation ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Pan/Khattab via Prompt Engineering YouTube]]).

This source's structural value: it pairs Karpathy's *[[agentic-engineering|agentic engineering]]* discipline-naming and Chatterjee's [[agent-harness|harness anatomy]] with **the operational team-norms rewrite that follows from them**. Where Karpathy says *"the 10× engineer used to be the upper bound; agentic engineering pushes far past 10×"*, Fung shows the org-shape, hiring, review, and process choices that ship the 10×-plus product (Claude Code itself).

## TL;DR

- **The organising claim**: *"What may have served you prior may not serve you any longer."* Bottlenecks have shifted away from engineering bandwidth. The work is now to find which existing processes "quietly stopped working" and rewrite them.
- **Five themes**: (1) the bottleneck shift, (2) norms Anthropic rewrote at Claude Code, (3) how they rolled them out, (4) signals that show it's working, (5) open questions Fung is still asking.
- **Where bottlenecks moved**: from coding throughput → **verification, review, cross-functional partners, security**. *"Coding is no longer the bottleneck and we're doing so much more of it."*
- **The Karpathy phase-change at the org level**: Fung's own narrative — *"I just trusted the system more and more, and then I was vibe coding"* — mirrors [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's December 2025 moment]]. The org-level analogue ran ~simultaneously inside the Claude Code team.
- **Norms rewritten**: JIT planning (no more 6-month roadmaps); design docs out, prototypes in; "code wins" over whiteboard debate (generate three PRs instead); double-click past *"who made this change?"* (now a fuzzy question because every PR is Claude-assisted); code-review division of labour (Claude on style/lint/bug-catching/tests, humans on legal/security/product taste); team-makeup indexed on creative-builder + deep-systems-expertise rather than raw throughput; org shape **flat by design**, with every manager starting as an IC (recruiters initially thought this was crazy); **code is the source of truth** (not docs).
- **Rollout pattern**: mandate the few must-dos (*Claudify everything*; *explicit permission to kill processes*); leave the rest to pod-level high agency.
- **Signals it's working** (the three Fung tracks publicly): onboarding ramp-up time **dramatically reduced**; PR cycle time **shortening** (and surfacing pipeline gaps); Claude-assisted commits **trending toward 100%** (*"I don't think I've seen a non-Claude-assisted commit probably in the last four months"*).
- **The two engineer profiles Fung indexes on**: (1) *creative builders with product sense* and (2) *deep systems expertise*. **What she indexes less on: raw throughput** — *"thanks to the models we just have a lot more."*

## What was actually ingested

Full ~28:38 transcript (cleaned from auto-generated English captions; ASR fixes for product/people names; section headings inferred from topic shifts as the video itself has no YouTube chapters). 163 transcript lines.

**Plus 12 presentation slides** captured as screenshots in `raw/images/fung-slide-01-…-12-*.png`. The slides crystallise Fung's argument in compacter form than the spoken version and add several quotable framings absent from the transcript ("Cost of asking a 'dumb' question went to zero"; "Taste is scarce, typing is not"; "If these don't shift in six months, adoption isn't working"; the Monday-test diagnostic). The Slide-deck visual canon section below walks through them in talk order.

## Slide-deck visual canon

The 12 substantive slides distil the talk into the speaker's chosen on-screen wording — by definition the most boiled-down version of each section. Listed below in talk order, with the screenshot reference (in `raw/images/`), the full slide content, and a one-line note on what the slide adds vs. the transcript.

### Slide 1 — *Where the old process quietly stops working*

`raw/images/fung-slide-01-old-process-quietly-stops-working.png`

Five categories the AI-native shift has invalidated:

| Category | What now matters |
|---|---|
| **Planning norms** | Engineering speed and throughput is now very different |
| **Code ownership** | "Who wrote this" is a weirder question now |
| **Code review** | New shape, new scale, new tools now available |
| **Team make-up** | Roles are blurring, what skillsets now serve you? |
| **Knowledge sharing** | Documentation no longer the source of truth |

*Slide vs. transcript:* the slide title — *"quietly stops working"* — is the verbatim phrase from the transcript she calls out as a favourite. The five-category ordering matches the rest of the deck's section structure.

### Slide 2 — *Five norms we rebuilt from the ground up*

`raw/images/fung-slide-02-five-norms-rebuilt.png`

| Norm | New shape |
|---|---|
| **Code review** | Human judgment on what actually needs it |
| **Onboarding** | Cost of asking a "dumb" question went to zero |
| **Planning** | Less upfront. More prototype. |
| **Hiring** | Creativity & judgment over raw output |
| **Org shape** | Flatter org. Every manager an IC first. |

*Slide vs. transcript:* **"Cost of asking a 'dumb' question went to zero"** is the slide's framing for onboarding — a sharp consequence of having Claude available that the transcript only gestures at. Worth quoting standalone.

### Slide 3 — *One thing we reduced, one thing we're doubling down on*

`raw/images/fung-slide-03-design-docs-out-verification-up.png`

Two-card layout (light card / dark card):

- **Reduced — *The "design doc before any code" ritual.*** *"For most work it was theater. Replaced with prototype-first. The doc, if it needs to exist, comes after."*
- **Doubling down — *Verification.*** *"When things break in an AI-native flow, they break in new ways. The only way to scale and ensure quality is to keep automating verification to 'shift left.'"*

*Slide vs. transcript:* the slide adds two crisp framings the transcript doesn't have verbatim — **"For most work it was theater"** (design docs) and **"When things break in an AI-native flow, they break in new ways"** (verification). The "break in new ways" line is the canonical reason verification has to scale ahead of throughput.

### Slide 4 — *Human review where it matters*

`raw/images/fung-slide-04-human-review-where-it-matters.png`

Two-column trust-distribution (light card / dark card):

| Claude handles | I still want a human |
|---|---|
| Style and lint | Legal review |
| Obvious bugs | Risk tolerance |
| **Spec drift and missing tests** | Product sense and taste |
| **Repeated patterns, bug-bounty triage** | Trust boundaries and security-sensitive code |

*Slide vs. transcript:* the slide adds **two "Claude handles" categories** the transcript only summarised — *spec drift and missing tests* (operationally upstream of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s *Contracts* layer) and *repeated patterns, bug-bounty triage* (operationally a *Constraints*-layer pattern at fleet scale). Both deserve to be quoted directly when discussing the trust division of labour.

### Slide 5 — *Two profiles I now index on*

`raw/images/fung-slide-05-two-profiles-i-index-on.png`

Two-card layout:

- **Profile 01 — Creative builders with product sense.** *"Can spot the right thing to build and prototype it fast. **Taste is scarce, typing is not.**"*
- **Profile 02 — Deep systems experts for the hard parts.** *"The places where 'trust but verify' matters most. **Subtly wrong is still wrong.**"*

Footer: *"What I index on less: raw output. I don't care how many lines you can write per hour. **I care what you choose to build and how you know it's right.**"*

*Slide vs. transcript:* three quotable lines here — **"Taste is scarce, typing is not"** (the hiring one-liner of the year), **"Subtly wrong is still wrong"** (the subtle-bugs argument for systems expertise), and **"I care what you choose to build and how you know it's right"** (which explicitly names *spec-design taste* + *evaluation craft* as the two human-load-bearing capabilities).

### Slide 6 — *Filling cross-functional gaps with Claude*

`raw/images/fung-slide-06-filling-xfn-gaps-with-claude.png`

Before/After process diagram:

| | Step 1 | Step 2 | Step 3 | Step 4 |
|---|---|---|---|---|
| **Before** | Eng ships bug fix | Wait for content designer | Ship mediocre copy, or wait days | — |
| **After** | Eng ships bug fix | Claude drafts copy | Human decides | Ship same day |

Caption: *"The XFN gap stops being a bottleneck and becomes a collaborator. **Humans still decide, they just aren't the first draft anymore.**"*

*Slide vs. transcript:* the **Before/After process visualisation** is its own contribution — concretises the "roles blurring" abstraction into a specific four-step workflow. **"Humans still decide, they just aren't the first draft anymore"** is the cleanest framing in the deck for the human-in-the-loop pattern under role-blurring.

### Slide 7 — *No 10:1 ratio here. Every manager started as an IC.*

`raw/images/fung-slide-07-no-10-to-1-ratio-manager-as-ic.png`

Org-shape diagram (Claude Code team):

- Centre: **Manager (also an IC)** — orange-circled
- Around it: row of ICs (grey circles)
- Footer label: *"Running an AI-native org"*

Side panel — *Leaders keep some individual work*:
- *"You can't coach scrappiness if you're not in the code yourself"*
- *"If I'm asking engineers to prototype fast and throw things away, I need to be doing that too"*
- *"Plus, this is the best way for me to get hands-on experience with our products"*

*Slide vs. transcript:* the visual emphasises the **break with the standard 10:1 IC-to-manager ratio**. The three bullets are crisper rationales than the transcript provides for "every manager starts as IC."

### Slide 8 — *Align on core team principles*

`raw/images/fung-slide-08-align-on-core-team-principles.png`

Two-column "must-do vs adapt" structure (light card / dark card):

| The forcing function (*"Align with teams on 'Must dos'"*) | The room to adapt (*"Emergent from teams"*) |
|---|---|
| Every engineer uses Claude Code | How Claude shows up in each team's triage |
| "Claudify everything you can" | Planning rituals, standups, on-call shape |
| Explicit permission to kill old processes | Which workflows get Claudified first |

*Slide vs. transcript:* the **"forcing function vs room to adapt"** two-column structure is sharper than the transcript's mandate-vs-enable description and worth holding as the canonical articulation. It's also a pattern other teams could adopt directly: name your three must-dos, leave everything else to pod agency.

### Slide 9 — *Three things I'd prioritize*

`raw/images/fung-slide-09-three-things-id-prioritize.png`

Numbered cards (01/02/03):

1. *We keep the team as flat as possible. Managers support pods of work, but we stay agile so people can shift to where the work is.*
2. *If Claude can do it, Claude should. That frees us up for the harder work.*
3. *People don't delete processes on their own. They pile new ones on top. Name the ones that can go.*

*Slide vs. transcript:* the slide phrasing is cleaner; **"Name the ones that can go"** is more action-oriented than the transcript's "see what you should let go."

### Slide 10 — *If these don't shift in six months, adoption isn't working*

`raw/images/fung-slide-10-six-month-signals-threshold.png`

Three-column signal dashboard with arrows:

| Signal | Direction | Evidence |
|---|---|---|
| **Onboarding ramp time** | ↓ | *Materially faster than a year ago. **Week-one engineers ship real code now.*** |
| **PR cycle time** | ↓ | *Shorter end-to-end. **Queue depth stopped being a leading complaint.*** |
| **Claude-assisted commits** | ↑ | *Very high share of what ships. This is the default, not the exception.* |

*Slide vs. transcript:* the **slide title is the concrete threshold the transcript doesn't state outright** — *"If these don't shift in six months, adoption isn't working."* That's a clean six-month checkpoint other teams can borrow directly. The two new framings — **"week-one engineers ship real code"** and **"queue depth stopped being a leading complaint"** — are concrete signal-criteria worth holding alongside the directional metrics.

### Slide 11 — *Three questions I'm still working through*

`raw/images/fung-slide-11-three-open-questions.png`

Three-card open-questions panel:

| Question | Why it's open |
|---|---|
| **Do you still need separate iOS and Android orgs?** | Engineers can now more easily flex against mobile platforms |
| **How far do you push fully automated review?** | There's a line between "fast enough" and "we lost something important" |
| **With roles blurring how do we ensure everyone equally productive?** | How to ensure all roles **feel confident about their changes** |

*Slide vs. transcript:* the **roles-blurring question's answer-axis is "feel confident about their changes"** on the slide, not "feel productive" as the transcript phrases it. *Confidence-about-own-changes* is the more actionable framing — it points at verification tooling for non-traditional coders, not at a fairness measurement problem.

### Slide 12 — *The one thing to do on Monday*

`raw/images/fung-slide-12-pick-noisiest-workflow.png`

Sage-coloured closing slide:

> **Pick your noisiest workflow. Ask if it still earns its place.**
>
> *If it only exists because engineering used to be expensive, it probably doesn't. Start there with Claude Code. One thing at a time.*

*Slide vs. transcript:* the slide gives the talk's parable a **single-test diagnostic** — *"if it only exists because engineering used to be expensive, it probably doesn't."* That's a much sharper Monday-morning question than the transcript's longer 50-person-meeting story, and worth landing as the canonical takeaway from the talk.

## Key claims, with quotes

*The slide canon above carries the speaker's chosen on-screen wording for each section. The prose claims below extend the slides with transcript-only context (anecdotes, asides, narrative connective tissue) and integrate cross-source positioning. When in doubt about canonical wording — slides win.*

### The bottleneck shift

> *"For years engineering bandwidth was the expensive thing. Coding throughput was really expensive. … On the Claude Code team, coding really isn't the slow part anymore. … Bottlenecks shift to other areas. For example: verification, review, cross-functional partners, security — because coding is no longer the bottleneck and we're doing so much more of it."*

The historical analogy Fung uses to warrant the framing: shipping VS 2005 on CD-ROMs vs. online distribution. Each substrate change forces a process rewrite that's hard to see from inside the old paradigm.

### "What may have served you prior may not serve you any longer"

The titular refrain. Pairs with a second slogan worth saving on its own:

> *"Rarely do processes kill themselves."*

Which becomes the operational point in the rollout section: *"explicit permission to kill those processes"* is one of three core team principles, because *"processes will not kill themselves."* This connects directly to [[2026-05-04-rethinking-agents-harness-is-all-you-need|Anthropic's "subtraction principle"]] at the team-process level (rather than the harness-component level).

### Planning: JIT, not 6-month

> *"When I first joined I was like, 'don't we need a six-month roadmap?' We put some effort in, wrote it, it was pretty good for three months. Then I came back over the new year and so many things had already changed. So I realized — wow, a six-month roadmap just seems like a little bit too long. … I call it JIT planning, almost like JIT compiling."*

This is operationally consistent with [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun's Octopus]] *"do less to achieve more"* and with **Augmented Learner** posture from [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]] (*"we keep these up to date — every few months we ask, 'is this still having the same effect?'"*).

### Technical debates: code wins (generate three PRs)

> *"I almost leaned into my old toolbox — almost tapped him on the shoulder, 'let's go to that room, get a whiteboard.' And I'm like, wait a minute — nowadays I can just generate all the different options we've been discussing. I generated three PRs."*

The deeper consequence: **"when building is cheap, arguing is expensive."** This sharpens the cost calculus for design discussion in the agentic-engineering era — and, importantly, shifts what good team culture protects against. Fung's specific anti-pattern: *"the last person who checked in wins. 'I'm going to stay up at 3am to submit this PR, set up a routine so I get the last word in.' Definitely a no-no."* Cheap building means strong **alignment culture** has to do more work than it used to.

### Verification "shift left" and confidence-for-everyone

> *"Because roles are blurring — for example, my designers — I'd love them to have more confidence that when they check in code, they don't break something."*

The throughput change pushes verification work earlier in the pipeline (*"shift left"*) and across role boundaries — which directly engages [[agent-harness|the harness's Constraints layer]] (pre/post-tool middleware) at the team level: organisation-scale automation that catches things before a human review touches them.

### Code review: trust Claude for what, keep humans for what

> *"Where do you trust Claude (a lot), and where do you still want a human?"*

Fung's published division:

| Trust Claude | Keep humans |
|---|---|
| Style and lint feedback | Legal review (*"I always want my legal partner"*) |
| Catching some bugs and fixing pre-commit | Risk tolerance / trust boundaries / security-sensitive code |
| Adding tests | Product sense and taste (the *Mr. Peanut snowman* anecdote — design partner caught what Claude couldn't) |

This is the on-the-ground concretisation of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s *Constraints* layer (pre/post-tool hooks) and *Contracts* layer (formal-evaluable specifications of "good") at the engineering-team level rather than per-agent.

### "Who made this change?" — double-click

> *"My advice here: because all our PRs are assisted by Claude, 'who made this change?' is a little bit of an odd question. What's more helpful than that question is what I call double-clicking into it."*

The interrogation pattern: when reaching for *"who made this change?"*, ask what you're really after — regression source? expert for a customer question? context-gain? — and **automate the underlying double-click question** rather than re-route through a human. This is operationally what [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]] mean by **"verification → evaluation → learning capture"** at the codebase-attribution layer, not the deployment-flywheel layer.

### Team makeup — what to index on, what to drop

The two engineer profiles Fung indexes heavily on:

1. **Creative builders with product sense** ("the dreamers"): curiosity-driven; iterative; ships toward delight.
2. **Deep systems expertise**: distributed-systems engineers for things like Claude Code remote.

> *"What I index less on is raw throughput, because thanks to the models we just have a lot more."*

This is the **hiring-cohort version** of the rent-vs-own framing from [[agent-harness]]: throughput is rented (it comes from the model + harness), while creative judgement and deep-systems craft are the durable hiring signals.

### Cross-functional roles blurring

> *"With Claude, you have non-traditional coders now able to do more engineering, but you also have engineers who can lean into things that traditionally weren't on the technical side — content, design."*

The blur runs both ways: PMs ship code; engineers ship content/design. Fung's own example: she used Claude as a **content-design partner** for survey copy because her writing skills were "quite terrible." See [[ai-employment-effects]] for the labor-market correlate (Brynjolfsson canaries + role-content shift).

### Org shape — flat, with managers starting as ICs

The *spicy* section, told as a recruiter-management story.

> *"I really structure the org to be as flat as possible because I want us to be super agile. … Every manager in Claude Code starts out as an IC first — also to earn some street cred with the team and learn how to be an effective engineer. … This was where my recruiters had concerns. They said, 'you want to hire managers and they'll start as ICs first? No manager will be interested in that.'"*

The dogfooding rationale (*"there's no way I'd be able to ramp or do code without Claude — there's just so much context-switching"*) ties leader-effectiveness to direct hands-on use of the product. This is operationally [[2026-04-28-werner-lebrun-octopus-organization|Octopus-shape]] with a specific staffing rule attached.

### Knowledge sharing — **code is the source of truth**

> *"On our team on Claude Code, the code is the source of truth. When I'm answering customer requests, I just have my desktop Claude Code and all my local repositories, and I answer a lot of customer questions from there. Having the codebase be the source of truth prevents some of the lag you might have had before — keeping documentation correct alongside the code."*

Caveat she names: teams with strong **specs** (rather than docs that drift) should check those into the repo and have Claude continuously verify code-vs-spec alignment. This is the team-internal version of what the wiki holds at the discipline level via [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s *Contracts* layer.

### The three core team principles Fung mandates

1. **Every Claude Code team member, including cross-functional partners, uses Claude Code** (not just engineers).
2. **Claudify everything you can.** Always ask: is there some way Claude could help? Verification, shift-left, automation.
3. **Explicit permission to kill those processes.** *"Processes will not kill themselves."*

Combined with the pod-level high-agency for *how* to roll changes out, this is the smallest set of organisational invariants Fung carries forward.

### Three priorities that made the biggest difference (her zoom-out)

1. **Keep the team as flat as possible** — pods of work, but agile; one overall mission rather than per-pod missions that fragment.
2. **Claudify everything** — frees humans for the harder work.
3. **Processes pile on** — work with the team to see what to let go.

### The three signals to watch — with a six-month threshold

Fung can't share absolute numbers but names three direction-of-travel metrics, and the **slide title states the threshold the transcript leaves implicit**: *"If these don't shift in six months, adoption isn't working."* (Slide 10.) That's a concrete checkpoint other teams can borrow.

- **Onboarding ramp-up time has dramatically reduced.** How fast a new engineer / designer / PM is effective. Slide phrasing: *"Materially faster than a year ago. **Week-one engineers ship real code now.**"*
- **PR cycle time shortening.** *"This one is interesting to double-click into, because it might actually help you identify a gap that's not just about lack of AI adoption — it's where the rest of the pipeline might be struggling to scale. As we put through so much more code, sometimes product infrastructure or CI can't keep up."* Slide phrasing: *"**Queue depth stopped being a leading complaint.**"*
- **Claude-assisted commits going up.** *"For us, by default every commit is Claude-assisted. I don't think I've seen a non-Claude-assisted commit probably in the last four months."* Slide phrasing: *"This is the default, not the exception."*

### Cancel-the-50-person-meeting anecdote

> *"There was a team I was on where we used to have this weekly review. Very expensive — like 50 people in this large room. I noticed everybody was on their laptops, except for when it was their turn to give their status report, and then they'd pop their head up, say the status, and go back down. I'm like, this is a very expensive meeting. I just asked the simple question: why are we having it? And just that one question — everybody's like, 'yeah, it's true.' So we canceled it."*

The closing parable — pick your noisiest workflow and ask whether it's still serving its intended purpose. Operationally it's the *resistance-as-data* posture from [[2026-05-07-carucci-resistance-as-data|Carucci 2026]] applied to one's own meetings.

Slide 12 sharpens the parable into a **single-test diagnostic for Monday morning**:

> ***Pick your noisiest workflow. Ask if it still earns its place.*** *If it only exists because engineering used to be expensive, it probably doesn't. Start there with Claude Code. One thing at a time.*

The question *"does this exist only because engineering used to be expensive?"* is the most action-forwardable framing in the talk — a literal first-Monday-back exercise.

### Fung's open questions (not yet resolved)

- **iOS and Android orgs.** When engineers can flex across mobile platforms more efficiently, does the traditional team-per-platform shape still make sense?
- **How much fully automated review?** Where's the balance between fast-enough and *we lost something important*?
- **Model capabilities keep improving.** The *trust but verify* line moves over time as the model improves; *"that's why it's always important to re-evaluate."* (References *Daren Lannon*'s earlier session at the same event.)
- **Roles blurring → fairness.** *"How do you make sure everybody feels equally productive?"* — flagged but not answered.

## Cross-source positioning

| Source | Construct | What this Fung talk adds |
|---|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | Agentic engineering as discipline; "10× ceiling pushed past" | The **operational team-norms rewrite** that follows: hiring, review, planning, org shape. Karpathy named the discipline; Fung shows what running an org built around it looks like. |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | Harness 4 layers (Context/Constraints/Contracts/Compounding) | The **team-level analogue**: Claude Code Review on style/lint/bugs (Constraints); legal/security/product-taste reviews (Contracts boundary); team retros where principles get refreshed (Compounding). |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron-Schrage 2026]] | Verification → Evaluation → Learning capture; CLAUDE.md as judgment-capture | Reinforces with a separate Anthropic vantage. Fung doesn't name Boris by name in this segment but the *morning-routine → routines* progression (customer-feedback summarization moved from a daily Claude Code spawn to a scheduled routine) is the same flywheel from a different operator. |
| [[2026-04-28-werner-lebrun-octopus-organization\|Werner-Le-Brun 2025]] | Octopus org / "do less to achieve more" / spreading not scaling | Concrete inside view of an Octopus-shaped technology org: flat, pod-driven, agile-by-design, with leader dogfooding as a structural commitment. |
| [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|Dutt-Chatterji et al. 2026]] | Process redesign as the load-bearing decision | This talk is operationally what *"reimagine workflows across the organization"* (step 2 of Bain/OpenAI's 4-step) looks like when the firm doing it is itself building the model + harness. |
| [[2026-05-07-ransbotham-augmented-learners\|Ransbotham et al. 2024]] | Augmented Learners 2×2 (org-learning × AI-specific learning) | An identifiable Augmented Learner in operation. *"We keep these up to date — every few months we ask, 'is this still having the same effect?'"* is the org-learning practice; *"Claudify everything you can"* is AI-specific learning. |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic Managed Agents 2026]] | Brain/Hands/Session decoupling | Same parent organisation; this Fung talk is the **engineering-leadership** view of what gets built on top of that infrastructure platform. |

## Linked entities and concepts

**Existing pages (touched or referenced):**

- [[Anthropic]] — heavy: this is an inside view of Anthropic's own engineering practice; bumps source_count and adds the Claude Code engineering organisation as a body section.
- [[agentic-engineering]] — heavy: this is the day-to-day operational anchor for the discipline.
- [[agent-harness]] — moderate: code-review automation as Constraints layer; trust-but-verify boundary as Contracts layer.
- [[vibe-coding]] — moderate: Fung's "I just trusted the system more and more" mirrors Karpathy's December 2025 phase change at the org level.
- [[software-3.0]] — light: the talk is implicitly built on the paradigm; mentioned as background.
- [[enterprise-ai-adoption]] — heavy: Octopus-shape, JIT planning, Claudify-everything, dogfooding, process-pruning.
- [[micro-productivity-trap]] — moderate: Anthropic *avoids* the trap by making process-pruning a first-class team principle.

**New pages created with this ingest:**

- [[Boris Cherny]] — entity (cross-page-presence promotion: third source mention; previously in [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]] with the *10–15 concurrent Claude instances + CLAUDE.md as in-workflow learning capture* anecdote, and in [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]]; Fung names him here as her partner running Claude Code).

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):**

- *Fiona Fung* — speaker (Director of Engineering for Claude Code; previously Meta and Microsoft).
- *Cat* — Anthropic colleague delivering the keynote-of-the-morning on Claude Code Review.
- *Jared* — colleague (mentioned alongside Boris).
- *Daren Lannon* — colleague delivering an earlier talk at the same event on model-capability progression.
- *Code with Claude 2026* — the conference / venue (Anthropic-hosted event).
- *Cowork* — Anthropic product (mentioned alongside Claude Code; Fung leads engineering for both).

## Source-quality flag

- **Strengths**: high-information density (every section names a concrete operational practice rather than rhetoric); first **inside-engineering** vantage in the wiki on running an AI-native org (vs. consulting/practitioner essays from outside); aligns operationally with multiple independent sources without re-citing them. Speaker is the Director of Engineering for the most-discussed AI-coding product in the wiki's 2026 corpus.
- **Caveats**: vendor-of-product talk (Anthropic is selling Claude Code; Fung leads the team). The *"Claudify everything"* prescription is internally rational but read with that vantage. No empirical numbers shared on stage (*"I can't go into the explicit numbers"*); Fung explicitly defers to direction-of-travel signals.
- **Per CLAUDE.md §Lifecycle**: confidence baseline 0.70 (single supporting source for the operational-norms-rewrite specifics) + 0.05 for cross-source resonance with already-ingested 2026 sources at multiple stack layers (Karpathy paradigm; Chatterjee harness anatomy; Kiron-Schrage flywheel; Werner-Le-Brun Octopus; Ransbotham Augmented Learners). Held below the peer-review tier; not raised to 0.80 because it's a single conference talk by an interested party. **Confidence: 0.75.**

## Open questions for the wiki

- **Population-level confirmation of Fung's three signals.** Onboarding ramp-up time, PR cycle time, Claude-assisted commit share — these are tractable and would be ingestable from a follow-up Anthropic Economic Index report or a third-party engineering-productivity study. Worth tracking which lab/firm publishes first.
- **The "iOS and Android orgs" question.** Fung leaves this open. If a follow-up talk or post resolves it, it changes the org-shape thesis for any team supporting cross-platform deliverables.
- **The fully-automated-review threshold.** Fung names this as the *trust-but-verify-frontier-shifts-with-model-capability* problem. The *Daren Lannon* session referenced here might already address it; worth tracking whether that talk gets published.
- **"Roles are blurring" fairness signal.** Fung flags but does not answer how to make sure everybody feels equally productive when content designers ship code and engineers ship content. The wiki's [[ai-employment-effects]] cluster could absorb this as an open question.
- **Cowork as a distinct product.** Mentioned alongside Claude Code but not described in detail. Promote on second-source mention.
- **Code with Claude 2026 (the event itself).** First mention; if a second source from the same event lands, promote to entity.
