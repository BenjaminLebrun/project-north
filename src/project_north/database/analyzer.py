from project_north.numerology.expression import calculate_expression
from project_north.numerology.personality import calculate_personality
from project_north.numerology.soul import calculate_soul


def analyze_first_name(first_name: dict):

    name = first_name["name"]

    return {
        **first_name,
        "gender": first_name.get("gender", "unknown"),
        "expression": calculate_expression(name),
        "soul": calculate_soul(name),
        "personality": calculate_personality(name),
    }


def analyze_first_names(first_names: list[dict]):

    return [
        analyze_first_name(first_name)
        for first_name in first_names
    ]