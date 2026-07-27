from project_north.numerology.profile import create_profile
from project_north.analysis.interpreter import interpret_profile


def analyze_profile(
    full_name: str,
    day: int,
    month: int,
    year: int,
):

    profile = create_profile(
        full_name,
        day,
        month,
        year,
    )

    interpretation = interpret_profile(profile)

    return {
        "profile": profile,
        "interpretation": interpretation,
    }