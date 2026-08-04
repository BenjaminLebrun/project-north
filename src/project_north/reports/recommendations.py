def recommendations(result):

    recommendations = []

    if result.expression == 1:
        recommendations.append(
            "Privilégier les projets où il est possible de prendre des initiatives et de diriger."
        )

    if result.expression == 8:
        recommendations.append(
            "Chercher des environnements permettant de construire, organiser et atteindre des objectifs ambitieux."
        )

    if result.soul == 6:
        recommendations.append(
            "Veiller à équilibrer aide aux autres et besoins personnels."
        )

    if result.personality == 4:
        recommendations.append(
            "Favoriser une organisation structurée tout en gardant une capacité d'adaptation."
        )

    return recommendations