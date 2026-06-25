"""Validate SBML from BioModels (no simulation needed)."""
import praisonai_bio
from praisonai_bio.tools.sbml_validate import sbml_validate

print(sbml_validate.run(model_id="BIOMD0000000206"))
