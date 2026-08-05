from project_north.search.search import search_first_names
from project_north.models.search_profile import SearchProfile
from project_north.models.search_filters import SearchFilters


def test_gender_filter_male():

    profile = SearchProfile(
        expression=5,
        soul=5,
        personality=9,
        life_path=22,
    )

    filters = SearchFilters(
        gender="male",
    )

    results = search_first_names(
        profile,
        filters=filters,
    )

    assert len(results) > 0