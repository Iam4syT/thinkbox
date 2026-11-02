# Model evidence review lab

## A Purpose and outcome
Turn a model-evaluation record into an explainable hold or await human review result. A successful local check never deploys a model or authorises a network change.

## B Sourced need and scenario limits
The public advert includes AI testing, technical planning, governance and security. A review before an AI-assisted network change is a plausible recurring use, not an inspected client process. Client identity and actual regulatory controls are unknown. Source https://www.techrecruitmentspecialists.uk/job/13/detail/ checked 2 November 2026. No claim that three client developments or an internal stack were verified.

## C Requirement mapping
Targets R02 interface-contract thinking, R06 cloud/data handover concepts, R07 evaluation checks, R08 documentation and R09 governance. Exercises Python, analysis, privacy awareness and human oversight. JSON file exchange simulates an interface; no real telecom/cloud connector is implemented.

## D Gap and contribution
Academic model work supplies the context; operational gates, auditable evidence and a safe failure mode need practice. This is assisted local implementation, not Bunamin's independently observed work or production governance. A privacy_review flag is a supplied assertion, not proof of legal review. Exact regulations and jurisdiction must be established separately with the employer.

## E Repeated use and simpler baseline
An engineer could run checks for every candidate model and review changed input evidence. The simpler baseline is a fixed checklist with numeric rules; it is sufficient here. No LLM is used because an ambiguous generated decision would weaken a clear safety boundary. Measure missed invalid releases on unseen cases; no time or financial saving has been measured.

## F Architecture and security
Synthetic JSON record -> strict keys, version and type checks -> error/baseline/sample/privacy/rollback conditions -> human-readable reasons and an input SHA-256 -> no deployment. SHA-256 is a change-detection fingerprint, not a digital signature, trusted identity or tamper-proof audit service. Files and flags are local and user-editable. There is no authenticated API, approval workflow or regulatory certification.

## G Prerequisites and cost
Python 3.10 or newer, terminal and text editor; no packages or credentials. data/example.json and data/held.json are synthetic. The local path requires no cloud subscription, licences or paid services. Plan about an hour for the basic path and another hour for an own failure case, not a measured duration. Access to real model records would need explicit permission and privacy review and is outside this lab.

## H Step by step implementation
### Step 1 Start in the scenario root
Open the downloaded folder that contains main.py, data and tests. Run python3 --version and ls. Expected Python 3.10+ and the listed files. If data/example.json is missing, check your path before editing. No dependency installation is required.

### Step 2 Inspect one record
Open data/example.json. Read schema_version, model_id, model_mae_ms, baseline_mae_ms, test_n, data_scope, privacy_review and rollback_plan. Expected version 1, errors 0 and 9, sample 8, synthetic scope and two boolean true flags. These booleans only simulate an evidence checklist. Never set them true for real data without the required review.

### Step 3 Follow the contract
Open main.py. Check REQUIRED, strict type checks and the threshold rules. Verify unknown keys and non-finite errors fail rather than silently defaulting to safe values. Explain why the string true is different from the boolean true. If your edited contract accepts missing data, restore fail-closed validation before proceeding.

### Step 4 Run normal evidence
Run python3 -B main.py. Expected decision await_human_review, no reasons, deployment_performed false and a 64-character input fingerprint. Check that no approved or deployed result appears. If the program cannot find the file, return to the scenario root; the default path is relative to the script.

### Step 5 Run an unsafe case
Run python3 -B main.py data/held.json. Expected decision hold, including an error threshold failure and missing privacy review. It must still report deployment_performed false. If it proceeds to human review without reasons, inspect the rules instead of removing the failure fixture.

### Step 6 Check the baseline boundary
Copy example.json to learner-test.json. Set model_mae_ms equal to baseline_mae_ms. Run python3 -B main.py learner-test.json. Expected hold with does_not_beat_baseline. Restore the model error before the next exercise. A more complicated model must earn its use; matching a simpler baseline is insufficient under these chosen lab rules.

### Step 7 Break the schema and recover
In learner-test.json add an extra field such as customer_name or change privacy_review from true to the string true. Run again. Expected ValueError schema mismatch or review flags must be boolean. Restore the exact schema/types and verify normal output returns. Save the failure message. This personal manual exercise remains unrun until you do it.

### Step 8 Run behavioural checks
Run python3 -B -m unittest discover -s tests -v. Expected 9 test methods and OK. They check poor/tied model results, missing privacy and rollback, disallowed real-data scope, too-small samples, invalid schema/types and changed fingerprints. Read any failure and fix the cause. Do not weaken policy merely to obtain a passing result.

### Step 9 Connect the learning scenarios manually
Read the first lab's result. In a disposable copy of this lab's example, enter its actual model id, held-out sample and two MAE values. Keep synthetic scope, and record that privacy and rollback flags are lab assertions. Run the checker. Expected the first lab's ordinary evidence can reach human review and its drift result holds. This is file-contract integration, not an automated or live cloud connection. Never convert eligible_for_review directly into deployment approval.

### Step 10 Make a personal improvement
Choose one new invariant, for example a required evidence date with an explicit freshness policy. Define the policy, add a failure case, implement the check and record your own command/output/source hash. Expected an explained own change and unseen fixture. Supplied automated logs do not count as your personal practice.

### Step 11 Hand over and clean up
Write a runbook: who owns model evidence, who checks privacy, who can approve a change, how the previous model would be restored and who handles an incident. State which parts are planned rather than implemented. Save learner evidence, then remove only learner-test.json when unwanted. No real model, tenant or network was changed, so no production rollback or cloud cleanup is claimed.

## I Break and fix exercises
Wrong schema -> reject -> repair the contract. Real/customer scope -> hold -> use approved synthetic data. Missing rollback/privacy -> hold -> obtain actual evidence before proceeding. Excess error or baseline tie -> hold -> investigate or retain the baseline. Do not use an LLM to override these rules.

## J Acceptance and evaluation
Both CLI paths return documented decisions without deployment. All 9 test methods pass in the supplied automated local run. Two sample JSON files exercise the normal and held paths. Human approval, authenticated identities, cloud integration, real-data fairness testing, monitoring and regulatory compliance remain unestablished.

## K Artefacts
Keep source, two fixtures, tests, documentation, source receipt and output logs together. A future screenshot or video must be from your actual run. Preserve the distinction between deterministic safety checks and model quality. Publish no private CV, recruiter or employer information.

## L Interview story
Describe how model evidence crosses a system boundary, why missing information stops progression, how baseline/error/privacy/rollback conditions are explained and why the output still needs a person. Show a failure and the resulting reasons. Explain the gap between a local rule engine and a real controlled deployment service.

## M Conditional wording
After personal completion only: Reviewed and extended a local model-evidence contract with baseline, privacy and rollback checks, documenting a rejected failure case and human-review boundary. Use wording that reflects your actual assisted contribution. This lab is excluded from the current CV and no LinkedIn post is sent.

## N Next extension
Design an authenticated batch/API contract with a real evidence store, signed approvals, access controls, audit retention and rollback testing. Use a separately approved sandbox and budget. A provider service and legal compliance review are not implemented by these local flags. Add generative explanations only if they improve an evaluated task without controlling approvals.

## Technical sources
Python unittest https://docs.python.org/3/library/unittest.html and standard-library JSON/hashlib documentation apply. Checked 2 November 2026. No external API, commercial model or proprietary architecture used.
