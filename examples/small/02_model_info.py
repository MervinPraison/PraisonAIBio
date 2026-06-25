"""Get metadata for one model ID."""
import praisonai_bio
from praisonai_bio.tools.get_modelinfo import get_modelinfo

print(get_modelinfo.run(model_id="BIOMD0000000206"))
