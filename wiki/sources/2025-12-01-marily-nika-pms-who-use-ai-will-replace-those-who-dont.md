---
type: source
kind: video
title: "\"PMs who use AI will replace those who don't\": Google's AI product lead on the new PM toolkit"
author: ["How I AI"]
url: "https://www.youtube.com/watch?v=fFqZm_dJXdw"
date_published: 2025-12-01
date_ingested: 2026-05-10
length: "~40:10 minutes (transcript ~7,000 words / 968 ASR segments / 181 polished lines, 10 chapters)"
raw: "../../raw/videos/marily-nika-pms-who-use-ai-will-replace-those-who-dont.md"
tags: [how-i-ai, marily-nika, claire-vo, google, ai-product-management, ai-pm, vibe-coding, perplexity, custom-gpt, v0, veo, flow, sora, notebooklm, tool-hopping, smart-fridge-demo, ai-product-academy, prd-generation, ai-as-judge, persona-debate-prompting, anti-sycophancy, december-2025-phase-change]
---

# "PMs who use AI will replace those who don't": Google's AI product lead on the new PM toolkit

> Marily Nika, AI Product Lead at Google and founder of the AI Product Academy, demonstrates how product managers can leverage AI tools to dramatically accelerate their workflow. Using a smart-fridge concept as an example, Marily walks us through the exact workflow she uses to build products faster: doing user research with Reddit debates, generating PRDs with custom GPTs, prototyping with v0, and even creating stakeholder-ready video mockups using VEO and Sora. She shows how "tool hopping" between specialized AI applications creates a powerful workflow that transforms traditional PM processes and enables more compelling product storytelling. — *channel description*

A worked-example episode of [[How-I-AI]] (host **[[Claire Vo]]**; guest **[[Marily Nika]]**, AI Product Lead at [[Google]]) demonstrating an end-to-end "AI-enhanced PM" workflow for an imagined smart-fridge product. The video runs **~40 minutes** and traces a single product idea from market-research-via-Reddit-debate through PRD generation through interactive prototype through video mockup, with NotebookLM as a bonus chapter on AI-as-judge for demo days. Auto-generated transcript, ASR-cleaned at ingest.

This is the wiki's **earliest** source by publication date — landing **2025-12-01**, ~5 months before the next-earliest source ([[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Cheung et al.]]) and **directly inside Karpathy's "December 2025 phase change"** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]). The wiki's previous treatment of that phase-change has been retrospective (Karpathy describing it ~5 months later); this source is *contemporary primary-source evidence* of the PM-side analogue: a Google AI product lead doing the workflow live, on camera, in late November 2025 / December 2025, treating the tool stack as already-trustworthy.

## TL;DR

- **Headline claim**: *"AI is not taking over a role. PMs that use AI are the ones that are going to take over the role of people that don't use AI."* The framing is competitive, not existential — the discipline isn't disappearing, but the people in it are being re-sorted.
- **The 20-minute end-to-end workflow** demonstrated live (with on-air laughter and chitchat extending it past 30 min, but the *productive* time is 15–20 min):
  1. **User research** via Perplexity's *Discussions and Opinions* filter (≈3 min) — surfaces Reddit threads + sentiment + adoption barriers from "the entirety of the world" instantly.
  2. **PRD generation** via Marily's custom GPT (≈90 s) — feature list from step 1 → fully-formatted PRD in her own voice with problem statement, target users, summary, feature analysis, architecture, prioritization.
  3. **Interactive prototype** via v0 (a few minutes) — paste the whole PRD as input → working "Open Fridge" dashboard with door-status widget, fridge temps, power usage, recent activity, safety monitoring, all in dark mode.
  4. **Promo video** via Flow (Google Labs, powered by Veo) and/or Sora — a couple-using-the-smart-fridge clip ready for stakeholder review.
  5. **AI-as-judge for the demo day** via NotebookLM — upload all student-pitch audio recordings, prompt the audio-overview hosts with judging criteria, generate a live interactive radio-style podcast that announces winners.
- **The "twin-personas debate" anti-sycophancy prompt** (worked example with Perplexity, generalizable):
  > *"Create two items, one that is pro smart fridge and one that is against smart fridge. Use everything you read and have these two agents debate at least 20 times about it and give me the minimum set of features I would need in order to convince the against agent."*

  This is the load-bearing prompting pattern of the episode: instead of asking *"do families want X?"* (which trips LLM agreeableness), ask the LLM to construct opposing personas, simulate ≥20 rounds of debate using *actual references from the source material*, and report the minimum-viable feature set to convert the skeptic. Claire Vo names this explicitly as a *critical-thinking hack* applicable beyond product ideas — code reviews, implementation choices, design decisions.
- **Tool-hopping** as the load-bearing operational pattern, not a single-tool workflow:
  > *"There is something I do call **tool hopping**. We're going to hop on to our next tool... it's just so important to explore and adapt and see which tools fit to your workflow because my choices might not be the same as other people's choices."* — Marily Nika.

  Each tool is specialized; the workflow's leverage comes from the *composition*, not from any individual tool. This generalizes [[2026-05-07-anthropic-economic-index-5-learning-curves|the Anthropic Economic Index 5th report's]] **model-selection slope** finding (picking the right model tier per task is itself a learned skill) up one level: picking the right *tool* per workflow stage is its own learned skill.
- **PRD as input, not output** (architectural insight): Claire Vo and Marily independently converge on this — *"a PRD is a higher quality input to [vibe-coding tools]"*. The PRD is no longer the artifact you write *for engineers to read* — it's the structured prompt-input you write *for the prototype tool to consume*. This re-positions PRDs as a step in a programmatic workflow, not as the terminal artifact. Claire Vo's product **ChatPRD** (mentioned in passing as having a v0 integration) is built around this insight.
- **Prototypes as stakeholder-influence tools, not just design artifacts**: *"The perfect place to use this is at the product review."* When stakeholders can touch / feel / move-around an interactive prototype, AI-skeptical leaders are easier to convince than with a deck-converted PRD. Naming this work as **influence engineering** is novel for the wiki.
- **When AI doesn't give you what you want — kill, restart, longer prompt**:
  > *"The best thing you can do is just kill that instance and start over and use Gen AI to help you write the best prompt. So I stopped trying to guess it myself and I use AI to help me with it. And the longer the prompt is, the better it's going to be and the less likely to have more iterations. So, yeah, **use AI on AI**."*

## What was actually ingested

Full ~40:10 video transcript (auto-generated captions, ASR-cleaned at ingest — proper nouns fixed, filler reduced, ~10-second-window line grouping while preserving lead timestamps; chapter section headings inserted from the YouTube microformat). All 10 chapters covered end-to-end. Two sponsor reads (WorkOS, Miro) included verbatim in the raw transcript and skipped in the wiki interpretation.

Per [§Source-page conventions specific to videos](../../CLAUDE.md#source-page-conventions-specific-to-videos), the source page's `author:` field carries **the channel name** (How I AI), not the host or guest names. Presenter names are named in body prose: **Claire Vo** (host) and **Marily Nika** (guest, the substantive speaker for ~85% of the runtime).

## Detailed walkthrough

### Smart-fridge inspiration

Marily opens with a real moment: walking out of her house on a Sunday with her kids, she notices her smart fridge displaying *"these items are expiring soon"* with her Coca-Cola flagged at 80 days old. *"First of all, I didn't know Coca-Cola expires. Second of all, I did not know my fridge could do that."* She posts a photo to LinkedIn — 700 likes, 100 comments, 13 reposts — uses the engagement to pick the use case. The *real* product she's PM-ing is unstated; the smart-fridge example is hypothetical and chosen for accessibility.

### Step 1 — User research via Perplexity

The chosen tool is Perplexity's **Discussions and Opinions** filter (alongside Web / Academic Papers / SEC Filings), which scopes the search to Reddit specifically. The first prompt is unremarkable:

```
Would families be interested in a smart fridge?
```

Result: opinions, references, threads, positive/negative use-cases, adoption barriers, sentiment.

The *load-bearing* second prompt is the anti-sycophancy twin-personas debate (full text quoted in the TL;DR above). Output: 20-round simulated debate, with Perplexity citing actual Reddit references for both sides, ending with a feature recommendation the skeptic-agent would accept. *"I can't even begin to describe how much time this has saved and how much more likely I am to find product market fit by leveraging this technology."*

Claire Vo's counter-comment is critical-thinking-focused:

> *"So often we hear about AI that it really wants to tell you your ideas are great. If you just said, 'Do families want a smart fridge?' without any additional prompting, it would probably bias towards telling you that families do want a smart fridge, maybe with some caveats. ... I love this idea — actually prompting the AI to create two different personas in its analysis. Create a persona that's very for your idea or implementation or design or code. Create an agent that's very against your idea. ... Have them do a hypothetical or artificial debate on the topic and then deconstruct that debate in a way that allows you to identify what would be the convincing arguments."*

Generalizable beyond product. The pattern is reusable for code review, implementation-choice debates, design decisions, etc.

### Step 2 — PRD generation via custom GPT

Marily has built a personal **custom GPT** ("AI Product GPT"), seeded with her preferred PRD template and her writing voice. Inputs: feature list copied verbatim from Perplexity's debate output. Outputs: a fully-formatted PRD with named sections (problem statement, user definitions, summary, feature analysis, architecture, key features, prioritization).

Claire Vo's commentary anchors the structural insight:

> *"This is a GPT specifically to create PRDs around AI-powered products. ... You can create sort of general-purpose document generators, but the more you can do a combination of structure and content in terms of your prompting, I think the higher quality results you're going to get."*

This is consistent with the wiki's existing [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] **Context layer** observation: *"the system prompt is a document, not a string."* Marily's custom GPT is a domain-specific contextualization of ChatGPT — a named, reusable, structured-prompt artifact she invokes per task.

### Step 3 — Interactive prototype via v0

Tools mentioned: **v0** (Vercel), **Lovable**, **Google AI Studio prototyping**. Marily uses v0. Prompt: `Create the UI of a smart fridge given this PRD as an input` + paste of the entire PRD.

Output (live demo): an "Open Fridge" dashboard in dark mode with:

- A **door status** widget (open/closed; "my favorite part" — both presenters volunteer that their kids leave the freezer cracked).
- Fridge temperatures with adjustment controls.
- Power usage.
- Recent activity timeline (door-open/close timestamps).
- Safety monitoring controls.
- Hardware/diagnostics page noting GPU presence (a winking nod to Silicon Valley fridge-as-edge-compute).
- Privacy/local-processing band.

Claire Vo's positioning of the artifact:

> *"It seems like for you a prototype is really a **communication tool**. So if somebody read the PRD you're like 'yeah it's a locally intelligent smart fridge, sure, whatever.' But once you can see, touch, feel it, it becomes much more compelling."*

Marily on the higher-quality-input claim:

> *"I do a lot of experimentation and I experimented because I wanted to move fast at some point and I realized that the number of tweaks I had to do later on really got me overwhelmed and tired versus me starting spending some more time in order to make sure the input is very very good. It really pays off."*

Claire Vo (in passing): *"We have an integration with v0 and all these vibe-coding tools because we really believe that a PRD is a higher-quality input to this."* — this is **ChatPRD**, Claire Vo's product, not yet a wiki entity but worth noting (single-mention; defer entity promotion).

### Step 4 — Stakeholder influence via prototypes

Marily's framing of *where* this lands organizationally:

> *"The perfect place to use this is at the product review. I find that a lot of product reviews happen more often now with AI because things move fast, because some people are really not convinced with AI yet. So if you enter a product review that's just about 'hey here's what I want to do', are you in or are you out, here's where you need to invest your resources in. And they can get a link and on their laptop actually touch it, feel it, see it, move around. You communicate your vision and your passion more effectively versus 'here's a PRD that I turned into a deck for you so that I can walk you through it.' It's just so much more. It adds credibility. It adds value. It's just so so so much more effective."*

This positions the prototype as an **influence-engineering tool** rather than a design artifact — distinct from how prototypes were used in the pre-AI era (where prototypes mostly served the design/engineering team's iteration loop, not the executive review meeting). The new prescription: *generate a clickable prototype as soon as you have a PRD, before you ever ask for engineering allocation.*

### Step 5 — Promo videos via Flow + Sora

**Flow** (Google Labs) is the surfaced product; **Veo** is the underlying model. Prompt: `create a promotional clip for a couple using a smart fridge that has these features` + paste of the PRD. Flow generates three candidate clips. The first two over-index on the door-ajar use case (consequence of the Perplexity output: door-ajar was a frequent Reddit complaint). Two clips put the screen *inside* the refrigerator. The third lands the lasagna-recipe pitch but swaps actors mid-clip (the man becomes a woman). Claire Vo's PM-eye feedback: *"I would probably pull [the door-ajar use case] from the prompt. And I would also maybe as a good product manager, one of my favorite parts to put in a PRD ... is actually what's called a **narrative**, which is a story about an end user getting value from the product."*

**Sora** (OpenAI) is the parallel demo. Marily uses a **Cameo** of herself + Mark Cuban (custom-instruction-shipped: "always make me look good"; Cuban's cameo reportedly auto-injects a Cost Plus Drugs ad). Result: Marily and Mark Cuban opening a smart fridge that suggests "Mediterranean quinoa bowl, Greek salad, pasta primavera." Marily is Greek; the AI inferred. Quality good; novelty high.

Claire Vo's epistemic hedge on Sora-the-social-network: *"I think the the social-network aspect of it is a distribution method for the underlying API models. So I think it just shows sort of power users what's possible with it and probably then people get excited about commercial applications."*

### The 20-minute end-to-end recap

Claire Vo's framing-as-rallying-cry:

> *"PMs, what I want you... we've had some giggles here, but let's just take a step back and talk about what we've done in basically 20 minutes. We have done full end-to-end user research using the wealth of information available in Reddit. We've come up with a highly defensible set of features which we turned into a PRD. We turned that PRD into a prototype that then you could take into a product review and click through. And then ... pairing that with some sort of video-generated visual or set of visuals that really just hammer home the value proposition of the thing that you're trying to build. And that package, which we just talked about, we just did, can actually be built in like 15 to 20 minutes without the chitchat. And it's just something that is was never ever ever possible before. ... The way we do product has changed. The way we convince and influence our internal stakeholders has changed. The way we communicate both product value and functionality has changed."*

Marily's competitive-coda: *"AI is not taking over a role. PMs that use AI are the ones that are going to take over the role of people that don't use AI."*

### Step 6 (bonus) — NotebookLM as AI judge

Marily runs an **AI Product Management Bootcamp** (six-week certification, students paired with an engineer to ship a product end-to-end). The bootcamp's signature event is a demo day with VC pitches and prizes. She wanted to add AI as a judge alongside human judges; she landed on **NotebookLM**.

Workflow:

1. Record audio of every student pitch.
2. Upload the audio files into a single NotebookLM notebook.
3. Use the audio-overview feature with custom instructions: *"This is the demo day of Marily's AI Product Management Bootcamp. I want you to select the top three apps based on (1) how innovative it was, (2) impact, (3) storytelling. Announce these three winners."*
4. Generate the audio overview in **interactive mode** (live radio-podcast format with two AI hosts; audience can call in).

In the demo Marily plays from a real bootcamp graduation: Claire Vo calls in mid-stream pretending to be impatient (*"We're actually in a rush. Can you please announce the three-way winners right now?"*), the AI hosts adapt mid-sentence (*"Oh absolutely. We hear you. We could definitely cut to the chase, but we do want to give just a little context for ..."*) — and ultimately announce three winners (Endopath, Study Buddy, Front Desk).

Marily's empirical observation: *"AI really chooses the best demos indeed."* Multi-judge agreement (live human judges + community vote + AI) typically converged.

Claire Vo's generalization: *"Demo days both for courses and for hack days or hack weeks could be really useful. ... Sales kickoff meetings where AEs do pitch competitions — what a fun way to add sort of like a third-party analysis."*

### Lightning round — when AI won't give you what you want

> *"The best thing you can do is just **kill that instance and start over** and use Gen AI to help you write the best prompt. So I stopped trying to guess it myself and I use AI to help me with it. And the longer the prompt is, the better it's going to be and the less likely to have more iterations. So, yeah, **use AI on AI**."* — Marily Nika.

Claire Vo summarizes: *"Kill it. Use AI. And make it detailed."*

This is the wiki's first source naming **prompt-rewriting-by-LLM as a recovery loop** ("use AI on AI"). It is operationally consistent with [[2026-05-04-rethinking-agents-harness-is-all-you-need|the Khattab et al. Meta-Harness finding]] (an LLM agent reads failure traces and rewrites the harness) — same shape, applied at the casual-prompt-iteration layer.

## Cross-source resonance

| Source | Connection |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026]] | This is the **PM-side worked example** of Karpathy's *vibe coding raises the floor* claim — a Google AI product lead, not an engineer, wielding the Software-3.0 substrate professionally. Its publication date (2025-12-01) puts it *inside* Karpathy's "December 2025 phase change" window. The video treats the workflow as already-trustworthy; Karpathy retrospectively names that window. Two complementary anchors of the same phenomenon. |
| [[vibe-coding\|vibe-coding]] | The v0 prototyping segment is the canonical PM use of vibe coding. Marily explicitly calls v0 / Lovable / Google AI Studio "vibe-coding tools" via Claire Vo in the dialogue. Concept-page entry warranted (PM expansion of audience). |
| [[2026-04-30-ai-index-report-2026\|AI Index 2026]] | Documents the broader "88% organizational adoption" of AI; this is one PM's lived workflow inside that adoption — useful as a *worked example* the AI Index numbers can attach to. |
| [[2026-05-07-anthropic-economic-index-5-learning-curves\|Anthropic Economic Index 5]] | The **model-selection slope** (high-tenure Claude users earn ~+1.5–2.8 pp per +$10/hr task value via better model selection) is the Anthropic-side empirical anchor of Marily's qualitative *"tool-hopping"* claim. Same finding at two granularities — model tier (within Anthropic's tools) and tool stack (across vendor tools). Single integrated insight: **the choice of substrate per task is itself a learned skill.** |
| [[2026-05-07-chatterjee-anatomy-of-agent-harness\|Chatterjee 2026]] | Marily's "AI Product GPT" (her custom-GPT'd PRD generator) is a domain-specific Context-layer artifact in Chatterjee's vocabulary — a named, reusable, structured-prompt construct. Her "kill that instance and start over" recovery move is the practitioner-level analogue of the Constraints-layer's pre-tool intent-validation hooks (when intent diverges, restart cleanly). |
| [[2026-05-07-kiron-schrage-compound-benefits\|Kiron-Schrage 2026]] | "Tool hopping" is the practitioner-individual-level analogue of Kiron-Schrage's organizational *return on iteration*. Marily reuses her custom GPT across product ideas; the artifact compounds. Her bootcamp's end-to-end build pattern is the educational analogue of consume-vs-compound. |
| [[2026-05-08-running-an-ai-native-engineering-org\|Fung 2026]] / [[2026-02-11-lopopolo-codex-harness-engineering\|Lopopolo / OpenAI Codex]] | Mirror-image audience: Fung and Lopopolo describe the *engineering-org* rewrite at Anthropic / OpenAI. Marily describes the *PM-individual* rewrite. Both confirm the same abstract claim: the tool-stack and process-norms have shifted enough that not adapting is a competitive liability. |
| [[micro-productivity-trap\|micro-productivity-trap]] | Marily's 20-minute demonstration is, in Bain/OpenAI vocabulary, a *micro-productivity moment* — task-level gains. The episode's weakness is that it does not address how those moments aggregate into firm-level value (the Dutt-Chatterji trap). A skeptic asking *"this PM is faster, is anyone's revenue better?"* won't find an answer here. |

## Linked entities and concepts

- **Channel (1st mention; Dangling per [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion))**: **How I AI** — podcast with website [howiaipod.com](https://www.howiaipod.com/), produced by penname.co. Defer entity-page promotion to second-source mention.
- **Host (1st mention by name; Dangling)**: **Claire Vo** — product leader; runs the **ChatPRD** product (chatprd.ai); website clairevo.com. Body-prose mention only; not promoted on a single source.
- **Guest (1st mention by name; Dangling)**: **Marily Nika** — AI Product Lead at [[Google]]; founder of **AI Product Academy**; runs the **AI Product Management Bootcamp & Certification** (six-week cohort, partnered with Maven / Lenny's List). LinkedIn / website / Substack / bootcamp link in the video description.
- **Organizations**:
  - [[Google]] — Marily's employer; Google Labs ships **Flow** (powered by Veo); **NotebookLM** is also a Google product. Add this source to Google's inbound set; minor entity-page extension warranted (Google's surface area now visibly includes Flow + NotebookLM at the consumer-PM end, not just the cloud / agent-platform / research-arm angles already in the entity page).
  - [[OpenAI]] — Sora is the cameo demo; ChatGPT is the host of Marily's custom GPT. Add this source to OpenAI's inbound set.
  - **AI Product Academy** — single-source mention; defer.
  - **Maven** — single-source mention; defer.
  - **Vercel** (publisher of v0) — implicit, not named in the transcript; defer.
- **Products**:
  - **Perplexity** — search/reasoning tool; *Discussions and Opinions* filter is the load-bearing capability used here.
  - **ChatGPT** + **custom GPTs** — Marily's "AI Product GPT" is the named instance.
  - **v0** (vibe-coding tool) — PM-prototyping demo.
  - **Lovable**, **Google AI Studio prototyping** — mentioned as alternatives.
  - **Flow** (Google Labs, powered by **Veo**) — text-to-video.
  - **Sora** (OpenAI) — text-to-video, with cameo functionality.
  - **NotebookLM** (Google) — multi-file audio in / interactive audio out.
  - **ChatPRD** (Claire Vo's product) — mentioned in passing.
  - **WorkOS**, **Miro** — sponsor reads (not load-bearing for the wiki argument; recorded for completeness).
- **Concepts touched**:
  - [[vibe-coding]] — the PM-side worked example of *vibe coding raises the floor*. Concept-page minor extension warranted (broaden the *audience* coverage from "hobbyists, non-engineers, side-project builders" to explicitly include "PMs, designers, business analysts" — a non-engineer professional class wielding the substrate as part of their job).
  - [[generative-ai]] — practitioner workflow demonstration.
  - [[agent-development-lifecycle]] — adjacent but not engaged: Marily's workflow is for *product ideas*, not for *agents*. Notable that the PM-workflow lifecycle (research → PRD → prototype → video → review) is structurally similar to the ADLC (capability exploration → design → context engineering → eval → UAT) but for a different artifact.
  - **Tool hopping** as a candidate concept — single-source for now; promote on second-source mention. Worth tracking; the empirical convergence with [[2026-05-07-anthropic-economic-index-5-learning-curves|Anthropic Economic Index 5's]] *model-selection slope* is suggestive.
  - **AI-as-judge** as a candidate concept — single-source for now; the NotebookLM demo-day pattern is generalizable (sales kickoff pitch competitions, hackathon judging, course demo days).
  - **Influence engineering / prototype-as-stakeholder-tool** as a candidate concept — single-source for now.
  - **Anti-sycophancy prompting / twin-personas debate** as a candidate concept — single-source for now.

## Notes on confidence and lifecycle

- **Source quality**: practitioner conversational demo on a podcast/YouTube channel ("How I AI"). Vendor-affiliated speaker (Marily works at Google; Marily plugs her own bootcamp; Claire plugs ChatPRD; sponsor reads from WorkOS and Miro). Authoritative on what the demonstrated workflow looks like *for one practitioner on one day*; not externally replicated, no benchmark, no quantitative anchor.
- **Page does not carry `confidence:`** — sources are evidence, not claims (per [§Lifecycle](../../CLAUDE.md#lifecycle)).
- **Video transcript provenance**: auto-generated (ASR), cleaned at ingest. Per the [skill convention](../../.claude/skills/youtube-transcript-skill/SKILL.md), this is a `kind: asr` track — treat specific quoted phrases as *paraphrasable* rather than verbatim, especially for proper nouns (which were corrected) and for the cameo-segment dialogue (which was clearly difficult for the ASR system due to overlapping voices).
- **Date positioning**: published 2025-12-01; ingested 2026-05-10 (5+ months of latency). The wiki's prior earliest-by-publication source was [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|the Google Agents CLI announcement]] from 22 April 2026; this source pushes the wiki's earliest-source date back five months. **Karpathy's "December 2025 phase change" anchor** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]) is now empirically substantiated by a contemporary demonstration of the trustworthy-tool-stack practitioner workflow.

## What this source does *not* do

- It does **not** quantify outcomes. No A/B comparison, no time-saved measurement, no quality comparison between AI-PM-generated PRDs and traditional ones. Marily's claims about speedup ("3 minutes," "90 seconds," "20 minutes end-to-end") are demo-time observations, not measured productivity numbers.
- It does **not** address failure modes. The Veo/Sora generations went wrong in funny ways (screens inside the fridge, swapped actors mid-clip), but the discussion is laughter, not analysis. *What does the workflow look like when the smart-fridge prototype actually has to ship to engineering?* — outside scope.
- It does **not** address authoring economics. ChatGPT, custom GPTs, Perplexity Pro, v0, Flow, NotebookLM, Sora — the cumulative subscription/usage cost of the demonstrated workflow is unstated.
- It does **not** engage with the harness / agentic-engineering / agent-development-lifecycle vocabulary the wiki has built up around the engineering side. The PM-side and engineering-side practitioner literatures are presently siloed in the wiki's intake; bridging them is open work.
- It does **not** address how the workflow scales beyond a single PM. A team of 20 PMs each with their own custom GPT would face composition / consistency / shared-context problems analogous to [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's "AGENTS.md as table of contents"]] need. *No team-shared-PM-toolstack discussion in this source.*
- It does **not** address what happens when the unstated *real* product Marily PMs at Google fails in ways the smart-fridge demo doesn't expose. Demo product is hypothetical; the framing is implicitly *"this works for me at Google"* without specifying which Google products bear out the claim.

These are reasonable elisions for a 40-minute conversational demo; flag as gaps that a follow-up source (case study, controlled comparison, team-scale workflow study) would need to fill.
