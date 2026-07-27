from .alphabet import PYTHAGOREAN_ALPHABET
from .normalizer import normalize_name


def calculate_letters_value(word):
    total = 0

    for letter in word:
        if letter in PYTHAGOREAN_ALPHABET:
            total += PYTHAGOREAN_ALPHABET[letter]

    return total


def calculate_name_value(name):
    normalized = normalize_name(name)
    return calculate_letters_value(normalized)


def calculate_letters_details(word):
    details = []

    for letter in word:
        if letter in PYTHAGOREAN_ALPHABET:
            details.append((letter, PYTHAGOREAN_ALPHABET[letter]))

    return details
