# Local prediction API with validation and failure checks

## A Outcome
Serve the synthetic model through a small HTTP interface, reject invalid requests and count response statuses without logging raw query data.
## B Research basis
The graduate role includes API work, deployment assistance and monitoring. This is a plausible recurring developer task. The unnamed start-up's product, stack and production design are unknown. This learning server does not recreate them.
## C Requirements exercised
Backend/API practice, software testing, failure handling, monitoring basics and privacy-aware operational notes (E3–E6,R3–R5,R7,R8,D4). Not a production cloud deployment.
## D Gap addressed
Practise the move from model calculation to an interface with repeatable normal/failure tests. Existing Python/REST study supports entry; live production ownership and robust service security remain unestablished.
## E Recurring value
Each model-service change needs predictable input/output and a clear failure response. Status counts help a developer notice errors. No actual user adoption or uptime gain measured.
## F Architecture and simpler alternative
Local HTTP client ->127.0.0.1 loopback server -> strict query validation -> versioned synthetic model coefficients -> JSON response; only aggregate status counts remain in memory. No identity provider, cloud, authentication, TLS or durable telemetry. Python http.server is explicitly not recommended for production. A CLI calculation is simpler and preferable for a single user; HTTP earns its place only to practise integration. No generative AI needed for deterministic prediction/validation.
## G Environment
Status: locally implemented learning demo. Guides and implementation prepared with AI assistance; the private evidence record separates implementation tests from Bunamin's own execution and explanation. No client work, live system or production outcome. Python 3.11 standard library only; no cloud account, paid API, licence purchase or external dataset. Budget £0 excluding existing device/internet; estimated learner time one focused weekend per lab, not a measured duration. Use only synthetic data. Do not enter personal/client information. Intended for individual learning on an isolated machine.

## H Implementation and walkthrough
Step 1 Starting state: prediction-service folder downloaded. Open terminal there; run `python3 --version` and `ls`. Expected Python 3.11, main.py, model and tests. If missing, fix path/runtime. No credentials, packages or Docker installation required. Use a second terminal for requests.

Step 2 Open model/model.json. Expected version demo-v1, slope 2, intercept 10, scope synthetic_local_only. Compare coefficients with lab 1 normal result. They are a supplied fixed teaching artefact, not an automatically approved model release. Do not load arbitrary downloaded model files. If version/schema differs, retain the original and investigate before starting.

Step 3 Run `python3 -B main.py --port 8765`. Expected message Synthetic loopback demo only. Keep the terminal open. If address is in use, stop your own earlier instance with Ctrl-C or use8766 and change the following URLs consistently. Do not bind to0.0.0.0 or expose this service outside your device.

Step 4 In the other terminal run `curl -i http://127.0.0.1:8765/health`. Expected HTTP200 and JSON status ok, version demo-v1. If curl is unavailable, visit the URL in your browser. Connection refused means check process/port; a404 means check path spelling. No application credentials are involved.

Step 5 Run `curl -i 'http://127.0.0.1:8765/predict?x=3'`. Expected HTTP200, prediction16, version demo-v1 and synthetic scope. Quotes keep the query intact. Compare16 with2×3+10. If mismatched, inspect model version and coefficients; do not adjust expected output merely to hide the difference.

Step 6 Run `curl -i 'http://127.0.0.1:8765/predict?x=nan'`. Expected HTTP400 and error invalid input without echoing the raw value. Repeat x=-1 and x=101. Expected 400. These range limits are synthetic teaching rules. If any succeeds, stop and inspect validation before continuing.

Step 7 Run `curl -i 'http://127.0.0.1:8765/predict?x=1&x=2'`. Expected 400 because a single value is required. Try an extra parameter such as q=test; expect400. Visit /admin; expect404. No real personal data should be used to test redaction.

Step 8 Stop the server with Ctrl-C. Expected aggregate request_status_counts with200,400 and404 keys for statuses actually exercised. Check that query values are absent. These are in-memory counts, not durable monitoring or a service-level agreement. If nothing prints, check how the process was stopped and preserve the observation.

Step 9 Run `python3 -B -m unittest discover -s tests -v`. Expected 20 methods on a socket-permitted machine:10 offline contract tests plus10 HTTP integration tests. If bind permission is blocked, only10 offline tests pass and the integration class is skipped; that is not an HTTP pass. HTTP tests start a real loopback server on an operating-system-assigned free port and close it afterwards. They check normal response, health, unknown route, invalid range, missing/duplicate fields, no echo, binding, model schema, status counts and bad coefficient. On failure, inspect error and rerun exact case; do not remove assertions. If local sockets are blocked, record that integration tests were not run and use pure predict/load checks separately.

Step 10 Copy the model into a scratch file and set version unknown. Run `python3 -B main.py --model model/bad.json` only after saving that copy as model/bad.json. Expected fail before listening. Restore/delete the scratch file, restart using original and recheck health/prediction. Preserve failure and recovery output. Rollback here means restoring the known model and restarting, not blue/green infrastructure.

Step 11 Read the source with a reviewer. Explain query validation, model loading, non-finite checks, generic errors and the absence of raw request logging. Identify production needs: proper serving platform, authentication/TLS, request/body/rate limits, structured logs, concurrency-aware metrics, model provenance, secrets handling, robust rollback and authorised deployment. These are not implemented by this lab.

Step 12 Record your own small change and tests, for example a reviewed new valid range with an explicit expected rejection outside it. Run the full suite, restore the original range if it was only an exercise, then rerun. Save a diff and demonstrate one unseen bad request before claiming personal completion.
## I Break/fix
Occupied port: choose another loopback port and retest URLs. Wrong version: reject before bind, restore known artefact. NaN/duplicate input: return400 without internal details; fix validation only if broken. Unknown path:404, do not expose arbitrary files. Stop/restart: counts reset; document this telemetry limitation.
## J Acceptance
Both success endpoints behave, invalid requests rejected, no input echoed, only loopback binding, wrong model refused, all 20 tests pass on a socket-permitted machine and socket/process closes. This proves a local learning interface only. Cloud/container/performance/load/security certification steps remain unrun.
## K Artefacts and cleanup
Keep source/tests/model version, command notes, normal/failure JSON, own diff and operational handover. Stop server with Ctrl-C, delete scratch bad.json and temporary outputs only after retaining useful evidence. Tests close their ephemeral server. No cloud resources to remove.
## L Interview story
Problem integrating a model; constraints synthetic data/local-only; design explicit schema and version; build HTTP adapter; failure invalid input/model; verification real loopback tests; intended benefit predictable handover; next step reviewed production service. Say exactly which parts you personally changed and ran.
## M Conditional wording
Use only after personally completed/evidenced: Built and tested a local Python prediction API with input validation, model-version checks and aggregate status counts. No claim of cloud deployment, production scaling or customer users.
## N Extension
Use a production serving framework and container only with pinned dependencies, tests, access review, budget and authorised deployment target. Add durable metrics and integration CI. Planned only; this lab does not prove Docker or Azure delivery.
## Sources
https://docs.python.org/3.11/library/http.server.html and https://docs.python.org/3.11/library/unittest.html, read2 November 2026. The HTTP source explicitly warns against production use; preserve that boundary.
