from project_north.export.json_exporter import export_json
from project_north.exporters.markdown import export_markdown


def export_profile(result, format="json"):

    if format == "json":
        return export_json(result)

    if format == "markdown":
        return export_markdown(result)

    raise ValueError(
        f"Unsupported export format: {format}"
    )