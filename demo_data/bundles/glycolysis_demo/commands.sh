#!/usr/bin/env bash
# Glycolysis demo reproducibility — BIOMD0000000206
set -euo pipefail
pip install -e "src/praisonai-bio[simulation]" -q
python -c "import praisonai_bio"
python -c "
from praisonai_bio.tools.search_models import search_models
from praisonai_bio.tools.get_modelinfo import get_modelinfo
print(search_models.run(query='BIOMD0000000206', num_results=1))
print(get_modelinfo.run(model_id='BIOMD0000000206'))
"
