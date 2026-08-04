from project_north.search.search import search_first_names


def test_search_first_names():

    results = search_first_names({})

    assert len(results) == 5

    scores = [
        result["score"]
        for result in results
    ]

    assert scores == sorted(
        scores,
        reverse=True,
    )

def test_search_limit():

    results = search_first_names({})

    assert len(results) <= 50