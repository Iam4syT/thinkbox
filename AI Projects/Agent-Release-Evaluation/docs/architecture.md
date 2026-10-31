 Architecture and baseline
Synthetic JSON traces → strict parser/type checks → allowed tools/source scope → review/quality/latency/token rules → HOLD or READY_FOR_REVIEW. Caller-supplied quality is a fixture; no judge model, human identity verification or tool execution occurs.
Use the deterministic baseline first. Generative AI may help propose summaries or analyse complex failure patterns, but it adds cost and failure modes. Compare on the same held-out cases before choosing it. A simple rules/search solution may be sufficient.
