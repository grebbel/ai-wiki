---
type: entity
kind: organization
aliases: ["O'Reilly Media", "O'Reilly", "O'Reilly Radar"]
tags: [oreilly, publisher, oreilly-radar, learning-platform, tech-publishing, conferences]
confidence: 0.85
last_confirmed: "2026-05-16"
accessed_at: "2026-05-16"
source_count: 8
relationships:
  - type: employs
    target: Mike-Loukides
    via: "VP of Content Strategy; editorial lead of O'Reilly Radar and the monthly Radar Trends to Watch digest"
---

# O'Reilly Media

US-based technology publisher and learning platform founded 1978 by **[[Tim O'Reilly]]**. Headquarters Sebastopol, California. Publishes technical books, runs the O'Reilly learning platform (subscription-access library + live training), and operates **O'Reilly Radar** (radar.oreilly.com / *oreilly.com/radar*) — its long-running technology-trend editorial channel under [[Mike Loukides]]'s curation.

Promoted to entity status in the **16 May 2026 batch ingest** that landed eight O'Reilly Radar articles (five monthly *Radar Trends to Watch* installments Jan–May 2026 plus three feature pieces: Baron's annual *Signals for 2026* outlook, Shyamsundar-Jain's *Organizational Strategies from the Collective Wisdom of Nature*, and Osmani's *Agent Harness Engineering*).

## O'Reilly Radar — the editorial channel the wiki most engages

The wiki currently anchors on O'Reilly Radar via two recurring formats and three feature pieces:

**Monthly format** — Loukides's *Radar Trends to Watch* digest (six-section curated roundup; ~30 items per issue). Threads forward from one month to the next via recurring topic blocks (Skills / Agents / MCP / Harnesses / Security / Models).

**Annual format** — *Signals for [year]* — editorial annual-outlook framed around a curated paradigm-vocabulary shift (in 2026: *"the year of increased accountability"*).

**Feature pieces** — solicited long-form essays. The wiki has ingested:

- [[2026-02-11-shyamsundar-jain-organizational-strategies-collective-wisdom-nature|Shyamsundar & Jain — *Organizational Strategies from the Collective Wisdom of Nature*]] (11 Feb 2026; ~9-min editorial on distributed-coordination archetypes).
- [[2026-05-15-osmani-agent-harness-engineering|Osmani — *Agent Harness Engineering*]] (15 May 2026; ~17-min essay reposted from addyosmani.com; the wiki's first practitioner-side cross-author synthesis on the harness-engineering discipline).

## Appears in this wiki via

- [[2026-01-06-loukides-radar-trends-january-2026]] — January 2026 digest.
- [[2026-01-09-baron-signals-for-2026]] — Annual *Signals for 2026* outlook by [[Julie Baron]].
- [[2026-02-03-loukides-radar-trends-february-2026]] — February 2026 digest.
- [[2026-02-11-shyamsundar-jain-organizational-strategies-collective-wisdom-nature]] — Feature: distributed coordination.
- [[2026-03-03-loukides-radar-trends-march-2026]] — March 2026 digest.
- [[2026-04-07-loukides-radar-trends-april-2026]] — April 2026 digest.
- [[2026-05-05-loukides-radar-trends-may-2026]] — May 2026 digest (Loukides + Claude co-byline).
- [[2026-05-15-osmani-agent-harness-engineering]] — Feature: harness engineering.

## Editorial signature

Across the eight ingested pieces, three editorial-policy threads are visible: **(1) explicit vocabulary curation** (the *Signals* piece names *vibe coding / agentic dev / context engineering / eval- and spec-driven development / multi-agent orchestration* as 2026's operating vocabulary, matching [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's]] paradigm framing from the practitioner side); **(2) deliberate cross-platform reposting** (Osmani's piece is reposted-with-permission from his personal blog — O'Reilly Radar is functioning as an editorial *consolidator* of the strongest practitioner essays in the space); **(3) AI-assisted-curation transparency** ([[2026-05-05-loukides-radar-trends-may-2026|May 2026 digest]] carries Claude as named co-author).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "oreilly-radar")
SORT file.name ASC
```
