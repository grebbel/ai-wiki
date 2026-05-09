---
type: concept
aliases: ["software 3.0", "Software 3.0", "software-3.0", "LLM as computer", "LLMs as a new computer", "context window as program", "prompting as programming"]
tags: [software-3.0, software-2.0, software-1.0, llm-paradigm, prompting, context-window, ai-engineering, karpathy]
confidence: 0.80
last_confirmed: "2026-05-09"
source_count: 2
relationships:
  - type: instance-of
    target: generative-ai
    via: "Software 3.0 is a paradigm-vocabulary description of what generative-AI engineering is, structurally"
  - type: depends-on
    target: foundation-models
    via: "Software 3.0 programs need a foundation model as their interpreter"
  - type: depends-on
    target: agent-harness
    via: "a Software 3.0 program needs a runtime; that runtime is the agent harness"
---

# Software 3.0

The **third paradigm of software**, per [[Andrej Karpathy]]'s 1.0 / 2.0 / 3.0 trilogy framing. **Software 1.0** is explicit rules written as source code. **Software 2.0** is learned weights — programming by curating datasets and designing neural-network architectures (Karpathy's coinage in the original *Software 2.0* Medium post, 2017). **Software 3.0** is **prompting**: the LLM is a *programmable computer*, the **context window is the program**, and the LLM is the *interpreter*.

The framing's load-bearing claim is not "Software 3.0 will speed up existing development" — it is **"Software 3.0 makes new things possible that couldn't exist before."** [[Andrej Karpathy]] frames the *speed-up* mindset as the failure mode to avoid: it keeps you working in the old paradigm, building scaffolding apps that the underlying model could now do natively. The clearest worked example in the wiki is the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Menu Gen episode]] — see below.

## Working definition

A **Software 3.0 program** is a piece of text (the prompt + assembled context) that, when interpreted by a sufficiently capable foundation model, performs useful computation in the digital information space. The unit-of-work is the **piece of text you copy-paste to your agent**, not a function definition or a data pipeline.

| Paradigm | Programming substrate | Programmer's job | Era |
|---|---|---|---|
| **Software 1.0** | Source code (explicit rules) | Write the code | 1950s – present |
| **Software 2.0** | Datasets + neural-net architectures (learned weights) | Curate the dataset; design the architecture; train the network | 2010s – present |
| **Software 3.0** | **Prompts / the context window** | Write the prompt; assemble the context; the LLM is the interpreter | 2022 – present, accelerating in 2025–26 |

[[Andrej Karpathy]]'s framing in the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]] (29 April 2026):

> *"Software 3.0 is about your programming now turns to prompting, and what's in the context window is your lever over the interpreter that is the LLM that is interpreting your context and performing computation in the digital information space."*

## Two operational consequences

### 1. The unit of work is "what to copy-paste to your agent"

The clearest single example in the wiki: **OpenClaude's install instructions are not a `bash` script**. They are a prose block you copy-paste into your agent. The agent inspects your environment (OS, Python version, paths, existing tools), performs intelligent actions, and **debugs in the loop** — sees an error, tries a fix, retries.

Karpathy's framing of the shift:

> *"You're working now in the Software 3.0 paradigm where you don't have to precisely spell out all the individual details of that setup. The agent has its own intelligence that it packages up and follows the instructions… so much more powerful. So I think that's a very different kind of way of thinking about it: what is the piece of text to copy-paste to your agent? That's the programming paradigm."*

The deliverable shifts from *"a script that handles every platform variation"* to *"a prose description of what the install needs to accomplish"* — and the LLM's general intelligence covers the platform variation.

### 2. New things become possible — not just faster

This is the load-bearing reframe Karpathy keeps returning to. The Menu Gen worked example:

- Karpathy v-coded **Menu Gen** as a Software 1.0/2.0 hybrid: photo of restaurant menu → OCR → image-gen for each item → overlay onto the menu. Vercel deployment. Functioning, useful app.
- Then he saw the **Software 3.0 version**: just give Gemini the photo + prompt *"use Nanobanana to overlay items onto the menu"*. Nanobanana returns an image that is *exactly the original photo* — same composition, same lighting — but with the menu items rendered into the pixels of the menu surface.

> *"All of my menu gen is spurious. It's working in the old paradigm. That app shouldn't exist."*

The general claim:

> *"The Software 3.0 paradigm is a lot more raw. Your neural network is doing more and more of the work and your prompt or context is just the image and the output is an image, and there's no need to have any of the app in between. So I think that people have to reframe — not to work in the existing paradigm of what things existed and just think about it as a speed-up of what exists. It's actually like new things are available now."*

Karpathy explicitly applies the reframe **beyond code**:

> *"It's not just even about code. Previous code worked over structured data. But for example with my LLM knowledge bases project — basically you get LLMs to create wikis for your organisation or for you in person etc. — this is not even a program. This is not something that could exist before, because there was no code that would create a knowledge base based on a bunch of facts. But now you can just take these documents and recompile them in a different way and reorder them and create something new and interesting as a reframing of the data. So these are new things that weren't possible."*

This is the same claim the wiki's existence is predicated on — see [[Andrej Karpathy]] for the upstream-spec connection.

## Architectural relationship to [[agent-harness]]

Software 3.0 is **upstream** of the harness construct:

- A Software 3.0 *program* is the prompt + context (the **what to compute**).
- A foundation model is the *interpreter* (the **how to compute it**).
- The **runtime** that assembles context, manages tool execution, validates intent, applies post-tool hooks, and feeds telemetry back is the [[agent-harness]] (the **operational vehicle**).

Karpathy doesn't use the harness vocabulary in the [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia interview]], but the architectural relationship is direct. Phrased through the [[2026-05-04-rethinking-agents-harness-is-all-you-need|harness-as-OS analogy]]:

| OS analogy layer | Software 3.0 mapping |
|---|---|
| **CPU** — powerful but inert | The LLM (the interpreter) |
| **RAM** — fast but limited | The context window (the program loaded for execution) |
| **Disk** | External databases / state stores |
| **Device drivers** | Tool integrations |
| **Operating system** | The agent harness |
| **The application** | A Software 3.0 program |

Both framings agree on the same architecture from two vantages: Karpathy describes the *programming paradigm* (what's the program?); [[2026-05-04-rethinking-agents-harness-is-all-you-need|the harness video]] describes the *runtime engineering* (what executes the program reliably in production?).

## Implications

### For builders

- **Inspect every glue-code app for whether it's spurious in Software 3.0.** Karpathy's Menu Gen experience is a template: a working v1.0/2.0 app may be doing scaffolding work the model could now do natively.
- **The unit of work shifts**. Time spent perfecting Python orchestrators may be better spent perfecting the prompt + context that asks the model to do the orchestration itself.
- **Agent-native infrastructure becomes a precondition.** If your tooling, docs, and infrastructure are still written for humans, you're paying a translation tax on every Software 3.0 program. Karpathy's pet peeve: *"Why are people still telling me what to do? I don't want to do anything. What is the thing I should copy-paste to my agent?"*

### For founders

- Distinguish **speed-up opportunities** (faster versions of existing apps) from **new-things opportunities** (apps that couldn't exist before). Karpathy: *"I almost think that [the new-things side] is more exciting."*
- **LLM knowledge bases / wikis built from documents** are a named example Karpathy gives of a Software 3.0 product class that has no Software 1.0/2.0 antecedent. This is also the artifact this entire repo implements.

## Predictions: where Software 3.0 leads

Karpathy's [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|extrapolation]] for what's "obvious by 2026" is more radical than typical:

> *"You could imagine completely neural computers in a certain sense. You feed raw videos — imagine a device that takes raw video or audio into basically what's a neural net — and uses diffusion to render a UI that is unique for that moment."*

His historical reference: in the 50s and 60s, people were unsure whether computers would look like *calculators* or *neural nets*. The calculator path won; neural nets now run *virtualised* on top of classical computers. Karpathy's hypothesis: **this might flip**. The neural net becomes the **host process**; the CPU becomes the **co-processor** — used for tool-use over deterministic tasks as a "historical appendage."

He explicitly holds this as *TBD*: *"That progression is TBD, I would say."* The wiki tracks it as an open question, not a settled forecast.

## Debates and supersession

- **Is Software 3.0 a paradigm or a vocabulary rebrand?** [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]]'s sceptical view ("90% rebranded systems engineering") would extend naturally to Software 3.0 — the *primitives* of context-window-as-program have antecedents in DSLs, scripting, expert systems. The defensible position: Software 3.0 is at minimum a useful **vocabulary** for what's qualitatively new (non-determinism at the core; context-as-program), even if individual primitives have older antecedents. The wiki holds it as a paradigm-naming framework, not a claim of total novelty.
- **Does the "new things possible" claim survive cost scrutiny?** Karpathy's Menu Gen example assumes Nanobanana-class image-gen is cheap enough to invoke per-menu. As of 29 April 2026 this is true for hobby use; production cost-curves are still volatile. Worth tracking as a debate.
- **Is the "neural net as host process" extrapolation plausible?** Karpathy holds it as TBD. No second source in the wiki engages it directly yet. Open.

## Related concepts

- [[agent-harness]] — the runtime layer that executes Software 3.0 programs reliably in production. Software 3.0 *is the program*; the harness *is the OS*.
- [[ai-agents]] — agents are the *deployment shape* of Software 3.0 programs that pursue goals across multiple steps.
- [[foundation-models]] — the *interpreter* that executes Software 3.0 programs.
- [[generative-ai]] — Software 3.0 is structurally a paradigm-vocabulary description of what generative-AI engineering *is*.
- [[agentic-engineering]] — the engineering discipline of writing Software 3.0 programs that meet the quality bar of professional software.
- [[vibe-coding]] — the floor-raising side of Software 3.0 (everyone can vibe code anything).
- [[jagged-frontier]] — Software 3.0 programs run on jagged interpreters; verifiability + labs care determine which programs run reliably.

## Open questions

- **Is there an empirical signal that the "new things possible" framing is producing distinctive product categories?** Wiki has not yet ingested a 2026 catalogue of *Software-3.0-only* products. Karpathy's *LLM knowledge base* class is one named example; *Menu Gen-as-Nanobanana-overlay* is another. Worth tracking.
- **Where does the Software 3.0 / Software 2.0 boundary actually fall?** Fine-tuning is squarely Software 2.0; pure prompting is squarely Software 3.0. Hybrid systems (RAG, prompt-augmented tool-use, RL-fine-tuned-then-prompted) blur the boundary. A second source that maps the boundary explicitly would lift confidence here.
- **Aesthetics-as-RL-reward** — Karpathy specifically calls out that current code from agents is *"bloaty, copy-paste, awkward abstractions, brittle."* If labs add an aesthetic-quality reward signal, Software 3.0 program *quality* (not just correctness) closes the gap. Worth tracking which lab does this first.
