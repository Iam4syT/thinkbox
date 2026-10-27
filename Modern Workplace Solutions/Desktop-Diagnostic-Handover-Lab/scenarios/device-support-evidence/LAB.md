# Lab 1 — Device support: evidence before closure

Status: offline Python checker implemented and tested on synthetic inputs. All Windows, physical-device and Learner independent-rebuild steps below are unrun. An offline report cannot prove a repair.

## A. Outcome

Create a repeatable device-support ticket whose evidence separates an observed failure, missing information and a task ready for human closure. Intended user: a support engineer handing work to a colleague.

## B. Company context

BCN's advert asks for ticket ownership, notes, customer updates, hardware/software troubleshooting and escalation. Its 21 November 2025 support-services announcement emphasises responsive support; April 2026 Copilot and July 2026 Microsoft partnership announcements signal a broader Microsoft direction. Reliable endpoint support plausibly underpins that direction, but no specific BCN incident or internal system is known. This is a hypothetical client-device scenario, not commissioned work. Research URLs are at the end.

## C. Job mapping

ticket lifecycle and notes; customer communication; reusable knowledge; device/software investigation; onsite scope. This narrow lab does not satisfy advanced virtualisation, firewalls, Intune or SAN/NAS requirements.

## D. Learning gaps

Use existing M365 case handling as the foundation. Actual authorised device practice is a separate learning step. A+ supports theory, not a completed repair. Existing Intune work remains separate from this offline checker.

## E. Recurring use

Use at each device incident and handover. The manual baseline is a five-check ticket with a real original-task retest. The tool can flag omitted checks consistently; no time saving or service improvement has been measured. A rule checklist is adequate. AI would add cost and uncertainty without helping these explicit checks.

## F. Architecture

Synthetic JSON observations → strict Python validation → state and missing-check list → human decision. Five fields: power_ok, peripheral_ok, os_ok, task_ok, user_confirmed. true/false/null mean observed pass/fail/unknown. Data never authorises repair or closes a case. No tenant, network API or customer data is connected.

## G. Prerequisites, limits and cost

Offline: Python 3.10+ and the public folder; standard library only, no account or bill. Windows section: an authorised spare Windows 11 PC or licensed VM for software checks, plus a real spare device for physical checks. Confirm model, ownership, backup and permitted actions before use. A VM cannot show cable/component handling. Host hardware and licences are unknown; use existing/borrowed equipment before spending. New spend assumed £0. Budget 2 hours offline plus two 1–2 hour reviewed device sessions; these are estimates, not measured completion times. Keep device serials and real user details private.

## H. Implementation — follow in order

### 1. Inspect a clean copy

Start: open a terminal in this scenario's public folder, not the parent product. Run `python3 --version` (Windows: `py -3 --version`). Expected: Python 3.10 or later. Open templates/sample.json and read each field. Check that all aliases are fictitious and that null stays unknown. If Python is unavailable, install an approved compatible release or use the manual baseline; do not report a tool run.

### 2. Write the manual answer first

Start: unchanged sample. Without running the checker, write four lines in a private baseline note. DEVICE-01 should need failure review; DEVICE-02 should need missing evidence; DEVICE-03 should be ready only for human closure; DEVICE-04 should retain both failure and unknown fields. Verify against each observed boolean, not the label. If unsure, mark the observation unknown rather than guessing. This note is the baseline; no stopwatch comparison is claimed.

### 3. Run the source and meaningful tests

Run `python3 -m unittest discover -s tests -v`, then `python3 scripts/check.py templates/sample.json outputs/result.json`. Expected: all test methods pass and four results. Open the output; verify DEVICE-03 still has closed=false and DEVICE-04 lists both missing and failed fields. If a test fails, keep the output, inspect the failed condition and repair the code or fixture deliberately before rerunning. Do not edit expected answers merely to make the run green.

### 4. Prove bad evidence cannot overwrite a report

Copy templates/sample.json to outputs/bad.json. Change a true value to the string "true". Keep outputs/result.json from step 3 and record its hash, using `python3 -c "import hashlib; print(hashlib.sha256(open('outputs/result.json','rb').read()).hexdigest())"`. Run `python3 scripts/check.py outputs/bad.json outputs/result.json`. Expected: nonzero exit and the existing report hash unchanged. Restore the boolean and retry with a duplicate id, then an unknown field. Each should reject. Recovery: restore the original fixture; never interpret rejection as a device result.

### 5. Prepare a real device session — unrun

Start: agreed spare PC, a named reviewer if needed, manufacturer instructions for its exact model, backup and no irreplaceable data. Create a private ticket with date, fictitious alias, user symptom, effect and permitted checks. Record whether the fault can be reproduced. Expected: a clear starting task, such as opening a test file with a known-good USB mouse attached. Verify that the device is not workplace equipment and that no destructive action is planned. If access, backup or scope is missing, stop this section and leave physical practice pending.

### 6. Observe power and peripherals — unrun

With the device closed, inspect power indication, external cables and connections. Compare an authorised known-good cable or peripheral one item at a time; retest the same task after each change. Record what you personally did and which comparison changed the result. Expected: an observed pass/fail or an unresolved symptom, not a guessed component diagnosis. Keep liquid, damaged batteries and mains/internal work outside this starter lab; use a qualified supervisor. Recovery: return the original external setup and escalate if no safe comparison explains the fault. Do not open powered equipment.

### 7. Observe Windows software state — unrun

Start: signed in on the authorised spare Windows device. Open ordinary PowerShell and run `Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version`; `Get-PSDrive -Name C | Select-Object Used,Free`; and `Get-NetIPConfiguration`. Expected: OS, storage and adapter observations. Open Device Manager from Start and record any warning without assuming its cause. Verify values against the visible UI. If a command or access fails, keep the error and ask the reviewer; do not change execution policy or install random drivers. Local identifiers stay private.

### 8. Test one reversible software task — unrun

Start: a dummy file and chosen known-good application. Open, edit, save and reopen the file. Record each result. If the original symptom concerns connectivity and outbound testing is authorised, run `nslookup www.microsoft.com` and `Test-NetConnection www.microsoft.com -Port 443`. Expected: a lookup and a TcpTestSucceeded value, each observed separately. A successful TCP test does not prove login or the application works; a failed ping alone does not prove the host is down. Recovery: compare another approved target, preserve errors and escalate instead of changing firewalls. No reinstall, driver change or reimage is included in this first session.

### 9. Record the decision and user check — unrun

Copy the fixture into a private folder outside the public repository. Create a new fictitious alias and set fields only from the actual observations. Leave user_confirmed null until the reviewer/user repeats the original task. Run the checker against this private copy and write a handover: symptom, impact, evidence, actions, result, owner, next update and requested specialist help. Expected: failure/unknown fields stay visible. Verify the original task after any separately authorised repair; no successful checker result is enough to close a ticket. Recovery: reopen the investigation if the task still fails.

### 10. Finish the handover and deployment boundary

Start: completed offline run or actual permitted device session. Save a sanitised before/after note, test output and a short screen recording with no private identifiers. Ask a reviewer to pick an unseen scenario and explain it aloud. Expected: repeatable reasoning and an explicit scope statement. This package is deployed only as local files; it installs no agent and changes no service. If the reviewer finds an unsupported claim, correct the note and preserve the earlier result as history.

## I. Break and fix

Offline: make power_ok false and task_ok null; verify failure plus missing evidence, then restore both. Make all checks true but user_confirmed null; verify collect_evidence. Put a command-like string in a field; expect rejection, never execution. Real device, unrun: disconnect only a permitted external mouse, reproduce the symptom, reconnect it and retest; do not simulate damage or power faults. Record failure, own action and repeat verification.

## J. Acceptance and cleanup

Accept the offline slice when four manual outcomes agree, invalid types/duplicates reject, prior output survives bad input and closed is always false. Real-device acceptance separately requires the original task, observed checks, reviewed evidence and a repeat run; not achieved here. Keep sanitised evidence, then remove generated outputs/bad.json and local scratch reports only. Do not delete original evidence or user files. Shut down a lab VM when done. No credentials or real diagnostic logs belong in public evidence.

## K. Portfolio evidence

Keep README, LAB, EVALUATION, DEMO SCRIPT, CONTRIBUTIONS, CHANGELOG, scripts/check.py, tests, synthetic fixtures and compact test evidence together. Add genuine device screenshots and a two-minute demo only after performing the real session and removing private identifiers. Link source revision and environment to each actual result. Offline tests support code behaviour, not hardware competence.

## L. Interview story

Problem: incomplete device handovers. Constraint: no live customer access and no claim of a repair. Design: explicit observations with unknowns preserved. Build: strict checker and synthetic fixtures. Failure: a string pretending to be a boolean is rejected without overwriting the previous report. Verification: compare manual outcomes and tests. Possible value: more consistent handovers if adopted and checked in real use. Improvement: supervised physical practice and an unseen fault. The learner must rebuild/explain this before presenting it as personal independent capability.

## M. Conditional CV wording — use only after evidenced completion

"Built and independently explained a small device-support evidence checker, tested invalid-input and unknown-evidence cases, and recorded reviewed checks on an authorised spare Windows PC." Remove the real-PC clause if only the offline section is completed. No production or professional repair claim is justified by this lab.

## N. Next version and sources

Optional: add a reviewed PowerShell read-only collector after manually validating each field. Do not collect serial numbers, personal paths or credentials by default. Compare collected values with manual observations before relying on them. No AI integration is needed.

Sources checked 27 October 2026: BCN advert https://bcngroup.recruitee.com/o/2nd-line-support-consultant-5 ; support direction https://bcn.co.uk/resources/bcn-achieves-microsoft-solution-partner-designation-for-support-services/ ; Copilot https://bcn.co.uk/resources/bcn-achieves-microsoft-copilot-specialisation/ ; partnership https://bcn.co.uk/resources/bcn-achieves-microsoft-managed-partner-status/ ; DNS https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup ; TCP https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?view=windowsserver2025-ps . Use exact-model manufacturer instructions before physical work; none has been selected yet.
