# Project North API

## Profile Analysis

Generate a complete numerology profile.

Input:

- Full name
- Birth day
- Birth month
- Birth year

Output:

- Expression number
- Soul number
- Personality number
- Life path number
- Interpretations

Example:

```python
from project_north.api.analyze import analyze_person

result = analyze_person(
    "Benjamin Lebrun",
    12,
    11,
    1997,
)