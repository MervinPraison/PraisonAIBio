#!/usr/bin/env bash
# Run full PraisonAIBio test suite
set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== Plan compliance ==="
bash scripts/check_no_submission.sh
python scripts/validate_repo.py

echo "=== Unit tests ==="
pytest tests/unit -q

echo "=== Integration (live BioModels) ==="
pytest tests/integration -q

echo "=== Benchmark suite ==="
python benchmarks/run_all.py

echo "=== CLI ==="
python -m praisonai_bio.cli.main validate check
python -m praisonai_bio.cli.main tools validate

if [[ -n "${OPENAI_API_KEY:-}" ]]; then
  echo "=== Agentic (LLM) ==="
  pytest tests/agentic -q
else
  echo "=== Agentic SKIPPED (no OPENAI_API_KEY) ==="
fi

echo "=== ALL PASSED ==="
