---
type: thread
status: closed
opened: 2026-04-28
closed: 2026-05-05
synthesized_into: organizational-frameworks-for-ai-adoption
tags: [ai-adoption, organizational-design, frameworks, cross-source-comparison]
---

> [!success] Closed — synthesized 2026-05-05
> This thread was closed when a 5th and 6th framework appeared (McKinsey *Rewired* 2nd ed and Bain/OpenAI). The synthesis lives at [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption synthesis]] and supersedes the analysis below for use as a reference.

# Thread: Multiple frameworks for thinking about AI in organizations — competing or complementary?

## The question

Across the 6 sources ingested so far, **at least four named frameworks** prescribe how organizations should think about AI adoption. They use different vocabulary and target different layers (task / capability / readiness / org-design). Do they compete, or are they complementary lenses on the same underlying problem? When advising an executive, which framework should be picked first?

## The frameworks under comparison

### 1. MIT CISR — Four Stages of AI Maturity + Four S

**Source:** [[2026-04-28-mit-sloan-ai-maturity|Burnham (2025), MIT Sloan]] reporting on [[Stephanie Woerner]], [[Peter Weill]], Ina Sebastian, Evgeny Káganer at [[MIT CISR]].

**Layer:** Capability progression and gap analysis.

**Structure:**
- 4 stages: Experiment / Pilots / Ways of Working / Future-ready (28%/34%/31%/7% in 2022 baseline)
- 4 challenges to scale Stage 2 → Stage 3 (the financial inflection point): **Strategy / Systems / Synchronization / Stewardship**

**Strength:** clear progression model with empirical distribution; locates the financial inflection point precisely.

**Weakness:** 2022 baseline is pre-GenAI explosion; the binary "in-stage" classification hides intra-stage variance.

### 2. Anand-Wu — 2×2 task suitability framework

**Source:** [[2026-04-28-anand-wu-genai-playbook|Anand & Wu (2025), HBR Nov–Dec]].

**Layer:** Task-by-task deployment decisions.

**Structure:** 2×2 matrix on **cost of errors** × **type of knowledge** → four zones:
- **No regrets** (low cost / explicit data) — AI does it all; agents thrive here
- **Creative catalyst** (low cost / tacit) — AI creates options, human selects
- **Quality control** (high cost / explicit) — AI produces, human verifies
- **Human-first** (high cost / tacit) — Human leads, AI assists with minor tasks

**Strength:** directly operational at task level; the framework most likely to influence a procurement or deployment decision today.

**Weakness:** silent on org-level capability or change management; assumes the org can act on per-task decisions.

### 3. MITTRI/Cisco — Five Foundations

**Source:** [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco (2025)]].

**Layer:** Readiness / infrastructure prerequisites.

**Structure:** 5 foundations to get right — **Strategy / Infrastructure / Data / Governance / Culture and Talent**.

**Strength:** explicit on the *prerequisites* (especially infrastructure and data) that the other frameworks tend to assume.

**Weakness:** sponsored by Cisco; "Infrastructure" gets framed in network/security terms aligned with Cisco's commercial offerings. Generic at the strategy/governance/culture levels.

### 4. Werner-Le-Brun — Tin Man vs. Octopus Org

**Source:** [[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun (2025), HBR Nov–Dec]].

**Layer:** Org-design / change-management archetype.

**Structure:** Two archetypes (Tin Man = predictability-optimized machine; Octopus = adaptive, distributed, customer-centric). Three principles for change (with people / entwine learning + impact / do less to achieve more). Three antipattern categories (compromise clarity / undermine ownership / stifle curiosity). Hierarchy of leverage (parameters / system engine / DNA).

**Strength:** the only framework here that's explicit on the **org-design** layer — the one most likely to be the actual bottleneck.

**Weakness:** not primarily about AI; AWS-affiliated authorship colors the framing; lacks empirical distribution data.

### Bonus — Anand-Wu's "Why Don't Gen AI Gains Show Up in My P&L?" exhibit

Worth flagging separately because it's **diagnostic rather than prescriptive**. Six leakage points along the value chain (task efficiency / employee adoption / resource redeployment / org throughput / market demand / competitive retention) with explicit owners (Everyone enabled by CTO/CIO; Every manager enabled by CEO/COO; CEO + C-suite). This is the most directly actionable artifact for an executive trying to figure out *why* their GenAI investment hasn't shown up in P&L.

## Initial reading: complementary, with overlap

The frameworks are **mostly complementary, not competing**:

| Layer | Framework | Question it answers |
|---|---|---|
| Org design | **Octopus / Tin Man** | Is your organization structurally capable of adapting? |
| Readiness | **Cisco 5 foundations** | Do you have the infrastructure / data / governance foundations? |
| Capability progression | **MIT CISR Four Stages + Four S** | What stage are you at, and what blocks the next transition? |
| Task deployment | **Anand-Wu 2×2** | For *this specific task*, should we deploy AI today, and how? |
| Diagnosis | **Anand-Wu leakage points** | If gains aren't showing up in P&L, where in the value chain are they leaking? |

Read top-down, an executive could plausibly use them in this order:
1. **Octopus / Tin Man**: is the org capable of change?
2. **MIT CISR Four Stages**: where are we in maturity progression?
3. **Cisco 5 Foundations**: do the prerequisites exist?
4. **Anand-Wu 2×2**: which tasks to point GenAI at first?
5. **Anand-Wu leakage points**: when ROI underwhelms, diagnose where it leaked.

## Overlap and tension

- **MIT CISR Four S Stewardship vs. Cisco Foundations Governance.** Different vocabulary, same idea — embed RAI in architecture review and governance structures. The MIT CISR framing is sharper (because it's tied to stage transition).
- **MIT CISR Four S Synchronization vs. Octopus principles.** "Create AI-ready people, roles, and teams" vs. "make changes WITH people, not TO them" + customer-centric distributed intelligence. Octopus is more radical — full org redesign — while CISR Synchronization is more incremental (reskilling, role redesign).
- **Anand-Wu's 2×2 vs. MIT CISR's Stage 4 attribute "combining traditional + generative + agentic + robotic AI."** Both are thinking about *how* AI gets deployed, but at different abstractions: 2×2 is per-task; Stage 4 is org-wide capability portfolio.
- **Where do the Cisco "5 foundations" fit in the MIT CISR stages?** Plausible read: foundations 1–4 (Strategy, Infrastructure, Data, Governance) are mostly Stage 1–2 (Experiment / Pilots) work; foundation 5 (Culture and Talent) is needed for Stage 3+ transition. The MIT CISR Four S maps roughly onto a *gap analysis* between foundation states.

## What's missing / candidate sources to find

- **Direct framework comparison.** None of the 4 frameworks acknowledge the others — each is presented as a standalone contribution. A meta-analysis paper bridging them would be valuable. Worth searching for on next lint.
- **Gartner / Deloitte / McKinsey AI maturity frameworks.** The wiki currently lacks the consultancy-firm framings. McKinsey is referenced indirectly via [[AI Index]] (the 78% figure). Gartner's hype-cycle and "AI maturity" model and Deloitte's State of AI in the Enterprise reports would round out the framework landscape.
- **Empirical validation.** Of the four frameworks, only MIT CISR Four Stages has explicit distributional data (28/34/31/7 in 2022). The other three are prescriptive without distributional grounding. A future ingest that *validates* one of these frameworks against survey data would substantially strengthen this thread.

## How this thread should resolve

When a 5th or 6th comparable framework appears, this thread should resolve into a [[syntheses|synthesis]] page that:

1. Maps each framework to the layer it operates on (org / readiness / capability / task / diagnostic).
2. Provides a **decision tree** for which framework to use first depending on the user's question.
3. Identifies where they genuinely disagree vs. where they say the same thing in different vocabulary.
4. Notes where empirical validation is missing.

Until then, this thread stays open as a reminder to **always include the framework's layer when citing it** — "MIT CISR's Four Stages" carries different weight depending on whether it's used for capability assessment or org-design diagnosis.

## Related pages

- [[enterprise-ai-adoption]] — main concept page; the four frameworks all live here in summary form
- [[ai-maturity-measurement-comparison]] — sister thread on *measurement* (the data side); this thread is on *frameworks* (the prescriptive side)
- [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan article]] — Four Stages + Four S
- [[2026-04-28-anand-wu-genai-playbook|Anand-Wu HBR]] — 2×2 + leakage diagnostic
- [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] — 5 foundations + agent transition
- [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun HBR]] — Tin Man / Octopus
