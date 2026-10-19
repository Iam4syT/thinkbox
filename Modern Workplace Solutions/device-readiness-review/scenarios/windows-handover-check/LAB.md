# Endpoint handover check

## A. Outcome and status
A local, read-only checker makes a support decision and its missing evidence visible. Implemented and locally evaluated using synthetic records; Microsoft services and physical devices are not connected. The lab guide is complete. the learner has not yet been observed rebuilding it.

## B. Sourced need
First-line support work involves incident handling, access questions, device setup and patch checks. This is an independent synthetic learning scenario. No proprietary environment or commissioned work is reproduced.

## C. Requirements exercised
Device setup assistance, patch support, access approval and documented user checks. This exercises a local decision process, not execution of an account reset or update rollout. The employer's actual ITSM vendor and device policies are unknown.

## D. Evidence gap
The practice target is evidence-led device handover. This local checklist does not prove physical-device experience. The preparation environment ran the recorded checks; learner rebuild and live operational experience require separate evidence.

## E. Repeat-use value
Every device handover/change needs repeatable evidence. Missing approval or unknown encryption must stop a checklist from being called complete. Device state is synthetic input, not telemetry. Intended value is fewer missing checks and clearer handover; no workplace saving measured.

## F. Architecture and baseline
Operator → synthetic CSV → Python schema validation → explicit rules → JSON report → human review. No network calls, secrets or administrative permissions. Read-only inputs; output goes to the terminal unless redirected. Generated report is an advisory artefact. Rules are the baseline and the selected design. AI could explain a report but adds cost, privacy and correctness risks to these small explicit checks; it must not authorise access, patching or case decisions.

## G. Prerequisites, scope and costs
Use a personal isolated folder, a text editor, terminal and Python 3.11 or later. Existing local Python means no API/subscription cost; hardware/internet costs excluded. The tested bundled interpreter is recorded in private QA. No paid cloud resources, administrator account, Microsoft licence or real user data needed. Set aside60–90 minutes for first local practice (estimate, not measured time). Optional Windows/device practice later needs a spare non-production device/VM, valid Windows licence, approval, recovery media and a knowledgeable reviewer; it is unrun.

## H. Step-by-step lab
### 1. Open the project
Start in an empty personal practice area. Obtain the published project folder or its prepared local public copy. Open a terminal at that folder. On Windows use the terminal's Open in Terminal option; on macOS open Terminal and type cd followed by the folder path in quotes. Run `python3 --version` (Windows: `py -3 --version`). Expect Python 3.11 or later. If command missing, use a trusted Python installation; do not install random scripts. Check that README.md, scripts/check.py and templates/sample.csv exist before continuing.

### 2. Understand the input
Open templates/sample.csv in a plain-text editor. The first line contains column names and the next four lines contain invented records. Do not insert real names, emails, credentials, incident text or case data. Compare the columns with FIELDS in scripts/check.py. Expect exact agreement. If Excel changes a delimiter or header, return to the original CSV rather than guessing. Save an untouched copy for recovery.

### 3. Run the normal task
From the project folder run `python3 -B scripts/check.py templates/sample.csv` (Windows: replace python3 with py -3). Expect a JSON list with four records and a human-review action. Check every row against the criteria below. If the file is not found, check the current folder and exact relative filename. If input is rejected, restore the supplied sample and rerun. The command reads the file; it does not connect to or change a tenant.

### 4. Save and inspect the report
Create an output directory with `mkdir output`. Run `python3 -B scripts/check.py templates/sample.csv > output/report.json`. Open report.json. Expect the same four results. Compare with evidence/example-output.json and record any difference. If the output is empty, inspect the error printed in the terminal and rerun without redirection. Never treat an empty file as a passed check.

### 5. Read the decision rules
Open scripts/check.py. Find evaluate, FIELDS and the decision expression. Trace the first sample record by hand. Explain which values cause its result and what the program cannot observe. For triage, priority thresholds are teaching values, not the employer's agreed SLA. For endpoint review, yes is a synthetic assertion; the script cannot verify encryption or patch state. Record that distinction in a practice note before changing a rule.

### 6. Run behavioural checks
Run `python3 -B -m unittest discover -s tests -v`. Expect five tests and OK. They check normal outputs, duplicate identifiers, schema mismatch, invalid input and boundary/unknown behaviour. Check that the failure-path test actually rejects data rather than suppressing errors. If a test fails after an edit, save the failure, compare your change with the reference and restore the original file. Do not remove the failing test merely to pass.

### 7. Break, diagnose and fix
Copy sample.csv to a new practice file with your editor's Save As. In a copy change L001 encrypted to unknown: status must become REVIEW. Restore yes only to represent synthetic evidence: complete. Use TRUE instead of yes: reject input with exit 2. Duplicate an asset: reject. Unknown data must never silently pass. Run the checker after each single change. Capture the rejected input, error and corrected output. Restore the original before the next fault. Never edit the evidence/example-output.json file to make a failed run appear correct.

### 8. Practise user communication and escalation
Write a two-sentence update: what is known, the temporary next step and who reviews it. Avoid promising a fix time that the evidence does not support. Add a handover note listing identifier, checks performed, result, missing evidence and escalation owner. For the local exercise use fictional roles only. Have another person or your future self read it and explain the next action; this is a planned usability check until done.

### 9. Optional Windows/M365 practice — unrun
After permission for a spare device/VM, record a baseline and recovery plan. Inspect Windows Settings → Windows Update and record status without launching an unapproved rollout. Inspect the device's encryption status without changing it. With a separate test identity, perform an approved M365 sign-in and application check; never copy real tokens. A reviewer must confirm which observations may support a checklist field. For AD/access changes, obtain delegated test access and approval before any mutation. Capture actual observed values, errors and rollback. This extension needs its own evidence and cannot be inferred from a passing local CSV.

### 10. Hand over and clean up
Record runtime, command, date, source hash, observed results and unrun dependencies in a practice log. Review the output before sharing it. Remove only the output directory and your copied practice CSV using the file manager; leave the source and immutable evidence intact. No cloud resources were created. If you later created a test identity/VM, use its separately approved cleanup plan and verify deletion or deallocation. Do not delete a shared account or work device.

## I. Break/fix reference
Invalid schema, duplicate identifier and unrecognised state stop processing with exit 2; no successful report should be printed. Restore the exact input schema and rerun before handover. A boundary/unknown case must visibly change the advisory status. Keep both failed and fixed observations.

## J. Acceptance criteria
- L001 must be CHECKLIST_COMPLETE; this label is not approval to deploy.
- L002 must be REVIEW with approved missing.
- L003 must be REVIEW with encrypted and patched missing.
- L004 must be REVIEW with m365_test and owner_recorded missing.
- Five behavioural tests pass; malformed CLI input exits2 without success JSON.
- No network call, credential or tenant change; synthetic-only artefacts.
- Human reviews and can explain the output; live Windows/Microsoft checks remain unrun.

## K. Artefacts
Source scripts/check.py; templates/sample.csv and invalid.csv; tests/test_behaviour.py; evidence/example-output.json and test-results.txt; EVALUATION.md; docs/architecture.md; DEMO SCRIPT.md; CHANGELOG.md. A video and actual user-run screenshots are optional future evidence and have not been produced. Keep the private application and claim ledger out of public exports.

## L. Interview story
Problem: support work needs repeatable checks. Constraint: no employer systems or private data. Design: explicit rules and human review. Build: local CSV-to-JSON prototype. Failure: malformed/unknown state cannot silently pass. Verification: four synthetic records plus behavioural and CLI rejection tests. Value: clearer handover is intended, not measured. Improve: supervised Windows practice and evidence-linked inputs. the learner should tell this as a learning plan until he personally rebuilds and can explain it.

## M. Conditional wording
Use only after the learner completes and evidences his own work: “Rebuilt and tested a synthetic support checker, documented normal and rejected inputs, and explained where human review and live-system evidence remain necessary.” Do not claim production integration, hardware repair, automated patching, staff time saved or employer deployment. Any public social post remains a draft until separately authorised.

## N. Extension
Add a read-only approved export from a test environment, record field provenance and review what is missing before extending rules. Add a small held-out fixture set authored separately. An optional AI explanation must cite rule outputs and abstain on unknowns; compare it against the deterministic baseline before adoption.

Technical references: Python CSV documentation https://docs.python.org/3/library/csv.html ; Microsoft Windows Update troubleshooting https://learn.microsoft.com/en-us/windows/deployment/update/windows-update-troubleshooting . Local checker needs no vendor API. Reviewed19 October 2026; Windows extension unrun.
