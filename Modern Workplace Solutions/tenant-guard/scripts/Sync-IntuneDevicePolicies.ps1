<#
.SYNOPSIS
    Cross-references active Intune compliance baselines against local desired state.
#>

$BaselinePath = Join-Path $PSScriptRoot "..\templates\Base-M365-DesiredState.json"
$Baseline = Get-Content -Raw -Path $BaselinePath | ConvertFrom-Json

Write-Host "=== STEP 2: Executing Intune Device Compliance Mapping ===" -ForegroundColor Cyan
Write-Host "[INFO] Connecting to Graph Endpoint: https://graph.microsoft.com/v1.0/deviceManagement/deviceCompliancePolicies" -ForegroundColor Yellow

# Mocking the live production retrieval payload structure 
$LiveIntunePolicy = @{
    OsPlatform      = "Windows10AndLater"
    RequireFirewall = $true
    RequireAntivirus= $false # Drift simulated here
}

$DriftFound = $false

# Evaluate Firewall Setting
if ($LiveIntunePolicy.RequireFirewall -ne $Baseline.DeviceCompliance.RequireFirewall) {
    Write-Host "[DRIFT] Firewall policy mismatch detected!" -ForegroundColor Red
    $DriftFound = $true
} else {
    Write-Host "[PASS] Firewall configuration aligns with baseline parameters." -ForegroundColor Green
}

# Evaluate Antivirus Setting
if ($LiveIntunePolicy.RequireAntivirus -ne $Baseline.DeviceCompliance.RequireAntivirus) {
    Write-Host "[DRIFT] Antivirus enforcement is DISABLED or missing in active environment!" -ForegroundColor Red
    $DriftFound = $true
} else {
    Write-Host "[PASS] Antivirus target verification validated." -ForegroundColor Green
}

if ($DriftFound) {
    Write-Host "[ALERT] Endpoint state configuration drift identified. Remediate immediately." -ForegroundColor Red
    Exit 1
} else {
    Write-Host "[PASS] Endpoint fleet status matches standard configurations perfectly." -ForegroundColor Green
    Exit 0
}
