# Eval-Driven Agent System — Build Blueprint

> A spec a coding agent can execute end-to-end to produce a working, production-grade eval system for an LLM agent. Adapted from the [Anthropic CWC `eval-driven-agent-development` workshop](https://github.com/anthropics/cwc-workshops/tree/main/eval-driven-agent-development) and grounded in two complementary talks: Anthropic's *"Evals for taste: Hill-climbing a slide-generation agent"* (Claude channel, 2026-05-22, [v9FTCvkV_a0](https://www.youtube.com/watch?v=v9FTCvkV_a0)) and Cline's *"Evals Are Broken Use Them Anyway"* (Ara Khan, DeepLearning.AI AI Dev '26 SF, [fAfuQN0WwFE](https://www.youtube.com/watch?v=fAfuQN0WwFE)).

> **Audience.** A coding agent (Claude Code / Cursor / Cline-style) that is reading this spec to scaffold a real eval system in someone else's codebase. The blueprint is therefore written as: *concept → contract → file → command → acceptance criterion*. Where it makes sense, the spec is **domain-agnostic** (any agent that produces an artefact you can grade); where domain anchoring helps clarity, it borrows the workshop's slide-generation example.

---

## 0. What you're building, in one paragraph

A repeatable, replayable, parallelised pipeline that (a) drives a *target agent* to produce artefacts against a fixed task set, (b) runs a *grader array* — cheap deterministic checks plus reasons-first LLM judges — against every artefact, (c) materialises a *scorecard* with deltas against a pinned baseline, (d) feeds the failure portfolio back into agent iteration as the inner loop, and (e) treats the evals themselves as a living artefact that can saturate, drift, or measure the wrong thing — so it ships with calibration discipline and exit ramps, not just numbers.

The system has three layers:

1. **The target agent** — what you're evaluating (e.g. a coding agent, a slide-generation agent, a shopping agent, a legal-summarisation agent).
2. **The eval harness** — the rig that drives the target, captures outputs, builds a per-task context once, runs every grader in parallel, and writes results.
3. **The iteration loop** — the human-in-the-loop discipline of reading failure portfolios, changing **one** lever (system prompt, tool surface, model, scaffold), and re-running to confirm the change moved the right needle.

The whole system is **eval-driven** in the same sense that TDD is test-driven: you do not change the agent without a numerical hypothesis about which grader should move, and you do not trust a change until the scorecard confirms it didn't silently regress something else.

---

## 1. The mental models you must encode (philosophy, not theatre)

The blueprint will fail if the coding agent ships boilerplate without these priors. Encode them as comments, doc strings, or assertions in the system itself.

### 1.1 Evals are the bridge from vibes to action

> *"Evals are the bridge between 'it seems to work' and 'we know it works'… vibes have their place but they're not actionable."* — Anthropic talk.

A vibes-only workflow ("model feels worse today") is a reactive loop: you only catch issues in production, you can't separate genuine feedback from noise, and you can't verify whether a fix improved or regressed the agent. Evals turn vibes into a delta against a pinned baseline.

**Encode as:** every change to the target agent ships with a paired `eval --baseline` run before the change and an `eval` run after; the PR description shows the diff.

### 1.2 But evals are **broken** — use them anyway

> *"Eelss are not the end-all and be-all… there are right ways to use them and there are wrong ways to use them."* — Cline talk.

Two failure modes to design against:

- **The objective-metrics camp** — treats benchmark scores as ground truth. Falls for **benchmark-max** model releases that score high but feel worse than predecessors.
- **The taste-king camp** — dismisses all numbers as noise; iterates purely on vibes; can't onboard new team members and can't migrate models without re-deriving the agent.

The blueprint is the middle path: numbers plus judgment, with explicit hooks for each.

### 1.3 Three things are under test at once

Cline's key insight, drilled into the blueprint as a tagging convention:

| Layer | What it is | Symptom of failure |
| --- | --- | --- |
| **Model** | The underlying LLM (Sonnet 4.6, Opus 4.7, DeepSeek V4, …) | Score gap closes on a smarter model with no other change |
| **Harness** | Your scaffolding: prompts, tools, retries, memory, sub-agents, error handling, context shape | Same model scores much higher in Claude Code than your agent — that's a harness gap |
| **Problem** | The eval task set plus grader rubric — the question you're asking | All graders score the run high but the artefact is obviously bad → the problem definition is wrong |

Every regression triage starts with: *which of the three?* Build that question into the failure-report template.

### 1.4 Hill-climbing has three zones

| Zone | What you're fixing | Risk |
| --- | --- | --- |
| **1 — Obvious flaws** | Tool that doesn't work, loop that doesn't terminate, prompt that contradicts itself | Low. Just fix them. |
| **2 — Philosophical hill-climb** | Prompt nuance, tool surface, retry logic, sub-agent design, model choice | Medium. This is where most real work lives — calibration matters. |
| **3 — Goodhart's danger zone** | Overfitting to the eval — adding skills/prompts that only pass the test set | High. Score goes up; real users notice nothing or feel worse. |

The system must surface zone-3 risk explicitly: a *held-out task set* the iterating engineer doesn't see day-to-day, and an *aggregate user-vibe check* (or held-out human-graded sample) before any model-ship decision.

### 1.5 Evals are a living artefact, not a fixed ruler

> *"It's not because you have set up your evals once that they are now the ground truth… evals over time, they need to be a living artifact… if you ever hear people talk about saturation of evals, that's what they mean."* — Anthropic talk.

Three lifecycle events you must support:

- **Saturation** — every model scores ≥0.95 on a grader; it stops discriminating. Action: retire or sharpen.
- **Calibration drift** — judge model scored a no-image deck 5/5 on the image judge. Action: rewrite rubric with anchored exemplars (see §6.4).
- **Domain drift** — the agent grew a new capability the eval set doesn't probe. Action: add tasks.

Encode as a quarterly `eval lint` operation (§9).

---

## 2. System architecture (the workshop's shape, generalised)

The workshop's directory layout is the right shape because it cleanly separates **agent definitions** (changeable), **task definitions** (mostly fixed), **grader definitions** (slowly evolving), **harness code** (rarely changes), and **outputs** (gitignored, per-run).

```
your-eval-system/
├── resources/
│   ├── environment.yaml           # Cloud / container spec for the target agent
│   └── agents/
│       ├── 00-naive.agent.yaml    # Iteration round 0 — baseline
│       ├── 01-typography.agent.yaml
│       ├── 02-qa-loop.agent.yaml
│       ├── 03-diagrams.agent.yaml
│       └── 04-opus-bare.agent.yaml
├── src/
│   ├── drive.ts                   # Drives the target agent on one task → artefact
│   ├── render.ts                  # (Optional) artefact → renderable form (e.g. PPTX → JPGs)
│   ├── parse.ts                   # Artefact → structural features for code-graders
│   ├── graders.ts                 # The grader array (code + judge)
│   ├── graders/
│   │   ├── types.ts               # Grader, GraderContext, ScoreCell types
│   │   ├── code/*.ts              # Deterministic checkers
│   │   └── judge/*.ts             # LLM-judge prompt builders
│   └── eval-runner.ts             # The harness: build ctx once, run graders in parallel, write scores
├── tasks.json                     # The fixed task set
├── tasks.held-out.json            # The held-out task set (do not look at during iteration)
├── runs/                          # Per-run outputs: artefacts + score.json + traces
│   └── <agent-id>/<task-id>/...
├── baselines/                     # Pinned reference scorecards
│   └── <agent-id>.json
├── reports/                       # Human-readable scorecards + failure portfolios
├── Dockerfile                     # Whatever the artefact needs to render/run (LibreOffice, Chromium, …)
├── package.json                   # Or pyproject.toml — the language is incidental
├── CLAUDE.md                      # Coding-agent-facing build & operation guide
├── README.md                      # Human-facing guide
└── .env.example                   # ANTHROPIC_API_KEY (and provider keys for multi-model)
```

**Why this shape works** (from the workshop's design):

- One artefact → one context object → many graders, all run in parallel against the same context. Rendering / parsing happens **once per artefact**, not once per grader, so adding the tenth grader costs almost nothing.
- Agent versions are YAML files, so iteration rounds are diff-able and revertable. `00-naive` is the baseline; subsequent versions encode one hypothesis each.
- The harness is the only file that knows about parallelism, retries, and scoring; graders are pure functions of context.

---

## 3. The contracts (what every file commits to)

A coding agent building this needs typed seams. Here is the minimum interface contract; reuse the workshop's TypeScript where you can, port to your language otherwise.

### 3.1 Task

```ts
// tasks.json — an array of these
type Task = {
  id: string;             // stable slug; appears as a column in scorecards
  prompt: string;         // the user-facing instruction handed to the agent
  context?: unknown;      // optional: files, URLs, prior state the agent needs
  tags?: string[];        // optional: domain / capability tags for slice analysis
};
```

The workshop's `tasks.json` (verbatim) — five prompts, each one sentence, each in a different domain (career, environment, food, social media, technology). This is deliberate: the task set spans the agent's intended domain coverage, so any single-domain regression is visible.

For a coding agent: keep tasks **short, specific, and independent**. A task should fit on one screen and not require a multi-task fixture.

### 3.2 GraderContext

The harness builds this **once per (agent_version, task)** pair and passes it to every grader:

```ts
type GraderContext = {
  taskId: string;
  agentId: string;
  agentVersion: string;
  rawArtifact: Buffer | string;     // the thing the agent produced
  parsedArtifact: ParsedArtefact;   // structural features (e.g. parsed PPTX, AST, JSON)
  rendered?: RenderedArtefact;      // optional: visual rendering for visual judges (JPGs, screenshots)
  sessionTrace: AgentTrace;         // tool calls, turns, tokens, latency, errors
  memo: Map<string, unknown>;       // memoised judge calls — share across graders
};

type AgentTrace = {
  turnCount: number;
  toolCalls: { name: string; durationMs: number; success: boolean }[];
  inputTokens: number;
  outputTokens: number;
  totalLatencyMs: number;
  errors: { kind: string; message: string }[];
};
```

The `sessionTrace` is the half of Cline's blueprint most builders skip: **turns / tool calls / tokens / latency / cost are graders too**, just cheaper ones. A model that scores high but takes 45 minutes per task is a different decision from one that scores the same in 90 seconds.

### 3.3 Grader

The workshop's exact shape (paraphrased verbatim from `src/graders.ts`):

```ts
type Grader = {
  name: string;                                // appears as column header
  kind: "code-grader" | "llm-judge";
  description: string;                         // one line — what does the column mean
  grade: (ctx: GraderContext) => Promise<ScoreCell>;
};

type ScoreCell = {
  value: number | string;                      // numeric (judges, counts) or label (status checks)
  detail?: unknown;                            // raw evidence, per-slide breakdowns, judge reasoning
  reasons?: string[];                          // for judges — MUST precede `value` in the prompt; see §6.3
};
```

**Two rules that the contract enforces, not the harness:**

1. Each grader must answer one question. If a grader can't articulate what action a low score should trigger, drop the grader. (*"If you have a grader that you get no useful information out of, you should not have that part of your eval."* — Anthropic talk.)
2. Each grader is a **pure function of context**. No I/O, no shared state. The harness owns parallelism.

### 3.4 The grader array

```ts
// src/graders.ts
import type { Grader } from "./graders/types.js";
import { producedResult } from "./graders/code/produced-result.js";
import { emojiCount } from "./graders/code/emoji-count.js";
// … etc

export const GRADERS: Grader[] = [
  producedResult,    // gate: did the agent produce anything?
  emojiCount,
  clutteredSlides,
  slideCount,
  smallFontSlides,
  textHeavySlides,
  // judges
  textJudge,
  imageJudge,
  layoutJudge,
  colorJudge,
  titleBodyCoherenceJudge,
];
```

**Ordering matters for the UI**, not the harness: the human reading a scorecard scans left to right, so put **gating checks first** (did the agent produce a parseable artefact?), then *cheap discriminators*, then *judges*. The harness runs them all in parallel anyway.

---

## 4. The grader catalogue (what to build, by kind)

### 4.1 Code-graders — fast, cheap, deterministic, **brittle**

Equivalent of unit tests. Use when the property is mechanically decidable.

Patterns from the workshop:

| Grader | Returns | Why |
| --- | --- | --- |
| `produced-result` | `"missing" \| "invalid" \| "ok"` | Gate — if this fails, downstream graders are noise |
| `slide-count` | integer | Did the agent follow the structural constraint (5 slides)? |
| `emoji-count` | integer | Frequency check — useful because LLMs love decorative emoji |
| `cluttered-slides` | integer (count of slides over a shape threshold) | Structural over-density |
| `small-font-slides` | integer | Readability constraint |
| `text-heavy-slides` | integer | "Avoid wall-of-text" constraint |

**Generalising for any agent:**

- *Did the artefact get produced and parse cleanly?* — always your zero-th grader.
- *Did the agent obey explicit structural constraints?* (file count, function names, schema fields, key presence).
- *Quantifiable surface properties* — token count, file size, lines of code, number of TODOs introduced, count of forbidden-pattern occurrences (e.g. stray `console.log` calls, the JavaScript dynamic-code-execution builtin, decorative emoji, debugger statements).
- *Tool-call shape* — did it call `read_file` 47 times in a loop? Surface from `sessionTrace`.
- *Resource budget* — turns, tool calls, tokens, latency, $cost (Cline's emphasis: these are first-class signals).

**Anti-pattern:** code-graders that try to encode taste. *"How readable is this code?"* is not a code-grader question — it has no deterministic answer. Move it to a judge.

### 4.2 LLM-judge graders — flexible, scalable, nuanced, **nondeterministic and uncalibrated by default**

Use when the property is judgement-laden.

Patterns from the workshop:

| Judge | Scale | What it scores |
| --- | --- | --- |
| `text-judge` | 0–5 | Is the title simple and clear? Is the body concise and on-message? |
| `image-judge` | 0–5 | Image quality and contextual fit |
| `layout-judge` | 0–5 | Spacing, alignment, hierarchy |
| `color-judge` | 0–5 | Contrast and accessibility |
| `title-body-coherence-judge` | 0–5 | Does each slide's body match its title? |

**Generalising for any agent:**

- *Quality* judges (text quality, design quality, code idiomaticity).
- *Coherence* judges (does part A say the same thing as part B?).
- *Safety / faithfulness* judges (does the legal summary actually match the cited case? — pair with a faithfulness rubric).
- *Pairwise comparison* — *"given outputs A and B, which is better and why?"* The Anthropic talk flags this as underrated: it sidesteps the calibration problem (the judge doesn't need an absolute scale, just a relative ranking) and lets you A/B variants directly.
- *Multi-judge consensus* — three independent judges, majority wins. Costs more, adds determinism, useful when a single judge swings wildly across runs.

### 4.3 Human graders — slow, expensive, **highest signal**

Reserve for: calibration of judges (§6), A/B spot checks before a model migration, and held-out sample audits. Do not put humans in the per-commit loop — they are the regression net, not the iteration loop.

---

## 5. The harness — `eval-runner.ts`

This is the file you almost never change. Its job:

1. **Select tasks** (`--all`, `--task <id>`, `--tag <tag>`).
2. **For each task**, drive the agent (`src/drive.ts`), get an artefact, persist to `runs/<agent-id>/<task-id>/`.
3. **Build context once**: parse, render, capture trace.
4. **Run graders in parallel** — `Promise.all(GRADERS.map((g) => g.grade(ctx)))`.
5. **Persist** to `score.json` (per task) and aggregate into `reports/<agent-id>.scorecard.md`.
6. **Compare to baseline** (`baselines/<agent-id>.json`) — colour deltas red/yellow/green.
7. **`--baseline` mode** writes the current scores as the new pinned baseline.

The harness uses `Promise.allSettled` at the task level (one task failure must not abort the others), and `Promise.all` at the grader level inside a task (graders share context and shouldn't outlive their sibling failures).

**Memoisation rule.** Inside one context, judge calls are memoised in `ctx.memo` keyed by `(judge_name, content_hash)`. Two judges that read the same rendered image share the model call. Across contexts, no memoisation — every (agent, task) pair gets fresh judges. The workshop's wording: *"The harness builds the context once per deck — parsed pptx, rendered JPGs, memoized judge calls — and runs every check against it."*

**Wall-clock contract.** Per the harness comment: *"Each task spawns its own render and parallel judge calls; total wall time is roughly max(per-task), not sum."* If you ship a harness that's serial-per-task, the iteration loop dies — engineers don't re-run 6-hour eval suites between commits.

**Containerisation for agentic evals** (Cline's emphasis): when tasks involve the agent installing dependencies, mutating a filesystem, or running shell commands, each task **must** run in its own container. Otherwise tasks pollute each other ("install a Python library" in task 3 changes the environment for task 7). Workshop uses Docker; Cline mentions Modal (https://modal.com) and Harbor as off-the-shelf substrates for parallel containerised eval workloads.

---

## 6. Calibration discipline (the part most builds skip)

This is where the inner loop meets the outer loop. A judge that gives a no-image deck a 5/5 on the image judge is worse than no judge — it creates false confidence.

### 6.1 Anchor every judge rubric with exemplars

The Anthropic talk's diagnosis: *"It has nothing to anchor on… it doesn't really know what good looks like, it doesn't know what bad looks like."* The fix: every judge prompt includes 1–3 short worked exemplars at the bottom of each score level.

Template:

```text
Score this {artefact} on {dimension} from 0–5.

Definitions:
- 0: <worked exemplar — what failure mode looks like>
- 2: <worked exemplar — middling>
- 5: <worked exemplar — ceiling>

First, list pros and cons of the artefact across {dimension}.
Then output your final integer score on a single line: `score: N`.
```

### 6.2 Multi-judge consensus when stakes are high

Three independent judges, majority wins. Apply when: ship/no-ship gates, model migrations, or when a single-judge variance is observed > 1 point across re-runs of the same artefact.

### 6.3 **Reasons-first, score-last** (load-bearing)

This is the single most important calibration rule in the Anthropic talk, restated as a quote:

> *"An LLM works autoregressively, right? So if it is anchored on this four, it will do anything it can to argue why it should be a four. Anything. And even if it's like extremely bad, if it should be like a one, it will still say 'oh it is good for these and these reasons' because it needs to justify the four that it put out. So how you do it is you actually turn it around. So first you say 'give me a bunch of reasons, give me pros, give me cons, give me reasons why it should be high, give me reasons why it should be bad.' And then based on all of those reasons together, then you need to make a final decision on the output."*

Encode this in the judge prompt template (§6.1 already does) **and** in the grader's `grade()` implementation: parse the reasoning block first, parse the score last, log both. If the score appears before the reasons in the model output, fail the grader with a calibration error rather than silently accepting an anchored number.

### 6.4 Calibrate against a human-graded sample, periodically

Pick ~20 artefacts at random per quarter. A human scores them on the same rubric. Compute judge-vs-human correlation per dimension. If correlation drops below ~0.6 for any dimension, the rubric needs rewriting — usually with sharper exemplars.

### 6.5 The "is this grader earning its place?" audit

For every grader, every quarter, answer: *what action have we taken in the last 90 days that was triggered by this grader's signal?* If "none" — either the grader is at ceiling (saturated, retire) or no one is reading it (delete). The corpus of graders should be ~10–15, not 50.

---

## 7. The iteration loop (the day-to-day workflow)

This is the workflow a coding agent or human engineer runs against the system, repeatedly.

### 7.1 Pin a baseline

```bash
npm run drive -- --all --agent 00-naive
npm run render -- --all
npm run eval -- --all --baseline
npm run show-baseline
```

The `00-naive` agent is deliberately under-prompted (the Anthropic talk's starter agent is literally *"You are a slide generation agent. When the user gives you a topic, create a powerpoint file at this location. You have a shell with python-pptx pre-installed."*). It sets the floor.

### 7.2 Form **one** hypothesis per iteration

From the workshop's iteration ladder:

| Round | Hypothesis | Lever changed |
| --- | --- | --- |
| 01 | "Typography rules will reduce font/density failures" | System-prompt: typography spec, anti-emoji guidance |
| 02 | "Forcing diagrams will improve image-judge score" | System-prompt: every slide must include a diagram |
| 03 | "A QA sub-agent will reduce structural failures" | Add critic loop — *"assume there are problems, approach QA as bug hunt not confirmation"* |
| 04 | "A smarter model dominates careful prompting" | Same naive prompt, swap Sonnet 4.6 → Opus 4.7 |

Round 04 is the most uncomfortable and most informative round: it tests whether the harness work you've done is *additive* on top of a stronger model, or whether the model swallows it. Build the system so this comparison is one YAML swap.

### 7.3 Run, diff, read the failure portfolio

```bash
npm run drive -- --all --agent 01-typography
npm run render -- --all
npm run eval -- --all
# scorecard renders with red/yellow/green deltas vs 00-naive baseline
```

The aggregate view answers *did anything regress?* The per-task failure portfolio answers *where, and which of model/harness/problem*.

### 7.4 Triage with Cline's three-question template

For every regression:

1. Is the failure a **model** issue? (Does a stronger model fix it without other changes?)
2. Is the failure a **harness** issue? (Same model in a different scaffolding works — your scaffolding is the gap.)
3. Is the failure a **problem** issue? (The grader is measuring the wrong thing, or the task is unrepresentative.)

Bucket each regression. Address one bucket at a time. Resist the urge to fix all three in one PR — you lose the signal about which fix worked.

### 7.5 Ship gate

A change ships when:

- No grader regressed by more than the noise floor (define per grader; usually `|Δ| ≥ 0.3` for 0–5 judges, `|Δ| ≥ 1` for counts).
- The held-out task set (`tasks.held-out.json`) shows the same direction of movement as the main set. If it doesn't, you may be overfitting — Cline's "zone 3 danger".
- A human spot-check on a sample of artefacts agrees, vibes-wise, with the score delta. If the score went up but a human prefers the old artefacts, your judges are miscalibrated — see §6.

---

## 8. The agent YAML — what changes between rounds

A round is one YAML file in `resources/agents/`. The diff is the entire hypothesis.

```yaml
# resources/agents/00-naive.agent.yaml
name: slide-gen-naive
model: claude-sonnet-4-6
system_prompt: |
  You are a slide generation agent. When the user gives you a topic,
  create a powerpoint file at /workspace/output.pptx. You have a shell
  with python-pptx pre-installed.
environment_id: <env-id-from-environment.yaml>
tools:
  - shell
```

```yaml
# resources/agents/01-typography.agent.yaml
name: slide-gen-typography
model: claude-sonnet-4-6
system_prompt: |
  You are a slide generation agent. When the user gives you a topic,
  create a powerpoint file at /workspace/output.pptx.

  Typography:
  - Slide title: 36–44pt
  - Section header: 28–32pt
  - Body: 18–22pt
  - Caption: 12–14pt

  Layout and density:
  - Keep body text concise; aim for ≤30 words per slide
  - Leave breathing room; left-align paragraphs
  - Five slides total

  Avoid AI-generated tells:
  - Never use thin accent lines in titles
  - Don't pepper slides with decorative emoji
  - Don't use placeholder text or filler bullets

  You have a shell with python-pptx pre-installed.
environment_id: <env-id-from-environment.yaml>
tools:
  - shell
```

Two principles:

- **One diff, one hypothesis.** If a round changes both prompt and model, you cannot attribute the score delta.
- **YAML is the spec.** Anything an engineer could change ad-hoc in a notebook must end up in YAML before it counts as a round.

---

## 9. Living-artefact maintenance — the `eval lint` operation

Run quarterly, or whenever the team smells drift.

```bash
npm run eval-lint
```

It produces a report with these sections:

- **Saturated graders.** Any grader where >90% of agent versions over the last 90 days scored >0.95 (or its kind-equivalent ceiling). Action: sharpen the rubric or retire.
- **Dead graders.** Any grader whose value has not influenced a code change in 90 days. Action: prune.
- **Drift candidates.** Judges whose human-correlation has dropped (§6.4). Action: rewrite rubric.
- **Task coverage gaps.** New capabilities the agent has gained (visible from `sessionTrace` — new tools used, new model swaps) that no task probes. Action: add task.
- **Held-out divergence.** Rounds where the main task set and held-out task set moved in opposite directions. Action: investigate overfit.

`eval-lint` does **not** mutate graders — it only reports. Pruning a grader is a human decision and a PR, because removing a grader retroactively changes the meaning of all historical baselines (§10.2).

---

## 10. Anti-patterns to refuse, with mitigations

### 10.1 The "single number" trap

A scorecard that collapses to one composite score hides regressions. The workshop's scorecard surface is a *table*: tasks × graders, with deltas. Keep it that way. Resist demands for a "headline number" — if you must publish one, publish the *count of red cells*, not a weighted mean.

### 10.2 The "edit graders mid-iteration" trap

If you rewrite a grader between baseline and current, the delta is meaningless. Rule: a grader change is its own commit; rebase the baseline (`eval --baseline`) immediately afterwards; do not mix grader edits with agent edits in the same PR.

### 10.3 The "judge before reasons" trap

See §6.3. The grader implementation must reject any judge output where the score precedes the reasoning. Don't trust the LLM to follow the rubric format — parse and assert.

### 10.4 The "vibes-or-numbers" false binary

Ship gate (§7.5) requires both: numerical non-regression *and* human vibe agreement on a sample. Either alone is insufficient; both together are stronger than either in isolation.

### 10.5 The "evaluate-the-evaluator-with-itself" trap

The judge model and the target model should differ — or, at minimum, the judge prompt and the target prompt should not share template scaffolding. Otherwise correlated errors cancel and the judge gives misleading high marks. When the same model is used for both, run a periodic calibration against a different family (e.g. judge with Claude when target is Claude, but also sample-judge with Gemini or GPT to detect shared blind spots).

### 10.6 The "Goodhart hill" trap (zone 3)

If a round's improvement comes from adding skills/prompts that are obviously eval-specific ("when the task mentions sourdough, …"), the held-out set will detect it. If you can't justify a prompt change in terms of a *general* capability the agent should have, don't make it.

---

## 11. Failure-portfolio template (the human-readable artefact of every run)

```
# Run 2026-05-25T14:31Z — agent: 02-qa-loop — baseline: 00-naive

## Aggregate

| grader            |  baseline | current | Δ      | verdict |
|-------------------|----------:|--------:|-------:|--------|
| produced-result   | 5/5 ok    | 5/5 ok  |        | ✓       |
| slide-count       | 5.0       | 5.0     |   0.0  | ✓       |
| emoji-count       | 20        |  0      | -20    | ✓ big   |
| cluttered-slides  |  3        |  0      |  -3    | ✓       |
| text-judge        | 3.2       | 4.4     |  +1.2  | ✓       |
| image-judge       | 2.8       | 4.4     |  +1.6  | ✓       |
| layout-judge      | 3.0       | 4.2     |  +1.2  | ✓       |
| color-judge       | 3.4       | 4.8     |  +1.4  | ✓       |
| coherence-judge   | 3.6       | 4.4     |  +0.8  | ✓       |
| turns (avg)       | 4.0       | 9.2     |  +5.2  | ! cost  |
| latency (avg)     | 38s       | 94s     | +56s   | ! cost  |
| cost (avg)        | $0.02     | $0.07   | +$0.05 | ! cost  |

## Per-task

### task: career
… (per-task slide-by-slide notes)

## Triage

- Quality up across the board.
- ! Cost regressed: QA loop adds turns + tokens. Decision: ship, but cap the loop at 2 iterations and re-measure.
- Held-out set: main movement direction confirmed. Not overfitting.
```

Make the cost-and-latency row first-class — Cline is emphatic that an agent that scores well but takes 45 minutes per task fails a real-world ship gate.

---

## 12. Multi-model and provider portability

Cline's talk underscores that the team beat Claude Code on Opus 4.5 evals by tuning the **harness** while the model was identical. The takeaway for the blueprint: the harness must be **model-agnostic**.

- The agent YAML names a model; the harness has no hard-coded model identifier.
- The judge prompts are pure strings — swappable across providers. Wire judges through a provider abstraction (`anthropic`, `openai`, `gemini`, `together`, `groq`) so a quarterly "judge cross-check" run is one CLI flag.
- The `sessionTrace` schema is provider-neutral: turns / tool calls / tokens / latency / errors are universal. The model-specific fields (anthropic cache tokens, openai logprobs) live in `sessionTrace.providerMeta`, never in the grader signature.

This is what lets you migrate from Sonnet 4.6 to Opus 4.7 with a YAML swap, or swap the underlying agent runtime (Claude Code → Cline → your own scaffolded loop) without rewriting graders.

---

## 13. The bootstrap checklist (what the coding agent does, in order)

Given a target agent and a domain, the coding agent executing this blueprint runs through:

1. **Scaffold directory layout** (§2). Add `.gitignore` for `runs/`, `node_modules/`, `.env`, and any vendor binaries.
2. **Draft the task set** — five tasks, one per intended sub-domain, short prompts, independent. Mirror to `tasks.held-out.json` with five fresh tasks the iterating engineer must not look at.
3. **Define the GraderContext type** (§3.2) — include the `sessionTrace` block. Wire `drive.ts` to populate it from whatever runtime drives the target agent.
4. **Write the gating code-grader** (`produced-result`) plus 3–5 cheap deterministic graders that match the domain's structural constraints.
5. **Write 3–5 judge prompts** with anchored exemplars (§6.1) and reasons-first ordering (§6.3). Memoise via `ctx.memo`.
6. **Write the harness** (`eval-runner.ts`) — task selection, parallel grader execution, baseline pin/diff, scorecard render.
7. **Containerise** if the agent runs shell or installs deps (§5). A `Dockerfile` plus per-task isolation.
8. **Wire `--baseline` and `--show-baseline`** flags. Pin `00-naive` as the floor.
9. **Build the failure-portfolio renderer** (§11) — markdown table with deltas, per-task drill-down, cost row.
10. **Draft `CLAUDE.md`** for the eval system itself — operating instructions for the next coding agent that touches it.
11. **First three iteration rounds**: typography / structure tighten → QA-loop sub-agent → model swap to stronger model. Stop and let a human read the deltas.

---

## 14. Acceptance criteria (how the coding agent knows it's done)

A working eval system passes all of these:

- [ ] `npm run drive -- --all --agent 00-naive && npm run render -- --all && npm run eval -- --all --baseline` runs end-to-end and writes a baseline.
- [ ] Re-running `npm run eval -- --all` against the same artefacts produces identical code-grader values and judge scores within ±0.2 (otherwise the system is too noisy — investigate seeds, judge temperature, parallelism races).
- [ ] Changing the agent YAML and re-running produces a diffed scorecard with red/yellow/green deltas vs baseline.
- [ ] Graders run in parallel; a single 10-task run completes in roughly `max(per-task)` wall-clock, not `sum(per-task)`.
- [ ] Removing a grader from `GRADERS` removes its column from the scorecard with no other code change.
- [ ] A judge whose output omits reasons before the score is rejected (calibration assertion).
- [ ] `runs/` is gitignored. `baselines/` is checked in. `reports/` is checked in for traceability of past runs.
- [ ] `CLAUDE.md` documents at least: how to add a task, how to add a grader, how to run the loop, how to interpret the failure portfolio, how to pin a new baseline, how to run `eval-lint`.
- [ ] A held-out task set exists and is referenced by name in the ship gate (§7.5).
- [ ] The first three iteration rounds (typography → QA loop → model swap) produce three distinct scorecards demonstrating the loop works.

When all ten boxes check, hand off to the human and stop. The next round is a human-judgement call: what hypothesis to test next.

---

## 15. Five lessons the system encodes (transferable beyond this blueprint)

These appear repeatedly across both talks and the workshop, and are worth pinning above the desk:

1. **"It's not what you measure, it's what you act on."** Every grader earns its place by triggering at least one decision per quarter. Otherwise prune.
2. **Reasons before scores. Always.** Autoregressive LLMs anchor on the first number they emit; reverse the order or you're measuring the model's appetite to justify, not the artefact's quality.
3. **Three things under test at once.** Model, harness, problem. Every regression starts with "which of the three?" Cline's contribution to the field.
4. **Evals are a living artefact.** They saturate, they drift, they go stale. Build the lint operation on day one or you'll discover this on month nine.
5. **The middle path between metrics-fundamentalism and vibes-fundamentalism is built, not assumed.** Ship gates require both numerical non-regression *and* human vibe agreement on a sample. The system makes both observable; the team makes the call.

---

## Appendix A — Source mapping

| Section | Anthropic talk (v9FTCvkV_a0) | Cline talk (fAfuQN0WwFE) | Workshop repo |
| --- | --- | --- | --- |
| §1.1 Vibes → action | [2:55–3:14], [4:59–6:35] | – | – |
| §1.2 Both camps wrong | – | [2:00–4:50] | – |
| §1.3 Three things under test | – | [19:18–20:20] | – |
| §1.4 Three improvement zones | [27:36–29:01] (QA loop = zone 1+2) | [21:11–23:30] | round folders in `resources/agents/` |
| §1.5 Living artefact / saturation | [20:48–21:32] | [8:51–9:35] | – |
| §2 Architecture | – | – | full `eval-driven-agent-development/` tree |
| §3 Contracts | – | – | `src/graders.ts`, `src/eval-runner.ts`, `src/graders/types.ts` |
| §4.1 Code-graders | [9:25–10:01], [17:34–18:11] | [13:18–15:00] (turns/tokens/latency/cost) | `src/graders.ts` code graders |
| §4.2 LLM-judges + pairwise + multi-judge | [10:01–12:13] | – | `src/graders.ts` judge graders |
| §5 Harness, parallel context | – | [15:35–17:20] (containerised parallel) | `src/eval-runner.ts` comments |
| §6.1 Anchored exemplars | [33:38–35:01] | – | – |
| §6.3 Reasons-first | [35:38–37:12] | – | – |
| §7.2 Iteration ladder | [21:38–32:13] (rounds 0–4) | – | `resources/agents/00..04` |
| §7.4 Triage template | – | [17:55–19:18] | – |
| §10.6 Goodhart zone 3 | – | [22:53–23:30] | – |
| §11 Failure portfolio | [25:01–27:30] (red/green deltas + cost) | [18:11–19:18] (failure portfolio aggregate) | scorecard table colour-coded |
| §12 Multi-model harness-agnosticism | [30:53–32:13] (Sonnet → Opus swap) | [19:33–20:20] (harness ≠ model) | `agent.yaml` model field |

## Appendix B — One-screen quick-reference

```
ROLE             FILE                              EDIT FREQUENCY
─────────────────────────────────────────────────────────────────
target spec      resources/agents/NN-*.agent.yaml  every iteration
task set         tasks.json                        rarely (additions only)
held-out tasks   tasks.held-out.json               rarely; never read during iteration
grader catalogue src/graders.ts                    occasionally — one PR per grader
grader internals src/graders/{code,judge}/*.ts     occasionally
harness          src/eval-runner.ts                almost never
context types    src/graders/types.ts              almost never
container        Dockerfile                        almost never
baselines        baselines/<agent>.json            after every accepted ship
reports          reports/<agent>-<ts>.md           every run (append-only)
runs             runs/<agent>/<task>/              gitignored
```

```
LOOP             COMMAND                                    EXPECTED OUTPUT
────────────────────────────────────────────────────────────────────────
drive            npm run drive -- --all --agent NN          artefact + sessionTrace
render           npm run render -- --all                    rendered artefacts (jpg, svg, …)
evaluate         npm run eval -- --all                      score.json + delta scorecard
baseline-pin     npm run eval -- --all --baseline           baselines/<agent>.json
inspect          npm run show-baseline                      pretty scorecard, no re-grading
lint             npm run eval-lint                          saturation / drift / coverage report
```

---

*Blueprint authored 2026-05-25 by [[index|the wiki]] from material in [[sources/2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|the Anthropic CWC slide-eval walkthrough]] and [[sources/2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Ara Khan's Cline talk]]. Workshop template: anthropics/cwc-workshops/eval-driven-agent-development.*
