#!/usr/bin/env bash
# run_all_tests.sh
# Runs all language test suites (Python, Java, C#) in sequence.
# Works on Linux/macOS/WSL/Git Bash and inside Docker.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

run_suite() {
  local label="$1"
  local script_rel="$2"
  local script_path="$ROOT/$script_rel"

  echo "==> ${label} tests"
  if [[ -f "$script_path" ]]; then
    # Ensure executable (harmless if already)
    chmod +x "$script_path" || true
    bash "$script_path"
    echo "✔ ${label} tests passed"
  else
    echo "✖ ${label} test script not found at: $script_rel"
    echo "   Create it or remove this suite from run_all_tests.sh"
    exit 1
  fi
  echo
}

# Run suites (adjust paths if you rename/move scripts)
run_suite "Python" "python/run_tests.sh"
run_suite "Java"   "java/run_tests.sh"
run_suite "C#"     "csharp/run_tests.sh"

echo "✅ All test suites passed."