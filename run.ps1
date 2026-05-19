# InvoiceFlow AI — Textract vs LLM Comparison
# One-command setup and launch for Windows PowerShell.
#
# Usage:
#   .\run.ps1
#
# Prerequisites:
#   - Python 3.10+ installed (python.org or Microsoft Store)
#   - AWS CLI installed and configured (aws configure)
#   - Bedrock model access enabled (Claude Sonnet 4.6 or Opus 4.5)

$ErrorActionPreference = "Stop"
$PORT = 8501
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$APP_DIR = Join-Path $SCRIPT_DIR "code\invoiceFlow-AI\backend"
$VENV_DIR = Join-Path $SCRIPT_DIR ".venv"

Write-Host ""
Write-Host "=== InvoiceFlow AI - Textract vs LLM Comparison ===" -ForegroundColor Cyan
Write-Host ""

# --- Check Python ---
$python = $null
foreach ($cmd in @("python", "python3")) {
    try {
        $ver = & $cmd --version 2>&1
        if ($ver -match "Python 3") {
            $python = $cmd
            Write-Host "[OK] $ver" -ForegroundColor Green
            break
        }
    } catch {}
}
if (-not $python) {
    Write-Host "[ERROR] Python 3.10+ required. Install from https://python.org" -ForegroundColor Red
    exit 1
}

# --- Check AWS credentials ---
try {
    $identity = aws sts get-caller-identity --output json 2>&1 | ConvertFrom-Json
    Write-Host "[OK] AWS credentials valid (account: $($identity.Account))" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] AWS credentials not configured." -ForegroundColor Red
    Write-Host "  Run: aws configure" -ForegroundColor Yellow
    Write-Host "  Or set: `$env:AWS_ACCESS_KEY_ID, `$env:AWS_SECRET_ACCESS_KEY, `$env:AWS_DEFAULT_REGION" -ForegroundColor Yellow
    exit 1
}

# --- Setup virtual environment ---
if (-not (Test-Path $VENV_DIR)) {
    Write-Host ""
    Write-Host "-> Creating virtual environment..." -ForegroundColor Yellow
    & $python -m venv $VENV_DIR
}

$pip = Join-Path $VENV_DIR "Scripts\pip.exe"
$streamlit = Join-Path $VENV_DIR "Scripts\streamlit.exe"

# --- Install dependencies ---
Write-Host "-> Installing dependencies..." -ForegroundColor Yellow
& $pip install --quiet --upgrade pip
& $pip install --quiet boto3 streamlit pandas
Write-Host "[OK] Dependencies installed" -ForegroundColor Green

# --- Kill existing instance on port ---
$existing = Get-NetTCPConnection -LocalPort $PORT -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "-> Stopping existing app on port $PORT..." -ForegroundColor Yellow
    $existing | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    Start-Sleep -Seconds 1
}

# --- Launch ---
Write-Host ""
Write-Host "Launching application..." -ForegroundColor Cyan
Write-Host "  Open: http://localhost:$PORT" -ForegroundColor White
Write-Host ""
Write-Host "  Steps:" -ForegroundColor Gray
Write-Host "  1. Select a model (Sonnet 4.6 or Opus 4.5)" -ForegroundColor Gray
Write-Host "  2. Upload an invoice PDF (samples in docs\ folder)" -ForegroundColor Gray
Write-Host "  3. Click 'Extract & Compare'" -ForegroundColor Gray
Write-Host ""
Write-Host "  Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

Set-Location $APP_DIR
& $streamlit run "pages\textract_vs_llm.py" --server.port $PORT --server.headless true --browser.gatherUsageStats false
