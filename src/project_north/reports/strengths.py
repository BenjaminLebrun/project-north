def strengths(result):

    strengths = []

    if result.expression == 1:
        strengths.append("Leadership naturel")

    if result.expression == 8:
        strengths.append("Grande capacité d'accomplissement")

    if result.soul == 6:
        strengths.append("Sens des responsabilités")

    if result.personality == 4:
        strengths.append("Fiabilité et stabilité")

    return strengths