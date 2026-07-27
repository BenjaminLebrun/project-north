from project_north.core.validators import calculate_name_value
from project_north.core.reducers import reduce_number


def calculate_expression(full_name: str):
    total = calculate_name_value(full_name)
    reduced = reduce_number(total)

    return {
        "total": total,
        "expression": reduced,
    }
    