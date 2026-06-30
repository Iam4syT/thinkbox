# Standard Operating Procedure: Remediating Tenant Security Drifts

## 1. Purpose & Scope
This document outlines operational actions required when the `aurora-tenant-guard` pipeline identifies administrative, device compliance, or AI governance policy drift within Microsoft 365.

## 2. Step-by-Step Remediation Protocols

### Scenario A: Unauthorized or Un-MFA'd Global Administrators Found
1. Log in to the [Microsoft Entra Admin Center](https://entra.microsoft.com) using an authorized account.
2. Navigate to **Identity > Roles & Administrators > Roles**.
3. Search for and select the **Global Administrator** role.
4. Locate the user flagged by the automated script report.
5. **Action:** Click on the ellipses (`...`) next to the flagged unauthorized identity and choose **Remove Assignment**.
6. If the identity requires access but lacks Multi-Factor Authentication:
   * Direct the user to configure MFA immediately via `https://aka.ms/mfasetup`.
   * Apply an **Entra Conditional Access Policy** requiring MFA for all administrative actions.

### Scenario B: Intune Endpoint Policy Drift Detected
1. Log in to the [Microsoft Intune Admin Center](https://intune.microsoft.com).
2. Navigate to **Devices > Compliance Policies**.
3. Locate the policy matching the platform version (e.g., Windows 10 Baseline).
4. Review the **Properties** configuration against our `Base-M365-DesiredState.json` template.
5. Correct the drifted metric (e.g., change *Require Antivirus* from *Not Configured* to *Require*).
6. Save and select **Sync Fleet** to enforce settings immediately.

## 3. SLA Compliance Target Matrix
| Metric Class | Incident Severity | Action Target SLA |
| :--- | :--- | :--- |
| Un-MFA'd Administrator Access | Critical | 15 Minutes |
| Device Baseline Disabling Drift | High | 2 Hours |
| Over-Shared AI Data Footprint | Medium | 12 Hours |
