---
type: source
kind: paper
title: "Towards Scalable Measurement of Durable Skills"
author: ["Amir Globerson", "Amy Keeling", "Anisha Choudhury", "Anna Iurchenko", "Aviad Segal", "Avinatan Hassidim", "Ayça Çakmakli", "Ben Gomes", "Benn Witt", "Cathy Cheung", "Cristine Legare", "Diana Akrong", "Eliad Carmi", "Elisabeth Bauer", "Gal Elidan", "Hadas Gelbart", "Hairong Mu", "Katherine Chou", "Lev Borovoi", "Nir Kerem", "Niv Efron", "Noa Kerrem Gilo", "Preeti Singh", "Rajvi Kapadia", "Rena Levitt", "Roni Rabin", "Ronit Levavi Morad", "Rotem Yulzary", "Shashank Agarwal", "Sophie Allweis", "Tracey Lee-Joe", "Tzvika Stein", "Yael Bar Moshe", "Yael Haramaty", "Yaniv Carmel", "Yishay Mor", "Yoav Bar Sinai", "Yoav Bergner", "Yossi Matias", "Yuri Lev"]
publisher: "Google Research"
journal_volume: "Preprint, 12 April 2026"
url: ""
date_published: 2026-04-12
date_ingested: 2026-05-07
tags: [durable-skills, future-ready-skills, 21st-century-skills, ai-assessment, generative-ai, gemini, llm-as-judge, psychometrics, collaboration, creativity, critical-thinking, scalable-assessment]
length: "~31 pages (full ingest including appendix rubrics)"
raw: "../../raw/papers/toward_scalable_measurement_of_durable_skills.pdf"
---

# Globerson et al. — Towards Scalable Measurement of Durable Skills

## TL;DR

A **Google Research** preprint (12 April 2026) by ~30 authors with collaborators at **NYU**, **University of Texas at Austin**, and **OpenMic**. The paper tackles a long-standing measurement problem: **durable skills** (collaboration, creativity, critical thinking — also called "21st-century skills" or "future-ready skills") are widely agreed to be central to the modern workforce, yet measuring them at scale has been infeasible. Open-ended human-human interactions are ecologically valid but psychometrically noisy; structured human-agent tasks (PISA-style) sacrifice authenticity for control.

**Core contribution:** an LLM-orchestrated assessment platform — **Vantage** — that resolves the validity-vs-rigor tradeoff. A human subject converses with multiple AI teammates on group tasks (~30 minutes, 50 turns); a single **"Executive LLM"** generates responses for *all* AI teammates and *steers the conversation* toward eliciting observable evidence for the skill being measured; a separate **AI Evaluator LLM** then scores the transcript against psychometric rubrics.

**Validation (large-N):** 188 US-based participants ages 18-25 (Prolific platform), 373 conversations. Two NYU pedagogical raters provided ground-truth ratings.

- **LLM-vs-human-rater agreement matches inter-human agreement** (Cohen's κ ~0.45–0.64 for both). Auto-rating is a viable scalable substitute.
- **Executive LLM significantly increases skill-evidence elicitation** vs Independent Agents — at conversation level, evidence rates of 92.4% (Project Management) and 85% (Conflict Resolution) when the Executive LLM is skill-matched.
- For a downstream **creativity task** with 280 high-school students (180 held out), Pearson correlation between the Gemini-based autorater and human expert scores reached **0.88**.
- Telling participants which skill to focus on (without LLM steering) had **no effect** (p > 0.6) — the steering needs to come from the AI side.

**Models used:** Gemini 2.5 Pro for the collaboration experiments; Gemini 3 for creativity/critical-thinking initial results. Vantage is described as analogous to a **computerized adaptive test (CAT)** but for *complex social/cognitive* constructs rather than item-difficulty calibration.

## The measurement problem

Durable skills are notoriously hard to measure for three intertwined reasons (cited in the paper's intro):

1. **Definitional fluidity.** Different frameworks operationalize "collaboration" or "creativity" differently — PISA 2015 used scripted simulated teammates with multiple-choice answers; ATC21S used human-human dyads in a digital environment. Both span a small slice of the validity-vs-rigor tradeoff.
2. **Group-task interdependence.** Assessing an *individual* in a group setting is psychometrically hard — other team members introduce uncontrolled variance.
3. **Scarcity of evidence.** As Sijtsma (2011) put it, "long-lasting observation of a person in real life until (s)he spontaneously exhibits the behavior of interest would take too much time before enough evidence was collected." Authentic interactions are evidence-thin per minute; structured assessments are evidence-rich per minute but artificial.

Vantage's design directly responds: **AI teammates introduce zero per-encounter variance** (the Executive LLM is reproducible) AND **steer the conversation to elicit evidence at high density** (analogous to CAT increasing item informativeness).

## The Vantage / Executive LLM architecture

```
Participant ⇄ AI Teammates (Executive LLM driving all of them)
                             ↓
                    Conversation transcript
                             ↓
                    AI Evaluator (separate LLM)
                             ↓
                    Skill rubric scores
```

Three architectural choices distinguish this from naïve LLM teaming:

- **Single Executive LLM, multiple personas.** Rather than one LLM per teammate ("Independent Agents"), a single LLM generates responses for *all* AI teammates. It has access to the assessment rubric and is prompted to **maximize information about the participant's skill level**. If "Conflict Resolution" is being assessed, the Executive LLM may have one teammate start a conflict and maintain it until evidence of resolution is observed.
- **AI Evaluator separated from Executive.** The scorer doesn't drive the conversation. Each subject turn is rated 20 times by Gemini 3.0 against the multi-dimensional rubric (linear regression for scores; logistic regression for "no-evidence" NA labels), with leave-one-out cross-validation for model performance.
- **Adaptive in conversation flow, not item difficulty.** Standard CAT varies item difficulty within a narrow domain (e.g., math). The Executive LLM varies *conversational dynamics* in a group task — heightening or softening conflicts, creating project-management opportunities, or eliciting additional creative ideas.

## What was assessed

| Skill | Sub-skills | Rubric source |
| ----- | ---------- | ------------- |
| **Collaboration** | Conflict Resolution; Project Management | Team cognition (Cannon-Bowers & Salas; Mohammed et al.); shared mental models; grounding (Clark & Brennan 1991) |
| **Creativity** | Generating Ideas (fluidity, originality, quality); Evaluating Ideas (elaborating, selecting); Building on Ideas | Said-Metwaly et al. systematic review; OECD 2019 fostering creativity report; CAT-aligned divergent + convergent thinking |
| **Critical Thinking** | Interpret and Analyze; Evaluate and Judge | Facione (Delphi report 1990); Ennis 1991; Halpern 1998; explicitly includes "AI-Supported Exploration" and "AI-Supported Verification" as sub-categories |

All rubrics use a 4-level scale (Beginning/Emerging/Developing/Demonstrating; or Dormant/Emerging/Demonstrating/Excelling for creativity), with explicit behavioral indicators per level. Tasks were designed to be **ill-structured / ambiguous** (e.g., a critical-thinking task asks the participant, as a "Chief Editor", to evaluate a deliberately flawed editorial about teen social-media policy — forcing detection of motivated reasoning rather than fact-checking).

Notable methodological choice: **the critical-thinking rubric explicitly evaluates how well participants** ***use AI tools*** **during the assessment** (e.g., for fact-checking, retrieval, stress-testing arguments). The paper treats AI fluency as a sub-component of critical thinking in 2026, not a confounder.

## Key results

### 1. LLM auto-rating is on par with human expert raters

Cohen's κ measured at conversation level for Conflict Resolution and Project Management:

- **Inter-human-expert agreement**: κ in the 0.45–0.64 range (moderate, per Landis-Koch; consistent with the inherent ambiguity of these constructs).
- **LLM-vs-human-expert agreement**: similar range. The LLM is approximately as reliable as a human expert at scoring.

Interpretation: automatic rating is a **scalable alternative** to human rating in this assessment setup. Subsequent experiments use only autoraters.

### 2. Executive LLMs elicit significantly more skill-relevant evidence

Comparing three conditions — Executive LLM focused on Conflict Resolution, Executive LLM focused on Project Management, and Independent Agents — at both turn level and conversation level:

- An Executive LLM focused on a skill **always** elicits significantly more evidence for that skill than Independent Agents (p ≤ 0.05, Fisher exact test).
- A desirable cross-over: steering toward CR *increases* CR evidence and *decreases* PM evidence, and vice versa. The Executive LLM is doing what it's designed to do.
- At conversation level with skill-matched Executive LLM: **92.4% of conversations had sufficient PM evidence** and **85% had sufficient CR evidence** for a skill-level rating.

### 3. Telling subjects to "focus on the skill" is not sufficient

Participants who received text prompts like "In the following task, pay particular attention to your role in [Conflict Resolution]" showed **no significant effect** on conversation informativeness (all p > 0.6). Steering must come from the AI side; subject focus alone doesn't substitute.

### 4. Recovery of "known" skill levels using simulated subjects

To assess construct validity, an LLM was prompted to *simulate* a subject at a fixed skill level L. The autorater then inferred a level L̂ from the simulated conversation. **Mean Absolute Error |L̂ − L|** was significantly lower for Executive LLM than for Independent Agents on both Conflict Resolution (~0.20 vs ~0.65) and Project Management (~0.40 vs ~0.55).

### 5. Creativity assessment — a 0.88 correlation with human experts

In a partnership with **OpenMic** (a startup developing AI-powered tools for assessing durable skills), 280 high-school students completed a complex multi-modal creativity task: read a short story, design a news segment based on it, generate character interview questions, and so on. 100 submissions tuned the rubric and Gemini prompt; 180 held-out submissions evaluated the autorater.

- **Pearson r = 0.88** between Gemini autorater scores and human expert scores on total submission grades.
- Per-item Cohen's κ = 0.66 (good agreement).

The paper notes that aggregate-score correlation is the more relevant validity signal, since real-world skill assessment uses overall proficiency, not per-item ratings.

## Limitations the paper acknowledges

- **Cultural situatedness.** The authors explicitly flag: "human skills are culturally situated, and will therefore also focus future work on exploring performance across diverse cultural settings and languages to ensure our technology is inclusive and equitable." Current results are US, English-speaking, ages 18-25 (Prolific recruitment).
- **Authenticity-vs-control tradeoff partially preserved.** AI teammates are still less variable than real human teammates. The paper frames this as an acceptable trade for comparability and reliability — but it's a real cost.
- **Critical thinking and creativity validation is partial.** Inter-human-rater data was collected only for collaboration; CT and creativity rely on simulated-subject recovery (CT) and OpenMic partnership data (creativity). Full human-rated CT/creativity validation is "ongoing."
- **Construct validity vs criterion validity.** The paper measures *construct* validity (Cronbach & Meehl 1955) — does the test measure the construct? It does not yet establish *criterion* validity — does the score predict real-world outcomes (manager reports, teacher reports over semesters, downstream career success). The authors acknowledge criterion validity is the gold standard but is "largely impractical" to collect at scale.

## Cross-source positioning

This paper enters the wiki primarily as the **first operational anchor** for the durable-skills concept (a new wiki concept, [[durable-skills]], promoted in this ingest). It also has substantial methodological overlap with several existing entries:

- **Reinforces and extends [[ai-benchmarks]].** The Vantage system is explicitly methodologically distinct from existing benchmarks (PISA 2015, ATC21S, METR task horizons). It demonstrates a path for scalable assessment of *complex social/cognitive constructs*, not just tasks. Adds a row to the wiki's benchmark roster.
- **Anchors the inverse of [[ai-deskilling]].** Where deskilling asks *which skills are AI substituting away*, this paper measures *which skills humans should retain* — the same labor-economics question viewed from the other side. The two concept pages now reference each other.
- **Extends [[generative-ai]].** A specific deployed application of Gemini 2.5 Pro and Gemini 3 in a measurement system, with concrete validation data (κ ranges, Pearson 0.88). Adds to the wiki's roster of empirical GenAI productivity / measurement applications.
- **Methodological overlap with [[2026-04-29-boussioux-crowdless-future|Boussioux et al. (Crowdless Future)]].** Both papers use LLMs to evaluate creative outputs against rubrics. Boussioux uses GPT-4 as a generator+evaluator in human-AI ideation; Globerson et al. use Gemini as evaluator only, with humans doing the producing. Together they establish "LLM-as-judge" as a recurring methodological pattern in 2024-2026 AI research — worth tracking as a possible future concept page if a third source extends it.
- **Adjacent to [[automation-vs-augmentation]].** Vantage is itself a deep augmentation system — AI doesn't replace the human assessor (rubrics still come from pedagogical experts) but *amplifies* the assessor's reach by automating the evaluation. A textbook augmentation pattern.
- **Adjacent to [[responsible-ai]].** The cultural-situatedness limitation, the construct-vs-criterion validity gap, and the explicit inclusion of "evaluate AI-generated content for bias" as a critical-thinking sub-skill all touch RAI.

## Source-quality flag

- **Type:** Google Research preprint, not a peer-reviewed journal article. © 2026 Google.
- **Empirical rigor:** large-N (188 participants, 373 conversations, 280 students), multi-method (human-human inter-rater agreement; LLM-vs-human agreement; simulated-subject recovery; cross-corpus generalization to OpenMic creativity tasks). Reports Cohen's κ, Fisher exact test, Pearson r, Mean Absolute Error.
- **Confidence boost:** +0.05 per the [§Lifecycle](../../CLAUDE.md#lifecycle) "additional supporting source" rule, **plus** +0.05 for being a large-N empirical study (counts once).
- **Vendor-of-deployment caveat:** Google Research has commercial interests in Gemini deployment. The paper validates Gemini-based autoraters using human raters, which mitigates but does not eliminate the bias.
- The results are sufficiently strong (Pearson 0.88; LLM-vs-human κ matching human-vs-human κ) and sufficiently methodology-honest (acknowledged limitations in cultural scope and criterion validity) that this is a high-quality source. Treat as research-grade preprint.

## Linked entities and concepts

**Entities (this wiki):** [[Google Research]] *(new — promoted from dangling; Google has been mentioned across multiple wiki sources as a model contributor and AI Index funder, and this paper is the first dedicated entity-level anchor)*. **Dangling** (single-mention, deferred): Amir Globerson and ~30 other individual paper authors; **OpenMic** (the AI-skills-assessment startup partner — startup, single mention; promote to entity if a 2nd source covers them); **NYU** and **UT Austin** (academic affiliations; would tip into entity territory if a 2nd source from these institutions ingests).

**Concepts:** [[durable-skills]] *(new — this paper is the operational anchor)*, [[ai-benchmarks]] (heavy enrichment — Vantage as a new evaluation methodology), [[ai-deskilling]] (light enrichment — provides the inverse measurement frame), [[ai-employment-effects]] (light — durable skills are the labor-market anchor), [[generative-ai]] (Gemini 2.5 Pro and Gemini 3 deployed; LLM-as-judge methodology), [[foundation-models]] (Gemini family entries), [[responsible-ai]] (cultural-situatedness; AI-supported critical-thinking sub-skills).

**Threads/syntheses:** none directly affected (this paper sits in a different cluster than the organizational-frameworks-for-ai-adoption synthesis).

## Source

- **Raw PDF (~31 pages, full ingest):** [paper file](../../raw/papers/toward_scalable_measurement_of_durable_skills.pdf)
- **Publisher:** Google Research (preprint)
- **Date:** April 12, 2026
- **Lead institutions:** Google Research; New York University; The University of Texas at Austin; OpenMic
- **Authors:** ~40 co-authors (full list in the frontmatter `author` field; note: paper has no clearly designated lead author — this is a team paper)
