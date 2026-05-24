---
type: concept
aliases: ["agentic engineering", "Agentic Engineering", "agentic-engineering", "agent engineering"]
tags: [agentic-engineering, vibe-coding, software-3.0, ai-agents, agent-harness, software-engineering, hiring, karpathy, codex-case-study]
confidence: 0.97
last_confirmed: "2026-05-22"
accessed_at: "2026-05-22"
source_count: 27
relationships:
  - type: depends-on
    target: agent-harness
    via: "agentic engineering's primary operational tool is the harness"
  - type: instance-of
    target: software-3.0
    via: "agentic engineering is the disciplined practice of writing Software 3.0 programs at production-quality bar"
  - type: contradicts
    target: vibe-coding
    via: "vibe coding raises the floor; agentic engineering preserves the ceiling — same artifact, opposite goal"
quality_score: 0.98
quality_notes: ['2 near-empty section(s)']
---

# Agentic Engineering

The **engineering discipline of writing software with AI agents that preserves the quality bar of professional software while going much faster**. Coined explicitly as a paired concept with [[vibe-coding]] by [[Andrej Karpathy]] in the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]] (29 April 2026): vibe coding *raises the floor* (everyone can vibe code anything); agentic engineering *raises the ceiling* (professional engineers can ship faster *without* sacrificing quality).

The construct's load-bearing claim: **"the 10× engineer used to be the upper bound; agentic engineering pushes far past 10×"** — implying the productivity distribution gets fatter-tailed, with agentic engineers at the top of it pulling significantly further away. The discipline's day-to-day artifacts are the [[agent-harness]] (the runtime), the spec (the design the human owns), and the agents (the *intern entities* that fill in the blanks).

### Practitioner-side ratification: "harness engineering" as the working-engineer naming

[[2026-05-15-osmani-agent-harness-engineering|Osmani's O'Reilly Radar essay]] (May 2026) introduces **"harness engineering"** as the working-engineer-altitude name for the same discipline Karpathy named *agentic engineering* at paradigm altitude. The wiki holds them as a paired vocabulary: **paradigm-level frame = agentic engineering (Karpathy)**; **practitioner-level discipline = harness engineering (Trivedy, Osmani)**. Osmani's load-bearing rule — **"every line in a good AGENTS.md should be traceable back to a specific thing that went wrong"** (*ratchet, don't brainstorm*) — is the operational test for what *preserves the quality bar at agent speed* actually looks like in a working codebase. The convergence observation Osmani names — *top coding agents (Claude Code, Cursor, Codex, Aider, Cline) look more like each other than their underlying models do* — is the empirical confirmation of agentic engineering's claim that the discipline is more load-bearing for outcomes than the model is.

## Working definition

[[Andrej Karpathy]] in the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]]:

> *"Agentic engineering when I call it that, because I do think it's kind of like an engineering discipline. You have these agents which are these spiky entities — they're a bit fable, a little bit stochastic, but they are extremely powerful. How do you coordinate them to go faster without sacrificing your quality bar? Doing that well and correctly is the realm of agentic engineering."*

**Key contrast with [[vibe-coding|vibe coding]]:**

| Dimension | [[vibe-coding\|Vibe coding]] | Agentic engineering |
|---|---|---|
| Effect on the productivity distribution | Raises the floor (everyone) | Raises the ceiling (professionals) |
| Trade-off | Speed and accessibility | **Speed *without* sacrificing quality** |
| Audience | Hobbyists, non-engineers, side-project builders | Production engineers |
| Karpathy's verdict on ceiling | "Amazing, incredible" — democratisation | *"People who are very good at this peak a lot more than 10×"* |
| Quality requirement | Not load-bearing | *"You're not allowed to introduce vulnerabilities. You're still responsible for your software just as before."* |

The wiki holds these as **two complementary modes of the same Software 3.0 substrate**, not opposites.

## Architectural relationship to other constructs

- **Substrate**: [[software-3.0]] — agentic engineering is the disciplined practice of writing Software 3.0 programs at production-quality bar. Vibe coding is the same substrate without the quality bar.
- **Operational vehicle**: [[agent-harness]] — the runtime that wraps the model with context management, constraints, contracts, and compounding telemetry. *Most of the day-to-day work of an agentic engineer is harness work* (per [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]).
- **Workforce**: [[ai-agents]] — *intern entities* (Karpathy's framing) that fill in the blanks once the human has specified the design.

The construct's sharpest single-line synthesis (across [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] + [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]):

> Agentic engineering is to the harness what software engineering is to the IDE — the discipline that uses the tooling to ship reliable systems.

[[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] names the *artifact* (the harness — what you build); [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]] names the *practice* (agentic engineering — what you do).

## Key claims

### The ceiling pushes far past 10×

> *"People used to talk about the 10× engineer previously. I think that this is magnified a lot more. 10× is not the speed-up you gain. People who are very good at this peak a lot more than 10×."* — [[Andrej Karpathy]]

The claim is structural, not just rhetorical: in a Software 3.0 paradigm, the engineer who can articulate a clean spec, structure an effective harness, design quality contracts, and review agent output skilfully **multiplies their leverage** in a way that the old "fast typist who knows the language" 10× engineer didn't.

### Humans own design; agents own fill-in-the-blanks

The vivid Karpathy debugging anecdote (his Menu Gen agent associating Stripe and Google accounts by *email match*):

> *"There wasn't a persistent user ID. It was trying to match up the email addresses, but you could use different emails for your Stripe and your Google and basically would not associate the funds. Why would you use email addresses to crossorelate the funds? They can be arbitrary."*

The architectural error (using non-persistent identifiers for cross-system reconciliation) is exactly the kind of thing a senior engineer catches in design review — and exactly the kind of thing an agent confidently produces and ships. The implication for the discipline:

- **Humans own**: aesthetics, judgment, taste, oversight, the spec/plan, the **architectural decisions** (*"these have to be unique user IDs"*).
- **Agents own**: the **fill-in-the-blanks** — API details, syntax variations (*"keep_dims vs keepdim, axis vs dim, reshape vs permute vs transpose — I don't remember this stuff anymore. You don't have to."*).

This is operationally consistent with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s *Constraints* layer (pre-tool / post-tool middleware that catches what intent the model is *actually* expressing). The Karpathy email-matching bug is a textbook case of a missing intent-validation hook.

### Spec-first, not plan-mode

> *"I actually don't even like the plan mode. I would, I mean, obviously it's very useful, but I think there's something more general here — work with your agent to design a spec that is very detailed and maybe basically the docs, and then get the agents to write them and you're in charge of the oversight and the top-level categories, but the agents are doing a lot of the under the hood."* — [[Andrej Karpathy]]

The substance: planning shouldn't be a *mode toggle in the UI* — it should be a **collaborative spec-design step that produces persistent docs the agent then implements against.** This is operationally close to what the wiki's [[agent-harness]] *Contracts* layer ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]) does: a formal evaluable specification of "successful output" calibrated to the inputs available. Karpathy's framing emphasises that **the spec is also the docs** — same artifact, different consumers.

### Tool mastery is the new craft

> *"I think it's just trying to get the most out of the tools that are available — utilising all of their features, investing into your own setup. Just like previously all the engineers used to basically getting the most out of the tools they use, either it's vim or VS Code or now it's Claude Code or Codex."* — [[Andrej Karpathy]]

Implication: a 2026 engineer's "tool stack" (Claude Code, Cursor, Codex, Anti-gravity, OpenCode, etc. — same model behind each; **different harnesses**) is the load-bearing skill. Per [[2026-05-04-rethinking-agents-harness-is-all-you-need|the empirical-anchor video]], the same model produces 6× variance across these tools — so tool selection and mastery is not a peripheral skill, it's central to the discipline.

### Hiring is still broken (and the proposed fix)

> *"What I'm seeing is that most people have still not refactored their hiring process for agentic engineering capability. If you're giving out puzzles to solve, this is still the old paradigm."* — [[Andrej Karpathy]]

Karpathy's proposed alternative interview format:

> *"Hiring has to look like 'give me a really big project and see someone implement that big project — let's write a Twitter clone for agents, make it really good, make it really secure, then have some agents simulate some activity, then I'm going to use 10 Codex 5.4× for X-high to try to break it. They should not be able to break it.'"*

The shape: **project-scale, build-and-defend, adversarial-test-by-agent-fleet.** This format directly tests the engineer's ability to:

- Specify a complex artifact at the right level of detail.
- Direct agents to fill in the blanks.
- Build constraints (per [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]'s harness Constraints layer) that hold under adversarial pressure.
- Review and reject low-quality agent output.

It is not testing what the old algorithm-puzzle interviews tested.

## Practitioner observations

### What good agentic engineers do differently

From [[Andrej Karpathy]]'s answer to *"how would you describe the difference between mediocre and AI-native coders"*:

- **Invest in their own setup**: tool configuration, custom skills, project templates, harness tuning.
- **Use all the features** of the tools (not just chat-completion mode; full agentic loops with tool-use, file-edit-with-diff, multi-file context).
- **Iterate on prompts and skills**: their CLAUDE.md / repo-level skill files are continuously refined.
- **Coordinate fleets**: per [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]] (Boris Cherny's 10–15 concurrent Claude instances), top operators are running parallel agents, not single sequential ones.

### What separates agentic engineering from "AI-assisted development"

The distinction is not about *how much* AI is used — it's about *who owns what*:

| Layer | AI-assisted development (older framing) | Agentic engineering (Karpathy 2026) |
|---|---|---|
| Specification | Human writes; AI helps polish | Human writes (collaboratively with agent); becomes the docs |
| Implementation | Human writes; AI suggests completions | Agent writes; human reviews and rejects |
| Code review | Human reviews other humans | Human reviews agent output; agent fleet reviews other agent output |
| Adversarial testing | QA team runs scenarios | Agent fleet attempts to break the artifact |
| Tool mastery | Optional sophistication | **Load-bearing** core skill |

## Convergence with other wiki sources

| Source | Construct | What it adds to agentic engineering |
|---|---|---|
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | 4-layer harness anatomy | The *artifact* the agentic engineer builds (Context / Constraints / Contracts / Compounding) |
| [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane 2026]] | "90% systems engineering rebranded" | The *primitive skills* an agentic engineer needs (retries, idempotency, observability, state machines) — Karpathy's "investing in your setup" implicitly assumes this background |
| [[2026-05-04-rethinking-agents-harness-is-all-you-need\|Empirical anchor video]] | Same-model 6× variance across harnesses | The *tool-mastery requirement* — your harness choice and tuning matters more than the model |
| [[2026-04-22-cheung-ippolito-secchi-google-agents-cli\|Google Agents CLI]] | 9-stage ADLC + 7 specialised skills | The *productisation* of agentic engineering as a vendor-published lifecycle toolkit |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic Managed Agents]] | Brain / hands / session decomposition | The *architectural pattern* for shipping agentic-engineered systems as products |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron-Schrage 2026]] | Verification → evaluation → learning capture | The *organisation-level analogue* of the agentic engineer's day-to-day flywheel |
| [[2026-05-07-ransbotham-augmented-learners\|Ransbotham et al. 2024]] | Augmented Learners 2×2 | The *empirical correlate*: agentic engineers are individual-level Augmented Learners — high org-learning capacity + high AI-specific learning |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung 2026]] | What running an AI-native engineering org *looks like operationally* — JIT planning, code-wins-over-whiteboard debate, three-signal dashboard, manager-starts-as-IC dogfooding, "Claudify everything", "explicit permission to kill processes" | The **inside-engineering vantage**: Karpathy named the discipline; Fung shows the team-norms rewrite that ships the 10×-plus product (Claude Code itself). First wiki source on the *org-shape* of agentic engineering at scale |
| [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex 2026]] | *0 manually-written lines, ~1M LOC in 5 months, 7 engineers, 3.5 PRs/engineer/day with throughput **increasing** as the team grew* — repository-as-system-of-record + AGENTS.md table-of-contents + layered-domain Providers + custom linters + golden-principles GC + doc-gardening agent | The **vendor-side production case study** at scale. Karpathy named the discipline; Fung described the org-shape; Lopopolo shows the artifact-shape inside one repo. Substantiates *"the discipline shows up more in the scaffolding rather than the code"* with five months of operational data |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler / Thoughtworks at QCon London 2026]] | Year-on-year practitioner review across many client engagements; explicit propagation of *harness engineering* as the discipline name (crediting the OpenAI Codex team); feed-forward × feedback × CPU-vs-GPU decomposition of the harness; *Goldilocks speed* counter-framing to speed-at-all-costs | The **practitioner-observer-from-consultancy vantage**. Karpathy named the discipline (paradigm); Fung described the org-shape (vendor team norms); Lopopolo showed the artifact-shape (one repo); Böckeler shows what the discipline looks like when *observed across many client codebases* — and confirms the discipline's name-form is settling on *harness engineering* in operator circles |
| [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs\|Thompson / NYT The Daily 2026]] | 75-developer cross-industry field-report; *"feel like Steve Jobs picking from nine designs"* operator self-description; Socratic-dialogue spec elicitation (agent interviews the developer); Manu Ebert's "10 Commandments" rules-file as small-startup analog of OpenAI Codex golden-principles; construction-workers-to-architects shift in operator vocabulary | The **journalist-observer vantage** on the discipline. Karpathy named it / Fung showed the org-shape / Lopopolo the artifact / Böckeler the consultancy view across many clients / Thompson reports what 75 working developers *say it feels like* in week-to-week practice. Confirms the discipline-shape from outside the practitioner community to a general (NYT) audience |
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu / Y Combinator Startup School 2026]] | *Software factories* as the next evolution of TDD — humans write specs and tests; agents generate implementation and iterate until tests pass; Strong DM as a worked example of a repo with no handwritten code; **the 1,000× engineer thesis** explicitly extending Karpathy's 10× by two orders of magnitude *"by surrounding a single engineer with a system of agents"*; **token-maxing not headcount-maxing** as the resource-allocation discipline | The **YC-accelerator-partner-observer vantage** on the discipline. Karpathy named the discipline (paradigm); Fung described the org-shape (vendor team norms); Lopopolo showed the artifact-shape (one repo); Böckeler the consultancy view across many clients; Thompson the journalist-observer 75-developer survey; Hu adds the **VC-portfolio-observer vantage** + names the productivity-ceiling explicitly (*"thousand or even 10,000× engineer is here"*). Strong DM is the wiki's second-vendor software-factory worked example (after OpenAI Codex), generalising Lopopolo's pattern beyond a single case |
| [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie / Braintrust 2025]] | The eval discipline — task / dataset / scores / experiments + offline-online-flywheel three-mode operation; *"evals as offense, not just defense"* reframing (Anker Goyal, Braintrust CEO); start-without-a-golden-dataset operator-advice; LLM-as-judge + code-based scoring families | the **eval-platform-vendor vantage** on what the agentic engineer's *Compounding* layer requires in production. Karpathy named the discipline; Guthrie supplies the *quality-bar-preservation mechanism* — evals are how agentic engineering maintains the quality bar at agent throughput. **Wiki's earliest formalised-eval-discipline anchor** (June 2025, ~9 months before the harness-cluster sources crystallised the discipline) |
| [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack\|Tan / Y Combinator (GStack) 2026]] | 10-15 parallel Claude Code sessions; ~400 PRs in review; *"10, 15, 20, sometimes 50 PRs in any given day, depending on the number of meetings I have"*; Yegge Gas Town stage 7 invoked explicitly (*"GStack does not get you to level 8, but I do think it gets you to level seven"*); ADHD-CEO-vs-autistic-CTO model-allocation framing (Opus 4.6 vs Codex) | the **founder-CEO operationalisation vantage**. Karpathy named the discipline; Fung showed the org-shape; Lopopolo the artifact; Böckeler the consultancy view; Thompson the journalist-survey; Hu the VC-portfolio-observer; Guthrie the eval-platform-vendor; **Tan is the worked example of Hu's *AI founder type* archetype at YC-president scale**. Two-source Yegge-Gas-Town threshold met (Böckeler + Tan) |
| [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era\|Chamath / Stanford AI Club 2026]] | 8090's *Software Factory*: humans + powerful models bound to engineering plans + work orders that operate in **forward pass** (intent → code) and **reverse pass** (dump tens-of-millions-of-lines of legacy code → propagate backwards to reconstruct English-language understanding); *"a control plane for AI"* sitting above the embedding space; *"PRDs and requirements are the hard-fought secrets that allow companies to be successful"* | the **enterprise-rebuild operationalisation vantage**. Where Lopopolo (OpenAI Codex), Hu (Strong DM), and Tan (GStack) operationalise agentic engineering at *new-codebase* or *startup-velocity* scale, Chamath operationalises it at the **brownfield-legacy-modernization** scale — the wiki's first **agentic-engineering case study at the enterprise-rebuild layer** (target sectors: healthcare, financial services, manufacturing, government). The *symbolic-space-above-the-embedding-space* construct generalises Karpathy's *"the spec is the design the human owns"* claim: at enterprise scale, the spec is the *entire institutional symbolic representation* — not just per-feature acceptance criteria, but the firm's complete legible logic |
| [[2026-05-13-jha-emergent-democratizing-app-building-with-claude\|Jha (Emergent CEO) interviewed by Carly Ryan (Anthropic Applied AI) 2026]] | Multi-agent orchestration on own Kubernetes-based container tech (disk + memory snapshotting for parallel agents); long-term memory **across user sessions** so the agent learns from every error / library upgrade seen platform-wide; pre-deploy + post-deploy security agents + refactoring agent; *index on highest reasoning, not speed* (Opus as workhorse; agents run for hours); *every-new-model-class-delete-and-reimagine* (system rewritten 4× in 9 months); *"agent is the product, the harness quality really really matters"* | the **founder-CEO outside-Anthropic counterpart to Fung's inside-Anthropic vantage**. Fung described the *team-norms rewrite* inside Claude Code that ships the 10×-plus product internally; Jha describes the *product-stack rewrite* outside that ships an analogous discipline to 7M users / 70–80% non-coders / $100M ARR in 8 months. Closes the loop: agentic-engineering as a discipline is now visible *both* as the internal-team practice that builds frontier AI products *and* as the external-company practice that builds AI-native customer products at scale. Same *delete-and-reimagine-against-each-new-model* operating cadence at both vantages |
| [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer\|Forsgren & Macvean / Google I/O 2026]] | **Five patterns of top AI-native engineers**: higher altitudes / shift-left-on-intent / designing-environments-not-vibe-coding / micro-teams / scientific-mindset. **Evolved T-shape** with four skill domains (core SWE + AI engagement + adjacent engineering + adjacent non-engineering). *"Our top engineers are **not** vibe coding."* *"Delegate tasks, not judgment."* DORA-grounded productivity-paradox + amplifier-and-mirror framings. Three-agent TensorFlow migration (planner / orchestrator / coder); code-review / shepherding / risk-assessor agent stack at fleet scale. **"Designing systems, not just bits of code."** | the **second inside-engineering vantage from a major AI lab** (Google ↔ Anthropic Fung-twin), with the corporate-research backing Fung's talk didn't have. Karpathy named the discipline; Fung described the org-shape inside Anthropic; **Forsgren/Macvean confirm the same operational model from Google with DORA's empirical backbone**. Independent ratification of the five-pattern shape within a fortnight of the Fung talk |
| [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself\|Garg / AnswerThis on YC Root Access 2026]] | **Agentic engineering at 2-FTE micro-scale** — $2M ARR with two full-time employees + 2–3 contractors, on an internal Claude-Code-CLI-wrapped-in-Python harness with read-only DB/codebase snapshots, SaaS-tool CLIs, a coding sub-agent that self-authors new CLIs on demand (45+ to date), and an agent-editable `instructions.md` ratcheted by Slack feedback. **Three-memory framework** named explicitly (factual / behavioural / procedural). Non-technical co-founder ratchets the agent's behaviour in chat — *"he just messaged the agent in Slack and told it what was wrong. The agent updated its own instruction set and tool link and then that entire class of mistakes stopped happening again."* | the **founder-vantage at startup-micro-scale operationalisation**. Karpathy named the discipline; Fung described it inside Anthropic; Forsgren/Macvean confirmed it at Google; Jha showed it at $100M-ARR Emergent scale; **Garg shows it at 2-FTE-startup scale** — the smallest end of the wiki's scale ladder for agentic engineering. The *self-extending CLI library* + *agent-edits-its-own-rules* loop are the cleanest founder-scale instance of Karpathy's *"investing in your setup"* and Osmani's *"ratchet, don't brainstorm"* operating in the same artifact |

## Operational invariants from the Codex case study

[[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]] surfaces a cluster of operational invariants worth naming as a checklist for agentic-engineering practice — distilled from the Codex team's five-month experience:

- **Repository-as-system-of-record.** *"From the agent's point of view, anything it can't access in-context while running effectively doesn't exist."* Every architectural rule, design decision, taste invariant, and acceptance criterion belongs in repo-local versioned markdown. Knowledge in Slack, docs, or people's heads is *illegible*.
- **AGENTS.md as table of contents, not encyclopedia.** Progressive disclosure: ~100-line top-level map with pointers to deeper sources, each with verification status, ownership, freshness checks, and mechanical lints. Monolithic instruction files fail predictably (context scarce / too much guidance becomes non-guidance / rots / hard to verify).
- **Layered architecture, mechanically enforced.** Forward-only dependency direction within domains; cross-cutting concerns route through one explicit interface (Lopopolo's Providers). Custom linters enforce. *"This is the kind of architecture you usually postpone until you have hundreds of engineers. With coding agents, it's an early prerequisite."*
- **Throughput inverts the merge philosophy.** Minimal blocking gates; PRs short-lived; flakes addressed with follow-up runs. *"In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive."*
- **Encode taste as mechanical rules, not Friday cleanups.** Human-taste corrections become either (a) doc updates the agent reads, or (b) custom lint rules the agent's commits must pass. *"Human taste is captured once, then enforced continuously on every line of code."*
- **Garbage-collection as background workload.** Codex replicates patterns including suboptimal ones; entropy creeps in. Background scheduled tasks scan for deviations and open targeted refactoring PRs, mostly auto-merged. *"Technical debt is like a high-interest loan: better to pay it down continuously."*
- **Make the application legible to the agent.** UI legibility (Chrome DevTools Protocol so Codex can take DOM snapshots / screenshots / validate UI behaviour); observability legibility (per-worktree LogQL/PromQL/TraceQL). The harder you make application-state legible, the more leverage the agent gets.
- **Hire for taste in environment design, not coding-puzzle speed.** *"Building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code."* Operationally consistent with [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's]] hiring-refactor argument.

These are not *additions* to Karpathy's discipline definition — they're the **operational instantiation** in one production environment. Other vendor case studies will likely vary specifics; the *invariants* (legibility, encoded taste, mechanically-enforced boundaries, GC-as-workload) are the candidates for cross-org generalization.

## The eval-discipline counterpart ([[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe 2026]])

[[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's *Agent Evaluation: A Detailed Guide*]] (Deep (Learning) Focus, 18 May 2026) is the wiki's first source whose primary contribution is the **eval-side counterpart** to the engineering-side rule-set above. Where [[2026-05-15-osmani-agent-harness-engineering|Osmani 2026]] gives *how to build the harness carefully* and [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]] gives *what production looks like*, Wolfe gives *how to measure whether the engineering actually works*. The 7-step roadmap (define success → small task set → useful tasks → ground truth → graders → eval harness → inspect-iterate-maintain) is the eval-side ratchet — *eval suites are living artifacts that continually improve in difficulty, diversity, and reliability*. The corollary closes the discipline loop: **agentic engineering without measurement is unmeasurable; agentic engineering with measurement compounds.** Wolfe explicitly recommends using the production scaffold as the eval scaffold — the same artifact serves both disciplines, which is what makes them mutually reinforcing rather than two separate efforts.

## Debates and supersession

- **Is "engineering discipline" the right framing, or is it just "advanced tool-use"?** Karpathy's claim is that it's a discipline; [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] would push back that 90% of it is mature systems engineering rebranded. Both can be true — the *discipline* is real *and* its primitives are mature systems engineering applied to a new substrate.
- **Does the 10× → "much more than 10×" ceiling claim hold under measurement?** The wiki has not yet ingested an empirical study of agentic-engineer productivity distributions. Worth tracking.
- **Is the multiplier conditional on existing skill, or unconditional?** [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu / Momentic 2026]] argues *"Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with"* — a direct rhetorical inversion of [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153 2026]]'s unconditional *1,000× engineer* framing. Filed as productive contradiction: both founders may be right at different conditionalities — Tan & Hu describe what *the best* engineer can now do unconditionally (the 5-day Posterous rebuild as worked example); Wu describes what *Codex deployed on the average engineer* produces. The wiki carries both anchors without resolving — adaptability, ambiguity-navigation, curiosity, and passion as meta-skills (Wu's framing) are not in tension with the unconditional-headline figure (Tan & Hu's framing) when the latter is read as *what the top of the distribution becomes capable of*.
- **Is the discipline transferable across domains?** Karpathy's worked examples are all coding (Menu Gen, Twitter-clone interview, micro-GPT). The discipline should generalise to non-code domains (research synthesis, data analysis, design) — but that hasn't been tested at scale yet in the wiki's source corpus.

## Related concepts

- [[software-3.0]] — the substrate; agentic engineering is the disciplined practice of writing Software 3.0 programs at production quality.
- [[vibe-coding]] — the floor-raising counterpart; same substrate, different goals.
- [[agent-harness]] — the operational vehicle of the discipline.
- [[ai-agents]] — the workforce (*intern entities*).
- [[jagged-frontier]] — agentic engineers must know which RL circuits their work is in (verifiable + labs-cared-about → fly; otherwise → struggle).
- [[foundation-models]] — the interpreter; "rented from a vendor whose competitor will outperform them within the year" per [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]; agentic engineering's value compounds across model upgrades.
- [[enterprise-ai-adoption]] — the organisational context in which agentic engineering becomes a hireable role.

## Open questions

- **Empirical measurement of the ceiling lift.** Karpathy's "much more than 10×" is rhetorical; a 2026–27 controlled study would settle whether it generalises.
- **Domain transfer.** Does agentic engineering as a discipline generalise to research synthesis, design, scientific work, etc., or is the coding-centric framing load-bearing?
- **Hiring-process refactor.** Karpathy says most companies haven't refactored hiring; if a second source documents companies that *have* (Anthropic? Cursor?), that's worth ingesting.
- **The aesthetics gap.** Karpathy specifically says current agent code is "bloaty, awkward abstractions, brittle." If this gap closes, do agentic engineers spend less time on review and more on spec/design? Worth tracking.
- **"Tool mastery is the new craft"** — does this generalise across model families, or is it specific to the current Claude Code / Cursor / Codex tool generation? If a tool-vendor consolidation happens (one wins, others fade), the "craft" specialises into mastery of one tool rather than navigation across many.
