# Discovery and solution design lab

## A Outcome
Turn a synthetic service request into a traceable design discussion, with requirement owners, acceptance checks, open questions and an architecture decision record. An architecture decision record explains a choice, its reasons and its limits.

## B Research basis and scope
Solirius describes business-first data modelling and documentation in its HMCTS article dated 18 August 2026: https://www.solirius.com/post/supporting-digital-transformation-through-data-architecture-at-hmcts . This lab uses that general learning pattern. The service, data and proposed design below are invented for training; they do not reproduce HMCTS systems or establish a real client need.

## C Role mapping
Practise discovery, requirement translation, diagrams, solution proposals, technical risk identification and presenting trade-offs to a senior architect. Match the output to technical assessments and planning, rather than treating a technology list as an architecture.

## D Candidate gap
This develops formal discovery artefacts, diagramming and evidence-led estimates. Existing support communication and early-stage proposals provide a foundation. Completing the guide would not establish production architecture ownership.

## E Recurring value
A consultant repeats discovery at project start and whenever a requirement changes. Missing owners, acceptance rules or data-handling decisions create uncertainty for developers and support teams. The checklist makes those omissions visible. No time or defect reduction has been measured.

## F Architecture and baseline
A local Python command reads data/brief.json, validates a small checklist and prints Markdown. A human reviews the output. There is no network, model, cloud account or real user data. Begin with a spreadsheet/manual checklist as the simpler baseline. Code provides repeatable checks; AI adds no established value to these explicit rules. An optional future summariser must never approve requirements.

Draw a context diagram in Draw.io: Example service owner -> discovery tool -> review report -> architect. Draw a container view with input JSON, Python checker and Markdown output. Mark the local computer boundary and label all information synthetic. The diagram is a learning task until personally created and reviewed.

## G Prerequisites and cost
Use a spare local folder, Python 3.11 or later and a text editor. No pip packages are required. Git is useful for keeping revisions. Draw.io web or desktop is optional for the diagram; check its terms before use. Use only synthetic data. The local CLI has no cloud/API charge. Time plan: two 90-minute sessions plus review, not measured completion time. Windows users can replace python3 with py -3 and use File Explorer instead of Unix commands.

## H Step by step

### 1 Open the project
Starting state: source files are available in discovery/. Open Terminal in that folder and run python3 --version, then list the files. Expect main.py, data/brief.json and tests/test_main.py. Check that the Python version is at least 3.11. If files are missing, recover the package; do not create empty replacements. From a fresh clone use git clone https://github.com/Iam4syT/thinkbox.git and open Software Development/Architecture-Delivery-Workbench/discovery.

### 2 Understand the example need
Open data/brief.json in a text editor. Read R1, R2 and R3, their owners, needs and acceptance checks. They describe recording a request once, rejecting unauthorised writes and retaining open constraints. Explain each in one sentence. If you cannot explain a field, write it as a workshop question before choosing technology.

### 3 Establish a manual baseline
Without running code, inspect the four top-level constraint fields and all three requirement records. Write a short baseline.md saying which decisions are complete and which still require a person's approval. Expect no blanks in the supplied fixture. Verify that a completed checklist does not imply production readiness. There is no measured time comparison; do not invent one.

### 4 Run the normal path
Run python3 main.py data/brief.json. Expect Status: checklist complete; human approval still required and three traceability lines. Read the output, not only the exit code. If JSON parsing fails, check commas, quotes and brackets against the untouched original.

### 5 Save a review artefact
Run python3 main.py data/brief.json > review.md. Open review.md and compare every requirement ID, owner and check with the input. Expect all three to appear. If output differs, confirm your working folder and input file, then rerun. Keep review.md as a generated artefact and brief.json as the source.

### 6 Find a real omission safely
Copy brief.json to a new local file named incomplete.json in the same data folder. Remove the owner from R2 and set retention_days to null. Run python3 main.py data/incomplete.json. Expect R2: missing owner and Unresolved retention_days. Verify both, then restore the owner and a justified training retention value. Rerun to confirm the warnings clear. A value is not approved simply because the code accepts it.

### 7 Make the design explainable
Create docs/decision.md. Compare a manual spreadsheet, a single service with relational storage, and multiple services. Use the same attributes: user need, ownership, deployment complexity, security and failure recovery. For this small training workload, propose a single service and explain why separate deployment is not yet justified. State what evidence would change that choice. Ask a reviewer to challenge one assumption.

### 8 Draw and check the boundaries
Create the context and container diagrams described above. Save editable .drawio files and exported PNGs under docs/. Add arrow labels such as synthetic requirements and review output. Check that no diagram claims cloud hosting or an authentication service that the code lacks. If a reviewer cannot trace one input to one output, simplify the diagram and retry.

### 9 Estimate without false precision
Create docs/estimate.md. Break the next build into input validation, persistence, API contract, tests, diagrams and review. Give ranges and list assumptions rather than a promised delivery date. Record dependencies such as review time and test access. Check estimates with a senior reviewer; the tool does not calculate effort or commercial costs.

### 10 Run acceptance tests
Run python3 -B -m unittest discover -s tests -v. Expect 10 tests, OK. A failure identifies a behaviour to investigate. Compare the failing assertion with main.py, fix only the relevant cause and rerun. Do not delete a test or weaken its assertion to obtain a pass.

### 11 Review and version
Compare baseline.md with review.md, decision.md, estimate.md and the diagrams. All R1-R3 items must connect to a check or open question. Run git diff before committing your own changes in a personal checkout. Record which files you personally changed and what a reviewer challenged. Publish no real client information.

### 12 Cleanup
Keep source, tests, decisions and selected synthetic evidence. Delete only your generated review.md and incomplete.json if no longer needed. There is no cloud resource or account to tear down. Keep a copy of the original brief before removing experiment files.

## I Break and fix
Duplicate R1 in a copied input: expect the program to stop with requirement IDs must be nonempty and unique. Give the copied item a distinct justified ID, then rerun. Remove acceptance from R3: expect a missing acceptance warning. Restore a measurable check. In both cases capture the failed and corrected outputs and explain why the omission matters to a delivery team.

## J Acceptance and actual evaluation
Acceptance: all IDs traceable; missing owners/constraints visible; duplicates rejected; human approval retained; two diagrams and a challenged decision documented. Automated evaluation on 2 November 2026 passed 10 local tests. Personal diagrams, workshop review and estimates have not been performed by the learner. This is checklist testing, not proof of design quality or production assurance.

## K Portfolio artefacts
Keep the synthetic input, review.md, baseline.md, docs/decision.md, docs/estimate.md, editable/exported diagrams, test output and a short demo. Record source revision and runtime. Screenshots are optional and must contain no private data. Public files include README.md, LAB.md, EVALUATION.md and CHANGELOG.md.

## L Interview story
Explain the missing information first, then the simpler options, chosen boundary, failure injection, check and remaining review. Show one actual personal edit and one failed-then-passed run. Describe expected business value as a hypothesis until real use is measured.

## M Wording only after personal completion
Use only after you have personally completed and evidenced the tasks: Built a synthetic discovery checklist and documented a small service design, tracing requirements to acceptance tests and recording unresolved decisions for review. Do not add this to an application as completed personal experience beforehand.

## N Extension
Compare the diagram with an Azure App Service plus managed database proposal. Identify identity, backup, monitoring, residency and cost assumptions using official Azure architecture guidance: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/ . Do not create paid resources. An AI summarisation experiment is optional; compare factual omissions against the deterministic baseline and keep approval human.
