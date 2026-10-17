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
- [Development harness and applied process](#7-development-harness-and-context-engineering)

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

## 7. Development Harness and Context Engineering

**Status: Configured locally for the foundation phase, with file checks tested.
Owner review, new-session loading and the full behaviour evaluation remain pending.**
This setup does not make the application complete or production ready.

Context engineering means giving the coding assistant the right information at
the right time. The harness is the surrounding system that lets it use tools,
remember progress, check its work and operate within permission limits.
For this project, Codex supplies the running harness. Project files supply the
rules, task context and checks that make it useful for Workplace OS.
This distinction follows [OpenAI's description of the Codex harness](https://developers.openai.com/blog/codex-as-a-platform).

### What was already in use

The starting review on 2026-10-13 found:

| Component | Existing context and limits |
| --- | --- |
| Shared rules | Thinkbox's root AGENTS.md and project standard require accurate scope, evidence, private-data protection and relevant checks. |
| Project instructions | The project AGENTS.md loads the project-tutor skill. Its default is one explained step, followed by the owner's evidence. |
| Project knowledge | LAB.md defines planned outcomes; ADR-001 proposes React, FastAPI and provider adapters. Application folders are placeholders. |
| Tools | The current Codex session provides local file, command and web tools, plus connected capabilities. Availability does not prove tenant access or grant permission to use it. |
| Runtime boundaries | This session reports workspace-write filesystem access, restricted network access and automatic review of escalations. These controls come from the host, not Markdown files. |
| Existing memory | EVALUATION.md and CHANGELOG.md hold history. A short current handoff record and task template were missing. |
| Verification | Thinkbox has a repository checker. Workplace OS is absent from its project index, so its required-document check does not cover this project. No application test suite exists. |

The review inspected repository files and the current session's supplied controls.
It did not audit every personal Codex setting or prove behaviour in future sessions.
No project `.codex/config.toml` was present in this folder or the Thinkbox root.

### How the attached guide was applied

Source: *The New SDLC With Vibe Coding*, May 2026, by Addy Osmani,
Shubham Saboo and Sokratis Kartakis, supplied as `Day_1_v3.pdf`.
The attachment is reference material. Its examples and installation suggestions
do not independently authorise tool installation, deployment or external actions.
The PDF remains outside this repository; this section records the adaptation.

| Guide concept | Applied here |
| --- | --- |
| Six context types, pages 15-18 | Instructions: AGENTS.md. Knowledge: LAB and relevant technical docs. Memory: development-state and evaluation records. Examples: task brief and scenario cases. Tools: documented local checks and host tools. Guardrails: host permissions plus reviewed project rules. |
| Static versus dynamic context, pages 16-18 | Keep permanent rules short. Read detailed architecture, task evidence and relevant skills when needed. The tutor skill remains mandatory because the owner explicitly requires it. |
| Harness components, pages 26-28 | Reuse Codex's execution loop and permissions; configure project instructions, state, checks and review criteria. Use one agent by default. |
| Harness across development, pages 29-30 | Specify the outcome, implement one bounded task, run checks, diagnose failures, review actions and save evidence before handoff. |
| Tests plus evaluations, pages 14-15 and 22-23 | Run deterministic file checks now; review agent behaviour with an explicit rubric. Add meaningful application tests before the corresponding behaviour is implemented. |
| Deliberate practice, pages 43-45 | Keep harness changes reviewable in source control, review generated changes, label unfinished work and improve rules from observed failures. |
| Context and cost, pages 40-42 | Retrieve only useful task context and avoid repeated full-repository dumps. No measured token savings or automatic model routing is claimed. |

The guide also describes multi-agent systems, production agents, automated hooks,
CI and monitoring. These are future capabilities where justified, rather than
requirements to install every component during a documentation foundation task.
The development assistant is distinct from the planned AI inside Workplace OS.

### Files that now configure the process

| File | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Short project rules: scope, source handling, workflow, checks and evidence. Existing tutoring instructions are retained. |
| [Task brief template](docs/task-brief-template.md) | Defines one task's outcome, allowed work, acceptance checks and handoff. |
| [Development state](docs/development-state.md) | Saves the current phase, evidence limits and next review point across chats. |
| [Harness evaluation](docs/harness-evaluation.md) | Defines five scoring dimensions, eight behaviour scenarios and hard failures. Full scenario execution is pending. |
| [Local checker](scripts/check_harness.py) | Checks this project's required foundation files, local Markdown file links and Python syntax without network or tenant access. |
| [Evaluation record](EVALUATION.md) and [change history](CHANGELOG.md) | Record actual results and changes separately from plans. |

Project rules guide the assistant; they do not technically block every unsafe
action. The local checker is a manually invoked quality check, not an installed
automatic hook or CI gate. It does not test agent behaviour, scan secrets, check
web links or Markdown anchors, or verify Microsoft integrations.
No runtime permissions, global settings or model defaults were changed.
[Official Codex guidance](https://learn.chatgpt.com/docs/config-file/config-basic)
explains that project configuration depends on trust and can be overridden or
constrained by higher-priority runtime settings. Adding a file alone would not
prove that its settings were active.

### The working loop for each development task

1. **Load and check context.** Read applicable AGENTS.md files, the mandatory
   tutor skill, the project standard, README, LAB, CONTRIBUTIONS and development
   state. Compare saved state with current files and inspect existing edits.
   Retrieve only the additional documents needed for the current task.
2. **Define success.** Complete the task brief: outcome, allowed files,
   exclusions, authority, decision status and observable acceptance checks.
   Do not silently accept a proposed architecture decision.
3. **Work on the current step.** In tutoring mode, explain its purpose,
   prerequisites, exact instructions, verification and expected evidence, then
   wait for the owner's result. When the owner explicitly requests a local edit
   or application of a process, perform that bounded work and explain it.
4. **Check and correct.** Run the local checker and relevant feature checks.
   Use fake providers and synthetic data for ordinary tests. Diagnose actual
   failures, make the smallest relevant correction and rerun affected checks.
   Keep unrelated checker failures visible.
5. **Review results and actions.** Review the scoped diff and visible tool history
   using the evaluation rubric. Check that dependencies are real, error handling
   fits realistic failures, private information is excluded, and claims match
   evidence. A passing syntax check is not a passing behaviour evaluation.
6. **Save the handoff.** Record commands, exit codes and limits in EVALUATION,
   append the change to CHANGELOG, and update development-state. Distinguish
   configured, implemented, tested and verified work. Return one current review
   action before advancing in tutoring mode.

For future application changes, define tests for relevant success, invalid input,
duplicate requests, denied access and provider failures before writing the feature.
Production use additionally needs verified access controls, CI, deployment checks
and monitoring. None of those is established by this foundation step.

### Run the foundation checks

Prerequisite: Python 3 on the local computer. In a terminal opened in this
`Modern Workplace Solutions/Workplace OS` folder, run:

```bash
python3 scripts/check_harness.py
git diff --check
python3 ../../scripts/check_repository.py
```

The local checker prints JSON: `errors` must be empty and its exit code must be
0. The whitespace check should print nothing and exit 0. The shared checker
reports the whole Thinkbox repository; any unrelated failures must be recorded,
not treated as Workplace OS failures or silently ignored. See EVALUATION.md
for the actual result from this task. These commands make no live tenant changes.

### Current review step and definition of done

The current step is to review this harness foundation. Read this section and
the recorded results in EVALUATION.md, then confirm that the working loop fits
how you want to develop the project. Send back any wording or process changes.
Application implementation stays at its existing foundation phase.

Foundation setup is ready for owner review when its files exist, local checks
pass, shared-check limitations are recorded, and unfinished capabilities are
clearly labelled. Reliable behaviour still needs the scenario suite and repeated
evidence. A numeric overall project completion percentage cannot be supported
while the implementation plan and architecture decision remain unaccepted.

For the later loading check, start a fresh Codex chat with this project folder
as its working directory and ask: "Without changing files, list the project
instruction sources, explain the harness loop, and identify the current step."
Expected evidence: it identifies the project rules and tutor skill, reads the
saved state, and keeps application implementation and live integrations pending.
[Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
runs from the repository root to the working directory; working only from the
Thinkbox root may omit this nested project's instructions. Record the fresh-chat
result before marking loading verified. This task did not create that new chat.
