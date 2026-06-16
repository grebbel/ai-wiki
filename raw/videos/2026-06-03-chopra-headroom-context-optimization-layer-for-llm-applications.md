---
title: "Headroom: A Context Optimization Layer for LLM Applications - Tejas Chopra, Netflix, Inc."
video_id: UOWSHg18cL0
url: https://www.youtube.com/watch?v=UOWSHg18cL0
channel: The Linux Foundation
channel_id: UCfX55Sx5hEFjoC3cNs6mCUQ
channel_url: https://www.youtube.com/channel/UCfX55Sx5hEFjoC3cNs6mCUQ
publish_date: '2026-06-03T11:16:03-07:00'
upload_date: '2026-06-03T11:16:03-07:00'
category: Science & Technology
duration: '41:11'
length_seconds: 2471
view_count: 2678
default_language: null
is_live: false
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
chapters: []
description: |
  Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

  Headroom: A Context Optimization Layer for LLM Applications - Tejas Chopra, Netflix, Inc.

  LLM tokens are expensive. With context windows expanding to 200K+ tokens, a single API call can cost several dollars & in production systems handling thousands of requests, these costs compound quickly. Most optimization efforts focus on model selection or prompt engineering, but the context itself often contains massive redundancy.

  Headroom is an open-source Python library (https://github.com/chopratejas/headroom) that sits between your application and your LLM provider, transparently optimizing context before it reaches the model. The core insight is simple: LLM contexts—especially in agentic workflows—are filled with repetitive tool outputs, verbose JSON arrays, and boilerplate that consumes tokens without adding proportional value.

  Headroom introduces novel concepts such as reversible compression, cache aligners, compression routers, and even persistent memory.

  Real-world results:
  - 50-90% token reduction on typical agentic workloads
  - Drop-in integrations for LangChain, OpenAI, Anthropic, and any OpenAI-compatible provider
  - Zero code changes required when using the proxy server
notes: |
  ASR-cleaned auto-transcript (single caption track, kind: asr). Cleanups applied:
  speaker name "Tjis"/"Tahas" → "Tejas" (Chopra, per video title); "cloud code"/"clot
  code"/"clock code"/"cla" → "Claude Code"/"Claude"; "codeex" → "Codex"; "OpenClaw"/"open
  code" → "OpenCode"; "Reddus" → "Redis"; "SQite" → "SQLite"; "GP" → "grep"; "d-mpress" →
  "--compress"; "LLM Lingua" → "LLMLingua"; "compress base"/"compress model" → "compress-base";
  "cache_cont control" → "cache_control"; "open lmetry" → "OpenLLMetry"; "Langmith" →
  "LangSmith"; "GPT 4 mini/40 mini" → "GPT-4o mini"; "AGNO" → "Agno". The tool name rendered
  "RTK" is left verbatim (ASR-uncertain). No YouTube chapters; section headings below are
  inferred from topic shifts. Talk by Tejas Chopra (senior engineer, Netflix; open-source
  author of Headroom) at a Linux Foundation open-source conference (Minneapolis), published
  3 June 2026. Repo: https://github.com/chopratejas/headroom
---

## Intro — who and why

[0:00] Hi everyone, thank you so much for coming over and listening to my topic today. I'm Tejas. I'm going to present an open-source project that I personally worked on — it's called Headroom. It's my first time in Minneapolis, so I'd like to thank the Linux Foundation for inviting me here, as well as all of you who have traveled from different parts of the world. It's great to see the power of open source — that even when we're seeing AI churn and produce code at each breath, we still value the foundations and the ethos of open source.

[0:46] Headroom is a project that started around four months ago, and the idea was very simple. I use a lot of Claude Code — there's no shame in admitting that. I ran out of tokens every day. I used to pull my hair: when will the clock reset so I can start using more tokens? That's where I decided — I have no idea where the tokens are going, so let me cut it open and see where tokens are being spent, and can I give myself some extra **headroom** when it comes to tokens. That's where the project started.

[1:24] Who am I? I'm Tejas, in California. I work at **Netflix** as a senior engineer. My day job is building the data storage that makes recommendations possible — when you click on Netflix, like something, watch something, skip something, I capture all that data and store it so recommendation models can recommend the latest movies or shows. But that's my day job. Headroom is what I do after Netflix.

[2:03] Headroom started off with just me trying to solve my own problem for Claude Code. As you can imagine, Python gets most of the work done when you're working for yourself, so I started Headroom in Python for just Claude Code. But it found resonance with the community and people started extending it — it has OpenCode integration, Codex integration. Then I realized they make it so hard to integrate with different providers. So Headroom has now grown from its Python base to a **Rust implementation** in just 4 months since it was open-sourced. We're at **1,900 GitHub stars** thanks to the community, **30+ contributors** from across the world. My background in data infrastructure and storage helped me build some of the core pieces.

## The problem: context bloat, not prompt verbosity

[3:10] Let's talk about the problem that exists everywhere nowadays. [Show of hands — who uses Claude Code? Codex? Anything that saves you tokens?]

[3:33] When I started looking at where my money is being spent: in one of my Claude Code sessions, my CPU usage went high and crashed my laptop, so I asked it to find from the logs where that happened. There was a tool call made to read the log files — the **entire log file was pulled into the context window**. That's wasteful because 90% of it is garbage I don't care about. And if it happens with one log file, it extends to other pieces — a database call returns JSON, you get multiple entries, 80% of them are waste; you just care about the 20% that answers the user's query.

[4:29] Most of the literature on token compression has focused on **user-prompt compression** — if I use very flowery language, it condenses my prompt into something semantically similar and calls it token compression. But 90% of my coding workflow involves anything *but* the user prompt: local reads to code files, external tool calls, web pages, arxiv papers being read. One-size-fits-all will not work here. **Most of the agent's token budget is really noise.**

## Prior art and the gaps

[5:20] I looked at what others have done.

- **Provider-native prefix caching + compaction** (OpenAI, Claude): when you run out of context window, they summarize/compact. It's **extremely lossy** — and it restricts everything you've captured to a flat wall of text, because compaction just represents it in a markdown file. That's a lot of information loss.
- **KV cache / prefix caching mechanics**: when you talk to Claude, it's not just your new sentence — it's *everything you've said until now plus the new bit* going again to the LLM, a contiguous appended array of all historical messages. So every time you say "hi," everything before it goes too; 99% is already-sent. Providers offer **prefix caching**: if you've sent the data before, they charge ~10%. But if you change even a little within that window, it's **not a cache hit — they penalize you for the entire window.** These nuances are hidden in the documentation.
- **RTK** [ASR-uncertain] — a "token killer": when Claude Code issues a lot of GitHub CLIs to investigate a failed PR, the default CLI outputs aren't compressed; many CLIs have a `--compress` option. RTK looks at the CLIs your agent calls and compresses them at the point of the call. **LeanCTX** (lean context) is another variant.
- **Commercial YC-funded companies** expose a cloud API: you call `compress`, give it a payload, get a compressed output back. But because every provider has different harness nuances, it's impossible to integrate these into daily workflows.

[8:46] That's where Headroom started: I wanted the same experience as all these combined, with the idea that it should **work on your laptop as a proxy** — a simple `pip install`, works out of the box. And the other aspect is **reversible compression**.

## Reversible compression

[9:05] How can compression be reversible? It's sort of a marketing term — it's the fact that you compress something but **inject information to the LLM saying that if you need more, here is a tool call you can make.** So if the LLM wants the original context back (because you compressed too aggressively), it can make a tool call and fetch it. That's how it's reversible.

[9:37] In essence it's a **local compression layer between the agent and the model**, and it shrinks everything in between — tool calls, file reads, glob or grep data — depending on the type of tool call. It has **six compressors**, **four deploy modes**, and **no data leaves your box** — it runs on your laptop.

## The three stages: cache aligner → content router → CCR

[10:08] [Slides made with claude.ai/design — put your GitHub repo there and ask for slides; maybe put Headroom in front of it to save tokens.] There are three stages:

**1. Cache aligner.** If everything is packed and cached, your provider charges only 10%. But if you change even a single thing in that previous huge array, you get a cache miss. What changes? If your system prompt (which you don't control) contains a **date field or a UUID that changes per session**, you're effectively getting a cache miss every time — which blows up costs. The cache aligner looks at your system prompt and tools, **extracts dynamic fields, and moves them toward the end** so you still get a cache hit for the majority of your session.

**2. Content router.** Once you have a payload to send, applying the same compression logic everywhere **does not work** (I tried — it was the simplest model I built and it failed). You need **different compressors per type of data**: an AST-based compressor for code files (code has natural structure you can parse), a JSON compressor for JSON, a DOM compressor for web-page DOMs. You can extend and build more.

[12:32] Fitting compressors together in the context is where **knowledge of different harnesses** comes into play. Example (I got burnt by this): Claude's **default prefix cache TTL is 5 minutes** — interact continuously within 5 minutes and you get the 10% sweet deal; cross into the sixth minute and you pay for the entire array. The 5 minutes isn't even in your control: if Claude forks off a **sub-agent**, the sub-agent has its own prefix cache, so by the time it returns you've exhausted your five minutes. (A neat trick they play: even for simple things they spin up a sub-agent to push past 5 minutes so you pay more.) There's a hidden setting — a **1-hour TTL** instead of 5 minutes — but you pay **2× the cost for your writes to get 90% savings on reads.** Depending on your coding style (how often you resume sessions, how interactive you are), one choice beats the other. Headroom is trying to expose that — a PR will look at your historical sessions and automatically set that environment variable to maximize savings.

[14:38] Codex exposes extremely different APIs; Gemini is still figuring out what it wants to do (confusing to get working); OpenCode lets you work with external models but some don't play well with these settings. Another nuance: Claude has a **subscription model and an API model** — a $200 plan works for Claude Code up to a point, then falls back to APIs, and they go through different paths. It's extremely complex to get working for all combinations.

**3. CCR — Compress, Cache, and Retrieve.** This is the reversibility: when giving a JSON payload to Claude, you compress and squash it and put a marker saying that if the LLM wants to uncompress it, it should make a tool call. CCR is the **local storage** that holds the reversible original context so the LLM can retrieve it.

## Integration and hooks

[16:15] Four ways to integrate:
- Call a `compress` command with messages (for LangChain, **Agno**, and other pipelines).
- `headroom wrap claude` / `headroom wrap codeex` — starts the proxy on your local machine and routes all calls through it.
- An **MCP server** that lets it retrieve these tools.

[16:44] Under the hood there are **11 hooks**. Whether or not you use coding agents, Claude/OpenAI expose hooks — good interception points if you want to build a harness: what to call before the session starts, before a tool call, after a tool call. Headroom integrates intelligently with all these hooks.

## The compressors

[17:16] Different compressors per data type:
- **JSON — "smart crusher": 83–95% savings** in the best case. Looks at the JSON payload and the user's prompt, decides which fields the user/response cares about, computes mean/standard-deviation across fields, and squashes the unimportant ones. Has a **learning mechanism**: if you compressed too much and the LLM had to fall back and retrieve the original, it detects that and compresses less next time.
- **Code compressor** — uses the structured nature of code; if you have an LSP, your code isn't read directly (Cursor won't grep over your code to answer a question, but Claude will). Language support across several languages.
- **compress-base** — an **encoder-only model** (not a summarizer; it doesn't generate text). It weighs each token and decides whether keeping or removing it impacts the output. Initially I used Microsoft's **LLMLingua** (text compression only), but it didn't perform well — it was trained on **meeting summaries**, which don't represent coding-agent work. So I trained my own **compress-base on agentic traces**. "It's not the best model, honestly, but that's where the opportunity lies to make it better" — it's open source, with a v2 planned.

[20:48] **Cache aligner** discount table by provider: **Anthropic — 90% discount** if you specify `cache_control` tags (Headroom does this automatically); **OpenAI — 50% discount**, no tag needed; **Google — 75% discount** with cached content, but it "almost doesn't work well."

[21:42] CCR works not just for JSON — for compress-base, code, or any compressor. It runs on your laptop and is **ephemeral**: backed by **local Redis + SQLite with a 5-minute TTL.** Data older than 5 minutes needs the TTL configured separately, at the cost of storage.

## Demo + results

[22:26] [Demo: `headroom wrap claude` starts Claude; ask a basic question; Claude works in parallel; go to localhost:8787 to see cost savings, token savings, cache prefix hits.] Typically users save **20–30%**, a function of the tool calls they do. We've reached **200 billion tokens saved — roughly $700,000 saved for users** — and that's from **opt-in telemetry** (tokens-saved only; we look at no data), so 200B is the minimum people are willing to share. That tells you how much providers charge for bloat.

[24:06] **Memory mode** demo: three tabs, first two have memory, the last doesn't. Say "remember I like dark mode" in a memory tab; ask "what do I prefer?" in the other memory tab and it says "you like dark mode"; the third (no memory) doesn't. When I built this, Claude didn't have memory.md (it has since added it). The value: today, working across agents, some companies offer a cloud-based knowledge graph to save information from a Claude session and use it in a Codex session. This is a basic one — **SQLite on your laptop**, storing a simple graph of memory from one coding session (e.g. Claude Code), then **bridging between the SQLite DB and the agent.md / memory.md file** so a new agent (e.g. Codex) can use the same memory. Extended forward, you could build it as a managed offering — using learnings from one person's agents and passing that memory to another.

## Why beyond cost: latency and accuracy

[25:36] Community numbers across different agentic workloads (not just coding). Headroom is **great when you have a lot of data to process but need a small piece of it; not great when everything is important.**

[26:02] All of this only works if it's accurate — otherwise there's no point compressing. We benchmark across accuracy frameworks (still ongoing; a great contribution opportunity), measuring versus the baseline; because we have reversibility, we should be the same.

- **Latency**: compressing tokens saves latency. One user uses Headroom in a **voice agent** — speech→text→LLM (with tool calls)→text→speech. Voice-agent latency is generally ~300ms; **human-perceptible latency is ~200ms** (under which it feels human). Their whole game is getting latency down — that's where Headroom helps, in the middle phase sending data to the LLM.
- **Accuracy**: as context windows grow, **accuracy drops significantly** ("context rot"). By compressing tokens and being intelligent about what goes into the context window, accuracy is also benefited.

## Where it's going

[27:43] We've built something basic that works for coding agents, with a compressor trained on some agentic workloads. Next:
- **Per-domain compressors**: financial data has very different compression characteristics (you can't just remove numbers or clauses); medical data is separate again.
- **Voice agents** (already in use).
- **Image/video**: one user goes to factories, wears glasses, records someone operating machines; the whole video is sent to Claude at **$3 per video upload**, and Claude outputs instructions on how to operate the machine. Using an **image variant of Headroom** that chops the video into pieces and compresses tokens, the cost drops to **$0.20 per upload.**
- **Provenance for every token**: confirm what has gone into a context window and from where. Because Headroom sits between LLMs and agents, it can track the source of data and that metadata — which **cannot live in a foundation model** (they don't care where your data comes from, and you may use three different providers). Companies want to keep this metadata and memory in-house. New project, to be open-sourced soon: **Headlight** — context provenance, on the idea that today's observability (OpenTelemetry, OpenLLMetry) is **built for humans to consume**, but "a year out, agents will consume telemetry data," so the telemetry output should be **token-efficient for agents to use.**

[30:21] [Last demo: document compression on a **190-page 10-K financial document — 34% token reduction**, with accuracy preserved on a weird question.] Instead of typing the GitHub repo, please scan this code, try it, break it, send PRs. Thank you.

## Q&A

**Q — Distinguishing compressible vs non-compressible content (RBAC claims, deny rules, delegated identity, PII/PHI)?** Headroom has a PR route that **removes PII/PHI and identity data before compressing** — we don't touch it. compress-base is trained **not to compress** UUIDs, links, and similar fields. And if something like that *is* compressed, reversibility helps — the LLM makes an MCP call to retrieve it, and we keep it around.

**Q — Will I get in trouble using Headroom with Claude Code at work?** A lot of workplaces don't talk to Claude directly — they have a proxy in the middle (a **LiteLLM proxy** or a **Bedrock proxy**). The challenge is integrating Headroom with that (you don't want proxy→proxy→Claude). We're working on integrating well with LiteLLM. On privacy/security: we capture no data; it lives on your laptop; opt-in telemetry is just tokens-saved. Netflix has many teams using Headroom with no data leakage.

**Q — How does the LLM know when to decompress?** MCP tools carry an explanation ("call this tool whenever…"). We register `headroom retrieve` as the MCP tool and say: if information is missing or compressed out of this payload, call this tool. In the squashed/compressed data we embed an **ID** for the LLM to call with. We tried this with **GPT-4o mini** (small, old) and it still worked. In practice, **99% of the time the LLM doesn't call** because it finds its answers elsewhere — it doesn't need it.

**Q — Local models + Headroom: lower electricity costs?** Yes — compressing tokens means less context-window usage, and energy cost scales with context-window usage; plus local tool calls avoid some calls. No statistics yet (most users are people burnt by token costs — Claude Code, Codex, Gemini users).

**Q — How do you measure accuracy?** Mostly anecdotal first ("it seemed to do its job"), but also **accuracy benchmarks** that show the same numbers with and without Headroom for different coding tasks — proving it didn't "go around in circles" (benchmarks cover how quickly you converge to a goal). Eval is a big field and Headroom's success rests on getting it right; many PRs/issues are about better evals.

**Q — Scaling from local-first to org-wide?** Headroom is an interface/implementation mechanism where you plug in different pieces. Memory and CCR are local-only today; org-wide they'd sit on (e.g.) AWS RDS. We use easily interchangeable components across cloud providers. Observability uses OpenTelemetry (we don't collect it), but an org can route to their OTel collector / Prometheus / Langfuse / LangSmith — a plugin. Community members are working on **PII/PHI removal** plugins (Nightfall AI, Google DLP).

**Q — How do you handle drift (new models releasing over time)?** A **weekly job** does this today, protecting against unintended drift. The goal is to evaluate drift against the base model versus our original accuracy measurements on every check-in, but it's expensive — so we run it at major/minor version bumps. "Honestly, we don't have a good story there" — input welcome.
