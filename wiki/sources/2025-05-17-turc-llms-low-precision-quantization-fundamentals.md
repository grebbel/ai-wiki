---
type: source
kind: video
title: "How LLMs survive in low precision | Quantization Fundamentals"
author: ["Julia Turc"]
url: "https://www.youtube.com/watch?v=qoQJq5UwV1c"
date_published: 2025-05-17
length: "~20:34 (transcript 918 ASR lines; 7 chapters)"
raw: "../../raw/videos/turc-llms-low-precision-quantization-fundamentals.md"
tags: [quantization, model-compression, inference-optimization, ptq, qat, fixed-point-arithmetic, bfloat16, deepseek-r1, llama-4, h100, coral-edge-tpu, ggml, gguf, gptq, awq, unsloth, qwen, julia-turc, edge-ml, one-bit-llm, calibration, clipping-range, zero-point, ieee-754]
---

# How LLMs survive in low precision | Quantization Fundamentals

> In this video, we discuss the fundamentals of model quantization, the technique that allows us to run inference on massive LLMs like DeepSeek-R1 or Qwen.
>
> Among others, we'll discuss:
> ⚆ What quantization really means (hint: it's more than just rounding)
> ⚆ Why integers are faster than floats (with a deep dive into their internal structure)
> ⚆ How quantization preserves model accuracy
> ⚆ When to quantize: during training vs after training (PTQ vs QAT)
> ⚆ A hands-on explanation of scale, zero point, clipping ranges, and fixed-point math
>
> If you enjoyed this, consider subscribing for upcoming videos on:
> ⚆ Post-training quantization (PTQ)
> ⚆ Quantization-aware training (QAT)
> ⚆ Training in low precision (e.g., FP4)
> ⚆ 1-bit LLMs

(Channel description, Julia Turc.)

A **~20-minute solo-educator explainer** on quantization fundamentals, published **17 May 2025** (a full year before this ingest). The wiki's **first source on model efficiency / inference optimisation as a topic in its own right** — the first 26 concepts of the wiki are largely about *what* LLMs are used for; quantization is about *how* they are run at all. As Turc opens: *"Quantization is what allows us to run massive models like Deepseek R1 on just two GPUs and deploy AI models on edge devices that don't even support floating-point operations."* The video is **part 1 of a planned mini-series** — Turc explicitly defers PTQ, QAT, FP4 training, and 1-bit LLMs to future episodes.

This is also the wiki's **second-earliest source by publication date** (after Leskovec 2023). At 12 months old at the time of ingest, **its content has aged unevenly**: the technical fundamentals (fixed-point arithmetic, calibration, clipping ranges) are timeless; the empirical anchors (DeepSeek R1 = 671B/720GB; FP8 training as the frontier) are 2024–2025 cutting-edge but already being pushed by 2026 frontier work (FP4 and 1-bit LLMs are now an active research area, not a forecast). Source pages with `publish_date` earlier than ingest date carry no special schema flag in CLAUDE.md, but readers should treat dated empirical claims as snapshots.

## TL;DR

Five substantive contributions:

1. **The two-anchor motivation for quantization.** Turc opens with two empirical end-points that *together* justify the technique: at one end, **DeepSeek R1 = 671 billion parameters ≈ 720 GB at FP16**, which quantization shrinks **by over 80% to ~131 GB**, fitting across **two Nvidia H100 GPUs**; at the other end, **Google's Coral Edge TPU** (a processor for IoT/sensors/smart cameras) *"doesn't even support floating-point operations at all"* — making 8-bit integer quantization not an *optimisation* but a *prerequisite* for on-device ML. The wiki's first **dual-end-point quantization-motivation framing** (massive-models-on-cloud and tiny-models-on-edge as the same compression problem).

2. **The training-vs-inference asymmetry as the timeline anchor.** Turc names the **precision floor** explicitly: training needs fine-grained precision for gradients (historically FP32; today mostly FP16 / Bfloat16; recent frontier **FP8** on **DeepSeek R1 and Llama 4** — *"though the mechanics are not well understood publicly"*). Her forecast: *"there's a natural end to this trend and it's unlikely that gradient descent will allow us to go much lower."* Inference, by contrast, has been pushed to **8-, 4-, and even 1-bit integer precision** — the inference path is *much more resilient to precision loss* than training. **The wiki's first explicit articulation of why model-compression is overwhelmingly an inference-time problem**.

3. **PTQ vs QAT as the two ingestion points.** Turc cleanly distinguishes:
   - **Post-training quantization (PTQ)** — quantize after training, before deployment. *"This is the case for most open-weights LLM today."*
   - **Quantization-aware training (QAT)** — train with quantization-foresight; *"extreme quantization down to four bits or lower is very likely to require this in order to avoid significant degradation in model performance. This is how the famous one-bit LLMs are trained."*

4. **The fixed-point-arithmetic trick that makes integer matmul work.** The video's **technical centrepiece**: how to multiply an integer x by a real value s and get an integer y back, without re-introducing floating-point. The naive approach (store s as a fixed-point number) fails on precision — *"if s is a relatively small value like 0.003, it ends up rounded to zero."* The actual trick: **decompose s = (negative-power-of-2) × s₀** where s₀ > 0.5 by construction; store s₀ as fixed-point; the multiplication becomes **integer multiply + bit shifts**. Crucially, **the decomposition is precomputed once before deployment**. This is the **load-bearing operational insight** that connects the *clipping-range / zero-point / scale* mathematical machinery to actual integer-only hardware execution.

5. **Memory-bandwidth as the real bottleneck on modern GPUs.** Turc's most-counterintuitive operational claim: *"On modern GPUs like Nvidia, float and int multiplications can be similarly fast. And in those cases, the real bottleneck isn't really compute, it's memory bandwidth. And the real gain from quantization is the reduced bit width."* The wiki's first **memory-bandwidth-not-FLOPs framing** for understanding what quantization buys at the hardware level — refining the naive *"quantization saves compute"* mental model.

## What was actually ingested

Full ~20:34 transcript (918 ASR lines, 7 chapter sections: *Intro / What / When / How / Fixed point arithmetic / Matrix multiplications / Outro*). **ASR caption track** with characteristic auto-generation errors that future readers should ignore-and-correct:

| ASR rendering | Intended term | Notes |
|---|---|---|
| *"Bloat 16"* | **Bfloat16** | Brain Floating Point 16 — see [§Bfloat16 vs IEEE 754 FP16](#bfloat16-vs-ieee-754-fp16) |
| *"Quadization"* | quantization | one-off slip |
| *"Quen"* | **Qwen** | Alibaba's model family |
| *"GBTQ"* | **GPTQ** | quantization format suffix |
| *"Onyx"* | **ONNX** | Open Neural Network Exchange |
| *"postraining"* | post-training | typo-rendering |
| *"TW's complement"* | **Two's complement** | binary signed-int representation |
| *"ILE E"* | **IEEE** | the standards body for FP formats |
| *"Daario"* | (not present in this video; flag carried from the Ries 2026 ingest) | n/a |
| *"floatingoint"* | floating-point | recurring rendering |
| *"Deepsee R1"* | **DeepSeek R1** | recurring; also rendered correctly as *"Deepseek R1"* elsewhere |
| *"1/3 of the way"* | (rendered correctly) | n/a — flagged to confirm intended fraction is 1/3 not 1/2 |

The substantive content is fully intact; the corrections above are surface-rendering.

## Why quantization exists — the dual-end-point motivation

Chapter [0:50] (*What*) opens with the **what** but quickly pivots to the **why** via two empirical end-points. Turc's framing is that these two seemingly-opposite use cases are *the same compression problem*:

**Top end: massive LLMs on cloud accelerators.**

> *"DeepSeek R1, the largest open weights model today, has a total of 671 billion parameters. In its original floating-point precision, that's about 720 GB. Granted, it uses a mixture of experts architecture, so only a subset of its parameters are active at once, but we often still need to load the entire model in memory for inference. Quantization can shrink that footprint by over 80% down to 131 GB, which is small enough to fit across two Nvidia H100 GPUs."*

Numeric anchors:
- 671B parameters
- 720 GB at FP16 precision
- → 131 GB after quantization (**−82%**)
- Fits across 2 × Nvidia H100 GPUs (H100 = 80 GB HBM each, so 160 GB aggregate)
- DeepSeek R1 uses **Mixture-of-Experts (MoE)** — only a subset of parameters are active at once, but the *full* model must be loaded for inference (this caveat is wiki-load-bearing: MoE reduces *compute* but not *memory footprint*)

**Bottom end: edge ML on hardware that doesn't support floating-point at all.**

> *"Consider, for instance, Google's Coral Edge TPU, a processor found in IoT devices like sensors or smart cameras. It was optimized for low power consumption and doesn't even support floating-point operations at all. So the only way to locally deploy your porch-pirate-detection model would be to quantize it into 8-bit integers."*

Numeric/structural anchors:
- Coral Edge TPU = Google's edge-ML processor
- *No floating-point support* — INT8 quantization is **required**, not optimization
- Use case: *"porch-pirate-detection model"* — Turc's vivid example of a smart-camera ML deployment
- The structural point: **the unification** — *"quantization is a method for model compression and faster inference"* — applies to both massive cloud models and tiny edge models *because both are bound by integer-only or memory-bandwidth-limited hardware*.

## When — the lifecycle of a quantized model

Chapter [6:45]. Turc separates the two ingestion points:

### During training: the precision-floor trend

> *"Historically, models were trained in full precision or floating-point 32. Throughout the years, we've been striving to make do with less precision so that we can speed up the training process. Today, we mostly train in half precision or floating-point 16 enabled by Google's Bfloat 16 format. Recent LLMs like DeepSeek R1 and Llama 4 managed to train in floating-point 8. Though the mechanics are not well understood publicly, there's a natural end to this trend and it's unlikely that gradient descent will allow us to go much lower."*

The training-precision floor as of mid-2025:

| Precision | Status (per Turc, May 2025) |
|---|---|
| FP32 | Historical; full precision |
| FP16 / Bfloat16 | Current default |
| FP8 | Frontier — **DeepSeek R1**, **Llama 4** |
| FP4 | Forecast; *"natural end of trend"*; Turc names FP4 as a future-video topic, not as a stable state |
| 1-bit | **QAT-only** (see below); active research |

### Inference: the resilience asymmetry

> *"Inference, on the other hand, which only consists of a forward pass, is more resilient to the loss in precision. People have successfully run inference in integer precision as low as 8, four, or even one bit."*

The **load-bearing asymmetry** in the wiki: training needs gradient precision; inference does not. This is *why* quantization is overwhelmingly an inference-time problem.

### PTQ vs QAT

**Post-training quantization (PTQ):**
- Most common ingestion point
- *"This is the case for most open-weights LLM today"*
- **Some providers publish only floating-point** (Meta, DeepSeek) — open-source communities and infrastructure companies like **Unsloth** pick them up and quantize them
- **Other providers publish quantized versions** (Qwen) — recognisable by format suffixes: **GGUF**, **GPTQ**, **AWQ**

**Quantization-aware training (QAT):**
- Train *with quantization-foresight*
- Required for *extreme* quantization (≤4-bit) to avoid significant model-quality degradation
- **The famous 1-bit LLMs are trained this way**

## How — the technical machinery

Chapter [9:21]. Turc's *quantization scheme* / *quantization paradigm* is the formula that converts a float to an integer. Worked example: **FP16 → INT4**.

### Clipping range, calibration, scale

- **2's complement** signed integers encode an *asymmetric* interval (for INT4: **−8 to 7**); frameworks often **disregard the extra negative bucket** to get a *symmetric* range
- Neural-network values live in a narrow range **[α, β]** = the **clipping range**
- **Calibration** = determining α and β by finding the min/max values flowing through the network
  - **Trivial for weights** — they're static
  - **Non-trivial for activations** — must run inference on a *calibration dataset* — *"depending on the size of the model and your hardware can take a few minutes to a few hours"*
- **Symmetric quantization** (e.g. α = −1, β = 1) is the simplest case
- **Scale s** = the ratio of range-lengths (real-range over integer-range)
- For a value r: quantize as **round(r / s)**

### Zero point and asymmetric quantization

When the clipping range is asymmetric (e.g. caused by **ReLU** which has strictly positive outputs, skewing the distribution):

- α maps to the leftmost bucket
- β maps to the rightmost bucket
- **Zero falls somewhere strictly inside** — its host bucket is the **zero point z** (Turc's example: zero falls in bucket −2)
- z acts as an *offset* in the mapping
- The quantization formula becomes: **q = round(r / s) + z**
- **Dequantization** (q → r̂) recovers an *approximation* of r, not r itself — *"we cannot undo the entire damage of the rounding operation"*

### Fixed-point arithmetic — the integer-only multiplication trick

Chapter [14:40] is the video's most technically dense section, and the section where the conceptual framework lands on hardware reality. The problem: how do you multiply an integer x by a real-valued scale s, **and get an integer y out, without ever materialising a float**?

**The setup.** Fixed-point representation: store a fractional value as an integer plus a known scale. Turc's worked decimal example: *"to represent a value like $12.34, we could instead store it as 1,234 and keep track of the scale. That means to recover the original value, we'd have to divide by 100. So fixed point means the decimal point doesn't float. We fixed it [at] two positions from the right."*

In practice: **powers-of-2 scales** (not base-10) for hardware-efficiency. For a 4-bit unsigned int, smallest step = 2^(−4).

**The naive approach fails.** *"Your first instinct might be: just store s as a fixed-point number and perform the multiplication with fixed-point arithmetic. But that's not quite right. ... The main problem is there's too much loss in precision. If s is a relatively small value like 0.003, it ends up rounded to zero. So the final product y would also be zero."*

**The trick.** Decompose s = (negative-power-of-2) × s₀, **choosing s₀ > 0.5 by construction**. Then:

- *"We're absorbing a lot of the precision into this negative power of two so that the leftover s₀ is by choice higher than 0.5."*
- s₀ stored as fixed-point — the rounding error on a large number is negligible
- x × s = (x × s₀) × (negative-power-of-2) = **integer multiply + bit shifts**
- **The decomposition is precomputed once** before model deployment

This is the **operational bridge** between the math of quantization and the reality of integer-only or integer-fast hardware. Without this trick, every quantized multiplication would re-introduce floating-point overhead at the inner loop.

### Matrix multiplication — where the efficiency wins materialise

Chapter [18:00]. The scalar case generalises to matmul with an extra sum over each row.

> *"In matrix multiplication, efficiency gains become much clearer. Under the hood, it requires m × n × p multiplications where m, n, and p are the dimensions of the matrices. In a modern LLM like llama 4, where we find matrices of size 4,000 × 4,000, that's 10 billion operations that we implemented more effectively."*

**Subtle optimisation**: *"The scale S only needs to be applied once per output row as opposed to every entry — and that's only a few thousand times for a matrix. So when the hardware allows it, certain quantization implementations actually perform the scale multiplication in floating point."*

The wiki-load-bearing **memory-bandwidth claim**:

> *"On modern GPUs like Nvidia, float and int multiplications can be similarly fast. And in those cases, the real bottleneck isn't really compute, it's memory bandwidth. And the real gain from quantization is the reduced bit width."*

The structural point: on modern GPUs, **quantization is a memory-pressure relief, not a compute-throughput relief**. The naive mental model *"quantization saves FLOPs"* is wrong; the correct mental model is *"quantization halves (or quarters) the bytes you have to move per element, so memory-bandwidth-bound kernels run faster"*.

### Granularity

Quantization-constants (S, Z) can be applied at varying granularity:
- **Per-network** (single S, Z for all parameters — Turc's default for pedagogy)
- **Per-layer** (one set per layer)
- **Per-matrix** (one set per weight tensor)
- **Per-row** (one set per row of a weight matrix)

Granularity applies to **both weights and activations** independently. Trade-off: finer granularity = better accuracy = more metadata to store per model.

## Bfloat16 vs IEEE 754 FP16

Chapter [6:45] surfaces an under-told subplot: not all 16-bit floats are the same. Turc names **two competing 16-bit formats** and the architectural decision behind each:

| Format | Origin | Bit allocation | Trade-off |
|---|---|---|---|
| **IEEE 754 half-precision (FP16)** | IEEE general-purpose float standard | 1 sign + 5 exponent + 10 mantissa | More mantissa bits → better numeric precision in a *narrow* dynamic range |
| **Bfloat16** | **Google Brain** (the *B* is for *Brain*); ML-specific | 1 sign + 8 exponent + 7 mantissa | More exponent bits → wider **dynamic range** (ability to represent numbers across orders of magnitude); less mantissa precision |

Turc's framing of why Bfloat16 won on training: *"This was introduced by Google Brain, hence the B, specifically for machine learning. It allocates more bits to the exponent, which increases something called the dynamic range or the ability to represent numbers at different orders of magnitude. This turns out to be important for training models where we want the ability to represent very low numbers in the vicinity of zero."*

The wiki-meaningful observation: **the AI-training-precision floor moved because the format trade-offs moved**. FP16 was the IEEE-general-purpose half-precision; Bfloat16 was a *ML-bespoke* format designed by Google Brain that re-allocated bits according to what gradient-descent training actually needs. The same logic applies on the way down (FP8 has further format variants; FP4 will too). **Bfloat16 is the wiki's first explicit example of a hardware-format-as-ML-engineering-artefact** — a vendor-built data format that subsequently became an industry standard because it matched the workload better than the existing IEEE-general format did.

## Why integers are faster than floats — the hardware substrate

Chapter [0:50] (continued) is a brief but load-bearing digression on **why** integers are faster, **before** quantization is even relevant. The argument:

- **Unsigned integers** = a number in base 2 — no overhead.
- **Signed integers** = same efficiency thanks to **two's complement** (1960s; using one bit for the sign with no overhead).
- **Integer addition** = a trivial bitwise XOR with carryover. *"On modern CPUs, this instruction typically completes in a single clock cycle."*
- **Floats** = sign + exponent + mantissa, combined in a more-complex scientific-notation-like formula with hidden bit and exponent bias.
- **Float addition** = align exponents, add significands, normalise — *"on modern CPUs, this instruction can take three or even four clock cycles."*

The unstated implication: a quantized model is **not just smaller** — when its arithmetic stays in integer space, **each individual operation is 3–4× faster at the clock-cycle level**, on top of the memory-bandwidth wins.

## The ecosystem map

Turc's brief but useful **player map** as of May 2025:

| Player | Role in the quantization ecosystem |
|---|---|
| **DeepSeek**, **Meta** | Publish models in **floating-point only** — quantization is downstream |
| **Qwen** (Alibaba) | Publishes **pre-quantized** model variants alongside FP versions |
| **Unsloth** | Open-source infrastructure community / company that **post-publication-quantizes** models other providers ship in FP |
| **GGUF** | Quantization-format suffix (popularised by llama.cpp ecosystem) |
| **GPTQ** | Quantization-format suffix (gradient-based PTQ algorithm) |
| **AWQ** | Quantization-format suffix (activation-aware weight quantization) |
| **PyTorch**, **TensorFlow** | Frameworks with **built-in quantization support** |
| **ONNX Runtime**, **Nvidia TensorRT** | Inference engines that apply **hardware-specific optimisations** on top of quantized models |

Turc's closing operational note: *"In practice, you probably won't have to implement these low-level tricks yourself."* The fundamentals matter for understanding what's happening; the actual quantization is handled by tooling.

## The cultural reference

Chapter [0:00] opens with an *unforced* pop-culture reference that's worth noting because it captures the pedagogical voice:

> *"If you watch the Severance TV show, quantization is a little bit like working for the MDR department. We take real values, we put them into buckets, and never really understand what they mean."*

The reference (Apple TV+'s *Severance*, MDR = Macrodata Refinement) is the kind of unexplained intuition-pump that suggests Turc's audience is *"adjacent-technical-millennials"* rather than CS-undergrads-or-research-scientists. The wiki notes this without judgement — the framing is a hint about *who Turc is teaching to* and is useful context for placing the source in the **practitioner-explainer** tier of the wiki rather than the **research-paper** tier.

## Convergence and contradictions

| Source | Connection |
|---|---|
| [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering\|Karpathy 2026 (Sequoia AI Ascent)]] | Karpathy positions the LLM as a **programmable computer** ([[software-3.0|Software 3.0]]); Turc explains **what makes that computer actually run on commodity hardware**. The two operate at different layers of the same stack — Karpathy on the *programming-abstraction* layer, Turc on the *substrate* layer. The wiki's first **substrate-layer-of-the-Software-3.0-stack** ingest |
| [[2026-05-11-huber-chroma-rag-is-dead-agentic-search\|Huber / Chroma 2026]] | Huber claims Chroma Context One is **10× faster, 25× cheaper, on-par-or-better at search** than gigabrain models (Opus 4.5/4.6, GPT-5). Turc's mechanism makes the *25× cheaper* claim mechanistically plausible: small specialised models can be aggressively quantized (PTQ + INT8 or lower) where frontier models are constrained to FP8/FP16 at minimum. **Specialised-and-quantized vs gigabrain-and-FP** is one of the wiki's emerging axes of model-deployment economics |
| [[2026-05-07-anthropic-economic-index-5-learning-curves\|Anthropic Economic Index 5 (March 2026)]] | The 5th Economic Index report quantifies the *Opus-premium* — users select Opus differentially for higher-value tasks (+1.48 pp Opus per +$10/hr task value on Claude.ai; +2.79 pp on the 1P API). Read against Turc: this is the **economic surface** of the **technical substrate** Turc describes — the *bigger models cost more* gradient is partly *because* the bigger models can't be quantized as aggressively without degrading the value they deliver. Adjacency, not direct connection |
| [[2026-04-28-ftsg-convergence-outlook-2026\|FTSG Convergence Outlook 2026]] | FTSG names **compute**, **agentic economies**, and **edge AI** as three of its 24 convergence chapters. Turc's edge-ML motivation (Coral Edge TPU) is the **technical substrate** of FTSG's *edge-AI convergence* claim. Turc gives the bottom-up mechanism; FTSG names it as a top-down trend |
| [[Google]] entity page (existing) | Turc supplies **two substantive additions** to the Google entity: (a) **Bfloat16 / Google Brain** as the wiki's first explicit Google-Brain-format mention with the *why-it-won-training* explanation; (b) **Coral Edge TPU** as the wiki's first Google-edge-ML-hardware mention. Google's entity page is updated to surface both |
| [[2026-05-11-blank-mit-6s191-three-laws-of-ai\|Blank / MIT 6.S191 2026]] | Blank's *MIT 6.S191* course-content vantage on AI fundamentals is **pedagogically adjacent** to Turc's *solo-educator* vantage on a single technical topic. Both treat **mechanistic explanation** as the load-bearing pedagogical move (Blank on the eval-discipline three laws; Turc on the integer-arithmetic-substrate). The wiki's emerging **practitioner-explainer cluster** (Turc, Blank) is distinct from the **vendor-marketing cluster** (most of the 2026 corpus) and from the **academic-paper cluster** (Dell'Acqua, Brynjolfsson, etc.) |

### Contradictions

None substantive. Turc's content is descriptive-technical and on a topic the wiki has not previously addressed; the most-relevant **cross-source asymmetry** is that Turc's empirical anchors (FP8 as frontier; 1-bit LLMs as research) are a year old at ingest time — by 2026 these have moved (FP4 training is now an active research area; multiple 1-bit and sub-bit architectures have published). This is **temporal drift**, not contradiction. Future ingests on quantization should flag this source as the *2025-baseline* and reference newer sources for current frontier numbers.

## Linked entities and concepts

**Existing entity pages affected**:

- [[Google]] — Turc supplies the wiki's first **Bfloat16 / Google Brain** description with the *why-it-won-training* explanation, and the wiki's first **Coral Edge TPU** mention as the edge-ML hardware that motivates 8-bit quantization. `source_count` 4 → 5, `confidence` 0.82 → 0.87, `last_confirmed` 2026-05-13.

**Dangling** (single-source first-mentions, deferred per the [author-entity promotion rule](../../CLAUDE.md#author-entity-promotion)):

- **Julia Turc** (channel = author of this source) — solo educator on quantization, ML fundamentals, and adjacent topics. Patreon-supported. **Strong promotion candidate** if a second Julia Turc source is ingested.
- **DeepSeek** — Chinese AI lab; publisher of **DeepSeek R1** (671B-parameter mixture-of-experts model, the central anchor of the *cloud-end* motivation). Already a strong promotion candidate from the Ries / Anthropic-narrative ingest and now the Turc / model-efficiency ingest — **but the two prior mentions are tangential** (Ries names DeepSeek only as an FP8-training example via this ingest's cross-link), so promotion is deferred until a source narrates DeepSeek as the principal subject.
- **Meta** — publisher of **Llama 4** (named as one of the two FP8-trained models). Strong promotion candidate; Meta is also relevant to the wiki via PyTorch (Meta's open-source ML framework). Defer to second source.
- **Nvidia** — GPU manufacturer; **H100** (80 GB HBM3 datacentre GPU) and **TensorRT** (inference engine) are both named. Nvidia is a strong promotion candidate on a second source.
- **Llama 4** (model) — Meta's 2025 frontier model; FP8-trained per Turc.
- **DeepSeek R1** (model) — DeepSeek's 671B-parameter mixture-of-experts; FP8-trained; ~720 GB at FP16 → 131 GB after quantization.
- **Qwen** (Alibaba) — model family that publishes pre-quantized variants.
- **Unsloth** — open-source infrastructure community for post-publication quantization.
- **Coral Edge TPU** — Google's edge-ML processor; *does not support floating-point operations*; would be promoted as a Google sub-product.
- **Bfloat16** — Google Brain's ML-bespoke 16-bit float format (1+8+7); won the training-precision war over IEEE FP16 (1+5+10) because of dynamic-range advantages.
- **PyTorch** — Meta's ML framework; has built-in quantization support.
- **TensorFlow** — Google's ML framework; has built-in quantization support.
- **ONNX Runtime** — model-interchange inference engine.
- **Nvidia TensorRT** — Nvidia's inference engine for hardware-specific optimisations.
- **GGUF**, **GPTQ**, **AWQ** — quantization-format families. *Format candidates rather than entity candidates*; promote on a second source narrating their differences in operator detail.
- **IEEE 754** — the half-precision standard; named in the FP16-vs-Bfloat16 comparison.
- **Severance** (TV show) — pop-culture reference for *"taking real values, putting them into buckets, never really understanding what they mean"*. Cultural-context flag, not promotion candidate.
- **MDR / Macrodata Refinement** — Severance fictional department. Same.

**Concept candidates surfaced (deferred until second-source mention)**:

- *quantization* (the technique) — strong promotion candidate on second source. The wiki's first source treating it as the principal subject.
- *PTQ* (post-training quantization) — strong promotion candidate.
- *QAT* (quantization-aware training) — strong promotion candidate.
- *fixed-point arithmetic* — strong promotion candidate; the integer-only-multiplication trick is a *deeply transferable* technical primitive that recurs across embedded systems, signal processing, and ML deployment.
- *clipping range / calibration* — vocabulary candidate.
- *zero point / asymmetric quantization* — vocabulary candidate.
- *Bfloat16 / dynamic-range-vs-precision trade-off* — vocabulary candidate; strong promotion candidate if a second source explains the bit-allocation reasoning.
- *memory-bandwidth-not-FLOPs (on modern GPUs)* — strong promotion candidate. This is one of the wiki's first *hardware-substrate* claims, and it inverts the naive *quantization-saves-compute* mental model.
- *mixture-of-experts (MoE) and the inference-memory caveat* — DeepSeek-R1 example; promotion candidate if a second source narrates MoE in operator detail.
- *the training-vs-inference precision asymmetry* — concept candidate; the cleanest articulation in the wiki of why model compression is overwhelmingly an inference-time problem.

## Open questions raised by this source

- **The DeepSeek R1 FP8 training mechanics** — Turc explicitly disclaims understanding: *"Though the mechanics are not well understood publicly."* Primary-source ingest target: DeepSeek's R1 paper for the training-precision details.
- **The Llama 4 FP8 training architecture** — same status; Meta's documentation is a primary-source target.
- **The exact bit-allocation of FP8 (multiple variants exist)** — Turc names FP8 as the frontier but doesn't enumerate the variants (E4M3, E5M2, etc.). A follow-up ingest on FP8 specifically would clarify.
- **Calibration-dataset construction** — Turc names calibration as the activation-statistics step but doesn't address how the calibration dataset is selected, sized, or whether it's task-aligned. Primary-source target: PTQ papers (GPTQ, AWQ) on calibration design.
- **GGUF / GPTQ / AWQ algorithmic differences** — Turc lists them as format suffixes without comparing the underlying algorithms. Primary-source target: the original papers for each.
- **The 1-bit LLM training regime** — Turc names it as research-frontier and as a future-video topic. Primary-source target: BitNet, 1.58-bit LLMs (Ternary nets), and successor architectures.
- **Severance is not load-bearing** — flagged here only because the framing-reference is unusual for a technical explainer and may be useful context for understanding Turc's audience model.
- **Update for the year of drift** — this source is 12 months old at ingest. A follow-up Turc video (the promised PTQ / QAT / FP4 / 1-bit LLM episodes) or a 2026 quantization-frontier paper would update the empirical anchors.
