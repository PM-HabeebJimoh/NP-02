#!/bin/bash
# ============================================================
# V4 LOCAL TEST RUNNER — Run on YOUR machine with API keys
# ============================================================
#
# SETUP:
#   1. Get a FREE Google Gemini API key at: https://aistudio.google.com/
#      (No credit card needed! Gemini 3.5 Flash is free, 1500 req/day)
#
#   2. Get an OpenAI API key at: https://platform.openai.com/api-keys
#      (Needs credit card, but ~$5 free credits)
#
#   3. Set environment variables:
#      export GOOGLE_API_KEY="AIza..."
#      export OPENAI_API_KEY="sk-..."
#
#   4. Install dependencies:
#      pip3 install openai google-genai anthropic
#
#   5. Run this script:
#      bash LOCAL_TEST_RUNNER.sh
#
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "============================================================"
echo "V4 BUG BOUNTY TEST RUNNER"
echo "============================================================"

# Check for API keys
if [ -z "$GOOGLE_API_KEY" ] && [ -z "$OPENAI_API_KEY" ]; then
    echo ""
    echo "❌ No API keys set!"
    echo ""
    echo "Get a FREE Gemini API key (no credit card):"
    echo "  → https://aistudio.google.com/"
    echo ""
    echo "Then run:"
    echo "  export GOOGLE_API_KEY='AIza...'"
    echo "  bash LOCAL_TEST_RUNNER.sh"
    echo ""
    exit 1
fi

# Install dependencies if needed
pip3 install -q openai google-genai anthropic 2>/dev/null || true

# Run the Python test runner
python3 "$SCRIPT_DIR/auto_test_runner.py" --track all "$@"
