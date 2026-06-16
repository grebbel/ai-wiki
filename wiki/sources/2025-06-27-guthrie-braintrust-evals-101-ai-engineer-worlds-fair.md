---
type: source
kind: video
title: "Evals 101 — Doug Guthrie, Braintrust"
author: ["AI Engineer"]
url: "https://www.youtube.com/watch?v=bk0TmxoZlUY"
date_published: 2025-06-27
length: "~48:31 minutes (transcript ~217 grouped segments from 1280 raw ASR lines)"
raw: "../../raw/videos/guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md"
tags: [evals, ai-evaluation, llm-as-judge, observability, agent-development-lifecycle, agent-harness, braintrust, ai-engineer-worlds-fair, flywheel-effect, human-in-the-loop, online-scoring, offline-evals]
relationships:
  - type: supports
    target: agent-development-lifecycle
    via: "fills in the Test phase of Chase's Build->Test->Deploy->Monitor->Iterate loop with operational vocabulary: task / dataset / scores; offline vs online evals; LLM-as-judge vs code-based scores; online scoring with sampling rates"
  - type: supports
    target: agent-harness
    via: "the eval discipline operationalises Chatterjee's Contracts (scored output against criteria) and Compounding (telemetry feeds learning) harness layers; Braintrust is the wiki's first vendor-specific eval-platform anchor"
  - type: supports
    target: agentic-engineering
    via: "specs+tests-and-iterate is exactly the agentic engineer's primary artefact pattern; Hu's software factories and Karpathy's spec-driven discipline both require an eval layer Braintrust represents commercially"
  - type: supports
    target: 2025-09-28-husain-ai-evaluations-clearly-explained-50-min
    via: "Husain (3 months later) describes the same offline→online→learning flywheel from the practitioner-trainer vantage with vendor-neutral tooling (Google Sheets, pivot tables, binary LLM-as-judge with TPR/TNR); Guthrie is the vendor-engineer 'what', Husain is the human-process 'who and how'"
  - type: supports
    target: 2026-03-20-huggingface-agentic-evaluations-workshop
    via: "HF Agentic Evals Workshop (9 months later) is the research-frontier conversation about what makes the benchmarks Guthrie's flywheel runs *against* trustworthy in the first place (Narayanan's capability-reliability gap, Habib's scar-fragmentation, Sathiamoorthy's level-0-vs-level-1 verifiability)"
---

# Evals 101 — Doug Guthrie, Braintrust

> This hands-on workshop guides participants through the full AI evaluation lifecycle with Braintrust, from initial prompt testing to production monitoring. Attendees will build evaluation frameworks, practice offline and online strategies, and implement logging systems.
>
> Doug Guthrie is a solutions engineer at Braintrust. Previously, he helped customers deploy data infrastructure at dbt Labs.
>
> Recorded at the AI Engineer World's Fair in San Francisco.

(Channel description, [[AI Engineer]].)

A 48:31 hands-on workshop by **Doug Guthrie** (Braintrust solutions engineer) at the [[AI Engineer]] World's Fair in San Francisco. Published 27 June 2025 to the AI Engineer YouTube channel — **the wiki's earliest source on AI evaluation as a formalised discipline**, predating the wiki's existing eval-adjacent sources by ~9 months. ASR caption track; no chapters.

## TL;DR

The wiki's **first vendor-specific anchor on the eval/observability layer**. Three substantive contributions:

1. **The four ingredients of an eval**: **task** (the code or prompt to evaluate — *"this can be as simple as a single prompt or it could be this full agentic workflow"*); **dataset** (real-world examples to run the task against; input + optional expected + optional metadata); **scores** (the logic behind the eval — **LLM-as-judge** or **code-based**); and the **experiment** (snapshot in time of an eval, comparing runs over weeks/months to detect regressions). Maps directly onto [[2026-05-09-chase-agent-development-lifecycle|Chase's Test phase]] of the ADLC (datasets / metrics / experiments / simulations) with shared vocabulary; Guthrie's account gives the operational *how* that Chase's framework gives the conceptual *what*.

2. **Offline / online / flywheel — three operational modes that compound**: **Offline** = pre-production iteration (define tasks, scores, datasets; identify and resolve issues before deployment). **Online** = real-time tracing in production (log model inputs/outputs, intermediate steps, tool calls, latency, cost, tokens, duration). **Flywheel** = online logs are filtered (e.g. *user-feedback = 0*) and added back to offline datasets, which inform the next round of offline evals. *"This is what's missing oftentimes when we're building these AI applications and what Braintrust allows for really seamlessly."* The flywheel framing is **structurally identical** to [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]'s verification → evaluation → learning capture cycle and to [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu 2026]]'s *closed-loop company* framing — same compounding pattern at three different scales (telemetry-feedback / org-learning / company-org-design).

3. **The "evals as offense" reframing** — credited to **Anker Goyal** (Braintrust CEO): *"I think people think of [evals] as almost like unit tests for our applications, but [Anker] kind of described it another way of like: this is a really great way for us to play offense as opposed to just playing defense where I think maybe unit tests are kind of used for. This can actually be used as a tool to really help create a lot of rigor around us building and developing these applications and ensuring that we actually build things that we can put into production."* Distinguishes the eval discipline from the test discipline at the framing level — tests catch defects post-hoc; evals drive intent forward. Convergent with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s *"contracts as formal evaluable specifications of what successful output means"* at a different vantage.

## What was actually ingested

Full workshop transcript including the Q&A tail (refrigerator-fix anecdote and government-eval-before-launch question). Light ASR cleanup; the speaker uses heavy filler words (*"like"*, *"really really"*, *"sort of"*) preserved verbatim. Transcript ends mid-Q&A — the recording cuts off during the government-pre-launch-evals question with *"They have huge data sets of thousands of questions, believe me, as a—"* — implying ~45 seconds of further content not captured by the YouTube upload.

## Operational mechanics — the four ingredients

### Task

> *"The really cool thing about Braintrust is that this can be as simple as a single prompt or it could be this full sort of agentic workflow where we're calling out to tools. There's no sort of limit onto the complexity that we put into this task. The only thing it requires is an input and an output."*

The minimum interface is `(input) -> (output)`. Guthrie's worked example uses **a change-log generator**: input is a GitHub repository URL, output is a generated change log based on most-recent commits. The task internally invokes a multi-step agentic workflow (fetch commits → understand latest release → generate change log) — each step traceable as an individual span.

### Dataset

> *"These are our real-world examples. This is essentially what we're going to run the task against to understand how well our application is performing ... The only thing that's required is the input. You also have the ability to add expected. So what is the expected output for that input ... You also have metadata as well."*

Schema: `{input, expected?, metadata?}` per row. Metadata is load-bearing for filtering: *"being able to filter down different things pulling the data set maybe into your own codebase and 'I want to filter by X, Y, or Z' via the metadata."* Worked example score that pairs with expected: **Levenshtein distance** (named explicitly by Guthrie) — *"allows you to measure the difference between [output and expected]. So you can do some different things based on what you provide to that dataset."*

Critical operator-advice from Anker Goyal (Braintrust CEO), repeated multiple times by Guthrie: ***"Just get started — create that baseline that you can then iterate and build from. A lot of people get caught in creating this golden dataset of test cases that they can then iterate from. Start — you don't necessarily have to do that. Start and build that baseline."*** The wiki's first first-party-vendor articulation of the *"don't optimise the dataset first"* anti-pattern.

### Scores (the eval logic)

Two score families:

| Score type | What it does | When to use |
|---|---|---|
| **LLM-as-judge** | Give the LLM the output + criteria; it returns a label (excellent/fair/poor) mapped to a numeric (1 / 0.5 / 0) | Subjective quality (relevance, helpfulness, formatting) |
| **Code-based** | Heuristic or binary check in TypeScript/Python (or pull from your codebase into Braintrust) | Deterministic correctness (regex match, JSON validity, Levenshtein distance) |

**Auto-Evals package**: Braintrust ships out-of-the-box scores (both LLM-as-judge and code-based) that *"just allows you to get started very, very quickly."* Mentioned as a pull-in dependency.

Three customer-tested practices Guthrie names:

1. **Use higher-quality models for scoring than for the prompt**. *"While we're running that application to use the cheaper model but use the more expensive one to actually go out and score it."*
2. **Break scoring into focused areas**. Worked example: a change-log task would have **three separate scores** (accuracy / formatting / correctness) rather than one combined score. *"Have your scores be very targeted to the thing that they're supposed to be doing."*
3. **Avoid overloading the score prompt with context**. *"Focus it on the relevant input and the output."*

### Experiment

A snapshot-in-time of an eval run. *"As we are doing this development and we're trying to understand the last month or so — are we getting better, the changes that we are making, the model changes — are we improving our application?"*. Experiments enable regression detection across weeks/months and let the system answer the questions Guthrie opens the talk with:

- *When I change the underlying model, is it getting better or worse?*
- *When I change my prompt, is it getting better or worse?*

Both questions are *"really really hard to [answer] without a rigorous process around building with large language models, which as you all know, [are] non-deterministic outputs."*

## Offline vs online — the two operational modes

| Mode | When | What it measures | Where it lives |
|---|---|---|---|
| **Offline** | Pre-production | Iteration quality against curated datasets; defining tasks + scores + datasets | Playground IDE / SDK |
| **Online** | Production traffic | Real-time tracing: model inputs/outputs, intermediate steps, tool calls, latency, cost, tokens, duration | Instrumented application (wrap LLM clients, decorate functions with trace decorators, span-level customisation) |

### Online scoring with sampling rates

> *"This is where like when our logs are coming in, we can actually configure within the platform those scores that we want to run and we can specify a sampling rate. So we don't necessarily run that score across every single log that comes in. Maybe it's 10%, 20%, so on. But it creates that really tight feedback loop."*

**Score-at-the-span-level**, not just root-level — important for agentic workflows. Worked example: a conversational analytics app rephrases the user's question as its first step; if rephrasing is bad, the rest of the chain falls down. *"What I can do is create a score specifically for that span to understand how well the LLM did in rephrasing that question."*

### The flywheel — online → offline feedback

> *"It becomes very very easy now to take the logs that are generated within production and add those back to datasets. This also speaks to some of that human-review component where we want to now bring those humans in. They can start to review some of the logs that are relevant — like maybe there's user-feedback equals zero, maybe there's a comment, whatever it is. They can filter down to those particular things and as they find really interesting test cases, it's very very easy to add those back to the dataset that we use in our offline evals."*

This is the **canonical eval-flywheel** pattern: production failures (low scores or thumbs-down) get filtered, human-reviewed, and become the next generation of offline test cases. The dataset compounds; the eval discipline tightens.

## Human-in-the-loop — two distinct modes

Guthrie distinguishes carefully between:

1. **Human review of logs** — internal-team members (engineers, PMs, even **doctors at a healthcare-customer company** Guthrie mentions) parse logs in a paired-down review UI, scoring against configured rubrics.
2. **User feedback** — application-end users provide thumbs-up/down + free-text comments; their feedback is logged to Braintrust as a score-source.

**Sarah from Notion** (referenced from a prior workshop, not in this transcript): Notion uses *"a special type of role for human-in-the-loop type of interaction — almost like a product manager mixed with an LLM specialist."* For smaller organisations, *"engineers actually go through and do this as well."*

Guthrie's response to a question about scoring-inconsistency-across-human-reviewers: *"Maybe before it gets to that place, like have a rubric, have a guideline of what scoring looks like for your humans."* No platform-side adjudication tool; humans align via rubric, not via inter-rater-reliability machinery.

## The "Loop" feature — eval-driven AI prompt optimisation

Released the day of the workshop (27 June 2025): a Cursor-like IDE feature where AI optimises prompts against eval scores. *"It has access to those evaluation results. And so when it goes to change that prompt, it understands [the eval]: it changes the prompt, it runs the evaluation, it understands if it got better relative to the scores that we defined."* Demonstrated but failed live (*"I think I have an issue with my anthropic API keys"*) — flagged here as a vendor-side feature rather than a fully-validated workflow.

## CI/CD integration

> *"This can be run via CI/CD. We do have some customers that want to run their eval as part of the CI process. So understanding in a more automated way, the score for A and C, whatever they've configured — has it gotten better, has it gotten worse, this becomes maybe a check as part of CI. There is, if you look within our documentation, a GitHub action example that shows you how you could set this up."*

The wiki's first first-party-vendor articulation of **evals-as-CI-check** — a discipline-level practice that completes the offline/online/flywheel loop with a pre-merge gate.

## SDK + version-controlled prompts

Two consumption paths:

- **UI-first** (Playground): prompts/scores/datasets created in Braintrust; *"a healthcare company that has doctors coming into the platform and interacting with the playground."*
- **Codebase-first** (Python/TypeScript SDKs; Go/Java/Kotlin also available): define prompts/scores/datasets in your codebase, push to Braintrust via CLI command. *"Prompts that you create within the UI are version controlled as well."*

The two paths interoperate — anything created in UI is accessible via SDK and vice versa.

## Convergence and contradictions with existing wiki sources

| Source | Connection |
|---|---|
| [[2026-05-09-chase-agent-development-lifecycle\|Chase / LangChain ADLC 2026]] | **Direct vocabulary match**. Chase names *datasets / metrics / experiments / simulations* in the Test phase; Guthrie fills in the operational *how* with task/dataset/scores/experiments. Guthrie's *online scoring* corresponds to Chase's Monitor phase; the flywheel corresponds to Chase's *Iterate* arrow looping back to Build/Test. Two-source convergence on the eval/observability discipline's vocabulary |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | Guthrie's *scores* operationalises Chatterjee's *Contracts* layer (formal evaluable specifications of what "successful output" means); Guthrie's *flywheel* operationalises Chatterjee's *Compounding* layer (structured telemetry → self-tuning). Different vantage on the same construct |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron-Schrage 2026]] | The Braintrust flywheel is the *technical instantiation* of Kiron-Schrage's verification → evaluation → learning-capture organisational pattern. Kiron-Schrage names *"the expert as evaluator is not a transitional role"*; Guthrie's *"human-in-the-loop"* operationalises that role at the eval-platform level — humans curate which production logs become offline test cases |
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu 2026 (YC)]] | Hu names *software factories* (spec + tests + agents-iterate-until-tests-pass) as the architecture; Guthrie's Braintrust workshop is the *eval-tooling layer* a software factory requires. The two together describe a complete software-factory implementation: spec authoring (Hu's framing) + eval scoring (Guthrie's framing). |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex]] | Lopopolo's *custom linters + structural tests + golden-principles GC* are eval-like primitives at OpenAI Codex's vendor scale. Guthrie's Braintrust is the *commercial third-party version* of what Lopopolo built in-house. Convergent on the *need* for the eval layer; divergent on the *build-vs-buy* decision |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler 2026 (Thoughtworks)]] | Böckeler names *evals* as an "early stage" open question — *"Anthropic just released something to make it easier to do evals, the [Tessell?] skills registry also released something recently. So that's kind of in the early stages as well."* Braintrust is the wiki's first **dedicated eval-platform anchor** that fills the gap Böckeler names |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | Karpathy distinguishes agentic engineering (preserves the quality bar) from vibe coding (raises the floor); evals are *the discipline mechanism* by which the quality bar is preserved at agent throughput. Karpathy doesn't name evals specifically; Guthrie supplies the operational vocabulary |
| [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers\|Jassy 2025 (Amazon)]] | Jassy's *Bedrock* middle layer names *guardrails / RAG / agentic capabilities* — eval-like primitives. Guthrie's Braintrust is the third-party-platform analog of what Bedrock packages at the cloud-provider layer |

### Contradictions

None substantive. Guthrie's framing is operator-level prescriptive; the wiki holds no opposing source on the eval discipline.

## Linked entities and concepts

**Concept pages updated**:

- [[agent-development-lifecycle]] — fills in the Test phase with operational vocabulary; second-wiki-source on the ADLC's Test phase after Chase's Build phase taxonomy.
- [[agent-harness]] — Braintrust as the commercial vendor-specific anchor for Chatterjee's Contracts + Compounding layers.
- [[agentic-engineering]] — evals as the discipline mechanism for preserving quality at agent throughput; Guthrie's *"evals as offense"* reframing.

**Dangling** (single-source first-mention, deferred):

- **Doug Guthrie** — Braintrust solutions engineer; presenter; ex-dbt Labs.
- **Braintrust** — end-to-end developer platform for AI products (evals + observability). Strong promotion candidate — likely to recur on future eval-tooling ingests.
- **Anker Goyal** — Braintrust CEO.
- **[[AI Engineer]]** — conference series + YouTube channel (AI Engineer World's Fair).
- **dbt Labs** — Guthrie's previous employer.
- **Versel AI SDK** — named as a wrappable client.
- **Notion** — referenced via Sarah-from-Notion's workshop (separate from this video).
- **Cursor** — referenced as the IDE-paradigm Braintrust's new Loop feature emulates.

**Concept candidates surfaced (not yet promoted)**:

- *Eval flywheel / online-to-offline feedback* — Guthrie's framing. Direct convergence with Kiron-Schrage's verification-evaluation-learning-capture and Hu's closed-loop company. **Three-source convergence threshold met** for a candidate *learning-capture flywheel* concept page distinct from but related to [[micro-productivity-trap]] and [[agent-harness]]'s Compounding layer.
- *LLM-as-judge* — Guthrie names the construct. Single-source for now; likely to recur in eval-related ingests.
- *Auto-evals* — Braintrust's built-in score library. Vendor-specific term; defer to product-page treatment.
- *Score-at-the-span-level* — eval pattern for agentic workflows. Single-source.
- *Evals-as-CI-check* — pre-merge eval gate. Single-source.

## Open questions raised by this source

- **Braintrust competitor landscape** — Guthrie names no direct competitors. Ingests of competing eval platforms (LangSmith, Helicone, Weights & Biases for LLM-ops) would let the wiki triangulate.
- **Inter-rater-reliability in human-in-the-loop** — Guthrie's answer (*"have a rubric"*) is rubric-based, not statistical. Open question: does any eval platform provide IRR / Cohen's kappa / alignment-machinery for multi-reviewer scoring?
- **LLM-as-judge calibration drift** — when the judging model itself improves, does the *meaning* of a "fair" score drift over time? Workshop question (asked by an audience member) acknowledged the relativistic problem; Guthrie's answer (*"eval the LLM-as-judge"*) is recursive but doesn't address drift directly.
- **Sarah-from-Notion's earlier workshop** — primary-source ingest target for the *PM-mixed-with-LLM-specialist* role taxonomy.
- **Strong DM software factory** — Hu's worked example from her YC ingest. Worth tracking whether Strong DM uses Braintrust or a competitor for their eval-layer.
