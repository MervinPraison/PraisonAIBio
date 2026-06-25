#!/usr/bin/env bash
# Fail if submission / grant / private proposal text would enter the public repo.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PATTERN='OS4LS|OS4 Science|LOI|letter of support|fiscal sponsor|work package|Renaissance Philanthropy|Track 1|21 Jul 2026|info@os4science|proposal outline|full proposal|submission deadline|Sheriff Malik|Karthick Subramanian'

echo "Checking tracked files for submission-sensitive text..."
FOUND=0
while IFS= read -r -d '' f; do
  [[ "$f" == .gitignore ]] && continue
  if grep -i -E -q "$PATTERN" "$f" 2>/dev/null; then
    echo "  $f"
    FOUND=1
  fi
done < <(git ls-files -z)

if [[ "$FOUND" -eq 1 ]]; then
  echo "FAIL: submission-sensitive text found in tracked files (see above)."
  exit 1
fi

if [[ -d grant ]] && ! git check-ignore -q grant/ 2>/dev/null; then
  echo "FAIL: grant/ directory exists and is NOT gitignored."
  exit 1
fi

echo "OK: no submission-sensitive content in git-tracked files."
