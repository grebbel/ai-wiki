---
type: entity
kind: person
aliases: ["Adi Ignatius"]
tags: [hbr, journalism, editor-in-chief, podcasting]
affiliation: "[[Harvard Business Review]]"
role: "Editor-in-Chief, Harvard Business Review; host, HBR IdeaCast"
confidence: 0.78
last_confirmed: "2026-05-11"
source_count: 2
relationships:
  - type: part-of
    target: Harvard Business Review
    via: "Editor-in-Chief"
---

# Adi Ignatius

**Adi Ignatius** is Editor-in-Chief of [[Harvard Business Review]] and host of the **HBR IdeaCast** podcast. Promoted to a wiki entity page on 11 May 2026 after appearing as the named interviewer in two ingested HBR IdeaCast sources.

## Role in the wiki

Ignatius is the interviewer on **two HBR IdeaCast sources** the wiki currently holds. As editor-in-chief his role is the curator-interviewer of HBR's audio long-form — he selects the interviewees and frames the conversation, but does not author the substantive content himself.

### Interviews ingested

1. **[[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025]]** — interview with **Andy Jassy** (Amazon CEO) on Amazon's three-layer AI strategy, the +15% IC-to-manager-ratio flatten-management initiative, 5-day RTO, and the May-2025 natural-language-coding-floor-raising prediction. **29:39, manual caption track.**
2. **[[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels 2026]]** — interview with **Bob Sternfels** (McKinsey Global Managing Partner) on McKinsey's outcome-underwriting business-model migration, the $1B compliance overhaul post-OxyContin / South Africa controversies, and the 20-year hiring-overhaul. **31:36, manual caption track.**

Both interviews use the **manual caption track** (the wiki's only two `kind: manual` video sources to date — a notable HBR production-quality signal versus the ASR-only norm).

## Interviewing style observable across both ingests

- **Frames questions around the listener's recognition** (e.g. *"a lot of CEOs say that — how do you try to make that happen?"*) — sets up the interviewee to differentiate from the rhetorical cliché.
- **Probes for the operational mechanism** behind framing claims — asks for the *how* not just the *what*.
- **Returns to societal / leadership themes** in the back third of each interview (governance, leadership style, geopolitical uncertainty) — predictable HBR-IdeaCast structural beat.

## Notable affiliations

- **[[Harvard Business Review]]** — Editor-in-Chief.
- **HBR IdeaCast** — host. The wiki's primary HBR audio-source channel.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## Open questions

- **Pre-HBR-IdeaCast history** — Ignatius's prior career (Time Magazine reporter / Beijing bureau / Forbes adventures) is biographically substantive but not load-bearing for the wiki's current concept clusters. Promote material on demand.
- **Editorial-selection pattern** — whether the wiki can infer editorial-priority signals from the cadence and topic-mix of HBR-IdeaCast guests Ignatius selects. Speculative.
