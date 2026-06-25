"""SBML structure protocol."""

from typing import Any, Protocol


class SBMLStructureProtocol(Protocol):
    """Parse SBML bytes into a graph-friendly structure."""

    def load_sbml_bytes(self, content: bytes) -> Any: ...

    def parse_structure(self, content: bytes) -> dict[str, Any]: ...

    def to_graph(self, structure: dict[str, Any]) -> dict[str, Any]: ...
