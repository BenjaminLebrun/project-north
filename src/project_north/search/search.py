from project_north.database.analyzer import analyze_first_names
from project_north.database.first_names import load_first_names
from project_north.models.search_result import SearchResult
from project_north.scoring.scorer import calculate_score
from project_north.analysis.score_interpretation import interpret_score


def search_first_names(
    profile,
    settings=None,
    filters=None,
):
    if filters is None:
        from project_north.models.search_filters import SearchFilters

        filters = SearchFilters()
    
    seen_names = set()

    first_names = load_first_names()
    analyzed = analyze_first_names(first_names)

    results = []

    for first_name in analyzed:

        if first_name["name"] in seen_names:
            continue

        seen_names.add(first_name["name"])

        if filters.gender:
            gender = first_name.get("gender", "unknown")

            if filters.gender == "male":
                if gender not in ("male", "unisex"):
                    continue

            elif filters.gender == "female":
                if gender not in ("female", "unisex"):
                    continue

            elif filters.gender == "unisex":
                if gender != "unisex":
                    continue

        if filters.expression_values:
            if (
                first_name["expression"]["expression"]
                not in filters.expression_values
            ):
                continue

        if filters.soul_values:
            if (
                first_name["soul"]["soul"]
                not in filters.soul_values
            ):
                continue

        if filters.personality_values:
            if (
                first_name["personality"]["personality"]
                not in filters.personality_values
            ):
                continue

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

                base_score=scoring["base_score"],
                bonus_score=scoring["bonus_score"],
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