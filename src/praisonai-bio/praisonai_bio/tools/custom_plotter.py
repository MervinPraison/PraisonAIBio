from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json


@tool
def custom_plotter(
    data_json: str,
    x_column: str,
    y_column: str,
    title: str = "Simulation plot",
    output_path: str = "plot.png",
) -> str:
    """Create a line plot from simulation data (JSON or CSV-like dict)."""
    import json

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return as_json({"error": "Install plot support: pip install praisonai-bio[plot]"})
    try:
        data = json.loads(data_json) if isinstance(data_json, str) else data_json
        if isinstance(data, dict) and "result_preview" in data:
            data = data["result_preview"]
        x = list(data.get(x_column, data.keys()))
        y = list(data.get(y_column, list(data.values())[0] if data else []))
        plt.figure()
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.savefig(output_path)
        plt.close()
        return as_json({"saved": output_path, "title": title})
    except Exception as exc:
        return as_json({"error": str(exc)})
