---
type: source
kind: paper
title: "GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks"
author: ["Tejal Patwardhan", "Rachel Dias", "Elizabeth Proehl", "Grace Kim", "Michele Wang", "Olivia Watkins", "Simón Posada Fishman", "Marwan Aljubeh", "Phoebe Thacker", "Laurance Fauconnet", "Natalie S. Kim", "Patrick Chao", "Samuel Miserendino", "Gildas Chabot", "David Li", "Michael Sharman", "Alexandra Barr", "Amelia Glaese", "Jerry Tworek"]
publisher: "OpenAI (arXiv:2510.04374v1)"
url: "https://arxiv.org/abs/2510.04374"
date_published: 2025-10-05
date_ingested: 2026-06-13
length: "~29 pages (full text read: abstract, §1–6, results/figures; appendices skimmed)"
raw: "../../raw/papers/2510.04374v1.pdf"
tags: [gdpval, ai-benchmarks, ai-employment-effects, economically-valuable-tasks, bls-onet, win-rate, human-expert-comparison, frontier-models, claude-opus-4-1, gpt-5, automation-vs-augmentation, openai, reasoning-effort, scaffolding, knowledge-work, foundational-benchmark]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: published-by
    target: OpenAI
    via: "OpenAI research paper; public grader at evals.openai.com"
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "complementary capability-trend record — GDPval adds a non-saturating, economically-grounded benchmark to the AI Index's saturating academic-benchmark tracking"
---

# GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

OpenAI's **economically-grounded capability benchmark** (arXiv:2510.04374v1, 5 Oct 2025): instead of an academic test, GDPval measures how frontier models perform on **real deliverables drawn from real expert work** across the occupations that contribute most to US GDP. It is the wiki's first **direct AI-capability-measurement primary source** — distinct from the adoption/usage record ([[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]]) and the academic-benchmark record ([[2026-04-30-ai-index-report-2026|AI Index]]) — and the primary source behind a benchmark the [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe agent-evaluation guide]] had named as a deferred-ingest candidate. Lead author Tejal Patwardhan, et al.; 19-author byline, [[OpenAI]].

## TL;DR

- **What it measures.** 1,320 tasks across **44 occupations** in the **top 9 US-GDP sectors** (collectively ~$3T annual wages). Occupations chosen as the 5 highest-wage *predominantly-digital* occupations per sector (≥60% of O*NET tasks classified digital). Each task is built from the actual work product of an industry expert (avg **14 years' experience**), validated over multiple review rounds, and tied to the real time/cost to complete.
- **Realistic and hard.** Tasks span CAD files, photos, video, audio, slide decks, spreadsheets, support transcripts; require parsing up to 38 reference files (17 in the gold subset); take an expert an **average of 7 hours** (up to multiple weeks) to complete.
- **The metric is win rate vs human experts** — deliberately *non-saturating*. Blind pairwise expert grading of model vs human deliverables; the baseline can be swapped for stronger models over time, so the benchmark never tops out (unlike MMLU/GPQA-style accuracy scores).
- **Headline result (Oct 2025).** Models evaluated: GPT-4o, o4-mini, o3, GPT-5, **Claude Opus 4.1**, Gemini 2.5 Pro, Grok 4. **Claude Opus 4.1 was the best model**, with **47.6% of its deliverables graded wins-or-ties** against human experts on the gold subset — "model deliverables outperformed or matched expert humans in just over half the tasks." Performance is **improving roughly linearly over time**. *Frontier models are approaching industry experts in deliverable quality.*
- **Model personalities.** Claude Opus 4.1 excelled at **aesthetics** (document formatting, slide layout; better on `.pdf`/`.xlsx`/`.ppt`); GPT-5 excelled at **accuracy / instruction-following** (better on pure text). Across models, the most common reason experts preferred the human was **failure to fully follow instructions**; GPT-5 lost mainly on formatting, had the fewest instruction-following misses.
- **Human oversight beats either alone, cheaper and faster.** Under a "try the model, fix it yourself if unsatisfactory" workflow, pairing frontier models with expert oversight saved both time and money vs unaided experts — the empirical core of the [[automation-vs-augmentation|augmentation]] case.
- **Capability is steerable.** More **reasoning effort**, more **task context**, and better **scaffolding** all improve scores. A general (non-overfit) prompt to self-check layouts/formatting cut PowerPoint formatting errors 86%→64%, eliminated black-square PDF artifacts, drove multimodal self-inspection 15%→97%, and lifted win rate +5pp. Best-of-N (N=4) with a GPT-5 judge helped further.
- **Open-sourced.** 220-task gold subset (prompts + reference files) released; experimental automated grader at evals.openai.com (66% agreement with human graders).

## What was actually ingested

Full 29-page PDF: abstract, introduction, task creation (sector/occupation selection via BLS/O*NET, expert recruitment), grading methodology, results (win rate, speed/cost, model strengths/weaknesses), the reasoning-effort/scaffolding experiments, open-sourcing, and limitations. The numerical appendices (A.2–A.7) were skimmed, not transcribed.

## Why this matters to the wiki

GDPval gives the wiki a **third, distinct empirical lens** on AI-and-work, complementing the two it already holds:

| Lens | Question | Wiki anchor |
|---|---|---|
| **Adoption/usage** | What are people actually doing with AI? | [[2026-04-28-anthropic-economic-index-q4-2025\|Anthropic Economic Index]] |
| **Academic capability** | How do models score on reasoning tests? | [[2026-04-30-ai-index-report-2026\|AI Index]] |
| **Economic capability (this paper)** | Can models produce the actual deliverables of paid expert work? | **GDPval** |

The authors' framing is that capability evaluations are a **leading** indicator where adoption/GDP metrics are **lagging** — you can see economic relevance *before* widespread adoption. This sharpens [[ai-employment-effects]] (capability ≠ deployment; the 47.6% is a capability ceiling, not a labor outcome), gives [[ai-benchmarks]] its first non-saturating economic benchmark, and supplies [[jagged-frontier]] hard evidence that the frontier is uneven *by occupation and modality*, not just by task. The reasoning-effort/scaffolding findings are an empirical echo of the [[agent-harness]] thesis that the wrapper around the model drives performance.

## Limitations (author-stated)

- **Small initial cut** — 44 occupations, 30 tasks each; not comprehensive.
- **Self-contained knowledge work only** — no manual/physical labor; excludes tacit knowledge, PII access, proprietary tools, and inter-person communication.
- **One-shot, precisely-specified, non-interactive** — the full context is handed to the model; real work requires figuring out the context. Performance degrades with less context (their "under-contextualized" experiment).
- **Grader + cost** — the automated grader is a limited proxy; expert grading is expensive.

## W&W lens

Tagged `digital-sensing/digital-scouting`: GDPval is an instrument for **scanning the AI capability frontier** as it bears on economically valuable work — sensing, ahead of adoption, which occupations and task types are becoming automatable. (Single light tag; the paper is otherwise a measurement-methodology contribution rather than a digital-transformation playbook.)

## Linked entities and concepts

- Publisher: [[OpenAI]].
- **Dangling** (single-source, deferred): all 19 named authors (Tejal Patwardhan, Rachel Dias, Elizabeth Proehl, Grace Kim, Michele Wang, Olivia Watkins, Simón Posada Fishman, Marwan Aljubeh, Phoebe Thacker, Laurance Fauconnet, Natalie S. Kim, Patrick Chao, Samuel Miserendino, Gildas Chabot, David Li, Michael Sharman, Alexandra Barr, Amelia Glaese, Jerry Tworek).
- Concepts: [[ai-benchmarks]], [[ai-employment-effects]], [[automation-vs-augmentation]], [[jagged-frontier]], [[foundation-models]].

## Relationships

- *published-by* [[OpenAI]].
- *supports* [[2026-04-30-ai-index-report-2026]] — complementary capability record (GDPval = non-saturating economic benchmark; AI Index = saturating academic benchmarks + adoption stats).
- Closes a deferred-ingest named in [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's benchmark roundup]] (GDPval listed there as "economically-valuable task benchmark").
- Cited directly by [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti (HBR, June 2026)]], who extrapolates the linear trend to ~80% wins-or-ties for mid-2026 frontier models.
