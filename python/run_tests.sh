#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

PYTHON_BIN="python3"  # default for local runs

# If running inside Docker, force the venv python
if [[ "${VIRTUAL_ENV:-}" == "/opt/venv" && -x "/opt/venv/bin/python" ]]; then
  echo "Running inside Docker (venv already prepared)"
  PYTHON_BIN="/opt/venv/bin/python"
else
  echo "Running locally - setting up virtual environment..."
  if [ ! -d ".venv" ]; then
    python3 -m venv .venv
  fi
  # shellcheck disable=SC1091
  source .venv/bin/activate
  PYTHON_BIN="python3"
  $PYTHON_BIN -m pip install --upgrade pip
  if [ -f requirements.txt ]; then
    $PYTHON_BIN -m pip install -r requirements.txt
  fi
fi

# Run tests using the selected interpreter (module call is robust)
$PYTHON_BIN -m pytest -q