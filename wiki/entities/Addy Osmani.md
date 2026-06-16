---
type: entity
kind: person
aliases: ["Addy Osmani", "Addi Osmani", "@addyosmani"]
tags: [addy-osmani, google-chrome, web-developer-advocate, agent-harness-engineering, oreilly-radar, agentic-engineering-blog, ralph-loop, agents-md, hooks-compaction]
affiliation: "Google (Chrome team)"
role: "Software engineer at Google working on Chrome; web-developer advocate; prolific blogger on web performance, JavaScript, and (since 2025) AI-assisted software engineering; O'Reilly Radar contributor"
confidence: 0.82
last_confirmed: "2026-05-28"
accessed_at: "2026-05-28"
source_count: 2
---

# Addy Osmani

**Software engineer at Google** working on the Chrome team and a prolific web-developer advocate. Blog at [addyosmani.com](https://addyosmani.com); books on web performance and JavaScript patterns. From 2025 onward, his blog and O'Reilly Radar contributions have shifted substantially toward **AI-assisted software engineering and agentic engineering as a discipline**.

Osmani's wiki anchor is **harness engineering as a named discipline** — his [[2026-05-15-osmani-agent-harness-engineering|*Agent Harness Engineering* article on O'Reilly Radar (15 May 2026)]] is the wiki's first article-altitude treatment of harness engineering as a deliberate practice, covering: the **Ralph Loop** pattern, [[AGENTS.md]] convention, hooks, sandboxes, compaction, and *harness-as-a-service*. The article positions harness engineering as the *scaffolding-around-the-model-as-real-artifact-that-tightens-every-time-the-agent-slips* discipline — convergent with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's *Anatomy of an Agent Harness*]] (Osmani credits Viv as the originator of the *harness engineering* term).

[[Paul Everitt]] at [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|AI Dev 26 SF]] (one week later) cites Osmani as an influence: *"Addy Osmani wrote a blog post about Agentic Engineering. And as I tell you these blah-blah wrote a blah-blah in your mind you should be thinking it's entering the hype cycle. I should put this on my LinkedIn as a global recognized expert."* The self-deprecating framing notwithstanding, Everitt's nine-element agentic-engineering practice taxonomy includes *harness engineering* as a discrete element — Osmani's article is a direct conceptual predecessor.

## Appears in this wiki via

- [[2026-05-15-osmani-agent-harness-engineering]] — first-party article: *Agent Harness Engineering* on O'Reilly Radar; the wiki's first article-altitude treatment of harness engineering as a named practitioner discipline.
- [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering]] — cited by Everitt as influence on the nine-element agentic-engineering practice taxonomy.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "addy-osmani")
SORT file.name ASC
```

## Open questions

- Osmani's pre-2025 web-performance + JavaScript-patterns writing — substantial body of work but pre-AI-agent context. Worth flagging if a wiki concern surfaces around *web-performance + AI-coding-agent intersection* (the *AI-generated front-end performance regression* pattern).
- Osmani's specific *Ralph Loop* origin — Everitt mentions Osmani citing Viv as the originator of harness engineering; the precise attribution chain (Ralph Loop → AGENTS.md → harness engineering) is partly traced in the wiki via [[2026-05-07-chatterjee-anatomy-of-agent-harness]] but worth tracking further.
