#!/bin/bash
# InvoiceFlow AI — Textract vs LLM Comparison
# One-command setup and launch for any machine with AWS credentials configured.
#
# Usage:
#   ./run.sh
#
# Prerequisites:
#   - Python 3.10+ installed
#   - AWS credentials configured (aws configure, or env vars exported)
#   - Bedrock model access enabled in your AWS account (Claude Sonnet 4.6 or Opus 4.5)
#   - Textract access enabled in your AWS region

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_DIR="$SCRIPT_DIR/code/invoiceFlow-AI/backend"
VENV_DIR="$SCRIPT_DIR/.venv"
PORT=8501

echo "╔══════════════════════════════════════════════════════════╗"
echo "║   InvoiceFlow AI — Textract vs LLM Comparison           ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# --- Check Python ---
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "❌ Python 3.10+ is required. Install from https://python.org"
    exit 1
fi

PY_VERSION=$($PYTHON -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✓ Python $PY_VERSION found"

# --- Check AWS credentials ---
if ! aws sts get-caller-identity &>/dev/null; then
    echo ""
    echo "❌ AWS credentials not configured. Run one of:"
    echo "   aws configure"
    echo "   OR export AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN"
    exit 1
fi

ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
echo "✓ AWS credentials valid (account: $ACCOUNT)"

# --- Setup virtual environment ---
if [ ! -d "$VENV_DIR" ]; then
    echo ""
    echo "→ Creating virtual environment..."
    $PYTHON -m venv "$VENV_DIR"
fi

# --- Install dependencies ---
echo "→ Installing dependencies..."
"$VENV_DIR/bin/pip" install --quiet --upgrade pip
"$VENV_DIR/bin/pip" install --quiet boto3 streamlit pandas

echo "✓ Dependencies installed"

# --- Kill existing instance ---
if lsof -ti:$PORT &>/dev/null; then
    echo "→ Stopping existing app on port $PORT..."
    lsof -ti:$PORT | xargs kill -9 2>/dev/null || true
    sleep 1
fi

# --- Launch ---
echo ""
echo "🚀 Starting application..."
echo "   Open: http://localhost:$PORT"
echo ""
echo "   Steps:"
echo "   1. Select a model (Sonnet 4.6 or Opus 4.5)"
echo "   2. Upload an invoice PDF (samples in docs/ folder)"
echo "   3. Click 'Extract & Compare'"
echo ""
echo "   Press Ctrl+C to stop"
echo ""

cd "$APP_DIR"
exec "$VENV_DIR/bin/streamlit" run pages/textract_vs_llm.py \
    --server.port $PORT \
    --server.headless true \
    --browser.gatherUsageStats false
