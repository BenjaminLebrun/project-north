def build_report(result):
    return f"""
{result.name}
{'=' * len(result.name)}

Score : {result.score}
Interprétation : {result.interpretation}

Détails :

""" + "\n".join(f"- {detail}" for detail in result.details)