from project_north.compatibility.rules import RULES
from project_north.compatibility.weights import WEIGHTS
from project_north.compatibility.meaning import evaluate_meaning


def evaluate(expression, soul, personality, metadata=None):

    score = 0
    details = []

    if expression in RULES["expression"]:
        score += WEIGHTS["expression"]
        details.append(
            f"Expression {expression} : +{WEIGHTS['expression']}"
        )

    if soul in RULES["soul"]:
        score += WEIGHTS["soul"]
        details.append(
            f"Âme {soul} : +{WEIGHTS['soul']}"
        )

    if personality in RULES["personality"]:
        score += WEIGHTS["personality"]
        details.append(
            f"Personnalité {personality} : +{WEIGHTS['personality']}"
        )

    if metadata:

        if metadata.get("biblical") == "true":
            score += WEIGHTS["biblical"]
            details.append(
                f"Biblique : +{WEIGHTS['biblical']}"
            )

        if metadata.get("historical") == "true":
            score += WEIGHTS["historical"]
            details.append(
                f"Historique : +{WEIGHTS['historical']}"
            )

        if metadata.get("royal") == "true":
            score += WEIGHTS["royal"]
            details.append(
                f"Royal : +{WEIGHTS['royal']}"
            )

        meaning_matches = evaluate_meaning(
            metadata.get("meaning")
        )

        for match in meaning_matches:

            score += WEIGHTS["meaning"][match]

            details.append(
                f"Signification {match} : +{WEIGHTS['meaning'][match]}"
            )
            

    return {
        "score": score,
        "details": details,
    }