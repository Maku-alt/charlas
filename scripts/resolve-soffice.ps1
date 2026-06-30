param(
    [switch]$Quiet
)

$cmd = Get-Command soffice -ErrorAction SilentlyContinue
if ($cmd) {
    if (-not $Quiet) { Write-Output $cmd.Source }
    exit 0
}

$candidates = @(
    'C:\Program Files\LibreOffice\program\soffice.com',
    'C:\Program Files\LibreOffice\program\soffice.exe',
    'C:\Program Files (x86)\LibreOffice\program\soffice.com',
    'C:\Program Files (x86)\LibreOffice\program\soffice.exe'
)

foreach ($candidate in $candidates) {
    if (Test-Path -LiteralPath $candidate) {
        if (-not $Quiet) { Write-Output $candidate }
        exit 0
    }
}

Write-Error 'LibreOffice soffice.exe was not found in PATH or standard install locations.'
exit 1
