"""Reproducibility bundle protocol."""

from typing import Any, Protocol


class ReproBundleProtocol(Protocol):
    def export(self, model_id: str, output_dir: str, run_id: str | None = None) -> dict[str, Any]: ...
