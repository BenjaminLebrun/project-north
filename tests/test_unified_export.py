from project_north.export.exporter import export_profile


def test_unified_json_export():

    result = {
        "profile": {
            "identity": {
                "name": "Benjamin Lebrun"
            }
        }
    }

    output = export_profile(result, "json")

    assert "Benjamin Lebrun" in output


def test_unified_invalid_format():

    result = {}

    try:
        export_profile(result, "xml")
    except ValueError as error:
        assert "Unsupported export format" in str(error)
    else:
        assert False