---
type: entity
kind: product
aliases: ["Antigravity", "Anti-gravity", "Google Antigravity"]
tags: [antigravity, agent-harness, google-deepmind, gemini, windsurf, ide, cli, agent-sdk, vibe-coding, through-line]
since: 2026
confidence: 0.72
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 2
relationships:
  - type: part-of
    target: Google
    via: "Google's agent harness, built by the Windsurf team that joined Google; powers search, the Gemini app, Cloud, and AI Studio"
  - type: instance-of
    target: agent-harness
    via: "Antigravity is a concrete agent harness — an ecosystem of IDE, web agent surface, CLI, SDK, and a Gemini-API managed agent"
---

# Antigravity

Google's **single agent harness**, built by the **Windsurf** team that joined Google. Per [[Logan Kilpatrick]] in the [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Sequoia interview]], it is "a lot of things" — a core IDE, an agent-first web surface, a CLI, an SDK, and a managed agent available through the Gemini API — designed to "meet developers wherever they are."

## Why it matters to the wiki

- **The new through line for Google.** The *same* Antigravity harness powers search, the Gemini app, [[Google]] Cloud, and AI Studio — taking over the connective-tissue role that the Gemini *model/API* used to play across Google's ~50 products. A concrete instance of the [[agent-harness]] concept at hyperscaler scale.
- **Coding harness → general-purpose harness.** Kilpatrick: "coding has proved to be the general-purpose agent harness." ~80% shared base, specialized per use case (vibe coding vs. a 24/7 consumer agent).
- **Already in the corpus.** Named ("Anti-gravity") alongside Claude Code, Cursor, and OpenCode in [[2026-05-04-rethinking-agents-harness-is-all-you-need]] as one of the harnesses that drives same-model performance variance.

Built within [[Google DeepMind]]; the *model-eats-the-harness* tension (Kilpatrick's own thesis) applies to Antigravity as much as to any harness.
