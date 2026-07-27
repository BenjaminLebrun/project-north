# Project North Numerology Specification

Version: 1.0

## Purpose

This document defines the official calculation rules used by Project North.

The objective is to make every result explainable and reproducible.

---

# 1. General Rules

## Normalization

| Calculation | Master Numbers Policy |
|-------------|-----------------------|
| Expression  | Under review |
| Soul        | Under review |
| Personality | Under review |
| Life Path   | Preserved |

Before calculation:

- Convert text to uppercase
- Remove accents
- Remove spaces
- Remove punctuation
- Keep alphabetical characters only

Example:

Benjamin Lebrun

↓

BENJAMINLEBRUN

---

# 2. Letter Values

Each letter receives a numerical value according to the Project North alphabet mapping.

Example:

B = 2
E = 5
N = 5

---

# 3. Reduction Rules

Master numbers are preserved according to the Master Numbers Policy.

Master numbers:

- 11
- 22
- 33

are handled according to the calculation context.

The exact preservation rules are defined per calculation type.

---

# 4. Master Numbers Policy

Numbers are reduced using the Project North reduction engine.

Master numbers:

- 11
- 22
- 33

are preserved according to the Master Numbers Policy.

When a calculation produces 11, 22 or 33,
the value is preserved as the primary result.

The reduced equivalent is also calculated
and stored for traceability.

Example:

Life Path calculation:

12/11/1997

Day:

12 → 3

Month:

11 → 11

Year:

1997 → 8


Calculation:

3 + 11 + 8 = 22


Result:

Primary value:

22

Reduced value:

2 + 2 = 4

Master number:

true

---
## Reduction Strategy

Project North reduces numbers by summing their digits repeatedly.

Master numbers (11, 22, 33) are preserved as primary values.

Their reduced equivalent is calculated as secondary information.

Example:

22

Primary value:
22

Reduced value:
4

# 5. Expression Number

Input:

Full normalized name.

Calculation:

1. Convert every letter into its numerical value.
2. Sum all values.
3. Apply reduction rules.

Example:

BENJAMINLEBRUN

Total:

59

Reduction:

5 + 9 = 14

1 + 4 = 5

Result:

Expression = 5

---

# 6. Soul Number

Input:

Vowels only.

Calculation:

1. Extract vowels.
2. Convert vowels into values.
3. Sum values.
4. Apply reduction rules.

Example:

EAIEU

Total:

23

Reduction:

2 + 3 = 5

Result:

Soul = 5

---

# 7. Personality Number

Input:

Consonants only.

Calculation:

1. Extract consonants.
2. Convert consonants into values.
3. Sum values.
4. Apply reduction rules.

Example:

BNJMNLBRN

Total:

36

Reduction:

3 + 6 = 9

Result:

Personality = 9

# 8. Life Path Number

Status:
IMPLEMENTED

Method:
Component Reduction with Master Number Preservation

Example:

12/11/1997

Day:
12 → 3

Month:
11 → 11

Year:
1997 → 8

3 + 11 + 8

= 22

Life Path = 22

## Historical Methods Considered

Two calculation methods were evaluated during the design phase.

Two possible methods:

### Method A — Global Reduction

day + month + year

Example:

12/11/1997

12 + 11 + 1997

= 2020

= 4


### Method B — Component Reduction

day → 3

month → 11

year → 8

3 + 11 + 8

= 22

