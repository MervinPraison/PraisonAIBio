"""In-memory model state for agent sessions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ModelState:
    model_id: str | None = None
    sbml_path: str | None = None
    model_as_string: str | None = None
    simulation_df: Any | None = field(default=None, repr=False)

    def to_dict(self) -> dict[str, Any]:
        return {
            "model_id": self.model_id,
            "sbml_path": self.sbml_path,
            "has_model_string": self.model_as_string is not None,
            "has_simulation": self.simulation_df is not None,
        }
