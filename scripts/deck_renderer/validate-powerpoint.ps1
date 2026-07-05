param(
  [Parameter(Mandatory = $true)]
  [string]$PptxPath,
  [string]$OutDir = ""
)

$ErrorActionPreference = "Stop"

$resolved = Resolve-Path -LiteralPath $PptxPath
if ([string]::IsNullOrWhiteSpace($OutDir)) {
  $OutDir = Join-Path (Split-Path -Parent $resolved) ("native-export-" + [IO.Path]::GetFileNameWithoutExtension($resolved))
}
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$powerPoint = $null
$presentation = $null
try {
  $powerPoint = New-Object -ComObject PowerPoint.Application
  $powerPoint.Visible = -1
  $presentation = $powerPoint.Presentations.Open($resolved, $false, $false, $false)
  $slideCount = $presentation.Slides.Count
  $presentation.Export((Resolve-Path -LiteralPath $OutDir), "PNG", 1920, 1080)
  $presentation.Close()
  $presentation = $null
  $exported = @(Get-ChildItem -LiteralPath $OutDir -Filter "*.PNG" -File)
  [pscustomobject]@{
    pptx = $resolved.Path
    status = "ok"
    slides = $slideCount
    exported_png = $exported.Count
    export_dir = (Resolve-Path -LiteralPath $OutDir).Path
  } | ConvertTo-Json -Depth 3
}
catch {
  if ($presentation -ne $null) {
    try { $presentation.Close() } catch {}
  }
  [pscustomobject]@{
    pptx = $resolved.Path
    status = "failed"
    error = $_.Exception.Message
    hresult = ('0x{0:X8}' -f ($_.Exception.HResult -band 0xffffffff))
    export_dir = $OutDir
  } | ConvertTo-Json -Depth 3
  exit 1
}
finally {
  if ($powerPoint -ne $null) {
    try { $powerPoint.Quit() } catch {}
  }
}
