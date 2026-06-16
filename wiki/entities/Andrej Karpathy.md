---
type: entity
kind: person
aliases: ["Karpathy", "Andrej Karpathy", "@karpathy"]
tags: [andrej-karpathy, ai-researcher, openai, tesla, eureka-labs, software-3.0, vibe-coding, jagged-intelligence, llm-wiki]
confidence: 0.92
last_confirmed: "2026-05-28"
accessed_at: "2026-05-28"
source_count: 7
relationships:
  - type: authored-by
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "interview subject (~30 min, Sequoia AI Ascent, 29 April 2026)"
---

# Andrej Karpathy

AI researcher and educator; **co-founder of OpenAI** (2015–2017); led **Tesla Autopilot computer-vision** (2017–2022); founder of **Eureka Labs** (2024–) for AI-native education. The wiki's most cross-cutting individual contributor: he is both the **upstream-spec author for this entire repo** ([`llm-wiki.md`](../../llm-wiki.md), [`llm-wiki-v2.md`](../../llm-wiki-v2.md), [`llm-wiki-v2-plan.md`](../../llm-wiki-v2-plan.md)) *and* a substantive source on agentic-engineering paradigm vocabulary as of 2026 ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]]).

## Why this page exists (cross-page-presence promotion)

Per CLAUDE.md §Lifecycle "Author-entity promotion", first-source mentions are usually deferred to the dangling list. Karpathy is promoted on first source-page mention via the same **cross-page-presence judgment** that produced [[Jack Clark]]: he is named explicitly in repo-root specs ([`llm-wiki.md`](../../llm-wiki.md), [`llm-wiki-v2.md`](../../llm-wiki-v2.md), [`llm-wiki-v2-plan.md`](../../llm-wiki-v2-plan.md)) and in [`CLAUDE.md`](../../CLAUDE.md) as the originator of the LLM-wiki idea this repo implements. That means the wiki has been *implicitly citing Karpathy as the upstream-spec author since instantiation* — promoting him formalises a citation chain that already exists.

The promotion is a one-off judgment call (the same caveat noted in the Jack Clark log entry) — the audit script ([`scripts/lint-dangling-authors.mjs`](../../scripts/lint-dangling-authors.mjs)) tracks only the strict ≥2-source-frontmatter rule and was not modified.

## Career snapshot

- **PhD, Stanford** (2011–2016, advisor: Fei-Fei Li). Convolutional neural networks for visual recognition; co-instructor of the canonical Stanford CS231n *Convolutional Neural Networks for Visual Recognition* course. Authored the influential *Hacker's guide to neural networks* and the long-running [karpathy.ai](https://karpathy.ai) writing.
- **OpenAI co-founder and research scientist** (Dec 2015 – Jun 2017). One of the original group named in the founding announcement.
- **Tesla, Director of AI / Senior Director of AI** (Jun 2017 – Jul 2022). Led the Autopilot computer-vision team; widely credited with the *"vision-only / no-LiDAR"* path Tesla pursued. Coined and popularised **Software 2.0** during this period — the framing that programming neural networks (datasets + architectures + training) is itself a form of programming.
- **OpenAI, returning** (Feb 2023 – Feb 2024). Worked on improving GPT-class assistants.
- **Eureka Labs** (founded Jul 2024 – present). AI-native education company; the *LLM 101n* undergraduate-level course is the public-facing artifact.

## What he is the wiki's source for (vocabulary and conceptual artifacts)

Karpathy is unusually prolific at **naming things that the field then adopts**. The wiki is using or planning to use several of his coinages directly:

- **[[software-3.0|Software 3.0]]** — the 1.0 / 2.0 / 3.0 trilogy framing (rules → weights → prompts). 1.0 was the standard reference; **2.0 was Karpathy's coinage in 2017** (the famous *"Software 2.0"* Medium post); **3.0 is his 2025–26 extension** as foundation-model prompting consolidates as a programming paradigm.
- **[[vibe-coding|Vibe coding]]** — coined by Karpathy in 2024 for *intuitive, exploratory code-with-LLM workflows*. Now in widespread practitioner use.
- **The wiki's [[jagged-frontier]] explanatory layer** — Karpathy contributes the *cause* (verifiability + labs care + RL training mechanism) for the *task-level observation* described by Dell'Acqua et al. The "are LLMs jagged?" framing in the wiki sits across both pages.
- **"Animals vs ghosts"** — Karpathy's mindset framing for what kind of intelligence LLMs are: *"We're not building animals; we are summoning ghosts."* He himself flags this as "a little bit of philosophising"; the wiki captures it as a sub-section inside [[jagged-frontier]].
- **[[agentic-engineering|Agentic engineering]] as a discipline** — Karpathy positions this as the "preserve quality bar at agent speed" complement to *vibe coding's* "raise the floor". Names it explicitly as an *engineering discipline*.
- **The LLM-wiki / LLM-knowledge-base pattern itself** — the [`llm-wiki.md`](../../llm-wiki.md) conceptual spec at the root of this repo is Karpathy's articulation of the workflow. As of [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|29 April 2026]] he confirms continued use of the pattern: *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles… anytime I see a different projection onto information, I always feel like I gain insight."* On **4 April 2026** Karpathy posted a GitHub Gist that crystallised the pattern as an *"idea file"* — a markdown document designed to be copy-pasted into an LLM agent. The gist hit **17 million views, 5,000 stars, and 4,282 forks within days** (per [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]). Three explainer articles ingested in this batch ([[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase / ex-brain]], [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju]], [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu]]) collectively describe the pattern, build a reference implementation, and place it in the RAG / Wiki / Skills hybrid landscape. The wiki now anchors the construct as a dedicated concept page: [[concepts/llm-wiki|llm-wiki]].

## Key claims attributable to Karpathy (in this wiki)

From [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|the Sequoia AI Ascent interview]]:

- **The December 2025 phase change**: agentic coding tipped from "useful but needs corrections" → "I just trust it now" in a single month. *"I've never felt more behind as a programmer."*
- **Software 3.0 is a new computing paradigm**, not a faster way to do existing programming. *"It's not just about programming becoming faster — there are new things available now."*
- **LLMs automate what you can verify**, just as classical computers automate what you can specify in code. The mechanism is RL training in verification-rewarded environments.
- **Two factors of jaggedness**: verifiable + labs care. Either alone is insufficient; both together explain why models fly in some circuits and struggle in others. *"You're slightly at the mercy of whatever the labs are doing."*
- **Agentic engineering pushes far past 10×.** The 10× engineer used to be the upper bound; Karpathy's claim is that agentic engineering enlarges that bound substantially.
- **Agents are intern entities** — remarkable but error-prone in surprising ways. Humans must own aesthetics, judgment, taste, oversight, the spec/plan.
- **You can outsource your thinking, but you can't outsource your understanding.** Humans become the bottleneck for *what's worth building*, *why*, and *how to direct agents*.

## Affiliations

- **Founder, [[Eureka Labs]]** (2024 – present, dangling — not yet promoted to entity page).
- **Co-founder, [[OpenAI]]** (2015 – 2017 + 2023 – 2024).
- **Former Director / Senior Director of AI, [[Tesla]]** (2017 – 2022, dangling — not yet promoted).
- **Stanford PhD** (2011 – 2016).

## Mentioned in

- [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] — substantive source: the Sequoia AI Ascent interview.
- [[2026-05-04-rethinking-agents-harness-is-all-you-need]] — referenced indirectly via the Software 3.0 framing the video implicitly assumes (LLM-as-interpreter, harness-as-OS).
- [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals]] — **biographical-bridge mention** (5th source citation, added 22 May 2026): YC founder Kesava Kirupa Dinakaran names Karpathy on-stage as his Rubik's-cube YouTube tutor in his childhood — *"I learned Rubik's cubes from Andrej Karpathy on YouTube, who eventually ended up founding OpenAI."* Not analytically load-bearing; flagged as a small graph-traversal connection between the wiki's existing Karpathy entity and the YC Root Access founder-vantage cluster. Karpathy's pre-AI-research public output (Rubik's cube speedsolving tutorials in the late 2000s; he was the captain of the international Rubik's cube team at one point per public records) is a real biographical thread the wiki had not previously surfaced.
- Repo-root specs: [`llm-wiki.md`](../../llm-wiki.md) (his original framing), [`llm-wiki-v2.md`](../../llm-wiki-v2.md), [`llm-wiki-v2-plan.md`](../../llm-wiki-v2-plan.md), [`CLAUDE.md`](../../CLAUDE.md) — the upstream specs that this entire repo implements.
- Concept pages he originated or shaped: [[software-3.0]], [[vibe-coding]], [[agentic-engineering]], [[jagged-frontier]] (cause-side framing).

## Open questions

- **Eureka Labs** as an entity page — currently a dangling reference. If a second source surfaces (interview, blog post, course materials), promote.
- **Tesla** as an entity page — currently dangling but mentioned in the AI Index reports too; could be promoted on cross-page-presence grounds in a future pass.
- **The original "outsource thinking ≠ outsource understanding" tweet** — Karpathy quotes it but doesn't name the author. Worth a citation upgrade if the original surfaces.
- **Karpathy's hinted "valuable RL environments not in the labs' mix"** — declined on stage. If a follow-up writeup names the domains, that's a high-value second source.
