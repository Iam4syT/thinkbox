# Lab 1 — Exchange mail change readiness

## A. The need and why it repeats
Avoid switching mail routing before DNS and message delivery checks are evidenced. Repeat use: Every domain onboarding, connector change or authentication review. This is a general engineering scenario, inferred from common workplace change needs. The actual organisation's process may differ.

## B. Skills shown and gaps
The exercise covers baseline, pilot, checks, rollback and handover. Live Microsoft 365 administration, external provider coordination and formal sign-off require separate evidence. Use these checks: baseline, mx, spf, dkim, dmarc, inbound, outbound, rollback.

## C. Design and baseline
The operator records observations in JSON, Python checks completeness, then a human reviewer makes the change decision. A paper checklist is a viable baseline. The script applies the same rule consistently and shows missing items. An AI model could draft a summary after redaction. It could also misread a log, so the decision uses the fixed checks only.

## D. Prepare safely
Allow 30–45 minutes for the local run. Use Python 3 and a terminal. No packages, tenant licence, credentials or spend are needed locally. The optional native exercise needs an approved sandbox, the relevant Microsoft 365 service licences, approved test identities and a reviewer. Confirm access and costs before using any cloud resources.

## E. Run the baseline
Open a terminal in this solution's public folder. Check that python3 --version returns Python 3. Run python3 -B Scripts/review.py Configuration/ready.json. Expect READY_FOR_REVIEW and every check pass. If the file is missing, list Configuration and check the working directory. Keep the output as a baseline.

## F. Break the process safely
Run python3 -B Scripts/review.py Configuration/hold.json. Expect HOLD with both a missing and a failed check. Duplicate hold.json as trial.json and edit the copy in a plain-text editor. Restore one missing check using a recorded synthetic observation. Run against trial.json and expect HOLD until the failed check also has a passing observation. Try a typo in a check name and expect exit code 2 with an input error. Compare the output with the supplied evidence folder.

## G. Optional Microsoft 365 exercise
An Exchange Online engineer and domain administrator agree on expected records and collect controlled send and receive tests. Use Exchange Admin Center → Mail flow → Message trace to look up a test message by sender and recipient. Capture the UTC time and delivery result. Compare MX with the agreed route and check SPF, DKIM and DMARC against the change plan. For a gateway setup, a non-Microsoft MX may be intentional. Check both directions with authorised test mailboxes. Review actual headers for authentication and alignment. The native stage remains unrun. Do not connect the local script to a tenant or use real user data in the fixture.

## H. Recovery and handover
If inbound fails, check the expected MX route and trace results before assuming the mail never arrived. If authentication fails, check selector, policy and alignment separately. Keep the approved pre-change settings and named rollback owner. Record the fault, last good state, affected users, observed result, next action and owner. The human reviewer approves recovery or rollout separately.

## I. Acceptance tests
Run python3 -B -m unittest discover -s tests -v. Seven local methods should pass. One missing outbound result keeps the gate on HOLD. After new evidence confirms outbound delivery, rerun and expect READY_FOR_REVIEW. A failed DKIM result still keeps the gate on HOLD. A human reviews the underlying evidence before approval. Local tests cannot establish actual service health or permission.

## J. Cleanup
Remove your trial.json copy after saving anonymised observations. Remove only temporary authorised test messages, redact identifying headers and keep the signed change record according to policy. Never edit live DNS during this lab.

## K. Evidence and limits
Keep the two input fixtures, two decisions, test output and a short note on an unseen fault. Seven local tests and two command-line fixture runs passed. Candidate execution and native checks remain pending.

## L. Interview walkthrough
Walk through the first missing check, explain why it cannot pass on assumption, and identify who would decide on rollback. Explain the difference between a script outcome and approval to change a service.

## M. Conditional portfolio wording
After independently reproducing the result: “Tested a synthetic exchange mail change readiness checklist, including a missing-check failure and a handover decision.” Add only the checks personally run. If shared later, label it an independent practice lab.

## N. Extend only after the baseline
Model separate inbound and outbound checks for an intentional third-party gateway. Compare the result with the manual checklist and report disagreements. Keep customer information and credentials out of the repository.
