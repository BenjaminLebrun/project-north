from project_north.compatibility.evaluator import evaluate


def evaluate_first_name(
        first_name,
        settings=None,
    ):

    if isinstance(first_name, dict):

        expression = first_name["expression"]["expression"]
        soul = first_name["soul"]["soul"]
        personality = first_name["personality"]["personality"]

    else:

        expression = first_name.expression
        soul = first_name.soul
        personality = first_name.personality

    return evaluate(
      expression,
      soul,
      personality,
      first_name,
      settings=settings,
    )