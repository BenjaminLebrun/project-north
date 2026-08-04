def summary(result):
    return f"""# {result.name}

Score : {result.score}
Interprétation : {result.interpretation}
"""


def details(result):
    return "\n".join(f"- {detail}" for detail in result.details)

from project_north.reports.strengths import strengths

def strengths_section(result):
    values = strengths(result)

    if not values:
        return "## Points forts\n\nAucun point fort identifié."

    return "## Points forts\n\n" + "\n".join(f"- {item}" for item in values)


from project_north.reports.warnings import warnings


def warnings_section(result):

    values = warnings(result)

    if not values:
        return "## Points de vigilance\n\nAucun point de vigilance identifié."

    return "## Points de vigilance\n\n" + "\n".join(
        f"- {item}" for item in values
    )


from project_north.reports.recommendations import recommendations


def recommendations_section(result):

    values = recommendations(result)

    if not values:
        return "## Recommandations\n\nAucune recommandation disponible."

    return "## Recommandations\n\n" + "\n".join(
        f"- {item}" for item in values
    )

from project_north.reports.conclusion import conclusion


def conclusion_section(result):

    return "## Conclusion\n\n" + conclusion(result)