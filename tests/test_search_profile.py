from project_north.models.search_profile import SearchProfile


def test_search_profile():

    profile = SearchProfile(
        expression=5,
        soul=5,
        personality=9,
        life_path=22,
    )

    assert profile.expression == 5
    assert profile.life_path == 22