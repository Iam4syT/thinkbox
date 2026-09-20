# Evaluation scope

Default mode uses fixtures. Existing labels require review; replacement is a separate explicit option. Live writes require delegated access, selected group IDs and -Apply.

Commands and outcomes are recorded in the root docs/verification.json after the verification pass.

Scope limit: Live Graph operations are implemented but have not been tenant-tested. Fixtures do not establish tenant security or regulatory compliance.

See [repository verification](../../docs/VERIFICATION.md) for actual command results, environment and date. An installed dependency or successful syntax check alone is not an end-to-end test. Live services not exercised remain unverified.

The additional Test-ChangeGuards.ps1 harness passed on 20 September 2026. It replaces all Graph functions with local mocks to verify scope, WhatIf, concurrency, backup-before-write, deduplication, read-back, idempotence and guarded restore. These are behavioural tests, not a live Graph permission or tenant test.
