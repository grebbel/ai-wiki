---
type: concept
aliases: ["vibe coding", "Vibe coding", "vibe-coding", "vibe-code", "v-coding"]
tags: [vibe-coding, agentic-engineering, software-3.0, ai-agents, accessibility, hobbyist-coding, karpathy, pm-tooling, prototype-as-influence-tool, december-2025-phase-change]
confidence: 0.88
last_confirmed: "2026-05-11"
source_count: 6
relationships:
  - type: instance-of
    target: software-3.0
    via: "vibe coding is the floor-raising mode of Software 3.0 — same substrate, no quality bar"
  - type: contradicts
    target: agentic-engineering
    via: "vibe coding raises the floor; agentic engineering preserves the ceiling — same artifact, opposite goals"
---

# Vibe Coding

The **intuitive, exploratory mode of writing code with an AI agent** — coined by [[Andrej Karpathy]] in 2024 and widely adopted as practitioner vocabulary through 2025–26. Karpathy's working framing in the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]] (29 April 2026):

> *"Vibe coding is about raising the floor for everyone in terms of what they can do in software. The floor rises, everyone can vibe code anything, and that's amazing — incredible."*

Vibe coding is the **democratisation half of [[software-3.0]]**: it makes software-creation accessible to people who don't have classical software-engineering backgrounds. Its complement — [[agentic-engineering]] — is the *professionals' half*, where the same substrate is wielded with quality discipline. The wiki holds both as **two complementary modes of the same Software 3.0 substrate**, not opposites.

## Working definition

A **vibe-coding session** is one in which the human:

- Has a goal in mind (build a thing, try an idea, scratch an itch).
- Describes the goal to an agent in natural language, often without rigorous specification.
- Iterates by *feel* — looks at the output, asks for changes, accepts what works.
- Does *not* take responsibility for production-grade properties (security, scalability, maintainability, code aesthetics).

The *vibe* in vibe coding refers to the **mood/feel-driven iteration loop**, in contrast to the *spec-and-test-driven* iteration loop of traditional software engineering.

## Key claims

### The "December 2025 phase change" — vibe coding tipped from useful to trustworthy

[[Andrej Karpathy]]'s [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|first-person account]] of the moment vibe coding stabilised:

> *"I've been using agentic tools like [Claude] code and adjacent things for a while, maybe over the last year as it came out, and it was very good at chunks of code and sometimes it would mess up and you have to edit them. December was this clear point where for me — I was on a break, so I had a bit more time, I think many other people were similar — and I just started to notice that with the latest models the chunks just came out fine. And then I kept asking for more and it just came out fine. And then I can't remember the last time I corrected it. And I just trusted the system more and more. And then I was vibe coding."*

The structural claim: a single-month phase change in late 2025 when **the correction overhead dropped to ~zero** for a sufficiently broad class of tasks. This is not just "models got better" — it's the threshold at which the *iteration loop* changes shape (from generate → review → edit → retry to generate → accept).

Two consequences Karpathy notes:

1. **"My side projects folder is extremely full"** — when the friction drops to zero, the volume of personal experimentation explodes.
2. The shift was **not visible at the typical user's distance** — most people experienced AI in 2024 as "ChatGPT-adjacent thing." Karpathy stresses on Twitter/X that you have to *look again* in late 2025 because the agentic-coherent-workflow has changed fundamentally.

### Vibe coding raises the floor

The democratisation claim is the load-bearing operational outcome:

- People who could not previously write code can now build working software.
- Engineers who were intimidated by an unfamiliar stack (frontend if they're backend; mobile if they're web; etc.) can now ship across stacks.
- Side-project velocity for individual operators goes up multiple orders of magnitude.

The wiki's [[enterprise-ai-adoption]] page tracks the *organisational* analogue of this; vibe coding is the *individual* analogue.

### What vibe coding is *not*

Karpathy is explicit that vibe coding is **not the same as professional software engineering at agent speed**:

> *"Agentic engineering is about preserving the quality bar of what existed before in professional software. You're not allowed to introduce vulnerabilities due to vibe coding. You're still responsible for your software just as before."*

The danger in conflating them: vibe-coded artifacts shipped to production *as if* they were agentic-engineered carry risks (security, correctness, maintainability) that the vibe-coding loop didn't validate. The wiki tracks this as an open hazard — see [[agentic-engineering]] for the quality-discipline complement.

## When vibe coding is the right tool

- **Side projects.** Personal experiments, weekend builds, hobbyist apps. The Karpathy [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Menu Gen]] story is a vibe-coded artifact; he then *reasoned about* it through an [[agentic-engineering]] lens (and concluded most of it was spurious).
- **Throwaway scripts.** Glue code, one-off data transformations, ad-hoc analysis.
- **Proof-of-concept demos.** Where the goal is to learn *whether* something is possible, not yet to ship it reliably.
- **Education and exploration.** Learning a new framework or library by having an agent walk you through a working example.
- **Stakeholder-influence prototypes for non-engineers.** Per [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]], the canonical PM use of v0 / Lovable / Google AI Studio is to turn a PRD into a clickable prototype *before* asking for engineering allocation, then take the prototype into a product review where stakeholders can touch / feel / move-around the vision. The prototype is **a communication and influence-engineering tool**, not a design artifact. This is vibe coding's *first-class non-engineer professional use* — the floor-raising claim made operational for the PM audience specifically.

## When vibe coding is the wrong tool

- **Production systems handling third-party data, money, or identity.** Karpathy's email-matching-Stripe-and-Google-accounts bug is a vibe-coding-shipped-to-production failure mode.
- **Code that other engineers will maintain.** Vibe-coded code is often *bloaty, copy-paste-heavy, awkward in its abstractions, brittle* (Karpathy's own description) — fine for a one-off, expensive to inherit.
- **Anything that requires correctness verification.** Vibe coding's iteration loop trusts the model's output; for verifiable domains, the more rigorous [[agentic-engineering]] loop (with formal contracts and adversarial testing) is the right pattern.
- **Anything safety-critical.** Same reason as above — the vibe loop doesn't validate against an explicit quality bar.

## Convergence with other wiki claims

| Source | What it adds to vibe coding |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | Original coinage + December 2025 phase change + the floor-vs-ceiling contrast with [[agentic-engineering]] |
| [[2026-04-28-dellacqua-jagged-technological-frontier\|Dell'Acqua et al. 2026]] | The empirical underbelly: vibe-coded output *inside* the [[jagged-frontier]] is genuinely good; *outside* it can degrade performance even relative to the un-AI-assisted baseline |
| [[2026-05-07-anthropic-economic-index-5-learning-curves\|AEI 5]] | Capacity-ceiling caveat: vibe coding works at single-task scale; once tasks compose (multi-step, long-horizon) the ceiling becomes load-bearing, and you need [[agentic-engineering]] |
| [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont\|Nika 2025 (How I AI)]] | The **PM-side worked example** + the **earliest contemporary primary source** for the December 2025 phase change. A Google AI Product Lead, on camera in late November / early December 2025, doing the workflow live (Perplexity → custom GPT → v0 → Veo/Sora → NotebookLM) and treating the tool stack as already-trustworthy. Substantiates *floor-raising* with a non-engineer professional (PM) audience: vibe coding's clickable-prototype pattern as **stakeholder influence engineering**, not just hobbyist iteration. *"PMs that use AI are the ones that are going to take over the role of people that don't use AI."* |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler 2026 (Thoughtworks at QCon London)]] | **Conference-circuit timeline anchor**. Böckeler's year-on-year QCon retrospective dates *"the term vibe coding was about 2 months old"* at QCon London 2025, anchoring the term's coinage to early 2025 from an independent observer (consultancy practitioner). Frames vibe coding as one end of an autonomy spectrum the broader [[agent-harness]] discipline now attempts to widen *safely* — directly compatible with Karpathy's floor-vs-ceiling split |
| [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs\|Thompson 2026 (NYT / The Daily)]] | **75-developer field-report anchor**. The wiki's first cross-industry survey of working software developers — Thompson reports *"a majority outsourcing day-to-day programming to AI"*, with **small startups at ~100% AI-written code** (full-day features now ~30 min, ~20x faster) and **Google at ~40-50%** AI-written code with ~10% overall speedup. Dates the developer-side phase change to *"last 6 months, accelerating in the last 3"* — i.e. November 2025 → February 2026, ~4 months behind Nika's PM-side December-2025 phase change. Vibe coding observed in production at the small-startup floor; the consultant-observer + journalist-observer + vendor-engineer + practitioner vantages now all align on the same transition |
| [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers\|Jassy 2025 (Amazon CEO on HBR IdeaCast)]] | **Pre-coinage CEO anchor for the floor-raising thesis** — the wiki's earliest vendor-CEO statement of the natural-language-coding democratisation prediction. Jassy in May 2025: *"the number of people who are going to be able to be software developers is going to go up exponentially. Because you're going to have these coding apps that allow you to use natural language to describe what you want to go build. And it's going to be very empowering."* Predates [[Andrej Karpathy]]'s vibe-coding coinage by ~12 months and Nika's December-2025 PM-side worked example by ~7 months. The qualifying *"but"* clause (US-education-quality concern: *"30 out of 35 developed countries in efficacy of education"*) anticipates the wiki's [[ai-deskilling]] / [[durable-skills]] concern that floor-raising democratisation depends on a baseline of human capability that may itself be eroding |

## Debates and supersession

- **Is "vibe coding" a derogatory term or a legitimate mode?** When the term first spread on Twitter/X in 2024–25, some practitioners used it dismissively (*"that's just vibe coding, not real engineering"*). Karpathy's [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia framing]] resolves this: vibe coding is a *legitimate mode* (floor-raising democratisation) — the dismissive framing is misplaced because it conflates vibe coding with agentic engineering. The wiki adopts Karpathy's resolution.
- **Does the December 2025 phase change generalise beyond Karpathy's experience?** ~~No second source has yet ingested a parallel first-person account.~~ *Partially answered* by [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] — a Google AI Product Lead doing the workflow live on camera in late November / December 2025, contemporary with Karpathy's named pivot. This isn't a survey or controlled study, but it is a second independent practitioner whose tool-stack is already trustworthy by the date Karpathy retroactively names. The remaining open question is whether a *population-level* signal (survey / empirical study) confirms it across professional audiences; the wiki now holds *two* practitioner anchors at the engineer (Karpathy) and PM (Nika) ends.
- **Will vibe coding always need an [[agentic-engineering]] complement, or will model improvements close the gap?** Karpathy's view: *"I'm hoping that improves… there's nothing fundamental preventing it. It's just the labs haven't done it yet."* If labs add aesthetics-as-RL-reward and agent code stops being *bloaty / awkward / brittle*, the gap between vibe coding and agentic engineering narrows substantially. Open question.

## Related concepts

- [[software-3.0]] — the substrate; vibe coding is the floor-raising mode of Software 3.0.
- [[agentic-engineering]] — the discipline complement; same substrate, professional quality bar.
- [[ai-agents]] — the *intern entities* you vibe-code with.
- [[agent-harness]] — vibe coding can happen with a thin or absent harness; [[agentic-engineering]] requires a substantial one.
- [[jagged-frontier]] — vibe coding inside the frontier is genuinely good; outside it, the iteration loop trusts model output that may be wrong.

## Open questions

- **Empirical measurement of the December 2025 phase change.** Karpathy's account is first-person; a population-level signal would lift this concept's confidence.
- **The vibe-coding-to-agentic-engineering boundary in practice.** When does a vibe-coded side project earn promotion to agentic engineering? Karpathy's Menu Gen example was vibe-coded then *replaced entirely* by a Software 3.0 prompt — a rarer pattern than gradual hardening. Worth tracking which trajectory dominates.
- **Will vibe coding remain the *individual* mode or become the *team* mode too?** Currently it's framed for solo operators. If teams adopt vibe-coding loops collectively (with each member trusting the agent's output without review), the safety implications change substantially. Open.
- **Tooling specialisation.** Will vibe-coding-specific IDEs/tools emerge that are explicitly *not* agentic-engineering-grade (lower friction, weaker guardrails)? The pet-vibe-coding tools that exist today (Replit's Agent, Cursor's vibe modes) hint at this; second sources documenting the trajectory would be useful.
