---
type: entity
kind: organization
aliases: ["METR", "Model Evaluation and Threat Research"]
tags: [metr, ai-evaluation, ai-benchmarks, ai-safety]
confidence: 0.70
last_confirmed: "2026-04-28"
accessed_at: "2026-04-28"
source_count: 1
---

# METR

A research organization that builds AI evaluations, focused on **task horizons** — the length of time over which AI models can successfully complete tasks.

## Why it appears in this wiki

METR's task-horizon benchmark is referenced in [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic's fourth Economic Index report]] as a complementary measure of AI capability:

- Benchmark: a fixed task set spanning varied human-time durations.
- Metric: the duration at which an AI model achieves 50% success.
- For [[Claude Sonnet 4.5]]: METR reports ~2 hours.

The Anthropic report's own data, computed differently, finds Claude Sonnet 4.5 reaches 50% success at ~3.5 hours (1P API) and ~19 hours (Claude.ai). Methodology differences (selection bias on Claude.ai, task decomposition with feedback loops) account for the gap; see the source page for detail.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "metr")
SORT file.name ASC
```

## Open questions

- METR's underlying benchmark methodology is not yet directly ingested — it's only known here through Anthropic's reference. A primary METR source would clarify the comparison.
