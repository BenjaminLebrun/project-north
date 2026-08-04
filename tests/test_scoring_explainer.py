from project_north.scoring.explainer import explain_score


def test_explain_score():

    result = {
        "score": 48,
        "details": [
            "Expression 8 : +30",
            "Âme 6 : +25",
        ],
    }

    text = explain_score(result)

    assert "Score : 48" in text
    assert "Expression 8 : +30" in text
    assert "Âme 6 : +25" in text