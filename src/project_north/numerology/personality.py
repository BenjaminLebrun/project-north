from project_north.core.normalizer import normalize_name
from project_north.core.reducers import reduce_number
from project_north.core.validators import (
    calculate_letters_value,
)

VOWELS = {
    "A",
    "E",
    "I",
    "O",
    "U",
    "Y",
}


def extract_consonants(name: str):
    normalized = normalize_name(name)

    return "".join(
        letter
        for letter in normalized
        if letter.isalpha()
        and letter not in VOWELS
    )


def calculate_personality(name: str):
    consonants = extract_consonants(name)

    total = calculate_letters_value(consonants)
    reduced = reduce_number(total)

    return {
        "consonants": consonants,
        "total": total,
        "personality": reduced,
    }
    