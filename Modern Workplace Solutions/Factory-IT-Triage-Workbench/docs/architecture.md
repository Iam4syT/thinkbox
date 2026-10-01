# Architecture and operational limits

Local JSON → deterministic validation/routing → JSON output → human review. Standard library only; no external calls. Malformed JSON fails without creating an output; fixtures carry only synthetic data. The aid trusts input assertions and cannot prove current account/device state. No access approval, provisioning, patching, network scan, device wipe or PLC control exists.

A real deployment needs an authenticated source, schema validation, policy-aligned rules, permissions, review/audit, retention, monitoring and operational owner. AI summary extension is unimplemented and must be compared with a template.
