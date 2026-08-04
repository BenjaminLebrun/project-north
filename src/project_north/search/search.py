from project_north.database.analyzer import analyze_first_names
from project_north.database.first_names import load_first_names
from project_north.scoring.scorer import calculate_score


def search_first_names(profile):

    first_names = load_first_names()

    analyzed = analyze_first_names(first_names)

    results = []

    for first_name in analyzed:

        score = calculate_score(
            profile,
            first_name,
        )

        results.append(
            {
                **first_name,
                "score": score,
            }
        )

    return results