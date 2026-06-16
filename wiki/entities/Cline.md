---
type: entity
kind: product
aliases: ["Cline", "cline.bot", "Claude Dev"]
tags: [cline, coding-agent, vs-code-extension, open-source, agent-harness, eval-discipline, terminal-bench, harbor, modal, beat-claude-code-opus-4-5, deepseek-v4-flash, multi-model-support, customer-of-model-vendor]
since: 2024
website: "https://cline.bot"
confidence: 0.78
last_confirmed: "2026-05-25"
accessed_at: "2026-05-25"
source_count: 5
relationships:
  - type: instance-of
    target: agent-harness
    via: "Cline is a named coding-agent harness — one of the *convergent* top coding agents Osmani identifies (alongside Claude Code, Cursor, Codex, Aider)"
  - type: employs
    target: Ara-Khan
    via: "leads Cline's eval-discipline programme; speaker at AI Dev 26 x SF"
---

# Cline

**Cline** is the open-source AI coding agent / VS Code extension, formerly named *Claude Dev*. **The wiki's first deeply-treated *customer-of-model-vendor coding-agent* entity** — Cline runs *on* model vendors' APIs (Anthropic, OpenAI, DeepSeek, etc.) rather than building its own foundation model, and competes directly with model-vendor reference agents like Claude Code, OpenAI Codex, and Cursor by **out-performing them on the same model via harness engineering**.

The wiki promotes Cline to an entity page on 25 May 2026 via the **cross-page-presence judgment** (same convention that produced [[Andrej Karpathy]], [[Jack Clark]], and [[Dalton Caldwell]]): Cline is referenced across 4 prior wiki pages plus the [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan / AI Dev 26 ingest]] (22 May 2026), which is a solo-headlining ingest of a Cline employee. The cross-page-presence judgment is appropriate because Cline is operating-system-installable software with a clear identity — naming it as an entity simplifies the wiki's coding-agent-vendor map.

## Why Cline matters for the wiki

Cline is the **canonical wiki anchor for the *customer-of-model-vendor coding-agent vendor* category**. The category sits between:

- **Model vendors with reference agents** ([[Anthropic]] / Claude Code, [[OpenAI]] / Codex, Google / Gemini CLI) — vertically integrated model + agent
- **Coding-agent vendors with proprietary stacks** ([[Cursor]] is the canonical example) — closed-source agent, often with custom model layers
- **Open-source coding-agent harnesses** (Cline, Aider, Open Code) — third-party harnesses runnable on multiple model vendors' APIs

Cline's competitive thesis (Khan / AI Dev 26): **harness engineering systematically beats vendor reference-agents on the vendor's own model**. The empirical anchor: *"We were able to beat Claude Code in Opus 4.5 evals"* on Stanford terminal-bench, *"we figured out some tiny knobs that they couldn't figure out or they didn't optimize for."*

## Sources under this entity

| Source | Vantage | Cline-specific contribution |
|---|---|---|
| [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway\|Khan / AI Dev 26]] (22 May 2026) | **Solo-headlining** ingest by Cline employee Ara Khan | Cline's eval-discipline programme; terminal-bench adoption; Harbor + Modal infrastructure; three-zones-of-improvement framework; **beat Claude Code on Opus 4.5 evals** anchor claim |
| [[2026-05-15-osmani-agent-harness-engineering\|Osmani / harness engineering]] (15 May 2026) | Cross-reference in the *convergence-of-top-coding-agents* observation | Named alongside Claude Code, Cursor, Codex, Aider as part of the convergent coding-agent set: *"they look more like each other than their underlying models do"* |
| [[2026-05-08-bratanic-unified-agentic-memory-hooks\|Bratanic / unified agentic memory]] (8 May 2026) | Cross-reference in the *built-in memory* comparison | Named alongside Cursor for built-in memory features that the *roll-your-own outside the harness* design contrasts with |
| [[concepts/agentic-engineering\|agentic-engineering]] concept page | Cross-reference in Osmani's convergence-observation framing | Confirmation of the *practice-is-more-load-bearing-than-the-model* thesis |
| [[concepts/agent-harness\|agent-harness]] concept page | Cross-reference in Osmani's convergence-observation framing | Same |

## Cline's eval-discipline programme (the Khan / AI Dev 26 anchor)

The most-load-bearing substantive content the wiki holds on Cline. Headline elements:

1. **Adopted Stanford terminal-bench** as the eval substrate — 89 problems at the real-software-engineering-task altitude (database issues, race conditions, frontend bugs, regex, latency, caching). Agents run 5-45 min per problem; deterministic unit-test grading.
2. **Used Harbor** (terminal-bench's containerised isolated-environment infrastructure) for parallel eval runs without cross-contamination.
3. **Used [[Modal]]** as the underlying infrastructure layer for parallel containerised eval environments.
4. **Tracked turns / tool calls / tokens / run-time** alongside pass/fail to enable cost-aware model selection.
5. **The three-things-being-tested framework**: model + harness + problem-space alignment. The harness-as-confounder observation: *"if a new model from Anthropic comes out, I guarantee you would have noticed that it works better in Claude Code compared to say Droid or Cursor sometimes. If it's the same model, why is it that it's much better in Claude Code than some other agent? That's basically what you're testing here."*
6. **The three-zones-of-improvement framework**: Zone 1 (obvious flaws — broken read-file tool, broken agent turns, broken checkpoints — fix first) → Zone 2 (real hill-climbing — too many tools, wrong tools, prompt engineering issues) → Zone 3 (danger zone — Goodhart-style overfitting to the metric).
7. **The Cline-beats-Claude-Code-on-Opus-4.5-evals headline claim**: *"We made changes to the CPU memory layer, raised timeouts, improved the thinking behavior... eventually we were able to beat Claude Code in Opus 4.5 evals. We found over time we're able to beat Claude Code in other evals as well, because we figured out some tiny knobs that they couldn't figure out or they didn't optimize for."* This is the **third independent primary-source confirmation** of the *harness-changes-alone-improve-eval-scores-substantially-on-the-same-model* pattern in the wiki (after [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain]] March 2026 and [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] 21 May 2026).
8. **Multi-model portfolio support**: Cline supports many open-source models alongside frontier models (DeepSeek V4 Flash explicitly named as a *"1/50th the cost"* alternative). Khan: *"We never would have figured out all these beautiful nuances of these open-source models which are incredible and much cheaper had we not run eval. We just would have completely ignored them and just worked on vibes."*

## Cline in the coding-agent convergence picture

Osmani's framing (*[[2026-05-15-osmani-agent-harness-engineering|harness engineering]]*, 15 May 2026): *"Look at the top coding agents side by side — Claude Code, Cursor, Codex, Aider, Cline — and they look more like each other than their underlying models do. The models are different. The harness patterns are converging."*

Cline's positioning within the convergent set:

- **vs Claude Code** ([[Anthropic]]'s reference agent): Cline runs on the same Anthropic models, with a third-party harness that Khan claims out-performs Claude Code on at least some Opus 4.5 evals. The vendor-vs-customer-of-vendor competitive tension is the most-pointed in the wiki's coding-agent landscape.
- **vs [[Cursor]]**: closed-source competitor; Khan references Cursor as an example of the *same-model-different-harness-different-results* observation.
- **vs Codex** ([[OpenAI]]'s reference agent): the OpenAI-side equivalent of Claude Code.
- **vs Aider**: open-source CLI-first coding agent; less surface area in the wiki than Cline at ingest time.
- **vs Open Code**: another open-source agent referenced in [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng / AI Dev 26]] as a coding-agent option.

## Origin / context

- **Founded 2024** as *Claude Dev* — initially a VS Code extension specifically for Claude. The rebrand to *Cline* coincided with multi-model support.
- **Open source** under permissive license; installable as a VS Code extension.
- **Multi-model support**: Anthropic (Sonnet, Opus), OpenAI (GPT-4, GPT-5, etc.), DeepSeek (V4 Flash named explicitly by Khan), open-source models.
- **Plan-act loop pattern** — Cline introduced *plan mode* / *act mode* as a default UX construct that has since been imitated by other coding agents.

## Open questions

- **Cline's revenue model** — VS Code extension is free; the monetisation surface (paid tiers, enterprise plans, hosted-Cline service) isn't detailed in the wiki's sources yet. Khan doesn't disclose this on stage.
- **Cline's team size + funding** — not disclosed in the wiki's sources. Khan implies a small team but doesn't name numbers.
- **The specific Opus 4.5 eval scores Cline cites for beating Claude Code** — Khan's claim is qualitative on stage; the specific terminal-bench task counts / pass rates that back the *beat Claude Code* anchor are not disclosed in the ingested talk. **Audit candidate**: a Cline blog post or terminal-bench leaderboard snapshot would substantiate this empirically.
- **Cline's relationship to terminal-bench / Stanford SAIL** — Khan describes adopting Stanford's terminal-bench as the canonical eval substrate. The wiki should track whether Cline contributes terminal-bench tasks upstream or is a pure consumer.

## Mentioned in

- [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway]] — substantive solo-headlining source: Khan's AI Dev 26 talk on Cline's eval-discipline programme.
- [[2026-05-15-osmani-agent-harness-engineering]] — cross-reference in the convergence-of-top-coding-agents framing.
- [[2026-05-08-bratanic-unified-agentic-memory-hooks]] — cross-reference in the built-in-memory comparison.
- [[concepts/agentic-engineering]] — cross-reference in the convergence-of-top-coding-agents framing.
- [[concepts/agent-harness]] — cross-reference in the convergence-of-top-coding-agents framing.
