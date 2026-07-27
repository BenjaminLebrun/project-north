from project_north.core.validators import calculate_name_value
from project_north.core.reducers import reduce_number


def calculate_expression(*names: str):
    full_name = " ".join(names)

    total = calculate_name_value(full_name)
    reduced = reduce_number(total)

    return {
        "full_name": full_name,
        "total": total,
        "expression": reduced,
    }