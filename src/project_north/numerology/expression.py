from project_north.core.reducers import reduce_number
from project_north.core.validators import (
    calculate_letters_details,
    calculate_name_value,
)


def calculate_expression(*names: str):
    full_name = " ".join(names)

    details = calculate_letters_details(full_name.upper())

    total = calculate_name_value(full_name)
    reduced = reduce_number(total)

    return {
        "full_name": full_name,
        "details": details,
        "total": total,
        "expression": reduced,
    }