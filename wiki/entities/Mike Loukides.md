---
type: entity
kind: person
aliases: ["Mike Loukides"]
tags: [mike-loukides, oreilly, oreilly-radar, radar-trends, editor, trend-curation]
confidence: 0.85
last_confirmed: "2026-05-16"
accessed_at: "2026-05-16"
source_count: 5
relationships:
  - type: part-of
    target: O-Reilly-Media
    via: "Content and editorial leadership at O'Reilly Radar; author of the monthly Radar Trends to Watch series"
---

# Mike Loukides

VP of Content Strategy at [[O'Reilly Media]] and editorial lead of **O'Reilly Radar**. Author and curator of the monthly *Radar Trends to Watch* digest — a six-section, ~30-item editorial roundup of the prior month's tech news, with explicit emphasis on threads expected to compound (agents, MCP, harnesses, security, infrastructure, design). Long-time technical editor (Unix system programming, data science, AI books). Quoted by [[Julie Baron]] in [[2026-01-09-baron-signals-for-2026|Signals for 2026]] on the *"signs of the future in the present"* signal-detection framing.

The wiki promoted Loukides to entity status in the **16 May 2026 batch ingest** that landed all five of his Jan–May 2026 *Radar Trends* digests plus three other O'Reilly Radar articles. Loukides is the wiki's first *recurring-digest curator* entity — his editorial weighting itself counts as a signal worth citing, distinct from any individual item in the digest.

## Editorial moves the wiki has tracked

- **Genre shift in [[2026-04-07-loukides-radar-trends-april-2026|April 2026]]**: from chronicling toward signal-detection. *"News from the future"* framing via William Gibson. Adopts scenario-planning language compatible with [[2026-04-28-webb-strategic-foresight|Webb's strategic-foresight methodology]].
- **AI co-authorship in [[2026-05-05-loukides-radar-trends-may-2026|May 2026]]**: Claude added as named co-author. **First time the digest carries an explicit human-AI co-byline** — transparency from the publisher about AI-assisted curation.
- **Recurring threads**: agent harnesses / MCP / Skills / OpenClaw / agent-runtimes-becoming-HaaS / prompt-injection-as-first-class-threat / model-release cadence (GPT, Claude, Gemini, Kimi, Qwen, DeepSeek, Mistral, Nemotron).

## Appears in this wiki via

- [[2026-01-06-loukides-radar-trends-january-2026]] — January digest (GPT-5.2, Agent Skills open spec, MCP, cognitive-architect role).
- [[2026-02-03-loukides-radar-trends-february-2026]] — February digest (*"AI has colonized everything"*; Cursor hundreds-of-agents; Anthropic Claude constitution; OpenClaw first mention; Gas Town).
- [[2026-03-03-loukides-radar-trends-march-2026]] — March digest (OpenClaw ecosystem; AI as offensive security tool; benchmark-gaming surfacing; Claude Remote Control; C-compiler-via-agents).
- [[2026-04-07-loukides-radar-trends-april-2026]] — April digest (genre shift to "news from the future"; world-models category; Codex Plugins; SHA-256 vulnerability; Copilot collaboration-erosion finding).
- [[2026-05-05-loukides-radar-trends-may-2026]] — May digest (*"AI becoming operational"*; HaaS productization across vendors; Claude Mythos / Project Glasswing; GPT-5.5; npm supply-chain attack; GPT-Rosalind; Boston Dynamics gauge-reading).
- [[2026-01-09-baron-signals-for-2026]] — Quoted by Baron on signal-detection framing.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "mike-loukides")
SORT file.name ASC
```
