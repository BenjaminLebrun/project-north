from project_north.numerology.life_path import calculate_life_path


def analyze_birth_date(day: int, month: int, year: int):

    life_path = calculate_life_path(
        day,
        month,
        year,
    )

    return {
        "date": {
            "day": day,
            "month": month,
            "year": year,
        },
        "life_path": life_path,
    }