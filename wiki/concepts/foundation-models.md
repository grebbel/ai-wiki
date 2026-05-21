---
type: concept
aliases: ["foundation model", "foundation models", "FM", "frontier model", "frontier models"]
tags: [foundation-models, generative-ai, ai-research]
confidence: 0.85
last_confirmed: "2026-05-21"
accessed_at: "2026-05-21"
source_count: 9
quality_score: 0.75
quality_notes: ['missing ## Debates and supersession (concept with >1 source)', '1 near-empty section(s)', '2 broken body wikilink(s)']
---

# Foundation Models

Large pretrained models — typically transformer-based — that serve as the substrate for downstream AI applications via prompting, fine-tuning, or retrieval. Foundation models drive most modern [[generative-ai]] capability and are the locus of the "frontier" debate (capability, safety, transparency). In the [[software-3.0]] framing they are *the interpreter* — the runtime that executes context-window programs.

Their capability profile is **jagged** — see [[jagged-frontier]] for the task-level observation (Dell'Acqua et al. 2026) and the cause-of-jaggedness mechanism ([[Andrej Karpathy]] in [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent 2026]]: *"LLMs automate what you can verify"* — verifiability + labs-care editorial choices about RL training data combine to produce uneven peaks and valleys).

## Working definition

A **foundation model** is a model trained on broad data at scale that can be adapted to a wide range of downstream tasks. The term, coined by Stanford's [[Center for Research on Foundation Models]] (CRFM), foregrounds the *adaptation* role — the model is a foundation other things are built on, not the end product.

**Frontier model** is a near-synonym foregrounding *capability* (top of the leaderboard). The two terms diverge in policy/regulatory contexts: "frontier" often implies the regulator-relevant subset of foundation models above a capability threshold.

## Key claims

### Industry has decisively taken the frontier

- **~90% of notable AI models in 2024 came from industry** (vs. 60% in 2023); **91.18% in 2025** per the [[2026-04-30-ai-index-report-2026|AI Index 2026]] update. Academia remains the leading source of *highly cited* research, but not of new notable models.
- **2024**: U.S. 40 notable models, China 15, Europe 3.
- **2025** ([[2026-04-30-ai-index-report-2026|AI Index 2026]]): U.S. 59, China 35, South Korea 8, Europe 2.
- **Top organizations 2025**: OpenAI 20, Google 14, Alibaba 11, Anthropic 7, xAI 5, DeepSeek 4, LG AI Research 4, Meta 4, Tsinghua University 4 (only academic institution in the top 9), ByteDance / Moonshot / Nvidia 3 each.
- The U.S.-China **performance** gap has effectively closed: DeepSeek-R1 briefly matched the top U.S. model in Feb 2025; as of March 2026, Anthropic's top model leads by just **2.7%**.

### Compute is scaling fast

- Training compute for notable models doubles every **~5 months**.
- Dataset size for training LLMs doubles every **~8 months**.
- Power required for training doubles **annually**.
- **Global AI compute capacity reached 17.1M H100-equivalents** by 2025, growing **3.3× per year since 2022** ([[2026-04-30-ai-index-report-2026|AI Index 2026]] §1.2).
- **Nvidia: >60%** of total compute; Google + Amazon supply most of the remainder; Huawei holds small but growing share.
- **U.S. hosts 5,427 AI data centers** — more than 10× any other country.
- **TSMC** fabricates almost every leading AI chip; TSMC-U.S. expansion began operating in 2025.
- **AI data center power capacity: 29.6 GW** — comparable to New York state at peak demand.
- Carbon emissions trajectory:
  - AlexNet (2012): 0.01 tons
  - GPT-3 (2020): 588 tons
  - GPT-4 (2023): 5,184 tons
  - Llama 3.1 405B (2024): 8,930 tons
  - **Grok 4 (2025): 72,816 tons** ([[2026-04-30-ai-index-report-2026|AI Index 2026]])
  - (Reference: average American = 18 tons/year.)
- **Annual GPT-4o inference water use** alone may exceed the drinking water needs of **1.2 million people**.

### Disclosure is dropping ([[2026-04-30-ai-index-report-2026|AI Index 2026]])

- Training code, dataset sizes, parameter counts increasingly **withheld** for the most resource-intensive systems including those from OpenAI, Anthropic, Google.
- Reported parameter counts have stayed near **1 trillion for three years** as disclosure dropped — but training compute (estimable independently from hardware) has continued to rise.
- **OLMo 3.1 Think 32B** with ~90× fewer parameters than Grok 4 achieves comparable benchmark results via pruning, deduplication, curation alone — evidence that data quality and post-training matter as much as scale.

### Open-weight catching up to closed-weight

- Performance gap between top closed-weight and top open-weight models on the **Chatbot Arena Leaderboard**: **8.0% in early Jan 2024 → 1.7% by Feb 2025** on some benchmarks.
- The frontier is also tightening overall: **top-2 model gap = 0.7%, top-10 gap = 5.4%** (down from 4.9% / 11.9% the year before).

### U.S.-China performance gap narrowing fast

- End-2023 vs. end-2024 gaps on major benchmarks:
  - **MMLU**: 17.5pp → 0.3pp
  - **MMMU**: 13.5pp → 8.1pp
  - **MATH**: 24.3pp → 1.6pp
  - **HumanEval**: 31.6pp → 3.7pp

### Transparency improving

- **Foundation Model Transparency Index** (CRFM): avg score among major developers **37% (Oct 2023) → 58% (May 2024)**. Substantial progress, ~42% gap remaining. See [[responsible-ai]].

### Smaller is mighty

- **142× model-size reduction for the same MMLU >60% threshold** in two years: **PaLM (540B params, 2022) → Phi-3-mini (3.8B, 2024)**.

### Models converging to commodity status: the "rent vs own" framing ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] + [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]])

By April–May 2026, practitioner writing on [[agent-harness|agent harnesses]] had converged on a sharp framing of foundation models as **commercial inputs to differentiated products** rather than as the differentiator itself:

> *"Models are converging toward commodity status. They are rented from vendors whose competitors will outperform them within the year. They are swapped between, routed across, replaced quarterly. Two years ago, choosing a foundation model felt like choosing a database. Today it feels closer to choosing a CDN. The decision still matters, but the moat it produces lasts months, not years."* — [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]

The framing has three implications worth flagging:

1. **The CDN analogy** is sharper than prior wiki framings (database, library, API). It captures the *speed* of substitution: you do not architect a multi-quarter CDN selection process; you keep your stack CDN-agnostic and switch when the price/performance gradient justifies it.
2. **Layer-4-swappable architectures are now the practitioner default.** Kokane's harness diagram explicitly labels the model layer as "swappable backends" — Azure OpenAI/GPT-5, Claude (Anthropic), Gemini/Llama/Ollama, AWS Bedrock — selected at runtime. This is consistent with the open-weight performance gap closing trend documented above (1.7% on Chatbot Arena by Feb 2025).
3. **Where competitive advantage moves**: from model selection to the **harness layer** (memory architecture, quality contracts, learned per-customer overrides, telemetry). The "rent vs own" aphorism: *"The model is what you rent. The harness is what you own."* See [[agent-harness]] for the full treatment. As of [[2026-05-04-rethinking-agents-harness-is-all-you-need|May 2026]] this framing now has its first **empirical anchor**: an optimised harness from Khattab et al. (DSPy team) **transferred across five different foundation models** without re-optimisation, lifting all of them — turning *"plan for swap"* from a prudential design hint into a measured property of the harness layer.

**Caveat against over-commoditization narrative**: [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] documented that Claude Sonnet 4.5's "context anxiety" failure mode was *absent* on Opus 4.5 — same family, different reliability. Within-family variation can be large enough that the "models converging" framing needs nuance: the *frontier* converges in benchmark performance, but *production-relevant reliability characteristics* (long-horizon stability, refusal behaviour, cost/latency curves) can vary substantially even between sibling models. The "plan for swap, not for marriage" prescription survives the caveat — but harness designers should expect to discover model-specific quirks at production scale and budget for them.

## Notable foundation model series (mentioned via [[2026-04-28-ai-index-report-2025|AI Index 2025]])

To be promoted to standalone entity pages when discussed in depth in another source. Currently noted here as a roster:

- **OpenAI**: GPT-4, GPT-4o, **o1**, o3 (test-time compute reasoning), **SORA** (video).
- **Google DeepMind**: Gemini family (Gemini-1.5-Flash-8B is the 280×-cost-reduction marker), Veo 2 (video).
- **Anthropic**: Claude 3 family (incl. Sonnet — implicit-bias study); [[Claude Sonnet 4.5]] (predominant model in AEI 4 sample, exhibits "context anxiety" per [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Managed Agents post]]); **Claude Opus 4.5** (released between AEI 4 and AEI 5 windows; the Managed Agents post notes the "context anxiety" failure mode is *absent* on Opus 4.5 — first evidence in this wiki of long-horizon reliability varying by model **within** a family, not just across families); **Claude Opus 4.6** (released coincident with AEI 5 sample window, Feb 2026).
- **Meta**: Llama 3.1 405B (the 8,930-ton-CO2 marker), Movie Gen (video).
- **Microsoft**: Phi-3-mini (the 3.8B-param-MMLU marker).
- **Mistral AI**: French open-source.
- **xAI**: Grok family.

## Debates / contradictions

- **"Frontier" vs. "foundation" framing.** "Frontier" emphasizes capability gap; "foundation" emphasizes adaptation role. Different policy/regulation implications — frontier-model bills target capability thresholds; foundation-model bills target the broader pretraining-then-adapt pattern.
- **Compute-scaling sustainability.** Data-commons shrinkage (see [[responsible-ai]]) plus rising energy demands (driving nuclear-energy partnerships — Microsoft's Three Mile Island, Google's SMRs, Amazon's SMRs) raise structural questions about the 5-month-compute-doubling trajectory continuing.
- **Open-weight closing the gap.** As open-weight performance catches closed-weight, the policy logic for restricting model release weakens — but so does the commercial moat for closed-weight providers. Open question how 2025–2026 plays out.

## Related concepts

- [[generative-ai]] — the dominant *use* of foundation models today
- [[ai-benchmarks]] — how foundation-model capabilities are evaluated
- [[responsible-ai]] — the transparency, safety, and governance overlay
- [[enterprise-ai-adoption]] — the deployment context

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "foundation-models") OR contains(tags, "frontier-models")
SORT file.name ASC
```
