from project_north.reports.markdown_report import export_markdown
from project_north.models.search_result import SearchResult


def test_export_markdown(tmp_path):

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

    file_path = tmp_path / "report.md"

    export_markdown(result, file_path)

    content = file_path.read_text()

    assert "Elias" in content
    assert "Score" in content
    assert "Très forte compatibilité" in content