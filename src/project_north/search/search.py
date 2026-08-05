from project_north.database.analyzer import analyze_first_names
from project_north.database.first_names import load_first_names
from project_north.models.search_result import SearchResult
from project_north.scoring.scorer import calculate_score
from project_north.analysis.score_interpretation import interpret_score


def search_first_names(
    profile,
    settings=None,
):

    seen_names = set()

    first_names = load_first_names()
    analyzed = analyze_first_names(first_names)

    results = []

    for first_name in analyzed:

        if first_name["name"] in seen_names:
            continue

        seen_names.add(first_name["name"])

        scoring = calculate_score(
            profile,
            first_name,
            settings=settings,
        )

        results.append(
            SearchResult(
                rank=0,
                name=first_name["name"],
                expression=first_name["expression"]["expression"],
                soul=first_name["soul"]["soul"],
                personality=first_name["personality"]["personality"],
                score=scoring["score"],
                details=scoring["details"],
                interpretation=interpret_score(scoring["score"]),
            )
        )

    results.sort(
        key=lambda result: result.score,
        reverse=True,
    )

    for index, result in enumerate(results, start=1):
        result.rank = index

    return results[:50]