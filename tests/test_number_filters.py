from project_north.models.search_filters import SearchFilters
from project_north.models.search_profile import SearchProfile
from project_north.search.search import search_first_names


def test_expression_filter():

    profile = SearchProfile(
        expression=5,
        soul=5,
        personality=9,
        life_path=22,
    )

    results = search_first_names(
        profile,
        filters=SearchFilters(
            expression_values=[5],
        ),
    )

    assert results

    assert all(
        result.expression == 5
        for result in results
    )


def test_soul_filter():

    profile = SearchProfile(
        expression=5,
        soul=5,
        personality=9,
        life_path=22,
    )

    results = search_first_names(
        profile,
        filters=SearchFilters(
            soul_values=[6],
        ),
    )

    assert results

    assert all(
        result.soul == 6
        for result in results
    )


def test_personality_filter():

    profile = SearchProfile(
        expression=5,
        soul=5,
        personality=9,
        life_path=22,
    )

    results = search_first_names(
        profile,
        filters=SearchFilters(
            personality_values=[4],
        ),
    )

    assert results

    assert all(
        result.personality == 4
        for result in results
    )