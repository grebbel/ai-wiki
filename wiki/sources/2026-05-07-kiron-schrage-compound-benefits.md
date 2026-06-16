---
type: source
kind: article
title: "How to Reap Compound Benefits From Generative AI"
author: ["David Kiron", "Michael Schrage"]
publisher: "MIT Sloan Management Review"
journal_volume: "MIT SMR Column, 6 April 2026"
date_published: 2026-04-06
date_ingested: 2026-05-07
length: "~12 pages of body content (13-page PDF; 12-min reading-time stated)"
raw: "../../raw/articles/How to Reap Compound Benefits From Generative AI.pdf"
tags: [mit-smr, kiron, schrage, compound-benefits, evaluation, verification, learning-capture, generative-ai, micro-productivity-trap, ai-iteration, asset-appreciation]
confidence: 0.80
last_confirmed: "2026-05-07"
---

# How to Reap Compound Benefits From Generative AI

A practitioner column in **MIT Sloan Management Review**, 6 April 2026, by **David Kiron** (MIT SMR editorial director, research; co-author of [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]]) and **Michael Schrage** (research fellow at the MIT Sloan Initiative on the Digital Economy). 12-min reading time. Op-ed-style argument that organizations should reorient AI deployment **from consumption (asset depreciation) to compounding (asset appreciation)**, building infrastructure to verify, evaluate, and capture learning from every AI interaction.

The column extends [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. (Nov 2024)]]'s empirical finding (only 15% of orgs are Augmented Learners) by specifying the **operational mechanism** that turns the 15% advantage into compounding returns: a three-step verification → evaluation → learning-capture flywheel.

## TL;DR

- **Old question**: "How do we produce more, faster?" (consumption economics → asset depreciation).
- **New question**: "How do we systematically learn from, and with, what AI produces?" (compounding economics → asset appreciation).
- Two structural dynamics make compounding management imperative: **Polanyi's tacit-dimension breach** (LLMs absorb how experts work from behavioral traces, including knowledge experts never articulated — tacit expertise is no longer a moat) and **Jevons paradox** (efficiency gains stimulate demand, so cheaper sophisticated capability proliferates faster, feeding the loop).
- **Three-step flywheel**: (1) **Verification** — does this output meet the standard? (2) **Evaluation** — what does this output reveal? (3) **Learning capture** — how do we ensure this insight persists?
- **The trap**: most organizations treat AI outputs as verdicts to confirm rather than starting points to interrogate. Verification masquerades as evaluation. *Consumption dressed up as adoption.*
- **Five concrete moves**: preserve evaluation expertise; build verification mechanisms (minimally viable verification); institute evaluation practices ("what was interestingly wrong?"); create capture systems (decision journals, prompt repositories, evaluation logs); measure the cycle, not just the output.
- **Anchor anecdotes**: Boris Cherny (Anthropic, Claude Code) — 10–15 concurrent Claude instances as smart subagents, CLAUDE.md as in-workflow learning capture; Jaana Dogan (Google, Gemini API) — "It's not perfect and I'm iterating on it" instead of accept/reject; Ransbotham et al. statistics on systematic-feedback-loop orgs being 6× more likely to derive financial benefits.

## What was actually ingested

Full column: 13-page PDF (online MIT SMR layout) read end-to-end. ~12 pages of body content (12-min reading time stated by publisher). Includes the column intro, three-step framework, two anchor anecdotes (Cherny, Dogan), five concrete moves, and the closing transformation argument.

## Core thesis: from consumption to compounding

The column opens with an economic-pattern reframing:

> "Most organizations still overinvest in answering the old question. They treat artificial intelligence as a throughput accelerator: task in, output out, loop closes. This is **consumption economics**. A serious CFO instantly recognizes the pattern: **asset depreciation**.
>
> The organizations pulling ahead answer the new question. They treat AI as a **capability accelerator**: task in, output out. But they also ask, 'What worked? What failed? What should change next time?' Insights get captured, converted into shared knowledge, and applied to subsequent interactions. Each cycle makes the next more effective. This is **compounding value**. Serious CFOs recognize this pattern, too: **asset appreciation**."

The framing is deliberately economic, not technical: AI deployments are either *depreciating* assets (knowledge evaporates after each interaction) or *appreciating* assets (knowledge compounds through systematic capture).

## Why this moment is structurally different

Two complementary economic dynamics that reinforce each other in a virtuous cycle make compounding management an imperative.

### 1. Polanyi's tacit dimension breach

In his 1966 book *The Tacit Dimension*, philosopher [[Michael Polanyi]] observed that **humans know more than they can articulate**. For decades, that tacit knowledge protected knowledge workers — what could not be explicitly described could not be automated. **Tacit expertise was a moat.**

The column argues AI breaches that moat — *not by codifying tacit knowledge but by inferring it from behavioral traces at scale.* Large language models absorb how experts actually work, including knowledge the experts never articulated:

- **Legal reasoning** in briefs and opinions
- **Financial judgment** in analyst reports and trading patterns
- **Strategic thinking** in board presentations

As these behavioral traces become more legible to AI models, the tacit expertise embedded in them becomes readable by machines.

**Anchor example**: Boris Cherny (Anthropic), who led Claude Code development, described a revealing moment. After he gave Claude tools to interact with his file system, the AI began *exploring the system on its own* to find answers. "It was mind-blowing," Cherny said. He had not programmed that capability. **The model inferred how developers work from the traces they had left behind — behaviors that no one had previously formalized.**

### 2. Jevons paradox amplification

In 1865, economist William Stanley Jevons observed that when steam engines became more efficient, coal consumption *increased* rather than decreased. Efficiency gains made the capability cheaper, stimulating demand.

Applied to AI: as tacit expertise becomes readable by machines, the cost of sophisticated capability drops dramatically. Projects that were previously too expensive to prototype proliferate. Iteration cycles that once took months compress to hours. **More expertise becomes readable to machines, expanding what AI can access while enhancing the AI's knowledge base and improving its capability. More capability expands what organizations attempt. The loop feeds itself.**

The data supports this structural shift: organizations that combine strong organizational learning with learning specific to AI are **up to 80% more effective at managing uncertainty** (citing [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]]). Becoming better learners *with* AI is at least as important as using AI to create efficiencies.

## The three-step compounding flywheel

When all three steps are present and connected, organizations reap compounding benefits. **When any step is missing, organizations merely consume AI outputs.**

### 1. Verification — "Does this output meet the standard?"

- Produces a **binary** answer: correct or incorrect, usable or not.
- Compares output against a criterion that **already exists**.
- **Unverified AI output is noise with a confident tone.**
- Verification used alone catches errors without generating learning.

### 2. Evaluation — "What does this output reveal?"

- Where verification compares output against existing standards, **evaluation may generate standards that did not exist before**.
- Requires domain expertise in ways verification often does not.
- *The expert as evaluator is not merely checking quality. They are discovering what quality means in this new context.*
- With AI outputs, evaluation is required across three dimensions: **volume, variety, and velocity**.
- **Human bandwidth to do evaluations, not AI access, becomes the binding constraint.**

### 3. Learning capture — "How do we ensure this insight persists?"

- When evaluation is not recorded, knowledge does not compound; it evaporates after each interaction.
- Learning capture converts single insights into organizational knowledge: documented criteria, updated prompts, shared repositories of what worked and why.
- **Think of it as version control for organizational judgment.**
- Without it, evaluation is a one-time event. And learning capture alone (documentation without verification or evaluation upstream) produces nothing but organized noise.

The three steps **dynamically reinforce one another**: better verification produces cleaner signals for evaluation; better evaluation generates richer material for capture; better capture improves the criteria used in the next round of verification. **The cycle is the point.**

> "Most experts cannot fully articulate what makes their judgment good. Forcing that judgment into written standards, such as the way developers write **CLAUDE.md** files that specify what 'good' code looks like, makes the tacit explicit for colleagues and for AI alike. The gap between what an LLM delivers and what the expert wanted surfaces unspoken knowledge."

## Worked example 1: Anthropic's Claude Code (Boris Cherny)

The column's most concrete operational example. **Boris Cherny** at **[[Anthropic]]** built Claude Code with the three-step flywheel in mind:

- **Verification**: gives the AI a way to verify its own work — a test suite, a browser check — *before a human ever sees it*.
- **Evaluation**: concurrently runs **10 to 15 Claude instances** that generate swarms of smart subagents — one checks style while another hunts bugs, then a second cohort challenges the first for false positives.
- **Capture**: a **CLAUDE.md** file gathers mistakes, corrections, and design principles **inside the workflow itself** — not after its completion but while it is happening. Each new session inherits what every prior session learned.

The pattern generalizes: every business function can build its equivalent of CLAUDE.md.

> "There are analogous questions for leaders of other business functions: What is your equivalent of version control for organizational decisions? Of automated testing for new approaches? Of code review to make evaluation criteria explicit and shared? The 'verification-evaluation-learning capture' flywheel offers both challenge and opportunity for managers and executives who want to use AI to do measurably more than simply cut costs and improve efficiencies."

The marketing parallel: a marketing team using AI to generate campaign briefs.

- **Verification** asks whether the brief meets basic brand standards: consistent tone, correct product claims, regulation-compliant disclaimers. Automation is fast and cheap.
- **Evaluation** asks what the brief *reveals*: did AI surface customer insights the team hadn't named? Did it miss the emotional register entirely? Are these insights *actionable* — meaning, can they trigger interactions and offers to cultivate relationships and/or close deals?
- **Learning capture** asks whether the strategist's correction — "Our brand never leads with product features; it leads with customer identity" — gets written into a shared prompt template or brief standard for the whole team to use the next time. **Without that last step, the strategist's insight dies with the session.**

## Worked example 2: Google's Jaana Dogan ("not perfect and I'm iterating on it")

A second anecdote that defines the *anti-pattern* of verification-masquerading-as-evaluation. **Jaana Dogan**, principal engineer at [[Google]] responsible for developer infrastructure on the Gemini API, ran a revealing experiment:

- She pointed **Claude Code** — *a rival tool* — at a problem her team had spent many months solving.
- Given a short prompt with no proprietary Google data, Claude Code generated a design solution comparable to the one her team had landed on, along with a working prototype.
- **Most managers, seeing that output, would just verify**: "Does this match what we built? Close enough? Adopt or reject." Verification is fast, comfortable, and binary. It answers the question already in your head.
- **Dogan did something different.** She decided: *"It's not perfect and I'm iterating on it."*

The eight words embody the shift:
> "Evaluation interrogates what the output reveals — about the problem, about your assumptions, and about what you haven't yet named. Dogan could do this because she had months of judgment to bring to the encounter. AI compressed the implementation; **it could not compress the formation of expertise.** Without that prior work, only two moves exist: Accept or reject. With it, a third move opens up: Stay in the encounter and learn."

**Critical distinction**: most organizations treat AI outputs as verdicts to be confirmed rather than starting points to be interrogated. The result is **consumption dressed up as adoption — verification mistaken for the whole job.**

**Implication**: Deploy AI first in domains where your people *already* have deep expertise — not because AI needs hand-holding but because evaluation requires someone capable of recognizing what "not perfect" actually means and knowing what iteration may reveal. **The expert as evaluator is not a transitional role.**

But Dogan's insight lives only in her head until infrastructure captures it. The question for any organization is not whether individual experts can hold loops open — some always will. **It's whether the machinery exists to convert their judgment into shared knowledge that persists.**

## Five concrete moves to build the capability

### 1. Preserve your company's evaluation expertise

To reap compound interest, you're dependent on people who can accurately evaluate AI output. **This is domain expertise repositioned: the expert as evaluator rather than the expert as producer.** Organizations that let people's deep expertise atrophy because "AI can do that now" will lose this very valuable capability.

### 2. Build verification mechanisms (minimally viable verification)

The cycle cannot begin without verification of output. Verification costs vary by domain:

- **Software**: cheap (code runs or it doesn't).
- **Finance**: moderate (models can be stress-tested against historical data).
- **Strategic planning**: expensive (long bets may not resolve for years).

Most organizations treat expensive verification costs as a good reason *not* to start some work with AI tools. **Instead, the smart move is doing minimally viable verification — the cheapest credible check that an AI output is not wrong.** Examples:

- **Multijudge systems** that surface disagreement.
- **Consistency checks** that compare outputs across different formulations of the same problem.

None of these guarantees correctness, but each offers enough verification to start the cycle.

### 3. Institute evaluation practices

Few organizations systematically evaluate AI outputs. **After every significant AI interaction, users should ask three questions:**

- What worked?
- What failed?
- **What was *interestingly* wrong** — wrong in a way that reveals something about the problem the team has not previously articulated?

That third question is where hidden value lives. An output that fails in a way the expert noticed but had not yet named becomes new organizational knowledge: **tacit expertise becoming explicit.** People must be prompted to ask these questions as part of the existing workflow.

### 4. Create capture systems

Evaluation without capture evaporates. Capture systems operate on **two levels**:

- **Inferential** — learning from patterns in accumulated traces, the way AI learns from historical data.
- **Explicit** — recording human judgment in retrievable form.

Both matter. A practical approach is lightweight infrastructure:

- **Decision journals** that record not just what was decided but why.
- **Prompt repositories** that preserve what worked and what failed instructively.
- **Evaluation logs** that make the team's evolving standards searchable.

The design principle is **retrievability, not comprehensiveness**. A marketing team's capture system is a prompt library and a shared brief template. A finance team's is an annotated model log. Every function can build its equivalent of CLAUDE.md. **Discipline, not cost or creativity, is the true constraint.**

### 5. Measure the cycle, not just the output

Most organizations judge an AI deployment's success using measures like **tools adopted, hours saved, or tasks completed**. *These are consumption metrics.*

Organizations trying to reap compound returns measure the cycle:

- How many interactions were verified?
- How many were evaluated?
- How much learning was captured?
- How quickly did captured learning change subsequent practice?
- *Did your team leaders learn things from AI interactions last week that changed how they worked this week?*

If not, the cycle is not running.

## Statistical anchors

Three citations carry empirical weight in the column:

| Statistic | Source per column | Wiki cross-link |
|---|---|---|
| Orgs that build systematic feedback loops between humans and AI are **6× more likely** to derive substantial financial benefits | MIT SMR / BCG research (Ransbotham et al.) | [[2026-05-07-ransbotham-augmented-learners]] |
| Orgs investing in **learning with AI** are **73% more likely** to achieve significant financial impact | MIT SMR / BCG research | [[2026-05-07-ransbotham-augmented-learners]] |
| As of 2024, **70% of companies** had adopted AI but **only 15%** were using it for organizational learning | MIT SMR / BCG 2024 report | [[2026-05-07-ransbotham-augmented-learners]] (the 15% Augmented Learners) |
| Orgs that combine strong organizational learning with AI-specific learning are **up to 80% more effective** at managing uncertainty | MIT SMR / BCG 2024 report | [[2026-05-07-ransbotham-augmented-learners]] |

The column is largely a *synthesis* of [[2026-05-07-ransbotham-augmented-learners|the November 2024 report]] plus the new operational flywheel — but extends the empirical claim with the Cherny / Dogan anecdotes that exemplify the flywheel in practice.

## Cross-source positioning

- **Direct extension of [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]]** — same author David Kiron, same operational thesis (combining org + AI-specific learning), now with a named flywheel mechanism.
- **Reinforces [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI micro-productivity-trap]]** — "consumption dressed up as adoption" is a precise restating of the [[micro-productivity-trap]]. The Kiron-Schrage flywheel is operationally what Bain/OpenAI's "reimagine workflows" prescription requires.
- **Connects to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]** — Boris Cherny's 10–15 concurrent Claude instances + CLAUDE.md pattern is consistent with the brain/hands/session decomposition; the post is operational evidence for the same architecture from a different team at the same company.
- **Connects to [[durable-skills]]** — "the expert as evaluator is not a transitional role" is a direct claim about which skills retain durable value; "evaluation requires domain expertise" is the operational definition.
- **Connects to [[ai-employment-effects]]** — the column explicitly argues against letting expertise atrophy because "AI can do that now." This positions the column on the **augmentation side** of the [[automation-vs-augmentation]] debate, with a specific mechanism (the expert is repositioned, not removed).
- **Connects to [[generative-ai]]** — the column reframes ROI as **return on iteration** rather than return on investment. Worth promoting as a coining.

## Source-quality flag

- **Strengths**: lead-author David Kiron carries the [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]] empirical foundation. Citations to Polanyi (1966), Jevons (1865) ground the column in established economic/philosophical theory. Two named, identifiable real-world examples (Cherny, Dogan) provide operational specificity that pure-thesis columns lack.
- **Caveats**: Op-ed format, not empirical research. The "6× more likely" and "73% more likely" statistics are restated from the MIT SMR / BCG research base — *not* independently validated by this column. The Cherny / Dogan anecdotes are vivid but n=2.
- **Per CLAUDE.md §Lifecycle**: confidence baseline 0.7 + 0.05 additional supporting source (the Anthropic Managed Agents post and Ransbotham et al. mutually reinforce the framework) + 0.05 for being co-authored by an author with prior empirically-grounded work in the wiki = **0.80**. Not raised to peer-review-tier 0.85 because the column itself is opinion-format.

## Open questions for the wiki

- **Is "return on iteration" worth a dedicated wiki concept page?** The column coins it once; if other sources independently arrive at the same reframing, promote.
- **What's the empirical correlate of "evaluation as binding constraint"?** The column claims **human bandwidth to evaluate** becomes the binding constraint as AI access ceases to be limiting. Anthropic Economic Index 5's tenure-success finding (~3-4pp after controls) is one signal that evaluation skill differentiates outcomes. A dedicated longitudinal study of "evaluation throughput per analyst hour" would be the next-source target.
- **Does the verification-evaluation-learning-capture flywheel map onto MIT CISR's Stage 3 attributes?** "Test-and-learn" + "architected for reuse" are CISR Stage 3 traits — the Kiron-Schrage flywheel may be the operational prescription for how to *do* Stage 3, complementing CISR's structural framing.
