from project_north.reports.sections import (
    summary,
    profile_summary_section,
    strengths_section,
    warnings_section,
    recommendations_section,
    conclusion_section,
    details,
)


def build_report(result):

    return "\n\n".join([
        summary(result),
        profile_summary_section(result),
        strengths_section(result),
        warnings_section(result),
        recommendations_section(result),
        "## Détails",
        details(result),
        conclusion_section(result),
    ])