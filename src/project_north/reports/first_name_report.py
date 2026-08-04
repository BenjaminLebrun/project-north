def generate_first_name_report(results):

    report = []

    for index, result in enumerate(results, start=1):

        report.append(
            {
                "rank": index,
                "name": result["name"],
                "score": result["score"],
                "details": result["details"],
            }
        )

    return report