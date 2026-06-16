---
type: entity
kind: organization
aliases: ["Google DeepMind", "DeepMind", "GDM"]
tags: [google-deepmind, gdm, ai-lab, gemini, antigravity, omni, autoharness, foundation-models, agent-harness, world-models, demis-hassabis]
since: 2023
confidence: 0.75
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 2
relationships:
  - type: part-of
    target: Google
    via: "Google's consolidated AI research division (DeepMind + Google Brain merged 2023); 'the engine room of Google'"
  - type: employs
    target: Logan Kilpatrick
    via: "Kilpatrick leads Google AI Studio and the Gemini API at GDM"
  - type: published-by
    target: 2026-03-05-lou-deepmind-autoharness-code-harness-synthesis
    via: "AutoHarness authored by a Google DeepMind team (Lou, Lázaro-Gredilla, Murphy et al.)"
---

# Google DeepMind

Google's consolidated AI research division (the 2023 merger of DeepMind and Google Brain), described from the inside as **"the engine room of Google"** ([[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick 2026]]). It is part of [[Google]] and produces the Gemini model family, the [[Antigravity]] agent harness, and the [[Omni]] multimodal model.

## What the wiki holds on GDM

- **Harness synthesis research.** [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis|AutoHarness]] (Lou et al., March 2026) shows a small model (Gemini-2.5-Flash) automatically synthesizing a code harness — up to the *harness-as-policy* extreme where the LLM is not called at runtime. Mechanism-level evidence for the "model subsumes the harness" direction.
- **The "model eats the harness" thesis.** Articulated by [[Logan Kilpatrick]] in the [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Sequoia interview]]: the harness gets upstreamed into the model within ~12 months.
- **Antigravity + Omni.** [[Antigravity]] (from the Windsurf team) is the single agent harness now rebasing Google's products; [[Omni]] is the single any-input→any-output model replacing ~8 separate systems.
- **Culture.** Strong research portfolio under Demis Hassabis (Nobel laureate); explicitly non-zero-sum framing; deploying Gemini to billion-user products at a scale "only two companies in the world" can.

## Relationship to Google

GDM is the AI-lab role within [[Google]]; this wiki's broader Google footprint (Cloud, ADK, [[Google Research]]) is tracked on the [[Google]] page. GDM employs [[Logan Kilpatrick]] among ~100,000+ Google engineers who dogfood Gemini.
