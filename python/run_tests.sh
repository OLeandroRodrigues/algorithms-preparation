#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Install dependencies 
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

# Run tests 
pytest -q