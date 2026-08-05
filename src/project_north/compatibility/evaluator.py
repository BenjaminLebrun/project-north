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

    score = 0
    details = []

    if (
        settings.use_expression
        and expression in RULES["expression"]
    ):
        score += WEIGHTS["expression"]
        details.append(
            f"Expression {expression} : +{WEIGHTS['expression']}"
        )

    if (
        settings.use_soul
        and soul in RULES["soul"]
    ):
        score += WEIGHTS["soul"]
        details.append(
            f"Âme {soul} : +{WEIGHTS['soul']}"
        )

    if (
        settings.use_personality
        and personality in RULES["personality"]
    ):
        score += WEIGHTS["personality"]
        details.append(
            f"Personnalité {personality} : +{WEIGHTS['personality']}"
        )

    if metadata:

        if (
            settings.use_biblical
            and metadata.get("biblical") == "true"
        ):
            score += WEIGHTS["biblical"]
            details.append(
                f"Biblique : +{WEIGHTS['biblical']}"
            )

        if (
            settings.use_historical
            and metadata.get("historical") == "true"
        ):
            score += WEIGHTS["historical"]
            details.append(
                f"Historique : +{WEIGHTS['historical']}"
            )

        if (
            settings.use_royal
            and metadata.get("royal") == "true"
        ):
            score += WEIGHTS["royal"]
            details.append(
                f"Royal : +{WEIGHTS['royal']}"
            )

        if settings.use_meaning:

            meaning_matches = evaluate_meaning(
                metadata.get("meaning")
            )


            for match in meaning_matches:

                score += WEIGHTS["meaning"][match]

                details.append(
                    f"Signification {match} : +{WEIGHTS['meaning'][match]}"
                )
            

    return {
        "score": score,
        "details": details,
    }