from project_north.analysis.profile_analysis import analyze_profile


def test_complete_profile_analysis():

    result = analyze_profile(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    assert result["profile"]["expression"]["expression"] == 5

    assert result["interpretation"]["expression"] == "Liberté, mouvement, adaptation"

    assert result["interpretation"]["life_path"] == "Chemin de construction"
