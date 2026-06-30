# Knowledge Base: Common Tenant Governance Pipeline Errors

## KB-1001: Script Execution Policy Restriction
* **Symptom:** Terminal states: `File cannot be loaded because running scripts is disabled on this system.`
* **Root Cause:** Default local execution policies prevent running unsigned automation scripts.
* **Resolution:** Open an elevated PowerShell prompt on your machine and run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
  ```

## KB-1002: Pipeline False Positives via Mock Testing Data
* **Symptom:** Pipeline triggers alerts continuously during sandbox simulation stages.
* **Root Cause:** Scripts contain hardcoded simulation profiles to demonstrate alerting pathways without connecting to an expensive production client directory.
* **Resolution:** Update parameters within the script files to map directly onto test staging endpoints prior to production environment merges.
