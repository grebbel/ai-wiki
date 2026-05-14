---
type: source
kind: video
title: "AI Evaluations Clearly Explained in 50 Minutes (Real Example) — Hamel Husain on Peter Yang's podcast"
author: ["Peter Yang"]
url: "https://www.youtube.com/watch?v=uiza7wp1KrE"
date_published: 2025-09-28
length: "~52:30 minutes (transcript ~1008 ASR lines)"
raw: "../../raw/videos/husain-peter-yang-ai-evaluations-clearly-explained-50-min.md"
tags: [evals, ai-evaluation, llm-as-judge, observability, binary-pass-fail, agreement-metric, true-positive-rate, true-negative-rate, error-analysis, axial-coding, spreadsheet-evals, hamel-husain, peter-yang, agent-development-lifecycle, agent-harness, ai-product-management]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: agent-development-lifecycle
    via: "operationalises the Test→Deploy→Monitor loop with a spreadsheet-first workflow: open-codes from production traces → axial coding → pivot-table failure counts → eval criteria → LLM-as-judge → TPR/TNR validation → continuous in-prod sampling"
  - type: supports
    target: agent-harness
    via: "fills in the Contracts and Compounding harness layers with a teachable PM/engineer workflow — Husain's 'annotation and counting is the most valuable process' echoes Chatterjee's contracts-as-evaluable-specifications claim"
  - type: supports
    target: agentic-engineering
    via: "the specs+tests-and-iterate discipline made concrete with a real production agent (Nurture Boss property-management assistant); demystifies eval as 'a spreadsheet and pivot tables' rather than 'specialised tooling'"
  - type: supports
    target: 2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair
    via: "Husain's workflow and Guthrie's flywheel describe the same offline→online→learning compounding cycle from different vantages (practitioner-trainer vs vendor-engineer); same vocabulary (task / dataset / scores / production traces / LLM-as-judge); 3-month gap"
---

# AI Evaluations Clearly Explained in 50 Minutes — Hamel Husain on Peter Yang

> Today, I want to share a new episode with Hamel Husain. Hamel has trained 2,000+ PMs and engineers from companies like OpenAI, Anthropic, and Google on how to run AI evals. In my new episode, he shares a free master class on how to build evals for a real AI agent in just 50 minutes using a simple spreadsheet. I learned a lot from Hamel and I think you will too.
>
> Hamel and I talked about:
> (00:00) What the most valuable part of evals is
> (01:25) Live walkthrough: Analyzing 100 real production traces
> (09:50) Creating the eval criteria using a simple spreadsheet
> (24:44) Why binary pass/fail ratings beat 1-5 scores every time
> (28:52) The agreement metric trap that fools most PMs
> (30:08) True positive and negative rates explained
> (36:00) How to set up continuous evals in production

(Channel description from Peter Yang's YouTube upload, ~52:30 runtime.)

A 50-minute hands-on walk-through by **Hamel Husain** (independent AI-evaluation educator; co-instructor of the Maven AI evals course — *"trained over 2,000 PMs and engineers from companies like OpenAI, Anthropic, and Google"*) interviewed on the **Peter Yang** podcast. Published 28 September 2025, auto-generated transcript, no chapters in the YouTube data but section markers in the description. ASR-cleaned for proper-noun consistency (`Hamel`/`Brain Trust`/`Arize`/`LangSmith`/`Maven`/the systematic `email`↔`eval` ASR mishearing).

## TL;DR

The wiki's **practitioner-trainer anchor on AI evaluation as a teachable, spreadsheet-first discipline**, complementing [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie / Braintrust 2025]]'s vendor-engineer vantage with a vendor-neutral curriculum stance. Three substantive contributions:

1. **The spreadsheet-first workflow** — *"You can get insane value by just doing [annotation and counting]. And that's the one part that everyone skips."* Husain demonstrates the full loop on a real production agent ([[Nurture Boss]] — an AI property-management assistant with ~100 production traces):
   - **Step 1: Open codes.** Sit with a spreadsheet of production traces; write free-text notes (`z_note` field) on what went wrong in each — *"tour scheduling rescheduling issue, human handoff or transfer issue, formatting error, conversational flow issue, made-up promises not kept"*.
   - **Step 2: Axial coding.** Dump the open codes into Claude/ChatGPT and ask it to propose 5–6 categories. *"Open code / axial code is some really old technique from social sciences and machine learning — the LLM knows exactly what you're doing."*
   - **Step 3: Categorise with the AI formula.** Use Google Sheets' built-in `=AI(…)` formula to assign each trace's z_note to a category.
   - **Step 4: Pivot tables.** Count occurrences per category — *"hey, conversational flow issue is happening quite a bit."*
   - **Step 5: Promote the dominant categories to evals.** Build an LLM-as-judge for the top 2–3 failure modes; validate it against human labels.
   The deliberate *un*-sophistication of the tooling — Google Sheets, not Braintrust/LangSmith/Arize — is the **floor-raising claim made operational for the [[ai-product-management]] audience**: the eval discipline is not a tooling problem.

2. **Binary pass/fail beats 1–5 scores — every time** ([[binary-pass-fail|24:44]]). Husain's strongest prescription: *"When you see an average score of 3.2 versus 3.7, no one really knows what the hell that means. It's not really actionable, honestly. They're like, 'Oh, it's like getting better.' Honestly, nobody really knows whether it's getting better or not."* The reason Likert scales fail: **inter-annotator agreement is dominated by category-boundary disagreements** (annotator A's *3* is annotator B's *4*) rather than capability disagreements. Binary collapses the noise. Husain's prescription extends to LLM-as-judge: build one binary judge per failure mode, not a multi-dimensional rubric.

3. **The agreement-metric trap** ([[agreement-metric-trap|28:52]]) — *"As a product manager, if you ever see the word agreement, you need to pause and be like, 'Hm, let me dig into this, please.'"* Naive accuracy/agreement between an LLM-judge and human labels is misleading when the failure class is rare (the trivial *"always predict pass"* judge looks ~95% accurate when only 5% of traces fail). The correct metrics are **true-positive rate** (TPR = recall over failures) and **true-negative rate** (TNR = recall over passes), reported as separate columns and ideally combined into a single F1-like aggregate. Husain: *"If people don't trust your evals, they won't even trust you. You're done."*

Plus a structural observation on **how production evals slot into continuous deployment**: an LLM-as-judge can run in CI on every code change AND on a random sample (~5%) of production traffic in real time — same judge, two surfaces. The dashboard reports TPR/TNR per judge plus an aggregate score. Husain estimates **under a dozen judges per app** is the right cardinality.

## What was actually ingested

Full ~52-minute episode transcript (auto-generated ASR, ~1008 raw segments). The interview format is heavily Husain-led — Peter Yang's role is to keep pace and ask clarifying PM-side questions. The episode ends with Husain inviting listeners to the October Maven cohort. Light cleanup of proper-noun mistranscriptions (`Hamill` → `Hamel`, `Mayheaven` → `Maven`, `email` → `eval` where the ASR systematically misheard the homophone). Transcript ends cleanly with both speakers' sign-off.

## Operational mechanics — the spreadsheet-first workflow in detail

### Step 1 — Read 100 production traces and take notes

Husain's discipline: open the observability tool ([[Braintrust]] in [[Nurture Boss]]'s case, but [[Arize]] / [[LangSmith]] equivalent), filter to ~100 recent traces, **open each one and write a free-text note** in a column called `z_note`. *"It's literally just me reading the trace and going, 'oh, this is broken because it sent a markdown blob inside a text message' — and I write that down."*

The discipline is the **annotation**, not the categorisation. Categorisation is downstream and easy; annotation is the part that requires human judgment about what *is* a failure in this domain.

### Step 2 — Axial coding via LLM

Once 100 traces have open-code notes, Husain dumps the CSV into Claude/ChatGPT with this prompt template:

> *"Please analyze the following CSV file. There's a metadata field which is a nested field called z_note that contains open codes. Open codes is just a fancy word for those comments that I made — just the notes for analysis of LLM logs that we are conducting. Please extract all of the different open codes from the z_note field. Propose five to six categories that we can create axial codes from."*

The terminology (*open code* / *axial code*) is **deliberate prompt engineering** — the LLM recognises it as a social-sciences-then-ML technique and adopts the right schema. *"You could also say 'categorize' — start wherever you want — but the terminology gives it specificity."*

### Step 3 — Categorise in-spreadsheet with `=AI(…)`

Husain's surprise discovery: **Google Sheets has a built-in `=AI(…)` formula** that lets you classify a cell using natural language. *"They're usually very slow. It's cool. It's can be slightly janky, but it's okay. It's lightweight and you don't have to use any tools and everyone can understand how to do this."* The cost of the un-sophisticated tooling is throughput; the benefit is **everyone in the room can follow the workflow**.

### Step 4 — Pivot tables

Once each trace is categorised, a pivot table immediately surfaces the **failure distribution**: conversational-flow issues N=23, human-handoff failures N=18, formatting errors N=11, etc. The categories with the most volume are the ones worth promoting to evals.

### Step 5 — Build the LLM-as-judge

For the dominant 2–3 failure modes, Husain writes an LLM-as-judge prompt that takes a trace as input and returns `{pass, fail, reason}`. The judge is **binary by construction** — see the next section for why. The judge gets validated against a held-out set of human-labelled traces, reporting **TPR and TNR separately**.

### Step 6 — Continuous evals

The same judge then runs **in two places simultaneously**:
- **CI**: every code or prompt change triggers the judge against a fixed regression set.
- **Production**: the judge samples ~5% of live traffic in real time and emits TPR/TNR-adjusted alarm signals.

Husain: *"Under a dozen judges is usually right. Sometimes more if they're cheap. Annotation is the budget — not the judge."*

## Why binary beats 1–5 scoring

The Likert-scale failure mode Husain identifies is **structural, not just psychometric**:

| Property | 1–5 Likert | Binary pass/fail |
|---|---|---|
| Inter-annotator agreement | Dominated by boundary disagreements | Clean: same label or different |
| Action threshold | Ambiguous (is 3.2 vs 3.7 bad?) | Explicit (fail rate ≥ threshold) |
| Cost of building the judge | Multi-dimensional rubric, hard to align with humans | Single criterion, easy to align |
| Aggregation across many judges | Average of averages, semantically empty | Per-judge fail rate + overall F1 |
| What it tells PMs | "It's getting better-ish?" | "Failure mode X is at 7%, target is 3%" |

The Likert trap is **especially seductive for product managers** because it looks like more information. Husain's reframe: *"You're not getting more information — you're getting more noise."*

## The agreement-metric trap, in detail

The most subtle of the three contributions. Setup:

- Production has a low base rate of failure (say 5%).
- You build an LLM-as-judge to flag failures.
- You compute *agreement* between the judge and a human labeller on 100 traces: 95%.

This *looks* great. But the trivial judge — *"always predict pass"* — would score 95% on the same metric, because 95% of traces are passes. The judge has learned nothing about failure detection.

Husain's prescription: **always report TPR and TNR separately**, never raw agreement:
- **TPR** (recall over failures): *of the actual failures, how many did the judge catch?*
- **TNR** (recall over passes): *of the actual passes, how many did the judge correctly let through?*

An honest judge has high TPR *and* high TNR. The naive-agreement trap hides the case where TPR is near zero. *"As a PM, if you see the word 'agreement', stop and dig."*

## Convergence with the wiki's existing eval corpus

| Source | What it adds relative to Husain |
|---|---|
| [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie / Braintrust 2025]] | Vendor-engineer vantage on the **same flywheel** — offline→online→learning cycle. Guthrie names the four ingredients (task / dataset / scores / experiment); Husain names the *human process* that produces them. Together: Guthrie is the *what*, Husain is the *who and how*. 3-month gap; published in the same evals-as-discipline wave. |
| [[concepts/agent-development-lifecycle\|agent-development-lifecycle]] | Husain operationalises the Test phase with concrete artefacts (spreadsheet, axial codes, AI formula, pivot tables, TPR/TNR) — exactly the *Test → Deploy → Monitor → Iterate* loop the ADLC names abstractly. |
| [[concepts/agent-harness\|agent-harness]] | The Contracts layer (scored output against criteria) gets a teachable workflow; the Compounding layer (telemetry → learning) gets the continuous-prod sampling discipline. |
| [[concepts/agentic-engineering\|agentic-engineering]] | The specs+tests-and-iterate primary-artefact pattern materialised for a non-coding-heavy AI product (a customer-service-assistant LLM, not a coding agent). |

## Linked entities and concepts

- **Hamel Husain** — the substantive speaker. Independent AI-evaluation educator; co-instructor of the Maven AI evals course. First wiki appearance — listed in this source page's body; entity page deferred until a second source cites him (per [§Author-entity promotion](../../CLAUDE.md#author-entity-promotion)).
- **Peter Yang** — host. Product-management YouTube/podcast channel. First wiki appearance as channel; entity page deferred.
- **[[Nurture Boss]]** — the worked-example AI agent (property-management assistant). First wiki appearance — deferred entity promotion (single source).
- **[[Braintrust]]** — the observability tool Nurture Boss uses (Husain's anonymised data lives there). Also the vendor anchor in [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie 2025]]. Second source citing Braintrust — eligible for entity promotion per the second-source rule.
- **Dangling** (single-source mentions, deferred): [[Arize]], [[LangSmith]], **Maven**, **Ankur Goel** (Braintrust CEO, mentioned in Guthrie 2025 too — also second-source-eligible).

Body-wikilink coverage for `relationships:` is satisfied through this section and the Convergence table above.

## Open questions raised

- Husain claims TPR/TNR-based aggregation should ideally collapse into a single F1-style number for dashboarding but defers the data-science detail. The wiki doesn't yet have a synthesised reference on which aggregation function survives the *Goodhart-on-evals* trap.
- The Maven course referenced is not in the corpus. If the slides or notes ever surface, they would be a higher-density source than the interview.
- The Nurture Boss eval architecture is described qualitatively; no second source has yet documented an in-the-wild AI-agent-eval architecture at this level of operational detail.

## Related sources

- [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair]] — vendor-engineer view of the same flywheel; same 2025 evals-as-discipline wave; 3-month gap.
- [[2026-03-20-huggingface-agentic-evaluations-workshop]] — the *research/policy/industry* vantage on evals from the agentic-systems frontier; together with Husain they bracket the practitioner-↔-frontier span.
- [[concepts/agent-development-lifecycle]] — ADLC concept page that Husain's workflow concretises.
- [[concepts/agent-harness]] — Contracts + Compounding layers Husain's discipline serves.
