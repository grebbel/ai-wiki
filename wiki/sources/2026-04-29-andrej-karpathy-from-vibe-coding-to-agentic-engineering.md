---
type: source
kind: video
title: "Andrej Karpathy: From Vibe Coding to Agentic Engineering"
author: ["Sequoia Capital"]
publisher: "Sequoia Capital (AI Ascent)"
url: "https://youtu.be/96jN2OCOfLs?si=4CPfTORIF_Cn8E2I"
date_published: 2026-04-29
date_ingested: 2026-05-08
length: "~29:42 minutes (transcript ~1,800 lines)"
raw: "../../raw/videos/andrej-karpathy-from-vibe-coding-to-agentic-engineering.md"
tags: [software-3.0, agentic-engineering, vibe-coding, jagged-intelligence, animals-vs-ghosts, agent-native-infrastructure, verifiability, llm-knowledge-base, karpathy]
confidence: 0.80
last_confirmed: "2026-05-08"
---

# Andrej Karpathy: From Vibe Coding to Agentic Engineering

> Andrej Karpathy (co-founder of OpenAI, former head of AI at Tesla, and now founder of Eureka Labs) talks with Sequoia partner Stephanie Zhan at AI Ascent 2026 about what's changed in the year since he coined "vibe coding." He explains why he's never felt more behind as a programmer, why agentic engineering is the more serious discipline taking shape on top of vibe coding, and why we should think of LLMs not as animals but as ghosts: jagged, statistical, summoned entities that require a new kind of taste and judgment to direct. He also touches on Software 3.0, the limits of verifiability, and why you can outsource your thinking but never your understanding.
>
> *— [Sequoia Capital YouTube channel description](https://youtu.be/96jN2OCOfLs)*

The **inaugural guest interview** at Sequoia Capital's *AI Ascent* event (29 April 2026) — ~30 minutes with [[Andrej Karpathy]] (ex-OpenAI co-founder; ex-Tesla Autopilot lead; coined *vibe coding* in 2024). The interview is structured around ten thematic questions, anchored on Karpathy's claim that **"I've never felt more behind as a programmer"** — a startling line from one of the field's most prolific practitioners — which he traces to a sharp **December 2025 phase change** when the latest agentic-coding workflows tipped from *"useful but needs corrections"* to *"I just trust it now."*

The interview lays out Karpathy's current synthesis of where AI engineering is going: a **Software 3.0** computing paradigm (prompting as programming; the LLM as interpreter; the context window as the program); **agentic engineering** as a discipline distinct from vibe coding; and a **jagged-intelligence** framing for why current models simultaneously refactor 100k-line codebases and tell you to walk to a 50-meter-away car wash.

This source has two unusual properties for the wiki:

1. **Karpathy is the upstream-spec author for this entire repo.** The repo's [`llm-wiki.md`](../../llm-wiki.md) conceptual spec is Karpathy's own articulation of the LLM-knowledge-base pattern; CLAUDE.md cites him at the top. In this interview Karpathy explicitly describes his **continued use of an LLM-knowledge-base workflow** (29:00–29:30): *"I really enjoy whenever I read an article I have my wiki that's being built up from these articles and I love asking questions about things… anytime I see a different projection onto information, I always feel like I gain insight."* This is the **upstream-spec author confirming the pattern is still load-bearing for him in 2026** — a rare and citation-worthy artifact.
2. **The video is an interview, not an explainer.** Per the wiki's `kind: video` schema, `author:` is the channel (*Sequoia Capital*); the substantive content owner ([[Andrej Karpathy]]) is the *interview subject*, named throughout the body. This is the convention's first interview-format test case; it works cleanly because every claim is attributable in body wikilinks.

## TL;DR

- **The December moment**: a single-month phase change in late 2025 when agentic-coding workflows started "just working" without corrections. Karpathy: *"I just trusted the system more and more, and then I was vibe coding."*
- **[[software-3.0|Software 3.0]]** completes a 1.0/2.0/3.0 trilogy: 1.0 = explicit rules (code); 2.0 = learned weights (data + neural-net architecture); **3.0 = prompting** — the LLM is a *programmable computer*, the *context window is the program*, the LLM is the *interpreter*. Implication: the unit of programming work shifts from "function definition" to "what is the piece of text you copy-paste to your agent?"
- **Two worked examples** that ground the framing:
  - **Agents as the installer**: OpenClaude's install instructions are "copy-paste this text into your agent." The agent inspects environment, performs intelligent actions, debugs in the loop. The deliverable is the prompt-text, not the install script.
  - **Menu Gen vs raw prompts** *(the load-bearing example)*: Karpathy v-coded a Menu Gen app (photo of menu → OCR → image-gen → overlay). Then realised: *"just give Gemini the photo + 'use Nanobanana to overlay items onto the menu'"* returns the same image with items rendered into the pixels. **"All of my menu gen is spurious. That app shouldn't exist."** The lesson is *not "Software 3.0 is a speed-up"* but *"Software 3.0 makes new things possible that weren't possible before"* — and entire classes of glue-code apps now look spurious.
- **Verifiability + jagged intelligence** (the headline framing for *why* models are uneven):
  - Traditional computers automate what you can **specify in code**. LLMs automate what you can **verify**.
  - Frontier labs train via massive RL → verification rewards → models peak on **verifiable** domains (math, code, adjacent) and stagnate elsewhere.
  - Two factors of jaggedness: (1) verifiable + (2) **labs care** — the chess-improvement from GPT-3.5 → GPT-4 was OpenAI deliberately adding chess data, not generic capability scaling. *"You're slightly at the mercy of whatever the labs are doing."*
  - The car-wash example (*"How is it possible Opus 4.7 simultaneously refactors a 100k-line codebase and finds zero-day vulnerabilities, yet tells me to walk 50m to a car wash because it's so close?"*) is the canonical jaggedness-in-2026 story.
- **[[agentic-engineering|Agentic engineering]] vs [[vibe-coding|vibe coding]]** (the title contrast):
  - **Vibe coding** = *raising the floor* (everyone can vibe code anything; this is amazing).
  - **Agentic engineering** = *preserving the quality bar* of professional software at agent speed. *"You're not allowed to introduce vulnerabilities due to vibe coding. You're still responsible for your software."*
  - Karpathy explicitly calls agentic engineering an **engineering discipline** with a very high ceiling: *"The 10× engineer used to be the upper bound; agentic engineering pushes far past 10×."*
- **Animals vs ghosts**: *"We're not building animals; we are summoning ghosts."* Animals have intrinsic motivation, fun, curiosity, empowerment — products of evolution. LLMs are statistical simulation circuits with RL bolted on top. *"If you yell at them, they're not going to work better or worse."* Karpathy notes this is "a little bit philosophising" — a mindset, not a recipe.
- **Hiring for agentic engineering is broken**: most companies still give puzzle-style interviews. Karpathy's proposed format: *"give me a really big project — write a Twitter clone for agents, secure it, then I'm going to use 10 codecs to try to break it. They should not be able to break it."* Project-scale, adversarial, build-and-defend.
- **Agents are intern entities**: remarkable but error-prone in surprising ways. Vivid example: Karpathy's Menu Gen agent associated Stripe and Google accounts by *email match* — but emails are not persistent user IDs. The agent missed the architectural error. **Humans own: aesthetics, judgment, taste, oversight, the spec/plan.** *"You're in charge of the design and the engineers (agents) are doing the fill-in-the-blanks."*
- **Agent-native infrastructure** (his pet peeve): *"Everything is still fundamentally written for humans."* Decompose workloads into **sensors over the world + actuators over the world**. Make data structures legible to LLMs. Test for agent-native infra: *"give an LLM a prompt, build menu gen, deploy, done — don't touch anything."*
- **What's worth learning when intelligence is cheap**: *"You can outsource your thinking, but you can't outsource your understanding."* Humans become the bottleneck for: knowing what's worth building, why, and how to direct agents. Karpathy: *"I still have to somehow… information still has to make it into my brain."*
- **The closing artifact** (29:00–29:30): Karpathy describes using **LLM knowledge bases / wikis built from articles** as his primary mechanism for processing information. *"Anytime I see a different projection onto information, I always feel like I gain insight."* This is the **upstream-spec author confirming the very pattern this repo implements** — a rare citation.

## What was actually ingested

Full transcript, ~29:42 minutes / ~1,800 lines. Ten thematic sections tracked by the transcript's own headers; no sponsor break.

| Time | Section | Substantive claim |
|---|---|---|
| 0:02–0:43 | Introduction | Sequoia AI Ascent's first-ever guest; framing as "felt more behind as a programmer" |
| 0:44–2:28 | Feeling Behind as a Coder | The **December moment** — single-month phase change to "just trust the agent" |
| 2:28–3:43 | Software 3.0 Explained | 1.0 = rules, 2.0 = weights, **3.0 = prompting**; LLM as programmable computer |
| 3:44–4:50 | Agents as the Installer | Install scripts → "copy-paste this text to your agent" |
| 4:50–7:37 | Menu Gen vs Raw Prompts | Software 3.0 makes new things possible, not just speeds up old things |
| 7:37–9:41 | What's Obvious by 2026 | Possible flip: neural net = host process, CPU = co-processor |
| 9:41–13:38 | Verifiability and Jagged Skills | LLMs automate what's verifiable; labs care + verifiability = jaggedness |
| 13:40–15:47 | Founder Advice and Automation | Build your own RL environments; ultimately "everything is automatable" |
| 15:47–25:16 | From Vibe Coding to Agentic Engineering | The title concept: floor vs ceiling; intern entities; animals vs ghosts |
| 25:18–29:42 | Agents Everywhere and Learning | Agent-native infra; outsource thinking ≠ outsource understanding; **wikis-from-articles** |

## Software 3.0 — the headline framing

Karpathy's 1.0 / 2.0 / 3.0 trilogy is the wiki's first cleanly-named definition of *what is qualitatively new* about the LLM era as a **computing paradigm** (rather than a model-class or a deployment-pattern):

| Paradigm | Programming substrate | Programmer's job |
|---|---|---|
| **Software 1.0** | Source code (explicit rules) | Write the code |
| **Software 2.0** | Datasets + neural-net architectures (learned weights) | Curate the dataset, design the architecture, train the network |
| **Software 3.0** | **Prompts / the context window** | Write the prompt; the LLM is the interpreter |

> *"Software 3.0 is about your programming now turns to prompting and what's in the context window is your lever over the interpreter that is the LLM that is interpreting your context and performing computation in the digital information space."*

Two operational consequences Karpathy makes explicit:

1. **The unit of work is the copy-paste-into-agent text** — see "Agents as the installer" below.
2. **New things become possible**, not just faster. Karpathy explicitly contrasts the *speed-up* framing (Software 3.0 makes existing apps faster) with the *new-things* framing (Software 3.0 makes apps possible that couldn't exist before — e.g., wikis built automatically from documents). *"I almost think that that's more exciting."*

The Software 3.0 framing is logically *upstream* of the wiki's existing [[agent-harness]] construct: a Software 3.0 program needs a runtime to execute it; that runtime is the harness. Karpathy doesn't use the harness vocabulary in this interview, but the architectural relationship is direct.

See [[software-3.0]] for the wiki's full treatment.

## Agents as the installer (worked example #1)

The setup: when **OpenClaude** released, you'd expect a `bash` install script — fragile, OS-specific, balloons in complexity to handle every platform. Instead the install instructions are *"copy-paste this text into your agent."* The agent:

- Inspects your environment (OS, Python version, existing tools, paths).
- Performs intelligent actions to make things work.
- **Debugs in the loop** — sees an error, tries a fix, retries.

The reframe Karpathy draws:

> *"You're working now in the Software 3.0 paradigm where you don't have to precisely spell out all the individual details of that setup. The agent has its own intelligence that it packages up and then it follows the instructions… so much more powerful, right? So I think that's a very different kind of way of thinking about it: what is the piece of text to copy-paste to your agent? That's the programming paradigm."*

The deliverable shifts from *"install script that handles every platform"* to *"prose description of what the install needs to accomplish"* — and the agent's general intelligence covers the platform variation.

## Menu Gen vs raw prompts (worked example #2 — the load-bearing one)

Karpathy v-coded **Menu Gen**: photo of restaurant menu → OCR titles → image-gen for each item → overlay onto the menu. Wrapped in Vercel infra; pretty good app. *"Then I saw the Software 3.0 version of this which blew my mind."*

The Software 3.0 version: just give **Gemini** the photo and prompt *"use Nanobanana to overlay items onto the menu."* Nanobanana **returns an image that is exactly the photo** — same composition, same lighting, same layout — but with the menu items rendered into the pixels.

> *"All of my menu gen is spurious. It's working in the old paradigm. That app shouldn't exist."*

The general claim Karpathy extracts:

- The Software 3.0 paradigm is **more raw**: the neural net does more, the surrounding code does less.
- **Reframe is required**: don't think *"speed up of what existed"*; think *"new things are now possible."*
- The reframe extends beyond code: Karpathy specifically calls out **LLM knowledge bases / wikis built from documents** as something *"that couldn't exist before because there was no code that would create a knowledge base based on a bunch of facts."* This is the same artifact as the closing-section reference (see *Outsource thinking ≠ outsource understanding* below) — Karpathy's own continued use of an LLM wiki workflow.

The general implication for builders: **inspect every glue-code app for whether it's spurious in the Software 3.0 paradigm.** The "speed-up" lens hides a lot of work that simply shouldn't exist anymore.

## What's obvious by 2026 (the extrapolation question)

Asked the year-2026 equivalent of *"building websites in the '90s, mobile apps in the 2010s, SaaS in the cloud era"*, Karpathy reaches for a more radical claim:

> *"You could imagine completely neural computers in a certain sense. You feed raw videos like imagine a device — takes raw video or audio into basically what's a neural net — and uses diffusion to render a UI that is unique for that moment in a certain sense."*

His historical reference: in the 50s and 60s, people were unsure whether computers would look like *calculators* or like *neural nets*. The calculator path won — and now neural nets run *virtualised* on top of classical computers. Karpathy's hypothesis: **this might flip**. The neural net becomes the **host process**; the CPU becomes the **co-processor** (used for tool-use over deterministic tasks, as a "historical appendage").

He frames this as TBD: *"That progression is TBD, I would say."* But the direction — neural-as-host, CPU-as-tool-use-coprocessor — is the most concrete extrapolation in the interview.

## Verifiability and jagged intelligence — the cause-of-jaggedness framing

The wiki already holds [[jagged-frontier]] (per Dell'Acqua et al. 2026, the *task-level* description of where AI is good vs. bad). Karpathy's framing in this interview is upstream of that observation: *why is the frontier jagged?*

> *"Traditional computers can easily automate what you can specify in code, and this latest round of LLMs can easily automate what you can verify."*

The mechanism:

1. Frontier labs train these LLMs in **giant reinforcement-learning environments** — the models receive verification rewards.
2. Models **peak in verifiable domains** (math, code, adjacent areas) and stay rough elsewhere.
3. **Two factors** combine to make a domain "fly" or "struggle":
   - **Verifiable**: the domain has a check function (correctness can be scored).
   - **Labs care**: the domain made it into the data distribution / RL environment mix.
4. Without one of these, you're "out of the RL circuits" — you have to fine-tune yourself.

Karpathy's most pointed example of how *"labs care"* materialises:

> *"From GPT 3.5 to GPT-4 people noticed that chess improved a lot, and a lot of people thought 'oh well, it's just a progression of capabilities.' But actually, a huge amount of chess data made it into the pre-training set. Someone at OpenAI decided to add this data, and now you have a capability that just peaked a lot more. So we are slightly at the mercy of whatever the labs are doing, whatever they happen to put into the mix. And you have to actually explore this thing that they give you that has no manual."*

The canonical jaggedness story for 2026 (which Karpathy uses to replace the older "how many letters in strawberry" example):

> *"Opus 4.7 will simultaneously refactor a 100,000-line codebase or find zero-day vulnerabilities, and yet tells me to walk to this car wash that's 50 meters away because 'it's so close.' This is insane."*

The implication for builders is operational, not philosophical: **stay in the loop**, treat models as tools, **explore which RL circuits you're in for your application**. If you're out of the circuits, fine-tune your own. See [[jagged-frontier]] for the cause-and-effect synthesis with Dell'Acqua's task-level observation.

### Animals vs ghosts (the mindset framing)

Karpathy's framing for *what kind of intelligence* LLMs are:

> *"We're not building animals, we are summoning ghosts. Jagged forms of intelligence shaped by data and reward functions, but not by intrinsic motivation or fun or curiosity or empowerment — things that came about via evolution."*

He explicitly discounts the framing's operational power: *"I'm not sure if it actually has like real power… it's a little bit of philosophising."* What it *does* give you is a **mindset**:

- **No anthropomorphic levers**: *"If you yell at them, they're not going to work better or worse — it doesn't have any impact."*
- **No assumption of consistent intrinsic motivation**: the LLM doesn't get bored, doesn't get curious, doesn't have empowerment drives that shape its outputs.
- **Statistical simulation substrate** (pre-training) + **RL bolt-on** (post-training): the model is the sum of these, not an animal mind.

The mindset shapes how to debug agent failures: don't assume the agent "wants" something; assume the agent is a statistical circuit shaped by what was rewarded. Be *suspicious* of confident outputs and *figure it out over time*.

## Founder advice and automation

When asked what founders should build given the lab-velocity in coding/math:

- **Verifiability remains tractable even when labs aren't focusing on it.** If your domain is verifiable, you can build your own RL environments and pull the fine-tuning lever yourself. *"You can use your favourite fine-tuning framework and pull the lever and get something that actually works pretty well."*
- Karpathy hints at *"some very valuable RL environments that I think are not part of the [labs' mix]"* — declines to name specifics on stage.
- On what *can't* yet be automated: *"I do think that ultimately almost everything can be made verifiable to some extent. Even for writing, you can imagine having a council of LLM judges and probably get something reasonable out."*
- The unmistakable closing aside (delivered with laughter): *"Everything is automatable."*

## Vibe coding vs agentic engineering — the title contrast

> *"Vibe coding is about raising the floor for everyone in terms of what they can do in software. The floor rises, everyone can vibe code anything, and that's amazing — incredible. But agentic engineering is about preserving the quality bar of what existed before in professional software. You're not allowed to introduce vulnerabilities due to vibe coding. You're still responsible for your software just as before. Can you go faster? Spoiler is, you can — but how do you do that properly?"*

The construct:

| Dimension | [[vibe-coding\|Vibe coding]] | [[agentic-engineering\|Agentic engineering]] |
|---|---|---|
| Effect | Raises the floor (everyone) | Raises the ceiling (professionals) |
| Trade-off | Speed and accessibility | Speed *without* sacrificing quality |
| Audience | Hobbyists, non-engineers, side-project builders | Production engineers |
| Karpathy's verdict on ceiling | "Amazing, incredible" — democratisation | *"People who are very good at this peak a lot more than 10×"* |

The "10× engineer" reference is a deliberate callback: in the pre-AI era 10× was the *upper bound* of the productivity distribution. Karpathy's claim is that **agentic engineering pushes far past 10×** — implying the productivity distribution gets fatter-tailed, with agentic engineers at the top of it pulling significantly further away.

### Hiring is still broken

> *"Most people have still not refactored their hiring process for agentic engineering capability. If you're giving out puzzles to solve, this is still the old paradigm."*

Karpathy's proposed alternative:

> *"Hiring has to look like 'give me a really big project and see someone implement that big project — let's write a Twitter clone for agents, make it really good, make it really secure, then have some agents simulate some activity, then I'm going to use 10 Codex 5.4× for X-high to try to break it. They should not be able to break it.'"*

The shape: **project-scale**, **build-and-defend**, **adversarial-test-by-agent-fleet**. This is consistent with the wiki's [[agent-harness]] *Constraints* layer — testing for whether the harness's pre-tool / post-tool middleware actually holds under adversarial pressure.

### Agents as intern entities

> *"It's remarkable. You basically still have to be in charge of the aesthetics, the judgment, the taste, and a little bit of oversight."*

Karpathy's vivid debugging anecdote (the one that grounds the *"intern entities"* framing):

> *"For Menu Gen, you sign up with a Google account but you purchase credits using a Stripe account, and both of them have email addresses. My agent actually tried to assign credits using the email address from Stripe to the Google email address — like, there wasn't a persistent user ID. It was trying to match up the email addresses, but you could use different emails for your Stripe and your Google and basically would not associate the funds. Why would you use email addresses to crossorelate the funds? They can be arbitrary."*

The architectural error (using non-persistent identifiers for cross-system reconciliation) is exactly the kind of thing a senior engineer catches in design review — and exactly the kind of thing an agent confidently produces and ships.

The implication Karpathy draws:

- **Humans own**: aesthetics, judgment, taste, oversight, the spec/plan, the architectural decisions ("these have to be unique user IDs").
- **Agents own**: the fill-in-the-blanks (API details — *"keep_dims vs keepdim, axis vs dim, reshape vs permute vs transpose"* — Karpathy: *"I don't remember this stuff anymore. You don't have to."*)

Karpathy adds an aside that's worth tracking: *"I actually don't even like the plan mode. I would, I mean, obviously it's very useful, but I think there's something more general here — work with your agent to design a spec that is very detailed, and maybe basically the docs, and then get the agents to write them and you're in charge of the oversight."* The substance: planning shouldn't be a *mode toggle* — it should be a **collaborative spec-design step** that produces persistent docs the agent then implements against.

### Will taste and judgment matter less over time?

Karpathy hopes future models close the gap: *"I'm hoping that improves. I think probably the reason it doesn't improve right now is again, it's not part of the RL — there's probably no aesthetics cost or reward, or it's not good enough."*

His critique of current model output: *"When you actually look at the code, sometimes I get a little bit of a heart attack because it's not super amazing code necessarily all the time and it's very bloaty and there's a lot of copy-paste and there's awkward abstractions that are brittle, and like it works but it's just really gross."*

Concrete example of pulling-teeth simplification: Karpathy's **micro-GPT project** (simplifying LLM training to be as simple as possible). *"The models hate this. They can't do it. I tried to keep prompting an LLM to simplify more, simplify more, and it just can't. You feel like you're outside of the RL circuits."*

The forecast: *"I do think that there's nothing fundamental preventing it. It's just the labs haven't done it yet, almost."*

## Agent-native infrastructure (the closing pet peeve)

> *"Everything is still fundamentally written for humans and has to be moved around. I still use most of the time when I use different frameworks or libraries or things like that, they still have docs that are fundamentally written for humans. Like, I don't want to do anything. What is the thing I should copy-paste to my agent?"*

The proposed direction:

- **Sensors over the world** + **actuators over the world** — decompose every workload into these two primitives.
- **Data structures legible to LLMs** — make state representations the LLM can read and write directly.
- **Agent-first docs** — replace "go to this URL → click this menu → set this value" with "copy-paste this text to your agent."

Karpathy's concrete deployment-pain example: *"Most of the work for Menu Gen was not even writing the code — it was deploying it in Vercel because I had to work with all these different services and I had to string them up and I had to go to their settings and the menus and configure my DNS and it was just so annoying."*

His test for whether infrastructure is agent-native:

> *"I would hope that for Menu Gen, I could give a prompt to an LLM 'build Menu Gen' and then I didn't have to touch anything and it's deployed on the internet."*

The end-state direction: **agent representation for people and organizations.** *"I'll have my agent talk to your agent to figure out some of the details of our meetings."*

## Outsource thinking ≠ outsource understanding (the closing claim)

The final question — *"What still remains worth learning deeply when intelligence gets cheap?"* — gets a tweet Karpathy says he keeps thinking about:

> *"You can outsource your thinking, but you can't outsource your understanding."*

His unpacking:

- *"I'm still part of the system and I still have to somehow… information still has to make it into my brain, and I feel like I'm becoming a bottleneck of just even knowing what we're trying to build, why is it worth doing, how do I direct my agents, and so on."*
- The bottleneck: **understanding is the thing that lets you be a good director.** *"You can't be a good director if the LMs certainly don't excel at understanding — you still are uniquely in charge of that."*

### The closing artifact (29:00–29:30) — Karpathy's own LLM-knowledge-base workflow

The single most-load-bearing-for-this-repo passage:

> *"I'm hoping that there's a lot of agent-first infrastructure out there… I really enjoy whenever I read an article I have my wiki that's being built up from these articles and I love asking questions about things, or um, I think that ultimately these are tools to enhance understanding in a certain way and this is still kind of like a bit of a bottleneck."*

And earlier in the same response:

> *"This is one reason I also was very excited about all the LLM knowledge bases — because I feel like that's a way for me to process information, and anytime I see a different projection onto information, I always feel like I gain insight. So it's really just a lot of prompts for me to do synthetic data generation kind of over some fixed data."*

Three observations the wiki should record:

1. **The upstream-spec author confirms the pattern.** The repo's [`llm-wiki.md`](../../llm-wiki.md) is Karpathy's articulation of exactly this workflow; CLAUDE.md operationalises it. As of 29 April 2026 Karpathy is *still using this pattern as his primary information-processing tool* — that confirms the pattern's durability beyond academic interest.
2. **"Synthetic data generation over fixed data"** is the cleanest framing yet for what wiki-style ingestion *is*. The raw articles are fixed input; the wiki pages, syntheses, threads are **synthetic projections** of the same data, generated to enable retrieval-via-different-questions.
3. **"Anytime I see a different projection onto information, I always feel like I gain insight"** is the most concentrated articulation of *why* the four-operations contract (ingest → query → lint → synthesise) is the right shape for this kind of repo. Each operation is a different projection.

## Cross-source positioning

This source sits **upstream of nearly every other source on AI engineering in the wiki**. It does not contain new empirical results; it contains the *paradigm vocabulary* the rest of the AI-engineering corpus is implicitly using. Specifically:

| Source | Construct | Karpathy's upstream framing |
|---|---|---|
| [[2026-05-04-rethinking-agents-harness-is-all-you-need]] | Same-model 6× variance; transferable harness | A *Software 3.0* program (the harness optimization process) running on an LLM-as-interpreter; jagged-intelligence explains why ablations of "verifier" modules can hurt |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness]] | "The model is rented; the harness is owned" | The harness *is* the operational vehicle for [[agentic-engineering]] — preserving the quality bar at agent speed |
| [[2026-05-07-kokane-agent-harness-vs-systems-design]] | "90% rebranded systems engineering + 10% novel" | Karpathy implicitly accepts both: agentic engineering is an *engineering discipline* (Kokane's 90%) but the 10% novel kernel maps directly onto "you have to explore this thing that has no manual" (the jagged-circuits problem) |
| [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands]] | Brain / hands / session decomposition | This is operational decomposition of a Software 3.0 program; "brain" = LLM-as-interpreter, "hands" = tool-use over the calculator-substrate, "session" = the context window as program |
| [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]] | ADLC + 7 specialised skills + scaffold templates | Productized harness toolkit *for* [[agentic-engineering]] |
| [[2026-04-28-dellacqua-jagged-technological-frontier]] | Task-level jagged frontier | Karpathy provides the *cause* (verifiability + labs care + RL training) for Dell'Acqua's *observation* |
| [[2026-05-07-anthropic-economic-index-5-learning-curves]] | Steepening learning curves; Sonnet 4.5 capacity ceiling | Operationalises Karpathy's "you have to stay in the loop" — the AEI 5 capacity-ceiling result is one of the empirical jaggedness-indicators |
| [[2026-05-07-kiron-schrage-compound-benefits]] | Verification → evaluation → learning capture | Karpathy's *"build your own RL environments"* prescription is the engineer-side instantiation of Kiron-Schrage's organisation-side flywheel |

The most surprising convergence: **[[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] *"the harness is the moat"* + Karpathy's *"agentic engineering as a discipline"*** = the same claim from two vantages. Chatterjee names the *artifact* (harness), Karpathy names the *practice* (agentic engineering).

## Linked entities and concepts

**Existing pages (touched or referenced):**

- [[agent-harness]] — agentic engineering's primary tool; this source places it inside the broader Software 3.0 paradigm.
- [[ai-agents]] — direct relevance, especially the "intern entities" framing.
- [[foundation-models]] — verifiability + jagged claims describe how foundation models behave.
- [[generative-ai]] — Software 3.0 = generative-AI under a paradigm-vocabulary rename.
- [[jagged-frontier]] — extended with Karpathy's *cause-of-jaggedness* framing (verifiability + labs care + RL).
- [[2026-04-28-dellacqua-jagged-technological-frontier]] — observation that Karpathy's framing explains.
- [[2026-05-04-rethinking-agents-harness-is-all-you-need]] — the empirical-anchor video, framed by the Software 3.0 programming paradigm.
- [[2026-05-07-chatterjee-anatomy-of-agent-harness]] — *"the harness is the moat"* + agentic-engineering = same claim from two vantages.

**New pages created with this ingest:**

- [[Andrej Karpathy]] — entity (cross-page-presence promotion: he's the upstream-spec author for this entire repo).
- [[software-3.0]] — concept.
- [[agentic-engineering]] — concept.
- [[vibe-coding]] — concept.

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):**

- *Sequoia Capital* — channel/publisher; placed in `author:` per video schema.
- *Nanobanana* — image-generation tool referenced inside Gemini.
- *OpenClaude* — agentic coding tool (the one whose install instructions are "copy-paste to your agent").
- *micro-GPT* — Karpathy's simplified-LLM-training project.
- *Menu Gen* — Karpathy's worked-example app.

## Source-quality flag

- **Strengths**: highest-prestige possible source for AI-engineering paradigm vocabulary (Karpathy = ex-OpenAI co-founder, ex-Tesla Autopilot lead, the originator of the 1.0/2.0/3.0 framing and of "vibe coding"); ten thematic sections each carrying distinct claims; rich worked examples (Menu Gen, install scripts, Stripe-Google email-matching bug, micro-GPT pull-teeth simplification); explicit acknowledgement of his own LLM-knowledge-base workflow.
- **Caveats**: live interview format means specific numeric claims are unverified asides ("Opus 4.7" and "10 Codex 5.4× for X-high" model-version names are casual); this is paradigm-naming and forecasting, not empirical research; the closing "everything is automatable" line is delivered with laughter and shouldn't be over-cited.
- **Per CLAUDE.md §Lifecycle**: confidence baseline 0.70 (single supporting source for the new concept-page claims); raised to **0.80** because (a) Karpathy is the originator of half the vocabulary in question (Software 3.0, vibe coding, jagged-intelligence framing) and (b) the framings have substantial cross-source resonance with already-ingested 2026 sources. Not raised higher because the source is opinion-format (interview) and several specific predictions are explicitly held as TBD.

## Open questions

- **Karpathy's "valuable RL environments not in the labs' mix"** — declined to name specifics on stage. If a follow-up writeup or talk surfaces the named domains, that's worth a separate ingest.
- **"Build your own RL environments" as a 2026 builder pattern** — Karpathy gestures at this as a tractable lever for verifiable-domain founders. The wiki has not yet ingested any case study of a startup actually doing this; worth tracking.
- **The plan-mode critique** — Karpathy's *"work with your agent to design a spec; then have agents write against the docs"* is a richer pattern than current plan-mode UIs. Worth tracking which IDE / harness vendors ship something matching this shape.
- **Aesthetics-as-RL-reward** — Karpathy says current code from agents is *"bloaty, copy-paste, awkward abstractions, brittle."* If labs add an aesthetic-quality reward signal, that closes the gap; worth tracking which lab does this first.
- **The neural-net-as-host, CPU-as-coprocessor flip** — Karpathy holds this as TBD. Worth a future synthesis page if multiple sources start arguing for or against it.
- **Animals vs ghosts as primary mindset** — Karpathy himself called this "philosophising"; worth tracking whether subsequent practitioner writing gives it operational force or quietly drops it.
- **"Outsource thinking ≠ outsource understanding"** — would benefit from second-source confirmation (Karpathy attributes this to a tweet whose author he doesn't name). If the original tweet/author surfaces, log as a citation upgrade.
- **Sequoia Capital as venue** — first source from Sequoia in the wiki. If a second source from Sequoia AI Ascent or similar venues lands, promote *Sequoia Capital* to an entity page.
