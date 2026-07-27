from project_north.analysis.profile_analysis import (
    analyze_profile,
)


def generate_profile_report(
    full_name: str,
    day: int,
    month: int,
    year: int,
):

    return analyze_profile(
        full_name,
        day,
        month,
        year,
    )
