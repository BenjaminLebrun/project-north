from project_north.analysis.interpretation import create_interpretation
from project_north.numerology.profile import create_profile


def test_basic_interpretation():

    profile = create_profile(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    interpretation = create_interpretation(profile)

    assert interpretation["core"]["expression"] == 5
    assert interpretation["core"]["soul"] == 5
    assert interpretation["core"]["personality"] == 9
    assert interpretation["core"]["life_path"] == 22
