---
type: source
kind: video
title: "Systems Thinking for Leaders: Designing Solutions That Work"
author: ["MIT Sloan Executive Education"]
publisher: "[[MIT Sloan Executive Education]]"
section: "YouTube webinar (MIT Sloan Executive Education channel)"
url: "https://www.youtube.com/watch?v=wSuQQYv-E64"
date_published: 2026-05-15
date_ingested: 2026-05-18
length: "~57:48 minutes (transcript ~546 lines)"
raw: "../../raw/videos/2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work.md"
tags: [systems-thinking, system-dynamics, policy-resistance, feedback, causal-mapping, mental-models, management-flight-simulators, project-management, healthcare-policy, mit-sloan, sterman, forrester, business-dynamics, group-modeling, climate-interactive, enroads]
roles: [ceo, coo, cso, tech-lead, transformation-lead, rd-director, innovation-lab-lead, strategy-consultant]
relationships:
  - type: supports
    target: 2026-04-28-bansal-birkinshaw-systems-thinking
    via: "Sterman's MIT system-dynamics lineage is the discipline Bansal & Birkinshaw cite as one of the intellectual foundations of systems thinking (Forrester → Senge → modern systems-thinking literature); Sterman delivers a 58-min in-depth treatment of the feedback-and-policy-resistance machinery underneath Bansal & Birkinshaw's three-modes-of-innovation framing"
  - type: instance-of
    target: systems-thinking
---

# Sterman — Systems Thinking for Leaders: Designing Solutions That Work

> *"In today's fast-changing and highly interconnected world, many of the most persistent challenges leaders face arise from unintended consequences of earlier decisions. Actions that succeed in the short run often create new risks and long-term failure. Leaders increasingly recognize systems thinking as a core capability… The challenge is how to move from slogans about systems thinking to practical tools and methods to identify high-leverage actions that lead to sustained success."* — [MIT Sloan Executive Education webinar description](https://www.youtube.com/watch?v=wSuQQYv-E64)

## TL;DR

A 58-minute MIT Sloan Executive Education webinar by **John D. Sterman** (Jay W. Forrester Professor of Management, MIT Sloan; director of MIT Sloan Sustainability Initiative), promoting the *Business Dynamics* 5-day executive course (June 8–12, 2026 on campus). Sterman is the wiki's **second source on [[systems-thinking]] and the first from inside the canonical MIT system-dynamics lineage** (Forrester → Senge → Sterman). The webinar directly addresses the open question flagged on the existing [[systems-thinking]] page — *"deeper Senge and Forrester texts would strengthen the concept"* — by delivering the modern in-house MIT articulation.

The structural payload, in one sentence: **policy resistance** is the universal failure mode the talk diagnoses (well-researched, expert-vetted solutions either fail outright or work in the short run and the problem returns elsewhere), the mechanism is a mismatch between **the open-loop mental model managers use** and **the feedback-rich complex system the world actually is**, and the toolkit is **causal mapping** (qualitative) plus **management flight simulators** (quantitative) deployed in **group-modeling processes** that *"put the system in the room."*

## What was actually ingested

Full 58-minute webinar transcript (546 ASR segments; auto-generated English captions; no chapters in the YouTube metadata). Acquired via the [`youtube-transcript-skill`](../../.claude/skills/youtube-transcript-skill/SKILL.md) Playwright DOM-ride path. Light ASR cleanup applied (full list in the raw file's `notes:` block): canonical fixes were *"Sturman" → "Sterman"* (spoken many times), *"JW Forester" → "Jay W. Forrester"*, and *"Sully" → "Sully Sullenberger"* on first mention. Light um/uh stripping; timestamps preserved verbatim. Source URL canonical; channel attribution is *MIT Sloan Executive Education*; the speaker on screen is John D. Sterman.

## Key claims

### Policy resistance is the universal failure mode (and it's 500 years old)

The webinar's load-bearing concept is **policy resistance**: a problem is identified, research is done, experts are consulted, a solution everyone agrees is terrific is implemented — and *either it doesn't work, or more commonly and insidiously it works in the near term but the problem returns a little later somewhere else.* Sterman calls this *"extremely common and extremely discouraging."*

Five worked examples named on a single slide:

| Example | Mechanism |
|---|---|
| **Urban traffic / build more roads** | Near-term: driving becomes more attractive → people drive more, abandon transit, move farther out. Often congestion gets *worse*, not better. |
| **US healthcare cost containment** | ~18% of US GDP, most expensive system in the world by any measure. *"Despite decades and decades of efforts to contain costs and slow down the cost escalation, none of this is really working. This is a major example of policy resistance over at least 70 years now."* |
| **M&A** | Promoted on cost-savings/synergy logic; often destroys value for the acquiring firm. |
| **Process improvement (TQM / Six Sigma / BPR)** | Tools work; vastly more attempts fail than succeed, breeding cynicism about the next one. |
| **Projects (NPD / software / construction)** | *"Typically late, expensive, and wrong (don't meet customer requirements)."* |

Historical anchor: Sir Thomas More, *Utopia* (1516): *"it will fall out as in a complication of disease that by applying a remedy to one sore you provoke another. And what removes one ill symptom produces others."* — a 500-year-old description of policy resistance.

### The mechanism is a mental-model mismatch, not "the world is complex"

Sterman is explicit that policy resistance is **not** caused by complexity per se. *"It's not just that the world is complex. It's that there's a mismatch between the mental models that we use to come up with our solutions for difficult problems and the complexity of the real world."*

The named bad mental model is the **open-loop** one: Issue → Gather Data → Evaluate Alternatives → Select Optimal Choice → Implement. *"Problem solved."* Sterman's verdict: *"I don't know about you, but no project that I've ever done — from co-chairing the project to develop the new building for the Sloan School of Management to putting together and shopping for the grocery list — has ever gone that way. Instead… there's constant iteration, planned and unplanned iteration where we discover problems, rework that has to be done, and we have to go back."*

The reality is **feedback**: *"You make decisions. Your decisions change the world in various ways and that creates new information that conditions your next decisions in a never-ending feedback cycle."* The bicycle is the load-bearing analogy — at any instant, you need to know which way to turn the handlebars, and you can't know unless you have feedback telling you where you are relative to your goal.

### "There is no such thing as a side effect"

A signature Sterman line, restated three times in the webinar:

> *"There's no such thing as a side effect in reality. There's no such thing. People talk about it all the time, but there's no such thing. There's just effects. You make decisions and your decisions have multiple effects."*

The corollary is rhetorical: when managers explain failure as *"that was a side effect, that was an unintended consequence, nobody could have anticipated that,"* what they are *"really communicating to you is how narrow and inadequate is the mental model they're using to make those decisions."* Bad explanations are mental-model diagnostics.

### Multi-stakeholder embedding closes the system-thinking case

Even if your own mental model were complete, you are not the only actor: *"You have your employees, your customers, the financial markets, your suppliers, the people in the communities in which you operate, and they all have their own goals. But since we all live in the same world, **when you pull the state of the system closer to your goals, you're almost certainly pulling it away from theirs.** And they aren't just going to sit there. They're going to take their own actions and try to pull the system back. Of course, they also have limited mental models, which means their actions are going to generate unintended so-called side effects."*

This is the dynamic-stakeholder articulation of why systems thinking is required at the operational scale, not just the strategic scale.

### Causal mapping: the US prior-approval healthcare case

Sterman walks the audience through a **causal map** of the US prior-approval / preferred drug list / step therapy machinery as a worked example. Empirical anchors:

- **Prior authorisation administrative cost in the US: $35 billion per year as of 2024.** ($11,000 per clinician per year; $20–30 per request.)
- **1996 study**: limiting drugs via prior approval, formularies etc. *"actually has the unintended effect of raising medical costs."*
- **Earlier-2026 meta-review of 25 evaluative studies**: authorisation requirements associated with delays in care, **disease exacerbation, preventable hospitalizations, prolonged hospital stays, and lower rates of disease-free survival** — *"medical jargon for more people died as a result of prior approval."*

Structurally: managers see the **above-the-waterline balancing loop** (costs up → tighten approval rules → lower drug/procedure unit cost → lower total costs). Below the waterline: appropriateness and timeliness of care decline → health outcomes deteriorate → patients return sicker → total costs rise. The causal-map technique is the named mechanism that makes the below-waterline portion visible to managers in a group setting.

### Management flight simulators: the project-sim worked example

Sterman demos a project-management simulator (live, in the webinar) for a consumer-electronics product launch (named *Kill the Competition* in the demo). Setup: 72,000 person-hours for detailed design + 33,600 for high-level design; budget-driven hire cut from 75 to 70; scope creep accepted to chase a 3.6% market-share lift; *"do it right, but get it done"* management pressure; work week climbs to 78 hours. By the end:

- Detail-design phase needs 166 people, simulator allows only 120;
- *"Reduce project scope by 50% of non-essential features? Whoops, can't do that. Got to keep all those bells and whistles in there"* — the sim's realistic constraints don't let the player escape the trap;
- **Final defect rate: 25%, against a target of <1%.**
- **Net present value of losses: ~$50 million.** Product fails in the marketplace.

Sterman: *"What you just saw here is actually quite common, and a significant amount of research shows that this kind of outcome is typical and often leads to outcomes that are far far worse than what you saw here, including very commonly disputes between contractors and customers, between contractors, subcontractors and suppliers that often escalate into legal action. I've been an expert witness in half a dozen of these lawsuits or arbitrations over projects gone bad. And the lawyers are the only ones who really win."*

The pedagogy thesis: *"Lectures don't work. Research shows that showing people research doesn't work."* Mental models held about complex systems are *"very very powerful and they're often strongly reinforced by our everyday experience"* — the short-run feedback of bad decisions feels rewarding; the long-delayed unintended consequences appear disconnected from the original choice. So the only way to update a mental model is to **let people experience the consequences themselves in a costless simulated environment.**

The **Sully Sullenberger** analogy operationalises this: *"He was a certified simulator instructor… After that amazing successful ditching in the river with nobody killed, one of his comments was, 'Well, you know, I've never experienced a bird strike that knocked out both engines, but we practiced that in the simulator many many times.'"*

### Other named successful applications

- **Kidney dialysis anemia treatment** (SDM alum, MIT Sloan) — flight-simulator-style intervention for frontline clinicians, *"saved millions of dollars and many many lives."*
- **Enroads climate-policy simulator** (Climate Interactive collaboration) — peer-reviewed assumptions but users can change them; *"there's a lot of uncertainty about the economy, the energy system, and the climate. And so you get to change the assumptions."*
- **Other application domains named**: high-tech, auto, pharma, drug development, construction, chemicals, project management, healthcare, energy policy, public health.

### Qualitative tools matter even without formal simulation

Not every project requires a full simulation model. Causal mapping in a **group modeling process** delivers value in two ways:

1. **Substantive insight** — people gain deeper understanding of what's going on by mapping the system together.
2. **Capability development** — the meta-impact is that participants develop their own systems-thinking skills.

The operational saying is *"you want the system in the room."* That includes traditional adversaries — *"consumer groups who are protesting that your products are not made in a sustainable way or with a living wage for the folks way upstream in your supply chain. You want those people in the room so that collectively they're much more able to identify the so-called side effects."*

### "Sage on the stage" → "guide on the side"

Sterman's facilitator-stance claim is one of the more durable practitioner reframings in the webinar:

> *"We need to get away from the sage on the stage and instead the role of the facilitator and your role is to be a guide on the side to catalyze the learning for the group."*

He explicitly applies it to himself: *"That's a terrible thing. I'm not the expert. I'm here to help catalyze your learning."* The implication for in-house systems-thinking interventions: the senior person convening the group-modeling exercise must *not* perform expertise; otherwise the group surfaces less, the system stays *outside* the room, and the causal map ends up reflecting the senior person's pre-existing mental model — which is exactly the failure mode the intervention was supposed to fix.

### George Box on models

Quoted in passing, in defence of accepting that *all systems-thinking interventions use simplified models*:

> *"All models are wrong, some models are useful."* — George Box

The defensive value of having this on the record: when intuition rebels against a simulator's output — *"that's not right, your model is wrong"* — Sterman observes the rebellion is *expected* and *predictable*, because the manager's mental model has been reinforced by short-run feedback for years. Updating it requires repeated experience in the safe space the simulator provides.

## Linked entities and concepts

- Existing concept page directly anchored: [[systems-thinking]] — Sterman is the wiki's second source on this concept; updates the page from confidence 0.75 / 1 source → 0.80 / 2 sources; closes one of the open questions ("deeper Senge and Forrester texts").
- Pre-existing entity referenced and now reinforced: [[Jay Forrester]] — the discipline's founder; Sterman holds the chair named for him.
- **Dangling** (single-source mention, deferred per author-entity rule):
  - **John D. Sterman** (speaker; Jay W. Forrester Professor of Management, MIT Sloan; director of MIT Sloan Sustainability Initiative; co-founder of MIT's Institute for Data Systems and Society faculty)
  - **MIT Sloan Executive Education** (publisher / channel) — first wiki source from this channel.
  - **Climate Interactive** (collaborator on the Enroads climate-policy simulator)
  - **Sully Sullenberger** (named in passing as a simulator-pedagogy anchor)
  - **George Box** (statistician, quoted for *"all models are wrong"*)
  - **Sir Thomas More** (named for the *Utopia* 1516 quote)
  - **MIT Institute for Data Systems and Society** (organisational unit)

## Source-quality flag

- **Genre**: vendor-promotional webinar by MIT Sloan Executive Education, recorded May 15 2026, for the *Business Dynamics* June 8–12 2026 on-campus course. The course pitch is the framing; the substantive content (~50 of the 58 minutes) is a high-quality first-person primary articulation of the MIT system-dynamics lens.
- **Speaker authority**: John Sterman is the canonical academic figure in MIT-system-dynamics — Jay W. Forrester Professor of Management; *Business Dynamics: Systems Thinking and Modeling for a Complex World* is the standard graduate textbook.
- **Empirical anchors**: live causal map (US prior approval), $35B/year admin-cost figure (2024), 1996 study + 2026 meta-review of 25 studies (cited but not named in body), live management-flight-simulator demo with named numerical outcomes ($50M NPV loss, 25% defect rate), Enroads + dialysis case studies named in passing.
- **Confidence calibrated at 0.82** — primary-source first-person delivery by the discipline's leading living figure; promotional context is light caveat, not material; empirical claims are mostly cited rather than original.

## Why this matters to this wiki

- **Closes a flagged open question on [[systems-thinking]]** — the existing concept page named *"deeper Senge and Forrester texts would strengthen the concept"* as an open item. Sterman is the institutional successor at MIT and the canonical living voice of the discipline; this source is the closest the wiki can get without ingesting Sterman's textbook.
- **Adds operational toolkit, not just framing.** The first source ([[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw 2025]]) gave the wiki the *three-modes-of-innovation* framing (breakthrough / design / systems). Sterman supplies the *machinery underneath the systems mode*: policy resistance, feedback as the load-bearing primitive, causal mapping, group modeling, flight simulators, the "no such thing as a side effect" reframing.
- **Cross-domain role-relevance** — explicitly named role tags reflect that systems thinking is non-specialist: `ceo` (multi-stakeholder pulling-system-back claim), `coo` (project management failure mode), `cso` (M&A policy-resistance example), `tech-lead` (project-management simulator runs straight against typical engineering-leadership decisions — staff cuts, scope creep, "do it right, but get it done"), `transformation-lead`, `rd-director`, `innovation-lab-lead`, `strategy-consultant` (group-modeling facilitation as a consulting capability). The W&W `dynamic_capabilities:` lens does not apply directly — this is upstream methodology, not a digital-transformation capability — so no W&W tags applied per the *skip-rather-than-stretch* rule.
