# Evaluation scope

Health and mocked contract tests need no key. A real audit request needs configured OpenAI/Azure access and may incur costs; it is outside the offline lab. Evaluation cases live in docs/evaluation-cases.json.

Commands and outcomes are recorded in the root docs/verification.json after the verification pass.

Scope limit: No legal/regulatory certification or automatic approval. Local tests mock the provider; live model false-approval and false-rejection rates remain unmeasured.

See [repository verification](../../docs/VERIFICATION.md) for actual command results, environment and date. An installed dependency or successful syntax check alone is not an end-to-end test. Live services not exercised remain unverified.
