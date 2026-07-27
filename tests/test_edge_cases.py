from project_north.core.normalizer import normalize_name
from project_north.core.reducers import reduce_number


def test_master_number_reduction():

    assert reduce_number(11) == 11
    assert reduce_number(22) == 22
    assert reduce_number(33) == 33


def test_large_number_reduction():

    assert reduce_number(999) == 9


def test_normalization_accents():

    assert normalize_name("Élodie") == "ELODIE"


def test_normalization_spaces():

    assert normalize_name("Jean-Pierre") == "JEANPIERRE"