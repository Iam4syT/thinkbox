# Lab 2 — Vulnerability remediation, change and user communication workbench

Status: assistant-authored and locally evaluated on synthetic inputs, 30 September 2026. the learner has not independently completed this lab. Windows, Intune, Defender and optional AI exercises are unrun. Offline approval fields simulate a workflow; they do not grant permission for real changes.

## A. Outcome

Help a workplace engineer prioritise a software finding, obtain review, prepare a pilot, validate the result and explain the change to employees without closing an unresolved risk.

## B. Industry problem and research basis

This independent synthetic lab explores a recurring workplace support workflow. Reliable endpoint access and controlled changes can help employees use their workplace tools while preserving security oversight. These are design goals, not measured workplace outcomes. No employer commissioned the work; no internal estate, customer or incident data was used. The technical procedure is based on the linked Microsoft documentation, checked 30 September 2026. Actual tenant choices require local evidence, entitlement and approval.

## C. Job mapping

| Vacancy requirement | Exercise and boundary |
|---|---|
| Review endpoint vulnerabilities | Synthetic severity/exposure queue; optional Defender observation |
| Coordinate patch/config/software change or risk escalation | Six explicit workflow states, approval and escalation plan |
| Windows modern endpoint management | A scoped Intune update-ring runbook, unrun |
| Logs, root cause and suitable solutions | Separate delivery, installed version, restart, app health and security recheck |
| Keep employees/stakeholders informed | Deterministic messages plus human review and rollback communication |
| PowerShell/automation; pilots | Read-only Windows checks, Python proposals and staged validation |

This solution manages the change lifecycle. Lab 1 diagnoses readiness and faults before deciding a change. Neither script deploys software.

## D. Learner gap and claim boundary

This guide develops the difference between recognising a fault and configuring, validating and explaining a complete workflow. The offline scaffold demonstrates synthetic behaviour only. A learner must execute and explain the relevant steps before treating them as personal project evidence. Tenant procedures remain unrun; this package is not evidence of second-line or production administration.

## E. Recurring use

A workplace/security pair would review this queue weekly, whenever a significant finding arrives and before/after each deployment stage. Repeated value comes from consistent decisions, approved scope, understandable messages and checks that keep unresolved findings open. Target outcomes are fewer premature closures and safer handovers; this run measures decision behaviour, not risk reduction, patch speed or customer impact.

## F. Architecture and baseline

Synthetic findings → strict input checks → deterministic severity/exposure ordering → approval/validation state machine → proposed action and message → human change owner/security review. All outputs are local files. A finding can only be `closed_verified_in_fixture` when recorded approval, installed version, restart, application health and security recheck satisfy the rules. Unknowns stay visible. Priority order is an illustrative rule, not a banking risk model; asset criticality and active exploitation would need real evidence.

The deterministic baseline is implemented. Optional AI may rewrite an already verified message for clarity; it cannot approve, choose a patch, change priority, invent dates or execute changes. Prefer the baseline unless a reviewed comparison demonstrates a material improvement. No model, prompt service or live data is used in the built slice.

## G. Prerequisites, licences and cost

Offline: Python 3.11+, text editor and supplied `public/` folder; standard library only. Budget 60–90 minutes as an estimate. No cloud charges or credentials.

Windows/Intune path: a disposable supported Windows 11 Pro/Enterprise device, snapshot or reliable reimage recovery, one test user, Intune Plan 1 entitlement and an isolated assigned device group. Reuse an evidenced enrolment from Lab 1 or complete that runbook first. Do not assume Intune supports Windows Home for this path. Existing Autopatch-managed devices must not receive an overlapping custom ring.

Defender path additionally needs a checked Defender for Endpoint/core Vulnerability Management entitlement; Plan 2 includes core vulnerability management, with advanced add-on/standalone options. Portal access alone is not licensing evidence. Use scoped read/manage permissions according to the task; service integration requires appropriate Intune/Defender setup rights. [Vulnerability Management prerequisites](https://learn.microsoft.com/en-us/defender-vulnerability-management/tvm-prerequisites); [integration prerequisites](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/overview), checked 30 September 2026.

Trial availability, expiry, data handling, renewal and pricing are unknown until checked. Do not purchase anything or start a trial from this run. Offline mode is the useful low-cost substitute, but does not prove scanning, task synchronisation or patch delivery. Plan 4–6 hours over two sessions for a one-device tenant exercise, plus reporting delays. An optional AI comparison would need an approved service, synthetic inputs, a cost cap and a fresh evaluation; no cost estimate is asserted here.

## H. Granular procedure

### 1. Record a reproducible starting point — offline, assistant-run

Start: the fresh `public/` folder. Action: run `python3 --version`; on Windows use `py -3 --version`. Read `CONTRIBUTIONS.md` and inspect `templates/findings.json`. Expected: six `LAB-VULN-` findings and no real CVEs, customers, users or secrets. Verify: record runtime and file hashes. Recovery: obtain an approved Python runtime if absent; if the data contains real identifiers, restore the synthetic fixture before proceeding. All version values are training values, not actual vulnerable software releases.

### 2. Define a manual baseline before using automation

Start: six unclassified findings. Action: list severity, exposure, patch availability, approval, installed version, reboot, app smoke test and security recheck. Decide a next action manually. Expected: 01 needs approval; 02 is ready for a test pilot; 03 escalates; 04 needs recheck; 05 passes synthetic closure; 06 needs rollback review. Verify: justify closure using every required field. Recovery: replace any assumed “probably patched” field with `null`. Manual time and human error rate have not been measured.

### 3. Produce the proposal and user messages

Start: unchanged fixtures. Action: run `python3 scripts/change_workbench.py --output outputs/change-plan.json`. Expected: six rows, LAB-VULN-03 first and `mutation: none`. Verify: inspect each state, reason and message; no message promises an unagreed date. Recovery: input rejection exits 2; correct explicit types, severity or versions rather than converting arbitrary text into approval. The program cannot approve a change or contact an employee.

### 4. Read the risky cases carefully

Start: the generated queue. Action: compare LAB-VULN-03 and LAB-VULN-06. Write an escalation note for the former with risk, affected synthetic scope, missing information, proposed owner and next review; write a stop-expansion/recovery-review note for the latter. Expected: an unpatched critical finding remains open, and a failed app health check prevents closure. Verify: the notes distinguish “installation completed” from “safe, validated outcome”. Recovery: if a message implies automatic rollback, rewrite it; the named change owner must decide recovery.

### 5. Run behavioural tests

Start: unmodified source. Action: run `python3 -m unittest discover -s tests -v`. Expected: ten tests pass. They cover six states, critical ordering, approval, old version, unknown recheck/exposure, malformed approval, duplicate findings, empty input and numeric version comparison. Verify: version `2.10` compares above `2.9`, not below through text sorting. Recovery: save failed output and fix its underlying rule; do not weaken a closure gate merely to pass.

### 6. Reproduce a premature-closure fault

Start: a copy `templates/learner-fault.json`. Action: change LAB-VULN-05's `security_recheck_pass` from true to null; run `python3 scripts/change_workbench.py --input templates/learner-fault.json --output outputs/fault.json`. Expected: `verify_again`. Verify: restoring the field to true returns synthetic closure only when all other gates remain satisfied. Recovery: if evidence is unavailable in a real scenario, keep the ticket open and agree the next check. Never treat task status alone as proof that a vulnerability disappeared.

### 7. Prepare an explicit change record — optional tenant path, unrun

Start: an isolated enrolled VM and authorised lab owner. Action: privately record device alias, current build (`cmd /c ver`), app launch result, recovery snapshot, update source and existing policy assignments. Write a change with purpose, one-device scope, maintenance window, expected restart, test steps, stop condition, recovery and approval owner. Expected: a reviewable plan before deployment. Verify: confirm the Windows edition, group membership and absence of conflicting update management. Recovery: if the device has no suitable applicable update, document that limitation and keep delivery untested; do not install an obsolete vulnerable release to manufacture a finding.

### 8. Create a narrow update ring — optional, unrun

Start: an approved one-device test change. Action: Intune Devices → By platform → Windows → Manage updates → Windows updates → Update rings → Create profile. Name `LAB-Patch-Pilot`, review defaults and assign only the dedicated device group. Expected: one scoped ring. Verify: screenshot settings, assignments and policy check-in report; this proves policy intent, not installation. Recovery: if an existing Autopatch/custom ring owns the device, resolve ownership before adding another. [Update-ring creation and scope](https://learn.microsoft.com/en-us/intune/device-updates/windows/manage-update-rings).

### 9. Make user experience settings deliberate — optional, unrun

Start: the new lab ring. Action: for this disposable device use quality update deferral 0 days, block driver updates, leave feature upgrades outside the exercise and choose an automatic-update behaviour with user-visible restart control. Agree active hours with the test user; leave forced deadlines unconfigured for this first lab. Expected: a documented training choice that preserves an agreed restart. Verify: compare the portal values with Windows Update → Advanced options → Configured update policies. Recovery: if the current portal presents different supported options, use the linked reference, record the exact value selected and retain a safe manual window. These values are not recommendations for a production estate. [Ring settings](https://learn.microsoft.com/en-us/intune/device-updates/windows/ref-update-ring-settings).

### 10. Validate policy delivery and the actual update — optional, unrun

Start: online test device, saved work and approval. Action: Settings → Accounts → Access work or school → test connection → Info → Sync; review policy status and Windows Update. Check for applicable updates and use the agreed restart window. Expected: either a documented update attempt or a clear no-applicable-update result. Verify: compare pre/post `ver`, installed update history, reboot state and application launch. Inspect Event Viewer → Microsoft → Windows → WindowsUpdateClient and MDM Admin logs if needed. Recovery: first distinguish policy failure from Windows download/install failure; check connectivity/source/assignment, then record a supported next test. Do not edit registry values as a shortcut. [Microsoft update-ring troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/mem/intune/device-protection/troubleshoot-update-rings).

### 11. Connect and onboard Defender only in a disposable tenant — optional, unrun

Start: verified entitlement and setup roles, with prior settings captured. Action: Intune Endpoint security → Defender for Endpoint; if not enabled, Defender System → Settings → Endpoints → General → Advanced features → Intune connection On, then save. Back in Intune, create a custom Endpoint detection and response policy, Windows platform, Auto from connector, assigned only to the lab device group. Expected: enabled connector, scoped policy and device in Defender inventory. Verify: record policy/device state; setup may take time. Recovery: check role, entitlement, connectivity and assignments; do not use broad preconfigured All Devices deployment. No Conditional Access or tenant risk blocking is added. [Integration procedure](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

### 12. Observe an actual recommendation without creating risk — optional, unrun

Start: onboarded lab device with normal supported software. Action: in Defender open Exposure management → Vulnerability management → Recommendations; choose a recommendation affecting this lab device if one exists. Record its real supporting advisory, current software/build, scope and recommended action privately. Expected: either an evidence-backed recommendation or “no suitable recommendation observed”. Verify: do not replace actual evidence with synthetic LAB-VULN data. Recovery: if there is none, complete the offline queue and record this path as untested; no vulnerable installation or protection disabling is required. [Remediation request workflow](https://learn.microsoft.com/en-us/defender-vulnerability-management/tvm-remediation).

### 13. Hand off and validate a security task — optional, unrun

Start: a supported real lab recommendation and approved scope. Action: the authorised security owner creates a remediation request with the lab device scope, review date and notes, selecting an Intune security task where supported. In Intune Endpoint security → Security tasks, review the task and Accept only within the agreed change. Perform the approved action; compare endpoint evidence, app health and subsequent Defender recheck before marking Complete Task. Expected: linked human-owned task; not every finding supports Intune remediation. Verify: security-owner confirmation and post-change evidence, not just status. Recovery: no task may mean connector, onboarding, unsupported recommendation or synchronisation; investigate rather than invent success. [Intune security tasks](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/remediate-vulnerabilities).

### 14. Rehearse operational handover

Start: the offline report or actual evidence from a completed tenant run. Action: write three messages: before change, incomplete verification and confirmed result. Include scope, impact, agreed window if known, employee action and support route. Expected: plain words and no unsupported claim that risk is eliminated. Verify: a colleague can identify who owns the next action. Recovery: if a restart or application test is pending, say so and keep the case open. This can be practised offline without sending any message.

### 15. Optional bounded AI comparison — planned only

Start: the deterministic message and synthetic evidence facts. Action: ask an approved model to improve wording using only those facts; forbid adding approvals, dates, patch instructions, recipients or completion claims. Have a human compare ten held-out synthetic messages against the baseline for clarity, unsupported facts and missing employee actions. Expected target: zero invented facts and no lost safety gate; benefit is unestablished. Verify: reject any incorrect draft, log failures/cost/time and retain the deterministic fallback. Recovery: do not use AI if it fails these checks or adds no clear value. No model integration or measured AI result exists in this scaffold.

## I. Break/fix and J. acceptance

Offline acceptance: six distinct states; missing approval/recheck or old version prevents closure; app failure triggers recovery review; unknown exposure escalates; invalid types reject; empty input is no data; ten tests pass. Tenant acceptance additionally requires correct scope, delivered ring, observed update or explicit no-update limitation, pre/post app health and an agreed restart. Defender integration/actual remediation can only pass after evidence is observed. A delivered policy or completed security task alone is insufficient. Manual Windows app checks demonstrate a small method, not a complete bank endpoint assurance process.

## K. Artefacts and cleanup

Keep source, synthetic data, source hashes, actual test output, proposal, review notes and `docs/architecture.md`. A future tenant run should retain private raw observations and sanitised screenshots/video only with permitted content. No recording is fabricated.

Offline: remove the temporary learner fixture and generated `outputs/` after saving evidence. Tenant: remove only this lab's assignments/ring after recording its settings; ring deletion does not necessarily restore prior device values. Restore the VM snapshot/reimage to the agreed baseline. If Defender was onboarded here, remove onboarding assignment first, obtain a current offboarding package and use the documented scoped offboarding procedure; never deploy onboarding/offboarding together. Verify stopped reporting and retain awareness of service data retention. Restore connector settings only if created solely for this isolated lab and no other device depends on them. Remove temporary roles/accounts and cancel unused trials through billing, checking renewal status. [Microsoft offboarding](https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm).

## L. Interview narrative

After your own run: “I separated patch approval from installation and verification. My synthetic queue kept unknown risks open and stopped wider rollout when an app check failed. I tested the rules, including a missing recheck and version comparison. [Only if completed: I then tested one device through a scoped update and documented the evidence.] The lesson was that clear communication and evidence matter as much as deployment status. I have not operated this in a production bank.” Explain how a critical no-patch case would reach a security/risk owner without claiming authority to accept the risk.

## M. Conditional future wording and N. extension

Use only after the learner independently completes and explains the evidence: “Built and tested a synthetic remediation workbench with approval, version, restart and health checks, producing reviewable change proposals and clear user messages.” Add tenant or Defender wording only for the actual completed path; do not call synthetic closure real remediation.

Next version: add asset criticality and exploitation signals from permitted sources; test human override and audit records. AI stays an optional drafting aid. Cloud/API or CI work should preserve least privilege and keep tenant changes out of ordinary CI. All linked technical documentation was checked 30 September 2026; reread current prerequisites and screens before execution.
