import json


def export_json(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        indent=4,
    )
