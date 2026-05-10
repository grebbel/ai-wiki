---
type: concept
aliases: ["durable skills", "future-ready skills", "21st century skills", "21st-century skills", "transferable skills", "human skills"]
tags: [durable-skills, 21st-century-skills, future-ready-skills, ai-deskilling, scalable-assessment, psychometrics, ai-evaluation]
confidence: 0.85
last_confirmed: "2026-05-07"
source_count: 4
relationships:
  - type: contradicts
    target: ai-deskilling
    via: "the inverse measurement frame: ai-deskilling asks which skills AI substitutes away; durable-skills asks which skills humans should retain and how to measure them"
  - type: instance-of
    target: ai-employment-effects
    via: "the labour-market consequences turn on which skills remain valuable; durable skills are the supply-side answer"
  - type: depends-on
    target: ai-benchmarks
    via: "measurement methodology — Vantage and similar protocols define new benchmark types for human skills (not model capability)"
---

# Durable Skills

The cluster of human skills that remain economically valuable as AI systems take on more codified, procedural, and information-retrieval work. The canonical examples — repeated across the educational, OECD, and labour-economics literatures — are **collaboration, creativity, and critical thinking**, sometimes joined by **communication, problem-solving, self-regulation, and adaptability**.

The wiki's anchor source is [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. (Google Research, 2026)]], which uses the term *durable skills* in its title and operationalises measurement for three of them. The terminology is not unique to that paper — the same construct appears in adjacent literatures as *21st-century skills*, *future-ready skills*, *transferable skills*, or simply *human skills*. This concept page treats them as substitutable for now and will note vocabulary drift if/when sources push back on the equivalence.

## Working definition

A **durable skill** is a human skill that is:

1. **Open-ended.** Not specifiable as a closed-form rule or a deterministic procedure (otherwise an AI system can encode and execute it).
2. **Socially or contextually situated.** Performance depends on grounding in a specific group, organisation, or domain in ways an AI system cannot reproduce without that context.
3. **Slow-changing.** The skill itself doesn't go stale every 18 months the way a specific tool or framework might.

The term explicitly contrasts with *codified knowledge* (factual content, procedural rules) which is far more substitutable by foundation models. The wiki's [[ai-deskilling]] concept tracks the substitution direction; this page tracks the inverse — which skills humans should retain and how to measure them.

## The measurement problem

Durable skills are notoriously hard to measure at scale. Three reasons recur in the literature ([[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al.]] §1):

1. **Definitional fluidity.** Different frameworks operationalise "collaboration" or "creativity" differently. The major prior efforts — **PISA 2015** (scripted simulated teammates, multiple-choice answers) and **ATC21S** (Assessment and Teaching of 21st Century Skills, human-human dyads in a digital environment) — span only a small slice of the validity-vs-rigor tradeoff.
2. **Group-task interdependence.** Assessing an *individual* in a collaboration setting is psychometrically hard — other team members introduce uncontrolled variance.
3. **Evidence scarcity.** As Sijtsma (2011) put it, "long-lasting observation of a person in real life until (s)he spontaneously exhibits the behavior of interest would take too much time before enough evidence was collected." Authentic interactions are evidence-thin per minute; structured assessments are evidence-rich per minute but artificial.

The historical compromise was *highly scripted* AI teammates (PISA) or *highly structured* human dyads (ATC21S). Both sacrifice authenticity to measurement reliability.

## Vantage / Executive LLM — the 2026 measurement breakthrough

[[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al.]] introduce **Vantage**, an LLM-orchestrated assessment platform that resolves the validity-vs-rigor tradeoff via two architectural choices:

- **Single Executive LLM driving multiple AI teammates.** Rather than independent agents, one LLM generates responses for *all* AI teammates and is prompted to maximise information about the participant's skill level — analogous to a computerized adaptive test (CAT) but for *complex social/cognitive constructs* rather than item difficulty.
- **Separate AI Evaluator.** A different LLM scores the conversation transcript against multi-dimensional rubrics (linear regression for scores; logistic regression for "no-evidence" labels), with leave-one-out cross-validation.

**Validation (large-N):** 188 participants ages 18-25 (US-based, Prolific), 373 conversations.

| Metric | Result |
| ------ | ------ |
| Inter-human-expert agreement (Cohen's κ) | 0.45–0.64 (moderate) |
| LLM-vs-human-expert agreement (Cohen's κ) | matches inter-human |
| Conversation-level evidence rate (skill-matched Executive LLM) | 92.4% PM, 85% CR |
| Independent Agents (no steering) | significantly less skill-evidence |
| Telling subject "focus on this skill" alone | no significant effect (p > 0.6) |
| Creativity autorater vs human expert (n=180) | **Pearson r = 0.88** |

This is the first scalable, ecologically-valid, psychometrically-controllable durable-skills assessment in the wiki — and arguably in the published literature given the validation rigour. Adds a row to [[ai-benchmarks]].

## Skills measured (Globerson et al. operational definitions)

| Skill | Sub-skills | Conceptual basis |
| ----- | ---------- | ---------------- |
| **Collaboration** | Conflict Resolution; Project Management | Team cognition (Cannon-Bowers & Salas); shared mental models; grounding (Clark & Brennan 1991) |
| **Creativity** | Generating Ideas (fluidity, originality, quality); Evaluating Ideas (elaborating, selecting); Building on Ideas | Said-Metwaly et al. systematic review; OECD 2019 fostering creativity report; CAT-aligned divergent + convergent thinking |
| **Critical Thinking** | Interpret and Analyze; Evaluate and Judge | Facione (Delphi report 1990); Ennis 1991; Halpern 1998 |

Notable methodological choice in the **critical-thinking** rubric: **AI-Supported Exploration** and **AI-Supported Verification** are explicit sub-categories. Globerson et al. treat AI fluency as a sub-component of critical thinking in 2026, not a confounder. A participant who blindly accepts the AI's output is rated lower than one who uses the AI to fact-check, retrieve specific information, and stress-test arguments. This is a notable update on Facione/Ennis-era critical-thinking definitions.

## Why this matters for the wiki

The durable-skills concept sits at the **intersection of three open questions in the wiki's labor-and-AI cluster**:

1. **What replaces the entry-level pipeline?** [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. (2025)]] showed early-career workers (22-25) in AI-exposed occupations have ~13% relative employment decline since 2022, concentrated in *automation* uses. If durable skills are what differentiate non-substitutable workers, then operationalising them tells us which entry-level training/curriculum still pays — a question the wiki has not been able to answer concretely until now.
2. **Which skills are decaying via [[ai-deskilling]]?** Deskilling is the substitution direction; durable skills are the retention direction. The two concepts together carve up the labor-skill space: codified-and-AI-substitutable vs. open-ended-and-AI-resistant.
3. **What's the operational definition of "AI-augmentative" work?** [[automation-vs-augmentation]] tracks the empirical split between AI uses that substitute for vs complement labor. Durable skills are the *content* of what augmentation augments — if we can measure them at scale, we can audit whether deployments are actually building durable-skill capacity in the workforce or hollowing it out.

## Cross-source positioning (descriptive only)

Other wiki sources have touched the underlying construct without using "durable skills" terminology:

- **Brynjolfsson, Chandar & Chen (2025)** — Canaries in the Coal Mine. Empirical labor-market evidence that *young* workers in AI-exposed occupations are losing employment, but doesn't operationalise *which skills* remain valuable. Durable-skills work is the missing supply-side measurement.
- **AI Index 2025 / 2026** — repeatedly cite McKinsey workforce-reshaping statistics ("46% expect >20% of the workforce to need reskilling") without a clean operational definition of *what* the reskilling targets should be. Durable skills are a candidate answer.
- **Anthropic Economic Index (Q4 2025)** — measures task complexity and AI autonomy at population scale on Claude.ai conversations. Doesn't directly measure individual durable skills, but the "task success" primitive captures something adjacent.
- **[[2026-05-07-anthropic-economic-index-5-learning-curves|Anthropic Economic Index 5 — Learning curves (Feb 2026)]]** — quantifies a different kind of *learnable* skill: **AI literacy itself**. High-tenure Claude users achieve **~3-4 percentage points higher task success** than lower-tenure users *after controlling for* task type, model selection, and conversation complexity. Model selection slopes (Opus differentially used for higher-value tasks: +1.48 pp per +$10/hour on Claude.ai; +2.79 pp on the 1P API) demonstrate that *choosing the right model tier* is itself a learnable behaviour visible in usage logs. This is a complementary kind of "durable skill" — not the open-ended, contextually-situated skills the Globerson paper measures, but rather a procedural meta-skill (knowing how to deploy AI well) that nonetheless is *learned-by-doing* and produces measurable productivity returns. Open question for synthesis: is AI-literacy a 5th durable skill alongside collaboration, creativity, critical thinking — or is it a fluency that *enables* the other three to operate in AI-saturated work environments?
- **[[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024 — Learning to Manage Uncertainty, With AI (MIT SMR × BCG)]]** — provides the *organizational-level* counterpart to Globerson's individual-level measurement. The 5-question organizational-learning battery (test-and-learn; failure tolerance; postmortem culture; learning codification; knowledge sharing) and the 4-question AI-specific-learning battery (AI generates new learning; AI learns from performance; human-feedback-loop AI; employees learn from AI) together define *what kind of organizational capacity* AI augments. **Augmented Learners** — the 15% combining both — outperform Limited Learners by 1.6× on uncertainty management and 1.4× on revenue benefits. The construct is *adjacent* to durable skills but at a different layer: durable skills measure individual humans; Augmented Learners measure organizational capacity. Both depend on the same underlying capability — converting tacit knowledge into surfaced, shareable, AI-readable form.
- **[[2026-05-07-kiron-schrage-compound-benefits|Kiron & Schrage 2026 — How to Reap Compound Benefits From Generative AI]]** — supplies the **strongest claim in the wiki to date** about which durable skill is now *most* economically valuable: **the expert as evaluator**. Direct quote: *"The expert as evaluator is not a transitional role."* Mechanism: where verification compares output against existing standards, **evaluation may generate standards that did not exist before** — and that requires domain expertise. The column reframes durable expertise around a specific operational role (recognizing what "not perfect" actually means; knowing what iteration may reveal). Also names the **Polanyi tacit-dimension breach** — LLMs no longer just codify explicit knowledge; they infer tacit knowledge from behavioral traces at scale. *Tacit expertise was a moat; it is no longer.* This sharpens the durable-skill question: if AI inferences tacit knowledge, what's left for humans? The answer the column proposes: the *judgment to evaluate what AI produces*, which itself depends on having previously developed deep expertise. **Implication**: deploy AI first in domains where your people already have deep expertise, *not* because AI needs hand-holding but because evaluation requires recognizing meaningful gaps. **CLAUDE.md as a worked example**: when developers write CLAUDE.md files specifying what "good" code looks like, *that* is tacit-to-explicit conversion at the team level — operationally identical to what Globerson's Vantage assessment elicits at the individual level.
- **OECD Digital Education Outlook 2026** (cited in Globerson et al. ref [68]) — mainstream educational policy framing of "21st-century skills" matches the durable-skills construct closely.

The construct is recurring; the operational measurement is new in 2026.

## Open questions and limitations

- **Cultural situatedness.** Globerson et al. explicitly acknowledge: "human skills are culturally situated, and will therefore also focus future work on exploring performance across diverse cultural settings and languages to ensure our technology is inclusive and equitable." Current empirical results are US, English-speaking, ages 18-25. Generalisation is a real open question.
- **Construct validity vs criterion validity.** The Vantage validation establishes construct validity (the test measures the construct as defined by the rubric). It does *not* establish criterion validity (the score predicts real-world outcomes — manager reports, teacher reports over semesters, downstream career success). Criterion validity is the gold standard but is "largely impractical" to collect at scale, per the paper.
- **Single-source operational definition.** The wiki has only one source operationalising the durable-skills construct so far. The terminology cluster (durable skills / 21st-century skills / future-ready skills / human skills) is consensus across the broader literature, but a 2nd ingest would substantially raise confidence and surface vocabulary disagreements.
- **Are durable skills actually durable under sustained AI augmentation?** [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (2025)]] showed augmentation under deliberate human-in-the-loop design produces +15% productivity and equalising effects — but also small quality declines among top performers. If the AI's training data degrades because skilled humans lean on it instead of producing original judgments, do "durable skills" stay durable? Open question.

## Debates and supersession

(None yet — single primary source.)

## Related concepts

- [[ai-deskilling]] — the inverse: which skills are getting hollowed out by AI use.
- [[ai-employment-effects]] — the labor-market consequences. Durable skills are the supply-side answer to "what protects employment?"
- [[ai-benchmarks]] — durable-skills assessment is methodologically a new *type* of benchmark (for humans, not models).
- [[automation-vs-augmentation]] — durable skills are the *content* of augmentative work; codified knowledge is the substrate of automative work.
- [[generative-ai]] — the substrate that creates the deskilling pressure *and* powers the new measurement methodology.
- [[responsible-ai]] — the cultural-situatedness limit and the AI-supported-critical-thinking sub-skills are RAI-adjacent considerations.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "durable-skills") OR contains(tags, "21st-century-skills") OR contains(tags, "future-ready-skills")
SORT file.name ASC
```
