#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
pip install -r docs/requirements.txt -q
mkdocs build --strict
echo "Built site/ — open site/index.html or run mkdocs serve"
