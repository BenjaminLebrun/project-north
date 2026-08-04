from project_north.database.first_names import (
    load_first_names,
)


def test_load_first_names():

    names = load_first_names()

    assert len(names) >= 15
    assert names[0]["name"] == "Samuel"