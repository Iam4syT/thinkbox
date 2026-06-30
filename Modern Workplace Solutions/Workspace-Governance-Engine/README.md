# Workspace Governance Engine

An automated, architecture-as-code solution that manages governance, eliminates infrastructure data sprawl, and programmatically enforces Microsoft Purview classification models across enterprise Microsoft 365 workspaces.

---

## Technical Architecture Overview

The solution operates as a hands-off operational lifecycle management loop:
1. **GitHub Actions Workflow Execution Engine** triggers nightly or via manual control inputs.
2. Authenticates safely without credentials via **Certificate-Based Credentials** linked to an **Azure Entra ID App Identity**.
3. Queries **Microsoft Graph APIs** to compile operational data analytics across the tenant surface.
4. Identifies structural compliance gaps and remediates platform configurations automatically based on `TenantSettings.json` definitions.

---

## Business & Financial Realities

### 📉 Quantifiable Operational Cost Optimization
Unmanaged workspace proliferation directly increases data storage costs. By automating the extraction and flagging of inactive, stale SharePoint environments, this solution reduces data storage waste, saving significant monthly operational capital expenditure (CapEx) costs.

### 🔒 Elimination of Security and Data Sprawl
Manual compliance tracking introduces human error risk. This engine automatically enforces **Microsoft Purview Data Classification Tags** across all unified collaborative workspaces. It ensures that critical intellectual property, complex data models, and enterprise source assets remain protected under corporate security boundaries.

### ⚡ Frictionless Deployment and Execution Experience
By shifting architectural setups directly to programmatic workflows (`SecureTeamsTemplate.xml`), team setup requests require zero direct human operations intervention, dropping standard engineering pipeline bottlenecks to zero.

---

## Deployment & Setup Blueprint

### 1. Configure Cloud Secrets Matrix
Configure your targeted repository deployment variables within **GitHub Settings > Secrets and variables > Actions**:

| Secret Identifier Name | Description Blueprint Value |
| :--- | :--- |
| `AZURE_TENANT_ID` | Directory ID reference value found in Entra ID |
| `AZURE_CLIENT_ID` | Application registration string identifier |

### 2. Run Local Evaluation Exercises
To test structural logic paths locally from an authenticated admin console:
```powershell
./Scripts/Audit-UnusedSharePointSites.ps1 -ConfigFilepath ./Configuration/TenantSettings.json
```

## Licensing Info

Distributed under the **MIT License**. Check out `LICENSE` for configuration details.
