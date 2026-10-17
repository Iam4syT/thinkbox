# Read only. Use on your disposable Windows lab VM; never export production event messages.
$ErrorActionPreference = 'Stop'
$events = @(Get-WinEvent -FilterHashtable @{
    LogName = 'Application'; ProviderName = 'WorkplaceLab'; StartTime = (Get-Date).AddHours(-1)
} -ErrorAction Stop)
$result = @($events | ForEach-Object {
    [pscustomobject]@{record_id=[int]$_.RecordId;host='LAB-WIN01';provider=$_.ProviderName;
        event_id=[int]$_.Id;time=$_.TimeCreated.ToUniversalTime().ToString('o');level=$_.LevelDisplayName}
})
ConvertTo-Json -InputObject $result -Depth 4 | Set-Content -LiteralPath '.\lab-events.json' -Encoding UTF8
