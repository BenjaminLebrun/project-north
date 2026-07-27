from project_north.core.reducers import reduce_with_masters


def calculate_life_path(day, month, year):

    day_value = reduce_with_masters(day)
    month_value = reduce_with_masters(month)
    year_value = reduce_with_masters(year)

    total = day_value + month_value + year_value

    life_path = reduce_with_masters(total)

    return {
        "day": day,
        "month": month,
        "year": year,
        "total": total,
        "life_path": life_path,
    }