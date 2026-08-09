# Workspace Governance Engine

[![PowerShell](https://img.shields.io/badge/Language-PowerShell-5391FE?style=flat-square&logo=powershell)](https://learn.microsoft.com/powershell/)
[![Microsoft Graph](https://img.shields.io/badge/API-Microsoft%20Graph-0078D4?style=flat-square&logo=microsoft)](https://learn.microsoft.com/graph/)
[![Purview](https://img.shields.io/badge/Security-Microsoft%20Purview-00a4ef?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **An automated, architecture-as-code solution that manages governance, eliminates infrastructure data sprawl, and programmatically enforces Microsoft Purview classification models across enterprise Microsoft 365 workspaces.**

---

## 1. Business & Financial Realities

### 📉 Quantifiable Operational Cost Optimization
Unmanaged workspace proliferation directly increases data storage costs. By automating the extraction and flagging of inactive, stale SharePoint environments, this solution reduces data storage waste, saving significant monthly operational capital expenditure (CapEx) costs.

### 🔒 Elimination of Security and Data Sprawl
Manual compliance tracking introduces human error risk. This engine automatically enforces **Microsoft Purview Data Classification Tags** across all unified collaborative workspaces. It ensures that critical intellectual property, complex data models, and enterprise source assets remain protected under corporate security boundaries.

### ⚡ Frictionless Deployment and Execution Experience
By shifting architectural setups directly to programmatic workflows (`SecureTeamsTemplate.xml`), team setup requests require zero direct human operations intervention, dropping standard engineering pipeline bottlenecks to zero.

---

## 2. Technical Architecture Overview

```
┌────────────────────────────────┐
│  GitHub Actions Workflow       │  Triggers nightly or via manual control inputs
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  Entra ID App Authentication   │  Authenticates safely without credentials via
│  (Certificate Credentials)     │  Certificate-Based Credentials & App Identity
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  Microsoft Graph Query Engine  │  Queries Graph APIs to compile analytics across
│  (Scripts/Connect-Graph.ps1)   │  the tenant surface
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  Automated Remediation         │  Identifies structural compliance gaps and
│  (Scripts/Audit & Enforce)     │  remediates based on TenantSettings.json
└────────────────────────────────┘
```

---

## 3. Project Structure

```
Workspace-Governance-Engine/
├── Scripts/
│   ├── Audit-UnusedSharePointSites.ps1  # Scans and flags inactive SharePoint sites
│   ├── Connect-AuroraGraph.ps1          # Graph API authentication wrapper
│   └── Enforce-PurviewLabels.ps1        # Automated Microsoft Purview label enforcer
├── Configuration/
│   ├── SecureTeamsTemplate.xml          # Teams architecture-as-code template
│   └── TenantSettings.json              # Central tenant governance settings
├── Dashboards/                          # Reporting assets & dashboard models
├── Documentation/                       # Deployment guides & architectural schemas
├── .github/                             # GitHub Actions CI/CD workflows
├── .env.example                         # Secret configuration template
├── .gitignore                           # Git ignore rules
├── LICENSE                              # MIT License
└── README.md                            # Technical documentation
```

---

## 4. Deployment & Setup Blueprint

### 1. Configure Cloud Secrets Matrix
Configure your targeted repository deployment variables within **GitHub Settings > Secrets and variables > Actions**:

| Secret Identifier Name | Description Blueprint Value |
| :--- | :--- |
| `AZURE_TENANT_ID` | Directory ID reference value found in Entra ID |
| `AZURE_CLIENT_ID` | Application registration string identifier |

---

## 5. Local Execution & Remediation

To test structural logic paths locally from an authenticated admin console:
```powershell
cd "/Users/4syt/Documents/thinkbox/Modern Workplace Solutions/Workspace-Governance-Engine"
./Scripts/Audit-UnusedSharePointSites.ps1 -ConfigFilepath ./Configuration/TenantSettings.json
```

---

## 6. Licensing Info

Distributed under the **MIT License**. Check out `LICENSE` for configuration details.
