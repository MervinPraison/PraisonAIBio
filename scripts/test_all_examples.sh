#!/usr/bin/env bash
# Run every Python example; report pass / skip / fail.
set -euo pipefail
cd "$(dirname "$0")/.."

export PYTHONPATH="${PYTHONPATH:-}:src/praisonai-bio"
export PYTHONWARNINGS=ignore

python -c "import praisonai_bio" 2>/dev/null || {
  echo "Run: pip install -e src/praisonai-bio" >&2
  exit 1
}

BASICO_OK=0
python -c "from praisonai_bio.adapters.basico_adapter import check_basico_available; import sys; ok,_=check_basico_available(); sys.exit(0 if ok else 1)" 2>/dev/null && BASICO_OK=1

PASS=0
SKIP=0
FAIL=0

run_one() {
  local script="$1"
  local reason="${2:-}"

  if [[ -n "$reason" ]]; then
    echo "SKIP $script ($reason)"
    SKIP=$((SKIP + 1))
    return 0
  fi

  local timeout=90
  [[ "$script" == examples/big/* ]] && timeout=180
  [[ "$script" == examples/python/* ]] && timeout=300
  [[ "$script" == examples/mcp/* ]] && timeout=120

  if timeout "$timeout" python "$script" >/tmp/pbio_ex.out 2>/tmp/pbio_ex.err; then
    echo "PASS $script ($(wc -c </tmp/pbio_ex.out | tr -d ' ') bytes)"
    PASS=$((PASS + 1))
  else
    echo "FAIL $script (exit $?)"
    tail -3 /tmp/pbio_ex.err >&2 || true
    FAIL=$((FAIL + 1))
  fi
}

OFFLINE=(
  examples/small/08_compare_sims.py
  examples/minimal/compare_runs.py
)

NETWORK=(
  examples/small/01_search.py examples/small/02_model_info.py examples/small/03_trust_score.py
  examples/small/04_validate_sbml.py examples/small/07_compare_models.py examples/small/09_repro_export.py
  examples/small/10_sbml_graph.py
  examples/minimal/search.py examples/minimal/info.py examples/minimal/trust.py
  examples/minimal/validate.py examples/minimal/graph.py examples/minimal/compare_models.py
  examples/minimal/export.py
)

BASICO=(
  examples/small/05_simulate.py examples/small/06_perturb.py
  examples/minimal/simulate.py examples/minimal/perturb.py
)

AGENT=(
  examples/minimal/agent.py examples/minimal/agent_simulate.py
  examples/big/01_find_models.py examples/big/02_summarise_model.py examples/big/03_discovery_study.py
  examples/big/04_glycolysis_demo.py examples/big/05_perturb_compare.py examples/big/06_full_repro_study.py
  examples/big/07_agent_with_configs.py examples/python/team_model_review.py
)

MCP=(examples/mcp/sysbio_client.py)

echo "=== Offline examples ==="
for s in "${OFFLINE[@]}"; do run_one "$s"; done

echo "=== Network examples ==="
for s in "${NETWORK[@]}"; do
  if [[ "${SKIP_NETWORK:-}" == "1" ]]; then
    run_one "$s" "SKIP_NETWORK=1"
  else
    run_one "$s"
  fi
done

echo "=== BASICO examples ==="
for s in "${BASICO[@]}"; do
  if [[ "$BASICO_OK" -eq 0 ]]; then
    run_one "$s" "BASICO not installed"
  elif [[ "${SKIP_NETWORK:-}" == "1" ]]; then
    run_one "$s" "SKIP_NETWORK=1"
  else
    run_one "$s"
  fi
done

echo "=== Agent examples ==="
for s in "${AGENT[@]}"; do
  if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    run_one "$s" "OPENAI_API_KEY not set"
  elif [[ "${SKIP_NETWORK:-}" == "1" ]]; then
    run_one "$s" "SKIP_NETWORK=1"
  else
    run_one "$s"
  fi
done

echo "=== MCP example ==="
for s in "${MCP[@]}"; do
  if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    run_one "$s" "OPENAI_API_KEY not set"
  elif ! command -v praisonai-bio-mcp >/dev/null 2>&1; then
    run_one "$s" "praisonai-bio-mcp not on PATH"
  else
    run_one "$s"
  fi
done

echo "---"
echo "PASS=$PASS SKIP=$SKIP FAIL=$FAIL"
[[ "$FAIL" -eq 0 ]]
