from project_north.scoring.rules import SCORING_RULES


def calculate_score(profile, first_name):

    score = 0
    details = []

    expression = first_name["expression"]["expression"]
    soul = first_name["soul"]["soul"]
    personality = first_name["personality"]["personality"]

    if expression == 8:
        score += SCORING_RULES["expression"][8]
        details.append(
            f"Expression 8 : +{SCORING_RULES['expression'][8]}"
        )

    elif expression == 1:
        score += SCORING_RULES["expression"][1]
        details.append(
            f"Expression 1 : +{SCORING_RULES['expression'][1]}"
        )

    elif expression == 4:
        score += SCORING_RULES["expression"][4]
        details.append(
            f"Expression 4 : +{SCORING_RULES['expression'][4]}"
        )

    elif expression == 5:
        score += SCORING_RULES["expression"][5]
        details.append(
            f"Expression 5 : {SCORING_RULES['expression'][5]}"
        )

    if soul == 33:
        score += SCORING_RULES["soul"][33]
        details.append(
            f"Âme 33 : +{SCORING_RULES['soul'][33]}"
        )

    elif soul == 6:
        score += SCORING_RULES["soul"][6]
        details.append(
            f"Âme 6 : +{SCORING_RULES['soul'][6]}"
        )

    if personality == 4:
        score += SCORING_RULES["personality"][4]
        details.append(
            f"Personnalité 4 : +{SCORING_RULES['personality'][4]}"
        )

    elif personality == 8:
        score += SCORING_RULES["personality"][8]
        details.append(
            f"Personnalité 8 : +{SCORING_RULES['personality'][8]}"
        )

    elif personality == 5:
        score += SCORING_RULES["personality"][5]
        details.append(
            f"Personnalité 5 : {SCORING_RULES['personality'][5]}"
        )

    if profile:

        if expression == profile.expression:
            score += SCORING_RULES["compatibility"]["expression"]
            details.append(
                f"Compatibilité Expression : +{SCORING_RULES['compatibility']['expression']}"
            )

        if soul == profile.soul:
            score += SCORING_RULES["compatibility"]["soul"]
            details.append(
                f"Compatibilité Âme : +{SCORING_RULES['compatibility']['soul']}"
            )

        if personality == profile.personality:
            score += SCORING_RULES["compatibility"]["personality"]
            details.append(
                f"Compatibilité Personnalité : +{SCORING_RULES['compatibility']['personality']}"
            )

    return {
        "score": score,
        "details": details,
    }