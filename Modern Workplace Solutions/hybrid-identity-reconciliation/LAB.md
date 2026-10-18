# Lab 1: hybrid identity reconciliation
Status: local synthetic tool built and evaluated on 18 October 2026. Live AD/Entra Connect validation is unrun. This is an independent learning project.

## A. Outcome
Help an identity support engineer spot missing, ambiguous, disabled or unsynchronised identity evidence before recommending a change. It does not calculate or apply a real soft match or hard match.

## B. Employer problem and research basis
The DWP Identity campaign describes AD/Entra hybrid services, lifecycle automation and reliable live operations. A repeatable comparison is a plausible supporting workflow, not a confirmed DWP internal problem or architecture. Microsoft's directory synchronisation documentation is the technical context; this tool deliberately stays outside a live directory.
Reference: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect

## C. Job mapping
R1: identify hybrid evidence gaps; R2: hand over a clear report to the directory owner; R3: repeat checks for returning/joining users. It does not cover enterprise design, federation, PKI, actual IGA provisioning or multisupplier leadership.

## D. Candidate gap
Builds on reported matching/sync support and develops reproducible diagnostic evidence. It does not convert support experience into enterprise architecture ownership. Exact production attributes and restore procedures remain separate from this synthetic model.

## E. Repeat-use test, baseline and success target
The support team could run the check whenever a user is missing or a returning user's access is uncertain. Baseline is a manual comparison of two small inventories. Target: flag every authored fault fixture and leave both inputs unchanged. No measured time saving. No AI model: exact comparisons are cheaper to inspect as rules.

## F. Architecture and fields
Two arrays, onprem and cloud, contain synthetic id, smtp and enabled fields. Cloud rows also contain synced. IDs must be unique within each source. smtp is normalised for case and whitespace only to locate possible comparison records. A shared email address is not proof that two real directory identities are the same. More than one matching candidate yields AMBIGUOUS. This model does not represent immutable IDs, source anchors, deletion states, licences, OU filters, sync errors or a real matching algorithm.

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

## H1. Exact expected results and investigations
The sample has one enabled local and one enabled, synced cloud record: CHECKS_PASS. The failure fixture has two cloud candidates with the same synthetic SMTP: REVIEW with AMBIGUOUS. The output always states writes_performed: 0.
When MISSING appears, check the source and timestamp first; a missing export record is not permission to create an account. For UNSYNCED, ask the authorised administrator to inspect actual synchronisation evidence. For DISABLED_REVIEW, verify the approved lifecycle state rather than enabling an account automatically.

## I. Break, diagnose, fix and repeat
1. Copy sample.json to experiment.json. Set cloud to an empty list. Run the checker: expect MISSING. Restore the original row and expect CHECKS_PASS.
2. Duplicate the cloud row and give it another id, preserving smtp. Expect AMBIGUOUS. Remove the duplicate experiment row and rerun. Never delete a real directory object to imitate this exercise.
3. Set the cloud synced value to false. Expect UNSYNCED; restore true. Then set onprem enabled to false and expect DISABLED_REVIEW.
4. Replace enabled: true with enabled: "true". Expect INVALID and exit code 2. Restore the proper boolean. This checks that incomplete or wrongly typed evidence cannot silently pass.
5. Run all eight behavioural tests again. Keep the failure output and corrected output as distinct evidence, not overwritten screenshots.

## J. Acceptance and optional live extension — unrun
Local acceptance: eight tests pass; normal CLI exits 0; ambiguity fixture exits 1; source input stays unchanged; invalid types exit 2. These were observed locally. No load/scale test was performed.
For a later separately authorised test tenant: record directory ownership and licensing, use a dummy on-premises AD user in a dedicated test OU, verify the intended OU/object sync scope and source-of-authority with the administrator, then capture actual object/sync evidence. Do not copy this toy SMTP comparison into real matching commands. Use Microsoft's current recovery/matching procedure for the actual case and review source-anchor consequences before any mutation. Validate Active users, on-premises synchronisation status and the test user's actual sign-in/service access; retain logs and rollback steps. No tenant commands or live changes are part of this completed build.
## K. Evidence and useful artefacts
Keep the README, this lab, source, tests, synthetic fixtures, architecture and handover note, EVALUATION.md, DEMO SCRIPT.md and CHANGELOG.md together. Actual local CLI outputs and test results are in evidence/. A screenshot is optional: show the synthetic fixture, command and result together. Keep private tickets, exports, names, account IDs and access logs outside the public package. No screenshot or run here proves a real tenant configuration.

## L. Interview explanation to practise
Explain the problem, constraints, rule choice, build, deliberate fault, diagnosis, correction and verification. Explain why a report needs a human owner. State which parts you personally rebuilt and tested; do not turn an assisted package into a claim of independent past delivery. A useful next exercise is to rebuild the core function without looking, then ask someone to supply an unseen fixture.

## M. Possible CV wording after independent completion
Use only after personally rebuilding, running and explaining the solution: “Built and tested an independent synthetic identity-evidence checker, with explicit review states and repeatable failure tests.” Add the actual task and measured test count you ran. Do not describe this as DWP employment, production Entra delivery, enterprise security assurance or workplace savings.

## N. Next version and cleanup
Next iteration: add an unseen held-out fixture and record whether the expected result was decided before seeing the program output. Then consider a separately authorised read-only tenant evidence adapter, with minimal permissions, provenance, approved storage and redaction. Live integration remains unrun. No AI enhancement is needed for exact comparisons; an optional explanation assistant must never approve changes and must be tested against the deterministic report.
Cleanup: remove only your experiment file and locally generated outputs if no longer needed. Keep original fixtures and evidence. This offline route creates no accounts, roles, cloud resources or licences, so there is no tenant rollback. If you later practise in a tenant, document and remove only your named test assignments/accounts after confirming a separate emergency administrator remains available.

