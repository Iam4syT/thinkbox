# REST integration and operational handover lab

## A Outcome
Build and explain a small synthetic request API with a database, token checks and safe retry behaviour, then document what another engineer needs to operate it. REST is an HTTP interface between systems. Idempotency means repeating the same request does not create another record.

## B Research basis and scope
The Solirius DevOps Hack Day article, dated 1 October 2026, describes engineers building and testing solutions together: https://www.solirius.com/post/solirius-reply-devops-hack-day . The architecture role also covers APIs, databases, integration risks and delivery documentation. The invented service is a learning scenario, not Solirius software or a real client workflow.

## C Role mapping
Practise Python, REST contracts, relational data, integration risks, design trade-offs, Git, test automation, container familiarity and handover. An optional cloud design is a proposal only. This small modular application is not a microservices estate or distributed deployment.

## D Candidate gap
Strengthen Docker, CI/CD evidence, API failure handling and operational design. Existing Python/REST/SQL study and Git use are a foundation. The new automated checks were run during package preparation; they are not a personal independent build or a professional deployment.

## E Recurring value
Client integrations retry requests after a timeout. Duplicate writes or silent conflicting changes can confuse users and support teams. This lab checks a repeated key and rejects incompatible reuse. No real service reliability or user-time improvement has been measured.

## F Architecture and simpler baseline
A local client calls GET or POST /requests on 127.0.0.1. The handler checks X-Lab-Token, limits payload size and calls the shared dispatch function. SQLite stores request_key as a primary key and a category. SQL uses parameters. Only synthetic categories access, mail and other are allowed; names and extra fields are rejected. Keep the token local; it is a learning control, not enterprise identity. Python http.server has basic security only and is not a production server.

Baseline: a manual CSV list or the in-process demo. The HTTP layer teaches integration contracts; it is not needed for a one-person list. AI is unnecessary for these exact rules. Production would need a supported web framework, proper identity, TLS, authorisation, concurrency design, logging, monitoring, backups, retention and operational ownership.

## G Prerequisites and costs
Use Python 3.11 or later with sqlite3, a terminal and a text editor. No pip dependency is required. curl is useful for HTTP checks. Docker is optional; check licensing for your environment. The CLI costs no cloud/API money. Do not enter real identifiers or credentials. Plan two to four study sessions; actual learner duration is unknown.

## H Step by step

### 1 Open the source
From a fresh thinkbox clone open Software Development/Architecture-Delivery-Workbench/handover. Run python3 --version and check main.py, tests/test_main.py and Dockerfile exist. If Python lacks sqlite3, use a supported Python distribution; do not replace persistence with a dummy success response.

### 2 Read the contract
Read dispatch in main.py. POST /requests accepts exactly request_key and category. Successful first creation returns 201; replay returns 200; different content with the same key returns 409; a wrong token returns 401. Write these states in docs/contract.md. Verify each is a distinct expectation before running code.

### 3 Run the offline baseline
Run python3 main.py demo. Expect status codes 401, 201, 200 and then 200 for the list. The demo uses an in-memory database and prints only synthetic values. Check that the repeated request reports replayed true. If the result differs, save the output and compare the body and key; do not assume a printed status proves network behaviour.

### 4 Run logic and storage checks
Run python3 -B -m unittest discover -s tests -v. Expect 14 tests, OK, including unauthorised no-write, persistence and conflicting key reuse. These tests call dispatch directly. They do not test HTTP parsing, TLS, concurrency or a live integration. Diagnose any failure from the assertion and rerun after a scoped fix.

### 5 Start a local HTTP session
In one terminal set HANDOVER_TOKEN to a throwaway local training string: export HANDOVER_TOKEN=replace-with-local-training-value . Then run python3 main.py serve --db lab.sqlite --port 8765. Expect a loopback URL. The process stays open. If binding is prohibited by the environment, record HTTP unrun and use the offline demo; never label that as a transport pass. If the port is occupied, choose another local port and update the following URL.

### 6 Prove an unauthorised call writes nothing
In a second terminal run curl -i -H 'X-Lab-Token: wrong' http://127.0.0.1:8765/requests . Expect HTTP 401. Then use the throwaway configured token and GET the same path; expect an empty requests list on a fresh database. If there are old rows, use a new training database filename rather than deleting evidence. Do not expose this server to the internet.

### 7 Create and retry
Run curl -i -X POST -H 'Content-Type: application/json' -H 'X-Lab-Token: replace-with-local-training-value' -d '{"request_key":"practice-1","category":"access"}' http://127.0.0.1:8765/requests . Expect 201. Repeat the identical command; expect 200 and replayed true. GET the list and confirm one practice-1 row. If duplicate rows appear, stop and inspect uniqueness and transaction handling.

### 8 Exercise a conflicting retry
Repeat the POST with practice-1 but category mail. Expect 409 and the original row unchanged. GET again to verify access remains. Recovery is a deliberate new request key after reviewing the business intent, not silently overwriting the original. Document this choice in docs/decision.md.

### 9 Check invalid input
Send malformed JSON, an extra field, or an unsupported category in separate synthetic requests. Expect 400. The HTTP handler rejects an excessive Content-Length and non-JSON POST media type. Capture actual responses if your environment permits HTTP. Do not claim these transport checks passed from the direct-function tests alone.

### 10 Draw the service
In Draw.io create a client, loopback HTTP boundary, handler, dispatch module and SQLite store. Label the token check, data fields and response codes. Mark the single-process design and untested network layer. Add a failure note for database contention and a future migration option to a managed database. A diagram must match the implementation, not the hoped-for cloud version.

### 11 Explore a container and CI
Optional: if Docker is installed and permitted, run docker build -t architecture-handover-lab . then docker run --rm architecture-handover-lab . Expect the same offline demo codes. The supplied image runs the demo, not a public server. Run docker run --rm architecture-handover-lab python -m unittest discover -s tests -v for the checks. Image build/pull and Docker execution are unrun in this package's environment. For CI, add a path-filtered workflow at repository-root .github/workflows only in your own authorised checkout; run tests from this project's directory. No active workflow is installed by this lab. Record the actual workflow URL before claiming CI execution.

### 12 Handover and cleanup
Write docs/runbook.md with start command, token handling, contract, known failures, backup/restore plan and owner. Stop the local server with Ctrl-C before touching its file. Copy lab.sqlite to a private local backup and verify a row count from the copy using sqlite3 or a small Python query. Delete only lab.sqlite and that synthetic backup when no longer needed. Unset HANDOVER_TOKEN. Docker users may remove the named lab image; do not prune other images or volumes. Keep source and test evidence.

## I Break and fix
Start without HANDOVER_TOKEN: expect startup refusal, then set a throwaway value and retry. Reuse a key with different content: expect 409, explain why a retry cannot silently change intent, then use a reviewed new key. Use a read-only or unavailable database location only in a disposable copy: record the failure, restore a writable local path and rerun. No automated failover is implemented.

## J Acceptance and actual evaluation
The 14 direct-function/storage tests passed locally on 2 November 2026. The normal demo produces 401, 201, 200, 200. HTTP integration was attempted but socket binding was denied with Operation not permitted; transport remains unrun. Docker was unavailable and CI was not executed. Personal learner execution, diagrams and restore evidence are pending. Production security, load, concurrent writers and external deployment are not proven.

## K Evidence
Keep contract.md, decision.md, runbook.md, editable/exported diagram, source diff, test logs, normal/failure responses and environment/revision. Keep databases and tokens out of Git. This package contains no real requests, names or secrets.

## L Interview story
Explain request duplication, the database-key decision, token boundary, failed conflicting retry, verification and operational limits. Show a personal code change and a meaningful failing-then-passing test. Describe expected value separately from actual local results.

## M Conditional wording
Only after personal completion and evidence: Built a synthetic Python and SQLite integration lab, checked authenticated request handling and retry behaviour, and documented failure recovery and production gaps. Do not claim HTTP, Docker, CI, cloud deployment or independent production operation unless separately run and evidenced.

## N Extension and authoritative references
Propose an Azure-hosted version with managed identity, a production web framework and managed database; include deployment, monitoring, recovery and cost assumptions, without provisioning. Compare that with the simpler single-service design before choosing microservices. References checked 2 November 2026: Python sqlite3 https://docs.python.org/3.11/library/sqlite3.html ; Python HTTP server limits https://docs.python.org/3.11/library/http.server.html ; Docker Python guide https://docs.docker.com/guides/python/ . AI is an optional explanation aid, not an authorisation or write decision maker.
