from project_north.search.search import search_first_names


def test_search_first_names():

    results = search_first_names({})

    assert len(results) == 5

    assert "score" in results[0]

    assert isinstance(
        results[0]["score"],
        int,
    )