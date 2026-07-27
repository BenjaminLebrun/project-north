from project_north.numerology.profile import create_profile


def test_benjamin_reference_profile():

    profile = create_profile(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    assert profile["expression"]["expression"] == 5
    assert profile["soul"]["soul"] == 5
    assert profile["personality"]["personality"] == 9
    assert profile["birth_date"]["life_path"]["life_path"] == 22
