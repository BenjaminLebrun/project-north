from project_north.reports.first_name_report import generate_first_name_report


def test_generate_first_name_report():

    results = [
        {
            "name": "Samuel",
            "score": 48,
            "details": [
                "Expression 8 : +30"
            ],
        }
    ]

    report = generate_first_name_report(results)

    assert report[0]["rank"] == 1
    assert report[0]["name"] == "Samuel"
    assert report[0]["score"] == 48