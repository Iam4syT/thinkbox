# Lab 1 — Endpoint readiness and diagnostic evidence workbench

Status: assistant-authored and locally evaluated using synthetic data on 30 September 2026. the learner has not independently completed this lab. All Intune, Windows VM, Microsoft 365 and tenant steps below are unrun. This learning instrument does not establish second-line or production Intune administration.

## A. Outcome

Help a workplace engineer turn a device snapshot and diagnostic evidence into a clear investigation plan, then practise enrolling, configuring, checking and supporting one isolated Windows device.

## B. Industry problem and research basis

This independent synthetic lab explores a recurring workplace support workflow. Reliable endpoint access and controlled changes can help employees use their workplace tools while preserving security oversight. These are design goals, not measured workplace outcomes. No employer commissioned the work; no internal estate, customer or incident data was used. The technical procedure is based on the linked Microsoft documentation, checked 30 September 2026. Actual tenant choices require local evidence, entitlement and approval.

## C. Job mapping

| Vacancy requirement | Exercise and boundary |
|---|---|
| Own investigation through resolution; communicate | Evidence-backed ticket, update and closure checks; simulated |
| Enrolment, configuration, authentication, applications, connectivity | Five offline fixtures plus a one-device tenant runbook |
| Intune configuration, compliance, deployment and diagnostics | Separate tenant policy, compliance check and marker app; unrun |
| Interpret logs and recommend solutions | Correlate snapshot/log hints; no automatic root-cause claim |
| Microsoft 365 and Windows support | Scope application versus identity/device faults; tenant sign-in check |
| Projects, pilots, improvements; PowerShell/automation | Isolated pilot, read-only diagnostic commands and repeatable Python report |

## D. Learner gap and claim boundary

This guide develops the difference between recognising a fault and configuring, validating and explaining a complete workflow. The offline scaffold demonstrates synthetic behaviour only. A learner must execute and explain the relevant steps before treating them as personal project evidence. Tenant procedures remain unrun; this package is not evidence of second-line or production administration.

## E. Recurring use

An engineer would use the checklist at onboarding, when a device fails check-in, after an application change and before a pilot. The recurring output is a ticket with symptoms, device/user scope, fresh observations, a hypothesis, next test and an agreed update. Target value is fewer unsupported changes and clearer handovers; time saved and workplace outcomes have not been measured.

## F. Architecture and decisions

Synthetic JSON inventory and inert log notes → schema checks → deterministic scope classification → JSON evidence report → human investigation and user update. Python does not execute log text, connect to Microsoft services or change a device. `ready_in_fixture` means only that supplied fixture fields pass. Stale or unknown fields require evidence.

Optional tenant path: test user → Microsoft Entra identity → one enrolled Windows VM → Intune policy/app assignment → endpoint and portal observations → sanitised evidence. The tenant administrator owns permissions and changes. No AI is needed for deterministic checks. A model's plausible explanation cannot replace fresh logs or policy status; the simpler baseline is deliberate.

## G. Prerequisites, time and cost

Offline: Python 3.11 or newer, a text editor and the supplied `public/` folder. No third-party packages, cloud account or licence are required. Budget 60–90 minutes for setup, tests and explanation; this is a planning estimate.

Tenant path: a separate test tenant with a verified Intune entitlement, one licensed test user, Entra P1/P2 for automatic MDM enrolment, a supported Windows 11 Pro/Enterprise VM or spare lab device, reliable internet and snapshot/restore capability. Windows Home is unsuitable for the join path. On an Apple silicon Mac, do not assume an available VM image supports the same architecture or management features; a compatible spare Windows device is an alternative. Assign only necessary lab roles; use an elevated setup account only for the documented task. Intune Policy and Profile Manager can manage the policy exercise; application/enrolment permissions must also be deliberately granted. Do not use an employer tenant.

Trial eligibility, duration, region, Windows licensing, VM software and current prices must be checked before purchase. This run creates no paid resources. Offline mode costs no cloud fees; it simulates observations and cannot prove enrolment or policy delivery. Budget a further 4–6 hours over two sessions for the tenant path, plus reporting delays; stop rather than purchasing access merely to finish this guide. [Intune licensing](https://learn.microsoft.com/en-us/intune/fundamentals/licensing), checked 30 September 2026.

## H. Granular procedure

### 1. Confirm the isolated starting point — offline, run by assistant

Start: a fresh copy of this solution. Action: open its `public/` folder in a terminal and run `python3 --version`; on Windows use `py -3 --version`. Record the version, operating system and source hashes in a learner note. Expected: Python 3.11+ and `scripts`, `templates`, `tests`, `docs`, `evidence`. Verify: open `CONTRIBUTIONS.md`; it states who authored and tested this scaffold. Recovery: install an approved Python runtime if absent, or use the bundled workspace runtime. Do not claim the supplied evidence as your own independent run.

### 2. Establish a manual baseline

Start: no generated report. Action: read `templates/readiness.json`, list each `LAB-` device and classify the five boolean states by hand. `null` means unknown; false means a supplied failure; a sync older than 24 hours means current state needs evidence. Expected: LAB-01 passes its fixture, LAB-02/03/04 need investigation, LAB-05 needs evidence. Verify: write a reason for each without consulting code. Recovery: if a log hint conflicts with an observation, keep both and name the uncertainty. Manual completion time has not been measured by this run.

### 3. Generate an investigation report

Start: the unmodified fixture. Action: run `python3 scripts/readiness.py --output outputs/readiness.json`. Expected: five devices, the states above and `mutation: none`. Verify: open the JSON; LAB-03 identifies configuration/compliance, LAB-04 identifies application and authentication/connectivity. Evidence codes are invented training labels, not real Microsoft error identifiers. Recovery: an input error exits with code 2; correct the named field or restore the fixture instead of forcing a report.

### 4. Inspect recommendations and write the user update

Start: a valid report. Action: choose LAB-04 and write: “I’m checking whether the problem is with the application, sign-in or connection. I’ll compare the device evidence before making a change and update you after that check.” Expected: a clear next test and an update point, with no invented resolution time. Verify: every technical recommendation links to an evidence code; `cause` stays a hypothesis. Recovery: replace any confident “DNS caused this” statement with the observation and a test that could disprove it.

### 5. Exercise the automated failure cases

Start: unchanged files. Action: run `python3 -m unittest discover -s tests -v`. Expected: ten passing behavioural tests for scope, stale evidence, unknown codes, duplicate IDs, incorrect booleans, inert log instructions, empty input, future timestamps, malformed logs and orphan device references. Verify: compare your output with `evidence/evaluation.json`. Recovery: retain any failing output; inspect the named case and repair the smallest cause. Do not delete a failing test to make the summary green.

### 6. Reproduce one fault manually

Start: the passing fixture. Action: copy it to `templates/learner-fault.json`; change LAB-01's `last_sync` to `2026-09-28T08:00:00Z`. Run `python3 scripts/readiness.py --input templates/learner-fault.json --output outputs/fault.json`. Expected: LAB-01 becomes `needs_evidence`. Verify: no suggested action applies a change or declares the device healthy. Recovery: restore the date and rerun; remove the temporary copy after capturing the lesson. Default `--now` is fixed for reproducibility; supply a deliberate new timestamp for a later scenario.

### 7. Verify tenant identity and permission — optional, unrun

Start: only an authorised disposable test tenant. Action: in Intune, open Tenant administration → Tenant status and check MDM authority/licences; open Roles → My permissions. Record tenant alias, licence expiry and assigned role privately. Expected: entitled test environment and scope limited to the lab. Verify: the signed-in directory is the intended tenant before every mutation. Recovery: if entitlement or scope is unclear, stop this path and continue offline; do not infer permissions from a successful portal sign-in.

### 8. Create a narrow enrolment scope — optional, unrun

Start: one test user with Intune entitlement. Action: create an assigned Entra security group `LAB-Workplace-Users`, add only that user, then Devices → Device onboarding → Enrollment → Windows → Automatic Enrollment. Set MDM user scope to Some and select this group; keep default service URLs and WIP scope None. Expected: only this test user is in the new scope. Verify: capture group membership and setting before saving. Recovery: have the tenant setup owner check licence/role prerequisites if the page is unavailable; never select All to bypass a problem. [Automatic enrolment](https://learn.microsoft.com/en-us/intune/device-enrollment/windows/enable-automatic-mdm).

### 9. Enrol one Windows device — optional, unrun

Start: a VM snapshot with a known local administrator recovery account. Action: Settings → Accounts → Access work or school → Connect → Join this device to Microsoft Entra ID; sign in as the test user, check directory branding and complete the flow. Restart if requested. Expected: Entra-joined identity and an Intune device record. Verify: compare device name and identity in both portals; run `dsregcmd /status` locally and retain only sanitised state values. Recovery: record the actual error/time, confirm scope and licence, and follow [Windows enrolment diagnostics](https://learn.microsoft.com/en-us/troubleshoot/mem/intune/device-enrollment/troubleshoot-device-enrollment-in-intune). Do not repeatedly wipe or re-enrol without a reason. [Windows MDM enrolment](https://learn.microsoft.com/en-us/windows/client-management/mdm-enrollment-of-windows-devices).

### 10. Configure and verify one device policy — optional, unrun

Start: enrolled device added to a separate assigned device group `LAB-Workplace-Devices`. Action: Devices → Manage devices → Configuration → Create → New policy; choose Windows 10 and later and Settings catalog. Name `LAB-DeviceLock`; add Device Lock's Device Password Enabled with the documented enable value 0 and Max Inactivity Time Device Lock 15 minutes. Assign only the lab device group. Expected: a policy and one scoped target. Verify: check per-setting status after device sync and test idle locking; record any Not applicable/Error state instead of guessing. Recovery: compare support/dependency details and restore the VM snapshot if necessary. These training values are not a bank baseline. [Profile creation](https://learn.microsoft.com/en-us/intune/device-configuration/create-device-profile); [DeviceLock CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-devicelock).

### 11. Check compliance separately — optional, unrun

Start: the same enrolled VM. Action: create Windows 10 and later compliance policy `LAB-OS-Compliance` under Devices → Compliance. Use the exact installed OS version from `cmd /c ver` as Minimum OS version; leave other settings unconfigured and assign the lab device group. Expected: compliance evaluation after check-in; configuration success is a separate result. Verify: inspect this policy's setting result and timestamp. Recovery: correct an incorrectly entered version; never disable a tenant access control to make a lab pass. To practise noncompliance, temporarily require a greater numeric build on this isolated policy, record the result, then restore the original minimum. No Conditional Access is added. [Windows compliance settings](https://learn.microsoft.com/en-us/intune/device-security/compliance/ref-windows-settings).

### 12. Package a harmless test app — optional, unrun

Start: empty `C:\Lab\source` and separate output/tool directories on the VM. Action: create `install.cmd` with `mkdir "C:\ProgramData\WorkplaceLab"` followed by `>"C:\ProgramData\WorkplaceLab\version.txt" echo 1.0` and `exit /b 0`. Create `uninstall.cmd` with `del "C:\ProgramData\WorkplaceLab\version.txt"` and `exit /b 0`. Run each locally once, checking the marker contains exactly `1.0` and then disappears, then run the official Content Prep Tool: `IntuneWinAppUtil.exe -c C:\Lab\source -s install.cmd -o C:\Lab\output -q`. Expected: `.intunewin`; no real business app changed. Verify: keep the tool outside source so it is not packaged. Recovery: fix paths/local behaviour before upload. [Content preparation](https://learn.microsoft.com/en-us/intune/app-management/deployment/create-win32-package).

### 13. Deploy, diagnose and recover the marker app — optional, unrun

Start: the tested package. Action: Apps → Windows → Add → Windows app (Win32); upload it. Use `cmd /c install.cmd` and `cmd /c uninstall.cmd`, System install context, supported Windows/architecture requirements and file-exists detection at `C:\ProgramData\WorkplaceLab\version.txt`. Assign Required only to the lab device group. Expected: marker and installation status after processing. Verify: compare local file with device app report and IME logs. Recovery: deliberately change detection filename to `missing.txt`; record failed detection, restore the correct rule and verify again. Do not state an exact error code before observing it. [Win32 app configuration](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-win32); [IME logs](https://learn.microsoft.com/en-us/intune/device-management/tools/management-extension-windows).

### 14. Gather diagnostics and close the pilot — optional, unrun

Start: one known test fault. Action: inspect Event Viewer → Applications and Services Logs → Microsoft → Windows → DeviceManagement-Enterprise-Diagnostics-Provider → Admin; export only relevant lab events. For app faults inspect `C:\ProgramData\Microsoft\IntuneManagementExtension\Logs`. Use Intune device → Collect diagnostics only with authorised access. Expected: observations tied to device/time; logs may contain private identifiers. Verify: reproduce, explain and retest the fault; write “observed → hypothesis → test → result → next action”. Recovery: if no logs arrive, check connectivity/check-in and request support rather than declaring resolution. [Collect diagnostics](https://learn.microsoft.com/en-us/intune/device-management/actions/collect-diagnostics). Test M365 sign-in only if the user has the relevant service licence; distinguish browser access from a complete Outlook/Teams/OneDrive support test.

## I. Break/fix and J. acceptance

Offline acceptance: five expected classifications; stale/unknown evidence cannot become ready; duplicate/malformed inputs reject; log instructions remain inert; ten tests pass. Tenant acceptance is additional: one verified enrolment, a setting delivered to that device, a separately checked compliance state, marker installation/detection recovery, a sanitised diagnostic chain and a clear user update. A portal screenshot alone does not establish the endpoint result. Neither slice proves production reliability or application service experience across all M365 products.

## K. Artefacts and cleanup

Retain source, original synthetic fixtures, learner changes, hashes, test output and the investigation note. Capture tenant screenshots only after execution, redact identifiers and retain originals privately. Do not invent screenshots or a demo recording. `README.md`, `EVALUATION.md`, `DEMO SCRIPT.md` and `docs/architecture.md` provide handover.

Offline: delete only this project's `outputs/`, temporary learner fixture and caches after saving evidence. Tenant: uninstall the marker, remove only `LAB-` assignments/policies/groups created here, restore the previous MDM user scope, then disconnect/remove the lab device and restore its snapshot. Removing policy assignment may not revert every device setting; the snapshot is the recovery boundary. Remove test accounts/temporary roles only after confirming dependencies. Cancel an unused trial through its documented billing flow and verify renewal status; device deletion alone does not cancel billing.

## L. Interview narrative

Use only after your run: “I wanted a repeatable way to investigate workplace device readiness. I separated stale evidence from failure and kept recommendations as hypotheses. I tested the offline checks, then [only if true] enrolled one isolated Windows device, compared policy status with endpoint behaviour and repaired a deliberately wrong detection rule. The useful result was an explainable handover. I have not tested this in a production estate.” Be ready to explain configuration versus compliance, enrolment versus Entra join, and why user impact must be checked before closure.

## M. Conditional future CV wording and N. extension

Use only after the learner completes and can explain the evidenced scope: “Built and tested a synthetic endpoint readiness workbench, checking enrolment, policy, application and stale-evidence conditions with an auditable investigation report.” Add any tenant sentence only after its actual completion; do not call it production administration.

Optional next version: read-only Microsoft Graph inventory with a narrow permission, export consent review and a held-out fault set. Authorisation, pagination, stale data, throttling and redaction must be tested first. Keep any change execution separate from diagnosis. All technical links were checked 30 September 2026; reread current screens and supported values before a future tenant run.
