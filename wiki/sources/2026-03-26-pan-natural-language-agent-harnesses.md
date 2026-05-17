---
type: source
kind: paper
title: "Natural-Language Agent Harnesses"
author: ["Linyue Pan", "Lexiao Zou", "Shuo Guo", "Jingchen Ni", "Hai-Tao Zheng"]
affiliations: ["Tsinghua University (Shenzhen International Graduate School)", "Harbin Institute of Technology (Shenzhen)"]
correspondence: "Hai-Tao Zheng <zheng.haitao@sz.tsinghua.edu.cn>; Linyue Pan <ply24@mails.tsinghua.edu.cn>"
arxiv_id: "2603.25723v1"
url: "https://arxiv.org/abs/2603.25723"
publisher: "arXiv (cs.CL preprint)"
date_published: 2026-03-26
date_ingested: 2026-05-17
length: "12 pages of main text + appendices; read in full"
raw: "../../raw/papers/01_Pan_Natural-Language-Agent-Harnesses_arxiv-2603.25723.pdf"
tags: [agent-harness, harness-engineering, natural-language-harness, intelligent-harness-runtime, IHR, NLAH, swe-bench-verified, osworld, os-symphony, trae, live-swe-agent, ablation-results, verifier-hurts, file-backed-state, contracts-runtime-charter, code-to-text-migration, tsinghua]
relationships:
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "Pan's NLAH (p, G, K, M)-equivalent formulation predates Karten's (p, G, K, M) formal definition by ~6 weeks and covers the same architectural layer from a different vantage (coding + computer-use benchmarks vs Pokémon embodied)"
  - type: supports
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "Pan articulates the harness *representation* (NLAH as portable executable artifact); Lee searches over harness *content* (Meta-Harness as outer-loop optimisation). Complementary — Pan asks 'what should a harness look like?', Lee asks 'how do we find a good one automatically?'"
  - type: supports
    target: 2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering
    via: "primary-source anchor for the PY video's two named results: the 14×-compute-reduction at equivalent SWE-bench pass rate (Pan's Table 1) and the OS-Symphony NL-migration 30.4% → 47.2% (Pan's Table 5)"
  - type: contradicts
    target: 2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering
    via: "PY's description claims 'Module-by-module ablation revealed that adding a Verifier actually hurt performance (-8.4 on OSWorld)' as a Pan et al. result. Pan's Table 3 confirms Verifier −8.4 on OSWorld — but the result is **Δ from a Basic OS-Symphony baseline of 41.7**, not −8.4 absolute. The magnitude is correct as a delta; PY's compressed paraphrase elides the baseline. Also: PY attributes the *Top 30 → Top 5 TerminalBench* result to Pan; **this claim is not in Pan's paper** — closer review suggests it is a LangChain-source result that secondary summaries have conflated with Pan."
  - type: supports
    target: 2026-05-07-kokane-agent-harness-vs-systems-design
    via: "Pan's runtime-charter / harness-skill / runtime-skill three-layer decomposition maps to Kokane's 7-block stack; the empirical ablations make the boundary-mediation point Kokane argued rhetorically"
  - type: uses
    target: agent-harness
---

# Pan, Zou, Guo, Ni, Zheng — *Natural-Language Agent Harnesses*

A **12-page arXiv preprint** (cs.CL, **2603.25723v1**, 26 March 2026) by **Linyue Pan**, **Lexiao Zou**, **Shuo Guo**, **Jingchen Ni**, and **Hai-Tao Zheng** (corresponding) at **Tsinghua University Shenzhen International Graduate School** and **Harbin Institute of Technology (Shenzhen)**. **The wiki's first peer-track academic primary-source on agent-harness *representation*** — the question of *what form a harness should take* (code vs natural language) and what becomes possible when it is treated as a first-class portable artifact. Together with [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al. (Meta-Harness)]] and [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al. (Continual Harness)]], Pan et al. forms the **March-May 2026 academic-anchor triple** for the harness-engineering construct the wiki has been triangulating from practitioner sources since late April 2026.

The wiki has been carrying Pan et al. as an *identification open-question* since 2026-05-04 (cited second-hand by [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]]) — closed yesterday by the [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video description]] which named the arxiv ID. **This is now the primary-source ingest**, which substantiates, corrects, and extends the second-hand reads the wiki has been operating on.

## TL;DR

- **The thesis.** *"Agent performance increasingly depends on harness engineering, yet harness design is usually buried in controller code and runtime-specific conventions, making it hard to transfer, compare, and study as a scientific object."* Pan et al. **lift the high-level control logic of an agent harness out of code into editable natural language**, treating the resulting NLAH as a portable executable artifact under a shared **Intelligent Harness Runtime (IHR)**.
- **The architectural separation.** A harness specifies **(i) control** (how work is decomposed and scheduled), **(ii) contracts** (what artifacts must be produced, what gates must be satisfied, when the run should stop), and **(iii) state** (what must persist across steps, branches, and delegated workers). NLAH carries this; IHR interprets it. The boundary between *harness* and *runtime* is "analytical rather than absolute" — generic services (tool adapters, sandboxing, child lifecycle) live in the runtime; task-family policy (stages, artifact contracts, verifiers) lives in the harness.
- **NLAH representation ingredients** (the five components every NLAH must expose to be executable):
  1. **Contracts** — required inputs and outputs, format constraints, validation gates, permission boundaries, retry and stop rules.
  2. **Roles** — role prompts (solver, verifier, researcher, orchestrator) with non-overlapping responsibilities.
  3. **Stage structure** — explicit workload topology (e.g., plan → execute → verify → repair).
  4. **Adapters and scripts** — named hooks for deterministic actions (tests, verifiers, retrieval, parsing).
  5. **State semantics** — what persists across steps (artifacts, ledgers, child workspaces) and how it is reopened (paths, manifests).
  6. *Plus* **failure taxonomy** — named failure modes that drive recovery (missing artifact, wrong path, verifier failure, tool error, timeout).
- **File-backed state as the load-bearing module.** Long-horizon autonomy fails in practice when critical state remains implicit or ephemeral. The file-backed state module enforces three properties: **externalized** (state written to artifacts), **path-addressable** (later stages reopen the exact object by path), **compaction-stable** (state survives truncation, restart, delegation). This is the wiki's first source on *path-addressability as a formal harness requirement*.
- **Three research questions, all empirically answered:**
  - **RQ1 (Behavioral Effect)** — Under fixed budgets, do the shared runtime charter and benchmark-specific harness logic change agent behavior and task outcomes? **Yes — but mostly on trajectory metrics (tokens, calls, runtime), not on resolved rate.** On SWE-bench Verified with TRAE, Full IHR achieves 74.4 vs w/o RTS 76.0 vs w/o HS 75.2 — *the runtime charter and harness logic produce much larger changes in tokens, calls, and runtime than in resolved rate.* **The runtime charter plus harness logic are behaviorally real controls rather than prompt decoration.** More than 110 of 125 stitched SWE samples agree between Full IHR and each ablation — the meaningful differences concentrate in a small frontier of component-sensitive cases.
  - **RQ2 (Composability)** — Once patterns are explicit, can modules be composed and ablated at the pattern level? **Yes, but module effects concentrate on a solved frontier rather than shifting the whole benchmark uniformly.** Three qualitative families: **self-evolution** improves end-task performance (the clearest example, e.g., +4.7 on SWE), **file-backed state and evidence-backed answering** mainly improve process structure / auditability without improving raw scores (Table 3: +1.6/+5.5), and **verifier / multi-candidate search / dynamic orchestration** can *hurt* on some benchmarks (Verifier −8.4 on OSWorld). ***RQ2 does not support a simple "more structure is always better" story.***
  - **RQ3 (Code-to-text migration)** — What differences remain between native code harnesses and reconstructed NLAHs under a shared runtime? **OS-Symphony NLAH = 47.2% on OSWorld vs Code = 30.4% — +16.8 points from migration alone**, with most of the gain coming from **relocation of reliability mechanisms from local screen repair to durable runtime state and artifact-backed closure**. Code paths use 11.4M prompt tokens / 651 tool calls / 1.2k LLM calls / 361.5 min runtime; NLAH uses 15.7M / 683 / 34 / 140.8 min — NLAH uses **34× fewer LLM calls** at the same task family for **2.5× lower wall-clock time**.
- **The 14× compute reduction at equivalent SWE-bench pass rate** ([[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering|PY video]] cited this) lands as: **TRAE w/o HS = 1.2M prompt tokens / 13.6k completion / 51.1 tool calls / 34.0 LLM calls / 6.7 min** vs **Full IHR TRAE = 16.3M / 211k / 642.6 / 414.3 / 32.5 min**, both at ~75% resolved rate. *The bloated full-IHR version burns ~13.5× more prompt tokens and ~15× more completion tokens for the same pass rate.* The "14×" PY claim is approximately correct.
- **The "more informative failures are alignment failures rather than random misses."** On `matplotlib__matplotlib-24570`, TRAE Full expands into a large candidate search and ends with a locally plausible patch that misses the official evaluator. Live-SWE exposes the lighter analogue on `django__django-14404`, `sympy__sympy-23950`, where extra structure makes the run more expensive while drifting from the shortest benchmark-aligned repair path. **These failures matter because they show not that the harness is inert, but that it can reshape local success signals in ways that do not always align with benchmark acceptance.**

## Why the wiki should re-attribute one prior claim

The wiki has been carrying the **"LangChain jumped from outside the Top 30 to rank 5 on TerminalBench 2.0 by changing only harness infrastructure"** claim as a Pan-et-al-attributed result (per the PY video description). **This claim is not in Pan et al.** Pan does not evaluate on TerminalBench-2 or rank harnesses against a leaderboard. The likely source is the [[2026-02-17-langchain-improving-deep-agents-harness-engineering|LangChain *Improving Deep Agents with Harness Engineering*]] blog post (Feb 2026), or possibly [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al.]] who *do* report TerminalBench-2 rankings (Meta-Harness #2 among Opus 4.6 agents at 76.4%, #1 among Haiku 4.5 agents at 37.6%). **The Top 30 → Top 5 specific framing is most likely a LangChain-post claim that secondary summaries have conflated with Pan.** Worth correcting in [[concepts/agent-harness]].

## What was actually ingested

Full 12-page PDF (sections 1-6 main text + appendices referenced; appendices A-E mentioned in body but not extracted in this batch — the load-bearing tables 1-5 are in the main text). All four named experiments (TRAE / Live-SWE on SWE-Verified; OS-Symphony on OSWorld code/NLAH). All three RQs.

**Experimental setup.** All experiments use the same IHR instantiation: **Codex CLI version 0.114.0, model GPT-5.4 ([[OpenAI]] 2026b), reasoning effort `xhigh`**. Ubuntu 24.04 servers with 64 CPU cores and 251 GiB memory; runs execute in Docker containers (32 vCPU / 84 GiB / 40 GiB storage per task). Subsets of 125 SWE-bench Verified samples and 36 OSWorld samples — *budget-limited; plan to rerun with GPT-5.4-mini.*

## Cross-positioning with the wiki

### Closes / re-attributes wiki open questions

| Wiki claim (status before this ingest) | Status after |
|---|---|
| **Verifier hurts on OSWorld by -8.4** (carried second-hand since [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering YouTube]]) | **Closed — verified.** Pan Table 3: OSWorld Verifier 33.3, vs Basic OSWorld 41.7. Magnitude (−8.4) is the Δ from Basic baseline, not absolute. The mechanism Pan articulates: *"verifier adds a genuine independent checking layer, yet failures such as `sympy__sympy-23950` show that verifier-level acceptance can still diverge from benchmark-level acceptance"* (RQ2 discussion). |
| **OS-Symphony NL migration 30.4% → 47.2%** | **Closed — verified.** Pan Table 5: identical figures. Mechanism: *"runs materialize task files, ledgers, and explicit artifacts, and they switch more readily from brittle GUI repair to file, shell, or package-level operations when those operations provide a stronger completion certificate."* |
| **14× compute reduction at equivalent SWE-bench pass rate** | **Closed — verified.** Pan Table 1 (TRAE w/o HS vs Full IHR): ~13.5× prompt-token reduction, ~15× completion-token reduction, ~12× tool-call reduction, ~12× LLM-call reduction, ~5× runtime reduction at 75.2 vs 74.4% performance. |
| ***"LangChain Top 30 → Top 5 on TerminalBench 2.0"*** **attributed to Pan et al.** | **Re-attributed.** Not in Pan's paper. Likely [[2026-02-17-langchain-improving-deep-agents-harness-engineering|LangChain (Feb 2026)]] or [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al.]] paper. PY video description conflated the two. |

### Maps onto the harness construct

Pan's NLAH ingredients map onto the wiki's existing harness vocabulary:

| Pan's NLAH component | Wiki harness layer |
|---|---|
| Contracts (inputs, outputs, gates, retries) | [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee]] **Contracts** layer; [[2026-05-11-karten-zhang-continual-harness-online-adaptation\|Karten]]'s implicit gates in the Refiner |
| Roles (solver, verifier, orchestrator) | Karten's *G* (sub-agents); [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands\|Anthropic]] brain / hands / session |
| Stage structure (plan → execute → verify → repair) | [[2026-05-09-chase-agent-development-lifecycle\|Chase ADLC]] phase model at task-instance scope |
| Adapters and scripts (named hooks) | [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic hooks]] applied to deterministic actions |
| State semantics (artifacts, ledgers) | Karten *M* (memory); [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo]] repository-as-system-of-record |
| Failure taxonomy | New addition — the wiki has carried Karten's failure-signature concept but not a *named taxonomy*. Pan elevates it to a first-class harness ingredient. |

### Adjacent contradiction with Karten et al.

[[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al.]] argue for **reset-free in-episode refinement**; Pan et al. operate under **per-instance budgets without refinement** (the harness is fixed for a run). Both are valid regimes for different task structures — Karten optimises for long-horizon embodied tasks where resets are costly; Pan ablates the harness as a fixed artifact at task-family scope. The two frame **harness as a learnable object** (Karten) vs **harness as a portable scientific object** (Pan). Neither contradicts the other; together they bracket the harness construct from both directions.

## Named entities (this ingest)

- [[Linyue Pan]], [[Lexiao Zou]], [[Shuo Guo]], [[Jingchen Ni]], [[Hai-Tao Zheng]] — Tsinghua + Harbin Institute of Technology (Shenzhen). **All first mentions. Dangling.**
- [[Tsinghua University]] — first wiki source from Tsinghua. **Dangling pending second source.**
- [[Harbin Institute of Technology (Shenzhen)]] — first mention. **Dangling.**

Plus reference-list entities (not new ingest targets): Anthropic (already in wiki), OpenAI (already), LangChain (already), AGENTS.md spec (already tracked).

## Source-quality notes

- **Genre**: arXiv preprint (cs.CL), pre-publication. Tsinghua + HITSZ academic affiliations.
- **Empirical-anchor count**: high — three RQs × multiple ablation conditions × two benchmark families (SWE-Verified, OSWorld) × two harness families per benchmark (TRAE/Live-SWE on coding; OS-Symphony on computer-use). Subsets (125/36 samples) due to budget constraints, with a planned rerun on cheaper model.
- **Open-source posture**: not explicitly stated; the IHR runtime and shared runtime skill are described as research artifacts but no public repo link in the body.
- **Confidence: 0.85.** Per Lifecycle: single source +0.05 for academic primary-source +0.05 for honest negative-result reporting (Verifier hurts on OSWorld; multi-candidate search is overhead-heavy; module effects concentrate on a frontier rather than shifting the whole benchmark) = 0.85. Will rise to 0.90+ on second-source corroboration or peer-reviewed publication.

## Open questions

- **The Top 30 → Top 5 LangChain attribution.** Worth verifying directly against the [[2026-02-17-langchain-improving-deep-agents-harness-engineering|LangChain *Improving Deep Agents with Harness Engineering*]] post (also being ingested in this batch).
- **Module-level effects on a richer task mix.** Pan's 125 SWE / 36 OSWorld subsets are budget-limited. The pattern that *more structure is not always better* might invert on harder task distributions where multi-candidate search and verifiers earn their cost.
- **The "alignment failure vs random miss" distinction.** Pan flags this as the most informative class of failures. Worth tracking against future ablation work whether harness-induced "alignment failures" can be detected and corrected in-loop (Karten's Refiner) vs only post-hoc.
- **Transfer of NLAHs across runtimes.** Pan demonstrates NLAH portability *within* IHR but not *across* runtimes. The promise of "natural language as a portable carrier" needs at least one cross-runtime test (NLAH evaluated on a non-IHR substrate).
