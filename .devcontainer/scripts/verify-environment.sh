#!/usr/bin/env bash
set -euo pipefail

fail() {
  echo "[FOUT] $1" >&2
  exit 1
}

echo "[INFO] Python versie:"
python --version || fail "Python is niet beschikbaar."

echo "[INFO] Git versie:"
git --version || fail "Git is niet beschikbaar."

echo "[INFO] Applicatie importcontrole:"
PYTHONPATH=src python -c "import change_request_tracker" || fail "Applicatie is niet importeerbaar vanaf src/."

echo "[INFO] Unit tests draaien:"
python -m unittest discover -s tests -v || fail "Unit tests falen."

if command -v copilot >/dev/null 2>&1; then
  echo "[INFO] Copilot CLI gevonden in PATH."
else
  echo "[INFO] Copilot CLI niet gevonden in PATH. Installeer en login handmatig via officiële GitHub-instructies."
fi

echo "[OK] Omgevingscontrole voltooid."
