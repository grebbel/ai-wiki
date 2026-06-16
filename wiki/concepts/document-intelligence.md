---
type: concept
aliases: ["document intelligence", "document AI", "intelligent document processing", "IDP", "agentic document extraction", "document understanding", "machine document understanding"]
tags: [document-intelligence, document-ai, agentic-document-extraction, ocr, visual-grounding, verifiable-rag, unstructured-data, idp, enterprise-ai]
confidence: 0.72
last_confirmed: "2026-06-15"
accessed_at: "2026-06-15"
source_count: 3
relationships:
  - type: part-of
    target: enterprise-ai-adoption
    via: "document understanding is a load-bearing capability for enterprise AI on unstructured back/front-office data"
  - type: uses
    target: foundation-models
    via: "modern document AI is built on vision/multimodal transformers (e.g. LandingAI DPT, Gemini Embedding) rather than rule-based OCR"
  - type: supports
    target: responsible-ai
    via: "visual grounding / page-level citations give document AI an audit trail that suppresses hallucination — the trust primitive for regulated-industry adoption"
quality_score: 1
---

# Document intelligence

**Document intelligence** (a.k.a. *intelligent document processing*, *document AI*) is the capability of extracting accurate, structured, and **grounded** data from **unstructured documents** — PDFs, scans, forms, emails, handwriting, nested tables, figures — so that the output can be trusted by downstream automated systems. In 2026 the category is shifting from rule-based / template **OCR** toward **vision- and multimodal-transformer** approaches that understand document *structure* and tie every output back to its source location.

The concept is created on 9 June 2026 from its first dedicated vendor source ([[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes|LandingAI / TCG webinar]]) with a supporting hyperscaler source ([[2026-05-05-google-gemini-file-search-multimodal|Gemini File Search multimodal]]).

## The accuracy gap (why OCR isn't enough)

The load-bearing claim of the category: **generic OCR (or OCR + LLM) tops out around 80–90% accuracy, which is below the threshold an *agentic* pipeline can build on.** Per [[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes|LandingAI]], reliable extraction needs *"the high 99 point something percent"* — otherwise the downstream agent stack inherits hallucination, low trust, and stalled adoption. This reframes document accuracy from a back-office nicety into a **gating constraint on [[enterprise-ai-adoption|enterprise AI adoption]]**: the agentic application is only as reliable as the data it ingests.

This is the document-layer instantiation of the wiki's recurring *garbage-in-garbage-out for agents* theme — the same logic by which [[agent-harness|harness]] / context quality bounds agent reliability, applied to the document-ingestion edge of the pipeline.

## Two technical approaches in the corpus

1. **Vision-first structured extraction** ([[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes|LandingAI ADE]]). Reads the page *as an image* — blocks, structure, human reading-order — and extracts in sequence, on proprietary [[foundation-models|document transformers]] (DPT). Zero-shot, no per-document-type training.
2. **Verifiable multimodal RAG** ([[2026-05-05-google-gemini-file-search-multimodal|Gemini File Search]]). Embeds images + text together, retrieves over a document store, and returns **page-level citations** for fact-checking.

The two differ in goal — *extract a schema* vs *retrieve-and-answer* — but converge on the same trust primitive below.

## Grounding as the trust primitive

Both sources land on the same accountability mechanism: **tie every output back to its source location.** LandingAI calls it *visual grounding* (each extracted value references the originating cell / word / figure / page); Gemini calls it *page-level citations*. The pitch is identical — *"rigorous fact-checking"* (Gemini) and an *"audit trail"* that *"financial services and life sciences love"* (LandingAI). Grounding is what makes document AI defensible in regulated industries and is the concept's primary tie to [[responsible-ai|responsible AI]].

## From extraction to outcome (the orchestration layer)

High-accuracy extraction is necessary but **not sufficient** for value: documents still have to be normalised across channels, validated, and connected to systems of record. [[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes|LandingAI's partner TCG/OCTO]] frames this as the *"octo-zone"* — where systems, services, and people interact to produce an outcome — and quantifies it on an insurance case (85% faster processing, 75% efficiency gain). The applied analogue is [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Luminai]], which wedges a fax-triage agent into hospital administration: document understanding plus workflow orchestration converts manual paper/people process into automated outcomes.

## The inverse direction: re-authoring documents *for* machines ([[2026-06-12-aws-leaders-guide-data-strategy-agentic-ai|AWS data-strategy / Sydney 2026]])

Document intelligence as covered above extracts structure *out of* human-formatted documents. The AWS data-strategy keynote names the **complementary inverse**: re-author the source documents into a machine-native format so agents don't have to reverse-engineer human formatting at all. Human cues — bold, italics, indentation, PDF layout — are "overhead to a machine" (more tokens, no signal); the prescription is converting docs to **markdown** so agents reason over structure directly (headers→hierarchy, lists→arrays, links→navigable), citing **Stripe** converting its human docs this way. The keynote's four-question data test culminates in *"can an agent consume this without a human translating?"* — a crisp design target. The two directions bound the field: *extract-from-human-docs* (OCR/ADE, when you can't change the source) vs *author-for-machines* (markdown/data-products, when you control it); the latter is cheaper and lossless where feasible.

## Debates and supersession

- **Vendor-reported accuracy.** The headline 99.x% / *"above human performance"* figures are vendor claims from a marketing webinar, citing an *"independent benchmark"* that was not shown; the Gemini claims are likewise product-announcement copy. Confidence on this page is **capped at the vendor tier (0.72)** until a third-party evaluation or peer-reviewed benchmark corroborates the accuracy step-change. (Per the wiki's lifecycle rules: single-vendor + product-post sources do not lift confidence above ~0.75.)
- **"Vision-first" vs "OCR + LLM" as a real distinction.** LandingAI positions vision-first structured understanding against an OCR+LLM strawman; whether the distinction holds across document types — or collapses as frontier multimodal models improve — is open. A model-internals or independent-eval source would adjudicate.
- **Open question — extraction vs RAG convergence.** Do schema-extraction (ADE) and retrieval-answer (File Search) remain distinct products, or converge into one document-understanding API? No source yet speaks to this.

## Related concepts

- [[enterprise-ai-adoption]] — document intelligence is a `part-of` capability; the accuracy gap is an adoption blocker.
- [[foundation-models]] — the modern technical substrate (vision/multimodal transformers) the category `uses`.
- [[responsible-ai]] — grounding/citations as the audit-trail trust primitive this concept `supports`.
- [[agent-harness]] — the broader "input quality bounds agent reliability" framing that the accuracy-gap thesis instantiates at the document edge.
