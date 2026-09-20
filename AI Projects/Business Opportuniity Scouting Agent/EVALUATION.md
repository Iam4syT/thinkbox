# Evaluation scope

Tests cover malformed results, missing pages and separation of hostile page text from trusted instructions. They do not establish immunity to prompt injection. Live workbook processing requires permitted URLs and a model key.

Commands and outcomes are recorded in the root docs/verification.json after the verification pass.

Scope limit: Fetch-and-prompt workflow, not indexed RAG or an autonomous strategy engine. Proposed objectives and targets are drafts, not achieved business results.

See [repository verification](../../docs/VERIFICATION.md) for actual command results, environment and date. An installed dependency or successful syntax check alone is not an end-to-end test. Live services not exercised remain unverified.
