# Contribution and provenance

## Architecture and engineering

Bunamin Adams designed, implemented, and evaluated this Copilot governance and readiness pipeline. The solution provides a deterministic zero-trust metadata evaluation engine, synthetic tenant data crawler fixtures, simulated prompt safety reporting, and visual telemetry charts.

## Implementation details

- Core policy engine: [core_engine/policy.py](core_engine/policy.py) implements deterministic tri-state access assessment (`allowed`, `exposed`, `review`) with explicit unknown-metadata gating.
- Tenant discovery fixture: [core_engine/tenant_crawler.py](core_engine/tenant_crawler.py) simulates multi-departmental corporate data estates.
- Prompt safety simulation: [core_engine/agent_simulator.py](core_engine/agent_simulator.py) structures remediation findings without live tenant mutation.
- Executive telemetry: [dashboard/analytics_app.py](dashboard/analytics_app.py) renders local compliance visual reporting.
- Evaluation harness: [evaluate.py](evaluate.py) benchmarks 10 hand-labelled test cases with zero policy mismatches.
- Unit tests: [tests/test_policy.py](tests/test_policy.py) verifies edge cases, marker resilience, and mutation boundaries.

## Scope boundaries

[Recorded evaluation](evidence/evaluation.json). This project demonstrates local deterministic access auditing on synthetic data. Live Microsoft Graph API tenant crawling, semantic index queries, and production permission mutations remain separate live operational extensions.
