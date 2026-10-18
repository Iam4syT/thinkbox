# Lab 2: privileged access evidence ledger
Status: local synthetic tool built and evaluated on 18 October 2026. It does not implement or test live Microsoft Entra PIM.

## A. Outcome
Help a role reviewer explain why a temporary-access request's supplied evidence passes, is denied, has expired or needs review. A local pass never grants access.

## B. Employer problem and research basis
The DWP advert requires privileged governance, RBAC, just-in-time access and technical influence. Microsoft describes PIM eligible and time-bound assignments, activation and audit history. A small evidence ledger is a plausible recurring review aid; no DWP internal workflow or deployment is asserted.
Reference: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-getting-started (checked 18 October 2026). PIM requires Entra ID P2 or ID Governance licensing. This offline lab needs neither.

## C. Job mapping
R5: understand eligibility, activation evidence and time boundaries. R6: explain least privilege, separate requester/approver and evidence-based escalation. It does not satisfy proven production PIM/CyberArk implementation, live RBAC enforcement or Zero Trust architecture leadership.

## D. Candidate gap
Extends reported certification/personal-tenant PIM practice into an inspectable test. Prior Global Administrator practice stays a user report. This safer example uses the narrower User Administrator role; it is not a claim that the candidate implemented this policy for an employer.

## E. Repeat-use test, baseline and target
A reviewer could check each activation request against an approved policy and evidence source. Baseline: manually compare eligibility, approval, MFA and times. Target: pass the normal synthetic record, reject missing controls and flag exact expiry. No timed comparison or workplace savings measured. Deterministic rules fit this task better than a probabilistic AI decision.

## F. Architecture and fields
Input contains a fixed now timestamp and a requests list. Each request has a unique id, role, requester, approver, eligible, approved, mfa, start and end. Booleans describe supplied evidence, not observations of Microsoft enforcement. All timestamps need a timezone. The narrow demonstration permits only User Administrator, a separate approver, true controls and at most one hour. These are local example rules, not universal Microsoft defaults. Global Administrator yields ROLE_REVIEW. Start is inclusive; end is exclusive. No tenant, Graph API, token cache or actual privilege state exists in this model.

## G. Prerequisites, cost and working folder
Use a computer with Python 3.10 or later and a text editor. Open a terminal and run `python3 --version`. If the command is unavailable, install Python from python.org or use an already approved Python runtime. These instructions use a local folder, not Azure Cloud Shell. No tenant, licence, API key or package installation is needed for the tested route. No paid resource is created. Budget one to two hours for learning and explanation; this is a planning allowance, not measured build time.
Download or clone the Thinkbox repository, then open this project's folder. Check that scripts/check.py and templates/sample.json exist before running a command. On systems where Python is named python, substitute python for python3 consistently. Keep the supplied fixtures unchanged; save experiments as templates/experiment.json.

## H. Build, operate and hand over the local route
1. Open README.md and identify the user task, scope and limits. Open docs/architecture.md; trace input → validation → rules → report → human review. There is no tenant-write component.
2. Open templates/sample.json in the editor. Read each field against the explanation below. Keep JSON booleans as true/false, without quotes. Never paste real customer identities or credentials into this public project.
3. Run `python3 scripts/check.py templates/sample.json`. Expect the success status described below and exit code 0. This means the supplied evidence passes the local rules, not that any live user can sign in.
4. Run `python3 scripts/check.py templates/failure.json`. Expect REVIEW and exit code 1. This is the intended safety path, not a program crash. Read the finding before taking any separate administrative action.
5. Run `python3 -m unittest discover -s scripts -p "test_*.py" -v`. Expect the test count recorded in EVALUATION.md and a final OK. If an import fails, return to this project's root folder and repeat the command exactly.
6. To capture a new report, create a local outputs folder, then run `python3 scripts/check.py templates/experiment.json > outputs/report.json`. Open that JSON file and record the input revision, time and operator in your private ticket. The outputs folder is ignored by Git.
7. Give the reviewer the report, source of the input, unresolved questions and proposed next action. A finding does not approve a change. Obtain separate authorisation through the normal change process. This lab performs no tenant changes.
8. After an independently approved correction, refresh the input and rerun the checker. Retain before/after evidence privately. Do not edit the report to turn REVIEW into a pass.

## H1. Exact expected results and operational use
The sample's clock is 12:30 UTC, within its approved 12:00–13:00 interval: EVIDENCE_PASS, exit 0. The failure fixture sets now to exactly 13:00: EXPIRED, REVIEW, exit 1. Output always states tenant_enforcement: false. Do not use an expired report to assume a real user's token or cached session was revoked.
The operator must compare the real PIM activation/audit records and actual permissions using a fresh session when validating a live system. A forged or stale input can fool a local evidence checker. Keep input provenance, policy version and approved storage in the handover.

## I. Break, diagnose, fix and repeat
1. Copy sample.json to experiment.json. Change approved to false. Expect DENY. Restore true and rerun.
2. Make approver equal requester. Expect DENY; restore the separate approver. Change mfa to false and expect DENY. Do not bypass a real organisation's approval/MFA controls.
3. Set now to 11:00 UTC on the same date. Expect NOT_STARTED. Set it to exactly the end time and expect EXPIRED. Restore 12:30.
4. Set end to 14:00 UTC. Expect DURATION_REVIEW. Restore 13:00. Change role to Global Administrator and expect ROLE_REVIEW.
5. Remove the timezone from now; expect INVALID, exit 2. Restore the full UTC timestamp. Run all ten behavioural tests. These deliberate failures demonstrate local rule boundaries, not real privilege enforcement.

## J. Acceptance and optional PIM practice — unrun
Local acceptance: ten tests pass, normal CLI exits 0, exact-expiry fixture exits 1 and invalid timestamps/types fail closed. Observed on local synthetic data only.
Optional later personal test-tenant route requires separate authorisation for live changes and valid P2/ID Governance licensing. Keep a separate emergency administrator; never test expiry on the last administrator. Create named dummy requester and approver accounts. In Entra admin centre, find PIM → Microsoft Entra roles. Under role settings, select User Administrator and configure a short maximum activation, MFA and a separate approval requirement. Add an eligible assignment for the dummy requester for a bounded period. Sign in as requester, open My roles and request activation with a reason. As approver, inspect and approve the request. Capture activation and audit history. Use a fresh test session to verify the intended action while active; after expiry refresh the session and verify that the privileged action is unavailable. Record actual times and cache/token limits, rather than assuming instant revocation. Remove only test assignments/accounts after checking the emergency account. No part of this tenant route was executed during this run.
## K. Evidence and useful artefacts
Keep the README, this lab, source, tests, synthetic fixtures, architecture and handover note, EVALUATION.md, DEMO SCRIPT.md and CHANGELOG.md together. Actual local CLI outputs and test results are in evidence/. A screenshot is optional: show the synthetic fixture, command and result together. Keep private tickets, exports, names, account IDs and access logs outside the public package. No screenshot or run here proves a real tenant configuration.

## L. Interview explanation to practise
Explain the problem, constraints, rule choice, build, deliberate fault, diagnosis, correction and verification. Explain why a report needs a human owner. State which parts you personally rebuilt and tested; do not turn an assisted package into a claim of independent past delivery. A useful next exercise is to rebuild the core function without looking, then ask someone to supply an unseen fixture.

## M. Possible CV wording after independent completion
Use only after personally rebuilding, running and explaining the solution: “Built and tested an independent synthetic identity-evidence checker, with explicit review states and repeatable failure tests.” Add the actual task and measured test count you ran. Do not describe this as DWP employment, production Entra delivery, enterprise security assurance or workplace savings.

## N. Next version and cleanup
Next iteration: add an unseen held-out fixture and record whether the expected result was decided before seeing the program output. Then consider a separately authorised read-only tenant evidence adapter, with minimal permissions, provenance, approved storage and redaction. Live integration remains unrun. No AI enhancement is needed for exact comparisons; an optional explanation assistant must never approve changes and must be tested against the deterministic report.
Cleanup: remove only your experiment file and locally generated outputs if no longer needed. Keep original fixtures and evidence. This offline route creates no accounts, roles, cloud resources or licences, so there is no tenant rollback. If you later practise in a tenant, document and remove only your named test assignments/accounts after confirming a separate emergency administrator remains available.

