<# Candidate inactivity report; modification time is not proof of usage or compliance. #>
[CmdletBinding()]
param(
    [string]$ConfigFilepath = (Join-Path $PSScriptRoot '../Configuration/TenantSettings.json'),
    [string]$FixturePath = (Join-Path $PSScriptRoot '../Configuration/sites.fixture.json'),
    [switch]$Live,
    [string[]]$SiteIds = @(),
    [datetime]$AsOf = (Get-Date),
    [string]$OutputPath = (Join-Path $PSScriptRoot '../artifacts/site-review.json')
)
$ErrorActionPreference = 'Stop'
$config = Get-Content -Raw -LiteralPath $ConfigFilepath | ConvertFrom-Json
$cutoff = $AsOf.AddDays(-[int]$config.TenantSettings.InactivityThresholdDays)
if ($Live) {
    if (-not $SiteIds.Count) { throw 'Live mode requires an explicit -SiteIds scope.' }
    Import-Module Microsoft.Graph.Sites -ErrorAction Stop
    if (-not (Get-MgContext)) { throw 'Connect to Graph before a live read.' }
    $sites = @($SiteIds | ForEach-Object { Get-MgSite -SiteId $_ -Property 'id,webUrl,displayName,lastModifiedDateTime' -ErrorAction Stop })
} else { $sites = @(Get-Content -Raw -LiteralPath $FixturePath | ConvertFrom-Json) }
$results = @($sites | ForEach-Object {
    $status = if (-not $_.LastModifiedDateTime) {'unknown_last_modified'} elseif ([datetime]$_.LastModifiedDateTime -lt $cutoff) {'review_inactivity_candidate'} else {'recent_modification'}
    [pscustomobject]@{ SiteId=$_.Id; Name=$_.DisplayName; Status=$status; Mode=$(if($Live){'live_read'}else{'fixture'}); LastModified=$_.LastModifiedDateTime }
})
New-Item -ItemType Directory -Path (Split-Path -Parent $OutputPath) -Force | Out-Null
$results | ConvertTo-Json -AsArray | Set-Content -LiteralPath $OutputPath
$results
