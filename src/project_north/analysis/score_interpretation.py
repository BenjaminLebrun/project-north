def interpret_score(score):

    if score >= 90:
        return "Très forte compatibilité"

    if score >= 70:
        return "Excellente compatibilité"

    if score >= 50:
        return "Bonne compatibilité"

    if score >= 30:
        return "Compatibilité moyenne"

    return "Faible compatibilité"