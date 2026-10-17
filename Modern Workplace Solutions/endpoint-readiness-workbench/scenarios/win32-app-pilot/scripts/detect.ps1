$ErrorActionPreference = 'Stop'
$path = Join-Path $env:ProgramData 'WorkplaceLab\SupportNote\version.txt'
$note = Join-Path $env:ProgramData 'WorkplaceLab\SupportNote\note.txt'
if ((Test-Path -LiteralPath $path) -and (Test-Path -LiteralPath $note)) {
    if ((Get-Content -LiteralPath $path -Raw).Trim() -eq '1.0.0') {
        Write-Output 'SupportNote 1.0.0 detected'
        exit 0
    }
}
exit 1
