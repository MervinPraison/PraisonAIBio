#!/usr/bin/env bash
# Capture example stdout into docs/examples/*/output.txt for documentation.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "Capturing example outputs into docs/examples/ ..."

mkdir -p docs/examples/small/{01-search,02-model-info,03-trust-score,04-validate-sbml}
mkdir -p docs/examples/big/{01-find-models,02-summarise-model,03-discovery-study,04-glycolysis-demo}

python -c "import praisonai_bio" 2>/dev/null || {
  echo "Run: pip install -e src/praisonai-bio" >&2
  exit 1
}

capture() {
  local out="$1"
  shift
  "$@" 2>/dev/null > "$out"
  echo "  $(basename "$(dirname "$out")")/$(basename "$out") ($(wc -c < "$out" | tr -d ' ') bytes)"
}

echo "Small examples:"
capture docs/examples/small/01-search/output.txt python examples/small/01_search.py
capture docs/examples/small/02-model-info/output.txt python examples/small/02_model_info.py
capture docs/examples/small/03-trust-score/output.txt python examples/small/03_trust_score.py
capture docs/examples/small/04-validate-sbml/output.txt python examples/small/04_validate_sbml.py

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "Skipping big examples (set OPENAI_API_KEY to capture agent output)" >&2
  exit 0
fi

echo "Big examples:"
capture docs/examples/big/01-find-models/output.txt python examples/big/01_find_models.py
capture docs/examples/big/02-summarise-model/output.txt python examples/big/02_summarise_model.py
capture docs/examples/big/03-discovery-study/output.txt python examples/big/03_discovery_study.py
capture docs/examples/big/04-glycolysis-demo/output.txt python examples/big/04_glycolysis_demo.py

echo "Done. Update docs/examples/*/ pages if output format changed significantly."
