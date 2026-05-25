---
type: source
kind: video
title: "AI Dev 26 x SF | Ara Khan: Evals Are Broken Use Them Anyway"
author: ["DeepLearningAI"]
publisher: "DeepLearning.AI YouTube channel — AI Dev 26 x San Francisco conference talk by Ara Khan (Cline); 22 May 2026"
url: "https://www.youtube.com/watch?v=fAfuQN0WwFE"
date_published: 2026-05-22
date_ingested: 2026-05-25
length: "~24:36 minutes (auto-generated English captions; 699 ASR segments)"
raw: "../../raw/videos/2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway.md"
tags: [ara-khan, cline, deeplearning-ai, ai-dev-26, evals, evals-broken-use-them-anyway, terminal-bench, harbor, modal, stanford-sail, beat-claude-code, three-zones-of-improvement, model-vs-harness-vs-problem-space, three-things-being-tested, dont-believe-model-lab-evals, stay-current-not-earliest-adopter, evals-for-your-problem, hill-climbing, goodharts-law-zone-3, vibes-only-camp, objective-metrics-camp, customer-of-model-vendor-altitude, swe-bench-saturation]
dynamic_capabilities:
  - digital-sensing/identifying-needs
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
  - contextual/external-triggers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent
    via: "**Same-day same-conference paired evals anchors at opposite vendor-altitudes** — both at AI Dev 26 x SF, both published 22 May 2026. [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|Anthropic / Claude channel]] is the *model-vendor-side* evals doctrine (slide-gen agent + grader taxonomy + QA-loop pattern + autoregressive-judge-ordering bug + Sonnet 4.7 → Opus 4.7 model-upgrade observation). This Khan / Cline talk is the *customer-of-model-vendor-side* evals doctrine: *'we adopted Stanford terminal-bench, hill-climbed our harness, and beat Claude Code on Opus 4.5 evals.'* Two sides of the eval-discipline applied to the same model substrate from opposite vendor altitudes — same day, same conference, opposite agency choices (Anthropic: switch model; Cline: optimise harness)."
    confidence: 0.85
  - type: supports
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "**Direct operational instantiation of Chase's three-layer continual-learning model + Top-30-to-Top-5 harness-improvement empirical anchor.** Chase (Interrupt 26, 21 May 2026): *'we moved from top 30 on terminal bench two to top five just by changing the harness itself — no changes to the model'* — articulated at the vendor-CEO altitude on LangChain's own agent. Khan (Cline, one day later) gives the *competitor-customer-of-Anthropic vantage*: *'eventually we were able to beat Claude Code in Opus 4.5 evals... we figured out some tiny knobs that they couldn't figure out or they didn't optimize for.'* Both anchored on **terminal-bench as the eval substrate**, both demonstrating that **harness optimisation can outperform the vendor's own reference agent on the same model**. Same numerical magnitude (jump on terminal-bench), same conclusion (harness is load-bearing), now coming from three independent agent-vendors (LangChain via Chase, Cline via Khan, Trivedy in [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|March 2026]]) — the wiki's clearest single-claim convergence on *harness > model* with three concrete worked examples."
    confidence: 0.9
  - type: supports
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "**Customer-of-vendor empirical instantiation of Trivedy's *harness is load-bearing* thesis.** Trivedy (LangChain, March 2026): the original *Top-30-to-Top-5 on terminal-bench-2 via harness changes alone* claim — the *load-bearing component* the harness anatomy paper introduced. Khan / Cline gives the third independent empirical confirmation (after Chase / Interrupt 26): *'we made some changes to like CPU memory layer, we raised some timeouts, we improved the thinking behavior, and as we made those changes iteratively our scores just improved.'* Khan's *three-zones-of-improvement* framework (obvious flaws → real hill-climbing → danger-zone Goodhart-overfitting) is the wiki's clearest *taxonomy of harness-improvement work* — operationalising Trivedy's harness-anatomy framing into a stage-gated improvement process."
    confidence: 0.85
  - type: supports
    target: 2026-05-18-wolfe-agent-evaluation-detailed-guide
    via: "**The article-altitude treatment + the competitor-vendor practitioner talk converge on the same eval-discipline territory.** Wolfe (Substack, 18 May): the wiki's deepest article-altitude treatment — graders taxonomy, tau-bench / terminal-bench / SWE-bench coverage, LLM-as-judge calibration, swiss-cheese-evaluation pattern. Khan / Cline (22 May, four days later) is the *competitor-vendor practitioner-track altitude* on the same territory — *'objective metrics camp vs taste-is-king camp, truth in the middle'* + heuristics for interpreting others' evals + Stanford terminal-bench + Harbor + Modal containerisation infrastructure + three-zones framework. **Productive complement to** [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|the Anthropic-side talk]] published the same day."
    confidence: 0.8
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "**The manual-human-driven variant of Karten & Zhang's p/G/K/M continual-harness-adaptation framework.** Karten & Zhang (academic paper, 11 May 2026): *the agent edits its own harness based on eval feedback* (automated continual learning). Khan / Cline (this source, 22 May 2026) shows the **manually-driven equivalent at the production-coding-agent vendor altitude**: human engineer iterates the harness (CPU memory layer, timeouts, thinking behaviour, tool definitions, prompt) based on terminal-bench scores; same hill-climbing loop, human-in-the-loop variant. Khan's three-zones-of-improvement framework is the *taxonomy of where harness-adaptation effort flows* — Karten & Zhang's automated framework eventually has to make the same zone-1/zone-2/zone-3 distinctions Khan makes manually."
    confidence: 0.75
  - type: supports
    target: 2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering
    via: "**Same-channel same-conference companion talks.** Ng (20 May): the meta-shift framing — PM-bottleneck, cascading bottlenecks, AI-engineer hiring rubric (coding-agent fluency + building-blocks knowledge + generalist skills), parallel skill development. Khan (22 May): the *coding-agent practitioner-vendor altitude* on one specific skill in Ng's rubric — *coding-agent fluency*, articulated from inside building the coding agent. Two sources under DeepLearningAI channel-author within 48 hours triggers entity-page promotion for [[DeepLearningAI]] per the channel-as-entity convention (cf. YC Root Access, Lenny's Podcast)."
    confidence: 0.65
  - type: contradicts
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "**Productive tension on the *vendor-vs-customer relationship in the coding-agent layer*.** Tan & Hu (CS153, 20 May): *the 1000× engineer can be built with a $200/month Claude Max plan + Claude Code* — implicit framing is *the model vendor's reference agent is sufficient for outsized engineering output*. Khan / Cline (22 May, two days later): *'we beat Claude Code in Opus 4.5 evals'* — the customer-of-model-vendor explicitly out-performing the vendor's reference agent via harness engineering on the same model. The two claims are not directly contradictory (Tan/Hu's point is about Claude Code as a sufficient substrate; Khan's point is that a competitor's harness can do better on the same substrate), but they sit in **productive tension on the question of whether model-vendor reference-agents are the optimal harness or whether third-party harnesses systematically beat them**. Filed as `contradicts` with that tension explicit; the resolution probably depends on use case + how much eval-driven harness optimisation the third party invests in."
    confidence: 0.6
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "**The *harness-is-all-you-need* thesis instantiated at the production-vendor altitude.** Pan & Khattab (academic-paper-cohort, 4 May 2026): the *harness-is-all-you-need* counter-thesis to model-only-scaling — agentic capability is bottlenecked by harness engineering, not by base-model capability. Khan / Cline operationalises the same claim at the production-coding-agent vendor altitude: *'there's actually three things you're testing — the model, the harness (your agent scaffolding), and the problem space... if a new model from Anthropic comes out, I guarantee you you would have noticed that it works better in Claude Code compared to say Droid or Cursor sometimes — and it's like, if it's the same model, why is it that it's much better in Claude Code than some other agent? That's basically what you're testing here.'* The wiki's clearest empirical articulation of *the same model behaves differently in different harnesses* as the load-bearing observation under the harness-is-all-you-need thesis."
    confidence: 0.8
---

> *This talk by Cline's Ara Khan explains why they went from "evals are useless" to using them as a core part of my agent improvement loop. I share practical heuristics for interpreting, running, and creating evals, and why doing them anyway is better than pure "vibes".*

# Khan / Cline / DeepLearningAI — Evals Are Broken Use Them Anyway (AI Dev 26 x SF)

A ~25-minute practitioner-track session by **Ara Khan** at AI Dev 26 x San Francisco, published on the [[DeepLearningAI]] YouTube channel — 22 May 2026. Khan works at **[[Cline]]** (the open-source VS Code coding agent), running the eval-discipline programme for their coding agent. **The wiki's first deep articulation of the *customer-of-model-vendor* vantage on eval discipline** — paired with the model-vendor-side [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|Anthropic / Claude-channel session]] published the same day at the same conference.

## TL;DR

- **The two-camps framing**: most people are wrong about evals in one of two ways.
  - **"Objective metrics" camp** (epoch AI, artificialanalysis.ai, the Twitter-feed-of-benchmark-scores crowd): takes published numbers at face value; *"a lot of labs these days are just doing this game where just get the highest score on eval, doesn't matter how good the model is."* Models close in score are not actually equally good — *"if you spent like half an hour using any of these models, you'll know very quickly that these scores don't necessarily mean much."*
  - **"Taste is king" camp**: vibes-only, anthropomorphises models (*"oh, I like talking to her, she sounds nice"*); *"it's just at this point I don't even know where to start."*
  - The truth: in the middle. *"Evals are not the end-all-and-be-all. They're not completely useless. There are right ways to use them and there are wrong ways to use them."*
- **Three levels of eval engagement** (the talk's organising structure):
  1. **Level 1**: How to interpret *other people's* evals (heuristics for reading benchmark cards critically)
  2. **Level 2**: How to use evals to *improve your own agents*
  3. **Level 3**: How to *build your own* evals (*"if you have a lot of money and a lot of time"*)
- **Three heuristics for interpreting others' evals** (Level 1):
  1. **"Don't ever believe model-lab evals"** — *"they're close approximations but they're not perfect."* Real AI researchers routinely take published numbers with a grain of salt.
  2. **"Stay current but don't be the earliest adopter"** — *"let the dust settle"* 2 weeks before swapping models; the mental bandwidth of always being on the latest frontier isn't worth it for most teams.
  3. **"Look for evals close to your problem"** — generic benchmarks don't apply to specific use cases. *"SWE-bench was a very standard eval marker for coding agents for so long and then OpenAI came along and said, yeah, this benchmark is so saturated we can't use it anymore."*
- **Cline's eval journey** (Level 2 + Level 3, the load-bearing operational worked example):
  - **Started 2024** thinking *"evals are great but bro it's just about the vibes, it's just about the vibes"* — *"I talked to OpenAI, I talked to Anthropic last year and they were basically like yeah, evals are great but bro it's just about the vibes."* At the time evals were measuring sophomore-year algorithm problems (Fibonacci, unit-test-implementations) — useless for real-world coding work.
  - **Adopted Stanford's terminal-bench**: 89 real-world software-engineering problems (database issues, race conditions, frontend bugs, regex bugs, latency, caching) at the right altitude for real coding agents. Critical features: agents run for 5-45 minutes per problem, deterministic unit tests check did-the-file-get-made / does-it-run / does-it-pass.
  - **Used Harbor** (terminal-bench's containerised isolated-environment infrastructure) — earlier evals ran sequentially over 6-7 hours with environments interfering with each other; Harbor parallelises via containerisation.
  - **Used Modal** as the underlying infrastructure for parallel containerised eval environments.
  - **Tracked: turns / tool calls / tokens / run-time** alongside pass/fail. *"Sometimes there are models which are very very good at performance but they'll take 45 minutes because the inference is so slow."*
  - **"Eventually we were able to beat Claude Code in Opus 4.5 evals"** — *"we figured out some tiny knobs that they couldn't figure out or they didn't optimize for."* This generalises: *"we found over time that we're able to beat Claude Code in other evals as well."*
- **The three-things-being-tested framework** (the talk's most-portable analytical primitive): when you run an eval, you're testing **(1) the model, (2) the harness (your agent scaffolding), and (3) the problem-space alignment**. The harness-as-confounder observation: *"if a new model from Anthropic comes out, I guarantee you you would have noticed that it works better in Claude Code compared to say Droid or Cursor sometimes. If it's the same model, why is it that it's much better in Claude Code than some other agent? That's basically what you're testing here — sometimes it's a great model and your harness just hasn't done the justice that the model needs to be able to make sense of it."*
- **The three-zones-of-improvement framework** (the talk's most-portable strategic primitive): once you're hill-climbing on evals, your work falls in one of three zones:
  - **Zone 1: Obvious flaws** — broken read-file tool, broken agent turns, broken checkpoints. *"Tells you your agent is broken on a fundamental level."* Fix these first; this is where evals are most clearly useful for triage.
  - **Zone 2: Real hill-climbing** — *"the philosophical aspects of how to make my agent better."* Too many tools, wrong tools, prompt-engineering issues, retry logic. *"Instead of sitting around and pontificating philosophically whether or not your agent is good, you can have very nuanced judgments by giving it real problems to solve."*
  - **Zone 3: The danger zone** — Goodhart-style overfitting. *"As soon as you give them a metric, all they do is just optimize for the number — they don't really care what the problem at hand is. They'll just overfit the model, change the prompt such a way that they only pass this specific task, add weird skills."* Don't let zone-3 dynamics take over.
- **Closing doctrine**: *"Find a benchmark that works for you. Build some evals if you can. You should hill-climb — honestly hill-climb means just improving your score on the eval. And then even if you get a good score, you always need to make sure you're passing the vibe check... is this a sensible agent? Is it actually solving our problems?"* Eval discipline + vibe-check sanity-check; **neither alone is sufficient.**

## What was actually ingested

The full ~24:36 transcript via the youtube-transcript-skill Playwright path (succeeded on first attempt with `--timeout 60000`; the Anthropic-side talk on the Claude channel, published the same day, required yt-dlp fallback). 699 ASR segments. ASR rendered the speaker's first name as *"Era"* in segment 1 (*"I'm Era"*) — the published title says *"Ara Khan"* and the description confirms; standardising to *Ara Khan* throughout. Stage cues and audience interjections retained. Full raw at [`raw/videos/2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway.md`](../../raw/videos/2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway.md).

## Substantive content

### 1. The two-camps framing (~0:48–4:46)

Khan opens with the talk's headline claim: *"my fundamental claim of this entire conversation is that people are wrong about evals."* The wrongness shows up in two opposite camps.

**The "objective metrics" camp**: takes published benchmark scores at face value. Examples Khan names: epoch AI, artificialanalysis.ai, the Twitter-feed-of-benchmark-scores. The mechanical critique: *"if you notice like there's sonnet 4.6 at 52 and then you'll notice a few other models quite close to it, it's very difficult to make the claim that the models which are close to each other in the score are actually equally as good because they're not."* The sociological critique: *"tons and tons of labs these days are just doing this game where just get the highest score on eval. Doesn't matter how good the model is, it will get the tweets in, it will get a clout in, and then you pull people in and then who knows maybe the model's good, maybe not."* Khan attributes a tweet from *"Francis"* (likely [[François Chollet]]) calling out Meta's Llama 4 benchmark-maxing as the canonical example.

**The "taste is king" camp**: vibes-only, no numbers. Khan's characterisation: *"who don't believe in the numbers at all. Who think that these numbers are completely pointless. It's just made up. It's all about wibes, man, it's all about wibes... if you talk to them they'll say things like 'oh why do you like Claude models?' and they'll say 'oh, I like talking to her, she sounds nice.' They'll talk about an AI model like it's an actual person. And it's just at this point I don't even know where to start."*

The middle path Khan argues for: *"Evals are not the end-all-and-be-all. They're not completely useless. There are right ways to use them and there are wrong ways to use them."* This is the talk's organising thesis — both extremes are wrong, the discipline lives in the middle.

### 2. Three levels of eval engagement + three heuristics for interpreting others' evals (~4:46–9:30)

Khan structures the talk around three levels of eval engagement:

1. **Level 1**: Interpreting other people's evals (the heuristics below)
2. **Level 2**: Using evals to improve your own agents
3. **Level 3**: Building your own evals (*"if you have a lot of money and a lot of time"*)

The three heuristics for Level 1:

**Heuristic 1 — Don't ever believe model-lab evals.** *"Whenever labs come out with whatever eval numbers come out for mythos preview or GPT-5.5 or whatever, they're great and they're probably accurate and those models are I'm sure they're very decent. I'm just saying don't take those numbers as a word of god. You have to use your own discernment. They're close approximations but they're not perfect."* Khan cites a tweet making the empirical claim that *"a lot of people they will routinely dismiss eval results... a lot of times real AI researchers would kind of take them with a grain of salt — and I think that's the right way to think of eval."*

**Heuristic 2 — Stay current but don't be the earliest adopter.** *"If you look at the SOTA score, every couple of months the SOTA model changes and it changes very quickly... If you keep playing this game of 'hey I want the best thing all the time,' the mental bandwidth that you'll spend trying to always be on top is just not worth it."* Khan's prescription: *"You want new models to come out, you want new things to come out — you got to wait out for a couple weeks and then you got to be like okay, let the dust settle, and that's when you try your own thing."* Self-disclosure: *"There are people like me who will spend all their time trying to find out what the new thing is, what's the best frontier thing at any point in time — and that is what I do for a living. So sure, I'll do that. But I don't think you should do that."*

**Heuristic 3 — Look for evals close to your problem.** *"When a lot of these model apps come up with a score, they're just generic general-purpose eval. They may not necessarily apply to you. I think as a problem solver, you should always look for eval close to your problem or as close as you can get."* The canonical example Khan names: *"SWE-bench was a very standard eval marker for coding agents for so long and then OpenAI came along and they said, yeah, this benchmark is like so saturated we can't use it anymore. If you've been in this space you would have known that this eval was saturated so hard that right now model apps come out they don't even mention the score because that's how saturated some of those evals are."*

### 3. Cline's eval journey — terminal-bench + Harbor + Modal (~9:30–17:22)

The talk's load-bearing operational worked example. Khan starts with the 2024 baseline at Cline: *"I talked to OpenAI, I talked to Anthropic last year and they were basically like yeah, evals are great but bro it's just about the vibes, it's just about the vibes."* The reason evals weren't taken seriously: *"the evals were just measuring something completely wrong. A lot of evals would have things like Fibonacci sequence — implement the Fibonacci sequence, implement the unit test — these algorithms problems that you solved in your sophomore year of university. It doesn't apply at all to your real-world coding experience."*

The pivot moment: *"Cline wanted to build our own evals which were more applicable, more accurate, more pertaining to real-world software problems — and as we were working on them, we found this incredible group from Stanford ... and they came out simultaneously with this benchmark called terminal-bench."*

**Terminal-bench** (Khan's framing — note this is the same eval substrate [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] cites for LangChain's Top-30-to-Top-5 claim):

- **89 problems** at the *real software-engineering-task* altitude — database issues, race conditions, frontend bugs, regex bugs, latency issues, caching bugs, implementation aspects
- **Agentic eval format**: agents run for 5-45 minutes per problem (web search, install dependencies, sandbox access, read files, edit files, run tests)
- **Deterministic unit-test grading**: did the file get made? does it run? does it pass the test?
- **Cross-agent applicability**: easy to make terminal-bench evals work with any coding agent — Codex, Claude Code, Cline, etc.

**Harbor** (terminal-bench's containerisation infrastructure): *"You make isolated containerised environments where you set up the whole thing. You set up the machine, you set up the environment, you install the dependencies — everything that you need in that specific machine in an isolated container, and then you run the agent on it."* The wins over sequential pre-Harbor approaches: parallelisation (no 6-7 hour serial runs), no cross-contamination of environments between tasks.

**Modal** (Cline's infrastructure layer): *"Model is the infrastructure layer that helps us build these parallelised containerised environments so that whenever our eval task would run they would run in different containers."* The shout-out to Modal as the dev-substrate.

The metrics Khan tracks per eval run: **turns / tool calls / tokens / total run-time** alongside pass/fail. The cost-quality framing: *"as much as I would love for everyone to use the most expensive frontier model for every problem, I don't think that's how the world works. We don't have infinite amount of money. Sometimes it just makes more sense to use Deep Seek V4 for Flash, which is like 1/50th the cost of another model."*

### 4. The three-things-being-tested framework (~17:24–20:14)

The talk's most-portable analytical primitive. When you run an eval, you're testing three things simultaneously:

1. **The model** — *"obviously you're testing the model whether or not it's good."*
2. **The harness** — *"your agent scaffolding. So when you write the agent, it's possible that there's a model that's really really good but you just wrote it the wrong way."*
3. **The problem-space alignment** — *"the problem same — because you could be solving a stupid problem that just doesn't apply to your eval."*

The harness-as-confounder observation (the wiki's clearest single empirical articulation of the *same-model-different-harness-different-results* phenomenon):

> *"The best explanation is that if a new model from Anthropic comes out, I guarantee you you would have noticed that it works better in Claude Code compared to say Droid or Cursor sometimes. It's like, if it's the same model, why is it that it's much better in Claude Code than some other agent? Why is that? And that's basically what you're testing here — sometimes it's a great model and your harness just hasn't done the justice that the model needs to be able to make sense of it."*

The implication for vendor competition: harness-engineering is a real moat against model-vendor reference agents.

### 5. The Cline-beats-Claude-Code anchor + three-zones framework (~20:14–22:55)

The headline operational claim: *"We ran the eval the first time, we got an original score. Then we made some changes to like CPU memory layer, we raised some timeouts, we improved the thinking behavior, and as we made those changes iteratively our scores just improved — and eventually we were able to beat Claude Code in Opus 4.5 evals. And what we found over time is that we're able to beat Claude Code in other evals as well, because we just figured out some tiny knobs that they couldn't figure out or they didn't optimize for."*

This is the **third independent primary-source confirmation** of the *harness-changes-alone-improve-eval-scores-substantially-on-the-same-model* pattern in the wiki, after [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain]] (March 2026, Top-30 → Top-5 on terminal-bench-2) and [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] (21 May 2026, restating the Trivedy claim from the CEO stage). Khan's vantage is **customer-of-model-vendor** — Cline runs *on* Anthropic models, and explicitly out-performs Anthropic's reference agent (Claude Code) on the same model via harness optimisation.

The strategic takeaway Khan draws: *"If you're working on an interesting problem, you can just be like 'hey, let me figure out what I'm doing. Let me figure out what my competitor is doing. Let me build some great evaluators... and I'm just going to beat them. I'm just going to do it so much better than them.'"*

The **three-zones-of-improvement framework** (the second most-portable strategic primitive in the talk):

**Zone 1 — Obvious flaws** (~21:17): *"The obvious flaws of like, okay, what is obviously wrong with your agent — read-file tool is wrong, agent turns are broken, checkpoints are broken. These things tell you that your agent is broken on a fundamental level."* Fix these first; this is where evals are most clearly useful for triage. *"Once you fix those basic things, your agent starts to work — it makes it look like okay, it's actually working, it's actually functioning."*

**Zone 2 — Real hill-climbing** (~22:00): *"The philosophical aspects of how to make my agent better. A lot of times you'll find that it's like you have all kinds of stuff in the prompt, in the tool call, in the tool-call definitions, in the logic of retries — that your agent is just not doing well. To some extent it's your fault of prompt engineering. Maybe it's a fault of using too many tools. Maybe you're using too few tools. Maybe you're using the wrong tools."* The strategic value: *"instead of sitting around and pontificating philosophically whether or not your agent is good, you can have very nuanced judgments of whether or not your agent is actually good by giving it real problems to solve."*

**Zone 3 — The danger zone** (~22:53, Goodhart's-law dynamics): *"As soon as you give them a metric, as soon as you give them a number to optimise for, all they do is just optimize for the number. They don't really care what the problem at hand is. They'll just overfit the model, change the prompt such a way that they only pass this specific task, add weird skills and stuff. So that's not nice — you want to be cautious that you're improving but not overfitting or doing something wrong."* The wiki's clearest single articulation of *Goodhart's law in eval-driven coding-agent development.*

### 6. Closing doctrine + the open-source-model discovery (~23:30–24:36)

The talk's closing prescription: *"If I could give you a final word, it is that find a benchmark that works for you. Build some eval if you can. You should hill-climb — honestly hill-climb means just improving your score on the eval. And then even if you get a good score, you always need to make sure you're passing the vibe check. You need to know on some emotional level that yes, my agent makes sense — it's not just about benchmarks, is this a sensible agent? Is it making sense? Is it actually solving our problems?"*

The eval + vibe-check pairing: **neither alone is sufficient.** Evals catch what vibes miss (regressions, edge cases, eval-saturation-on-other-people's-benchmarks); vibes catch what evals miss (Goodhart-overfitting, user-experience signals that no number tracks).

The open-source-model coda Khan ends with: *"Every time a new model comes out, we try eval. We improve the new model experiences with it. We're using a lot of open source models now. We're trying to support and improve eval — and I think that we never would have figured out all these beautiful nuances of these open-source models which are incredible and much cheaper had we not run eval. We just would have completely ignored them and just worked on vibes."* The eval-discipline-enables-multi-model-portfolio-management thesis — Cline can support DeepSeek V4 / open-source models alongside frontier-Anthropic models *because* their eval discipline catches per-model strengths and weaknesses that vibes-only would miss.

## Linked entities and concepts

**Entities directly named or substantively discussed:**

- **[[Cline]]** — Khan's employer; the open-source VS Code coding agent that explicitly out-performs Claude Code on certain Opus 4.5 evals. **Cross-page-presence promotion warranted now**: Cline is referenced in [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic]], [[2026-05-15-osmani-agent-harness-engineering|Osmani]], and the [[concepts/agentic-engineering|agentic-engineering]] + [[concepts/agent-harness|agent-harness]] concept pages — four existing wiki cross-references + this solo-headlining ingest = entity-page-promotion via cross-page-presence judgment.
- **[[Ara Khan]]** — Dangling first-mention (Cline employee leading the eval-discipline programme). Promote on second-source mention.
- **[[DeepLearningAI]]** — channel-entity; this is the **second source under this `author:` value** ([[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng / AI Dev 26]] was the first) → **entity-page promotion triggers per the channel-as-entity convention** (cf. YC Root Access, Lenny's Podcast).
- **[[Anthropic]]** — substantive cross-references (model vendor; Claude Code as the reference-agent Khan beats; Sonnet / Opus models); source-count: increment.
- **[[OpenAI]]** — substantive cross-reference (Khan talked to OpenAI in 2024 re: evals; SWE-bench-deprecation citation); source-count: increment.
- **[[Stanford SAIL]]** — Dangling first-mention (the *"incredible group from Stanford"* that built terminal-bench; Khan doesn't name the specific institute affiliation but Stanford SAIL is the implied institutional home).
- **terminal-bench** — substantive product mention; **Dangling first-mention as a named eval product** (it's been referenced in passing in earlier sources but never deeply treated). Concept-page candidate on second-source-mention.
- **Harbor** — Dangling first-mention (terminal-bench's containerised eval infrastructure).
- **[[Modal]]** — Dangling first-mention (the parallel containerised infrastructure Cline uses for eval runs).
- **DeepSeek V4 Flash** — Dangling first-mention (the *"1/50th the cost"* model Khan uses as the cost-conscious alternative).
- **Droid** — Dangling first-mention (competitor coding agent referenced in the harness-confounder example).
- **[[Cursor]]** — substantive cross-reference (competitor coding agent in the harness-confounder example).
- **Codex** — referenced as a coding-agent alternative.
- **François Chollet** — implied attribution of the *"Francis"* tweet about Meta benchmark-maxing (ASR-uncertain attribution; the wiki should not commit to François Chollet without verification).

**Concepts touched substantively:**

- **[[concepts/agent-harness|agent-harness]]** — *the harness is one of three things you're testing* + *same model behaves differently in different harnesses* + Khan's three-zones-of-improvement framework as the operational taxonomy of harness-improvement work. Source-count: +1.
- **[[concepts/agentic-engineering|agentic-engineering]]** — eval-driven hill-climbing as a core agentic-engineering loop primitive + Goodhart's-law-zone-3 as the discipline-failure-mode warning. Source-count: +1.
- **[[concepts/agent-development-lifecycle|agent-development-lifecycle]]** — the eval phase of the ADLC, operationalised at the customer-of-model-vendor practitioner altitude; complementary to Chase's vendor-CEO altitude. Source-count: +1.
- **[[concepts/foundation-models|foundation-models]]** — *don't believe model-lab evals* + *stay current but don't be the earliest adopter* + the cost-portfolio framing (DeepSeek V4 Flash @ 1/50th cost). Source-count: +1.

**Dangling first-mentions** (deferred to second-source): Ara Khan, terminal-bench (concept-page candidate), Harbor, DeepSeek V4 Flash, Droid, François Chollet (uncertain attribution).

## Caveats

- 25-minute practitioner-track session at a vendor-organised conference (AI Dev 26, run by [[DeepLearningAI]]) — Khan is presenting Cline's eval-discipline programme; some promotional sub-motive is present (the *we beat Claude Code* anchor is good for Cline's positioning).
- The *we beat Claude Code on Opus 4.5 evals* claim is **founder-vantage, unaudited, and specific to a particular eval set (terminal-bench) and a particular model snapshot (Opus 4.5)**. The wiki should treat this as a load-bearing claim from a specific competitor at a specific time, *not* as a generalisable claim that Cline systematically out-performs Claude Code across all use cases.
- The *"talked to OpenAI, talked to Anthropic last year and they were basically like yeah, evals are great but bro it's just about the vibes"* anecdote is Khan's personal recollection from 2024; OpenAI and Anthropic's actual eval-discipline programmes likely had more rigour than the *vibes-only* characterisation suggests. Treat as Khan's framing-from-customer-vantage, not as Anthropic's / OpenAI's self-description.
- The *"Francis"* tweet attribution is ASR-uncertain — the surname isn't given and the context (about Llama 4 being benchmark-maxed) is consistent with [[François Chollet]] but not verified. The wiki should not commit to the attribution without external confirmation.
- The terminal-bench task count (*"89 problems"*) is Khan's stated number; this may be a particular snapshot and the actual current task count may differ.
- The DeepSeek V4 Flash *"1/50th the cost"* claim is a cost-magnitude framing, not a precise cost-comparison-at-a-specific-context-window-length. Treat as directional.
- The three-zones-of-improvement framework is Khan's own framing — useful as a portable analytical primitive, but not (yet) cross-referenced against other eval-engineer taxonomies.
- ASR-uncertainty on the speaker's name: transcript opens *"I'm Era"* (segment 1) — the published video title gives *"Ara Khan"*; standardising on *Ara Khan* throughout, with this note as the audit trail.
- The talk does not deeply demo Cline's eval setup live — Khan presents the framework + the journey + the headline claims, but doesn't show the actual eval-running infrastructure on screen. The substantive content is the *framework + heuristics + worked-example narrative*, not the *infrastructure walkthrough*.
