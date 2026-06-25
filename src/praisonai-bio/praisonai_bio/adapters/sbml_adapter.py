"""SBML parsing adapter — structure extraction and graph conversion."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Any


def _local_tag(tag: str) -> str:
    return tag.split("}")[-1] if "}" in tag else tag


def load_sbml_bytes(content: bytes) -> ET.Element:
    """Parse SBML XML bytes into an ElementTree root."""
    return ET.fromstring(content)


def parse_structure(content: bytes) -> dict[str, Any]:
    """Extract species, reactions, compartments, and parameters from SBML."""
    root = load_sbml_bytes(content)
    species = [
        {"id": el.get("id"), "name": el.get("name"), "compartment": el.get("compartment")}
        for el in root.findall(".//{*}species")
    ]
    reactions = [
        {
            "id": el.get("id"),
            "name": el.get("name"),
            "reversible": el.get("reversible"),
            "reactants": [r.get("species") for r in el.findall(".//{*}listOfReactants/{*}speciesReference")],
            "products": [p.get("species") for p in el.findall(".//{*}listOfProducts/{*}speciesReference")],
        }
        for el in root.findall(".//{*}reaction")
    ]
    compartments = [{"id": el.get("id"), "name": el.get("name")} for el in root.findall(".//{*}compartment")]
    parameters = [{"id": el.get("id"), "value": el.get("value")} for el in root.findall(".//{*}parameter")]
    model_el = root.find(".//{*}model")
    return {
        "root": _local_tag(root.tag),
        "model_id": model_el.get("id") if model_el is not None else None,
        "species": species,
        "reactions": reactions,
        "compartments": compartments,
        "parameters": parameters,
        "counts": {
            "species": len(species),
            "reactions": len(reactions),
            "compartments": len(compartments),
            "parameters": len(parameters),
        },
    }


def to_graph(structure: dict[str, Any]) -> dict[str, Any]:
    """Convert parsed SBML structure into nodes and edges for graph tools."""
    nodes = []
    edges = []

    for sp in structure.get("species", []):
        sid = sp.get("id")
        if sid:
            nodes.append({"id": sid, "type": "species", "label": sp.get("name") or sid})

    for rx in structure.get("reactions", []):
        rid = rx.get("id")
        if not rid:
            continue
        nodes.append({"id": rid, "type": "reaction", "label": rx.get("name") or rid})
        for reactant in rx.get("reactants") or []:
            if reactant:
                edges.append({"source": reactant, "target": rid, "type": "reactant"})
        for product in rx.get("products") or []:
            if product:
                edges.append({"source": rid, "target": product, "type": "product"})

    for comp in structure.get("compartments", []):
        cid = comp.get("id")
        if cid:
            nodes.append({"id": cid, "type": "compartment", "label": comp.get("name") or cid})

    return {
        "nodes": nodes,
        "edges": edges,
        "meta": structure.get("counts", {}),
        "model_id": structure.get("model_id"),
    }
