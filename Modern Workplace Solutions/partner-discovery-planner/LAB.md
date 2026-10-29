# Partner discovery and option comparison lab

## A Outcome and status
Turn a fictional customer's collaboration need into a reviewed option, a bounded pilot and an honest cost discussion. This is independent practice, not a Pax8 commissioned project. The local worksheet can be tested without a tenant. Bunamin's discovery meeting, native Microsoft demonstration and customer outcome are unrun. Expected learning budget: two half-days offline, then one supervised sandbox session; estimate, not measured time.

## B Public problem and research basis
Pax8's Modern Workplace role asks for discovery, demos and business-value explanation. Its 19 October 2026 Managed Intelligence Guide organises partner work around discovery, selling, implementation and management. Our fictional ten-person training business repeats collaboration handovers weekly. That customer and its needs are a hypothesis, not a Pax8 customer account. This guide addresses how to decide on a solution before selling it.

## C Duties exercised
 customer consultation;  Microsoft ecosystem knowledge;  simple explanation;  cloud-solution design gap;  commercial value;  sales collaboration;  demos/workshops;  outcomes;  scalable partner practice. The tool aids reasoning; it does not prove extensive commercial experience.

## D Evidence gap
Build on reported support-led option advice and demos, the recorded experience. Practise a complete written discovery-to-pilot recommendation, assumptions and evaluation. New code execution is assisted project evidence. No production capability upgrade follows from passing tests.

## E Recurring use
A consultant can repeat the worksheet for every qualified customer opportunity and revisit it at each pilot review. Missing baseline, licence assumptions and permission ownership are recurring questions. Target value is more reviewable recommendations; no actual saving or sales conversion has been measured.

## F Architecture and baseline
Customer interview notes feed a local JSON worksheet. Python checks inputs and calculates illustrative capacity value minus first-year cost. A human reviews the recommendation before any tenant action. Data stays local, with fictional names and no identity, email or tenant export. Baseline is the same arithmetic in a spreadsheet plus a written checklist. AI is unnecessary for deterministic arithmetic. Optional AI wording later must be checked against the approved facts and cannot approve purchases or changes.

## G Prerequisites and costs
Use Python 3.11 or later, a text editor and a terminal. No paid packages, API, cloud account or tenant required offline; marginal service cost £0, excluding your computer/internet/time. Native extension requires an isolated Microsoft 365 test tenant, authorised account and actual feature licences. Check current entitlement with the administrator; a trial is not guaranteed. Do not start a chargeable subscription. The fixture's £10 monthly per seat and 15 minutes/week are invented teaching inputs, not Microsoft prices or observed benefits.

## H Step by step implementation

### Step 1 Create a clean workspace
Starting state and action: Start with an empty learning folder. With Git installed from its official source, run git clone https://github.com/Iam4syT/thinkbox.git. Then run cd "thinkbox/Modern Workplace Solutions/partner-discovery-planner". If the repository is already present, open that exact folder instead.
Expected result: README.md, scripts/planner.py, templates/customer.json and tests/ are present.
Verification and recovery: Check the folder name before running a command. If any file is missing, stop and record the checkout revision.

### Step 2 Check the runtime
Starting state and action: From this folder run python3 --version. On Windows use py --version, then replace python3 with py in later commands.
Expected result: Python 3.11 or later prints its version.
Verification and recovery: If the command is unavailable, install Python from its official source or use an approved runtime; do not run a random installer.

### Step 3 Capture the business problem
Starting state and action: Open a new notes file. For the fictional business record who hands work over, what is missed, how often, current method, data owner, desired outcome, budget and a named decision maker. Record unknowns as unknown.
Expected result: A one-page discovery record separates facts from assumptions.
Verification and recovery: Ask a peer to identify each assumption. Recover by narrowing the use case if there is no recurring user task.

### Step 4 Inspect the fixture
Starting state and action: Open templates/customer.json. Read every key. It assumes 10 seats, collaboration workflow, reviewed readiness, 15 minutes/week, £20 hourly capacity value, £10 monthly licence and £200 setup.
Expected result: The seven numeric/choice inputs are understood; readiness is a human input, not a tenant scan.
Verification and recovery: Compare the file against the README. Never enter actual customer data in the public fixture.

### Step 5 Run the worksheet
Starting state and action: Run python3 scripts/planner.py templates/customer.json.
Expected result: pilot_candidate; illustrative annual capacity value 2600, first-year cost 1400 and net 1200. Currency follows the illustrative inputs.
Verification and recovery: Check 10 × 15 ÷ 60 × 52 × 20 = 2600 and 10 × 10 × 12 + 200 = 1400. If output differs, inspect the JSON and preserve the failure.

### Step 6 Run behaviour checks
Starting state and action: Run python3 -m unittest discover -s tests -v.
Expected result: 12 tests pass, including invalid inputs and review states.
Verification and recovery: A failing assertion needs investigation. Do not delete a failing test or call an unrun test passed.

### Step 7 Compare two options
Starting state and action: Copy the fixture to templates/alternative.json. Change monthly_licence to 20 and rerun.
Expected result: First-year cost 2600 and net 0, with the same assumed capacity benefit.
Verification and recovery: Compare both saved outputs. A higher assumed price does not prove the second option is worse; feature need and quality still need validation.

### Step 8 Make missing readiness visible
Starting state and action: In alternative.json set the JSON field to "readiness": "unknown" and rerun.
Expected result: review_first even if the illustrative economics are positive.
Verification and recovery: If a recommendation is treated as authorised deployment, stop. Restore reviewed only after a real owner checks permissions, needs and entitlement.

### Step 9 Design the Microsoft option
Starting state and action: In notes compare a Teams/SharePoint collaboration pattern with current shared files. Record identity, groups, ownership, external sharing, licence dependencies, support and rollback. For email, distinguish a mail distribution list from access or licence assignment.
Expected result: A simple architecture and two-option decision record with no invented rollout.
Verification and recovery: Use current Microsoft Learn guidance and administrator review. If a requirement cannot be met, document the gap rather than changing the requirement.

### Step 10 Rehearse a customer demonstration
Starting state and action: Use synthetic screenshots or an approved test tenant only. Explain the current task, show one relevant feature, ask the customer role to repeat the task and capture uncertainty. Do not claim a live demo when using a storyboard.
Expected result: A five-minute storyboard or separately recorded authorised tenant demonstration.
Verification and recovery: If feature access/licence is absent, retain the storyboard and mark the native step unrun. Never use a live client tenant for this exercise.

### Step 11 Write pilot acceptance
Starting state and action: Define one task, baseline completion time/quality, pilot users, duration, success criteria, data owner, change approval and stop/rollback condition. Use placeholders until measured.
Expected result: A pilot plan a customer could review before spending or changing access.
Verification and recovery: A licence count or use statistic alone is not business value. Recover by adding a task-quality check and actual baseline.

### Step 12 Hand over and clean up
Starting state and action: Save fictional input, both outputs, architecture, assumptions and peer questions. Remove only alternative.json and generated copies when no longer needed; preserve source and test evidence. If native work was separately authorised, remove only the new test objects under that plan and verify billing.
Expected result: A reproducible local package and no abandoned paid resource.
Verification and recovery: Check git diff before public export. Keep real customer notes, credentials and tenant screenshots private.

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
