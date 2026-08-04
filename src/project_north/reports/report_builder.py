from project_north.reports.sections import (
    summary,
    strengths_section,
    warnings_section,
    details,
)


def build_report(result):

    return "\n\n".join([
        summary(result),
        strengths_section(result),
        warnings_section(result),
        "## Détails",
        details(result),
    ])