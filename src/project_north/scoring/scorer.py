from project_north.compatibility.engine import evaluate_first_name


def calculate_score(
    profile,
    first_name,
    settings=None,
):

    result = evaluate_first_name(
    first_name,
    settings=settings,
)
    return result