# Evaluation scope

The harness succeeds only when all three intentionally bad fixtures report drift. A clean script exit is not a live tenant assessment.

Commands and outcomes are recorded in the root docs/verification.json after the verification pass.

Scope limit: No Microsoft Graph connection or automated remediation. Exit 1 is expected for the supplied non-compliant fixtures.

See [repository verification](../../docs/VERIFICATION.md) for actual command results, environment and date. An installed dependency or successful syntax check alone is not an end-to-end test. Live services not exercised remain unverified.
