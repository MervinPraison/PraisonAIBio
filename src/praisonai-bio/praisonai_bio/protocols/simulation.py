"""Simulation protocol stub."""

from typing import Any, Protocol


class SimulationProtocol(Protocol):
    def run_timecourse(self, model: Any, duration: float, step: float) -> Any: ...
    def run_steady_state(self, model: Any) -> dict[str, Any]: ...
