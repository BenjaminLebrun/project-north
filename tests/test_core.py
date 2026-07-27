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
    assert result["total"] == 76
    assert result["expression"] == 4


from project_north.numerology.soul import calculate_soul


def test_soul_benjamin_lebrun():
    result = calculate_soul("Benjamin Lebrun")

    assert result["vowels"] == "EAIEU"
    assert result["total"] == 23
    assert result["soul"] == 5


from project_north.numerology.personality import calculate_personality


def test_personality_benjamin_lebrun():
    result = calculate_personality("Benjamin Lebrun")

    assert result["consonants"] == "BNJMNLBRN"
    assert result["total"] == 36
    assert result["personality"] == 9


from project_north.numerology.master_numbers import is_master_number


def test_master_numbers():
    assert is_master_number(11)
    assert is_master_number(22)
    assert is_master_number(33)


def test_non_master_number():
    assert not is_master_number(5)
    assert not is_master_number(44)


from project_north.numerology.life_path import calculate_life_path


def test_life_path_benjamin():
    result = calculate_life_path(
        12,
        11,
        1997,
    )

    assert result["total"] == 22
    assert result["life_path"] == 22


from project_north.numerology.birth_date import analyze_birth_date


def test_birth_date_analysis():

    result = analyze_birth_date(
        12,
        11,
        1997,
    )

    assert result["date"]["day"] == 12
    assert result["date"]["month"] == 11
    assert result["date"]["year"] == 1997

    assert result["life_path"]["life_path"] == 22

def test_life_path_master_number():

    result = analyze_birth_date(12, 11, 1997)

    assert result["life_path"]["life_path"] == 22


from project_north.numerology.profile import create_profile


def test_full_profile():

    profile = create_profile(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    assert profile["identity"]["name"] == "Benjamin Lebrun"

    assert profile["expression"]["expression"] == 5
    assert profile["soul"]["soul"] == 5
    assert profile["personality"]["personality"] == 9
    assert profile["birth_date"]["life_path"]["life_path"] == 22
