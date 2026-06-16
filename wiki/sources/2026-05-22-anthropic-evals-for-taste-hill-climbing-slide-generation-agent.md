---
type: source
kind: video
title: "Evals for taste: Hill-climbing a slide-generation agent"
author: ["Anthropic"]
publisher: "Anthropic — Claude YouTube channel (talk recorded at AI Dev 26 x San Francisco; 22 May 2026)"
url: "https://www.youtube.com/watch?v=v9FTCvkV_a0"
date_published: 2026-05-22
date_ingested: 2026-05-25
length: "~39:16 minutes (auto-generated English captions via yt-dlp fallback; 1,053 deduped ASR segments)"
raw: "../../raw/videos/2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent.md"
tags: [anthropic, claude-channel, ai-dev-26, evals, evals-for-taste, hill-climbing, slide-generation-agent, code-based-graders, model-based-graders, human-graders, llm-as-judge, pairwise-comparison, multi-judge-consensus, judge-calibration, qa-loop-adversarial, opus-4-7, sonnet-4-7, manage-agent, python-pptx, eval-saturation, autoregressive-judge-ordering-bug, agent-development-lifecycle, vendor-altitude-evals-doctrine]
dynamic_capabilities:
  - digital-sensing/identifying-needs
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway
    via: "**Same-day same-conference paired evals anchors at opposite vendor-altitudes** — both at AI Dev 26 x SF, both published 22 May 2026. The Anthropic talk (this source) is the *model-vendor-side* evals doctrine, working the slide-generation agent worked example through code-graders + judge-graders + the QA-loop adversarial pattern + the autoregressive-judge-ordering bug + model-switching (Sonnet 4.7 → Opus 4.7) as alternative to prompt-engineering. [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan / Cline]] is the *customer-of-model-vendor-side* evals doctrine: 'we adopted Stanford terminal-bench, hill-climbed our harness, and beat Claude Code on Opus 4.5 evals' — using the same eval-discipline vocabulary (graders / hill-climbing / harness-as-one-of-three-things-being-tested) to compete with the model vendor's own agent product. The paired sources lay out **what each side of the model-vendor-vs-coding-agent-vendor relationship looks like from inside the eval loop**: Anthropic shows how to define + calibrate + iterate; Cline shows what it looks like when a competitor uses the same discipline to outperform the model vendor's reference agent. The wiki's clearest single-day vendor-vs-customer-of-vendor evals-discipline pair."
    confidence: 0.85
  - type: supports
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "**Operational instantiation of Chase's *evals-as-gradient* framing.** Chase (Interrupt 26, 21 May 2026): *'the evals that you write act as a forcing function. Those evals are providing a similar type of this training gradient'* — articulated at the vendor-CEO three-layer-continual-learning altitude. This Anthropic talk (22 May 2026, one day later) is the *operational worked example* of the same claim at the practitioner-altitude: define code-graders + judge-graders → run on the slide-gen agent → identify failure modes → update system prompt (or switch model) → run again → measure improvement → loop. The hill-climbing diagram on stage is *literally* the gradient-descent metaphor Chase invokes. Together the two sources lock in the *evals-as-gradient* claim at vendor-CEO + vendor-engineer altitudes within 24 hours."
    confidence: 0.85
  - type: supports
    target: 2026-05-18-wolfe-agent-evaluation-detailed-guide
    via: "**Paired vendor-engineer + article-altitude anchors on the same eval-discipline territory.** Wolfe's *Agent Evaluation: A Detailed Guide* (Substack, 18 May 2026) is the wiki's deepest article-altitude treatment — taxonomies of graders (code / model / human), tau-bench / terminal-bench / SWE-bench coverage, LLM-as-judge calibration, swiss-cheese-evaluation pattern. This Anthropic talk (22 May, four days later) is the *vendor-side conference-talk altitude* on the same territory — same three grader categories (code / model / human), same calibration concerns, same judge-ordering-bug warning, plus a live slide-gen agent worked example Wolfe's article doesn't have. The two sources together give the wiki **paired article + conference-talk anchors on practitioner-altitude evals discipline** that should both be referenced from the agent-development-lifecycle concept page."
    confidence: 0.8
  - type: supports
    target: 2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering
    via: '**The *judge-calibration is fickle* observation operationalised at the model-vendor altitude.** Sinclair / Ivers / Benitez (SEI/CMU, 21 May 2026): *"under-specification is the bad-practice-AI-magnifies-most"* — vague specs let AI fill in the blanks badly. This Anthropic talk extends the under-specification observation into the *judge-spec* layer: a model-grader with the prompt *''evaluate if this is a good slide deck (0-5)''* with no anchored examples will rate an obviously-bad slide deck at 2.8-4.0 because it has nothing to anchor on. The fix: ground judges with explicit examples of what 0 looks like + 5 looks like. The Anthropic-side framing of *under-specification of judges* is the institutional-research-centre framing of *under-specification of agents* applied one layer up. Both anchor on **specs are load-bearing, more so under AI**.'
    confidence: 0.75
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "**The hill-climbing-the-harness pattern operationalised at the vendor-altitude.** Karten & Zhang (academic paper, 11 May 2026): formal p/G/K/M continual-harness-adaptation framework — *the agent edits its own harness based on eval feedback*. This Anthropic talk shows the *manually-driven equivalent*: human engineer iterates the system prompt + grader set + model choice based on eval scores; same hill-climbing loop, human-in-the-loop variant. The wiki now has paired anchors on **continual-harness-adaptation as the operational substrate of evals-driven agent improvement** at both academic (Karten/Zhang automated) and vendor-engineer (this talk, human-driven) altitudes."
    confidence: 0.7
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "**The *cross-modal evals as Skillify-built-in* claim Hu made at CS153 gains an operational worked example.** Hu (CS153, 20 May 2026): cross-modal evals (Opus 4.6 + GPT 5.5 + Deepseek V4 cross-evaluating with structured ratings fed back into the original sub-agent for iterative improvement) as a forward-looking Skillify-built-in feature. This Anthropic talk (22 May, two days later) is the *manual-equivalent* at the slide-gen-agent worked-example altitude: human iterates, judges (model-based graders) score, judge-calibration is fickle, multi-judge consensus underrated — exactly the substrate Hu's cross-modal-evals feature is automating. The vendor-side practitioner talk and the YC-partner-doctrinal talk converge on **multi-judge / cross-judge evaluation as the load-bearing eval-quality mechanism for non-deterministic-output systems**."
    confidence: 0.7
  - type: supports
    target: 2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering
    via: "**Same-conference companion talks** (both at AI Dev 26 x San Francisco; Ng on 20 May, this Anthropic session on 22 May). Ng frames the meta-shift (PM-bottleneck + 100%-AI-coding norm + parallel-skill-development); this Anthropic session is the *operational practitioner-track session* on one of the *complementary human skills* Ng names — eval-design-and-calibration. The pairing illustrates the conference's intended structure: Ng-altitude keynote on *the shift* + practitioner-track sessions on *the specific skills the shift requires*. AI Dev 26 is now anchored on the DeepLearningAI side (Ng + Khan) and on the Claude-channel side (this Anthropic session) — three sources from the same conference, three vantages."
    confidence: 0.6
---

> *Built rubric-driven replayable eval system from real user projects giving quality, cost, latency, error, token signals in under 6 hours per model change. Evolved into dev flywheel powered by real user dissatisfaction signals.*

# Anthropic / Claude channel — Evals for taste: Hill-climbing a slide-generation agent (AI Dev 26 x SF)

A ~39-minute Anthropic practitioner-track session at AI Dev 26 x San Francisco, published on the [[Anthropic|Claude]] YouTube channel — 22 May 2026. **Speaker not named on stage or in the channel metadata** (see caveats); presented as an Anthropic-employee session on building evals for a slide-generation agent (the *evals for taste* worked example). Tightly-paced 45-minute conference slot covering definitional grounding + grader-type taxonomy + live slide-gen agent demo + hill-climbing iteration loop + judge-calibration warnings + the autoregressive-judge-ordering bug.

## TL;DR

- **Definitional grounding**: *"Evals are systematic tests that measure how well an AI system performs on a specific domain or use case... made up of tasks that define certain scenarios that then encode certain expectations through the grading logic."* Evals are the *bridge between 'it seems to work' / 'it feels worse today' vibes and something actionable.* Generic public benchmarks (SWE-bench, terminal-bench, t-bench, BrowseComp, OSWorld, ARC-AGI-2) measure *general capabilities*, not *your specific use case* — *"build your own evals."*
- **The grader-type taxonomy** (the talk's most-reusable framing): three categories.
  - **Code-based graders** — deterministic: string match, regex, fuzzy match, tool-call checks. *"Fast, cheap, deterministic, but brittle and lacks nuance."* Useful when the property is binary or quantifiable (e.g. *was a slide deck produced? does it have 5 slides? how many emojis?*).
  - **Model-based graders (LLM-as-judge)** — rubric-based reasoning. Three sub-patterns: (a) **rubric scoring** (*"is this slide high-quality (0-5)?"*), (b) **pairwise comparison** (*"which of these two outputs do you prefer and why?"* — *"underrated in my opinion"*), (c) **multi-judge consensus** (*"three judges score independently and majority wins"* — introduces some determinism by averaging out non-determinism). Flexible, scalable, nuanced; nondeterministic, costs more, *needs calibration which is not easy at all*.
  - **Human graders** — highest quality, most nuanced; *"the graders you will use the least because they're incredibly expensive and slow"* — mostly for AB testing and spot-checking.
- **The slide-generation agent worked example** (the talk's load-bearing demo). Built with **Anthropic's `manage_agent` agent SDK** + `python-pptx` shell tool + Sonnet 4.7 as the default model. Pre-built **code graders** (emoji count, cluttered-slides, slide-count, slide-with-image, small-fonts, text-heavy) + **judge graders** (color contrast, image, layout, text — each 0–5). The hill-climbing arc on stage:
  1. **Naive prompt** (just "you are a slide generation agent, create a PowerPoint at this location") → output has overlapping text, weird coloring, emojis used as decoration. Judge scores 2.8–4.0.
  2. **Typography + density rules added** (specific font sizes by tier, layout/density rules, *"never use thin accent lines in the titles and don't pepper slides with emojis as decorative icons"*) → improvement in cluttering and emoji count.
  3. **Diagram requirement added** (*"every slide must include at least one generated diagram or chart inserted as an actual image"*) → slides get visually richer; image judge starts scoring.
  4. **QA-loop adversarial pattern added** (see below) → fix-and-verify cycle improves all four judges to 4.2–4.4.
  5. **Model switch to Opus 4.7** with just the *naive base prompt* (no typography rules, no diagram requirement) → *"immediately significantly better than the Sonnet one"*; Opus knows not to use emojis without being told; layout 4.2 / color 4.8 / title-body coherence 4.4. **The model upgrade clears most of what the prompt-engineering iteration achieved.**
- **The QA-loop adversarial pattern** (the talk's most-portable operational primitive): *"Required QA loop. Assume there are problems. Your job is to find them. Approach QA as a bug hunt, not a confirmation step... After writing the deck, convert it to images. Inspect every slide image yourself. Fix issues, rerender, reinspect. Do not stop until you've completed at least one fix-and-verify cycle."* The framing-the-agent-as-adversarial-reviewer-of-its-own-output construct is named on stage as the wiki's clearest operational primitive for *self-criticism as an eval substitute when external evals are slow*.
- **The autoregressive-judge-ordering bug** (the talk's most-pointed warning): *"It works auto-regressively, right? So if it's anchored on a four, it will do anything it can to argue why it should be a four... Even if it's like extremely bad, if it should be like a one, it will still say 'oh it is good for these and these reasons because it needs to justify the four that it put out.'"* The fix: **always ask for the reasons FIRST, then the score**. *"First you say, give me a bunch of reasons. Give me pros, give me cons, give me reasons why it should be high, give me reasons why it should be bad. And then based on all of those reasons together, you make a final decision."* The wiki's clearest single articulation of the *reasoning-before-rating* discipline for LLM-as-judge setups.
- **The judge-calibration problem** named as load-bearing: *"It's not because you have set up your evals once that they are now like the ground truth. Evals over time they can evolve, they need to be a living artifact."* Initial judge scores of 2.8–4.0 on an obviously-terrible slide deck signals that the rubric is too generic; the fix is **anchoring**: explicit examples of what 0 looks like + 5 looks like. *"This calibration of how your agent should behave and how your judges should judge is really something very fickle — you should spend proper time trying to find the ways on how you should make this happen."*
- **Eval saturation** named as a real concern: *"If you ever hear people talk about saturation of evals, that's basically what they mean — the eval is not giving any more relevant information that we can act on."* Reinforces the *evals as living artifact* framing.

## What was actually ingested

The full ~39:16 transcript via the yt-dlp fallback path (youtube-transcript-skill Playwright path failed at 60s timeout — the recurring panel-render failure mode). Custom VTT dedupe with the hour-aware `<\d\d:\d\d:` regex parser (same parser from the Caldwell + Ng ingests). 1,053 deduped ASR segments spanning the full 39:09 runtime. Stage cues and audience interjections retained. Full raw at [`raw/videos/2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent.md`](../../raw/videos/2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent.md).

**Speaker not named on stage or in channel metadata.** The transcript opens *"Hello, hello, hello. Good afternoon, everyone."* and never introduces the presenter by name. The channel metadata (channel = *Claude*, the Anthropic-product YouTube channel aliased on the [[Anthropic]] entity page) is the only identifying signal. The session is presented as an Anthropic-employee practitioner-track session at AI Dev 26 x San Francisco, with the slide-gen agent running on the **`manage_agent` SDK** (which the speaker references in passing as *"the same thing we did in the session before lunch"*) + Sonnet 4.7 / Opus 4.7 as models — both signals consistent with the Anthropic-vendor identity. **Flagged in caveats**; if a separate channel or write-up surfaces with the speaker's name, the source page should be renamed and the entity Dangling updated.

## Substantive content

### 1. Why evals beat vibes (~0:19–7:57)

The talk opens with the definitional case: evals are *systematic tests that measure how well an AI system performs on a specific domain or use case*. The contrast that motivates building them:

*Without evals*: customer complains *"something is off with this new model switch"* → you flying blind in a reactive loop → manually debug logs → fix one issue, create three others → can't distinguish genuine feedback from noise → no way to verify improvements or regressions on anything you've done.

*With evals*: you have clarity on what success looks like (forces you to formalise expectations); you iterate on optimal agent configs; you adopt new models faster (compare per-eval rather than per-vibe); you make problems visible before launch.

The model-vendor caveat the talk is honest about: *"Every time a new model releases, we always list a bunch of evals — this is what we achieved, what our models achieve, we compare them to other models, we compare them to competitor models. There's always a few usual suspects."* SWE-bench, terminal-bench, t-bench, BrowseComp, OSWorld, ARC-AGI-2 etc. give *general* signals but *"if you're building something agentic, this doesn't really say much for your specific use case."* The takeaway: model-vendor benchmark cards are useful for general orientation, *not* for your-agent-specific decisions.

The flow that places evals in the dev cycle: test cases → write prompt → test against tasks → refine → loop → ship. *"Over time it has gotten a little bit more complex with now agents coming into the loop with tool calls, skills, all the different ways to optimize your context — so it's also way more levers that you can pull to make changes, which makes it once again more important to have evals."*

### 2. The grader-type taxonomy (~7:22–12:53)

The talk's most-reusable framing. Three categories, each with a clear trade-off:

**Code-based graders** — deterministic: string match, regex, fuzzy match, tool-call checks. *"Pretty similar to a unit test as you might know in software engineering."* **Advantages**: fast, cheap, deterministic. **Drawback**: brittle and lacks nuance. *"Sometimes this is absolutely the way we want an agent to behave — for example, you want to make sure that in the end there is a slide deck present. Deterministic check. But if you want to check on what's the quality of this slide deck, this is way more nuanced — you cannot easily encode this in deterministic checks."*

**Model-based graders (LLM-as-judge)** — *"rubric-based reasoning."* Three sub-patterns the talk names:

- **Rubric scoring**: *"Is this slide high-quality (0-5)?"* — generic but generic-leads-to-generic.
- **Pairwise comparison**: *"You take two outputs and ask the model which one of the two do you prefer and why?"* — the speaker singles this out as *"underrated in my opinion."* Especially useful when you don't have a clear way of defining what makes a better output but you can recognise it when compared.
- **Multi-judge consensus**: *"Take like best-of-three: three judges score independently and majority wins."* The speaker frames this as *introducing determinism by averaging non-determinism*: *"if you run [a single judge] 100 times, a few times it might say 'oh this is great' and a few other times might say 'ah it's not that great.' If you have multi-judge consensus you're basically assuming let's put more compute into this and see what the majority of our judges' consensus is."* **Unlocks flexibility + scalability + nuance**; but nondeterministic, costs more, *requires calibration which is not easy at all*.

**Human graders** — highest quality, most nuanced. **The category the speaker is most explicit about being expensive**: *"These are probably the graders that when you're building these agentic systems you will be using the least, because they're incredibly expensive and slow."* Best for AB testing and spot-checking, not for continuous-eval loops.

### 3. The slide-generation agent worked example (~13:14–25:00)

The talk's load-bearing live demo. Stack: Anthropic's `manage_agent` SDK + a shell tool with `python-pptx` pre-installed + Sonnet 4.7 as the default model. The agent's job: *"You are a slide-generation agent. When the user gives you a topic, create a PowerPoint file at this location."* Pre-built grader sets (in `code/` and `judge/` directories of the workshop repo):

**Code graders** (the speaker calls these *quite straightforward — just count things in the slide deck*):
- `emoji_count` — *"how many emojis present in the slide deck"* (chosen because emoji-spam is a known failure mode)
- `cluttered_slides` — *"how many shapes do we see on these slides"*
- `slide_count` — *"we always ask for five slides, making sure that you have five slides"*
- `slides_with_image`, `small_font_slides`, `text_heavy_slides`

**Judge graders** (each gives a 0–5 score, with a system prompt specifying what to focus on):
- `color_judge` — *"judge what's the color contrast"*
- `image_judge`, `layout_judge`, `text_judge` — each scored 0–5

The hill-climbing arc the speaker demos on stage:

**Iteration 0 — naive prompt**. Output has overlapping text, dollar signs in odd places, teal-heavy color scheme, emojis used as decorative icons. *"This is not the best slide deck you guys have ever seen, but it's a good start — at least there's a slide deck, there's five slides."* Judge scores 2.8–4.0 — *"honestly quite high given the slide deck that we have seen"* — which the speaker flags as the **judge-calibration problem** (see §5).

**Iteration 1 — typography + density rules + AI-tell avoidance**. The system prompt now specifies:
- *"slide title should be this size, section header this size, body this size, caption this size"*
- *"keep the body text concise, leave breathing room, left-aligned paragraphs"*
- *"avoid AI-generated tells — never use thin accent lines in the titles and don't pepper slides with emojis as decorative icons"*

Result: visually cleaner, no dollar-sign artifacts, more consistent coloring. *Code-grader signal*: emoji count drops from 4 → 0 (mostly); cluttered-slides drops from 2 → 0; small-font slides still 4 (acknowledged as not fully fixed). Critically, the speaker also flags that one judge actually got *worse* — *"emoji count 20, I'm wondering where they are, I haven't seen them actually"* — which **flags a grader bug worth investigating**, not a model regression.

**Iteration 2 — diagram requirement added**. *"Every slide must include at least one generated diagram or chart inserted as an actual image."* Now slides have charts (salary-negotiation comparison, etc.). The image-judge now has something to score (3.88/5). *"I think this looks immediately way better just in the way that it's kind of grounded in some actual facts now instead of just waffling its way through the slide deck."*

**Iteration 3 — QA-loop adversarial pattern added** (see §4 below). Slides become more readable; image is bigger; *all four judges score 4.2–4.4* — *"we're on a good track."*

**Iteration 4 — model upgrade to Opus 4.7 with just the naive base prompt** (no typography, no diagram requirement, no QA loop). *"Immediately significantly better than the Sonnet one."* Opus *"just doesn't use any emojis — it kind of knows that if you want to make a slide deck about salary increase, emojis are probably not right place to put them."* Image judge 5/5 (despite no image actually present — a calibration-bug signal), layout 4.2, color 4.8, text 4.4. **The model upgrade clears most of what prompt-engineering iteration achieved**, with a calibration-quality warning attached.

### 4. The QA-loop adversarial pattern (~28:02–30:00)

The talk's most-portable operational primitive. The framing: *"For coding, this is quite intuitive — you create an agent that's actually writing the code, and then you add a second agent that's looking at the code that has been written and just criticises it. So it's basically saying this is bad, this is bad, this introduced a bug, this is not according to standards — and then that part of the feedback you give back to your original agent."* The same pattern applied to the slide-gen agent:

> *"Required QA loop. Assume there are problems. Your job is to find them. Approach QA as a bug hunt, not a confirmation step... After writing the deck, convert it to images. Inspect every slide image yourself. Fix issues, rerender, reinspect. Do not stop until you've completed at least one fix-and-verify cycle."*

The framing-the-agent-as-adversarial-reviewer-of-its-own-output construct is named on stage as the wiki's clearest operational primitive for *self-criticism as an eval substitute when external evals are slow*. Implementation note: requires multimodal (the slide-gen agent converts the deck to images and inspects them), and the loop terminates on *fix-and-verify-completed*, not on *no-issues-found* — actively pushing the agent away from confirmation-bias.

The multi-agent extension the speaker mentions (~36:33): *"You can have like multiple agents also doing the verification part where you have like one agent that is like finding all of the issues and then the other one is like refuting those."* Adversarial creator + critic + meta-critic — the wiki's clearest gesture at *N-agent debate as a calibration mechanism* in the eval context.

### 5. The judge-calibration problem (~20:25–25:34)

The talk's most-philosophically-loaded section. The speaker keeps surfacing the same pattern: judges return numbers that *don't match the human eye's assessment*. Examples:
- Initial 2.8–4.0 scores on the obviously-terrible Iteration-0 slide deck
- Image-judge 5/5 on an Opus 4.7 output with no image present
- *"Text heavy slides — surprisingly. Still small font slides. I think that's fine."* The speaker recalibrates *what counts as text-heavy* mid-demo

The root cause the speaker names: *"With this judging what we have done here is actually quite problematic. We basically say 'give a score from 0 to 5' and for text 'well the title should be simple and clear, for main content avoid too many text and keywords' — but it has nothing to anchor on. It doesn't really know what good looks like in this case. It doesn't know what bad looks like."*

The fix: **anchoring with explicit examples of what 0 looks like + 5 looks like**: *"I would for example say what could help is, this is a bad example — let's say you have a zero, like everything is just awful, these are some telltale signs that you're dealing with an extremely badly formatted slide deck. And then over time the different ranges you can express."*

The doctrinal framing: *"Evals over time can evolve — they need to be a living artifact. It's not something you make once and then forget and then use to make all of your future decisions on."* Plus the **saturation observation**: *"If you ever hear people talk about saturation of evals, that's basically what they mean — the eval is not giving any more relevant information that we can act on."*

### 6. The autoregressive-judge-ordering bug (~35:35–36:33)

The talk's most-pointed warning. The bug: ask an LLM-as-judge for the score first, then the reasons, and the judge will *rationalise the score it already committed to*:

> *"I've had it happen where I was setting this up and I did this exact thing. I had like the number and then I said 'okay, give me also the reasons why you did that.' And so then it said 'oh, it's a four and the reasons for this are this, this, and this.' But we know that an LLM works auto-regressively — so if it's anchored on this four, it will do anything it can to argue why it should be a four. Anything. And even if it's extremely bad, if it should be a one, it will still say 'oh it is good for these and these reasons' because it needs to justify the four that it put out."*

The fix: **reasoning-before-rating**.

> *"How you do it is you actually turn it around. So first you say give me a bunch of reasons. Give me pros, give me cons, give me reasons why it should be high, give me reasons why it should be bad. And then based on all of those reasons together, you make a final decision on the output."*

The wiki's clearest single articulation of the *reasoning-before-rating* discipline for LLM-as-judge setups. This is a *load-bearing operational primitive* — any LLM-as-judge setup that doesn't follow this pattern will systematically anchor on whatever number the model commits to first.

### 7. The model-upgrade-vs-prompt-engineering trade-off (~31:14–35:00)

The talk's underdeveloped-but-honest observation: switching from Sonnet 4.7 to Opus 4.7 with *just the naive base prompt* recovers most of the iterative-prompt-engineering gains:

> *"Sometimes — and this is where it gets quite interesting and more nuanced — you can also just go to a smarter model right? Because now you're defining 'oh this is what a good slide should look like, this is what it should do, this is what it should not do' but with these models getting smarter and better over time, you kind of expect them to be able to figure that out on their own."*

Opus 4.7 *"just does not use any emojis — it kind of knows that if you want to make a slide deck about salary increase, emojis are probably not the right place to put them."* Fewer small-font slides, *"it kind of has this innate knowledge of okay, it should be readable, this is how a slide deck should function."*

The implication the speaker doesn't fully draw out: **for many use cases, prompt-engineering investment loses to model upgrades**. This is the wiki's clearest model-vendor-side acknowledgement of the *model-tier-determinism-vs-prompt-engineering-effort* trade-off — a productive complement to [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan / Cline]]'s claim that Cline *beats* Claude Code on Opus 4.5 evals *via harness engineering, not model upgrade*: same observation, opposite agency choice. Both are correct conditionally — model upgrade clears prompt-engineering effort *when the model has the relevant knowledge baked in*; harness engineering wins *when the underlying capability is there but the agent scaffolding is suboptimal*.

### 8. The hill-climbing loop as the talk's organising metaphor

The talk's organising loop, made explicit through the demo:

1. **Run evals** on the current agent → get scores
2. **Identify failure modes** (from both code-grader signals and human review)
3. **Update the agent** — either prompt-engineering (system prompt rules) or model swap (Sonnet → Opus) or harness change (add QA loop)
4. **Run evals again** → measure improvement or regression
5. **Re-calibrate the graders themselves** when they're not measuring the thing you actually care about
6. **Loop**

The wiki's clearest single articulation of the *evals-as-hill-climbing-substrate-for-iterative-agent-improvement* loop at the vendor-engineer altitude. Sits structurally adjacent to:
- [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]]'s *evals-as-gradient* (vendor-CEO altitude)
- [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe / Agent Evaluation Guide]] (article altitude)
- [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten & Zhang]]'s p/G/K/M formalism (academic altitude)
- [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan / Cline]]'s *zone-1/zone-2/zone-3* hill-climbing (customer-of-vendor altitude)

## Linked entities and concepts

**Entities directly named or substantively discussed:**

- **[[Anthropic]]** — institutional vantage (the channel + the SDK + the models used in the demo); source-count: increment.
- **[[Claude]]** — the channel-entity aliased on [[Anthropic]]; this is the 5th-ish source under the Claude channel alias.
- **Sonnet 4.7 / Opus 4.7** — referenced as the model-tier comparison anchor in the demo.
- **`manage_agent`** — Anthropic's agent SDK construct referenced in passing; Dangling first-mention as a named SDK primitive.
- **SWE-bench / terminal-bench / t-bench / BrowseComp / OSWorld / ARC-AGI-2** — referenced as the standard public benchmark cards model vendors cite; terminal-bench separately gets a substantive treatment in [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan / Cline]] (the same day).

**Concepts touched substantively:**

- **[[concepts/agent-development-lifecycle|agent-development-lifecycle]]** — the evals phase of the ADLC, operationalised at the vendor-engineer altitude. Source-count: +1.
- **[[concepts/agent-harness|agent-harness]]** — the slide-gen agent stack (manage_agent + python-pptx + Sonnet 4.7) is a harness instance. Source-count: +1.
- **[[concepts/agentic-engineering|agentic-engineering]]** — hill-climbing-on-evals as a core agentic-engineering loop primitive. Source-count: +1.
- **[[concepts/foundation-models|foundation-models]]** — the *swap-the-model-for-most-of-the-prompt-engineering-gains* observation. Source-count: +1.

**Dangling first-mentions** (deferred to second-source): Anthropic-presenter (unidentified speaker), `manage_agent` SDK primitive.

## Caveats

- **The speaker is not identified on stage or in the channel metadata.** The transcript opens *"Hello, hello, hello"* and never introduces the presenter by name. The session is presented as an Anthropic-employee practitioner-track session at AI Dev 26 x SF; the stack is Anthropic SDK + Anthropic models. If the speaker's name surfaces elsewhere (Anthropic blog, AI Dev 26 conference page, LinkedIn post), this page should be renamed from the `anthropic-` prefix to a `<surname>-` prefix and the entity Dangling updated. Confidence in framing remains high because the institutional vantage is unambiguous; confidence in attribution of *specific quotes to specific named people* is low.
- 39-minute vendor practitioner-track session with overt promotional sub-motive (Anthropic SDK + Anthropic models + Anthropic stack are the demoed substrate). The substantive eval-discipline content is independently useful, but the demo is calibrated to make the Anthropic SDK look easy.
- The judge calibration problem the speaker flags (judges scoring 2.8–4.0 on an obviously-terrible slide deck; 5/5 image judge with no image present) is taken as honest practitioner observation in the wiki. The demo would have been more rigorous with the judges anchored from the start; the speaker treats this gap as a *teaching moment* rather than a bug.
- The QA-loop adversarial pattern is named with specific prompt text on stage, but the agent's actual execution of the loop is not deeply demoed (the screen demo skips most of the run-time). Treat the prompt construction as the load-bearing primitive; the empirical effectiveness on this specific slide-gen agent is one demo's worth of evidence, not a controlled study.
- The autoregressive-judge-ordering bug is stated as practitioner-observation; no empirical study or evals-of-evals data is cited on stage. The mechanism is well-grounded in LLM autoregressive token-generation (and matches the chain-of-thought literature's general findings on *reasoning-before-rating*) but the specific magnitude of the bias is not quantified.
- The Sonnet 4.7 vs Opus 4.7 comparison is one A/B with one prompt; not a controlled study. The *"model upgrade clears most of what prompt-engineering iteration achieved"* claim is suggestive of a general pattern but should be triangulated against other use cases before being treated as load-bearing.
- ASR transcription artefacts: timestamps may drift ±1–2 seconds; some technical terms may be lightly mis-rendered (e.g. *"manage agent"* / *"manageagent"* spacing varies across the transcript).
- Live demo conditions: the speaker mentions wanting to *"do this session a little bit differently"* but having to switch to demo-only because of the audience size; some interactive Q&A is captured incompletely (the audience interjections at 14:38, 16:58 are partially audible only).
