# All Graph commands below are local mocks. No module, credentials or tenant is used.
$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent $PSScriptRoot
$global:ThinkboxGuardtestDirectory = Join-Path ([System.IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString())
$global:ThinkboxGuardlabels = @()
$global:ThinkboxGuardwrites = 0
$global:ThinkboxGuardreads = 0
$global:ThinkboxGuardconcurrent = $false
$global:ThinkboxGuardtenant = 'fixture-tenant'
function Import-Module { [CmdletBinding()]param([string]$Name) if ($Name -ne 'Microsoft.Graph.Groups') { throw 'Unexpected module in mock test' } }
function Get-MgContext { [pscustomobject]@{ AuthType='Delegated'; TenantId=$global:ThinkboxGuardtenant } }
function Get-MgGroup {
    [CmdletBinding()]param([string]$GroupId, [string[]]$Property)
    $global:ThinkboxGuardreads++
    $value = $global:ThinkboxGuardlabels
    if ($global:ThinkboxGuardconcurrent -and $global:ThinkboxGuardreads -ge 2) { $value = @(@{LabelId='changed-by-someone-else'}) }
    [pscustomobject]@{ Id=$GroupId; DisplayName='Synthetic group'; GroupTypes=@('Unified'); AssignedLabels=$value }
}
function Update-MgGroup {
    [CmdletBinding()]param([string]$GroupId, [hashtable]$BodyParameter)
    if (-not (Get-ChildItem $global:ThinkboxGuardtestDirectory -Filter '*.backup.json')) { throw 'A backup must exist before any write' }
    $global:ThinkboxGuardwrites++
    $global:ThinkboxGuardlabels = @($BodyParameter.AssignedLabels)
}
function Assert-Rejected([scriptblock]$Action) {
    $rejected=$false
    try { & $Action | Out-Null } catch { $rejected=$true }
    if (-not $rejected) { throw 'Expected the change guard to reject this operation' }
}
try {
    Assert-Rejected { & "$project/Scripts/Enforce-PurviewLabels.ps1" -Live -OutputDirectory $global:ThinkboxGuardtestDirectory }
    & "$project/Scripts/Enforce-PurviewLabels.ps1" -Live -Apply -WhatIf -GroupIds 'fixture' -OutputDirectory $global:ThinkboxGuardtestDirectory | Out-Null
    if ($global:ThinkboxGuardwrites) { throw 'WhatIf must not write' }
    $global:ThinkboxGuardreads=0; $global:ThinkboxGuardconcurrent=$true
    Assert-Rejected { & "$project/Scripts/Enforce-PurviewLabels.ps1" -Live -Apply -Confirm:$false -GroupIds 'fixture' -OutputDirectory $global:ThinkboxGuardtestDirectory }
    if ($global:ThinkboxGuardwrites) { throw 'Concurrent changes must block writes' }
    $global:ThinkboxGuardconcurrent=$false; $global:ThinkboxGuardreads=0
    $result = @(& "$project/Scripts/Enforce-PurviewLabels.ps1" -Live -Apply -Confirm:$false -GroupIds 'fixture','fixture' -OutputDirectory $global:ThinkboxGuardtestDirectory)
    if ($global:ThinkboxGuardwrites -ne 1 -or $result.Count -ne 1 -or $result[0].Status -ne 'applied_and_verified') { throw 'Expected one deduplicated, backed-up, verified mock write' }
    $backup=$result[0].BackupPath
    $again = @(& "$project/Scripts/Enforce-PurviewLabels.ps1" -Live -Apply -Confirm:$false -GroupIds 'fixture' -OutputDirectory $global:ThinkboxGuardtestDirectory)
    if ($global:ThinkboxGuardwrites -ne 1 -or $again[0].Status -ne 'already_labelled') { throw 'Repeated application must be idempotent' }
    $global:ThinkboxGuardtenant='wrong-tenant'
    Assert-Rejected { & "$project/Scripts/Restore-PurviewLabels.ps1" -BackupPath $backup -Apply -Confirm:$false }
    $global:ThinkboxGuardtenant='fixture-tenant'; $saved=$global:ThinkboxGuardlabels; $global:ThinkboxGuardlabels=@(@{LabelId='later-change'})
    Assert-Rejected { & "$project/Scripts/Restore-PurviewLabels.ps1" -BackupPath $backup -Apply -Confirm:$false }
    if ($global:ThinkboxGuardwrites -ne 1) { throw 'Restore guards must block writes' }
    $global:ThinkboxGuardlabels=$saved
    & "$project/Scripts/Restore-PurviewLabels.ps1" -BackupPath $backup -Apply -Confirm:$false | Out-Null
    if ($global:ThinkboxGuardwrites -ne 2 -or $global:ThinkboxGuardlabels.Count -ne 0) { throw 'Mock restoration must restore the original empty label set' }
    'PASS: explicit scope, WhatIf, concurrent-change refusal, backup-before-write, deduplication, verification, idempotence, wrong-tenant/different-state refusal and restoration (all Graph calls mocked)'
} finally {
    if (Test-Path $global:ThinkboxGuardtestDirectory) { Remove-Item -LiteralPath $global:ThinkboxGuardtestDirectory -Recurse -Force }
}
