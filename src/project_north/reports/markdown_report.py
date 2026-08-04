from project_north.reports.report_builder import build_report


def export_markdown(result, path):

    report = build_report(result)

    with open(path, "w", encoding="utf-8") as file:
        file.write(report)

    return path