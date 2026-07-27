from project_north.exporters.markdown import export_markdown


def test_markdown_export():

    result = {
        "profile": {
            "identity": {"name": "Benjamin Lebrun"},
            "expression": {"expression": 5},
            "soul": {"soul": 5},
            "personality": {"personality": 9},
            "birth_date": {"life_path": {"life_path": 4}},
        },
        "interpretation": {
            "expression": "Liberté",
            "soul": "Besoin de liberté",
            "personality": "Inspirant",
            "life_path": "Construction",
        },
    }

    output = export_markdown(result)

    assert "# Project North Profile" in output
    assert "Benjamin Lebrun" in output
    assert "Number: 5" in output
