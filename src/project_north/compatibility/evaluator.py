from project_north.compatibility.rules import RULES
from project_north.compatibility.weights import WEIGHTS
from project_north.compatibility.meaning import evaluate_meaning
from project_north.models.compatibility_settings import (
    CompatibilitySettings,
)


def evaluate(
    expression,
    soul,
    personality,
    metadata=None,
    settings=None,
):

    if settings is None:
        settings = CompatibilitySettings()

    base_score = 0
    bonus_score = 0
    details = []

    # Compatibilité numérologique
    if (
        settings.use_expression
        and expression in RULES["expression"]
    ):
        base_score += settings.expression_weight
        details.append(
            f"Expression {expression} : +{settings.expression_weight}"
        )

    if (
        settings.use_soul
        and soul in RULES["soul"]
    ):
        base_score += settings.soul_weight
        details.append(
            f"Âme {soul} : +{settings.soul_weight}"
        )

    if (
        settings.use_personality
        and personality in RULES["personality"]
    ):
        base_score += settings.personality_weight
        details.append(
            f"Personnalité {personality} : +{settings.personality_weight}"
        )

    # Bonus
    if metadata:

        if (
            settings.use_biblical
            and metadata.get("biblical") == "true"
        ):
            bonus_score += settings.biblical_weight
            details.append(
                f"Biblique : +{settings.biblical_weight}"
            )

        if (
            settings.use_historical
            and metadata.get("historical") == "true"
        ):
            bonus_score += settings.historical_weight
            details.append(
                f"Historique : +{settings.historical_weight}"
            )

        if (
            settings.use_royal
            and metadata.get("royal") == "true"
        ):
            bonus_score += settings.royal_weight
            details.append(
                f"Royal : +{settings.royal_weight}"
            )

        if settings.use_meaning:

            meaning_matches = evaluate_meaning(
                metadata.get("meaning")
            )

            for match in meaning_matches:

                weight = settings.meaning_weights.get(match, 0)

                bonus_score += weight

                details.append(
                    f"Signification {match} : +{weight}"
                )

    score = base_score + bonus_score

    return {
        "base_score": base_score,
        "bonus_score": bonus_score,
        "score": score,
        "details": details,
    }