# AFRIST Modern Workplace OS

[![Platform](https://img.shields.io/badge/Platform-Microsoft%20365-0078D4?style=flat-square&logo=microsoft)](https://www.microsoft.com/microsoft-365)
[![Architecture](https://img.shields.io/badge/Architecture-Cloud--Agnostic%20Control%20Plane-blueviolet?style=flat-square)](#)
[![Compliance](https://img.shields.io/badge/Governance-Zero--Trust-green?style=flat-square)](#)

> **A Microsoft 365 foundation and workplace control plane for AFRIST Modern Workplace Solutions.**

---

## 1. Executive Overview

**AFRIST Modern Workplace OS** is an engineering project for a secure, repeatable workplace foundation and a provider-neutral control plane. The planned solution connects identity, access, devices, collaboration and governance through employee lifecycle workflows, desired-state verification and auditable approvals. Microsoft 365 is the first intended provider.

The current deliverable is a documented foundation: scope, acceptance criteria, an architecture proposal and evaluation records. Application capabilities and live integrations remain planned and unverified.

### Key Objectives:
- **Zero-Trust Identity & Access Management:** Entra ID governance, Conditional Access policies, Privileged Identity Management (PIM), and automated lifecycle workflows.
- **Unified Endpoint Management:** Intune compliance baselines, device configuration profiles, and zero-touch Autopilot provisioning.
- **Information Protection & Purview Governance:** Sensitivity labels, data loss prevention (DLP), and boundary controls before AI ingestion.
- **Extensible SaaS Adapters:** Architecture designed to keep cloud-specific logic behind clear interfaces for cloud-agnostic portability.

---

## 2. Documentation

### Engineering Documentation
- [Implementation scope and acceptance criteria](LAB.md)
- [Architecture](docs/architecture.md) and [proposed provider-adapter decision](docs/adr/ADR-001-control-plane-and-adapters.md)
- [Recorded contributions](CONTRIBUTIONS.md)
- [Demonstration walkthrough](DEMO%20SCRIPT.md)
- [Evaluation results and limitations](EVALUATION.md)
- [Change history](CHANGELOG.md)

Technical documents marked Planned will be completed alongside their corresponding implementation and verification.

---

## 3. Repository Structure

```text
Modern Workplace Solutions/Workplace OS/
├── README.md
├── LAB.md
├── CONTRIBUTIONS.md
├── DEMO SCRIPT.md
├── EVALUATION.md
├── CHANGELOG.md
├── .env.example
├── app/                  # API and frontend placeholders
├── config/               # Configuration placeholders
├── docs/                 # Technical documents and architecture decisions
├── infra/                # Infrastructure placeholders
└── scripts/              # Automation placeholders
```

---

## 4. Governance & Safety Notice

Per repository project standards, tenant-specific configurations, credentials, API tokens and private client data are maintained outside this public codebase. Validation uses dedicated non-production tenants, test identities and disposable devices where appropriate. Simulated results must be labelled explicitly.
---

## 5. Engineering Status

### Current phase

Foundation — Project Workspace and Documentation.

### Verified

- Project repository location and documentation scaffold established.
- Baseline documentation publication verified at commit `6dec95e`.
- Implementation scope and architecture proposal committed locally at `be95575`.

### In Progress

- Foundation documentation completion and review.
- Architecture decision acceptance.

### Planned / Not Yet Implemented

- Microsoft 365 tenant baseline
- Entra identity foundations
- Intune device management
- Microsoft Graph provider adapter
- FastAPI control plane
- Joiner workflow
- Mover workflow
- Leaver workflow
- Teams / SharePoint collaboration integration
- Planner task integration
- Defender operational signals
- Purview governance
- Drift detection and reconciliation
- React workplace portal
- AI status explanations and approval controls
- Automated testing
- CI/CD
- Hosted deployment
- Observability and operational runbooks

> A capability is not considered complete until implementation evidence and verification exist.

## 6. Development Prerequisites

The project will progressively use:

- Git
- VS Code
- Python 3.12+
- Node.js LTS
- PowerShell 7
- Microsoft Graph PowerShell SDK
- Microsoft 365 / Entra / Intune non-production tenant with appropriate licensing
- Azure subscription for hosted components where required

See the project documentation for the requirements of each implementation phase.
