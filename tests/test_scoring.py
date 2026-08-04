from project_north.database.analyzer import analyze_first_name
from project_north.scoring.scorer import calculate_score


def test_calculate_score():

    first_name = analyze_first_name(
        {
            "name": "Gabriel",
            "origin": "Hebrew",
            "meaning": "Force de Dieu",
            "biblical": "true",
            "historical": "true",
            "royal": "false",
        }
    )

    score = calculate_score({}, first_name)

    assert score["score"] == 45
    assert isinstance(score["details"], list)