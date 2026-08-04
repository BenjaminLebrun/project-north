from project_north.reports.report_builder import build_report
from project_north.models.search_result import SearchResult


def test_build_report():

    result = SearchResult(
        rank=1,
        name="Elias",
        expression=1,
        soul=6,
        personality=4,
        score=90,
        interpretation="Très forte compatibilité",
        details=[
            "Expression 1 : +30",
            "Âme 6 : +25",
        ],
    )

    report = build_report(result)

    assert isinstance(report, str)
    assert "Elias" in report
    assert "Score" in report
    assert "Très forte compatibilité" in report