from project_north.export.json_exporter import (
    export_json,
)


def test_json_export():

    data = {
        "expression": 5,
        "soul": 5,
    }

    result = export_json(data)

    assert '"expression": 5' in result
    assert '"soul": 5' in result
