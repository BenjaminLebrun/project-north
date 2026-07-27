from .constants import MASTER_NUMBERS


def reduce_number(number):
    while number > 9 and number not in MASTER_NUMBERS:
        number = sum(int(digit) for digit in str(number))
    return number
