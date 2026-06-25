# Search BioModels

Use `search_models` and `rank_models` to find curated SBML models on BioModels.org.

## When to use

- User asks for models of a pathway (glycolysis, MAPK, p53)
- Need curated-only results (`curated_only=True` by default)

## Tools

- `search_models(query, num_results=10)`
- `rank_models(query, research_question=...)`
- `get_modelinfo(model_id)`

## Example

```python
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(name="scout", toolsets=["biomodels-readonly"])
agent.start("Find yeast glycolysis models on BioModels.org")
```
