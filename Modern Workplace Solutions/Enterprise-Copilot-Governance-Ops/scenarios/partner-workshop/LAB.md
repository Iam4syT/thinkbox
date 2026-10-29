# Governed AI partner workshop lab

## A Outcome and status
Rehearse a Microsoft workplace AI readiness workshop that surfaces oversharing, licence and pilot-baseline questions before a demonstration. The local scenario extends Enterprise-Copilot-Governance-Ops through its existing metadata policy. It does not call an AI service, enforce permissions, read tenant content or implement Pax8 8os. Bunamin's workshop delivery, tenant integration and independent rebuild are unrun. Allow two half-days plus an optional separately authorised sandbox session.

## B Public problem and research basis
Pax8 announced managed-intelligence services on 8 June 2026 and limited early access to 8os/8bot on 19 October 2026, with broader availability planned for early 2027. Those announcements support a governance-and-value discussion. A recurring partner workshop on a fictional finance document is our hypothesis. No internal Pax8 architecture, toolkit access or actual customer demand is assumed.

## C Duties exercised
 Microsoft ecosystem knowledge;  engaging explanation;  design judgement;  business value;  AI curiosity;  trusted advice;  workshops;  security/productivity awareness;  cross-function handover. The project practices an early design conversation, not extensive customer architecture delivery.

## D Evidence gap
Build on professional support guidance, scoped own-tenant demonstrations the recorded experience and support-led solution demos the recorded experience. Practise distinguishing permission risk, licensing and outcome evaluation. This assisted local scenario is separate from Bunamin's own prior Copilot-governance concept/review, the recorded experience. No commercial AI production claim is created.

## E Recurring use
Run the checklist at each customer pilot and after material access or use-case changes. The repeated question is whether the planned demo is bounded and reviewable. Target is fewer unexamined assumptions; no measured reduction, security guarantee or client adoption is established.

## F Architecture and baseline
Local JSON contains document IDs, sensitivity labels, access groups and three explicit human checks. Existing core_engine/policy.py returns allowed, exposed or review for limited metadata rules. Scenario code combines those results with owner approval, licence check and a defined baseline. Output is a review report only. No file content, user authentication or API connection exists. A manual checklist is the simpler baseline; AI can later assist explanations only if its extra value is evaluated. A metadata pass cannot prove actual retrieval security or production readiness.

## G Prerequisites and cost
Use a clean Thinkbox clone and Python 3.11 or later. The scenario uses the standard library and existing policy, with no pip installation for this slice. Local marginal service cost £0. Work in Modern Workplace Solutions/Enterprise-Copilot-Governance-Ops/scenarios/partner-workshop. Do not move it out of this parent structure. A native Copilot demonstration would require current product entitlement, approved tenant, users and owner review. Product names are in transition: Microsoft Learn now calls Microsoft 365 Copilot Microsoft Copilot, while the advert and some interfaces retain earlier wording. Confirm the actual product and licence before any trial; no paid/native step is executed here.

## H Step by step implementation

### Step 1 Open the exact scenario
Starting state and action: With Git installed from its official source, run git clone https://github.com/Iam4syT/thinkbox.git in a new folder. Then run cd "thinkbox/Modern Workplace Solutions/Enterprise-Copilot-Governance-Ops/scenarios/partner-workshop". If the clone already exists, navigate to this exact scenario. Read the parent README, LAB and CONTRIBUTIONS.
Expected result: main.py, data/workshop.json, tests/ and the parent core_engine/policy.py are present.
Verification and recovery: If import core_engine fails, restore the exact repository folder structure. Do not copy the scenario into an unrelated folder.

### Step 2 Check Python
Starting state and action: Run python3 --version; on Windows use py. No cloud credential is needed.
Expected result: Python 3.11 or later.
Verification and recovery: Use an approved Python runtime if absent. Do not install the parent plotting dependencies for this isolated standard-library scenario.

### Step 3 Set the customer question
Starting state and action: Write a fictional workshop question: should a small training business pilot an AI assistant for internal handbook questions? Record users, data owner, exclusions and task-quality baseline.
Expected result: A single bounded use case, with finance data outside the intended employee question set.
Verification and recovery: If the business outcome is only buy AI, ask what repeated task needs improvement and narrow it.

### Step 4 Inspect synthetic metadata
Starting state and action: Read data/workshop.json. Handbook is Internal Only with All-Employees access; finance is Confidential with Finance-Execs. Read the allowed vocabulary in the parent policy.py.
Expected result: Two fictional records and three true human checks. No real employee or document content.
Verification and recovery: Unknown labels/groups must lead to review, not be renamed to force a pass.

### Step 5 Run the normal scenario
Starting state and action: Run python3 main.py data/workshop.json.
Expected result: bounded_demo_candidate and two allowed record decisions.
Verification and recovery: Read the limits field aloud. It explicitly excludes actual access enforcement, AI generation and tenant integration.

### Step 6 Test oversharing
Starting state and action: Copy workshop.json to data/broken.json. Change only finance access_groups to ["All-Employees"]. Rerun with data/broken.json.
Expected result: review_before_demo and finance exposed.
Verification and recovery: Explain why staff-wide access to confidential information needs owner review. Restore Finance-Execs in the fixture only; no live permissions were changed.

### Step 7 Test unknown evidence
Starting state and action: In broken.json set finance access_groups to ["New-Group"] and rerun.
Expected result: record decision review.
Verification and recovery: Unknown membership is unresolved, not safe. Record the owner question rather than guessing group membership.

### Step 8 Test missing approval
Starting state and action: Restore original records but set the JSON field to "owner_approved": false and rerun.
Expected result: review_before_demo even with allowed metadata.
Verification and recovery: A policy result does not replace owner approval. The fixture flag simulates a recorded check; do not claim it grants consent.

### Step 9 Run all behaviour checks
Starting state and action: Run python3 -m unittest discover -s tests -v.
Expected result: 12 tests pass, covering missing baseline or licence, malformed checks, duplicate IDs, exposure and unknown metadata.
Verification and recovery: Preserve failed input and traceback if anything differs. Correct code or fixture only after explaining the failure.

### Step 10 Compare the simple baseline
Starting state and action: Use a paper checklist for the same two records and three checks. Record your manual decisions, then compare with the JSON output.
Expected result: The same decisions with an explicit unknown/review state.
Verification and recovery: Any disagreement is investigated before proposing AI. No time saving is claimed unless both methods are actually timed under comparable conditions.

### Step 11 Build the workshop story
Starting state and action: Prepare a five-minute storyboard: user task, permitted data, normal result, oversharing failure, owner action, licence assumptions, support boundary and pilot metric. A peer plays customer and challenges the recommendation.
Expected result: A recorded storyboard plus questions and corrections; mark it simulated.
Verification and recovery: Do not show a stock answer as a real Copilot response. Keep native generation and permissions testing unrun unless separately authorised and completed.

### Step 12 Plan the native extension
Starting state and action: Review current Microsoft privacy and adoption guidance. In an authorised isolated tenant, document actual user permission tests, licence entitlement, baseline answers, unsafe/unanswerable prompts and human review. Do not perform these actions in this local lab.
Expected result: A clear unrun integration plan with owner and stop conditions.
Verification and recovery: If licences/access are unavailable, retain the offline demo and state the evidence limit. A metadata policy is insufficient to pass live security acceptance.

### Step 13 Handover and cleanup
Starting state and action: Save the original/failed reports, peer questions, architecture and test output. Remove only data/broken.json and disposable outputs. Keep source/evidence; do not remove parent files or alter tenant settings.
Expected result: A reproducible scenario with no credentials or customer data in exports.
Verification and recovery: Inspect git diff and public links. Native resources, if later created under separate authority, require their own targeted rollback and billing check.

## I Break and fix exercises
Repeat the invalid-input and unknown/readiness exercises above without overwriting the original fixture. Save input, actual output, cause, correction and rerun. A report is an observation, not an approval to alter a tenant. Deliberately test one assumption that could change the recommendation.

## J Acceptance criteria
The documented normal run matches expected outputs; invalid inputs fail visibly; unknowns require review; calculations or policy decisions match the manual baseline; no private data or credentials appear; a peer can explain the limitation. Local tests verify the limited scenario only. Candidate delivery, native integration, customer satisfaction and return on investment remain untested until evidenced separately.

## K Portfolio artefacts
Retain README, this full LAB, source, fictional input, tests, actual evaluation, architecture notes, two-minute demo script and dated change record. Keep private application/claim maps outside the public package. Record the repository revision and runtime with each run. Do not describe assisted implementation as independent personal execution.

## L Interview story
Explain the customer problem and constraints first. Show how you chose the simplest design, which assumption the failure exposed, how you checked the correction and what remains unknown. Describe intended business value separately from measured results. Practise answering why a full AI solution or licence upgrade was not automatically recommended.

## M Conditional wording after personal completion
Use only after Bunamin has personally completed and evidenced the work: Built and tested a synthetic Microsoft workplace discovery or governance demonstration, documented its assumptions and failure cases, and explained a bounded customer pilot. Replace this sentence with exact own actions and artefacts; do not add production or customer-adoption claims. LinkedIn remains draft-only.

## N Next extension
Add a permitted real-user workshop or isolated tenant validation only after access, licences and scope are agreed. Evaluate task quality, permission boundaries, failure recovery, usage costs and support handover against a simple baseline. Keep a human decision maker responsible for access and deployment.

## Technical references
Checked 29 October 2026: Microsoft adoption guide https://adoption.microsoft.com/en-us/copilot/essential-guide/ ; privacy and data access guidance https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy . The latter page included a sign-in notice but exposed substantive privacy content. The local simulator does not implement Microsoft's service architecture. Recheck current product/licence/UI details before any native extension.
