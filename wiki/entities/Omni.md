---
type: entity
kind: product
aliases: ["Omni", "Omni Flash", "Gemini Omni"]
tags: [omni, multimodal, world-models, foundation-models, google-deepmind, gemini, generative-media, any-to-any]
since: 2026
confidence: 0.70
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 1
relationships:
  - type: part-of
    target: Google
    via: "Google DeepMind's single any-input-to-any-output multimodal model, launched at Google I/O 2026"
  - type: instance-of
    target: foundation-models
    via: "a single multimodal foundation model that replaces ~8 previously separate systems (text, audio, music, image, video)"
---

# Omni

[[Google DeepMind]]'s **single any-input → any-output multimodal model**, launched at Google I/O 2026 and described by [[Logan Kilpatrick]] in the [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Sequoia interview]]. Part of [[Google]].

## What it is

- **One model, not routing.** A *true* omni model that replaces ~8 previously separate systems Google trained — text (baseline Gemini), audio, music (Lyria), image (nano banana), and video (Veo). Kilpatrick stresses it is "not routing to a bunch of different models."
- **A "world model" by the blurring definition.** Demis Hassabis framed Omni as a world model for its level of world understanding; Kilpatrick notes the term *world model* is blurring from "action-conditioned video model" toward "a model with understanding of the world." An instance of the [[foundation-models]] trend toward consolidation.
- **First iteration = Omni Flash**, currently strongest at video editing (the real-time stage-edit "dog" demo); other modalities functional but not yet state-of-the-art.

A near-term implication on the wiki's radar: vibe-coded games will be **coding-agent + game-engine** based, *not* pure world-model-based, until world models gain the scaffolding to be grounded in reusable use cases.
