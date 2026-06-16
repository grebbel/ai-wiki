---
type: source
kind: paper
title: "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality"
author: ["Fabrizio Dell'Acqua", "Edward McFowland III", "Ethan Mollick", "Hila Lifshitz", "Katherine C. Kellogg", "Saran Rajendran", "Lisa Krayer", "François Candelon", "Karim R. Lakhani"]
publisher: "Organization Science (INFORMS)"
journal_volume: "Articles in Advance, pp. 1–21"
peer_reviewed: true
url: "https://doi.org/10.1287/orsc.2025.21838"
doi: "10.1287/orsc.2025.21838"
license: "CC BY 4.0"
raw: "../../raw/papers/Mitchell and Dino - 2011 - In Search of Research Excellence Exemplars in Entrepreneurship.pdf"
date_published: 2026-03-11
date_ingested: 2026-04-28
tags: [productivity, knowledge-work, jagged-frontier, BCG, GPT-4, RCT, mollick, lakhani, dellacqua, equalizing-effect, augmentation, automation]
length: "~21 pages (read pp. 1-15: intro, experimental design, inside-the-frontier results, outside-the-frontier results)"
---

# Dell'Acqua et al. — Navigating the Jagged Technological Frontier

## TL;DR

A preregistered, randomized field experiment with **758 [[Boston Consulting Group|BCG]] consultants** (~7% of their individual-contributor workforce) testing the effect of **GPT-4** on knowledge work. Three conditions: no AI / GPT-4 only / GPT-4 + prompt-engineering overview. Two task arms: **inside the frontier** of AI capability (creative product/go-to-market with 18 subtasks) vs. **outside the frontier** (a deliberately AI-defeating business case requiring spreadsheet + interview triangulation).

**Headline findings:**
- **Inside the frontier**: AI users complete **+12.2%** more tasks, **+25.1%** faster, with **+40%** higher quality (Cohen *d* ≈ 0.96).
- **Outside the frontier**: AI users are **19 percentage points** *less likely* to produce a correct answer (84.5% control → 60.0% / 70.6% AI conditions).
- **Equalizing effect within elite professionals**: bottom-half-skill subjects gain **+31%**; top-half **+11%**. Both gain meaningfully — AI is a "significant equalizer" even among BCG-tier knowledge workers.
- **Subjective coherence quality** is *higher* with AI even when answers are wrong — AI improves presentation/persuasion regardless of correctness.

The paper introduces the **"jagged technological frontier"** concept: AI capability is uneven across tasks of similar perceived difficulty, and effective AI use requires diligent workflow inspection to identify which tasks fall on which side of the boundary.

> **File-naming note:** The raw PDF was misnamed as `Mitchell and Dino - 2011 - In Search of Research Excellence Exemplars in Entrepreneurship.pdf`; the actual content is this Dell'Acqua et al. paper. The `raw:` path preserves the original filename; consider renaming on disk for clarity.

## Key claims

### Experimental setup

- **Subjects**: 758 BCG consultants (eligibility ~1% of applicants; degrees from Harvard, Yale, Oxford, etc.).
- **Conditions** (random assignment within each task arm):
  - **Control** (no AI)
  - **GPT-only** (GPT-4 access)
  - **GPT + overview** (GPT-4 + prompt-engineering instructional materials)
- **Two task arms** (between-subjects):
  - **Arm 1 — Inside the frontier**: 385 consultants. New product + go-to-market task with 18 subtasks (creative ideation, analytical thinking, writing, persuasion).
  - **Arm 2 — Outside the frontier**: 373 consultants. Business case based on spreadsheet data + interview transcripts requiring triangulation, designed so AI alone (without close human supervision) would fail.
- **Model**: GPT-4 via OpenAI API (June 2023), default settings, ChatGPT-like interface.
- **Grading**: independent human graders (3 per response, 1–10 scale on creativity/analytical/writing/persuasion); composite quality score; replicated by GPT-4 self-grading.

### Inside-the-frontier results

| Outcome | GPT-only vs. control | GPT + overview vs. control |
|---|---|---|
| Quality (1–10) | +1.31 (29.9% gain) | +1.48 (33.9% gain) |
| Completion rate | +9.0 pp (89% → 91%) | +11.1 pp (89% → 93%) |
| Time spent (first 17 questions) | −1,388 sec (−27.6%) | −1,129 sec (−22.5%) |
| Effect size (quality, Cohen's *d*) | 0.87 | 0.96 |

### Equalizing effect (within high-skilled professionals)

Splitting AI-treated subjects by their pre-treatment assessment performance:

| Skill group | Baseline | Experimental | Gain |
|---|---|---|---|
| Bottom-half skill | 4.37 | 5.72 | **+31%** |
| Top-half skill | 5.34 | 5.82 | **+11%** |

Both groups gain. Bottom half gains more, narrowing within-group performance distribution — but top-half gains are still meaningful (contrary to some prior work showing zero gain at the top in customer-support studies).

### Outside-the-frontier results

| Outcome | Control | GPT-only | GPT + overview |
|---|---|---|---|
| Correctness (binary) | 84.5% | 70.6% | 60.0% |
| Subjective coherence quality | 5.86 | 6.90 | 7.33 |
| Time on task | baseline | −18% | −30% |

Two unsettling specific findings:
- **AI users are *less* likely to be correct** despite *more confidence* in their answer (higher coherence scores even when wrong).
- The **GPT + overview** treatment performs *worse* on correctness than **GPT-only** — more familiarity with the tool led to *more* over-reliance on it.

### Mechanism: "jagged frontier"

> "Tasks that appear similar in complexity for humans may nonetheless fall on opposite sides of the boundary where AI assistance helps versus harms performance."

The frontier is **expanding** (AI improves) and **invisible** (location not obvious to users from task appearance). Implication: knowledge workers must develop *meta-cognitive* skills to assess where any given task sits.

### Two adaptation patterns observed

The paper's qualitative analysis (online appendices) identifies two strategies among effective AI users:
- **Centaurs**: alternate between AI and human work, switching based on task-by-task fit.
- **Cyborgs**: deeply intertwine AI into their workflow with continuous human-AI co-production.

(Detailed in appendices not fully read; flag here as a hook for future deep-read.)

## Methodology notes

- Preregistered design.
- BCG operates "up or out" — promotion tied to evaluations on tasks the experiment closely mirrors.
- Tasks designed by senior BCG managing directors.
- 11 BCG MDs surveyed to confirm task validity for recruiting/promotion.
- Online Appendix F maps tasks to O*NET data, confirming generalization to high-skill knowledge work broadly.
- Robustness checks: shoe-design experts re-graded a subset; results consistent.

## Limitations / caveats

- Single firm (BCG), single task domain (consulting), one model (GPT-4 June 2023).
- The frontier shifts with model improvements — findings are a snapshot.
- Outside-the-frontier task is *deliberately constructed* to defeat AI; not a natural distribution of tasks.
- No long-run learning or skill effects measured (one-shot experiment).

## Quotes worth saving

> "AI capabilities cover an uneven set of knowledge work, and we introduce the concept of a 'jagged technological frontier' to characterize the performance of AI when used by knowledge workers."

> "Within this jagged frontier, AI can complement human work. However, outside the frontier, AI output is inaccurate, is less useful, and can degrade human performance."

> "Subjects using AI were 19% less likely to produce correct solutions compared with those without AI, pointing to potential limitations of AI supporting knowledge workers."

> "AI may serve as a significant equalizer in the realm of high-end knowledge work, narrowing the performance gap between different skill levels; however, those who were above average also benefited meaningfully through the use of the AI system."

## Related in this wiki

- [[jagged-frontier]] — concept page anchored on this source
- [[automation-vs-augmentation]] — frontier behavior is a per-task property
- [[ai-employment-effects]] — equalizing effect within knowledge workers
- [[generative-ai]] — GPT-4 capability evidence at task level
- [[ai-benchmarks]] — field-experiment evidence complements benchmark scores
- [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work]] — also documents an equalizing effect, in customer support, with within-occupation skill gradient
- [[2026-04-28-anthropic-economic-index-q4-2025]] — measures task-level speedup and success-rate gradients at population scale
- [[Boston Consulting Group]] — experimental partner
- [[Ethan Mollick]], [[Karim Lakhani]], [[Fabrizio Dell'Acqua]] — author entities
