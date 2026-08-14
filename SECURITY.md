# Security Policy: Planetary Energy Routing Protocol (PERP)

As an open-source conceptual framework for decentralized planetary energy management, systemic security, cryptography, and network resilience are our highest priorities. We are committed to patching vulnerabilities swiftly to protect local communities and microgrid nodes.

We operate on a strict **Zero-Trust Model**. No single contributor, developer, or automated system can alter the core logic of this protocol without rigorous, multi-party verification. This ensures the project remains resilient against hijacking, malicious injections, or supply chain attacks.

## 🚀 Supported Versions

We currently only support security updates for our main baseline branch.

| Version | Supported |
| :--- | :--- |
| v0.2.x | ✅ YES |
| < v0.2 | ❌ NO |

## 🔒 Core Repository Safeguards

To prevent anyone from hijacking the project or sneaking in dangerous code early on, we enforce the following rules:

### 1. The Two-Person Review Rule
* **No Direct Merges:** Direct pushing to the `main` or `master` branch is strictly disabled.
* **Mandatory Pull Requests:** All code updates, fixes, and feature additions must be submitted via a Pull Request (PR).
* **Independent Review:** Every Pull Request requires at least one comprehensive review and explicit sign-off from an authorized repository maintainer before it can be merged. 

### 2. Code Transparency & Anti-Obfuscation
* **Readability First:** We strictly reject any code that is obfuscated, hidden, or intentionally confusing. 
* **Clear Documentation:** Every script, algorithm, or configuration file must include plain-English comments explaining exactly what it does and why it is necessary.

### 3. Automated AI Guardrails
* This repository utilizes automated security scanners (including GitHub Dependabot). Any dependencies or external libraries with known vulnerabilities or insecure lifecycles will be blocked automatically.

## 🛡️ Reporting a Vulnerability

Please do not open a public GitHub Issue for security bugs or exploit vectors.

Publicly exposing vulnerabilities before a patch can be developed risks weaponizing decentralized grid components. Instead, please report all security concerns directly to the core maintainers.

* **Reporting Email:** widerview.web@gmail.com
* **Response Window:** The core maintainers will acknowledge your report within 48 hours and provide a regular status update until an open-source patch is pushed.

## 🔍 What We Are Actively Auditing

We are constantly watching out for threats against our core architecture:
1. **Tri-Key Consensus Loops:** Defeating the multi-agent recommendation consensus.
2. **Telemetry Spoofing:** Feeding malicious data payloads to bypass geoengineering thresholds.
3. **Workload Takeovers:** Manipulating the virtual grid balancing protocol to hijack regional data center computing streams.

Thank you for helping us keep the protocol safe for humanity.

