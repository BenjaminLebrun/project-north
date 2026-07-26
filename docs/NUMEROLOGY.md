# Numerology

## Scope

The first symbolic model implemented by Project North is the Pythagorean Numerology system.

The implementation focuses on reproducibility and transparency.

Every calculation is deterministic.

---

# Supported Calculations (v1)

Identity

- Expression Number
- Soul Urge Number
- Personality Number
- Maturity Number

Birth

- Life Path Number

Master Numbers

- 11
- 22
- 33

Future versions may introduce:

- Pinnacles
- Challenges
- Personal Year
- Personal Month
- Personal Day
- Inclusion Grid
- Karmic Lessons
- Karmic Debts
- Balance Number
- Hidden Passion
- Rational Thought
- Planes of Expression

---

# Reduction Rules

Default reduction:

Example:

38

↓

3 + 8 = 11

↓

11

Master numbers are preserved.

Master numbers:

- 11
- 22
- 33

All other values are reduced to a single digit.

Example

29

↓

2 + 9 = 11

↓

11

Example

38

↓

3 + 8 = 11

↓

11

Example

49

↓

4 + 9 = 13

↓

1 + 3 = 4

---

# Alphabet

Default alphabet:

Pythagorean

| Number | Letters |
|----------|----------|
| 1 | A J S |
| 2 | B K T |
| 3 | C L U |
| 4 | D M V |
| 5 | E N W |
| 6 | F O X |
| 7 | G P Y |
| 8 | H Q Z |
| 9 | I R |

Accented letters are normalized.

Examples:

É → E

À → A

Ç → C

Ü → U

---

# Vowels

Default vowels:

A

E

I

O

U

Y

Y behaves as a vowel in the default implementation.

Future versions may support configurable vowel rules.

---

# Consonants

Every non-vowel alphabetic character.

---

# Formula

Expression

All letters

Soul

Vowels only

Personality

Consonants only

Maturity

Life Path + Expression

---

# School

Identifier

pythagorean-v1

Version

1.0.0

---

# References

This document intentionally separates:

- formulas;
- implementation;
- interpretation.

Project North implements formulas.

Interpretation belongs to higher-level modules.
