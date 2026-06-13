---
type: concept
aliases: ["automation vs augmentation", "automation-vs-augmentation", "automate vs augment", "AI substitution vs complementarity", "AI labor substitution", "AI labor complementarity"]
tags: [automation, augmentation, generative-ai, ai-deployment, ai-task-design, capability-reliability-gap]
confidence: 0.95
last_confirmed: "2026-06-13"
accessed_at: "2026-06-13"
source_count: 40
relationships:
  - type: supports
    target: ai-employment-effects
    via: "Brynjolfsson Canaries Fact 3 — automation displaces entry-level employment, augmentation does not"
  - type: supports
    target: enterprise-ai-adoption
    via: "per-task deployment lens used by Anand-Wu, MITTRI/Cisco, MIT CISR"
  - type: supports
    target: ai-benchmarks
    via: "Narayanan's release-decision frame — reliability threshold required for automation deployment exceeds that for augmentation deployment; reliability is the gating dimension benchmarks have under-measured"
quality_score: 0.73
quality_notes: ['missing ## Debates and supersession (concept with >1 source)', '1 near-empty section(s)', '3 broken body wikilink(s)']
---

# Automation vs. Augmentation

A conceptual distinction that recurs across the wiki's sources with growing empirical weight: **does this AI deployment substitute for human labor (automation), or complement it (augmentation)?** The choice has consequences in three layers — strategy (where to deploy), task design (how to integrate), and labor markets (who keeps their job).

This page treats **automation vs. augmentation** as a standalone analytical lens, distinct from [[ai-agents]] (the technology), [[ai-employment-effects]] (the labor consequences), and [[enterprise-ai-adoption]] (the organizational decision-making).

## Working definition

The cleanest definition in the wiki comes from the [[Anthropic Economic Index]] used in [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025]]:

- **Automative use** — Claude conversations classified as "Directive" (complete task delegation with minimal interaction) or "Feedback Loop" (task completion guided by environmental feedback such as repeatedly relaying coding errors to the model). The AI is doing the work; the human is monitoring or absent.
- **Augmentative use** — conversations classified as "Task Iteration" (collaborative refinement), "Learning" (knowledge acquisition and understanding), or "Validation" (work verification and improvement). The human is doing the work, with AI as a tool/partner.
- "None" — neither substituting nor complementing, e.g., chitchat or exploration.

Note that these are **task-level** distinctions, not occupation-level. The same occupation can have both automative and augmentative AI uses; the empirical question is which dominates.

## Why this distinction matters

### 1. Strategic deployment ([[2026-04-28-anand-wu-genai-playbook|Anand-Wu]])

The Anand-Wu 2×2 — cost of errors × type of knowledge — implicitly maps to automation vs. augmentation:

| Quadrant | Automation/augmentation orientation |
|---|---|
| **No regrets zone** (low cost / explicit) | Pure **automation** — AI does it all, no human in the loop. Bulk customer inquiries, document summarization, résumé screening. |
| **Creative catalyst zone** (low cost / tacit) | **Augmentation** — AI creates options, human selects. Marketing taglines, design variations. |
| **Quality control zone** (high cost / explicit) | **Augmentation with strict verification** — AI produces, human verifies. Contract drafting (Harvey), code generation (Copilot), due diligence. |
| **Human-first zone** (high cost / tacit) | **Light augmentation** — Human leads, AI assists with minor tasks. Strategy, hiring, disciplinary decisions. |

Anand-Wu's strategic recommendation: deploy aggressively in the no-regrets zone (automation), use AI as a creative or quality-control partner elsewhere (augmentation), keep humans firmly in the lead in the human-first zone.

### 2. Task design ([[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]])

[[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] frames the distinction as a question of **agency and oversight**: *"It's not about replacing roles. It's about where we can give agency, with some human oversight and governance, to improve tasks within a workflow."* — [[Liz Centoni]], Cisco.

The chatbot → agent → multi-agent progression is a progression along the automation axis: more agency to AI, less direct human intervention.

#### The Ask → Assist → Automate ladder ([[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler|Beutler / OpenAI 2026]])

[[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler|Beutler (2026)]] gives the cleanest *deployment-maturity* version of this axis — a three-rung ladder OpenAI's solutions team uses with customers to deploy agentic systems responsibly:

| Rung | What the agent does | Automation/augmentation orientation |
|---|---|---|
| **Ask** | Read-only — reaches into data, pulls information, answers questions. Validate sources before any write action. | **Augmentation** — the human does the work; the agent is a retrieval/answer tool. |
| **Assist** | Recommends the action it thinks it should take; a human-in-the-loop validates (approve / reject) before execution. | **Augmentation with human verification** — surfaces where the agent falls short before it acts alone. |
| **Automate** | The things the agent reliably gets right stop going to humans; exceptions route to people. | **Automation** — agent acts; human handles the long tail. |

Three claims travel with the ladder. **(1) You can't go zero-to-Automate**, "especially in regulated environments where you have all those compliance things to worry about" — you build the eval-and-governance foundation at Ask first. **(2) The biggest value is at Automate, but so is the cost**: "the most integration, the highest quality bar, the strongest evaluations, and the most operational ownership." **(3) A natural flywheel**: start by building tools that *help people do their job* (Ask); once they see value they give feedback; you "hill-climb" toward Automate, and value grows "exponentially as you unlock each new level." The **T-Mobile** case is the responsible-scaling anchor — a $3B call-center cost center, already 60% automated, with a 75% ambition, that OpenAI walked back to start at Ask.

The ladder is a sharper operational restatement of the Anthropic-Economic-Index Directive/Feedback-Loop (automative) vs Task-Iteration/Validation (augmentative) split in the working definition above: Ask ≈ Validation/Learning, Assist ≈ Task-Iteration with a verification gate, Automate ≈ Directive. It complements the [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS]] USE/COMPOSE/BUILD frame (which answers the *economic-decision* question — build vs rent the model) by answering the orthogonal *how-much-agency-now* question on a single workflow. See [[enterprise-ai-adoption]] for the org-design context (embedded engineering, business owns the outcomes) in which Beutler situates the ladder.

### 3. Labor market consequences ([[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025]])

The strongest empirical signal in the wiki for why this distinction matters: **employment outcomes diverge sharply by automation vs. augmentation use.**

- Occupations with highest **automation share**: declining employment for early-career workers (22–25).
- Occupations with highest **augmentation share**: **NO** similar pattern — most-augmentative quintile shows fastest growth.

> "Consistent with automative uses of AI substituting for labor while augmentative uses do not." — [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025]] Fact 3.

This finding is the wiki's first **measurable empirical correlate** of a distinction that has otherwise lived as a strategic or philosophical framing.

### 4. Maturity progression ([[2026-04-28-mit-sloan-ai-maturity|MIT CISR]])

[[2026-04-28-mit-sloan-ai-maturity|MIT CISR]]'s Stage 4 ("AI future-ready") is described as "combining traditional, generative, agentic, and robotic AI" — which implies firms at that stage are deploying AI across the full automation/augmentation spectrum. Lower stages tend to lean augmentative (LLMs as tools); higher stages move toward more automation (agents, autonomous workflows).

### 5. Productivity gains under augmentation ([[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|primary source]])

The wiki's primary anchor for **augmentation's positive productivity effects** is [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (2025) "Generative AI at Work" QJE]]. The paper studies a customer-support AI that was **explicitly designed to augment**, not replace:

- AI shows real-time suggestions only to the agent
- Agents have **full discretion** to accept, edit, or ignore
- The system **declines to suggest** when training data is insufficient — leaving agents to respond on their own
- Authors describe this as "designed to augment (rather than replace) human agents"

Headline result: **+15% productivity** with strong equalizing effect (low-skill +30%, high-skill ~0% with small quality decline). This is the wiki's cleanest empirical demonstration that **augmentation under deliberate human-in-the-loop design produces positive labor outcomes**. The [[2026-04-28-ai-index-report-2025|AI Index 2025]]-cited productivity studies (Dell'Acqua 2023 consulting, Cui 2024 software, Hoffman 2024 software) replicate the pattern across other domains.

We do **not** have equivalent rigorous studies of *pure-automation* productivity gains in the wiki — because pure automation replaces the worker entirely, so "productivity per worker" is no longer a coherent measurement. The closest empirical signal we have for automation effects is occupation-level employment data ([[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson 2025 Canaries]]) showing entry-level employment declines in automate-able roles.

### 6. Longitudinal split on Claude.ai ([[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index, 4th report]] → [[2026-05-07-anthropic-economic-index-5-learning-curves|5th report]])

The [[Anthropic Economic Index]] tracks the augmentation/automation split on Claude.ai across reports. The current trajectory, now extended through February 2026:

| Sample period | Augmentation | Automation |
|---|---|---|
| January 2025 | 55% | 41% |
| March 2025 | 55% | 42% |
| August 2025 | 47% | 49% |
| November 2025 | 52% | 45% |
| **February 2026** | **53%** | **45%** |

Augmentation has led in four of five samples; the August 2025 sample remains the only one where automation led. Across the most recent quarter (Nov 2025 → Feb 2026), the split has been **stable, not drifting toward automation** — a noteworthy finding given headline narratives that agentic deployment is rapidly displacing collaborative use.

**Emergent automation patterns on the 1P API** (5th report, Feb 2026): three task clusters where automation share climbed sharply on the enterprise API endpoint between Aug 2025 and Feb 2026 — *first-line sales* (rising directive use of Claude in outbound sales workflows), *programmatic trading and brokerage* (automated financial-decision pipelines), and *coding agent harnesses* (Claude Code splitting work into many short directive calls). These are the three places where API automation is genuinely accelerating, even as the Claude.ai consumer split holds roughly flat. The divergence between consumer (mostly stable, augmentation-leaning) and API (automation rising in specific clusters) is a load-bearing methodological caveat: aggregate "AI is automating work" framings should specify which surface and which cluster.

### 7. Differentiated vs. independent search as fine-grained augmentation patterns ([[2026-04-29-boussioux-crowdless-future|Boussioux et al. 2024]])

A field study with [[Continuum Laboratory]] and Freelancer.com on circular-economy ideation distinguishes two human-AI search modes:

- **Independent search** — one initial prompt → multiple GPT-4 instances generate solutions independently; approximates parallel-path crowdsourcing.
- **Differentiated search** — one initial prompt + iterative *differentiation instructions* after each output ("tackle a different problem"); converts the LLM's tendency-toward-the-mean into a controllable parameter.

Empirical pattern in the study (300 evaluators, 3,900 evaluator-solution pairs):

| Dimension | Human Crowd | HAI multi-instance | HAI single-instance (differentiated) |
|---|---|---|---|
| Novelty | **Highest** | Lowest | Comparable to HC |
| Strategic viability | Lower | Comparable | **Highest** |
| Environmental value | Lowest | Higher | **Highest** |
| Financial value | Lowest | Higher | **Highest** |
| Overall quality | Lowest | Comparable to HC | **Highest** |

The differentiated/single-instance configuration is the more interesting augmentation pattern — it preserves novelty while delivering value/quality gains over both HC and the multi-instance HAI baseline.

### 8. The Pareto-improvement caveat ([[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond 2025]])

A subtle finding worth flagging: augmentation under the customer-support AI is **not strictly Pareto-improving**. Top performers experience small speed gains AND **small quality declines**. The mechanism: top performers increase adherence to AI recommendations even when those recommendations are slightly worse than what they would have produced unaided.

Two implications:
- **Distributional**: augmentation reliably benefits low-skill workers but may marginally harm top performers' output quality.
- **Long-run training-data risk**: if top performers reduce their original contributions, the AI's training data degrades over time. The AI's effectiveness on novel problems depends on continued original problem-solving from skilled workers.

This is a genuine wrinkle in the "augmentation is benign / automation is contested" framing — even augmentation has distributional and long-run dynamics that the headline numbers obscure.

### 9. Buy-Outcomes as the most automative deployment model ([[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar & Nohria 2026]])

Nishar & Nohria's four-model framework (Build / Compose / Collaborate / **Buy Outcomes**) for the firm-boundary decision under [[generative-ai]] surfaces a useful refinement of the automation-vs-augmentation cut: **Buy Outcomes is the most automative model in the spectrum.**

When a firm contracts for "accurate financials, compliance, and reporting as a service" rather than licensing accounting software and operating it internally, the entire job — not just discrete tasks — is automated by the vendor. The named industry signal: **Adobe's outcome-based pricing for its CX Enterprise + agentic AI tools**, where Adobe deploys agents directly with the customer and charges per outcome (e.g., successful ad campaigns) rather than per seat or per token. This is the operational shape of "AI does the work; the human is monitoring or absent" pushed to the firm-boundary level.

By contrast, the **Build** model is closer to deep augmentation of a firm's distinctive workflows — the system encodes *the firm's* data and decision logic, not the vendor's. The four models can therefore be ordered roughly along the automation-vs-augmentation axis:

| Nishar-Nohria model | Closest to | Why |
|---|---|---|
| Buy Outcomes | Pure automation (firm-level) | Vendor takes responsibility for the whole job |
| Collaborate | Mostly automation | Provider's forward-deployed engineers build the system; firm consumes it |
| Compose | Augmentation of business-user workflows | Business users configure scaffolding to their own motion |
| Build | Deep augmentation of distinctive workflows | The firm's own data and decision logic become the system |

This refines the wiki's task-level cut into a complementary firm-boundary cut: **at the task level, Anand-Wu's "no regrets zone" is where automation thrives; at the firm-boundary level, Nishar-Nohria's "Buy Outcomes" is where firms cede the whole function**. Both work best on **non-differentiating** territory; both become risky when performance there starts shaping competitive advantage.

Caveat: Nishar-Nohria explicitly warn that the choice of model is **not primarily a cost or feasibility decision** anymore — it is a strategic decision about where differentiation matters. This is the firm-boundary analogue of Anand-Wu's task-level "where to deploy GenAI today" question.

### 10. Reliability is the gating dimension for the automation/augmentation cut ([[2026-03-20-huggingface-agentic-evaluations-workshop|Narayanan / Princeton, HF Agentic Evals Workshop 2026]])

[[Arvind Narayanan|Narayanan]]'s release-decision frame **operationalises** the automation-vs-augmentation cut at the deployment-readiness layer:

> *"In a coding agent, many of these errors are maybe not too bad because the programmer is still in the loop and they're reviewing the code. But in a customer service agent, you want the agent to autonomously handle customers. These are much worse errors. Reliability really matters in automation tasks as opposed to augmentation tasks."*

The structural claim:

- **Augmentation deployments** can tolerate substantial unreliability because a human is in the loop validating each step — the coding agent at 70% reliability is still net-positive because the programmer reviews and corrects the 30%.
- **Automation deployments** require a high reliability threshold by construction — the autonomous customer-service agent at 90% reliability is dead-on-arrival because the 10% failures interact with the world (wrong order placed, wrong information given, customer trust burned) before any human can intervene.

The release-decision corollary: *"For release decisions, it's not just capability that matters. It's also some reliability threshold that needs to be met before you decide to deploy an agent."* Capability and reliability are orthogonal — Narayanan's team decomposes reliability into 12 sub-dimensions, most of which are unsolved (see [[ai-benchmarks]]). This means the automation-vs-augmentation cut is not just about *whether the AI does the work* but about *whether the AI is reliable enough to do the work autonomously* — a much higher bar than capability benchmarks currently measure.

This complements [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson's Fact 3]] (automation displaces, augmentation doesn't) with the **upstream gating mechanism**: a deployment that *could* be automation often *should* be augmentation today because reliability hasn't crossed threshold yet, and the augmentation-to-automation transition will follow reliability improvements per task class — not raw capability improvements.

### 11. The normative quality-over-quantity reframe ([[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni 2026]])

The wiki's first explicitly **prescriptive** voice on the augmentation pole. Where the prior ten contributions are descriptive (what's happening) or strategic (where to deploy), [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni]] supplies the **definitional reframe of efficiency itself**: in the AI era, the productivity contribution of humans is no longer proportional to the *quantity* of their output (AI handles that) but to the *quality* of their output — the ideas, the judgment, the second- and third-order thinking AI does not (yet) reliably produce.

> "Our idea of efficiency really stems from the era of assembly line work, where the more products you assembled on an assembly line, the better your output was. ... But right now, we are going through a period of tremendous change in AI and in technology, and the productivity of a company is no longer proportional to the quantity of output of its human workers, because the realm of quantity is being taken over by AI and technology. Humans now influence the productivity of their organization by the quality of their output." — [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni]]

Storoni's contribution is **the neuroscience mechanism for the augmentation pole**:

- **Quality cognitive work requires gear-2** — the Goldilocks state on the norepinephrine inverted-U curve (sustained focus, alertness, nuance-detection, prefrontal-cortex engagement). Storoni's *gear 2* maps to the work that *cannot be substituted by AI* — judgment, second/third-order reasoning, learning under uncertainty.
- **Modern work design pushes workers into gear-3** (high-norepinephrine reactive state — Slack pressure, deadline panic, constant context-switching), where the prefrontal cortex disengages and humans produce *fast, low-quality, nuance-blind* output. *This is exactly the work AI does better.* So workers trapped in gear-3 are producing the kind of output that *gets automated next* — they have placed themselves on the automation side of the cut by their work pattern, not by their job category.
- **The augmentation prescription is therefore not a deployment choice, it is a work-design choice**: protect the windows that enable gear-2 (chronobiology-aware schedules, protected focus blocks, walking breaks, intrinsic-motivation structures), and let AI take the gear-3-reactive work that should never have been a human job in the first place.

Storoni's framing closes a gap in the concept's prior corpus: the augmentation-pole sources have shown *that* augmentation works (Brynjolfsson-Li-Raymond, Forsgren & Macvean, Anthropic Economic Index) and *where* to deploy it (Anand-Wu, MITTRI/Cisco) but not *what kind of cognitive work the human side of the augmentation pair has to be doing* for the pairing to actually produce value. Storoni's answer: **gear-2 quality work, in time-of-day-aware schedules, with intrinsic-motivation structures protecting the underlying cognitive states.**

Per the [[../../CLAUDE.md#lifecycle|Lifecycle confidence rules]] this single-source prescriptive-popularisation contribution does *not* lift the concept's confidence above the existing 0.95 cap; it expands the *scope* of what the augmentation pole covers (now including the work-design layer, not only the AI-deployment layer).

### 12. *Humans on judgment, agents on execution* + the anti-disposable-applications stance ([[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London Exec Forum, 21 May 2026]])

A second prescriptive voice on the augmentation pole — this time at AWS-vendor altitude. Allen's load-bearing principle (~27:24–27:30): ***"put humans on judgment work, agents on execution work."*** This is the concept page's tightest **division-of-labour heuristic** for the augmentation cut to date — narrower than the Anand-Wu task-quadrant grid and the MITTRI/Cisco replace-vs-give-agency framing, more operationally tractable than Storoni's gear-2-vs-gear-3 work-design lens, and directly compatible with both.

Paired with Allen's anti-disposable-applications stance (~5:24): *"software is going through the roof and beyond. We are getting to disposable applications. We do not want this as leaders, right?"* — the **failure mode of the augmentation pole** that mirrors Storoni's quality-over-quantity reframe. Allen names *Jevons paradox* as the underlying mechanism (cheaper software → more software → more disposable software) and the moats-erosion thesis as the strategic-altitude consequence. Brooklyn Solutions' customer-side ratification of the *human-starts-human-ends* operational pattern (Francis, ~40:13–40:54: *"we essentially always have a human start the work and a human end the work. But we may have agents of all different sorts in between"*) is the **vendor-customer-side compatible-with-regulation operationalisation** of the same principle for regulated-customer contexts (MoD, Danske Bank).

Convergent with [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni 2026]] on the prescriptive frame, with [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] on the task-by-task deployment lens, with [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] on the agency-with-oversight progression. Adds the AWS-vendor altitude to the augmentation-pole prescriptive cluster.

### 13. *Don't treat AI agents like employees* — the BCG/HBR anti-anthropomorphizing-framing finding ([[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp, Bedard, Wiles, Hsu, Krayer 2026]])

The wiki's first **RCT-grade empirical evidence on framing**: in a N=1,261 randomized experiment, the *AI-as-employee* framing (vs *AI-as-tool* framing, holding everything else constant) caused — among managers in orgs that already have AI on org charts — a 9pp drop in personal accountability, a 44% increase in escalation requests, 18% fewer errors caught, and (whole-sample) 13% higher uncertainty about professional identity. **The framing alone moves the augmentation-vs-automation interpretation** workers apply — when companies fail to distinguish augmentable from substitutable roles, *"employees are left to interpret AI solely as a substitute rather than a support, undermining trust and culture for all adopting populations"* ([[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al.]]). The article's prescription is to *make accountability explicit and personal for employees and agents* — decision rights, escalation triggers, consequences — rather than diffuse responsibility through anthropomorphizing language. Convergent with [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen's]] *"put humans on judgment work, agents on execution work"* + Brooklyn's *"human starts the work, human ends the work"* at the operational layer (15 days apart, independent vantages).

### 14. Augmentation is contingent on interaction-design, not guaranteed by deployment choice ([[2025-06-09-krakowski-human-centered-ai-field-experiment|Krakowski et al. 2025 (Management Science)]])

The wiki's first DiD-grade academic field experiment on the augmentation pole showing **untailored augmentation can produce *negative* performance vs the legacy IT control**. N=72 Nordic pharma sales experts; three conditions (legacy IT control / untailored AI / tailored AI tuned to Kirton 1976 cognitive style across four parameters — work procedure, decision authority, training, incentives). The *same* AI system is identical across conditions; only the interaction-design parameters differ. Result: tailored AI improves performance vs both control and untailored; **untailored AI gradually declines vs the stable legacy-IT baseline**. The qualitative interview evidence supplies the mechanism: a Danish innovator in the untailored condition: *"We got this super tool, and at the same time, I felt like in prison... this level of controlling killed my internal drive!"* Login-data mediation analysis shows utilization gradually decreases in the untailored condition and increases in the tailored condition — *rational adaptation, not algorithm aversion*. The wiki's strongest single-source empirical claim that **augmentation is contingent on interaction-design, not guaranteed by deployment choice**. Sharpens the [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson-Li-Raymond +15% finding]] (whose augmentation deployment was *explicitly designed* to augment — i.e. *tailored* in Krakowski's vocabulary) by supplying the contrast case where the design discipline was missing. Pairs with [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua / Jagged Frontier]] (same INFORMS-journal family + same DiD/RCT method + same outside-the-frontier-loses pattern, with the bounded region being *task-shape* there and *interaction-design* here).

### 16. The HubSpot *redeployment-of-ten* + IBM *redesign-entry-level-roles* worked examples ([[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles / WP Intelligence May 2026]])

[[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles (May 2026)]] supplies two distinct **US-mid-cap practitioner worked examples** on the augmentation pole, each operationalising the *task-vs-job* distinction in a different direction.

**The HubSpot redeployment-of-ten.** Helen Russell (HubSpot CPO; ~9,000-employee AI-powered marketing/sales/customer-service platform): *"Our mantra is that we have no intention of doing some mass layoff."* Operational pattern: agents identify hundreds of thousands of new customer prospects + automate inbound queries. **The HR-function specific worked example**: *"When agents took over interview-scheduling and other tasks handled by recruiting coordinators, Russell moved 10 of them to handle work related to items such as assessing employee satisfaction and building group and individual development plans."* The augmentation pole executed at the **role-redesign level**: the *task* (interview-scheduling) is automated, the *person* is moved to higher-judgment work (satisfaction, development plans). Convergent with [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero|Scheffer's HelloPrint 100→18 customer-service]] at SME altitude — Scheffer also moves people-not-roles (via natural attrition) but the operational shape is the same.

**The IBM redesign-entry-level-roles.** Giles's third executive recommendation: *"When it announced its plan to triple entry-level hiring, IBM stressed its new recruits wouldn't be doing traditional starter tasks; instead, they will work on customer-facing projects and reviewing the output of agentic AI systems. That's going to require a greater level of managerial supervision, but it's a far better use of AI-native talent."* The augmentation pole executed at the **role-content-redesign level**: same job-title (entry-level analyst/associate), different task-portfolio (customer-facing + agent-output-review instead of process-routine work). Convergent with [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean]]'s *delegate tasks, not judgment* heuristic and with the [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS]] *humans on judgment work, agents on execution work* line — the IBM example is what those prescriptions look like *at the entry-level role*.

The two examples together extend the augmentation discipline from the *task-level deployment* layer (Anand-Wu, MITTRI/Cisco) into the *workforce-redeployment* layer (Russell, IBM) — the same conceptual cut applied to *what happens to the people whose tasks were automated*. The wiki's emerging operational rule: **augmentation works when the savings get reinvested in role-redesign, not in headcount-reduction.**

### 17. The Peron radiology-displacement-that-didn't-happen + radiologist-training-gap clinical anchor ([[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron / MIT SMR May 2026]])

[[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron (May 2026)]] supplies the wiki's first **clinical-domain historical-prediction-vs-outcome anchor** on the displacement question:

> *"A decade ago people were saying — Oh gosh, we're never going to have radiologists again because the machines are going to do everything. And that narrative has really not played out at all."* — Peron (Chief Medical Officer, Philips; physician by training).

The mechanism Peron names: AI takes the *low-value* radiology work (reviewing imprecisely-captured images, doing reports, reassessing normal images), frees radiologists for the *unique-judgment* work. **The Philips SmartArt cardiac-MRI worked example** — AI-driven one-click automation that compresses cardiac-imaging setup from ~15 minutes to **30 seconds** (FDA-cleared 2026), reducing dependency on highly-trained technicians and ~4×-ing throughput on expensive machines — is the operational shape of the augmentation pole at vendor-product altitude in a regulated clinical setting.

**The radiologist-training-gap follow-up question** Peron raises (from a recent radiologist-society meeting, currently unresolved): *"What if we could have AI defining all normal images and then radiologists will be looking at only abnormal? ... How are we going to get the radiologist trained in what is abnormal if they are not going to be seeing normal?"* The wiki's first clean **clinical-domain instance** of the augmentation-pole's *training-pipeline-gap* failure mode: if AI handles the *exemplar-of-normal* training-data class, downstream specialists lose the calibration-against-normal previously developed through volume practice. See [[ai-deskilling]] §"The Peron radiologist-training-on-normal-images gap" for the deskilling-specific reading.

The **structural-supply-shortage condition** that makes augmentation rather than displacement the equilibrium in healthcare specifically: *"As we incorporate technology we'll be able to do more with the same not with less."* The Peron source converges with [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee et al. / MGI 2025]]'s placement of clinicians in the **people-centric occupation archetype** (34% of US workforce, $71k avg pay — the *physical-and-interpersonal-protected* segment). MGI quantitative + Peron qualitative-practitioner = same finding at two altitudes.

### 18. *Humans as the interface, the product as the operation* — the AI-native services-vendor product-design pattern ([[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren / YC Startup School June 2026]])

[[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren (June 2026)]] supplies the wiki's first YC-altitude **product-design pattern** for AI-native services companies — distinct from both the *AI-software-product augmentation pattern* (the prior YC default) and the *enterprise-deployment augmentation pattern* (Anand-Wu, MITTRI/Cisco, Anthropic Economic Index).

> *"With AI services, the setup is the opposite of most software. The human is the interface of the customer, not the product. The product helps the human scale their work nonlinearly. That changes pretty much everything around building the actual product."*

Four operational implications Warren names:

**(a) Operations mindset.** *"Find the bottlenecks and build for the bottlenecks. Throughput and cycle time are now product metrics. Track them like you would daily active users."* The augmentation pole executed with **operations-research metrics as the primary product KPIs** — distinct from the per-task-quality lens that dominates [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]]'s 2×2 deployment framework. Warren's contribution: throughput and cycle-time *are* the augmentation success-metric in the services-vendor category, not a secondary operational concern.

**(b) Variance is the existential problem.** *"By variance, I mean non-uniform outputs from your actual service. Customers will fire you for variance faster than they will fire you for being a bit slower or a bit more expensive than the incumbents. They need to trust the output. Inconsistency destroys trust, which causes churn."* The wiki's clearest single-source statement that **variance-not-cost-not-speed** is the customer-firing trigger in AI-services augmentation. Convergent with [[2026-03-20-huggingface-agentic-evaluations-workshop|Narayanan / Princeton]]'s *reliability-as-the-gating-dimension* framing — Warren applies the same principle at the *service-delivery customer-relationship* layer rather than the *release-decision* layer.

**(c) Humans-in-the-loop should scale nonlinearly with revenue.** *"If revenue scales just in line with the number of humans you add, you'll have major problems. The humans in the loop also need to enjoy the software. They are your users."* The wiki's clearest single-source articulation of the *augmentation-pole-requires-superlinear-revenue-per-human-hour* economic test for AI-services vendors. Convergent with the prior §16 *HubSpot redeployment-of-ten + IBM redesign-entry-level-roles* framing applied at vendor-product-design altitude rather than at HR-redeployment altitude — same principle (augmentation works when the savings get reinvested), different operational layer.

**(d) Pilot-is-the-product, then automate the process.** *"It's okay to do things that don't scale at the very beginning, but eventually you really do need to scale. Automating the process is the product."* The augmentation-to-automation transition stated as an **operational sequencing rule** — pilot with humans-in-the-loop to learn the workflow, then progressively automate the process as the product matures. Convergent with [[2026-03-20-huggingface-agentic-evaluations-workshop|Narayanan]]'s *augmentation-to-automation-transition-follows-reliability-improvements-per-task-class* framing — Warren supplies the founder-altitude operational sequencing for the same transition.

Pair with §16 (Giles HubSpot + IBM) and §17 (Peron radiology) — the three sections together form the wiki's **role-redesign + vendor-product-design** cluster on the augmentation pole, complementing the prior task-level (Anand-Wu, MITTRI/Cisco, Anthropic Economic Index) and firm-boundary ([[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria]]) layers.

### 19. The *task vs job* analytical lever ([[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans / Lenny's Podcast May 2026]])

[[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans (May 2026)]] poses the cleanest **independent-analyst-altitude restatement** of the automation/augmentation question: *"What is the hard part of the job? Is the hard part of the job writing the code line by line? Is the hard part of the job making the PowerPoint? Or is the hard part of the job something else? Is it the task or the job?"* The McKinsey-deck worked example: a Claude-Code-generated McKinsey deck is *"a bunch of dog crap. That's not what you'd get from McKinsey. But even if it was, that's not what you paid them for. What you actually pay Bain to do is to go and walk all over your enterprise, your company, and work out, yes, but why is it that you didn't do that? And how do the politics of this work? And what do you actually need to do?"* Same argument applied to Amazon (*"Amazon does is get you the SKU, but knowing what SKU you want is another job"*) and software (*"Claude code can write you the code, but what code do you want? It can make you the features, sure, but what features do you want? Who's your customer?"*).

The *task vs job* framing is the **analytical alternative** to percentage-of-job decomposition that Evans rejects (see [[jagged-frontier]] §"Methodological critique of percentage-of-job decomposition" for the negative-space argument): instead of asking *"X% of your work is automatable"*, ask *"which task is the value-creating one, and which is the means?"* The McKinsey deck is the task; walking the enterprise is the job — automating the task without doing the job replaces the artefact and removes none of the value.

Convergent with the Anand-Wu task-quadrant grid (which already asks *which tasks belong in which deployment quadrant*) and with the Forsgren & Macvean *delegate tasks, not judgment* boundary marker. Evans's contribution is the **rhetorical compression**: the task-vs-job question is the same as *what are people actually hiring you for?* — a useful customer-substitution test for any automation deployment.

### 17. The MGI structural framework: 7 occupation archetypes + 65/35 nonphysical/physical work-hour split + 44/13 agent/robot capacity split ([[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee et al. / MGI 2025]])

[[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|MGI's *Agents, Robots, and Us* (November 2025)]] supplies the wiki's **most structural and panoramic anchor** on the automation-vs-augmentation cut. Four substantive additions to this concept:

**(a) The 65%/35% nonphysical/physical work-hour split** — the structural substrate for the agent/robot framing. *Two-thirds of US work hours require only nonphysical capabilities* (agent territory; ~$2.26T of the $2.9T economic-value claim) → automation through cognitive AI; *one-third require physical capabilities* (robot territory; ~$0.67T) → automation through embodied AI. The agents-vs-robots cut is therefore **not a deployment-style choice but a capability-substrate choice** rooted in the nature of the work activities themselves.

**(b) Technical automation potential by capacity split** — at current AI capabilities, **agents could perform 44% of US work hours** and **robots could perform 13%**. Together: **57% technical automation potential**. The remaining 43% breaks down as 21% nonphysical-only (requires real-time social/emotional awareness) + 22% physical-only (requires fine motor + situational awareness AI cannot yet replicate). The four-quadrant decomposition (Exhibit 2) is the wiki's most granular *technical-automation-potential* taxonomy.

**(c) The seven occupation archetypes** — `wiki/concepts/automation-vs-augmentation` now has a structural occupation-distribution frame:

| Archetype | Workforce share | Avg pay | Examples |
|---|---:|---:|---|
| People-centric (least automatable) | 34% | $71k | Registered nurses, psychologists, firefighters |
| People-agent | 21% | $74k | Sales reps, secondary school teachers, HR specialists |
| Agent-centric (most automatable cognitive) | 30% | $70k | Accountants, software developers, lawyers |
| People-robot | <1% | $54k | Insulation workers, drywall + ceiling-tile installers |
| Robot-centric (most automatable physical) | 8% | $42k | Stockers + order fillers, welders, cooks |
| People-agent-robot | 5% | $60k | Receptionists, medical assistants, correctional officers |
| Agent-robot | 2% | $49k | Machine setters, bakers, library assistants |

The **agent-centric quadrant** (30% of workforce, $70k avg pay) is the *wage-premium-at-risk* segment — knowledge-work occupations whose cognitive tasks are 55%+ technically-automatable. The **people-centric quadrant** (34%, $71k avg pay) is the *physical-and-interpersonal-protected* segment whose tasks current AI cannot replicate. The bimodal distribution puts the automation-vs-augmentation cut at the *occupation level*, not the firm/role level — informative against [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua's task-level jagged frontier]].

**(d) The 72% shared-skills finding** — even when occupations are clearly automatable or not, **72% of the underlying skills are required for both automatable and non-automatable work activities**. Only 11% of skills are required for people-led work only; only 17% for AI-led work only. This is the **skill-level decoupling** from the occupation-level archetype distribution: an accountant (agent-centric occupation) and a nurse (people-centric occupation) share most of the same skills — communication, problem-solving, detail orientation — they just apply them in different mixes of automatable / non-automatable activities. The implication: **automation reshapes how skills are applied, not which skills are valuable.**

The MGI framework joins the wiki's existing automation-vs-augmentation anchors — [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] (strategic deployment), [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] (task design), [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson]] (labor consequences), [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] (Claude.ai usage data) — as the **structural-modeling** layer that the others triangulate empirically. MGI alone gives the wiki the *occupation-level prospective distribution* of where people, agents, and robots will be by 2030.

### 20. The augmentation case, measured and prescribed: GDPval + Argenti (Oct 2025 / June 2026)

Two sources land the augmentation thesis from opposite ends — one empirical, one prescriptive:

- **Measured** — [[2025-10-05-patwardhan-et-al-openai-gdpval|GDPval (OpenAI)]] shows that **pairing frontier models with expert human oversight is cheaper and faster than unaided experts**. Under a "try the model, fix it yourself if unsatisfactory" workflow, model assistance saved the expert both time and money — even though the best model alone reached only 47.6% wins-or-ties. This is the cleanest empirical statement in the wiki that the *augmentation* configuration (human + model) dominates either the pure-human or pure-model configuration on real economic deliverables.
- **Prescribed** — [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti (Goldman Sachs CIO, HBR)]] names the human-side adaptation augmentation demands: the shift from **operator to supervisor/mentor** ("the new 100%"). The value-add moves from producing every deliverable to giving clear instructions, applying judgement, and ensuring systemic controls so agents execute safely. *"An agentic future requires everyone to turn into a manager of sorts."* This is the role-redesign correlate of the [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles/WP]] operator→orchestrator finding, here from a first-party CIO vantage.

Together they bracket the augmentation deployment model: GDPval shows it *works economically*; Argenti specifies the *mindset and role redesign* that lets an organization capture it.

## The four-source convergence on the distinction

Four wiki sources, with distinct vocabularies and methodologies, all draw essentially the same conceptual cut:

| Source | Distinction | Vocabulary |
|---|---|---|
| [[2026-04-28-ai-index-report-2025\|AI Index 2025]] | Productivity studies on augmentation; no clean automation split | "AI use" (binary) |
| [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] | "No regrets zone" (automation) vs. other three quadrants (augmentation) | "Cost of errors × type of knowledge" |
| [[2026-04-28-mittri-cisco-ai-enabled-enterprise\|MITTRI/Cisco]] | "Replace vs. give agency with oversight" | "Chatbot → agent → multi-agent" progression |
| [[2026-04-28-brynjolfsson-canaries-coal-mine\|Brynjolfsson et al. 2025]] | Automative vs. augmentative use (Anthropic Economic Index) | "Substitute vs. complement for labor" |
| [[2026-04-28-anthropic-economic-index-q4-2025\|Anthropic Economic Index, 4th report]] | Longitudinal Claude.ai split (52% augmentation / 45% automation in Nov 2025) | "Directive / Feedback Loop / Task Iteration / Learning / Validation" |
| [[2026-05-07-anthropic-economic-index-5-learning-curves\|Anthropic Economic Index, 5th report]] | Stable Claude.ai split through Feb 2026 (53/45); emergent API automation clusters (sales, trading, coding harnesses) where automation rose sharply at the surface where it matters for enterprise spend | "Surface- and cluster-specific automation"; "skill-biased technological change" |
| [[2026-05-07-ransbotham-augmented-learners\|Ransbotham et al. 2024]] (MIT SMR × BCG, 8th annual) | Augmentation reframed as *learning-augmentation*: 15% Augmented Learners combine high org-learning + high AI-specific-learning capability; 1.6× uncertainty management; 1.4× revenue benefits; 1.9× long-term-project investment; 2.4× high-risk investment | "Augmented Learners" (organizational-level construct, not task-level) |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron & Schrage 2026]] | The expert-as-evaluator argument: AI compresses *implementation* but cannot compress *formation of expertise*. Augmentation is operationalized as **verification → evaluation → learning capture**; without all three, orgs *consume* (deplete) rather than *compound* AI value | "Compound benefits"; "return on iteration"; "verification masquerading as evaluation" |
| [[2026-04-28-dellacqua-jagged-technological-frontier\|Dell'Acqua et al. 2026 (Jagged Frontier)]] | Per-task AI fit determines whether AI augments or harms; introduces "jagged frontier" | "Inside the frontier" (augmentation works) vs. "outside the frontier" (AI degrades performance) |
| [[2026-04-29-boussioux-crowdless-future\|Boussioux et al. 2024 (Crowdless Future)]] | Augmentation pattern is fine-grained: *independent* search (multi-instance) vs *differentiated* search (single-instance with iterative diversification prompts); per-dimension trade-off (HC higher novelty; HAI higher value/quality) | "Independent search" vs. "differentiated search"; "AI-in-the-loop" |
| [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|Dutt et al. 2026 (Bain/OpenAI HBR)]] | Two failure modes when augmentation is shallow: *offering lock-in* (AI optimizes existing offerings) and *process lock-in* (AI automates current processes without redesigning them). Successful firms "reinvent the business" instead, with 10–25% EBITDA gains | "Offering lock-in" vs. "process lock-in"; "improve the task" vs. "reinvent the business"; [[micro-productivity-trap]] |
| [[2026-05-05-nishar-nohria-end-of-one-size-fits-all\|Nishar & Nohria 2026 (HBR)]] | Firm-boundary 4-model decision: **Build** (deep augmentation of distinctive workflows) ↔ **Compose** ↔ **Collaborate** ↔ **Buy Outcomes** (firm-level automation: vendor takes responsibility for the whole job, e.g. Adobe's outcome-based pricing). Choice is no longer cost-driven; it's a strategic decision about where differentiation lives. | "Build / Compose / Collaborate / Buy Outcomes"; "the boundary of the firm becomes a variable rather than a given" |
| [[2026-03-20-huggingface-agentic-evaluations-workshop\|Narayanan / Princeton @ HF Agentic Evals 2026]] | **Reliability as the gating dimension**. Automation deployments require a higher reliability threshold (10% failure rate on autonomous customer service = dead-on-arrival) than augmentation deployments (10% failure rate on coding-agent suggestions = still net-positive with human review). Capability and reliability are orthogonal; 12-sub-dimension reliability decomposition, most unsolved. | "Capability-reliability gap"; "release-decision threshold"; "automation tasks vs augmentation tasks" |
| [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer\|Forsgren & Macvean / Google I/O 2026]] | **The automation-trap warning** at the engineering-team layer + **"delegate tasks, not judgment"** as the boundary-marker for what humans keep under augmentation. *"Our top teams avoid the automation trap by establishing clear human baselines for their work and measuring verification overheads. To hill climb towards a win, we run experiments to find the tasks where the probability of success is highest. This allows us to keep human attention on the tasks we know agents can't yet perform, or where taste and judgement is really essential."* Engineering-leadership operationalisation of the augmentation pole — keep human attention on *judgement-bearing* work, delegate *task-execution* to agents. The talk also operationalises the **orchestrator-not-conductor** mental shift: *"a big mental model shift from being a Conductor of an individual agent to an Orchestrator of a system"* — multi-agent automation framed as augmentation-of-the-engineer's-judgement rather than agent-as-employee-replacement. Convergent with Narayanan's reliability-gating: the automation-trap-avoidance discipline is Narayanan's release-decision threshold applied per-task-class at fleet scale | "Avoid the automation trap"; "delegate tasks, not judgment"; "orchestrator of a system, not conductor of an individual agent" |
| [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai\|Storoni / HBR IdeaCast 2026]] | **The normative quality-over-quantity reframe** + **neuroscience mechanism for the augmentation pole**. *"The productivity of a company is no longer proportional to the quantity of output of its human workers, because the realm of quantity is being taken over by AI and technology. Humans now influence the productivity of their organization by the quality of their output."* Three-gear framework on the norepinephrine inverted-U curve: gear-2 is the cognitive state in which humans contribute the work AI cannot do; gear-3 reactive work is what AI does better and what gets automated next. Augmentation prescription becomes a **work-design** decision, not only a deployment decision: protect the gear-2 windows (chronobiology-aware schedules, focus blocks, intrinsic-motivation structures), let AI take the gear-3-reactive work. The wiki's first prescriptive voice from a neuroscience vantage on what the human side of the augmentation pair has to be doing | "Quality over quantity"; "three-gear framework"; "norepinephrine inverted-U"; "AI managers"; "work-design as augmentation prescription" |

When four independent sources arrive at the same cut from different angles (theory, strategy, vendor framing, and large-scale payroll data), the distinction is robust enough to be a load-bearing concept in the wiki.

## The Claude-channel customer-story cluster (Feb–May 2026)

A 2026 cluster of [[Anthropic|Anthropic]] Claude-channel customer-story videos supplies named-incumbent / named-platform practitioner anchors on both legs of the cut:

| Source | Pattern | Vantage |
|---|---|---|
| [[2026-02-18-lyft-customer-support-with-claude\|Lyft / Claude customer support (Feb 2026)]] | **Augment-and-reinvest-the-savings** — 87% resolution-time reduction; savings (*"millions of dollars"*) explicitly reinvested into upskilling agents (anti-burnout) plus a new high-touch programme (*Lyft Silver*). The 87% time saving did *not* translate into headcount reduction in this telling | named-incumbent contemporary practitioner anchor for the augmentation leg. Practitioner-side data point on the same phenomenon [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work\|Brynjolfsson, Li & Raymond (QJE 2025)]] measured at +15% RPH in a 2020–21 GPT-3 deployment — direction-of-effect consistent, scale of the practitioner-reported gain reinforces the QJE finding as a floor |
| [[2026-02-09-hubspot-customer-success-with-claude\|HubSpot / Claude customer success (Feb 2026)]] | **Augmentation as role-level scope expansion** — Claude turns a call transcript + knowledge-base articles into hospitality-revenue analysis the CSM then takes to the customer (*"that is something so far beyond my typical role as a CSM"*). Augmentation here *changes what the role does*, not just how fast it does it. Vendor-side 40% developer-productivity claim included as testimonial only | extension of the augmentation framing into customer success (not only customer support), with role-scope-expansion as the operational mechanism — complementary to [[2026-05-07-ransbotham-augmented-learners\|Ransbotham's *augmented learners*]] and [[2026-05-05-nishar-nohria-end-of-one-size-fits-all\|Nishar/Nohria's *end of one-size-fits-all*]] |
| [[2026-05-13-jha-emergent-democratizing-app-building-with-claude\|Emergent / Jha-Ryan interview (May 2026)]] | **Full automation, replacement-of-the-outside-vendor** — Emergent users are *not* augmenting an existing dev team; they're replacing the dev-shop alternative. CEO names the comparison: *"a $250,000 price point that they would have paid if they had gone and and hired a dev shop"*. The user class is SMBs / domain experts who *never had software at all* (Christy in Alaska shipping *Equ*). $100M ARR in 8 months; 7M users in 190 countries; 70–80% never wrote a line of code | the **automation leg at scale for non-developers**. Distinct from enterprise-internal automation (where staff is augmented or displaced) — this is *SMB-replacement-of-an-outside-vendor-relationship-they-could-not-previously-afford*. Adds a previously-missing third deployment pattern to the wiki's cut: augmentation-of-staff, automation-of-staff, and *automation-as-substitution-for-an-outside-services-spend* |

The Lyft / HubSpot / Emergent triple is the wiki's first cluster on the automation/augmentation cut drawn entirely from *2026 named-incumbent practitioner self-reports* rather than third-party studies or vendor-CEO predictions. The two short-form videos (Lyft, HubSpot) are promotional and should not be cited as load-bearing on their own; the Emergent interview is substantive and load-bearing.

## Debates / contradictions

- **Is the cut binary or continuous?** Anthropic's Economic Index allows occupations to be classified as primarily-automative, primarily-augmentative, or mixed. In practice many AI uses sit on a continuum (e.g., a code assistant is augmentative when used for completion, automative when used for issue resolution). The dichotomy is useful for analysis but not always clean in the wild.
- **Does augmentation reliably *not* displace labor?** [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson 2025]]'s Fact 3 finds no displacement in augmentative uses *for young workers*. But long-run effects (productivity J-curve, demand elasticity, eventual task automation) might cause augmentative deployments to slide toward automation over time.
- **Augmentation can still concentrate gains.** The "equalizing effect" in [[2026-04-28-ai-index-report-2025|AI Index 2025]]'s productivity studies is at the worker level *within* a role. At the firm level, augmentation may still let the firm produce more with fewer workers — meaning the *individuals* who keep their jobs gain, but the *people who would have been hired* don't.
- **The cut is observable now via Claude conversations.** The Anthropic Economic Index methodology — sampling millions of Claude conversations and classifying each as automative/augmentative/none — is a novel measurement instrument. Its reliability depends on Claude's user base being representative of LLM usage broadly. Cross-validation with other LLM telemetry would strengthen the methodology.

## Related concepts

- [[ai-employment-effects]] — the labor-market consequences of the automation/augmentation choice
- [[enterprise-ai-adoption]] — the organizational decision-making layer
- [[ai-agents]] — agents are concentrated on the automation side of the cut
- [[generative-ai]] — the technology underlying both modes
- [[responsible-ai]] — labor displacement is an under-attended RAI concern

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "automation") OR contains(tags, "augmentation")
SORT file.name ASC
```
