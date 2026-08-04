from project_north.compatibility.evaluator import evaluate


def test_evaluator():

    score = evaluate(
        expression=8,
        soul=6,
        personality=4,
    )

    assert score == 75