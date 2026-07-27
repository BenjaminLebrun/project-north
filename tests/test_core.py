from project_north.core.reducers import reduce_number


def test_reduce_38():
    assert reduce_number(38) == 11


def test_reduce_49():
    assert reduce_number(49) == 4


def test_reduce_22():
    assert reduce_number(22) == 22


def test_reduce_33():
    assert reduce_number(33) == 33