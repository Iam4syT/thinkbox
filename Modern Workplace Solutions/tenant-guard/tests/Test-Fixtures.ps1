$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent $PSScriptRoot
foreach ($script in @('Run-EntraIdentityAudit.ps1','Sync-IntuneDevicePolicies.ps1','Test-CopilotReadiness.ps1')) {
    & (Join-Path $PSHOME 'pwsh') -NoProfile -File (Join-Path "$project/scripts" $script)
    if ($LASTEXITCODE -ne 1) { throw "Expected fixture drift exit 1 for $script; got $LASTEXITCODE" }
}
'PASS: all three deliberately non-compliant fixtures report drift (exit 1)'

# Every expected child exit code has been asserted above. Do not leak the
# final intentional drift exit (1) into the GitHub Actions shell wrapper.
$global:LASTEXITCODE = 0
