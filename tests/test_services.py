from project_north.services.profile_service import (
    generate_profile_report,
)


def test_profile_service():

    result = generate_profile_report(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    assert result["profile"]["expression"]["expression"] == 5
    assert result["profile"]["soul"]["soul"] == 5
    assert result["profile"]["personality"]["personality"] == 9