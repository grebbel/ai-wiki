---
type: source
kind: article
title: "ReAct: Synergizing Reasoning and Acting in Language Models (Google Research Blog)"
author: ["Shunyu Yao", "Yuan Cao"]
publisher: "Google Research Blog"
url: "https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/"
date_published: 2022-11-08
date_ingested: 2026-06-12
length: "~9 pages (full blog post, PDF capture)"
raw: "../../raw/articles/ReAct_ Synergizing Reasoning and Acting in Language Models.pdf"
tags: [react, reasoning-and-acting, agentic-loop, chain-of-thought, tool-use, llm-agents, palm-540b, hotpotqa, fever, alfworld, webshop, google-research, blog, shunyu-yao, popular-science]
relationships:
  - type: authored-by
    target: Shunyu-Yao
  - type: authored-by
    target: Yuan-Cao
  - type: published-by
    target: Google-Research
    via: "Google Research Blog announcement of the ReAct paper"
  - type: supports
    target: 2022-10-06-yao-et-al-react-synergizing-reasoning-acting
    via: "non-peer-reviewed blog popularisation of the same ReAct work; restates the paper's claims and headline results for a general audience"
---

# ReAct: Synergizing Reasoning and Acting in Language Models (Google Research Blog)

The **Google Research Blog** announcement (8 Nov 2022) of the ReAct paper — the accessible, figure-led popularisation of the same work the [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|ICLR 2023 paper]] reports rigorously. Posted by **[[Shunyu Yao]]** (Student Researcher) and **[[Yuan Cao]]** (Research Scientist), Google Research, Brain Team. It is the wiki's secondary, non-peer-reviewed register of the [[react-reasoning-acting|ReAct]] paradigm; the paper is the primary.

## TL;DR

- Frames the problem as two pre-existing but **separate** lines of work: chain-of-thought prompting (reasoning, but *ungrounded* in the external world — can't reactively explore or update knowledge) and LLMs for planning/acting in interactive environments (acting, but *no abstract reasoning over high-level goals or working memory*). ReAct's pitch: **combine them.**
- **ReAct = Reason + Act.** The model generates interleaved verbal reasoning traces and text actions; actions get observation feedback from an external "Env"; reasoning traces don't change the environment but update the model's internal context. Lists the useful thought types: decompose goals into plans, inject commonsense, extract from observations, track progress, handle exceptions.
- **Prompting setup**: frozen PaLM-540B, few-shot in-context. **Fine-tuning setup**: use prompted PaLM-540B to generate trajectories, filter to successes, fine-tune smaller PaLM-8B/62B (reduces human-annotation need).
- **Results** (the blog reproduces the headline tables): on HotpotQA/FEVER ReAct beats act-only and is competitive with CoT, with **ReAct+CoT best**; on ALFWorld ReAct 71 vs Act 45 vs IL 37 (2-shot), on WebShop ReAct 40 vs Act 30.1 vs IL 29.1 (1-shot) — **+34% / +10%** over baselines trained on ~10⁵ instances.
- **Human-in-the-loop correction**: a human inspector edits ReAct's reasoning traces; replacing a hallucinating sentence with inspector hints realigns the agent's behaviour — "new forms of human–machine collaboration."
- Concludes ReAct is "simple yet effective," giving **interpretable decision traces**, and flags follow-on work: multitask training and coupling ReAct with reward models.

## What was actually ingested

The full blog post (9-page PDF capture of the Google Research Blog page), including the four results tables and the figure captions. Content is a faithful subset of the [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|paper]]; no claims here that the paper does not also make.

## Linked entities and concepts

- **Promoted to entities this ingest** (second-source rule — also author the paper): [[Shunyu Yao]], [[Yuan Cao]].
- Concepts: [[react-reasoning-acting]], [[ai-agents]], [[agent-harness]], [[foundation-models]].
- Publisher: [[Google Research]] (Brain team).

## Relationships

- *supports* [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting]] — same work, popular register. Read the paper for the rigorous treatment; this page is the legible summary.
