#!/usr/bin/env bash
# Capture example stdout into docs/examples/*/output.txt for documentation.
set -euo pipefail
cd "$(dirname "$0")/.."

export PYTHONPATH="${PYTHONPATH:-}:src/praisonai-bio"

echo "Capturing example outputs into docs/examples/ ..."

DIRS=(
  docs/examples/small/01-search
  docs/examples/small/02-model-info
  docs/examples/small/03-trust-score
  docs/examples/small/04-validate-sbml
  docs/examples/small/05-simulate
  docs/examples/small/06-perturb
  docs/examples/small/07-compare-models
  docs/examples/small/08-compare-sims
  docs/examples/small/09-repro-export
  docs/examples/small/10-sbml-graph
  docs/examples/minimal/search
  docs/examples/minimal/compare-runs
  docs/examples/big/01-find-models
  docs/examples/big/02-summarise-model
  docs/examples/big/03-discovery-study
  docs/examples/big/04-glycolysis-demo
  docs/examples/big/05-perturb-compare
  docs/examples/big/06-full-repro-study
  docs/examples/big/07-agent-with-configs
)

for d in "${DIRS[@]}"; do mkdir -p "$d"; done

python -c "import praisonai_bio" 2>/dev/null || {
  echo "Run: pip install -e src/praisonai-bio" >&2
  exit 1
}

capture() {
  local out="$1"
  shift
  if PYTHONWARNINGS=ignore "$@" 2>/dev/null | grep -v '^$' > "$out"; then
    echo "  OK $(basename "$(dirname "$out")")/$(basename "$out") ($(wc -c < "$out" | tr -d ' ') bytes)"
  else
    echo "  WARN $(basename "$(dirname "$out")")/$(basename "$out") (exit $?, $(wc -c < "$out" | tr -d ' ') bytes)"
  fi
}

echo "Small examples:"
capture docs/examples/small/01-search/output.txt python examples/small/01_search.py
capture docs/examples/small/02-model-info/output.txt python examples/small/02_model_info.py
capture docs/examples/small/03-trust-score/output.txt python examples/small/03_trust_score.py
capture docs/examples/small/04-validate-sbml/output.txt python examples/small/04_validate_sbml.py
capture docs/examples/small/05-simulate/output.txt python examples/small/05_simulate.py
capture docs/examples/small/06-perturb/output.txt python examples/small/06_perturb.py
capture docs/examples/small/07-compare-models/output.txt python examples/small/07_compare_models.py
capture docs/examples/small/08-compare-sims/output.txt python examples/small/08_compare_sims.py
capture docs/examples/small/09-repro-export/output.txt python examples/small/09_repro_export.py
capture docs/examples/small/10-sbml-graph/output.txt python examples/small/10_sbml_graph.py

echo "Minimal examples:"
capture docs/examples/minimal/search/output.txt python examples/minimal/search.py
capture docs/examples/minimal/compare-runs/output.txt python examples/minimal/compare_runs.py

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "Skipping big examples (set OPENAI_API_KEY to capture agent output)" >&2
else
  echo "Big examples:"
  capture docs/examples/big/01-find-models/output.txt python examples/big/01_find_models.py
  capture docs/examples/big/02-summarise-model/output.txt python examples/big/02_summarise_model.py
  capture docs/examples/big/03-discovery-study/output.txt python examples/big/03_discovery_study.py
  capture docs/examples/big/04-glycolysis-demo/output.txt python examples/big/04_glycolysis_demo.py
  capture docs/examples/big/05-perturb-compare/output.txt python examples/big/05_perturb_compare.py
  capture docs/examples/big/06-full-repro-study/output.txt python examples/big/06_full_repro_study.py
  capture docs/examples/big/07-agent-with-configs/output.txt python examples/big/07_agent_with_configs.py
fi

echo "Done."
python scripts/generate_example_docs.py
echo "Doc pages refreshed."
