from project_north.api.analyze import analyze_person


def test_api_analysis():

    result = analyze_person(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    assert (
        result["profile"]["expression"]["expression"]
        == 5
    )

    assert (
        result["interpretation"]["expression"]
        == "Liberté, mouvement, adaptation"
    )