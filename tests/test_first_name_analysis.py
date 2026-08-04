from project_north.database.analyzer import (
    analyze_first_name,
    analyze_first_names,
)
from project_north.database.first_names import load_first_names


def test_analyze_first_name():

    result = analyze_first_name(
        {
            "name": "Gabriel",
            "origin": "Hebrew",
            "meaning": "Force de Dieu",
            "biblical": "true",
            "historical": "true",
            "royal": "false",
        }
    )

    assert result["name"] == "Gabriel"

    assert "expression" in result
    assert "soul" in result
    assert "personality" in result


def test_analyze_first_names():

    first_names = load_first_names()

    results = analyze_first_names(first_names)

    assert len(results) == len(first_names)

    assert "expression" in results[0]
    assert "soul" in results[0]
    assert "personality" in results[0]