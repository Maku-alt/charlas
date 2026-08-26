$ErrorActionPreference = 'Stop'
$talkRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$tempRoot = Join-Path $env:TEMP 'nichos_ml_pysubgroup_smoke_20260826'
if (Test-Path -LiteralPath $tempRoot) { Remove-Item -LiteralPath $tempRoot -Recurse -Force }
py -3.10 -m venv $tempRoot
$py = Join-Path $tempRoot 'Scripts/python.exe'
& $py -m pip install --disable-pip-version-check --no-input --progress-bar off --timeout 60 --retries 2 --only-binary=:all: pysubgroup==0.9.0 numpy==1.26.4 scikit-learn==1.7.2 pandas==2.2.3 scipy==1.14.1 matplotlib==3.9.4 statsmodels==0.14.5
& $py (Join-Path $talkRoot 'tools/generate_demo.py')
Write-Output "SMOKE_ENV=$tempRoot"
