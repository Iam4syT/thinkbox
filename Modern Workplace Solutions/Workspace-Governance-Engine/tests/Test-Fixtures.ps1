$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent $PSScriptRoot
$temp = Join-Path ([System.IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString())
try {
    $rows = @(& "$project/Scripts/Enforce-PurviewLabels.ps1" -OutputDirectory $temp)
    if ($rows.Count -ne 3) { throw 'Expected three fixture groups' }
    if (($rows | Where-Object GroupId -eq 'fixture-existing').Status -ne 'review_existing_label') { throw 'Existing labels must be retained' }
    if (($rows | Where-Object GroupId -eq 'fixture-target').Status -ne 'already_labelled') { throw 'Expected idempotent plan' }
    if (@($rows | Where-Object Performed).Count -ne 0) { throw 'Fixture mode must not write' }
    $sites = @(& "$project/Scripts/Audit-UnusedSharePointSites.ps1" -AsOf '2026-09-13' -OutputPath "$temp/sites.json")
    if (($sites | Where-Object SiteId -eq 'fixture-unknown').Status -ne 'unknown_last_modified') { throw 'Missing metadata must remain unknown' }
    $rejected = $false
    try { & "$project/Scripts/Enforce-PurviewLabels.ps1" -Apply -OutputDirectory $temp } catch { $rejected = $true }
    if (-not $rejected) { throw 'Apply must be rejected in fixture mode' }
    'PASS: label preservation, idempotence, no fixture writes, unknown metadata and apply boundary'
} finally { if (Test-Path $temp) { Remove-Item -LiteralPath $temp -Recurse -Force } }
