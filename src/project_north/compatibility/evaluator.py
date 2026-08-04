from project_north.compatibility.rules import RULES
from project_north.compatibility.weights import WEIGHTS


def evaluate(expression, soul, personality):

    score = 0

    if expression in RULES["expression"]:
        score += WEIGHTS["expression"]

    if soul in RULES["soul"]:
        score += WEIGHTS["soul"]

    if personality in RULES["personality"]:
        score += WEIGHTS["personality"]

    return score