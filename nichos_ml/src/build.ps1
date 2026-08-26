$ErrorActionPreference = 'Stop'
$src = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Split-Path -Parent $src
$candidate = Join-Path $root 'candidate'
New-Item -ItemType Directory -Force -Path $candidate | Out-Null
$template = Get-Content -Raw -Encoding UTF8 (Join-Path $src 'index.template.html')
$css = Get-Content -Raw -Encoding UTF8 (Join-Path $src 'styles.css')
$js = Get-Content -Raw -Encoding UTF8 (Join-Path $src 'app.js')
$html = $template.Replace('/*__INLINE_CSS__*/', $css).Replace('//__INLINE_JS__', $js)
Set-Content -LiteralPath (Join-Path $candidate 'index.html') -Value $html -Encoding UTF8
Write-Output (Join-Path $candidate 'index.html')
