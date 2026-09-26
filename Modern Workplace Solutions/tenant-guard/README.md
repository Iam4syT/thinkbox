# Tenant Guard Agent

[![PowerShell](https://img.shields.io/badge/Language-PowerShell-5391FE?style=flat-square&logo=powershell)](https://learn.microsoft.com/powershell/)
[![Microsoft Graph](https://img.shields.io/badge/API-Microsoft%20Graph-0078D4?style=flat-square&logo=microsoft)](https://learn.microsoft.com/graph/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **Automated Identity Governance, Endpoint Compliance Monitoring, and AI Integration Agent Framework for Modern Enterprises via Microsoft Graph and PowerShell CI/CD.**

---

## 1. Business Value & Core Concept

Manual administration across international cloud environments exposes businesses to compliance drifts, unmapped administrative access, and data over-sharing. **Tenant Guard Agent** implements **Infrastructure as Code (IaC)** principles across Microsoft 365 architecture. 

By tracking architectural standards inside a structured version-controlled repository, any changes to live configurations are caught, flagged, and audited systematically.

### Key Business Benefits
- **Zero-Trust Baseline Enforcement:** Enforces continuous identity and endpoint baselines across Entra ID and Microsoft Intune.
- **AI Readiness Assurance:** Validates Copilot environment readiness and data sharing policies automatically.
- **CI/CD Governance:** Runs automated audit checks in GitHub Actions workflows to stop configuration drift.

---

## 2. High-Level Architecture Flow

```
┌────────────────────────────────┐
│  Base Configuration Definition │  Core configurations reside in
│  (Base-M365-DesiredState.json) │  templates/Base-M365-DesiredState.json
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  PowerShell Audit Scripts      │  Connects securely via Graph API endpoints
│  (scripts/*.ps1)               │  to audit Entra, Intune, & Copilot readiness
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  Continuous Enforcement        │  GitHub Actions automatically runs checks
│  (.github/workflows/)          │  to audit shifts and alert administrators
└────────────────────────────────┘
```

---

## 3. Project Structure

```
Tenant-Guard/
├── scripts/
│   ├── Run-EntraIdentityAudit.ps1    # Entra ID identity & RBAC compliance auditor
│   ├── Sync-IntuneDevicePolicies.ps1  # Intune endpoint fleet policy matching script
│   └── Test-CopilotReadiness.ps1     # M365 Copilot AI readiness validation script
├── templates/
│   └── Base-M365-DesiredState.json   # Desired state baseline definition schema
├── docs/                             # Architectural and deployment documentation
├── .github/                          # CI/CD GitHub Actions workflow definitions
├── .env.example                      # Environment configuration template
├── .gitignore                        # Git exclusion rules
├── LICENSE                           # MIT License
└── README.md                         # Technical documentation
```

---

## 4. Quickstart & Local Verification

To run this laboratory simulation framework manually on your local system for testing, execute these commands inside your terminal:

```powershell
# 1. Navigate to your project workspace
cd "/Users/4syt/Documents/thinkbox/Modern Workplace Solutions/Tenant-Guard"

# 2. Execute Identity Access Review Script
./scripts/Run-EntraIdentityAudit.ps1

# 3. Execute Intune Fleet Matching Script
./scripts/Sync-IntuneDevicePolicies.ps1

# 4. Run AI Environment Validation Audit
./scripts/Test-CopilotReadiness.ps1
```

---

## 5. Continuous Governance CI/CD

The repository includes pre-configured GitHub Actions workflows in `.github/workflows/` that execute audit suites automatically on commit or scheduled cron intervals, maintaining constant visibility over cloud tenant drift.

---

## 6. License

Distributed under the **MIT License**. Check out `LICENSE` for configuration details.
