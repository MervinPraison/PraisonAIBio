"""Search BioModels.org — smallest example."""
import praisonai_bio
from praisonai_bio.tools.search_models import search_models

print(search_models.run(query="glycolysis", num_results=3))
