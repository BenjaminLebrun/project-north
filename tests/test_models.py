from project_north.models.profile import (
    NumerologyProfile,
    ProfileDate,
    ProfileIdentity,
)


def test_profile_model():

    profile = NumerologyProfile(
        identity=ProfileIdentity(
            "Benjamin Lebrun"
        ),
        birth_date=ProfileDate(
            12,
            11,
            1997,
        ),
        expression=5,
        soul=5,
        personality=9,
        life_path=4,
    )

    assert profile.expression == 5
    assert profile.life_path == 4