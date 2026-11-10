# Lab 2 — Teams and SharePoint pilot handover

## A. The need and why it repeats
Keep a Teams and SharePoint collaboration pilot from expanding before access and handover checks are evidenced. Repeat use: Every team rollout, access review or collaboration service change. This is a general engineering scenario, inferred from common workplace change needs. The actual organisation's process may differ.

## B. Skills shown and gaps
The exercise covers baseline, pilot, checks, rollback and handover. Live Microsoft 365 administration, external provider coordination and formal sign-off require separate evidence. Use these checks: baseline, allowed_access, denied_access, sharing, sync, rollback, handover.

## C. Design and baseline
The operator records observations in JSON, Python checks completeness, then a human reviewer makes the change decision. A paper checklist is a viable baseline. The script applies the same rule consistently and shows missing items. An AI model could draft a summary after redaction. It could also misread a log, so the decision uses the fixed checks only.

## D. Prepare safely
Allow 30–45 minutes for the local run. Use Python 3 and a terminal. No packages, tenant licence, credentials or spend are needed locally. The optional native exercise needs an approved sandbox, the relevant Microsoft 365 service licences, approved test identities and a reviewer. Confirm access and costs before using any cloud resources.

## E. Run the baseline
Open a terminal in this solution's public folder. Check that python3 --version returns Python 3. Run python3 -B Scripts/review.py Configuration/ready.json. Expect READY_FOR_REVIEW and every check pass. If the file is missing, list Configuration and check the working directory. Keep the output as a baseline.

## F. Break the process safely
Run python3 -B Scripts/review.py Configuration/hold.json. Expect HOLD with both a missing and a failed check. Duplicate hold.json as trial.json and edit the copy in a plain-text editor. Restore one missing check using a recorded synthetic observation. Run against trial.json and expect HOLD until the failed check also has a passing observation. Try a typo in a check name and expect exit code 2 with an input error. Compare the output with the supplied evidence folder.

## G. Optional Microsoft 365 exercise
A workplace engineer, pilot group and service desk agree who should have access and who takes support after launch. In an authorised sandbox only, create a private pilot Team and open the channel’s Shared tab and use Open in SharePoint where available. Create synthetic content. Test approved member access and attempt the same link with a separate account outside the group. Check sharing policy and try OneDrive sync on an authorised test device. Record the pilot group, test account roles, expected access, observed results and support owner. The native stage remains unrun. Do not connect the local script to a tenant or use real user data in the fixture.

## H. Recovery and handover
If an excluded account can open the file, pause the rollout. Check the link type, existing direct grants and group membership. Use a clean test session and recheck after approved correction. Revert only the scoped pilot permission or link using the agreed baseline. Record the fault, last good state, affected users, observed result, next action and owner. The human reviewer approves recovery or rollout separately.

## I. Acceptance tests
Run python3 -B -m unittest discover -s tests -v. Seven local methods should pass. One missing excluded-user test keeps the gate on HOLD. After proving the excluded test user is denied and the pilot user still has access, rerun and expect READY_FOR_REVIEW. A failed handover check holds the rollout. A human reviews the underlying evidence before approval. Local tests cannot establish actual service health or permission.

## J. Cleanup
Remove your trial.json copy after saving anonymised observations. Remove test links, test content and temporary memberships from the authorised sandbox after sign-off. Retain only redacted evidence according to policy.

## K. Evidence and limits
Keep the two input fixtures, two decisions, test output and a short note on an unseen fault. Seven local tests and two command-line fixture runs passed. Candidate execution and native checks remain pending.

## L. Interview walkthrough
Explain what the excluded-user test proves, which cases it leaves open and how the service desk would take over. Explain the difference between a script outcome and approval to change a service.

## M. Conditional portfolio wording
After independently reproducing the result: “Tested a synthetic teams and sharepoint pilot handover checklist, including a missing-check failure and a handover decision.” Add only the checks personally run. If shared later, label it an independent practice lab.

## N. Extend only after the baseline
Extend the test matrix to approved guests, with a separately authorised sandbox policy and separate identities. Compare the result with the manual checklist and report disagreements. Keep customer information and credentials out of the repository.
