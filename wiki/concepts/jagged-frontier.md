---
type: concept
aliases: ["jagged frontier", "jagged-frontier", "jagged technological frontier", "AI capability frontier", "jagged intelligence", "jagged skills", "jagged-intelligence", "animals vs ghosts", "ghosts not animals"]
tags: [jagged-frontier, jagged-intelligence, AI-capabilities, knowledge-work, productivity, automation, augmentation, verifiability, animals-vs-ghosts]
confidence: 0.93
last_confirmed: "2026-06-13"
accessed_at: "2026-06-13"
source_count: 13
relationships:
  - type: supports
    target: automation-vs-augmentation
    via: "per-task fit determines whether AI augments or harms — empirical mechanism"
  - type: instance-of
    target: generative-ai
    via: "characterizes the capability profile of GPT-class models specifically"
quality_score: 0.79
quality_notes: ['missing ## Debates and supersession (concept with >1 source)', '1 near-empty section(s)']
---

# Jagged Frontier

The boundary of what current AI systems can do well — described as **"jagged"** because tasks of similar perceived difficulty for humans can fall on opposite sides. Inside the frontier, AI assistance helps; outside, it harms. The frontier is **invisible** (workers can't easily tell which side a task sits on without inspection) and **moving** (it expands with model improvements).

## Working definition

Per [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. (2026)]], who introduced the term:

> "Tasks that appear to human knowledge workers to be of similar difficulty may be performed either better or worse by humans using AI. Within this jagged frontier, AI can complement human work. However, outside the frontier, AI output is inaccurate, is less useful, and can degrade human performance."

The "jagged" descriptor distinguishes it from a smooth, monotonic capability gradient: AI is unexpectedly good at some tasks (idea generation) and unexpectedly bad at others that look easy (e.g., basic math, multi-source triangulation requiring close reading).

## Key claims

### Empirical anchor: BCG field experiment ([[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026]])

- 758 [[Boston Consulting Group|BCG]] consultants, randomized into control / GPT-4 only / GPT-4 + overview, across two task arms (one inside-frontier, one outside-frontier).
- **Inside the frontier**: AI users +12.2% completion, +25.1% faster, +33.9% quality (Cohen *d* ≈ 0.96).
- **Outside the frontier**: AI users 19 percentage points *less* likely to be correct (84.5% control → 60.0% / 70.6% AI conditions).
- Same model (GPT-4), same elite users, same task domain — the jaggedness is a property of the *task-AI fit*, not user skill or model selection.

### Subjective coherence persists when correctness fails

- Outside-the-frontier AI users produced *more confident, more coherent* recommendations even when their answers were wrong (subjective coherence quality higher with AI in both correct- and incorrect-answer subgroups).
- Implication: AI improves *presentation* irrespective of *substance*, which can mask poor performance from supervisors and clients.

### Two adaptation patterns

The Dell'Acqua paper's qualitative analysis identifies two effective-user strategies:

- **Centaurs** — alternate between AI and human work, switching task-by-task.
- **Cyborgs** — deeply intertwine AI into the workflow with continuous human-AI co-production.

### Convergence with adjacent measurement frameworks

The jagged-frontier concept is consistent with and extended by:

- [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] — task-level success rate falls slightly with task complexity (70% → 66% from sub-HS to college-level), while speedup rises sharply; the speedup-times-success product is positive but uneven across tasks.
- [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (2025)]] — within customer support, the AI declines to suggest when training data is insufficient, an explicit acknowledgement that the system has bounded reliability.
- [[ai-benchmarks]] — METR's task-horizon work measures the duration of tasks an AI can complete with 50% success, providing a related but methodologically distinct picture of capability scope.
- [[2026-04-29-boussioux-crowdless-future|Boussioux et al. (2024)]] — in creative ideation, HAI solutions occupy a more *incremental* search space proximal to existing ideas, while human-crowd solutions exhibit more variable search at both the bottom and top extremes of novelty. The paper attributes the pattern to LLMs' training-data confinement, formal-rationality bias, and convergence toward the statistical mean. This is one face of jaggedness: AI is strong on value/quality and weak on extreme-novelty.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — the term "jagged frontier" is now part of the AI Index narrative (Top Takeaway #4). The report's anchoring example: **Gemini Deep Think wins gold at the IMO** while the top model reads analog clocks correctly only **50.1%** of the time. AI agents on **OSWorld** leapt from 12% → ~66% task success in one year, yet still fail roughly **1 in 3** structured-benchmark attempts. Robotic manipulation in software simulations (RLBench) reaches 89.4%, but real-world household-task success is only 12%.
- [[2025-10-05-patwardhan-et-al-openai-gdpval|GDPval (OpenAI 2025)]] — jaggedness **by occupation and modality**, measured on real deliverables: across 44 occupations, different models win on different file types (Claude Opus 4.1 stronger on `.pdf`/`.xlsx`/`.ppt` aesthetics; GPT-5 stronger on pure text and instruction-following), and the most common loss reason is *failing to fully follow instructions* — a frontier that is uneven not just across tasks but across **deliverable formats and competence dimensions**. GDPval also shows the frontier is *steerable*: more reasoning effort, context, and scaffolding move it (a self-check prompt cut PowerPoint formatting errors 86%→64%).
- [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti (HBR 2026)]] — the practitioner restatement of the jaggedness *trajectory*: AI has gone "from pretty good at simple tasks and terrible at complex tasks to **excellent at simple tasks and pretty good at complex tasks**." The frontier is jagged *and moving outward*, which is why Argenti argues against anchoring one's value to any fixed "10% AI can't do."

### Mechanism: the frontier is invisible

Workers cannot reliably tell ex ante which side of the frontier a given task sits on. Effective use therefore requires:

- Workflow-level inspection to identify deviations from human-only baselines.
- Meta-cognitive skill to assess AI fit task-by-task.
- Calibration against demonstrated performance, not perceived task similarity.

### Cause-of-jaggedness: verifiability + labs care ([[Andrej Karpathy]], [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent 2026]])

Where Dell'Acqua *describes* the jagged frontier (the *task-level observation*), [[Andrej Karpathy]]'s [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent interview]] (29 April 2026) supplies the **causal mechanism** at the training-process level — and renames the phenomenon **"jagged intelligence" / "jagged skills"** at the model side (vs. "jagged frontier" at the task side).

Karpathy's framing:

> *"Traditional computers can easily automate what you can specify in code, and this latest round of LLMs can easily automate what you can verify."*

The mechanism, as he describes it:

1. Frontier labs train these LLMs in **giant reinforcement-learning environments**. Models receive verification rewards.
2. Models **peak on verifiable domains** (math, code, adjacent areas) and stay rough elsewhere.
3. **Two factors** combine to make a domain "fly" or "struggle":
   - **Verifiable**: the domain has a check function (correctness can be scored automatically).
   - **Labs care**: the domain made it into the data distribution / RL environment mix because it was *commercially or strategically valuable to the labs.*
4. Without one of these, you're "out of the RL circuits" — your application has to pull a fine-tuning lever itself.

The **chess anecdote** Karpathy uses to make "labs care" concrete:

> *"From GPT-3.5 to GPT-4 people noticed that chess improved a lot, and a lot of people thought 'oh well, it's just a progression of capabilities.' But actually, a huge amount of chess data made it into the pre-training set. Someone at OpenAI decided to add this data, and now you have a capability that just peaked a lot more. So we are slightly at the mercy of whatever the labs are doing, whatever they happen to put into the mix."*

The implication: capability gains are **not uniform across domains** — they are *editorial* (decisions made by labs about what to include in training data and RL environments). A domain in 2024 that received no special attention might be added to the mix in 2025 and produce a step-change improvement; a different domain might never receive that attention and remain rough indefinitely.

#### The canonical 2026 jaggedness story (replacing "letters in strawberry")

Karpathy explicitly retires the older example (the model getting *"how many letters in strawberry"* wrong) — *"the models now patch this, I think"* — and replaces it with a 2026 version:

> *"Opus 4.7 will simultaneously refactor a 100,000-line codebase or find zero-day vulnerabilities, and yet tells me to walk to a 50-meter-away car wash because it's so close. This is insane. And to whatever extent these models remain jagged, it's an indication that number one maybe something's slightly off, or number two you need to actually be in the loop a little bit and you need to treat them as tools."*

The car-wash example is now the wiki's canonical jaggedness illustration. It captures the *qualitative* shape of the phenomenon better than benchmark statistics: simultaneous mastery of high-value verifiable domains and embarrassing failure on low-value reasoning the model wasn't optimised for.

#### Operational implications for builders

> *"You have to actually explore this thing that they give you that has no manual… you have to figure out which circuits you're in in your application. And if you're not in the circuits, then you have to really look at fine-tuning and doing some of your own work."*

- **Identify which RL circuits your application sits in.** Verifiable + labs care → flies; otherwise → struggles.
- **Build your own RL environments where labs aren't.** [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]'s founder advice: *"If you are in a verifiable setting where you could create these RL environments or examples then that actually sets you up to potentially do your own fine-tuning and you might benefit from that. That is fundamentally technology that just works."*
- **Stay in the loop**, treat models as tools, do not over-trust capability transfer across "similar-looking" tasks. This restates the Dell'Acqua observation in cause-and-effect form.

### Animals vs ghosts ([[Andrej Karpathy]])

Within the jagged-intelligence framing, [[Andrej Karpathy]] adds a **mindset framing** for *what kind of intelligence* the wiki should treat LLMs as:

> *"We're not building animals; we are summoning ghosts. Jagged forms of intelligence shaped by data and reward functions, but not by intrinsic motivation or fun or curiosity or empowerment — things that came about via evolution."*

He explicitly discounts the framing's operational power as *"a little bit of philosophising"* — but it does change three things about how to work with these systems:

- **No anthropomorphic levers.** *"If you yell at them, they're not going to work better or worse — it doesn't have any impact."* Strategies that work on humans (motivation, encouragement, deadlines) don't transfer.
- **No assumption of intrinsic drive.** The LLM doesn't get bored, curious, or empowered. There is no inner motivation pushing it toward a goal you didn't explicitly specify.
- **Substrate awareness.** *"Statistical simulation circuits where the substrate is pre-training, like statistics, and then there's RL bolted on top."* The model is the sum of these — not an animal mind.

The animals-vs-ghosts framing is held in the wiki as a **mindset convention**, not a recipe. It belongs alongside the verifiability mechanism above because both are about *what kind of intelligence the jaggedness reveals* — patchy, discontinuous, statistically-shaped, no underlying continuous-self that smooths over discontinuities.

## Practical implications

- **Don't generalize AI capability across tasks** that "feel similar."
- **Centaur/Cyborg strategies are post-hoc descriptions of effective use**, not prescriptions; both can fail when applied indiscriminately.
- **Familiarity training can backfire**: in the Dell'Acqua experiment, the GPT + overview condition performed *worse than GPT-only* on outside-the-frontier correctness — more familiarity led to more over-reliance.
- **The practitioner-operational form: probability × impact × detectability**. [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]] (Thoughtworks at QCon London) offers a risk-assessment trio for *how much human supervision a given task warrants*: probability of AI error in *this* context (assessed by knowledge of the context given to the agent + experience using the tool for similar tasks + requirement clarity), impact if it errs (proof-of-concept vs critical-path), and detectability of the error (quality of feedback loops). Of the three, only the first is genuinely new — the other two are pre-existing engineering judgement applied to a new tool. Böckeler's framing: *"you have to be this tall to ride the roller coaster — you have to be this tall to reduce supervision"*. The trio is the practitioner's operational expression of the jagged-frontier insight: don't assume capability, *assess* it per-task.
- **The "skill we thought was ours" inversion** ([[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs|Thompson 2026 (NYT The Daily)]]): the wiki's cleanest **expository** statement of jaggedness for a general audience. Thompson invokes the chess/speech historical inversion — *"Back in the '80s, it seemed like chess was so hard to play there was no way a computer was going to do it. But it seemed like speaking — that's easy. Surely a computer should be able to just speak. But it turned out that chess was actually easier for computers to do than to learn to speak."* — and generalises: *"things that we thought maybe were 'oh, this is my big skill' — yeah, that's not really your skill. Your skill lies elsewhere."* Operationally for working developers: the technical writing-the-code work they thought defined the craft is the more-automatable part; the communication, priority-setting and deciding-what-to-build work they took for granted is the less-automatable part. Direct convergence with the [[durable-skills]] frame and complementary to Dell'Acqua et al.'s controlled-experiment empirical anchor.
- **Methodological critique of percentage-of-job decomposition** ([[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans / Lenny's Podcast May 2026]]). Evans accepts the jagged-frontier concept (he names it explicitly) but rejects the methodology that decomposes a profession into percentage-automatable tasks: *"You can't look at a senior partner at a law firm and say, well 17% of their work could be automated. This is horseshit ... ironically this is the logical systems problem. The expert systems problem ... you start building up logical steps. So you make an edge detector and then you make a third detector and you make an eye detector and you make an ear detector and 15 years later you've got 700 steps and it doesn't work."* Evans's view is that the **frontier** is real and observable, but the analytical move from *frontier observation* to *X% of job Y is automatable* is the same fallacy expert-systems computer vision tried and abandoned. This is a methodological contradiction to the task-level decomposition that underlies Dell'Acqua, Brynjolfsson and O*NET-style analyses — not a contradiction to the empirical phenomenon. Pair with the [[automation-vs-augmentation]] **task-vs-job** distinction that Evans poses as the alternative analytical lever.

## Related concepts

- [[automation-vs-augmentation]] — fit determines whether AI substitutes or complements; the frontier is the empirical boundary.
- [[ai-employment-effects]] — the jaggedness explains why some occupations see employment declines while others see growth.
- [[generative-ai]] — the underlying technology whose capability frontier is jagged.
- [[ai-benchmarks]] — fixed-task benchmarks measure one slice of the frontier.
- [[software-3.0]] — Software 3.0 programs run on jagged interpreters; verifiability + labs care determine which programs run reliably.
- [[agentic-engineering]] — practitioners must know which RL circuits their work sits in; the discipline includes identifying when fine-tuning is needed.
- [[foundation-models]] — the substrate whose training-process editorial choices produce the jaggedness.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "jagged-frontier")
SORT file.name ASC
```

## Open questions

- The frontier shifts with model improvements; longitudinal measurement is sparse. The [[Anthropic Economic Index]] is the closest current source for tracking shifts at population scale.
- The Centaur vs. Cyborg dichotomy comes from one paper's qualitative coding; replications across other domains and tools would strengthen it.
- **Karpathy's hinted "valuable RL environments not in the labs' mix"** — declined to name specifics on stage in [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent]]. If a follow-up writeup names the domains, that's a high-value second source for the cause-of-jaggedness section.
- **Aesthetics-as-RL-reward** — Karpathy specifically calls out that current code from agents is *"bloaty, copy-paste, awkward abstractions, brittle."* If labs add an aesthetic-quality reward signal, that closes one specific jaggedness gap; worth tracking which lab does this first.
- **Animals-vs-ghosts as primary mindset** — Karpathy himself called it "philosophising"; worth tracking whether subsequent practitioner writing gives it operational force or quietly drops it.
