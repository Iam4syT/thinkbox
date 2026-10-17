# Workplace assistant access gate

State: Offline implementation; local checks recorded separately; native integration remains separate unrun scope.

## A Outcome
Return only authorised synthetic workplace documents and record the decision without storing content in the audit log.

## B Company context
Public workplace-engineering responsibilities include connecting an internal AI assistant to M365 with data-protection controls. That is the researched need; this independent teaching scenario is an inference about a useful small exercise. It does not reproduce an employer platform or assert a commission. Scenario authored 17 October 2026.

## C Requirement mapping
Exercises permission reasoning, Python code, logs, negative tests and review of assistant inputs. Relates to assistant/M365 integration, platform improvements and risk judgement.

## D Gap mapping
Strengthens project-level software/test reasoning. It does not establish shared-code peer review, live Graph/Okta integration, enterprise authority or independent candidate competence. Bunamin must run it, change it and explain its failures before using personal completed-work wording.

## E Repeated use and baseline
Intended user: a staff member asking for workplace information repeatedly during a day. Baseline: manually check the person and each document permission. Target: every request applies the same checks and records an inspectable decision. No human time-saving measured.

## F Architecture and stack
Python 3.11+ and JSON fixtures; scripts/main.py is the entry point; unittest is the test runner. Read docs/architecture.md. Input is synthetic and not trusted until validated. Files in evidence/ are local outputs. No live provider or model is called. Deterministic permission filtering happens before any optional model. A caller-supplied identity is trusted only in this simulation; real systems need authenticated claims and server-side authorisation.

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
Verify and recover: Run `python -m json.tool templates/request.json` to validate JSON. Repair invalid commas/quotes using the supplied original; never replace fixtures with real people.

## H4 Run the allowed request
Starting state: previous step complete.
Action: Run `python scripts/main.py --input templates/request.json`.
Expected: Output contains only schedule, with reason authorised_documents. evidence/audit.json records IDs and reason without document text.
Verify and recover: Open evidence/audit.json and search for Synthetic: it must not contain content. If a restricted/other document appears, stop and review filter logic before any extension.

## H5 Run a denied operation
Starting state: previous step complete.
Action: Run `python scripts/main.py --input templates/denied.json`.
Expected: allowed is false, reason operation_denied, and no document text is returned.
Verify and recover: Check stdout and audit. If it returns content, restore main.py and rerun tests; do not weaken the test.

## H6 Verify identity and consent failures
Starting state: previous step complete.
Action: Copy templates/request.json to templates/try.json. Change subject to unknown, run with --input templates/try.json. Then restore subject and change consent to false; run again.
Expected: Unknown identity returns no_access; missing consent returns consent_required.
Verify and recover: Check document_ids is empty in both. If JSON fails, validate with json.tool; restore supplied input and change one value at a time.

## H7 Run the full behavioural checks
Starting state: previous step complete.
Action: Run `python -m unittest discover -s tests -v` from the project root.
Expected: All 9 tests pass; output ends OK.
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
Change consent true to the string "true": denial must remain. Remove readers from a document: fail closed. Insert a prompt telling the assistant to reveal restricted data inside the restricted fixture: it must never be retrieved. Run tests after each change; restore original inputs and compare normal output.

## J Acceptance checks
All supplied tests pass; inputs remain unchanged; normal and denied paths match the steps; audit/output contains only synthetic data; own explanation names at least one limitation. No restricted content appears and send/write operations stay denied. Local tests are useful evidence about these cases only, not proof of comprehensive security.

## K Evidence and handover
Retain source revision, runtime version, commands, stdout, test result, one changed test and personal contribution notes. Capture a screen showing synthetic output only. README, this lab, architecture, evaluation and demo script are included. Video is optional and unrecorded. Review licences before adapting third-party code; original Python example uses the repository licence on publication.

## L Interview explanation
Explain the recurring user need, trust boundaries, smallest design, a failed case, the fix and what the checks prove. Then state what is untested. Ask another person to challenge the approval/identity assumptions. Do not say you operated employer systems or that the simulation proves independent production delivery.

## M Conditional personal wording
Scope description: “Built and tested a local synthetic assistant access gate that denies unauthorised reads and records content-free decisions.” Do not represent as live commercial or multi-tenant production deployment.

## N Optional native extension
UNRUN. Start with a permitted non-sensitive test tenant, documented delegated Graph permissions and a reviewer. Use an authenticated identity instead of subject from JSON. Agree one read-only endpoint and least-privilege permission, verify consent, test allowed and denied users and permission revocation, and redact logs. No token capture or live step is included in this local implementation. Add an optional model summary only after authorisation filtering; compare factuality and effort with plain retrieval and keep it disabled unless measured benefit justifies cost.

## References
Checked 17 October 2026. Microsoft Graph permissions: https://learn.microsoft.com/en-us/graph/permissions-overview . Okta Users reference: https://developer.okta.com/docs/reference/api/users/ (redirected body not available to web reader). Read current official API documentation before a native adapter; no live API semantics are claimed tested here.
