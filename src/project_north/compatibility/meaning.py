from project_north.core.config import load_yaml

MEANING_RULES = load_yaml("meaning_rules.yaml")

MEANING_KEYWORDS = {
    "light": [
        "light",
        "lum",
    ],
    "peace": [
        "peace",
        "rest",
    ],
    "wisdom": [
        "wisdom",
        "judge",
    ],
    "builder": [
        "build",
        "add",
        "guardian",
        "protector",
    ],
    "strength": [
        "strong",
        "strength",
        "rock",
        "warrior",
    ],
}


def evaluate_meaning(meaning):

    if not meaning:
        return []

    meaning = meaning.lower()

    matches = []

    for category, keywords in MEANING_RULES.items():

        for keyword in keywords:

            if keyword in meaning:
                matches.append(category)
                break

    return matches