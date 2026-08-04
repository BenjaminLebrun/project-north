from project_north.reports.sections import summary, details, strengths_section


def build_report(result):
    return "\n\n".join([
        summary(result),
        strengths_section(result),
        "## Détails",
        details(result),
    ])