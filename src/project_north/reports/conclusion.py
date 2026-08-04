def conclusion(result):

    if result.score >= 80:
        return (
            "Ce profil présente une forte cohérence entre ses différentes "
            "caractéristiques. Il peut exprimer pleinement son potentiel "
            "dans un environnement adapté."
        )

    if result.score >= 50:
        return (
            "Ce profil présente plusieurs éléments favorables. "
            "Les qualités identifiées peuvent se développer avec un "
            "environnement stimulant."
        )

    return (
        "Ce profil présente des caractéristiques intéressantes qui peuvent "
        "s'exprimer progressivement selon les expériences et les choix."
    )