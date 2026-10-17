# Workplace identity change planner

State: Codex-assisted offline implementation; local checks recorded separately; native integration and Bunamin reproduction unrun.

## A Outcome
Produce a reviewable synthetic identity-change plan, apply it only to a local copy after approval, and show a safe repeat run.

## B Company context
Public workplace-engineering responsibilities include Okta-based joiner/mover/leaver automation from a reliable people-data source. That is the researched need; this independent teaching scenario is an inference about a useful small exercise. It does not reproduce an employer platform or assert a commission. Scenario authored 17 October 2026.

## C Requirement mapping
Exercises Python data validation, repeatable automation, approvals and access-state reasoning. Relates to identity automation, operational workflows, follow-through and risk judgement.

## D Gap mapping
Strengthens project-level software/test reasoning. It does not establish shared-code peer review, live Graph/Okta integration, enterprise authority or independent candidate competence. Bunamin must run it, change it and explain its failures before using personal completed-work wording.

## E Repeated use and baseline
Intended user: an operations/identity administrator handling each joiner, move or exit. Baseline: manual source-to-account comparison. Target: consistent reviewable changes, no accidental deletion when a source row is missing, and no new changes on an identical repeat run. Frequency is event-driven, often several times weekly; it is valuable despite not being daily for every person.

## F Architecture and stack
Python 3.11+ and JSON fixtures; scripts/main.py is the entry point; unittest is the test runner. Read docs/architecture.md. Input is synthetic and not trusted until validated. Files in evidence/ are local outputs. No live provider or model is called. A source-present left state can disable a simulated account; missing people do not. Group sets are explicitly allowed. Approval protects the local tutorial path only; a real service needs authenticated approvers, versioned plan hashes and separate execution rights.

## G Prerequisites and cost
Use a personal computer, terminal, Python 3.11+ and a text editor. No licence, tenant, API key or paid model is needed for the local track; marginal service cost £0, excluding your computer. Estimate 2–4 hours to understand, reproduce and modify; not a measured duration. Optional native track may require eligible test tenants/licences and an authorised reviewer; cost/access must be agreed before provisioning. Do not use live employer accounts.

## H1 Open the folder
Starting state: fresh project copy.
Action: Start with the downloaded project files. In a terminal, change into the project root containing scripts/, tests/ and templates/. Run `python3 --version` and `pwd`.
Expected: Python 3.11 or later and the intended project path appear.
Verify and recover: Check that `ls templates` lists the supplied JSON files. If Python is absent, install from python.org or use your approved managed runtime; do not paste secrets into a terminal.

## H2 Create an isolated environment
Starting state: previous step complete.
Action: From the project root run `python3 -m venv .venv`. On macOS/Linux run `source .venv/bin/activate`; on Windows PowerShell run `.venv\Scripts\Activate.ps1`. Run `python --version`.
Expected: The environment is active; no packages need downloading.
Verify and recover: If Windows policy blocks activation, invoke `.venv\Scripts\python.exe` directly. If venv creation fails, fix the Python installation before continuing.

## H3 Read the inputs
Starting state: previous step complete.
Action: Open each file in templates/ in your editor. Compare the synthetic IDs with the code in scripts/main.py. Keep an unchanged copy outside this project for the break/fix exercises.
Expected: You can identify allowed and denied records before running anything.
Verify and recover: Run `python -m json.tool templates/people.json` to validate JSON. Repair invalid commas/quotes using the supplied original; never replace fixtures with real people.

## H4 Preview without approval
Starting state: previous step complete.
Action: Run `python scripts/main.py`.
Expected: evidence/plan.json contains create joiner, reconcile mover and disable leaver. No simulated-accounts.json is created on a clean run.
Verify and recover: Read the plan and confirm external is absent. If a prior output exists, move it aside first so stale output is not mistaken for a new action.

## H5 Approve only the local simulation
Starting state: previous step complete.
Action: After reading the three changes run `python scripts/main.py --approve-local`.
Expected: evidence/simulated-accounts.json contains joiner enabled in research, mover only in operations, leaver disabled with no groups, external unchanged.
Verify and recover: Compare with the input. The templates/accounts.json hash should be unchanged. If unexpected changes occur, stop; restore inputs and run tests.

## H6 Verify a repeat run
Starting state: previous step complete.
Action: Read tests/test_main.py test_idempotent. Run `python -m unittest discover -s tests -v`. The test feeds the updated copy back to plan.
Expected: The repeat plan has zero changes and the test passes.
Verify and recover: Do not just rerun the CLI against the original input and call it idempotent: that deliberately produces the original plan again. Inspect the test and explain why this matters.

## H7 Run the full behavioural checks
Starting state: previous step complete.
Action: Run `python -m unittest discover -s tests -v` from the project root.
Expected: All 10 tests pass; output ends OK.
Verify and recover: Read each named case. On failure, keep the output, inspect the expected/actual result and fix the cause. Do not delete a failing security check to make the suite pass.

## H8 Capture a reviewed change
Starting state: previous step complete.
Action: Create a Git branch locally with `git switch -c lab-review` if this is your own clone. Make one small documentation/test improvement, run checks, inspect `git diff`, and ask a reviewer to explain any concern before merging.
Expected: A small understandable change and its test output are available.
Verify and recover: No peer review is claimed merely from creating a branch. If no reviewer is available, keep review status pending and record your own explanation separately.

## H9 Demonstrate and clean up
Starting state: previous step complete.
Action: Follow DEMO SCRIPT.md, record your own explanation and compare with EVALUATION.md. Delete only generated evidence/audit.json or evidence/plan.json and evidence/simulated-accounts.json created by your run. Deactivate the environment; remove .venv only if disposable.
Expected: Original fixtures and source remain; generated outputs can be recreated.
Verify and recover: Check `git status --short` before deletion. Restore a deleted tracked sample from Git if needed; never use broad recursive deletion against a parent folder.

## I Break and fix
Duplicate a person ID: expect ValueError and no newly generated plan. Change an active team to admin: expect rejection. Remove a source person: existing unmatched account must remain unchanged, not be treated as a leaver. Restore inputs and rerun all checks. A runtime error must not be mistaken for a successful clean plan.

## J Acceptance checks
All supplied tests pass; inputs remain unchanged; normal and denied paths match the steps; audit/output contains only synthetic data; own explanation names at least one limitation. Joiner/mover/leaver decisions match expected state, approval is required, missing rows cause no destructive action, and repeat plan is empty. Local tests are useful evidence about these cases only, not proof of comprehensive security.

## K Evidence and handover
Retain source revision, runtime version, commands, stdout, test result, one changed test and personal contribution notes. Capture a screen showing synthetic output only. README, this lab, architecture, evaluation and demo script are included. Video is optional and unrecorded. Review licences before adapting third-party code; original Python example uses the repository licence on publication.

## L Interview explanation
Explain the recurring user need, trust boundaries, smallest design, a failed case, the fix and what the checks prove. Then state what is untested. Ask another person to challenge the approval/identity assumptions. Do not say you operated employer systems or that the simulation proves independent production delivery.

## M Conditional personal wording
Use only after your own completed run, modification and recorded explanation: “Built and tested a local synthetic identity-change planner with input validation, explicit local approval and repeat-run checks.” Add Codex assistance accurately. Do not use as commercial/Okta/M365 production experience; no LinkedIn post is authorised here.

## N Optional native extension
UNRUN. Use an authorised Okta sandbox and a synthetic HR source. Research the current Users/Groups lifecycle APIs, licence availability and authenticated plan approvals. Build a separate adapter with dry-run default, retries/rate-limit handling, plan version checks and reviewed rollback. Test create/move/disable and permission failure on disposable accounts before any live use. Airtable approval UI is an optional separate integration, not implemented. AI adds little to deterministic entitlement decisions and is deliberately omitted.

## References
Checked 17 October 2026. Microsoft Graph permissions: https://learn.microsoft.com/en-us/graph/permissions-overview . Okta Users reference: https://developer.okta.com/docs/reference/api/users/ (redirected body not available to web reader). Read current official API documentation before a native adapter; no live API semantics are claimed tested here.
