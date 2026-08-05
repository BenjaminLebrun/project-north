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
        base_score += WEIGHTS["expression"]
        details.append(
            f"Expression {expression} : +{WEIGHTS['expression']}"
        )

    if (
        settings.use_soul
        and soul in RULES["soul"]
    ):
        base_score += WEIGHTS["soul"]
        details.append(
            f"Âme {soul} : +{WEIGHTS['soul']}"
        )

    if (
        settings.use_personality
        and personality in RULES["personality"]
    ):
        base_score += WEIGHTS["personality"]
        details.append(
            f"Personnalité {personality} : +{WEIGHTS['personality']}"
        )

    # Bonus
    if metadata:

        if (
            settings.use_biblical
            and metadata.get("biblical") == "true"
        ):
            bonus_score += WEIGHTS["biblical"]
            details.append(
                f"Biblique : +{WEIGHTS['biblical']}"
            )

        if (
            settings.use_historical
            and metadata.get("historical") == "true"
        ):
            bonus_score += WEIGHTS["historical"]
            details.append(
                f"Historique : +{WEIGHTS['historical']}"
            )

        if (
            settings.use_royal
            and metadata.get("royal") == "true"
        ):
            bonus_score += WEIGHTS["royal"]
            details.append(
                f"Royal : +{WEIGHTS['royal']}"
            )

        if settings.use_meaning:

            meaning_matches = evaluate_meaning(
                metadata.get("meaning")
            )

            for match in meaning_matches:

                bonus_score += WEIGHTS["meaning"][match]

                details.append(
                    f"Signification {match} : +{WEIGHTS['meaning'][match]}"
                )

    score = base_score + bonus_score

    return {
        "base_score": base_score,
        "bonus_score": bonus_score,
        "score": score,
        "details": details,
    }