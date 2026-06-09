---
type: source
kind: video
title: "From Touchpoint to Outcome: Transforming Front-Office Processes with AI"
author: ["LandingAI"]
url: "https://www.youtube.com/watch?v=d7s7MJNukpM"
date_published: 2026-05-26
date_ingested: 2026-06-09
length: "~46:15 minutes (transcript ~443 segments / ~8,350 words)"
raw: "../../raw/videos/from-touchpoint-to-outcome-transforming-front-office-processes-with-ai.md"
tags: [landing-ai, agentic-document-extraction, ade, document-intelligence, dpt, document-pre-trained-transformer, vision-first-ai, visual-grounding, ocr-accuracy-gap, octo, tcg, process-automation, front-office-automation, insurance-automation, kyc, financial-services, life-sciences, deployment-options, air-gapped, vpc, andrew-ng, vendor-webinar]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - digital-seizing/rapid-prototyping
  - strategic-renewal/business-model
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals
    via: "Both deploy AI to convert document-heavy, manual enterprise workflows into structured automated outcomes — Luminai wedges a fax-triage agent into hospital admin ($trillion US healthcare administrative spend); LandingAI + TCG/OCTO wedge document-extraction + process-orchestration into front-office customer journeys (insurance quote-to-bind, KYC). Same *paper/manual-substrate → AI-native digitisation layer* template, attacked from a vertical-app angle (Luminai) vs a horizontal-platform angle (LandingAI ADE + OCTO orchestration). Both quantify the win as manual-effort reduction (Luminai: triage automation at scale; OCTO: 85% faster claims processing, 75% efficiency gain)."
    confidence: 0.75
  - type: supports
    target: 2026-05-05-google-gemini-file-search-multimodal
    via: "Both target *verifiable, citation-grounded retrieval from unstructured documents* as the anti-hallucination requirement for enterprise document AI. Gemini File Search adds page-level citations + multimodal embedding for *rigorous fact-checking* over PDFs; LandingAI ADE makes every extracted value *visually grounded* back to the cell/word/figure for an audit trail (pitched at finance + life-sciences). Convergent framing — grounding/citation is the trust primitive — from a RAG-retrieval angle (Gemini) vs a structured-extraction angle (ADE)."
    confidence: 0.7
---

# From Touchpoint to Outcome: Transforming Front-Office Processes with AI

> Join us for a hands-on session focused on turning customer interactions into fully orchestrated, outcome-driven processes.
>
> - Turn customer interactions into outcomes—not handoffs
> - Create a connected customer experience for all front-office channels
> - Increase customer engagement by working the way they want, not being constrained by rigid out of date processes
> - Understand any document your customers submit (with LandingAI ADE)
> - Orchestrate end-to-end processes with OCTO
> - Deliver faster, consistent, scalable experiences that transform customer experience
>
> This session is ideal for operations leaders, automation teams, data and AI practitioners, and developers looking to bring document intelligence into production and deliver faster, more reliable customer experiences.
> — *LandingAI webinar description*

A two-vendor marketing **webinar** (auto-captioned, ~46 min, 67 views at ingest) pairing [[LandingAI]]'s **Agentic Document Extraction (ADE)** with partner **TCG**'s **OCTO** process-automation platform. A LandingAI presenter (the ASR renders his name inconsistently; left unpromoted) covers the product and a global-bank case study; **Neil Walker** of TCG demos OCTO orchestrating ADE inside an insurance / car-rental front-office flow. Founder [[Andrew Ng]] is named as LandingAI's origin but is not present. This is the wiki's **first source published from the LandingAI channel** and its first dedicated [[document-intelligence|document-intelligence]] source.

## TL;DR

- **The OCR accuracy-gap thesis.** Generic OCR (or OCR + LLM) tops out at *"80 or 90%"*, which *"isn't even close to where it needs to be"* — reliable agentic pipelines need *"the high 99 point something percent"* or the downstream agent stack inherits hallucination and adoption risk. Accuracy is framed as the gating constraint on [[enterprise-ai-adoption|enterprise AI adoption]] of document workflows.
- **Vision-first understanding + visual grounding.** ADE reads the page *as an image* — understanding blocks, structure, and human reading-order — rather than treating it as pixels + text. Built on proprietary **DPT** (Document Pre-trained Transformer; **DPT2** shipping, **DPT3** imminent), zero-shot (no training / fine-tuning), and **visually grounded**: every extracted value references back to the cell / word / figure, giving an audit trail that *"financial services and life sciences love"* and that suppresses hallucination.
- **The "octo-zone" orchestration thesis.** High-accuracy extraction is necessary but not sufficient. TCG's **OCTO** sits in the *"octo-zone"* — where *"different systems, services and people interact in order to achieve a particular outcome"* — normalising varied front-office inputs (post, email, WhatsApp, mobile capture, zip/embedded files) into *"one consistent view"*, then applying validation + grounding to push past *"mid to high 90%"* toward *"100% accuracy"* before downstream systems are touched.
- **Touchpoint → outcome.** The strategic pitch: stop treating customer interactions as *handoffs*; orchestrate them end-to-end so a customer uploading last year's renewal document receives *"a fully customized quotation without doing any data entry."* Front-office customer experience is *"totally transformed from the outside."*
- **Deployment for regulated industries.** Three options: **ADE Cloud** (multi-tenant, US or EU, optional zero-data-retention), **ADE VPC** (deploy into your AWS/Azure hyperscaler tenancy), and **on-prem air-gapped** (government / high-control financial orgs).
- **Quantified case (insurance, via OCTO).** A claims/first-notice-of-loss project: *"85% faster processing"* and *"over 75% increase in operational efficiency"*, which led the insurer to expand OCTO into a front-office new-business quote assistant. A global bank used ADE for KYC / client due-diligence / fraud detection, moving from *"hundreds of analysts... thousands of hours"* of manual review toward automation; *"every month... adding two or three [banks]."*
- **Pricing.** Both value-based: ADE by document volume/size (self-serve credit-card sign-up → enterprise tiers); OCTO by process complexity (number of specialist activities) with *"aggressive economies of scale"* at high volume.

## What was actually ingested

The **full auto-generated transcript** of the ~46-minute webinar (ASR-cleaned for proper nouns — see the raw file's `notes:`). No slides or PDF were captured; product claims (DPT accuracy benchmarks, the *"independent benchmark"* cited but not shown) are the presenters' verbal assertions, not independently verified. As a **vendor marketing webinar**, treat performance numbers (99.x% accuracy, 85% faster, 75% efficiency) as vendor-reported, single-case, and uncorroborated — confidence on any concept page this feeds is capped accordingly (see [[document-intelligence]]).

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — OCTO's core pitch is redesigning the front-office process itself: replacing manual review / hundreds of analysts / paper-and-email handoffs with an orchestrated extract → validate → ground → route pipeline that *"connects different systems, services and people"* into one outcome.
- **`digital-transforming/improving-digital-maturity`** — the OCR→agentic-extraction accuracy step-change and the *"works out the box... point your information to it"* zero-shot model are framed as letting an enterprise scale document AI across the organisation without per-document-type training, raising baseline digital maturity.
- **`digital-seizing/rapid-prototyping`** — OCTO's *"no-code approach"* + *"solution accelerators"* (claims processing, invoice processing, shared-mailbox triage) are pitched explicitly for building *"something we've never even seen before"* fast and condensing time-to-go-live for proofs of concept.
- **`strategic-renewal/business-model`** — *"turn customer interactions into outcomes—not handoffs"*: the insurer's move from claims automation to a self-service front-office quote portal that returns *"a fully customized quotation without doing any data entry"* is a customer-experience-led renewal of the front-office model.
- **`contextual/external-triggers`** — the insurer adopted OCTO partly because *"other people are offering these portals... they need to be able to respond quickly"*; competitive pressure to match market efficiency is the named external trigger.

## Linked entities and concepts

- [[LandingAI]] — promoted to an entity on this ingest (channel-author + central subject; founder [[Andrew Ng]] already referenced across the wiki). Vision-first document AI company; ADE + DPT product line.
- [[Andrew Ng]] — named as LandingAI founder/CEO; substantive cross-reference (this is the wiki's first source *from* the company he founded).
- [[document-intelligence]] — new concept page created on this ingest; ADE is its first product exemplar.
- [[enterprise-ai-adoption]] — the accuracy-gap-as-adoption-blocker and regulated-industry deployment story sit squarely here.
- [[responsible-ai]] — visual grounding / audit trail / anti-hallucination as a trust-and-accountability primitive for document AI.
- **Dangling** (single-source mention, deferred per author-entity promotion rule): **TCG** (process-automation vendor, est. 1996, OCTO product), **Neil Walker** (TCG presenter), **OCTO** (TCG product), **DPT / Document Pre-trained Transformer** (LandingAI proprietary model family). Promote on a second source.

## Related sources

- [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Luminai / YC]] — `supports`: parallel *manual-document-substrate → AI-native automation layer* play, vertical-app angle.
- [[2026-05-05-google-gemini-file-search-multimodal|Gemini File Search multimodal]] — `supports`: parallel *verifiable, citation/visually-grounded retrieval from documents* framing, RAG angle.
