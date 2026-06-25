#!/usr/bin/env bash
# Run full PraisonAIBio test suite
set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== Plan compliance ==="
python scripts/validate_repo.py

echo "=== Unit tests ==="
pytest tests/unit -q

echo "=== Integration (live BioModels) ==="
pytest tests/integration -q

echo "=== Benchmark scorer ==="
python benchmarks/t2b_parity/scorer.py | head -5

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
