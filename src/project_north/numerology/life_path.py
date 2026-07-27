from project_north.core.reducers import reduce_number


def calculate_life_path(day: int, month: int, year: int):
    total = (
        sum(int(digit) for digit in str(day))
        + sum(int(digit) for digit in str(month))
        + sum(int(digit) for digit in str(year))
    )

    reduced = reduce_number(total)

    return {
        "day": day,
        "month": month,
        "year": year,
        "total": total,
        "life_path": reduced,
    }
