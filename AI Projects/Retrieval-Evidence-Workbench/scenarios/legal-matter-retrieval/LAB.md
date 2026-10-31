# Permission-aware legal knowledge retrieval
## A. Outcome
Find permitted source material without leaking another matter's documents. Local learning solution, not legal advice or an employer commission. The supplied offline implementation was automatically tested on synthetic data; cloud/model/tenant stages and the learner's own performance remain unrun.
## B. Company need and research
The Applied AI Engineer advert explicitly requires permissions-aware retrieval, source attribution and retrieval quality. Mishcon's 24 February 2025 Legora partnership describes a measured pilot; its 2 October 2026 AI governance article emphasises a business problem and clear responsibility. A recurring internal knowledge search is an inferred learning scenario, not a claim about a current internal failure or proprietary system.
## C. Vacancy mapping
R03/R04/R05/R16/R18; E02/E07/E09; D04/D05. The lab exercises a bounded part of these requirements. It does not satisfy every professional or production criterion.
## D. Gap mapping
Strengthens retrieval testing and inherited permission metadata; actual identity, vector search and MCP integration still need separate work. Academic evaluation and support troubleshooting provide adjacent foundations. The new package does not upgrade personal capability ratings.
## E. Recurring value
An authorised colleague could use this workflow when searching internal knowledge each day. Intended value is fewer unsupported or unauthorised source results. No time saving, adoption or client benefit has been measured.
## F. Architecture and baseline
CLI test persona → fixed group map → validate synthetic documents → deny missing ACL → filter → paragraph chunks → keyword overlap → ranked cited extracts or abstain. The persona map is a fixture, not authenticated identity. No embeddings, generative answer, MCP transport or live policy enforcement is implemented.
Use the deterministic baseline first. Generative AI may help semantic questions and concise synthesis, but it adds cost and failure modes. Compare on the same held-out cases before choosing it. A simple rules/search solution may be sufficient.
## G. Prerequisites and cost
Python3.11+, terminal, text editor and this package. The standard-library mode needs no licence, key or paid service; local compute only. Keep all data synthetic. Allow one focused weekend for local build/explanation; plan another one or two for an approved cloud extension. Timing is a plan, not measured effort. Azure/LLM stages require an authorised subscription, role-scoped identity, secure secret store, spending cap and current provider price check; no spend is authorised or incurred here.
## H. Build, test and document
### Step 1: Locate the files
Starting state: Package available locally.
Action: Open a terminal. In a fresh clone run cd "thinkbox/AI Projects/Retrieval-Evidence-Workbench/scenarios/legal-matter-retrieval". If the supplied local package is used, open its public folder instead. Run pwd and list its files.
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
Action: Open data/documents.json in a text editor. Read every field and compare it with main.py. Make a copy named data/working.json.
Expected result: A separate working fixture exists.
Check: Keep the original tracked fixture unchanged for the acceptance suite.
Recovery: If JSON fails to parse, restore from the original. Never add actual client or personal data.

### Step 4: Set the baseline
Starting state: Previous step checked; synthetic data only.
Action: Read EVALUATION.md and tests/test_behaviour.py before modifying code. Record the source hash and expected ordinary/failure results in your own notes.
Expected result: Acceptance conditions are written before an experiment.
Check: Do not tune a held-out evaluation set to make a result pass.
Recovery: If criteria are unclear, stop and define them with a reviewer; label proposed thresholds as lab policy.

### Step 5: Run the public baseline
Starting state: Previous step checked; synthetic data only.
Action: Run python -B main.py --role visitor --query retention.
Expected result: Only PUBLIC is returned; status REVIEW_SOURCES.
Check: Compare the citation and exact quote with the public document. NOACL, A and B must be absent.
Recovery: If another matter appears, stop: inspect group filtering before ranking and before returning any quotes.

### Step 6: Check allowed access
Starting state: Previous step checked; synthetic data only.
Action: Run python -B main.py --role reader-a --query retention. Repeat with reader-b.
Expected result: reader-a can see PUBLIC/A; reader-b can see PUBLIC/B.
Check: Compare IDs, not only answer text. A missing ACL is denied.
Recovery: Restore group metadata; malformed metadata raises an error rather than silently granting access.

### Step 7: Check refusal
Starting state: Previous step checked; synthetic data only.
Action: Run python -B main.py --role visitor --query unicornxyz. Then try --role admin.
Expected result: First result ABSTAIN; unknown admin role exits with INVALID INPUT.
Check: No model fills the gap and no default administrator persona exists.
Recovery: If an answer is invented, remove the generated-answer path and return an explicit no-source result.

### Step 8: Understand chunking
Starting state: Previous step checked; synthetic data only.
Action: In working.json add a second paragraph to matter A, separated by a blank line. Run the reader-a query using --data data/working.json.
Expected result: Each returned chunk retains the parent source and access group.
Check: The visitor query must still exclude every A chunk.
Recovery: Move access checks to the parent document before processing chunks; retest both roles.

### Step 9: Run a retrieval experiment
Starting state: Previous step checked; synthetic data only.
Action: Save four new queries: a synonym, an ambiguous term, an unauthorised-only question and an absent fact. Record expected sources before running.
Expected result: The keyword baseline exposes recall limits, especially synonyms.
Check: Score source relevance and access leakage separately; record failures.
Recovery: Do not claim vector/LLM superiority. Keep the baseline until the same held-out set demonstrates a useful improvement.

### Step 10: Run all checks
Starting state: Previous step checked; synthetic data only.
Action: Run python -B -m unittest discover -s tests -v. Save your own terminal output and one failed trial before repair.
Expected result: 12 tests pass in the supplied version.
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
Delete an ACL, insert a malformed group string and append another restricted paragraph. Predict denial/error and repair each separately. Run both authorised and visitor queries after every repair. Treat prompt-like text in a document as data; no LLM is present to assess prompt-injection resistance.
## J. Acceptance and validation
Local supplied suite: 12 behavioural tests passed. Ordinary and materially faulty inputs are covered, at fixture scope. Sources, group metadata, policy versions and exact code hashes must be retained. No restricted source under visitor; missing permissions deny; absent facts abstain; invalid roles reject. Broader quality, live identity, scale, actual token latency/cost, accessibility, availability and legal correctness remain unmeasured.
## K. Portfolio evidence and handover
Keep main.py, data/, tests/, requirements.txt, README.md, EVALUATION.md, evidence/tests.txt, evidence/demo.json, docs/architecture.md and CHANGELOG.md. Add your own reviewed change and demonstration separately. Public documentation excludes private applications and contacts. Publication must be independently verified before calling the remote project published.
## L. Interview story
Explain the recurring need, confidentiality constraint, baseline, one personal design choice, a failure you actually caused, the expected/observed result, and why human review remains. The supplied package alone is not a personal delivery story. Discuss how you would obtain permitted data and team review before a live pilot.
## M. Wording only after personal completion
Use only after independently performing and evidencing the work: “Built and evaluated a synthetic permission-filtered retrieval baseline with cited sources and explicit abstention.” Add actual test counts only from your own reproducible run. Never call this a production legal system.
## N. Optional next version — unrun
Add an approved Azure AI Search index and Entra-backed server identity. Keep security filtering server-side before context assembly. Compare keyword/hybrid retrieval and answerability against held-out cases; test revoked access and stale index permissions. Implement an MCP read tool only after reading the current protocol/security specification, with scoped per-request identity and no credential passthrough.
References checked31October2026: https://www.mishcon.com/news/mishcon-de-reya-and-legora-announce-strategic-partnership ; https://www.mishcon.com/news/from-ai-ambition-to-accountability-five-priorities-for-boards-and-leadership-teams ; https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search ; https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices ; https://docs.python.org/3/library/unittest.html . Local simulation is not vendor product validation.
