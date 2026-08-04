from project_north.models.search_result import SearchResult


def test_search_result():

    result = SearchResult(
        rank=1,
        name="Samuel",
        expression=8,
        soul=6,
        personality=4,
        score=48,
        details=[],
    )

    assert result.rank == 1
    assert result.score == 48