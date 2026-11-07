# Approval workflow with safe integration failures

## A. Outcome and status
Record a synthetic staff request, require an assigned reviewer, and simulate dispatch without duplicate completion or unsafe retries. A local Python state machine is built. SharePoint, Power Automate, Graph calls and AI summarisation are planned extensions, not working integrations.

## B. Research and employer context
DWP's June 2026 parliamentary answer describes controlled use of AI tools, and the vacancy calls for secure workload orchestration. The recurring request-review scenario is an independent inference about a common workplace need. It does not reproduce DWP's internal process or approve benefits, payments or access for real people.

## C. Role requirements exercised
E1 orchestration, E2 API/JSON concepts and R3 reliability; D5 scripting and D6 test discipline. The local HTTP status inputs are simulated. The unrun extension demonstrates how a SharePoint event could drive a Power Automate approval.

## D. Candidate gap
Support experience helps with diagnosis and escalation. The gap is a precise workflow, connector and validation example, plus reliable handling of retries and approval boundaries. This lab supplies a bounded practice path without claiming production implementation.

## E. Recurring use and baseline
A service team repeatedly reviews small requests. A list and manual approval may already be sufficient. The baseline automates deterministic state handling. An AI-generated request summary is optional; it must not decide approval, choose approvers or authorise dispatch. Keep the rules-only route unless summarisation adds measured value.

## F. Architecture
Local: validated request → pending state → assigned reviewer decision → approved state → injected Graph-like response → complete, retry, blocked or failed. A request key prevents duplicate local completion. Audit records retain event type and status rather than raw request content.
The actor strings are simulation inputs; the local script has no real authentication. Memory is lost between processes. Production needs a durable store with atomic updates, real identities, concurrency controls, a queue/scheduler and monitoring. A recorded delay is not an actual background retry service.
Tenant target: SharePoint test list → Power Automate approval → condition on reviewer outcome → update status and notify a test recipient. An optional connector reads a permitted Graph resource. Never use generated text as permission or a credential.

## G. Prerequisites, budget and boundaries
Local mode needs Python 3.11 or later and a terminal. It uses only the standard library, costs £0 in API usage and requires no credentials. A code editor is helpful. Allow 60–90 minutes for local practice and one to three weekends for the optional tenant work, as a planning estimate rather than measured completion time.
The Microsoft extension needs your own isolated test tenant, test accounts, a maker environment, suitable Microsoft 365/Power Platform entitlements and an administrator-approved licensing check. Trials have limits and may need billing details. Check your tenant's displayed price and capacity before enabling anything paid. This guide does not authorise purchases, tenant changes or access grants. If access is unavailable, stop at the local boundary and record the tenant steps as unrun.
Use fabricated staff information only. Do not use claimant, customer, pupil, health or production records. No benefit entitlement or other decision about a person is made by either project.

## K. Evidence to retain
Keep README, LAB, code, test output, a simple architecture note, one normal run and one failure run. Add a short screen recording when personally reproduced. Record the source version, Python version, date, exact command, result and who performed it. Keep tokens and real account identifiers out of screenshots, logs and commits.

## L. Interview explanation
Explain the recurring user problem, the boundary you chose and why. Show the baseline, one design decision, a failure you diagnosed, the test that proved the local fix and what remains untested. Distinguish your own changes from an assisted implementation. Explain that synthetic test results do not establish real user impact or production readiness.

## H. Granular build and practice
1. Open the scenario folder containing main.py. Run `python3 --version`, then `python3 -m unittest discover -s tests -v`. Expect 12 tests to pass. If imports fail, check the working folder before changing code.
2. Run `python3 main.py`. Expect a complete result and audit events for submitted, approved and complete. These events describe a local simulation; no message or API request is sent.
3. Run `python3 main.py --status-code 403`. Expect blocked. Explain that missing access needs investigation; repeatedly retrying the same forbidden request is not a fix.
4. Run `python3 main.py --status-code 429`. Expect retry and retry_after_seconds set to 5. The script records a scheduling instruction and does not wait or call Graph. Microsoft's guidance uses Retry-After and a fallback backoff when no header is present.
5. Open tests/test_workflow.py. Locate the no-unapproved-write, wrong-approver and rejection checks. Run the tests individually with `python3 -m unittest discover -s tests -p test_workflow.py -v` and read their names/results. Do not add permissions to avoid an expected refusal.
6. Inspect duplicate submission and duplicate dispatch tests. Explain why a retried event should not create a second completed request. Note the boundary: process memory is not a durable guarantee across restarts or concurrent workers.
7. Inspect bounded_retries and malformed_delay. Explain why retries end and why an invalid delay falls back safely. Add your own case for a negative Retry-After value; run the tests and record the result. This new personal action remains pending until you perform it.
8. Copy the source to a temporary practice file. Deliberately allow self-approval in that copy, observe the corresponding test fail, restore the check and rerun. Keep the temporary file out of the public package. Preserve the actual failure/fix notes.
9. Write a short handover: valid states, approval owner, retry limit, blocked-response escalation and a rollback plan. State that no real person receives a notification in local mode.

### Optional Microsoft workflow — not run
10. Confirm a test tenant, maker environment, licences, a SharePoint site and two consenting test users. Verify the approval connector entitlement in your environment. HTTP/custom connectors can need premium licensing; do not assume the standard approval connector covers them.
11. Create a SharePoint list called LabRequests. Add Title (text), RequestKey (text, unique values enforced), RequestSummary (multiple lines), ApprovalStatus (choice: Pending, Approved, Rejected, Complete, Failed) and ReviewerComments (multiple lines). Share only with test users. Treat Created By as the authenticated requester; never trust a requester name typed into a text field.
12. In make.powerautomate.com, choose the lab environment → My flows → New flow → Automated cloud flow. Name it Lab Request Review. Select SharePoint → When an item is created; choose the test site and LabRequests. Save and inspect connection identity. A failing connection needs the appropriate test account, not a broad production administrator credential.
13. Add Approvals → Start and wait for an approval. Choose a single approve/reject reviewer and assign the second test user explicitly. Map the item title, summary and link into the approval. Never let the request body or an AI response supply the reviewer. For a request by the fixed reviewer, stop or route to a separately approved alternate; do not allow self-approval.
14. Add a condition on the approval outcome. In the approval branch, update the original item to Approved and retain reviewer comments; in the rejection branch, set Rejected. Map the original trigger item ID, not a title search that could select the wrong row. Save, create one synthetic request and prove both branches with separate runs.
15. If notification is needed, add a message to an authorised test mailbox/channel after the status update. Record the run ID and confirm the recipient/output. A successful action indicator without the expected recipient result is not enough. Do not use a real team or mailing list for a test.
16. Add failure handling with a separate scope configured to run after the main scope fails or times out. Record a minimal Failed status and a non-sensitive correlation ID. Stop on 401/403 and ask the lab administrator to review the connection. For 429, apply a bounded retry policy consistent with Retry-After. Document what the connector retries automatically before adding another loop.
17. For the optional Graph read, use an administrator-approved delegated test connection and the narrowest supported permission for the specific resource. Select one synthetic list/item and a read-only endpoint from the current Graph documentation. Record endpoint, permission, calling identity, response and 403/429 evidence. This route is not implemented in the supplied Python model, and no token should be stored in the repository.
18. Compare manual review, deterministic automation and optional AI summary on a fixed set of 12 synthetic requests, including missing fields, duplicate key, self-review, rejection and expired approval. Score route correctness, duplicate side effects, privacy and summary accuracy separately. Do not call an AI summary an approved request.
19. Export the solution/configuration without live connections or secrets, record environment variables and test import into another isolated environment when available. A portable export/import and durable-idempotency test are separate acceptance items; no success is claimed here.

## I. Break and fix
Local failures: missing field, requester equals approver, wrong reviewer, dispatch before approval, rejected request, 403, repeated 429 and duplicate dispatch. The tests contain the expected safe outcomes. Tenant failures: expired connection, deleted list item and approval timeout. Preserve the run history, investigate cause, fix only the relevant lab setting and rerun the same case plus a normal request.

## J. Acceptance and cleanup
Local acceptance: all 12 tests pass; no dispatch before approval; rejection blocks dispatch; duplicate completion is suppressed within a single process; 403 blocks; retry attempts stop at the configured bound. No actual HTTP retry or cross-process guarantee is claimed.
Tenant acceptance: both decision branches and failure scope observed, no self-approval, authenticated requester retained, no duplicate side effect under repeated event, read-only Graph proof where added and sanitised export/import evidence. All remain unrun.
Local cleanup: close the Python process; its in-memory state disappears. Remove your temporary practice copy after retaining non-sensitive notes. Tenant cleanup: turn off only this lab flow, close outstanding test approvals, remove synthetic list/items and revoke only the test-specific connections/grants after checking dependencies. Confirm paid capacity/trials separately.

## M. Conditional portfolio wording
After personal reproduction and evidence: “Extended a local approval-workflow model with checks for reviewer identity, duplicate completion, forbidden responses and bounded retries.” Add Power Automate/SharePoint/Graph delivery only after the actual extension is built and validated.

## N. Next version and sources
Use a durable idempotency store and transactional dispatch, then test restart/concurrent-event behaviour. Add AI summaries only with a bounded accuracy/privacy evaluation against the manual baseline.
Microsoft references checked 7 November 2026:
https://learn.microsoft.com/en-us/power-automate/modern-approvals
https://learn.microsoft.com/en-us/graph/throttling
