---
type: entity
kind: person
aliases: ["Simon Willison", "Simon Wilson", "Simon Willis", "@simonw"]
tags: [simon-willison, django-co-founder, datasette, ai-developer-whisperer, challenger-disaster-worry, dark-factory-pattern, agentic-engineering-book, find-the-joy-find-the-purpose, llm-cli, prompt-injection]
website: "https://simonwillison.net"
role: "Co-founder of Django web framework; creator of Datasette; prolific AI-engineering blogger and developer-tool builder; widely-cited AI-developer-whisperer"
confidence: 0.82
last_confirmed: "2026-05-28"
accessed_at: "2026-05-28"
source_count: 2
---

# Simon Willison

**Co-founder of Django** (Python web framework, 2005) and **creator of Datasette** (data publishing / exploration tool). Prolific AI-engineering blogger at [simonwillison.net](https://simonwillison.net) — covers LLMs, prompt engineering, prompt-injection security, command-line AI tooling (`llm` CLI), and the broader practitioner discipline of AI-assisted software development. [[Paul Everitt]] calls him *"the developer AI developer whisperer"* — a widely-cited reference voice in the AI Dev 26 SF practitioner cluster.

Surfaces in this wiki for several substantive framings:

- **The *challenger disaster* worry** — *"you take the human out of the loop, you let the agent shove stuff into production, maybe it drops a bunch of tables. No, I'm sorry, that was this week. Maybe it does something really, really bad."* Cited by Everitt as the quality-crisis anchor (referring to the Replit-dropped-production-database incident).
- **The *dark factory pattern*** — *"you can turn the lights off in the factory because there ain't no humans in the factory. The humans are on the outside building the stuff in the factory to run the factory."* Cited by Everitt as the canonical *augmentation-not-replacement* metaphor for the agentic-engineering reframe.
- **The *find the joy / find the purpose* sign-off** — *"What's left for the humans? So much stuff."* Cited by Everitt as the closing rhetorical move.
- **Writing a book on agentic engineering** — Everitt: *"Simon's actually writing a book on this where he's doing kind of a taxonomy of these things."* Worth tracking for future ingest.
- **Red-green TDD for agents** — *"From Lenny's podcast that Simon was on. Red-green testing is one of those things we as engineers know about ... if you will write a broken test as the first step in your agent's work, the agent will start to learn the way you like to write tests and will mimic your testing style."*

## Appears in this wiki via

- [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering]] — cited extensively (challenger-disaster worry, dark-factory pattern, red-green TDD framing, *find the joy* sign-off, *writing a book on agentic engineering*).
- Earlier sources may cite Willison incidentally — worth a dataview audit when the source-count grows further.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "simon-willison")
SORT file.name ASC
```

## Open questions

- Simon Willison's upcoming book on agentic engineering — title and publisher not yet named in the talk. Worth tracking for ingest when it lands.
- The Lenny's-podcast episode Everitt references for the red-green-TDD-for-agents framing — worth identifying and ingesting if it adds substance beyond Everitt's compression.
- Willison's `llm` CLI tool — useful adjacent context for the [[agent-harness]] concept page when a substantive source ingests it directly.
