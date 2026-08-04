from project_north.scoring.rules import SCORING_RULES

def calculate_score(profile, first_name):

    score = 0
    details = []  

    expression = first_name["expression"]["expression"]
    soul = first_name["soul"]["soul"]
    personality = first_name["personality"]["personality"]

    if expression == 8:
        score += SCORING_RULES["expression"][8]
    elif expression == 1:
        score += SCORING_RULES["expression"][1]
    elif expression == 4:
        score += SCORING_RULES["expression"][4]
    elif expression == 5:
        score += SCORING_RULES["expression"][5]

    if soul == 33:
        score += SCORING_RULES["soul"][33]
    elif soul == 6:
        score += SCORING_RULES["soul"][6]

    if personality == 4:
        score += SCORING_RULES["personality"][4]
    elif personality == 8:
        score += SCORING_RULES["personality"][8]
    elif personality == 5:
        score += SCORING_RULES["personality"][5]

    # Compatibilité avec le profil existant
    if profile:

        if expression == profile.expression:
          score += SCORING_RULES["compatibility"]["expression"]
          details.append("Compatibilité Expression : +10")

        if soul == profile.soul:
            score += SCORING_RULES["compatibility"]["soul"]
            details.append("Compatibilité Âme : +10")

        if personality == profile.personality:
            score += SCORING_RULES["compatibility"]["personality"]
            details.append("Compatibilité Personnalité : +10")

    return {
    "score": score,
    "details": details,
    }