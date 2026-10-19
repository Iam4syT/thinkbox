# Architecture
Read-only synthetic CSV → schema validator → rule evaluator → stdout JSON → human review. Failure exits2 on invalid schema/value/duplicates; no partial success JSON. No authentication, network, tenant writes or auto-remediation. File size/concurrency and trusted provenance are production gaps.
