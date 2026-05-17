---
type: entity
kind: person
aliases: ["Garry Tan"]
tags: [garry-tan, y-combinator, gstack, gbrain, ai-founder-type, startup-school, fat-skills, thin-harness, accelerator-president]
affiliation: "[[Y Combinator]]"
role: "President & CEO, Y Combinator (since 2023); founder/engineer; ex-Palantir #10; Posterous co-founder"
confidence: 0.85
last_confirmed: "2026-05-12"
accessed_at: "2026-05-12"
source_count: 3
---

# Garry Tan

**Garry Tan** is President & CEO of [[Y Combinator]] (since 2023). Engineer by background — Stanford Computer Systems Engineering; **Palantir employee #10**; **Posterous** co-founder (sold to Twitter); built the first version of YC's **Bookface** (internal social platform + portfolio knowledge base). The wiki's **canonical AI-founder-type-archetype operationalised** ([[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|per Hu 2026]]) — runs 10-15 parallel Claude Code sessions, ~400 PRs in review, ships open-source toolkits at venture pace.

Promoted from Dangling to an entity page on 12 May 2026 after three substantive source mentions:

1. [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan / GStack 2026]] — first-party demo of his open-source Claude-Code-toolkit.
2. [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase / ex-brain 2026]] — names GBrain as a parallel concept to Karpathy's LLM Wiki.
3. [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] — deep first-party-class architectural treatment of Tan's **GBrain** (24 skills, 21 cron jobs, 17,888-page brain repo).

## Role in the wiki

Tan is the wiki's **first first-party-operating AI-founder-type-archetype** anchor. Where [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu 2026]] *prescribes* the AI-founder-type (still builds / still coaches / leads by example), Tan is the worked example. Three angles surface across the ingested sources:

### 1. As the operator of a packaged harness — GStack ([[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan 2026]])

**GStack** — open-source toolkit (github.com/garrytan/gstack) wrapping Claude Code with named skills:

- **Office Hours**: 16-YC-partners adversarial-review distilled at 10% strength. *"Pressure-tests your idea before you write a line of code."*
- **Plan / CEO Review / Adversarial Review**: multi-step auto-fix of design-doc issues; tracked scored improvement.
- **Design Shotgun**: multiple AI design variants in ~60s as choices.
- **Code Review**: staff-level bug-catching after plan.
- **SLQA / SL browse**: Playwright+Chromium wrapped as a CLI (replacing *"the worst piece of software I've ever used"* — Claude-in-Chrome MCP).
- **Ship**: pre-merge gate.

**Velocity**: built in 3 weeks; *"now has more GitHub stars than Ruby on Rails."* The wiki's first founder-CEO-of-major-accelerator open-source-harness instantiation.

### 2. As the architect of an autonomous-knowledge-base — GBrain ([[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]] + [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase 2026]])

**GBrain** — Tan's second open-source project; **24 autonomous skills + 21 cron jobs + 17,888-page brain repo** on **Postgres + pgvector**. Built for personal AI agents (OpenClaw, Hermes, Claude Code). README: *"Your AI agent is smart but forgetful. GBrain gives it a brain."*

Architectural principles Liu names:

- **"Thin harness, fat skills"** — harness is ~200 lines (model execution + read/write files + safety); all intelligence in skill files.
- **CLAUDE.md + RESOLVER.md routing** — RESOLVER.md dispatches user intent to skills across six categories (always-on / brain ops / content ingestion / thinking / operational / setup). *"Skill descriptions themselves function as the resolver. The model reads the descriptions and matches intent automatically. No explicit routing code needed."*
- **Fat skill = workflow contract** — each skill is *"not a prompt template, but an entire workflow: when to fire, what to check, how to chain with other skills, what quality bar to enforce."*
- **Always-on signal-detector** — fires on every inbound message; *"An unlinked mention is a broken brain."*
- **Cron skills that run themselves** — *"each job is deliberately thin — the prompt is literally 'Read skills/{name}/SKILL.md and run it.'"* Jobs respect quiet hours (11 PM–8 AM by default); enforce idempotency.
- **Deterministic split** — separates latent work (reading, synthesis, pattern recognition) from deterministic work (database writes, calculations, reproducible outputs). *"Mixing them is how agents hallucinate."*
- **Tan's latest iteration** (Liu cites): *"Fewer fatter skills makes the resolver shorter, which itself is less context bloat. Short resolvers are better than long ones."* Trend: fewer, more comprehensive skills with branching parameters > many narrow ones.

GBrain is the wiki's **operationalisation of [[concepts/llm-wiki|the LLM Wiki pattern]] augmented with autonomous-action skills** — the *"fat skills"* / *act* corner of [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu 2026]]'s three-architecture decision framework.

### 3. As the AI-founder-type archetype operationalised at YC-president scale

Tan's reported workflow (per [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|GStack 2026]]):

- **10 to 15 parallel Claude Code sessions** all at the same time.
- *"About 400 PRs to review right now."*
- *"10, 15, 20, sometimes 50 PRs in any given day, depending on the number of meetings I have."*
- *"I have multiple open-source projects with tens of thousands of stars."*

Direct operationalisation of [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu 2026]]'s *AI founder type* archetype: *"still builds, still coaches and leads by example. If you're the founder, this needs to be you at the forefront."* Tan IS the worked example.

## Notable framings Tan has contributed

- **"ADHD CEO vs autistic CTO" model allocation** — *"Claude Opus 4.6 is sort of ADHD CEO. He's the guy you want to get a beer with and he's got a billion ideas, but when the going gets tough, you got to call in your autistic CTO and that's Codex."* First-party-CEO articulation of model-allocation-by-personality-fit-to-task as a working practice.
- **"Level 7 software factory"** (invoking Steve Yegge's *Gas Town* eight-stages-of-dev-evolution-to-AI) — *"There's this idea of trying to get to a level 8 software factory and GStack does not get you to level 8, but I do think it gets you to level seven."* Two-source-on-Yegge convergence with [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]].
- **"Office hours as 10% strength YC partner review"** — codified 16 YC partners' adversarial-review approach as a single Claude Code skill.
- **"Fewer fatter skills"** — Tan's latest iteration: *"Short resolvers are better than long ones."*

## Career timeline

- **Stanford** — Computer Systems Engineering.
- **Palantir** — employee #10; engineer / designer / product manager.
- **Posterous** — co-founder; micro-blogging platform; sold to Twitter.
- **YC** — built first version of Bookface; later promoted to President & CEO.
- **2023–present** — YC President & CEO.

## Notable projects

- **GStack** — open-source Claude Code harness toolkit; github.com/garrytan/gstack.
- **GBrain** — open-source autonomous-knowledge-base; 24 skills + 21 cron jobs + 17,888-page brain repo.
- **Bookface** — YC's internal social platform + portfolio knowledge base (first version by Tan).
- **Conductor** — multi-session Claude Code orchestrator Tan demos GStack inside of (third-party tool; Tan is the worked-example user).

## Convergence with wiki sources

| Source | Connection |
|---|---|
| [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack\|Tan / GStack 2026]] | First-party demo; the wiki's primary Tan source |
| [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up\|Hu / Y Combinator 2026]] | The *AI founder type* archetype Hu prescribes is operationalised in Tan's reported workflow. Same accelerator, same architectural prescriptions, two consecutive days of publication (Tan 23 April + Hu 24 April) |
| [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks\|OceanBase / ex-brain 2026]] | Names GBrain as a parallel concept to Karpathy's LLM Wiki. Two-source first acknowledgment of GBrain |
| [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers\|Liu 2026 (AI Advances)]] | Deep first-party-class architectural treatment of GBrain — thin harness / fat skills / RESOLVER.md routing / signal-detector / cron architecture |
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | GBrain extends Karpathy's LLM Wiki pattern with the *act* layer; structurally complementary architectures |
| [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy\|Böckeler 2026 (Thoughtworks)]] | Two-source Yegge Gas Town convergence: Böckeler invokes Yegge as audience-orienting; Tan invokes Yegge with the specific *level 7 vs level 8* terminology |

## Open questions

- **GStack and GBrain GitHub repos** — both are open-source; primary-source ingest of RESOLVER.md, THIN_HARNESS_FAT_SKILLS.md, skill schemas would substantiate the *thin-harness/fat-skills* framing.
- **GStack adoption metrics** — *"more GitHub stars than Ruby on Rails"* is a velocity claim from April 2026; 3-month / 6-month adoption arc worth tracking.
- **GBrain enterprise extensions** — Liu notes GBrain *"optimizes for one power user's workflows, not organizational deployment."* If Tan or the YC community open-sources an enterprise extension, the pattern's scalability becomes empirically testable.
- **Conductor as a distinct entity** — Tan uses Conductor as the multi-session shell for GStack. First-party documentation on Conductor as a separate tool is an open ingest target.
- **OpenClaw and Hermes** — named by Liu as the personal AI agents GBrain is built for. Both currently Dangling first-mention; primary-source targets.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "garry-tan") OR contains(tags, "gstack") OR contains(tags, "gbrain")
SORT file.name ASC
```
