from project_north.compatibility.engine import evaluate_first_name


def calculate_score(profile, first_name):

    score = evaluate_first_name(first_name)

    return {
        "score": score,
        "details": [],
    }