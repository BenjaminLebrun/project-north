def calculate_score(profile, first_name):

    score = 0
    details = []

    expression = first_name["expression"]["expression"]
    soul = first_name["soul"]["soul"]
    personality = first_name["personality"]["personality"]

    if expression == 8:
        score += 30
    elif expression == 1:
        score += 28
    elif expression == 4:
        score += 25
    elif expression == 5:
        score -= 10

    if soul == 33:
        score += 30
    elif soul == 6:
        score += 25

    if personality == 4:
        score += 20
    elif personality == 8:
        score += 18
    elif personality == 5:
        score -= 8

    # Compatibilité avec le profil existant
    if profile:

        if expression == profile.get("expression"):
            score += 10

        if soul == profile.get("soul"):
            score += 10

        if personality == profile.get("personality"):
            score += 10

    return {
    "score": score,
    "details": details,
    }