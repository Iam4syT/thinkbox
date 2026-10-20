# Copilot permissions review lab
## A Outcome
Build a small evidence-review report that separates licence/service issues, permission oversharing and missing evidence before a human decides the next step. It does not inspect or change Microsoft 365.

## B Public need and limits
Burges Salmon's27 January 2026 Digital Enablement Programme announcement and selected Application Specialist JD emphasise secure Copilot support and responsible adoption. A reusable access-review worksheet is a reasoned scenario, not a known firm incident. Microsoft documentation explains underlying permission boundaries and information protection; this deliberately simplified model is not Copilot or Purview enforcement.
Sources checked20 October 2026: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture-data-protection-auditing ; https://learn.microsoft.com/en-us/purview/sensitivity-labels ; https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-service-plans . Recheck current interfaces/licences before any authorised tenant extension.

## C Requirements exercised
R3 Copilot content/security understanding; R5 licence/access/health triage; R6 information governance; R10 clear escalation; R11 accessible support documentation. R4 actual third-line ownership remains unproven.

## D Candidate gaps
Strengthens reasoning about M365 Copilot operations where current evidence is Developing/Not Yet Evidenced. Builds on professional M365/identity troubleshooting and own-tenant demonstrations. Synthetic flags cannot establish professional Copilot configuration or legal-policy authority.

## E Recurring value and baseline
A support engineer could use a structured checklist for each missing-app/access complaint and a weekly permission review. Baseline is a manual review of the same five fixtures using the published rule table. Code applies those rules consistently; no measured time saving, real leak prevention or productivity gain. AI is not used: deterministic evidence checks are easier to inspect, cheaper and do not send sensitive metadata to a model. An optional AI explanation would need a separate correctness/leakage test and could not approve changes.

## F Architecture
Operator → synthetic fixtures.json → validated Python review → JSON evidence report → human review. No authentication to Microsoft, Graph, SharePoint, semantic index or Purview. Boundary: input is manually asserted evidence, not trusted tenant telemetry. Unknown evidence remains collect_evidence. A confidential label without encryption is explicitly not treated as access enforcement. Scoped plus healthy plus licensed means only no flag in this model; it is not a security certification.
## Environment and cost
Local route: Python3.11 or newer, a terminal and a text editor. It uses only the standard library, synthetic JSON and local files. No licence, API key, network call or paid service; cloud/API cost £0 for this route. Time budget: one focused session for the local slice, then one to three weekends for independent explanation and optional tenant work; estimates, not measured duration. Existing computer cost excluded.

Optional Microsoft route is separate and UNRUN. It needs an authorised isolated Microsoft 365 tenant, suitable base subscription, a Microsoft 365 Copilot licence where the test requires it, two test users and least-privilege admin roles. Purview/advanced controls may require additional entitlements. Check current Microsoft licensing/admin guidance before obtaining anything. Do not buy or start paid resources without approval. No real client files, production tenant, global-admin shortcut or live permission changes are part of this local build.

## Engineering status
This scenario is implemented and locally evaluated on synthetic data. It is an independent exercise, not commissioned client work. Independent learner reproduction and live Microsoft tenant validation remain unobserved.

## H Setup and execution
1. Starting state: an empty local working folder and Python available. Open a terminal and run `python3 --version`. Expect3.11 or later; check the printed version. If missing, install Python from an approved official source before continuing; do not substitute a web-based runner holding private files.
2. Starting state: repository available. Download/clone the Thinkbox repository, then open `Modern Workplace Solutions/Enterprise-Copilot-Governance-Ops/scenarios/m365-support-access-review`. Run `pwd` and list files. Expect main.py, fixtures.json, test_main.py and this guide. If absent, correct the directory; do not run the parent project's tenant-looking scripts.
3. Starting state: scenario files visible in your editor. Read main.py's module statement and README. Expect a local-only model with no service calls. Search for network imports/credentials; check there are none. Stop if a later version adds a live integration until its authority is separately agreed.
4. Starting state: five fixturesA–E. Open fixtures.json. Read licence, service_health, access, label and encrypted fields. ExpectA scoped, B confidential/broad, C unknown, D no licence, E service incident. Check every row has a distinct ID. If JSON is invalid, restore the committed file and retry; keep your failed version separately for learning.
5. Starting state: no generated report. Before running code, manually write expected results: A no_flag_in_model with label_is_not_enforcement true; B review_oversharing; C collect_evidence; D check_licence; E check_service_incident. This is the baseline. Do not tune labels after seeing output to manufacture agreement.
6. Starting state: baseline saved in notes. Run `python3 -B -m unittest -v`. Expect eight tests pass, including unknowns, invalid/missing evidence and duplicate IDs. Check the exit code is0. If a test fails, save its traceback and examine the rule/test before changing either; never delete the failing test just to pass.
7. Starting state: tests pass. Run `python3 -B main.py --input fixtures.json --output report.json`. Expect a report file with five records. Open it and compare IDs/reasons with your baseline. No credentials should be requested. If the output path cannot be written, choose a new local output path in your folder.
8. Starting state: recordA reviewed. Check label_is_not_enforcement true although status is no_flag_in_model. Explain that a classification name alone does not lock down a file. Verify the report does not say safe, compliant or authorised for deployment. If your explanation assumes a label always encrypts, revisit actual label configuration documentation.
9. Starting state: recordB broad/confidential. Explain why the report requests oversharing review instead of changing access. Check authorises_change is false. Write a short escalation note listing ID, evidence states, uncertainty and proposed owner. Do not copy actual sensitive file names or contents into the public note.
10. Starting state: recordC unknown. Check unknown fields produce collect_evidence rather than a clean result. Add a note on who would supply licence/health/access evidence in a real case. If a report is clean despite unknowns, stop and investigate the rule before using the report.
11. Starting state: a disposable copy named broken.json. Change B's access to `everyone` and run the same command using broken.json with output broken-report.json. Expect exit2 and Invalid evidence state; no new output. Use a fresh output filename so an older report cannot be mistaken for a result. Restore `broad`, rerun and verify the flag returns.
12. Starting state: another disposable copy. Duplicate A's whole row without changing its ID. Expect Duplicate case ID and no fresh report. Restore unique IDs and rerun tests. This demonstrates refusal to count repeated evidence as two independent cases.
13. Starting state: successful local report. Save Python version, command, input hash, output hash, baseline comparison and unexpected findings in your private notes. Keep input/output paired. Public evidence should contain only the synthetic fixtures and reports.
14. Starting state: handover note drafted. Read it as a Service Desk colleague: can they identify issue, evidence, uncertainty, owner and next check without seeing client content? Ask a reviewer to explain one unseen unknown case. If unclear, revise the note and repeat; do not claim measured user adoption.

## I Break and fix
The invalid-state and duplicate-ID exercises above are implemented negative paths. Also change healthy to unknown: report must collect evidence. Restore it and rerun. Do not test by granting broad access in a live tenant. Recovery is restoring known fixtures, rerunning checks and confirming the correct report filename/time.

## J Acceptance and actual result
Acceptance: all five baseline rows have expected reasons; unknowns never clean; invalid/missing fields and duplicate IDs rejected; no operation authorises changes; a label without encryption is distinguished from enforcement. Actual automated local result20 October 2026: eight automated tests passed and five-fixture report generated. Tests use designed synthetic examples, not held-out user/tenant data; no general accuracy rate. Native Copilot retrieval/licensing/permissions and independent learner performance remain untested. Evidence: evidence/tests.txt and evidence/report.json.

## K Artefacts and cleanup
Keep source, synthetic fixture, report, tests, rule notes, architecture boundary and a brief demo. For a screenshot, show synthetic report only and remove personal path/account details. No video recorded. Remove only report.json and your disposable broken files when finished; keep committed evidence. Local route creates no cloud resources. For a later authorised tenant run, record and reverse only lab changes using a pre-agreed cleanup plan and verify access/licences/billing state; do not delete a tenant to tidy up.

## L Interview story and native extension
Problem: repeated licence/permission questions need evidence before action. Constraint: no real tenant or client data. Design: deterministic rules and explicit unknown state. Build: local model and report. Failure: invalid evidence or duplicate case must stop. Verification: eight checks and manual baseline. Intended value: clearer triage; no measured workplace benefit. The learner should reproduce one changed case and explain why it stays uncertain.
Optional tenant extension, unrun: authorised admin verifies actual Copilot entitlement/service plan and service health without buying a licence; create only approved dummy documents and user scopes; compare permitted/denied direct file access before any Copilot query; test actual retrieval with citations using licensed test identities; separately inspect configured label protection. Record identity, timestamp, propagation wait and result; unexpected exposure stops the test and goes to the security owner. Approval is required before changing access or protection. Collect actual evidence before any claim of integration.

## M Conditional wording
Use only after independently completing and evidencing the lab: Built and checked a synthetic support worksheet that flags oversharing, missing evidence and licence/service issues; documented why label names alone do not enforce access. Do not say deployed Microsoft 365 Copilot governance.

## N Next version
Add a read-only, least-privilege export adapter only after scope/licensing review. Treat API fields, evidence age and missing permissions explicitly. An AI summary is optional and must not decide access or approve remediation.
