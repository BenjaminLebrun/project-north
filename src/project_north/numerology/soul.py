from project_north.core.validators import (
    calculate_letters_value,
)
from project_north.core.reducers import reduce_number
from project_north.core.normalizer import normalize_name


VOWELS = {
    "A",
    "E",
    "I",
    "O",
    "U",
    "Y",
}


def extract_vowels(name: str):
    normalized = normalize_name(name)

    return "".join(
        letter
        for letter in normalized
        if letter in VOWELS
    )


def calculate_soul(name: str):
    vowels = extract_vowels(name)

    total = calculate_letters_value(vowels)
    reduced = reduce_number(total)

    return {
        "vowels": vowels,
        "total": total,
        "soul": reduced,
    }
    