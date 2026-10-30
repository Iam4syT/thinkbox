# Incident lifecycle practice
## Purpose and sourced context
This independent lab helps a service desk practise a recurring support responsibility. Public first-line role descriptions ask for prioritisation, escalation, useful records and safe guidance. The private role map records the specific vacancy source; this public exercise does not claim employer commission or knowledge of its internal tools.
The outcome is a suggested priority and next action for synthetic incidents, including explicit follow-up before closure.
## Requirements and capability gaps
Practise incident/request records, impact and urgency, scope/time escalation and user follow-up. Existing generic ITSM experience helps explain the task; exact employer product experience is separate.
This strengthens project practice after personal completion. It does not demonstrate physical hardware maintenance, named ticket-system production experience or authority to change company policy.
## Recurring use and value test
An analyst can return at the start of a shift and when ticket status changes. The proposed value is catching missed escalations and premature closure.
Baseline is manual review. No time saving or workplace error reduction has been measured. A future user test should compare the same held-out records and count missed unsafe decisions before claiming benefit.
## Architecture and stack
Analyst → synthetic JSON tickets → Python rules → priority/action report → human decision.
Python 3.11/3.12 standard library, local filesystem and unittest only. No service API, cloud, model, tenant, personal data, secrets or automated remediation. No operating system or cloud product is assumed to be the employer stack. AI is omitted because explicit structured rules suffice; test an optional model against this baseline only if messy text creates a real need.
## Prerequisites permissions costs and time
Ordinary local user account; terminal; text editor; project copy and Python 3.11/3.12. No admin rights for execution, paid licences or tenant access. Software installation may need your device owner's approval. Estimated practice time 60–90 minutes, not measured. Local run cost has no added service charge; your device and connectivity costs remain yours. On managed devices use approved installation routes.
## Input fields and decisions
Each ticket needs unique id; impact single/team/organisation; urgency normal/high; nonnegative age_hours up to 8760; status open/resolved; booleans outside_scope, user_confirmed and followup_done. Organisation plus high urgency gives P1; otherwise high urgency or team impact gives P2; other cases P3. Open work outside scope or aged at least 4 hours escalates. Resolved work closes only with both confirmation fields true. These are teaching rules, not a complete ITIL policy.
## End to end steps
### Step 1 Prepare a safe working copy
Action and starting state: Start with the downloaded project folder. Open a terminal in that folder and run `pwd` on macOS/Linux, or `Get-Location` in PowerShell. Copy templates/sample.json to templates/practice.json using the file manager.
Expected result verification and recovery: The practice file exists beside the original. Compare both files visually; they should match. If the copy is elsewhere, move only your copy back. Keep the original as the recovery point.
### Step 2 Check the runtime
Action and starting state: Start in the project folder. Run `python3 --version`; on Windows use `py --version` and replace python3 with py in later commands.
Expected result verification and recovery: Python 3.11 or 3.12 is expected. If missing, obtain Python from python.org through the normal approved installation process. Do not install service credentials or request tenant permissions. No virtual environment or pip packages are required.
### Step 3 Understand the sample
Action and starting state: Open templates/sample.json in a text editor. Read the four records and the fields documented below. Do not add real employee, customer or account information.
Expected result verification and recovery: All IDs are synthetic and unique. Check each bracket and comma before saving. If malformed, restore the sample from the untouched copy; the program reports Input error rather than silently inventing a value.
### Step 4 Run the reference case
Action and starting state: From the project root run `python3 scripts/workbench.py templates/sample.json`. Compare the printed JSON with evidence/demo-output.json.
Expected result verification and recovery: Expected INC001 P1/escalate; INC002 P3/investigate; INC003 P1/follow_up; INC004 P1/close. Check every ID, not only exit success. If the script is missing, return to the folder containing scripts, templates and tests.
### Step 5 Run the practice copy
Action and starting state: Run `python3 scripts/workbench.py templates/practice.json`. Save output through the terminal if useful, keeping it in a private learning folder.
Expected result verification and recovery: The unchanged copy produces the same four decisions. Compare record order and values with the reference output. If different, restore practice.json and repeat. This is local execution only; nothing changes a real ticket or article.
### Step 6 Introduce a meaningful fault
Action and starting state: In practice.json change INC002 age_hours from 1 to 4, leaving status open and outside_scope false. Run the practice command again.
Expected result verification and recovery: INC002 becomes escalate at the four-hour boundary; the priority remains P3. Compare before/after output. If it still says investigate, verify that you edited practice.json and ran that filename. Four hours is an illustrative lab threshold, never an employer SLA.
### Step 7 Recover and confirm
Action and starting state: Restore INC002 age_hours to 1. Run again. Then set INC003 user_confirmed and followup_done to true and run once more.
Expected result verification and recovery: INC002 returns to investigate; INC003 changes from follow_up to close only after both checks are true. If not, check that JSON booleans are true without quotation marks. A human must actually obtain confirmation in real support.
### Step 8 Test invalid input
Action and starting state: Copy INC001 to create a duplicate ID in practice.json, then run. Next restore and try age_hours:-1.
Expected result verification and recovery: Expect an Input error and process exit 2, with no partial report. Restore practice.json from the original after each case. Check the shell exit code with `echo $?` on macOS/Linux or `$LASTEXITCODE` in PowerShell. A successful exit here would fail acceptance; do not use an incomplete report.
### Step 9 Run the behavioural checks
Action and starting state: From the same project root run `python3 -B -m unittest discover -s tests -v`. Read the named checks and final summary.
Expected result verification and recovery: Expect 10 tests and OK, exit 0. These test normal results, boundaries, unsafe completion and invalid inputs. If imports fail, check the scripts/tests folders. If a rule test fails, preserve the failure, restore a fresh copy and compare before changing code.
### Step 10 Explain and clean up
Action and starting state: Write a short private note: one expected result, the deliberate failure, recovery, and what remains a human decision. Remove only your practice.json and any temporary report you created, using the file manager. Keep original source and evaluation evidence.
Expected result verification and recovery: The sample still runs and original evidence remains intact. No cloud cleanup is needed because no cloud resources were created. If you remove an original accidentally, restore it from the release copy. Do not mark your work completed until you can reproduce the results and explain the limits.
## Break fix and acceptance checks
Pass only when the four original demonstration decisions match the saved output, the deliberate unsafe case is detected, its recovery restores the expected result, duplicate/invalid records exit 2, and all 10 behavioural tests pass. Keep your own command output and notes. A missing result is Pending. Do not alter expected outputs merely to make a failing program appear correct.
## Actual evaluation and ownership
Development-assistant run 29 October 2026: 10 behaviour tests passed and 4 synthetic demo records produced expected output on Python 3.12.14/macOS arm64. Details in EVALUATION.md and evidence/. Bunamin independent execution and explanation remain pending. No real users, service tool or tenant were tested. Build readiness, personal capability and deployment readiness are separate.
## Operational handover and portfolio evidence
Preserve README, this lab, scripts/workbench.py, sample JSON, tests, architecture, evaluation, demo script and change log. Capture permitted screenshots of your synthetic output if useful. Record your own edits, failures, recovery and checks with dates. Review policies with a service owner before any integration; use approved authentication, retention, auditing, access controls and change review. Never upload real tickets to this demo or a model.
## Interview story after your own run
Explain the repeated task, why simple rules were chosen, the failure you introduced, how the output exposed it, what you restored and how you verified recovery. Say it is a synthetic local exercise and name the untested service/hardware boundaries. Do not present the development-assistant run as your own.
## Conditional CV and LinkedIn wording
Use only after personal completion and evidence review: Built and tested a local Python incident-workflow practice tool using synthetic data, including normal, failure and invalid-input cases. Add your actual contribution and observed check. This is project evidence, not commercial operation or an endorsed employer tool.
## Optional next version
Add a configurable approved-policy file and audit log, then evaluate held-out tickets with a service owner. A real ticket API integration would require separate access and authorisation.
## Technical sources
Checked 29 October 2026: Python 3.12 JSON documentation https://docs.python.org/3.12/library/json.html ; unittest documentation https://docs.python.org/3.12/library/unittest.html . Used for parsing, errors and behavioural checks. Exact runtime tested 3.12.14; documentation branch may show a later patch.
