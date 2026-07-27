from project_north.numerology.birth_date import analyze_birth_date
from project_north.numerology.expression import calculate_expression
from project_north.numerology.personality import calculate_personality
from project_north.numerology.soul import calculate_soul


def create_profile(
    full_name: str,
    day: int,
    month: int,
    year: int,
):

    return {
        "identity": {
            "name": full_name,
        },
        "expression": calculate_expression(full_name),
        "soul": calculate_soul(full_name),
        "personality": calculate_personality(full_name),
        "birth_date": analyze_birth_date(
            day,
            month,
            year,
        ),
    }