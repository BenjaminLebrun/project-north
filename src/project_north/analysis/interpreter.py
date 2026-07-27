from project_north.analysis.rules import (
    EXPRESSION_RULES,
    LIFE_PATH_RULES,
    PERSONALITY_RULES,
    SOUL_RULES,
)


def interpret_profile(profile):

    return {
        "expression": EXPRESSION_RULES[profile["expression"]["expression"]],
        "soul": SOUL_RULES[profile["soul"]["soul"]],
        "personality": PERSONALITY_RULES[profile["personality"]["personality"]],
        "life_path": LIFE_PATH_RULES[profile["birth_date"]["life_path"]["life_path"]],
    }
