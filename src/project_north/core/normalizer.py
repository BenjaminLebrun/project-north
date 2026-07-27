from unidecode import unidecode


def normalize_name(name):
    return unidecode(name).upper()
