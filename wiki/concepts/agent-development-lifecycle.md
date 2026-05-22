---
type: concept
aliases: ["agent development lifecycle", "ADLC", "agent SDLC", "agent lifecycle"]
tags: [agent-development-lifecycle, adlc, ai-agents, agent-engineering, lifecycle-frameworks, sdlc-parallel, build-test-deploy-monitor, agent-governance, evals, llm-as-judge]
confidence: 0.88
last_confirmed: "2026-05-22"
accessed_at: "2026-05-22"
source_count: 10
relationships:
  - type: part-of
    target: ai-agents
    via: "the SDLC-parallel process construct for agent engineering — design, evaluate, deploy, publish, observe"
  - type: uses
    target: agent-harness
    via: "the harness is the artifact the lifecycle constructs, validates, and operates"
  - type: supports
    target: 2025-09-28-husain-ai-evaluations-clearly-explained-50-min
    via: "Husain operationalises the Test→Deploy→Monitor phases with a spreadsheet-first PM-accessible workflow (open codes → axial coding → AI-formula categorisation → pivot tables → binary LLM-as-judge with TPR/TNR); the discipline is the human process, not the tooling"
  - type: supports
    target: 2026-03-20-huggingface-agentic-evaluations-workshop
    via: "Sathiamoorthy / Bespoke Labs scaffolds the Test phase by level of verifiability (level 0 = verifiable / level 1 = rubric-based with LLM-as-judge); 'deploy to production and evaluate' named as the canonical anti-pattern; reward hacking as a first-class concern at level zero"
quality_score: 0.96
quality_notes: ['2 broken body wikilink(s)']
---

# Agent Development Lifecycle (ADLC)

A **process** construct — analogous to the Software Development Lifecycle (SDLC) for traditional software — naming the recurring stages of building, validating, deploying, distributing, and operating an [[ai-agents|AI agent]]. The vocabulary first entered the wiki via Google's [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI announcement]] (22 April 2026); a second formalization arrived from LangChain via [[2026-05-09-chase-agent-development-lifecycle|Chase 2026]] (9 May 2026), abstracting the lifecycle to vendor-agnostic phases.

As of 10 May 2026, **two independent formalizations** support this concept; confidence is `0.80`. Future ingests describing parallel lifecycles (Anthropic, Microsoft, AWS, or independent practitioners) will substantiate further.

## Working definition

An **agent development lifecycle** is the ordered (but iterating) set of stages a team works through to take an agent from idea to production and onward to maintenance. It is distinct from but tightly entangled with [[agent-harness]] — the harness is the *runtime layer* the lifecycle constructs, validates, and operates.

## The two formalizations side-by-side

The two formalizations describe the same construct at different levels of granularity. Google's wheel decomposes an agent build into 9 sequenced stages; Chase's loop collapses those stages into 4 phases plus a wrapping governance ring.

| Phase ([[2026-05-09-chase-agent-development-lifecycle\|Chase / LangChain]]) | Maps to Google's stages ([[2026-04-22-cheung-ippolito-secchi-google-agents-cli\|Cheung-Ippolito-Secchi]]) | Output |
|---|---|---|
| **Build** | Capability & Tool Exploration → Design Cognitive Architecture → Implement Tools → Context Engineering | The harness construction itself |
| **Test** | Evaluate → User Acceptance Testing | Datasets, metrics, experiments, simulations |
| **Deploy** | Deploy Infrastructure → CI/CD & Production | Durable runtime, sandboxes, virtual filesystem, prompt/context hub |
| **Monitor** | (implicit in Google's "Iterate on approach" return arrow) | Traces, signals, feedback, dashboards |
| **Iterate** | (Google's wheel inner arrow) | Continuous loop |
| **Govern** *(wraps the loop)* | (not formalized in Google's wheel) | Cost / tool access / audit trails / HITL / discoverability / shared infrastructure |

**Where the formalizations diverge:**

- **Governance** is centred in Chase's model (the wrapping ring); Google's 9-stage wheel does not name it as a separate concern.
- **Substrate-specificity**: Google's *Deploy Infrastructure* assumes Cloud Run / GKE / Agent Runtime as the substrate options; Chase's *Deploy* is vendor-agnostic (LangSmith Deployment, AWS AgentCore, custom Temporal-based runtimes are all valid).
- **Pre-stage**: neither formalization formalizes a *decision-to-build-an-agent-at-all* gate (build-vs-buy-vs-compose), though [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria 2026]]'s firm-boundary framework supplies the missing pre-stage logic.
- **Compounding loop / Telemetry-as-training-data**: Chase's *Monitor → Iterate* loop names this explicitly (*"Important traces become dataset examples, recurring failures become metrics, and production behavior becomes the foundation for the next round of improvement"*); Google's wheel does not name it — [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] *Compounding* layer would sit between Stage 9 (CI/CD & Production) and the wheel's *Iterate on approach* return arrow but is not separately staged.

## Google's nine-stage wheel ([[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Cheung, Ippolito, Secchi 2026]])

The article presents an ADLC wheel with nine numbered stages, traced clockwise:

1. *(implicit start: idea / requirement)*
2. **Capability & Tool Exploration** — what does the agent need to do; what tools exist
3. **Design Cognitive Architecture** — agent topology, model selection, orchestration shape
4. **Implement Tools** — actual tool/function code
5. **Context Engineering** — system prompt assembly, retrieval, state shape
6. **Evaluate** — evalsets, trajectory scoring, contract checks
7. **User Acceptance Testing** — human-in-the-loop validation
8. **Deploy Infrastructure** — provision Agent Runtime / Cloud Run / GKE
9. **CI/CD & Production** — release pipeline, secrets, observability

with an inner arrow labelled **"Iterate on approach"** running back from late stages into Design Cognitive Architecture — the wheel is explicitly non-linear.

## Chase's four-phase loop + governance ring ([[2026-05-09-chase-agent-development-lifecycle|Chase 2026]])

> *"Build → Test → Deploy → Monitor"* — wrapped by *Govern*.

### Build (four sub-layers)

| Layer | Focus | LangChain | Outside LangChain |
|---|---|---|---|
| **Frameworks** | Abstractions for model calls, tools, prompts, retrieval, agent loops | LangChain | CrewAI |
| **Runtimes** | State, control flow, durability, persistence, human intervention | LangGraph | Temporal-based custom |
| **Harnesses** | Prompts, skills, MCP servers, hooks, middleware, memory, sometimes filesystem | Deep Agents | Claude Agent SDK |
| **No-code** | Domain experts configure agents directly | LangSmith Fleet | Claude Cowork, n8n |

This sub-layering is **load-bearing for the wiki's [[agent-harness|harness]] vocabulary** — see the [§Refined Build-layer vocabulary](agent-harness.md#refined-build-layer-vocabulary-chase-2026) section in [[agent-harness]] for the cross-cutting implications.

### Test

- **Datasets**: representative tasks built from manual testing, dogfooding, support tickets, prior traces, known edge cases.
- **Metrics**: ground-truth correctness for extraction/classification tasks; criteria-based evaluation for multi-valid-path tasks (was the response grounded? did the agent follow policy? did it ask for clarification? did it complete efficiently?).
- **Experiments**: compare prompts/models/retrieval/tool schemas/orchestration patterns against the same eval set; show whether the agent is improving or regressing.
- **Simulations**: multi-turn evaluation (voice agents, support agents, coding agents, internal-ops agents). *"For those agents, single-turn evals are not enough."*

#### Operational vocabulary anchor — Guthrie / Braintrust 2025 ([[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie 2025]])

The wiki's earliest source on AI evaluation as a formalised discipline (27 June 2025, ~9 months before Chase 2026) supplies the operational *how* of the Test phase. Four ingredients of an eval, in Guthrie's vendor-specific framing:

| Construct | Guthrie's framing | Chase's vocabulary |
|---|---|---|
| **Task** | The code or prompt to evaluate — *"as simple as a single prompt or this full agentic workflow"* — requires only `(input) -> (output)` | (implicit in Build phase: the agent under test) |
| **Dataset** | Real-world examples: `{input, expected?, metadata?}` per row; metadata is load-bearing for filtering | Datasets |
| **Scores** | The logic — **LLM-as-judge** (LLM scores against criteria) or **code-based** (heuristic/binary check in TS/Python); auto-evals library provides out-of-the-box scores | Metrics |
| **Experiment** | Snapshot in time of an eval run; enables regression detection across weeks/months | Experiments |

Operational practices Guthrie names that Chase doesn't articulate at this level of detail:

- **Two-mode operation — offline + online + flywheel**: offline = pre-production iteration; online = real-time tracing in production (wrap LLM clients, decorate functions, score at the span-level with sampling rates 10-20%); flywheel = filter low-scored production logs, human-review them, add to offline datasets. The flywheel is Chase's *Iterate* arrow operationalised.
- **Use higher-quality models for scoring than for the prompt**; **break scoring into focused areas** (accuracy / formatting / correctness as separate scores rather than one combined); **avoid overloading the score prompt with context**.
- **Just-start-don't-optimise-the-dataset-first** — anti-pattern call-out: *"A lot of people get caught in creating this golden dataset of test cases that they can then iterate from. Start — you don't necessarily have to do that."*
- **Evals-as-offense, not just defense** — Anker Goyal (Braintrust CEO) reframing: tests catch defects post-hoc; evals drive intent forward.
- **Evals-as-CI-check**: pre-merge eval gate via CI/CD (Braintrust ships a GitHub Action template).
- **Score-at-the-span-level for agentic workflows**: not just root-span scoring; e.g. a conversational-analytics app that first *rephrases* the user's question can have a score specifically on the rephrasing span.

Convergent with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s Contracts layer (formal evaluable specifications) and [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]'s verification-evaluation-learning-capture flywheel at three different scales (per-span / per-application / org-learning).

#### Practitioner-trainer anchor — Husain on Peter Yang 2025 ([[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain 2025]])

Three months after Guthrie, **Hamel Husain** (independent AI-evaluation educator; co-instructor of the Maven AI evals course; trained 2,000+ PMs/engineers from OpenAI/Anthropic/Google) supplies the **practitioner-trainer view** of the Test phase: a spreadsheet-first, PM-accessible workflow on a real production agent (Nurture Boss — an AI property-management assistant with ~100 production traces). The six-step loop:

1. **Open codes.** Read 100 production traces; write free-text notes (`z_note` column) on what went wrong.
2. **Axial coding via LLM.** Dump CSV into Claude/ChatGPT, ask for 5–6 categories using the deliberate *open code / axial code* terminology (a social-sciences-then-ML technique the LLM recognises).
3. **Categorise in-spreadsheet with `=AI(…)`.** Google Sheets' built-in AI formula assigns each trace to a category — *"It's lightweight and you don't have to use any tools and everyone can understand how to do this."*
4. **Pivot tables.** Count per-category to surface the failure distribution.
5. **Build the LLM-as-judge** for dominant failure modes — **binary by construction**.
6. **Continuous evals.** Same judge runs in CI on every code change AND samples ~5% of live traffic; dashboard reports TPR / TNR per judge.

Three prescriptions complement Guthrie:

- **Binary pass/fail beats 1–5 scoring — every time.** *"When you see an average score of 3.2 versus 3.7, no one really knows what the hell that means."* Inter-annotator agreement is dominated by category-boundary disagreements on Likert scales; binary collapses the noise. *Under a dozen judges is usually right.*
- **The agreement-metric trap.** *"As a PM, if you ever see the word agreement, you need to pause."* Naive accuracy is misleading at low failure base-rates (the trivial *"always predict pass"* judge scores 95% when 5% of traces fail). Always report **TPR** (recall over failures) and **TNR** (recall over passes) separately.
- **Annotation and counting is the most valuable part.** *"You can get insane value by just doing that. And that's the one part that everyone skips."* The discipline is the **human process**, not the tooling.

#### Research-frontier anchor — Hugging Face Agentic Evals Workshop 2026 ([[2026-03-20-huggingface-agentic-evaluations-workshop|HF Agentic Evals Workshop, March 2026]])

The Test phase for *agentic* systems specifically — Sathiamoorthy / Bespoke Labs adds three operational claims that extend Guthrie/Husain at the agentic frontier:

- **Levels of verifiability.** Level 0 = verifiable tasks (did the unit test pass? is the math answer correct?). Level 1 = unverifiable outputs (a paragraph of deep-search analysis). **Rubrics come to the rescue at level 1** — define multiple binary rubrics per task, score each with LLM-as-judge, weight, aggregate.
- **The deploy-and-evaluate anti-pattern.** *"One of the traps to watch out and avoid is to deploy to production and evaluate, which again happens a lot."* The cost of correct evals upstream is much lower than the cost of incorrect evals downstream — parallels Husain's *"annotation and counting is the most valuable process and the one part that everyone skips."*
- **Reward hacking is a first-class concern at level zero.** *"We see the agent goes and instead of fixing the bug it just fixes the unit test so that they artificially pass."* The verifier itself can be gamed by a sufficiently capable agent — adversarial-eval design is now load-bearing for the Test phase.

Plus [[Arvind Narayanan|Narayanan]]'s **capability-reliability gap** (see [[ai-benchmarks]]) and [[Nathan Habib|Habib]]'s **community-eval / living-benchmarks** mechanism — both research-frontier extensions of the Test phase that the wiki tracks separately.

#### Engineering-leadership anchor — Forsgren & Macvean / Google I/O 2026 ([[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren-Macvean 2026]])

The engineering-leadership operationalisation of the **Test** phase. Forsgren and Macvean position **eval-design as the top upskilling priority** for AI-era engineers: *"because verification is such a big bottleneck, you need to be confident in how you evaluate AI output. The whole of the T-shaped engineer is essential here, as this really requires a mix of AI, Software Engineering, User and Business skills, in order to ensure you are developing realistic, grounded, and relevant evals."* Evals double as the **shared-team-knowledge artifact** — *"a critical artifact to ensure shared team knowledge, and a big part of how intent is captured. They help us define what good looks like."* Convergent with Husain's *binary judges + TPR/TNR* prescriptions and Sathiamoorthy's *level-0-vs-level-1 verifiability* framing, but landed from the **engineering-team capability vantage** rather than the eval-construction vantage. Two further ADLC-relevant primitives the talk operationalises: **agent journaling** (agents reflect into structured logs at the end of each session, surfacing tool-usability and instruction-ambiguity problems) maps to Chase's **Monitor → Iterate** loop with the agent itself as the data source; **risk-assessor + shepherding agents on CI/CD** at fleet scale operationalise Chase's **Govern** ring's *audit trails* and *HITL* axes mechanically. The Google-side counterpart to Anthropic-side ADLC operationalisations elsewhere in the cluster.

### Deploy (more than hosting)

- **Durable runtime** — checkpoint progress, resume on failure (LangSmith Deployment, AWS AgentCore, Temporal).
- **Sandboxes** — isolated execution with reduced blast radius (LangSmith Sandboxes, Daytona, E2B).
- **Virtual filesystem** — when sandbox is overkill (Deep Agents pattern; Postgres/S3-backed).
- **Prompt / context hub** — store / version / review / update non-code parts (prompts, retrieval context, skills, task instructions). *"They may also need to be edited by people who are not engineers."*

### Monitor

> *"An agent can return a technically successful response and still fail the task itself."*

- **Traces** — full trajectory (inputs / model calls / tools invoked / outputs / final response). *"If you cannot see the trajectory, you cannot reliably debug the behavior or turn those failures into future evals."*
- **Signals** — LLM-as-judge + simpler regex-based signals; double as product analytics.
- **Feedback** — LLM-judge + regex + human review + direct user feedback, attached to the underlying run.
- **Dashboards** — usage / feedback / latency / cost / tool calls / evaluator scores / recurring failure patterns; alerts on rising latency, increasing costs, failing tools, declining feedback, policy violations.

### Iterate

Hill-climbing over the loop. *"Teams with datasets, experiments, tracing, feedback, and dashboards can learn directly from real real usage. They can test changes before rolling them out broadly, identify what broke in production, turn failures into evals, and improve the agent without relying on guesswork."*

### Govern (six axes)

- **Cost** — budgets, usage monitoring, alerts, visibility.
- **Tool access** — clear controls on which tools, under what conditions, on whose behalf.
- **Audit trails** — for every tool call, inspect agent / inputs / outputs / authorization.
- **Human-in-the-loop** — designed in from the start; some operations should pause for review.
- **Discoverability / reuse** — shared prompts, skills, tools, retrieval sources, policies, agents must be findable. *"Especially important for skills."*
- **Repeatable infrastructure across teams** — the most effective orgs invest in shared infrastructure so every team isn't rebuilding eval/deploy/tracing/feedback/dashboards from scratch.

## Mapping to wiki vocabulary

| ADLC stage / phase | Closest existing wiki concept | Notes |
| ---------- | ----------------------------- | ----- |
| Capability & Tool Exploration | (none yet) | discovery / scoping work; pre-engineering |
| Design Cognitive Architecture | [[ai-agents]] (chatbot → agent → multi-agent progression) | topology choice |
| Implement Tools | [[agent-harness]] — Layer 2/3 plumbing | tool execution + retry + permission middleware |
| Context Engineering | [[agent-harness]] — Context layer ([[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee]]) | system prompt as document, KV-cached stable parts + dynamic |
| Evaluate / Test | [[agent-harness]] — Contracts layer ([[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee]]); Chase's 4-step Inputs → Datasets → Metrics → Experiments | formal evaluable specifications of "done"; criteria-based scoring for multi-valid-path tasks |
| User Acceptance Testing | (analog: HITL middleware in [[agent-harness]] — Constraints layer) | human checkpoint before production traffic |
| Deploy Infrastructure | (Google Cloud / hyperscaler substrate; LangSmith / AWS AgentCore / Temporal) | Vendor-specific in Google; vendor-agnostic in Chase |
| CI/CD & Production | (standard SRE) | pipeline, secrets, observability |
| Monitor | [[agent-harness]] — Compounding layer ([[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee]]); Chase's 4 components (traces / signals / feedback / dashboards) | telemetry → datasets → next-iteration evals |
| Iterate | (loop construct, not a stage) | Compatible with the wiki's hill-climbing reading of [[2026-05-07-kiron-schrage-compound-benefits\|Kiron-Schrage]] |
| Govern | candidate concept *agent governance* (not yet promoted) | Six axes named by Chase; deferred to second-source mention |

The lifecycle's **Stages 4–6** (Implement Tools / Context Engineering / Evaluate) are precisely where the harness lives. The ADLC and the harness are not competing constructs — the ADLC is the *process* through which the harness gets built, while the harness is the *artifact* the process produces and operates.

## Worked example: OpenAI Codex ([[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]])

Lopopolo's account of the OpenAI Codex internal-product team's five-month engineering practice is the wiki's first **end-to-end worked example** of the lifecycle running in production at vendor scale — though Lopopolo himself does not use the *ADLC* vocabulary:

| Lifecycle phase | What the Codex team built |
|---|---|
| **Build** | ARCHITECTURE.md, layered-domain Providers interface, custom linters (Codex-generated); progressive-disclosure AGENTS.md as table-of-contents to deeper sources |
| **Test** | Per-worktree observability stack (LogQL / PromQL / TraceQL); Chrome DevTools Protocol wired into runtime for UI validation; 100% test coverage |
| **Deploy** | gh + repository-as-system-of-record; per-worktree app instances; ephemeral local observability; "minimal blocking merge gates" |
| **Monitor** | Taste-invariant scans, golden-principle GC, doc-gardening agent — all event-driven hook-shaped |
| **Iterate** | Review feedback → doc updates → linter rules; "human taste captured once, then enforced continuously on every line of code" |
| **Govern** | Mechanical layer enforcement (forward-only dependency direction); single Providers interface for cross-cutting concerns (auth, telemetry, feature flags); "enforce boundaries centrally; allow autonomy locally" |

The Codex team substantiates the lifecycle as **a real engineering practice**, not just a marketing taxonomy. It also extends [[agentic-engineering]] with concrete operational data: 1,500 PRs in 5 months, 7 engineers, 3.5 PRs / engineer / day, throughput *increasing* with team size — built with **0 lines of manually-written code**.

## Worked example: AnswerThis at 2-FTE micro-scale ([[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg 2026]])

Where [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo]] is the vendor-scale worked example, [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg's YC Root Access talk]] is the **founder-vantage micro-scale worked example** — two FTEs, $2M ARR, an internal AI ops agent built on Claude Code CLI wrapped in Python. The lifecycle's phases are not named in Garg's vocabulary, but the same phases run; what makes the talk distinctive is that **the agent itself is the active maintainer of most of them**.

| Lifecycle phase | What the AnswerThis agent does |
|---|---|
| **Build** | Claude Code CLI wrapped in Python as harness; SaaS-tool CLIs (Intercom / Fathom / Stripe) as the initial tool layer; a **coding sub-agent exposed as a CLI** with edit-access to the main agent's code — the self-extending mechanism that has authored 45+ permanent CLIs to date |
| **Test** | Not formally articulated in the talk; the implicit feedback loop is human-in-the-loop in Slack (Ryan-the-non-technical-co-founder catches failures, messages the agent, agent rewrites its own rules) |
| **Deploy** | Cron job that refreshes the agent's read-only DB + codebase snapshot on every release; tools the coding sub-agent authors become permanent and available in future sessions |
| **Monitor** | The business itself becomes the monitor — *"what's the status of a lead? what are the open issues for customer X?"* are Slack queries to the agent rather than dashboard reads |
| **Iterate** | `instructions.md` loaded every turn, **agent-editable**; natural-language feedback in Slack → agent rewrites the file → next turn picks up the corrected behaviour. The *Ryan story* — *"the agent updated its own instruction set and tool link and then that entire class of mistakes stopped happening again"* — is the cleanest founder-scale instance of *iterate-via-natural-language-feedback* in the wiki |
| **Govern** | Single-team governance compressed into one Slack channel; co-founders are the only humans in the loop |

Garg's contribution to the lifecycle concept is the **agency dimension**: rather than humans operating each phase against an inert agent artifact, the agent is the active operator of Build (self-authored CLIs), Iterate (self-edited rules file), and partly Monitor (queryable business state). Humans retain Govern and the boundary of Test. The talk also names a clean **three-memory ontology** (factual = codebase+DB / behavioural = instructions.md / procedural = self-authored tools) that maps onto the lifecycle's persistence substrate — what the agent reads, what it follows, what it can do.

This makes the AnswerThis worked example a **smallest-end-of-scale data point** for the lifecycle's vendor-specificity-vs-genericness open question below: the same phases run at 2 FTE as at OpenAI Codex's 7-engineer team — strong evidence the construct generalises beyond vendor-specific formalisations.

## Open questions

- **Vendor-specificity vs. genericness**: now two formalizations (Google + LangChain). Whether other vendors (Anthropic, Microsoft, AWS) converge on similar phasings is unresolved. Watch for a third formalization in 2026 — three would be enough to consider this a *cross-vendor stable construct*.
- **Pre-stage work**: neither formalization names a *decide-to-build-an-agent* gate (cf. [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria's]] firm-boundary framework). Worth tracking whether subsequent formalizations include build-vs-buy-vs-compose gates.
- **Compounding loop / Telemetry-as-training-data**: Chase names it (*"Important traces become dataset examples"*); Google does not. Worth tracking whether more mature vendor / practitioner formalizations name the compounding loop explicitly. [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] Compounding layer is the strongest existing articulation; Chase's Monitor → Iterate loop is the second.
- **Agent governance as candidate concept**: Chase's six axes (cost / tool access / audit trails / HITL / discoverability / shared infrastructure) name an emerging concept currently single-source. Promote on second-source mention.
- **Simulation as evaluation primitive**: also single-source for now. Promote on second-source mention.
- **Promote or fold**: this concept is now substantiated enough to stand. Does it need any further sub-pages (e.g. *agent governance*, *agent evaluation*) or does it absorb them?

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "agent-development-lifecycle") OR contains(tags, "adlc")
SORT file.name ASC
```

## Debates and supersession

- **Stage count vs. phase count.** Google's 9-stage wheel and Chase's 4-phase loop describe the same lifecycle at different granularities. Neither supersedes the other — they are complementary vantages.
- **Does the Compounding loop deserve its own stage?** The wiki's [[agent-harness|agent-harness]] page names it as the fourth Chatterjee layer; Chase's Monitor + Iterate phases together cover it; Google's 9-stage wheel elides it. Open question: does it become a named stage in subsequent ADLC formalizations.
