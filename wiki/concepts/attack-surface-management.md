---
type: concept
aliases: ["attack surface management", "ASM", "external attack surface", "EASM", "external attack surface management"]
tags: [attack-surface-management, cybersecurity, infosec, exposure-management, shadow-it]
confidence: 0.70
last_confirmed: "2026-05-18"
accessed_at: "2026-05-18"
source_count: 2
relationships:
  - type: depends-on
    target: osint
    via: "ASM uses OSINT techniques to discover externally visible assets"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Attack Surface Management

The continuous discipline of **discovering, cataloguing, and monitoring every externally observable asset** that belongs to an organisation, so that exposure is known before an attacker uses it. The operating principle, in the framing of [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]]: *"You can't protect what you can't see."*

## Working definition

Attack-surface management (ASM) — sometimes "external attack surface management" (EASM) when the scope is specifically internet-visible assets — answers four operational questions on a continuous loop:

1. **What assets does my organisation expose to the public internet?** (Servers, subdomains, certificates, cloud buckets, APIs, IoT, ICS/SCADA, login panels.)
2. **Which exposed assets are known to my security team, and which are not?** (The unknown set is **shadow IT** — forgotten dev servers, legacy systems, employee-spun cloud resources.)
3. **What is the security posture of each exposed asset?** (Vulnerabilities, misconfigurations, leaked credentials, exposed code.)
4. **What changed since the last scan?** (New asset appeared, old asset became vulnerable, certificate expired, credential leaked.)

The discipline is *continuous* by construction — the attack surface drifts as the organisation deploys new services, employees leave systems behind, and the internet itself reshuffles around it.

## Key claims

### ASM presupposes OSINT — the discovery layer is the same

Per [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]]: the platforms that map an organisation's attack surface — Shodan, Censys, FOFA, ZoomEye, FullHunt, SecurityTrails, SpiderFoot — are the same platforms attackers use for reconnaissance. ASM is **defensive [[osint|OSINT]] organised as continuous practice**. The asymmetry between attacker and defender is not in the tools; it is in *who runs them first and how often*.

### The five-step OSINT workflow is the ASM workflow

The same five-step recon flow that an attacker would run against a target is the workflow a defender runs against their own organisation (TechLatest 2026):

1. **Discover infrastructure** — Shodan / Censys / FOFA / ZoomEye to enumerate exposed services.
2. **Enumerate domains & certificates** — crt.sh / SecurityTrails / FullHunt for subdomains and certificate-transparency-derived assets.
3. **Analyse web technologies** — URLScan and Grep.app to detect tech stacks and find leaked secrets in public code.
4. **Check identity exposure** — Hunter / HIBP / DeHashed for harvested emails and breach exposure.
5. **Correlate vulnerabilities** — Vulners (CVEs + exploits) and GreyNoise (separate targeted-vs-noise) to prioritise.

The deliverable is a current map of *what an attacker would learn in two hours of free-tier recon*, which is the question [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] answered narratively for her own organisation.

### Shadow IT is the load-bearing failure mode

Both wiki sources foreground **shadow IT** — unmanaged, forgotten, or unauthorized assets — as the most exploitable category of attack surface. Khan 2026 found a public GitHub repo with internal API endpoints and a commented-out admin credential that *had been there for three years*. TechLatest 2026 names "shadow IT" explicitly as one of the four Shodan attack-surface-discovery use cases (alongside forgotten servers, old dev systems, misconfigured cloud assets). The pattern: ASM doesn't fail because the team didn't deploy correctly; it fails because the *known set of assets to monitor* doesn't include the ones nobody remembers.

### Five operational best-practices

Per TechLatest 2026, the operational discipline:

1. **Continuously monitor your attack surface** using external scanning against your own infrastructure.
2. **Monitor credential leaks** by tracking employee email exposure in breach datasets.
3. **Audit public repositories** for secrets, API keys, tokens, credentials.
4. **Track shadow IT** — actively hunt unmanaged or unauthorized assets.
5. **Automate reconnaissance** by integrating OSINT platforms into SIEM pipelines, SOC workflows, and threat-intelligence systems.

### Detection-first beats response-first

Both sources converge on a posture: the future of cybersecurity belongs to organisations that **continuously map their attack surface, automate intelligence collection, detect exposure early, and respond faster than attackers** (TechLatest 2026). Khan 2026's narrative is the worked example — once the audit was run, leadership rotated credentials and set up automated public-repo secret scanning. The fix came *after* the discovery; the discovery was the bottleneck.

## Debates and supersession

- **Open question — automation depth.** Both sources advocate automation but neither names a specific reference architecture for an ASM pipeline at production scale. The "AI-Augmented Offensive & Defensive Security" category named in TechLatest 2026 (LLMs + [[ai-agents]] correlating OSINT sources, generating attack graphs) is the plausible future of automated ASM but is still at vendor-narrative depth.
- **No supersession events yet.** Young concept page; no prior wiki claim to retire.

## Related pages

- [[osint]] — the discovery discipline ASM depends on.
- [[ai-agents]] / [[agent-harness]] — the substrate AI-augmented ASM relies on.
- [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] — narrative worked example of a one-off audit.
- [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] — platform catalogue and continuous-workflow framing.
