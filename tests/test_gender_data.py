from project_north.database.first_names import load_first_names
from project_north.search.search import search_first_names
from project_north.models.search_profile import SearchProfile
from project_north.models.search_filters import SearchFilters


def test_gender_exists():

    names = load_first_names()

    assert all(
        "gender" in name
        for name in names
    )

def test_male_includes_unisex():

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

    names = [
        result.name
        for result in results
    ]

    assert "Camille" in names
    assert "Robin" in names
    assert "Charlie" in names
    assert "Noa" in names

def test_male_excludes_female():

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

    names = [
        result.name
        for result in results
    ]

    assert "Emma" not in names
    assert "Marie" not in names