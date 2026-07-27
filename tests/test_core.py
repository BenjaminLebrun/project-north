from project_north.core.reducers import reduce_number


def test_reduce_38():
    assert reduce_number(38) == 11


def test_reduce_49():
    assert reduce_number(49) == 4


def test_reduce_22():
    assert reduce_number(22) == 22


def test_reduce_33():
    assert reduce_number(33) == 33


from project_north.numerology.expression import calculate_expression


def test_expression_benjamin_lebrun():
    result = calculate_expression("Benjamin Lebrun")

    assert result["total"] == 59
    assert result["expression"] == 5


def test_expression_multiple_names():
    result = calculate_expression(
        "Benjamin",
        "Samuel",
        "Lebrun",
    )

    assert result["full_name"] == "Benjamin Samuel Lebrun"
    assert result["total"] == 92
    assert result["expression"] == 11