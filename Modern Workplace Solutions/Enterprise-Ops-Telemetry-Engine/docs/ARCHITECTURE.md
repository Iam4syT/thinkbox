# Human-Centered Architecture Runbook

## Solution Workflow
This engine acts as an automated operational layer for a Managed Service Provider (MSP).

[GitHub Actions Trigger] -> [Graph API Tenant Hardening Deployment]
│
▼
[Azure Resources & Devices] ──> [Telemetry Log Streams] ──> [Isolation Forest ML]
│
▼
[Power BI Executive Insights]

## Security Strategy
* **Zero Trust Policy:** All authentication elements use named environment variable wrappers rather than clear text tokens.
* **Intune Baseline Compliance:** Enforces BitLocker encryption globally before access to data infrastructure is unlocked.