---
type: entity
kind: person
aliases: ["Shunyu Yao", "Yao", "S. Yao"]
tags: [react, llm-agents, reasoning-and-acting, princeton-nlp, google-research, agent-research, foundational-author]
confidence: 0.75
last_confirmed: "2026-06-12"
accessed_at: "2026-06-12"
source_count: 2
---

# Shunyu Yao

AI researcher and **first author of [[react-reasoning-acting|ReAct]]** — the 2022 paradigm interleaving reasoning and acting in language models that became the structural core of the modern [[ai-agents|agent]] loop. At the time of the work he was a PhD student in the **Princeton NLP Group** (advised by [[Karthik Narasimhan]]), conducting the research during a Google internship with the [[Google Research]] Brain team.

## Wiki contributions

- [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|ReAct (paper, ICLR 2023)]] — first author. Introduced the reason–act–observe loop, the dense/sparse thought regimes, and the human-in-the-loop trace-editing result.
- [[2022-11-08-yao-cao-react-google-research-blog|ReAct (Google Research blog)]] — co-author of the popular announcement (with [[Yuan Cao]]).

His work is the genealogical root of the wiki's [[agent-harness|harness]] and [[ai-agents|agent]] cluster: the *"LLM that uses tools in a loop"* definition the wiki adopts from 2026 practitioners is ReAct named four years earlier.

## Why he is an entity (promotion note)

Promoted on 2026-06-12: named author on **two** wiki sources (the ReAct paper and its Google Research blog), crossing the second-source threshold. A strong anchor for any future agent-foundations ingests (Tree of Thoughts, SWE-bench, and related agent-reasoning lineages are natural follow-ons).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
