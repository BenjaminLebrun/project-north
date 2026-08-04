def warnings(result):

    warnings = []

    if result.expression == 1:
        warnings.append("Peut avoir tendance à vouloir tout contrôler")

    if result.expression == 8:
        warnings.append("Peut se mettre une forte pression pour réussir")

    if result.soul == 6:
        warnings.append("Peut porter trop de responsabilités")

    if result.personality == 4:
        warnings.append("Peut manquer de souplesse face au changement")

    return warnings