"""Trust score for a curated model."""
import praisonai_bio
from praisonai_bio.tools.trust_scorecard import trust_scorecard

print(trust_scorecard.run(model_id="BIOMD0000000206"))
