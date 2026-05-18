---
type: concept
aliases: ["OSINT", "open-source intelligence", "open source intelligence"]
tags: [osint, cybersecurity, infosec, reconnaissance, attack-surface, threat-intelligence]
confidence: 0.75
last_confirmed: "2026-05-18"
accessed_at: "2026-05-18"
source_count: 2
relationships:
  - type: part-of
    target: attack-surface-management
    via: "OSINT is the discovery discipline that feeds attack-surface management"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# OSINT (Open-Source Intelligence)

The disciplined gathering and analysis of **publicly available information** about a target — people, organisations, infrastructure, code — using only legal channels. The same techniques are used by attackers (to map targets before exploitation) and defenders (to audit their own exposure before attackers do). Both sides work from the same data; the difference is intent and authorization.

## Working definition

Per [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]]: OSINT covers information from *websites, DNS records, internet-connected devices, public databases, leaked credentials, git repositories, metadata, social media, wireless networks, and search engines*. Its operational uses span **attack surface management, threat hunting, vulnerability discovery, breach investigations, brand monitoring, reconnaissance automation, and digital forensics**.

The defining property is *no privileged access* — no exploits, no credentials, no insider data. Everything the OSINT practitioner uses is data the target (or third parties) has already chosen to publish.

## Key claims

### OSINT runs on the gap between "what you publish" and "what you think you publish"

The [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] narrative walkthrough is the wiki's canonical worked example. In two hours and using only a browser, Khan found her own organisation's: developer comments revealing internal server URLs; image metadata with GPS coordinates; employee emails harvested via LinkedIn + password-reset-form account enumeration; a GitHub repo with internal API endpoints and a commented-out admin credential left public for three years; job postings disclosing the tech stack; office photos with employee badges and whiteboard diagrams in frame; Google dorks (`site:` + `ext:pdf` + `intitle:"index of"`) surfacing forgotten internal documents.

The unifying mechanism: *"Everything I found was public. We just never thought to look."* Defensive OSINT exists because organisations don't audit what they themselves publish.

### Hacker search engines vs general search engines

Per [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]]: Google indexes *webpages*. Hacker search engines index **open ports, exposed cameras, databases, cloud buckets, SSH servers, APIs, SSL certificates, industrial control systems, IoT devices, login panels, web technologies, vulnerabilities, leaked credentials**. They produce a real-time map of internet-exposed assets — fundamentally a different layer of the network than what Google sees.

This makes them load-bearing for the modern defender's question: *what is publicly exposed about my organisation that I don't know about?*

### Five-category taxonomy of OSINT platforms

The corpus's primary cataloguing source (TechLatest 2026) organises ~18 platforms into five categories:

| Category | Platforms named | What they discover |
|---|---|---|
| **Infrastructure Intelligence** | Shodan, Censys, FOFA, ZoomEye | Servers, IoT, ICS/SCADA, cloud assets, certificates |
| **Identity & Breach Intelligence** | Hunter, Have I Been Pwned, DeHashed | Emails, leaked credentials, breach exposure |
| **Web & Code Intelligence** | URLScan, Grep.app, crt.sh | Site behaviour, leaked secrets in public code, subdomains via cert transparency |
| **Vulnerability Intelligence** | Vulners, GreyNoise, FullHunt | CVEs, scanning activity, external exposure posture |
| **Deep OSINT & Exposure Mapping** | WiGLE, Intelligence X, LeakIX, SecurityTrails, SpiderFoot | Wireless, historical/dark-web data, exposed databases, DNS history, automated multi-source recon |

The standard five-step workflow combines them: *(1) infrastructure discovery → (2) domain & certificate enumeration → (3) web-tech & code analysis → (4) identity-exposure check → (5) vulnerability correlation*.

### AI-powered OSINT is an emerging category

TechLatest 2026 names **"AI-Augmented Offensive & Defensive Security"** as a 2026 category emerging from integrating LLMs and [[ai-agents]] with OSINT pipelines. Stated capabilities: correlate multiple OSINT sources, identify risky exposures automatically, generate attack graphs, detect infrastructure relationships, automate reconnaissance workflows. This is the one current bridge from the OSINT corpus into the wiki's broader [[agent-harness]] / autonomous-agent thread — though the claim is still at vendor-narrative depth, not empirically anchored.

### Defensive OSINT as standard practice

Both wiki sources frame OSINT as a *defender's* discipline first. Best-practice claims (TechLatest 2026): continuously monitor your own attack surface; track credential leaks affecting employees; audit public repositories for secrets / API keys / tokens; track shadow IT; automate recon into SIEM and SOC pipelines. Khan 2026's closing call is the same at narrative scale: *"Run a simple OSINT audit on your own organization. […] The attackers are already doing this. Now you can too — defensively."*

## Ethical and legal envelope

OSINT is legal by construction (only public data), but the *use* of that data can cross into illegal territory. Per TechLatest 2026, the framing is: authorization requirements, responsible disclosure, privacy laws, platform terms of service, and ethical hacking guidelines must be followed; OSINT tools must not be used for unauthorised intrusion, credential abuse, stalking, harassment, or illegal surveillance. *"The line between reconnaissance and illegal activity depends heavily on intent and authorization."*

## Debates and supersession

- **Open question — depth of the AI-OSINT claim.** TechLatest 2026 names "AI-Augmented Offensive & Defensive Security" as a 2026 category but the supporting detail is taxonomy-level, not empirical. The wiki has substantial primary-source depth on [[agent-harness]] and autonomous-agent runtimes but no source yet that benchmarks AI-augmented OSINT specifically. Future ingests would tell us whether this is a substantive emerging category or a vendor-narrative buzzword.
- **No supersession events yet.** This is a young concept page on a topic the wiki has just started covering.

## Related pages

- [[attack-surface-management]] — the management discipline OSINT discovery feeds into.
- [[ai-agents]] / [[agent-harness]] — the runtime substrate that AI-augmented OSINT depends on.
- [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] — narrative walkthrough.
- [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] — platform taxonomy and workflow.
