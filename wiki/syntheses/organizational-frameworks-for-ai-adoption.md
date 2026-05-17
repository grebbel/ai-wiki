---
type: synthesis
aliases: ["organizational frameworks for AI adoption synthesis", "AI adoption frameworks synthesis"]
tags: [enterprise-ai-adoption, organizational-frameworks, synthesis, cross-source-comparison, decision-tree]
derived_from: [organizational-frameworks-for-ai-adoption]
opened: 2026-04-28
closed: 2026-05-05
last_refreshed: "2026-05-08"
confidence: 0.90
last_confirmed: "2026-05-08"
accessed_at: "2026-05-08"
source_count: 12
relationships:
  - type: instance-of
    target: enterprise-ai-adoption
    via: "synthesizes 6 frameworks describing different decision layers within enterprise AI adoption"
  - type: supports
    target: micro-productivity-trap
    via: "the layered framing makes the trap legible — most failures are layer mismatches"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Synthesis: Organizational frameworks for AI adoption

Closes [[threads/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]]. Originally filed 2026-05-05 with **6 frameworks** ([[2026-04-28-mit-sloan-ai-maturity|MIT CISR]], [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]], [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]], [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun]], [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI]], [[2026-05-03-rewired-second-edition-sample|McKinsey Rewired 2nd ed]]).

**Refreshed 2026-05-08**: four additional framework-vantages have been ingested in the intervening three days, expanding the cluster from 6 frameworks to **10 frameworks across 12 sources**:

- **Firm-boundary lens** ([[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar & Nohria 2026]]) — Build / Compose / Collaborate / Buy Outcomes.
- **Human-reaction lens** ([[2026-05-07-carucci-resistance-as-data|Carucci 2026]]) — resistance as data; orthogonal cross-cutting lens applied to *any* of the other framework decisions.
- **Organizational-learning lens** ([[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]] + [[2026-05-07-kiron-schrage-compound-benefits|Kiron & Schrage 2026]]) — Augmented Learners 2×2 + verification → evaluation → learning capture flywheel. **Now the largest representative-sample dataset in the cluster (N=3,467, 21+ industries, 136 countries; 8-year longitudinal panel).**
- **Runtime-engineering lens** ([[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]] + [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]) — [[agent-harness|agent harness]] anatomy (Context / Constraints / Contracts / Compounding); the engineering-stack counterpart to the organizational-learning flywheel.

The 6→10 expansion does **not** change the synthesis's core thesis (*frameworks operate on different layers; pick by the executive's question, not the framework's brand*). It strengthens the empirical foundation, sharpens several disagreements, and surfaces a new structural finding: **the "compounding cycle" is now visible as the same operational mechanism at two different stack layers** (organizational learning per Kiron-Schrage, runtime engineering per Chatterjee), each independently reached by different practitioner communities.

## Question

When advising an executive on enterprise AI adoption, which framework should inform which decision — and where do they genuinely disagree rather than say the same thing in different vocabulary?

## Findings

### The frameworks operate on different layers

The ten frameworks are **mostly complementary, not competing**. Each names a different layer of AI-adoption decision-making, with overlap rather than conflict. Stack them top-down (organizational → engineering), with one **orthogonal cross-cutting lens** that applies to any layer:

| Layer | Framework | Question it answers | Source |
| ----- | --------- | ------------------- | ------ |
| **Org-design** | Tin Man / Octopus | Is your organization structurally capable of adapting? | [[2026-04-28-werner-lebrun-octopus-organization\|Werner-Le-Brun]] |
| **Readiness** | Cisco 5 Foundations (Strategy / Infrastructure / Data / Governance / Culture) | Do you have the prerequisites? | [[2026-04-28-mittri-cisco-ai-enabled-enterprise\|MITTRI/Cisco]] |
| **Capability progression** | MIT CISR Four Stages + Four S | What stage are you at, and what blocks the next transition? | [[2026-04-28-mit-sloan-ai-maturity\|MIT CISR]] |
| **Organizational learning** *(new)* | Ransbotham/Kiron Augmented Learners 2×2 + verification → evaluation → learning capture flywheel | Does your org metabolize AI interactions into compounding knowledge, or consume them and forget? | [[2026-05-07-ransbotham-augmented-learners\|Ransbotham et al. 2024]], [[2026-05-07-kiron-schrage-compound-benefits\|Kiron & Schrage 2026]] |
| **Transformation playbook** | McKinsey *Rewired* 6 capabilities | How do you actually execute the journey? | [[2026-05-03-rewired-second-edition-sample\|Lamarre, Smaje, Levin et al. 2026]] |
| **Firm-boundary** *(new)* | Nishar-Nohria 4-model (Build / Compose / Collaborate / Buy Outcomes) | Which workflows should the firm own, and which should it rent / outsource / outcome-source? | [[2026-05-05-nishar-nohria-end-of-one-size-fits-all\|Nishar & Nohria 2026]] |
| **Trap escape** | Bain/OpenAI 4-step transformation | How do you avoid the [[micro-productivity-trap]]? | [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|Dutt, Chatterji et al. 2026]] |
| **Task deployment** | Anand-Wu 2×2 (cost of errors × type of knowledge) | For *this specific task*, deploy AI today and how? | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |
| **Runtime engineering** *(new)* | [[agent-harness\|Agent harness]] (Context / Constraints / Contracts / Compounding); 4-layer stack with swappable model layer | What runtime infrastructure must exist between your model and your user? | [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]], [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] |
| **Diagnostic** | Anand-Wu 6 leakage points | If gains aren't showing up in P&L, where are they leaking? | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |
| **⊥ Cross-cutting: human reaction** *(new)* | Carucci resistance-as-data: 3 leader traps (personalize / moralize / rush) + 4 signal categories (Loss / Anxiety / Lack of control / Flaws in change) | When pushback arrives at *any* layer above, what is it telling you about the change itself? | [[2026-05-07-carucci-resistance-as-data\|Carucci 2026]] |

**The orthogonal lens.** Carucci's human-reaction lens is *not* a stack layer. It is a diagnostic posture applied when *any* of the other 9 layers triggers organizational pushback. A reorganization (Werner-Le-Brun's Octopus transition) generates resistance; a maturity-stage transition (MIT CISR Stage 2 → 3) generates resistance; a firm-boundary shift (Nishar-Nohria Compose → Collaborate) generates resistance; a workflow redesign (Bain/OpenAI) generates resistance. Carucci's framework is what you reach for *while running any of the other nine*.

### A decision tree for which framework to use

Sequenced by the typical executive question (top-of-house → engineering-floor):

1. **"Are we organizationally capable of changing?"** → Werner-Le-Brun (Tin Man vs Octopus). If you're a Tin Man, lower frameworks won't stick.
2. **"Do we have the foundations?"** → Cisco 5 Foundations. Infrastructure, data, governance must clear a bar before pilots scale.
3. **"Where are we in the maturity curve?"** → MIT CISR Four Stages. Locate your stage; the Four S diagnostic identifies what blocks the next transition. *The financial inflection sits specifically at Stage 2 → Stage 3.*
4. **"How does our org metabolize AI interactions?"** → Ransbotham/Kiron Augmented Learners 2×2. Score yourself on org-learning capability and AI-specific-learning capability; the 15% Augmented-Learner cohort outperforms Limited Learners 1.6× on uncertainty management and 1.4× on revenue benefits. *Then* layer Kiron-Schrage's verification → evaluation → learning capture flywheel as the operational mechanism that turns the 15% advantage into compounding returns.
5. **"What's our transformation playbook?"** → McKinsey *Rewired* 6 capabilities (business-led roadmap, talent, operating model, technology, data, adoption-and-scaling). Anchor: ~20% EBITDA uplift, $3:$1 ROI, 1–2yr breakeven across deep-dive AI-leader companies.
6. **"Where does the boundary of our firm sit?"** → Nishar-Nohria 4-model (Build / Compose / Collaborate / Buy Outcomes). Decide *per workflow*, not at the firm level. The decision is no longer cost-driven — it is strategic about where differentiation lives. Empirical anchor: enterprise GenAI app spending $1.7B (2023) → $37B (2025); SaaS valuations 30–60% below 2021 peaks.
7. **"How do we avoid the common failure mode?"** → Bain/OpenAI 4-step (narrow possibilities; reimagine workflows; engage those closest to the process; measure outcomes plus evals). Names the trap (offering lock-in / process lock-in) explicitly. Anchor: 10–25% EBITDA gains.
8. **"Which task do we point AI at first?"** → Anand-Wu 2×2. *No regrets zone* (low cost of errors / explicit data) is where to start; agents thrive there today.
9. **"What runtime infrastructure must we build?"** → [[agent-harness|Agent harness]] (Chatterjee's Context / Constraints / Contracts / Compounding; Kokane's 4-layer stack with swappable model layer). Build constraints before cleverness. The model is rented and replaceable; the harness is owned and compounds. *Caveat (Kokane):* ~90% of the harness work is mature systems engineering applied to a new substrate — hire systems engineers, not AI specialists; the 10% genuinely novel is non-determinism at the execution layer + context as a degrading resource.
10. **"Why isn't our investment paying off in P&L?"** → Anand-Wu 6 leakage points. Diagnostic, not prescriptive. Trace which of the 6 points is leaking.

**Cross-cutting (apply at any layer above):**

- **"How do we read the pushback we're getting?"** → Carucci resistance-as-data. Avoid the three traps (personalize / moralize / rush to resolution). Diagnose the four signal categories (Loss / Anxiety / Lack of control / Flaws in change). Resistance is rarely noise; it is feedback on the change itself.

### Where they genuinely disagree

Most apparent disagreements are vocabulary differences, but a few real splits:

- **Stage 2 → Stage 3 financial inflection (MIT CISR-specific).** MIT CISR claims firms in Stages 1–2 underperform their industry; Stages 3–4 outperform. The other frameworks don't make this stage-gradient claim — they describe the *destination* of transformation but not where the inflection lives. **If true, the inflection is the most actionable framing.**
- **"Reinvent the business" vs. incremental capability building.** McKinsey *Rewired* and Bain/OpenAI both push *aggressive* posture: process redesign first, technology second; business-led, not IT-led; "we don't have a single success story where senior business leaders weren't in the driver's seat." MIT CISR is more incremental — the Four Stages permit gradual progression. The Bain/OpenAI thesis explicitly contradicts the incremental approach by naming the [[micro-productivity-trap]] (offering lock-in, process lock-in).
- **Org-design as upstream prerequisite (Werner-Le-Brun) vs. downstream outcome.** Tin Man / Octopus treats org structure as the precondition for AI adoption to work. The other frameworks largely assume the org can act, then prescribe what to do. If Werner-Le-Brun is right, the lower frameworks may not stick on a Tin Man without org-design work first.
- **Pilots as a stage (MIT CISR) vs. pilots as a trap (Bain/OpenAI).** MIT CISR Stage 2 ("Build pilots and capabilities") frames piloting as a needed phase. Bain/OpenAI argue most companies *get stuck* in pilots — exactly because they don't reimagine workflows. Same observation, opposite valence.
- **Firm-boundary as variable (Nishar-Nohria) vs. organizational property (Werner-Le-Brun).** Nishar-Nohria explicitly argue *"the boundary of the firm becomes a variable rather than a given"* — workflows can move fluidly between Build / Compose / Collaborate / Buy Outcomes as the cost curve of custom software collapses. Werner-Le-Brun frame organizational structure as a deeper property requiring multi-year transformation. Both can be true at different time-horizons: Nishar-Nohria's per-workflow boundary fluidity is a near-term commercial decision; Werner-Le-Brun's org adaptive capacity is the multi-year underlying variable that determines whether the firm can *act on* boundary fluidity.
- **"Process redesign is the value" (Bain/OpenAI, McKinsey) vs. "the harness is the moat" (Chatterjee).** Bain/OpenAI claim *"process redesign is the most challenging part of AI deployment and creates most of the value"* — i.e., organizational/workflow work dominates. Chatterjee claims *"the harness is the only part of our stack that gets more valuable with every customer we ship to"* — i.e., runtime engineering work dominates. **Resolution: they sit at different stack layers. Both are required**; Bain/OpenAI is right at the org-process layer; Chatterjee is right at the runtime layer. The synthesis-level claim is that *both* compounding cycles must be running — the organizational verify-evaluate-capture loop *and* the runtime telemetry → harness adjustment → workspace overrides loop.
- **Kokane's sceptical vantage on the entire cluster.** Kokane argues *~90% of "agent harness" engineering is mature systems engineering applied to a new substrate.* Generalised: this cuts against the breathless framings implicit in some consulting frameworks (everything-must-be-rebuilt-for-AI). The wiki holds Kokane's vantage as a useful epistemic discipline — when a framework claims AI is uniquely transformational, ask whether the underlying work is genuinely new or rebranded.
- **Augmented Learners (Ransbotham/Kiron) as upstream of MIT CISR Stage transition.** Ransbotham/Kiron's 5-question org-learning battery + 4-question AI-specific-learning battery measure capabilities that map onto **MIT CISR Stage 3 attributes** (test-and-learn, architected for reuse, human-feedback-loop AI). **A Stage-2 firm with strong organizational learning culture is on the Augmented-Learner trajectory; a Stage-2 firm without one will stall.** This sharpens MIT CISR's Stage 2 → 3 inflection by naming the *upstream variable* that determines whether the transition happens.

### Cross-framework agreement

All ten frameworks converge on a few claims, with different vocabularies. The post-refresh evidence is substantially stronger:

- **Adoption breadth ≠ transformation depth.** AI Index pegs maturity at 1%; MIT CISR pegs Stage 4 at 7%; Cisco pegs ready at 13%; **Ransbotham/Kiron peg Augmented Learners at 15%**; Werner-Le-Brun's 12% transformation-success baseline. **Same diagnostic, five numbers — all clustering 7–15%.** When five independent measurement instruments arrive at a similar upper-tail size, the cohort is structurally narrow, not measurement-artefactual. See [[ai-maturity-measurement-comparison]].
- **Process redesign is the main cost, not technology.** Bain/OpenAI: "process redesign is the most challenging part of AI deployment and creates most of the value." McKinsey *Rewired*: "business-led roadmap" and "operating model" are 2 of the 6 capabilities. MIT CISR Four S "Synchronization" is reskilling and role redesign. Anand-Wu 2×2's strategic value comes from picking the *right tasks*, not the technology. **Now corroborated by 7 sources** (the original 6 frameworks plus Nishar-Nohria explicitly: *"data architecture, governance, and ownership as integral to the transformation rather than afterthoughts"*) — among the strongest cross-source agreements in the wiki.
- **The "compounding cycle" is the same operational mechanism at two stack layers.** Two practitioner essays from independent vantages (Kiron-Schrage at the organizational-learning level; Chatterjee at the runtime-engineering level) describe operationally identical machinery:

  | Kiron-Schrage step (organizational) | Chatterjee equivalent (runtime) |
  |---|---|
  | Verification — does this output meet the standard? | Constraints layer — pre/post-tool hooks score outputs |
  | Evaluation — what does this output reveal? | Contracts layer — formal evaluable specifications |
  | Learning capture — how do we ensure this insight persists? | Compounding layer — telemetry → harness adjustments → workspace overrides |

  This is the strongest *concept-level* convergence in the cluster — same mechanism, two layers, two practitioner communities, independently reached. The synthesis-level implication: **AI products that compound require both cycles running** (organizational + runtime); a firm with one but not the other is partially stuck.
- **Senior-leader ownership is non-negotiable.** McKinsey: "We don't have a single success story where senior business leaders were not in the driver's seat." Bain/OpenAI: "boardroom imperative." MIT CISR: united front of CEO / CIO / CSO / Head of HR. Cisco: "Strategy" pillar means top-down. Werner-Le-Brun: org-design ownership at C-level. **Refined by Carucci 2026**: senior leadership is necessary but not sufficient — leaders' three traps (personalize / moralize / rush to resolution) systematically *suppress* the operator-level signal that would otherwise correct course. *Senior-leader ownership* + *resistance-as-data discipline* together are what works.
- **Talent density shifts over hiring breadth.** McKinsey *Rewired*'s 70% benchmarks (70%+ in-house, 70%+ "doer" engineers, 70%+ at competent-or-expert skill levels) — distinctive but consistent in spirit with MIT CISR's "Synchronization" and Cisco's "Culture and Talent." **Sharpened by Chatterjee 2026** at the engineering layer: *"the most under-resourced role on most AI teams is the engineer who specializes in [harness work]... someone who thinks about agents the way SREs think about distributed systems."* The under-hire problem is specific, not general.
- **Most enterprise tasks today are augmentative, not automative.** Anand-Wu's "no regrets zone" (where agents thrive) is the *minority* of business tasks. MITTRI/Cisco's chatbot → agent → multi-agent progression places multi-agent as future-state. The empirical record ([[2026-04-30-ai-index-report-2026|AI Index 2026]]) confirms: agent deployment in single digits across nearly all business functions. **Worker-attitude data corroborates** ([[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]]): 84% hopeful that AI will assist with their tasks (vs. 70% in 2017); only 20% fearful (vs. 31% in 2017). The displacement panic that surged with ChatGPT has not been borne out at the worker-attitude level — at least within the 3,467-respondent MIT SMR × BCG sample.
- **Models commoditize; what's owned compounds.** Chatterjee 2026 makes this explicit at the engineering layer (*"the model is rented from a vendor whose competitor will outperform them within the year"*). Nishar-Nohria 2026 makes it explicit at the firm-boundary layer (the **Build** model produces hard-to-replicate institutional knowledge over time as it encodes the firm's data and decision logic). Kiron-Schrage 2026 makes it explicit at the organizational level (compounding economics = asset appreciation; consumption economics = asset depreciation). **Three independent vantages, same conclusion**: durable advantage in AI comes from what the firm *owns and accumulates*, not from which model it rents.

### Where empirical validation sits — and where it is still missing

Of the ten frameworks:

| Framework | Empirical anchor | Sample / instrument |
| --------- | ---------------- | ------------------- |
| MIT CISR Four Stages | 28%/34%/31%/7% distribution; financial inflection at Stage 2 → 3 | **2022 Future Ready Survey, N=721** — pre-GenAI baseline, now 4 years old |
| Ransbotham/Kiron Augmented Learners | 15% / 14% / 12% / 59% 2×2 distribution; 1.6× / 2.2× / 1.8× / 1.6× uncertainty-management multipliers; 99% revenue-benefit saturation in Augmented Learner cohort | **Spring 2024 MIT SMR × BCG global survey, N=3,467, 21+ industries, 136 countries; 8th annual wave of comparable methodology** — *the largest representative-sample dataset in the cluster* |
| Anand-Wu 2×2 | Conceptual framework; cited prior tech cycles (e-ticketing, CAD/ERP, Big Law) | No per-quadrant empirical baseline |
| Cisco 5 Foundations | 13% AI-ready / 98% urgency / 85% give themselves <18 months | Cisco's own 2025 readiness survey; vendor-instrument data, methodology not fully disclosed |
| Werner-Le-Brun Octopus | 12% transformation-success baseline | Case examples (Netflix, Google, Coca-Cola, U.S. Army); no distributional data; AWS-affiliated authorship |
| McKinsey *Rewired* | ~20% EBITDA uplift; $3:$1 ROI; 1–2yr breakeven; 70% talent-density shifts | ~20 deep-dive AI-leader companies (selected from ~200 study set); **vendor-of-deployment data — selection-effect-aware** |
| Nishar-Nohria 4-model | Enterprise GenAI app spending $1.7B (2023) → $37B (2025) ≈ 22×; SaaS valuations 30–60% below 2021 peaks; >1/3 of companies replaced ≥1 SaaS tool with custom GenAI | **Industry analyst data + Adobe outcome-based pricing as named industry signal** — third-party aggregate, not framework-specific survey |
| Bain/OpenAI 4-step | 10–25% EBITDA gains; Lowe's Mylow 2× online conversion; FabricationCo $30M profit | Bain client work; **vendor-of-deployment data — selection-effect-aware** |
| Agent harness (Chatterjee + Kokane) | Friday-in-March anecdote (n=1); architectural-pattern alignment with Anthropic Managed Agents | Practitioner essays; **no empirical anchor for harness-tuning compounding rates** |
| Carucci resistance-as-data | None named in the source | Practitioner essay; **no empirical anchor at all** — drawn from 30 years of consulting practice |

**The empirical landscape has shifted substantially since the original synthesis closed.** Three observations worth flagging:

1. **MIT CISR is no longer alone with N>500 representative-sample data.** Ransbotham/Kiron's 3,467-respondent cross-industry global survey is now the largest dataset in the cluster, and it is **post-GenAI** (spring 2024) where MIT CISR is **pre-GenAI** (2022). The MIT CISR vs. Ransbotham/Kiron methodology cross-walk is now a higher-priority open question than it was in May.
2. **The 10–25% EBITDA range from consulting frameworks (McKinsey *Rewired*, Bain/OpenAI) plus the 22× enterprise GenAI app spending growth (Nishar-Nohria) cluster on roughly the same magnitude of value claim** — different metrics, similar order of magnitude. Independent corroboration from non-vendor sources would still be valuable but the cluster is no longer a single sponsored data point.
3. **The new sources tilt the cluster toward the prescriptive side, not the distributional side.** Carucci, Chatterjee, Kokane, Kiron-Schrage all add prescriptive frameworks (resistance discipline, harness anatomy, "compounding cycle"); only Ransbotham/Kiron and Nishar-Nohria add empirical anchors. The wiki now has *more frameworks* than it did at original close, but the *empirical-vs-prescriptive ratio* has not improved proportionally.

## Sources consulted

**Original 6 (filed 2026-05-05):**

- [[2026-04-28-mit-sloan-ai-maturity]] — Burnham (2025) reporting on Woerner, Weill, Sebastian, Káganer at [[MIT CISR]]. Four Stages + Four S; representative-sample distribution.
- [[2026-04-28-anand-wu-genai-playbook]] — Anand & Wu (HBR Nov–Dec 2025). 2×2 task framework + 6 leakage points; paradox-of-access argument.
- [[2026-04-28-mittri-cisco-ai-enabled-enterprise]] — MIT Tech Review Insights × [[Cisco]] (2025). 5 Foundations + chatbot → agent → multi-agent progression.
- [[2026-04-28-werner-lebrun-octopus-organization]] — Werner & Le-Brun (HBR Nov–Dec 2025). Tin Man / Octopus archetypes; AWS Executives in Residence.
- [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] — [[Bain & Company]] + [[OpenAI]] Economic Research (HBR.org, 30 Apr 2026). 4-step transformation framework; names the [[micro-productivity-trap]].
- [[2026-05-03-rewired-second-edition-sample]] — Lamarre, Smaje, Levin et al. (Wiley/[[McKinsey & Company]] 2026, sample-only). 6-capability framework; 70% talent-density shifts; 20% EBITDA uplift.

**Added in 2026-05-08 refresh:**

- [[2026-05-05-nishar-nohria-end-of-one-size-fits-all]] — [[Deep Nishar]] & [[Nitin Nohria]] (HBR.org Digital, Apr 2026). **Firm-boundary lens**: Build / Compose / Collaborate / Buy Outcomes. Enterprise GenAI app spending 22× in 2 years; SaaS valuations 30–60% below 2021 peaks; Adobe outcome-based pricing as named industry signal.
- [[2026-05-07-carucci-resistance-as-data]] — [[Ron Carucci]] (HBR.org Digital, Apr 2026). **Human-reaction (cross-cutting) lens**: 3 leader traps (personalize / moralize / rush to resolution) + 4 signal categories (Loss / Anxiety / Lack of control / Flaws in change). Practitioner essay; no empirical anchor.
- [[2026-05-07-ransbotham-augmented-learners]] — Ransbotham, [[David Kiron]], Khodabandeh, Chu, Zhukov (MIT SMR × BCG Big Ideas Research Report, 8th annual, Nov 2024). **Organizational-learning lens (empirical foundation)**: Augmented Learners 2×2 distribution; 1.6× uncertainty management; 1.4× revenue benefits. Largest representative-sample dataset in the cluster (N=3,467).
- [[2026-05-07-kiron-schrage-compound-benefits]] — [[David Kiron]] & Schrage (MIT SMR Column, Apr 2026). **Organizational-learning lens (operational mechanism)**: verification → evaluation → learning capture flywheel; reframes ROI as "return on iteration"; consumption (asset depreciation) vs. compounding (asset appreciation) economics.
- [[2026-05-07-kokane-agent-harness-vs-systems-design]] — Kokane (Level Up Coding / Medium, Apr 2026). **Runtime-engineering lens (sceptical vantage)**: ~90% of agent-harness work is mature systems engineering rebranded; 10% genuinely novel (non-determinism + context-as-degrading-resource).
- [[2026-05-07-chatterjee-anatomy-of-agent-harness]] — Chatterjee (Medium, May 2026). **Runtime-engineering lens (taxonomical vantage)**: Context / Constraints / Contracts / Compounding. Friday-in-March worked failure example; "the model is what you rent. The harness is what you own."

## Lessons

- **Pick a framework by the executive's question, not the framework's brand.** Each framework names a different layer; mismatched layers explain most "why didn't this work" stories. The decision tree above (now 10 questions plus 1 cross-cutting) is the operational artifact.
- **The transformation-mindset frameworks (McKinsey *Rewired*, Bain/OpenAI) and the maturity-progression framework (MIT CISR) sit in tension on pilot stages.** *Rewired* and Bain treat pilots-as-trap; MIT CISR treats pilots-as-stage. Reconcile by treating MIT CISR's Stage 2 as a phase to pass through quickly, not dwell in.
- **Process redesign is the load-bearing decision across all 10 frameworks.** If your AI program treats redesign as something the technology team handles, it will land on the wrong side of the [[micro-productivity-trap]] regardless of which framework you cite. Now corroborated by 7 sources.
- **Organizational learning capability is the upstream variable for MIT CISR Stage 2 → 3 transition.** Ransbotham/Kiron's Augmented Learner traits (test-and-learn, failure tolerance, postmortem culture, learning codification, AI-specific learning) map directly onto Stage 3 attributes. *A Stage-2 firm with weak organizational learning culture will stall at Stage 2.* This sharpens the most actionable claim in the original synthesis (the Stage 2 → 3 inflection) by naming what determines whether the transition happens.
- **The "compounding cycle" is the same operational mechanism at two stack layers.** Kiron-Schrage at the organizational level (verification → evaluation → learning capture) and Chatterjee at the runtime level (Context / Constraints / Contracts / Compounding) describe operationally identical machinery. *AI products that compound require both cycles running.* A firm with strong organizational learning but weak harness-runtime engineering will struggle to ship; a firm with strong harness engineering but weak organizational learning will ship products that don't get better with use.
- **The human-reaction lens is cross-cutting, not stack-layered.** When applying any of the other 9 frameworks, watch for Carucci's four resistance signals (Loss / Anxiety / Lack of control / Flaws in change). The fourth — *Flaws in change* — is *operator-level signal that the framework's prescription is wrong for this particular firm.* Leaders' three traps (personalize / moralize / rush) systematically suppress it. Resistance discipline is what keeps the other 9 frameworks honest.
- **Models commoditize; what's owned compounds.** Three independent vantages reach this conclusion: Chatterjee at the engineering layer ("the model is what you rent. The harness is what you own."); Nishar-Nohria at the firm-boundary layer (Build encodes hard-to-replicate institutional knowledge over time); Kiron-Schrage at the organizational level (compounding economics = asset appreciation). The competitive-advantage question shifts from *which model do we choose?* to *what do we own and accumulate?*
- **Empirical maturity distributions older than 2024 are increasingly stale, but the cluster is no longer single-anchor.** The MIT CISR 2022 baseline (N=721) is now joined by the Ransbotham/Kiron 2024 baseline (N=3,467, post-GenAI) — the larger and more recent dataset. Cross-walking the two is now feasible; whether they agree is an open question worth investigating.

## Open questions

**Resolved (or partially resolved) by the 2026-05-08 refresh:**

- ~~"No empirical validation against a representative sample beyond MIT CISR."~~ — **partially resolved**: Ransbotham/Kiron's 3,467-respondent cross-industry global survey now sits alongside MIT CISR as a second large-N anchor. Still BCG-sponsored research, so the vendor-of-deployment caveat applies; but the methodology is longitudinal (8th annual wave) and representative.
- ~~"MIT CISR Stage distribution post-GenAI."~~ — **still open as a methodology question**, but Ransbotham/Kiron's post-GenAI 2×2 distribution (15% / 14% / 12% / 59%) gives an indirect signal: the upper-tail cohort size (15% Augmented Learners in 2024) is consistent with MIT CISR's 7% Stage 4 (2022) plus some upward drift, broadly compatible with the original framework if interpreted generously. A direct MIT CISR 2025/2026 wave would still be highly valuable.

**Still open:**

- **Cross-walk between MIT CISR Stages and Ransbotham/Kiron Augmented Learners 2×2.** The hypothesis (above, in the new disagreements section) is that **organizational learning capability is the upstream variable for the Stage 2 → 3 transition.** A worked-example test on a panel of firms tracked through both instruments would settle this.
- **How does the firm-boundary decision (Nishar-Nohria) interact with maturity stage (MIT CISR)?** Is "Buy Outcomes" only viable from Stage 3+, or can a Stage 1–2 firm leapfrog by outsourcing the function entirely? This is the wiki's strongest *practitioner-relevant* unresolved question.
- **Quantitative measurement of the compounding cycle.** Kiron-Schrage describe it qualitatively; Chatterjee's Compounding layer describes it qualitatively. Nobody has measured *the slope* of compounding — how much contract-score uplift per unit of telemetry-driven harness adjustment, or how much Augmented-Learner advantage growth per quarter. Without measurement, the "compounding cycle" is a plausible-sounding reframing rather than a quantified claim.
- **Whether the 10 frameworks converge on the same recommendation when applied to a specific firm.** The decision-tree above is still a hypothesis. A worked example — pick a real firm, run all 10 frameworks against it, compare the prescriptions — would test the "complementary not competing" claim. With 10 frameworks now, this is a substantial undertaking, but the test would be definitive.
- **Cross-walk with academic strategy theory.** Carucci's resistance-as-data lens has obvious resonance with change-management academic literature (Kotter, Lewin); none of the wiki's existing concept pages directly bridge to it. A follow-up synthesis could integrate the cluster with [[dynamic-capabilities]] (Teece), [[systems-thinking]], [[strategic-foresight]], and change-management theory.
- **The Kokane-Chatterjee tension (rebranded systems engineering vs. moat) in actual hiring data.** Kokane prescribes hiring systems engineers; Chatterjee prescribes hiring SRE-like AI specialists. Both are plausible; nobody has compared the build-quality outcomes of teams hired on each model. A 2026–27 source measuring this would settle the most concrete operational disagreement in the cluster.

## Related pages

- [[enterprise-ai-adoption]] — main concept page; the 10 frameworks all live here in summary form
- [[agent-harness]] — concept page for the runtime-engineering lens added in this refresh
- [[micro-productivity-trap]] — named failure mode that several frameworks target; **now confidence 0.90, the most strongly corroborated concept in the wiki** (7-source agreement across 5 vantages)
- [[ai-maturity-measurement-comparison]] — sister thread (still open) on the *measurement* side; the 1% / 7% / 12% / 13% / 15% maturity spread (Ransbotham/Kiron's 15% Augmented Learners is now the 5th measurement)
- [[automation-vs-augmentation]] — load-bearing distinction inside Anand-Wu's 2×2 quadrants
- [[dynamic-capabilities]] — academic-strategy bridge that none of the 10 frameworks engage with directly
