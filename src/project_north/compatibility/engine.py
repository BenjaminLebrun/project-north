from project_north.compatibility.evaluator import evaluate


def evaluate_first_name(first_name):

    expression = first_name.expression
    soul = first_name.soul
    personality = first_name.personality

    return evaluate(
        expression,
        soul,
        personality,
    )