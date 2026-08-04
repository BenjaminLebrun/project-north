def explain_score(result):

    lines = []

    lines.append(f"Score : {result['score']}")

    if result["details"]:

        lines.append("")

        lines.append("Détails :")

        for detail in result["details"]:
            lines.append(f"- {detail}")

    return "\n".join(lines)