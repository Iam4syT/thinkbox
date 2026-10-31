# Agent trace and release evaluation
## A. Outcome
Decide whether an AI workflow meets explicit quality, cost and safety gates. Local learning solution, not legal advice or an employer commission. The supplied offline implementation was automatically tested on synthetic data; cloud/model/tenant stages and the learner's own performance remain unrun.
## B. Company need and research
The Applied AI Engineer advert explicitly requires representative evaluations, intermediate agent traces, token economics and operational readiness. Mishcon's 24 February 2025 Legora partnership describes a measured pilot; its 2 October 2026 AI governance article emphasises a business problem and clear responsibility. A recurring internal release review is an inferred learning scenario, not a claim about a current internal failure or proprietary system.
## C. Vacancy mapping
R07–R11/R13–R19; E01/E06/E11/E12; D02/D06. The lab exercises a bounded part of these requirements. It does not satisfy every professional or production criterion.
## D. Gap mapping
Strengthens strict trace validation and failure analysis; real GenAI quality measurement, production monitoring and authored TypeScript still need separate work. Academic evaluation and support troubleshooting provide adjacent foundations. The new package does not upgrade personal capability ratings.
## E. Recurring value
An authorised colleague could use this workflow at each prompt/model/tool change and release. Intended value is consistent go/hold decisions and easier failure diagnosis. No time saving, adoption or client benefit has been measured.
## F. Architecture and baseline
Synthetic JSON traces → strict parser/type checks → allowed tools/source scope → review/quality/latency/token rules → HOLD or READY_FOR_REVIEW. Caller-supplied quality is a fixture; no judge model, human identity verification or tool execution occurs.
Use the deterministic baseline first. Generative AI may help propose summaries or analyse complex failure patterns, but it adds cost and failure modes. Compare on the same held-out cases before choosing it. A simple rules/search solution may be sufficient.
## G. Prerequisites and cost
Python3.11+, terminal, text editor and this package. The standard-library mode needs no licence, key or paid service; local compute only. Keep all data synthetic. Allow one focused weekend for local build/explanation; plan another one or two for an approved cloud extension. Timing is a plan, not measured effort. Azure/LLM stages require an authorised subscription, role-scoped identity, secure secret store, spending cap and current provider price check; no spend is authorised or incurred here.
## H. Build, test and document
### Step 1: Locate the files
Starting state: Package available locally.
Action: Open a terminal. In a fresh clone run cd "thinkbox/AI Projects/Agent-Release-Evaluation". If the supplied local package is used, open its public folder instead. Run pwd and list its files.
Expected result: main.py, tests, data and evidence are visible.
Check: Check the folder contains main.py before continuing.
Recovery: If files are missing, return to the package root; do not run commands from another project.

### Step 2: Check Python
Starting state: Previous step checked; synthetic data only.
Action: Run python3 --version. Use Python 3.11 or newer. Run python3 -m venv .venv, then source .venv/bin/activate on macOS/Linux. Windows PowerShell uses .venv\Scripts\Activate.ps1.
Expected result: The environment activates; python --version shows the selected interpreter.
Check: No dependencies or credentials are required.
Recovery: If Python is absent, install it from python.org; if activation is restricted, use the environment interpreter directly without weakening policy.

### Step 3: Inspect the data
Starting state: Previous step checked; synthetic data only.
Action: Open data/traces.json in a text editor. Read every field and compare it with main.py. Make a copy named data/working.json.
Expected result: A separate working fixture exists.
Check: Keep the original tracked fixture unchanged for the acceptance suite.
Recovery: If JSON fails to parse, restore from the original. Never add actual client or personal data.

### Step 4: Set the baseline
Starting state: Previous step checked; synthetic data only.
Action: Read EVALUATION.md and tests/test_behaviour.py before modifying code. Record the source hash and expected ordinary/failure results in your own notes.
Expected result: Acceptance conditions are written before an experiment.
Check: Do not tune a held-out evaluation set to make a result pass.
Recovery: If criteria are unclear, stop and define them with a reviewer; label proposed thresholds as lab policy.

### Step 5: Run the trace gate
Starting state: Previous step checked; synthetic data only.
Action: Run python -B main.py.
Expected result: Seven results: T01 READY_FOR_REVIEW; T02–T07 HOLD.
Check: Compare failed reasons with each deliberately changed field in data/traces.json.
Recovery: If all pass, inspect thresholds and allowlist; do not lower safety rules to make fixtures green.

### Step 6: Check tool boundaries
Starting state: Previous step checked; synthetic data only.
Action: In working.json set T01 tools to ["send_email"]. Run python -B main.py --data data/working.json.
Expected result: T01 HOLD, including tool_allowlist. No email is sent.
Check: This validates a recorded trace; it does not intercept or prevent a real tool call.
Recovery: For a live agent, put enforcement before execution as a separate control; the lab cannot supply that guarantee.

### Step 7: Check structured output
Starting state: Previous step checked; synthetic data only.
Action: Change human_review to the string "true" in working.json and rerun. Then restore the Boolean true.
Expected result: Malformed input exits INVALID INPUT; real JSON true parses.
Check: Inspect process exit status. A string cannot impersonate a Boolean approval.
Recovery: Restore the fixture; never coerce strings blindly or treat READY_FOR_REVIEW as human approval.

### Step 8: Check units and budgets
Starting state: Previous step checked; synthetic data only.
Action: Change latency_ms to 2001, then tokens_in to 1001 in separate trials. Keep a run log of expected and observed failures.
Expected result: Latency and token budget failures are explicit.
Check: Fixture inputs are simulated. Cost uses 1 input / 4 output units per million, not a provider tariff.
Recovery: Fix incorrect units or oversized context; a higher budget requires a reviewed policy change, not silent bypass.

### Step 9: Design the real evaluation
Starting state: Previous step checked; synthetic data only.
Action: Make a new held-out set of permitted document questions with expected citations, allowed tools and a human-reviewed quality rubric. Keep model outputs separate from policy.
Expected result: An evaluation plan specifies ordinary, unauthorised, unanswerable, injection and timeout cases.
Check: Actual model execution, traces, provider usage and human ratings are still unrun.
Recovery: If no approved service/budget is available, retain the offline gate; do not simulate measurements and call them real.

### Step 10: Run all checks
Starting state: Previous step checked; synthetic data only.
Action: Run python -B -m unittest discover -s tests -v. Save your own terminal output and one failed trial before repair.
Expected result: 14 tests pass in the supplied version.
Check: Rerun after every code or fixture change; your run is distinct from the supplied result.
Recovery: Use the first failing assertion to locate the behaviour. Restore the changed fixture and rerun; do not delete the test.

### Step 11: Record and explain
Starting state: Previous step checked; synthetic data only.
Action: Create evidence/my-run.md with date, environment, own change, expected result, observed result and limitation. Explain one failure without reading the guide.
Expected result: A personal evidence record exists.
Check: A reviewer can reproduce the change and trace it to code and a test.
Recovery: If you cannot explain it, repeat the smallest step and seek review; do not add a completion claim to a CV.

### Step 12: Clean up safely
Starting state: Previous step checked; synthetic data only.
Action: Deactivate the virtual environment. Delete only your working.json and generated local outputs after preserving permitted learning evidence. No cloud resources were created.
Expected result: Original source and acceptance fixtures remain.
Check: Review filenames before deletion; keep original evidence and do not delete unrelated work.
Recovery: If a cloud extension was attempted, stop its endpoint and delete the dedicated resource group only after checking it contains no shared resources.

## I. Break and fix
Try an unapproved tool, cross-matter citation, Boolean-as-token count, string approval, NaN quality and over-budget trace. Each must HOLD or reject input; record why. A post-hoc gate cannot stop an action already taken.
## J. Acceptance and validation
Local supplied suite: 14 behavioural tests passed. Ordinary and materially faulty inputs are covered, at fixture scope. Sources, group metadata, policy versions and exact code hashes must be retained. No automatic approval; invalid types reject; tool/citation violations hold; boundaries at quality0.8,2000ms,1000tokens are explicit lab choices. Broader quality, live identity, scale, actual token latency/cost, accessibility, availability and legal correctness remain unmeasured.
## K. Portfolio evidence and handover
Keep main.py, data/, tests/, requirements.txt, README.md, EVALUATION.md, evidence/tests.txt, evidence/demo.json, docs/architecture.md and CHANGELOG.md. Add your own reviewed change and demonstration separately. Public documentation excludes private applications and contacts. Publication must be independently verified before calling the remote project published.
## L. Interview story
Explain the recurring need, confidentiality constraint, baseline, one personal design choice, a failure you actually caused, the expected/observed result, and why human review remains. The supplied package alone is not a personal delivery story. Discuss how you would obtain permitted data and team review before a live pilot.
## M. Wording only after personal completion
Use only after independently performing and evidencing the work: “Built and evaluated a synthetic agent-trace gate with strict output validation and explicit review/hold decisions.” Add actual test counts only from your own reproducible run. Never call this a production legal system.
## N. Optional next version — unrun
Capture real approved model traces and provider-reported usage; version prompts, tool schemas and evaluation cases. Add read-only MCP transport and timeout/retry tests, a human-rated groundedness rubric, an accessible TypeScript review interface and rollback to a known prior model/prompt. No MCP, JavaScript UI or Azure deployment is claimed complete.
References checked31October2026: https://www.mishcon.com/news/mishcon-de-reya-and-legora-announce-strategic-partnership ; https://www.mishcon.com/news/from-ai-ambition-to-accountability-five-priorities-for-boards-and-leadership-teams ; https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search ; https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices ; https://docs.python.org/3/library/unittest.html . Local simulation is not vendor product validation.
