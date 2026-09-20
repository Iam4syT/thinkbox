<#
.SYNOPSIS
    Plan sensitivity-label changes for explicitly selected Microsoft 365 groups.
.DESCRIPTION
    Defaults to fixtures. Live reads require -Live and delegated Graph authentication.
    Writes additionally require -Apply and ShouldProcess; other labels are never replaced
    unless -ReplaceExisting is supplied. No tenant-wide enumeration is performed.
#>
[CmdletBinding(SupportsShouldProcess=$true, ConfirmImpact='High')]
param(
    [string]$ConfigFilepath = (Join-Path $PSScriptRoot '../Configuration/TenantSettings.json'),
    [string]$FixturePath = (Join-Path $PSScriptRoot '../Configuration/groups.fixture.json'),
    [string[]]$GroupIds = @(),
    [switch]$Live,
    [switch]$Apply,
    [switch]$ReplaceExisting,
    [string]$OutputDirectory = (Join-Path $PSScriptRoot '../artifacts')
)
$ErrorActionPreference = 'Stop'
$config = Get-Content -Raw -LiteralPath $ConfigFilepath | ConvertFrom-Json
$target = [string]$config.TenantSettings.ClassificationLabels.HighCompliance
if (-not [guid]::TryParse($target, [ref]([guid]::Empty))) { throw 'Supply a valid target sensitivity-label GUID in config.' }
if ($Apply -and -not $Live) { throw '-Apply requires -Live; fixture mode never writes to a tenant.' }
if ($Live) {
    if ($GroupIds.Count -eq 0) { throw 'Live mode requires explicit -GroupIds.' }
    Import-Module Microsoft.Graph.Groups -ErrorAction Stop
    $context = Get-MgContext
    if (-not $context -or $context.AuthType -ne 'Delegated') { throw 'Sensitivity-label updates require delegated Graph access, permissions and a supported administrator role.' }
    $groups = @($GroupIds | Select-Object -Unique | ForEach-Object { Get-MgGroup -GroupId $_ -Property 'id,displayName,assignedLabels,groupTypes' -ErrorAction Stop })
} else {
    $context = $null
    $groups = @(Get-Content -Raw -LiteralPath $FixturePath | ConvertFrom-Json)
    if ($GroupIds.Count) { $groups = @($groups | Where-Object { $_.Id -in $GroupIds }) }
}
New-Item -ItemType Directory -Path $OutputDirectory -Force -WhatIf:$false | Out-Null
$runId = [guid]::NewGuid().ToString()
$results = @()
foreach ($group in $groups) {
    $before = @($group.AssignedLabels | Where-Object { $_.LabelId } | ForEach-Object { @{ LabelId = [string]$_.LabelId } })
    $state = 'planned'
    if ('Unified' -notin @($group.GroupTypes)) { $state = 'skipped_non_m365_group' }
    elseif ($target -in @($before.LabelId)) { $state = 'already_labelled' }
    elseif ($before.Count -gt 0 -and -not $ReplaceExisting) { $state = 'review_existing_label' }
    $row = [ordered]@{ GroupId = $group.Id; DisplayName = $group.DisplayName; Mode = $(if ($Live) {'live'} else {'fixture'}); Status = $state; Before = $before; Proposed = @(@{LabelId=$target}); Performed = $false }
    if ($state -eq 'planned' -and $Apply -and $PSCmdlet.ShouldProcess($group.Id, "Set sensitivity label $target")) {
        # Re-read immediately before writing; refuse to overwrite a changed label set.
        $current = Get-MgGroup -GroupId $group.Id -Property 'id,assignedLabels' -ErrorAction Stop
        if ((@($current.AssignedLabels.LabelId | Sort-Object) -join ',') -ne (@($before.LabelId | Sort-Object) -join ',')) { throw "Concurrent label change for $($group.Id); no write performed." }
        $backup = [ordered]@{ TenantId=$context.TenantId; GroupId=$group.Id; Before=$before; Applied=@(@{LabelId=$target}); RunId=$runId }
        $backupPath = Join-Path $OutputDirectory "$runId-$($group.Id).backup.json"
        $backup | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $backupPath
        Update-MgGroup -GroupId $group.Id -BodyParameter @{AssignedLabels=@(@{LabelId=$target})} -ErrorAction Stop
        $row.Performed = $true
        $row.Status = 'write_returned_success_verification_required'
        $row['BackupPath'] = $backupPath
        $verified = Get-MgGroup -GroupId $group.Id -Property 'id,assignedLabels' -ErrorAction Stop
        if ($target -notin @($verified.AssignedLabels.LabelId)) { throw "Write returned but verification is pending for $($group.Id). Preserve backup $backupPath." }
        $row.Status = 'applied_and_verified'
    }
    $results += [pscustomobject]$row
    $results | ConvertTo-Json -Depth 10 -AsArray | Set-Content -LiteralPath (Join-Path $OutputDirectory "$runId-plan.json")
}
$results
