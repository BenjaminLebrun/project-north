# Scoring

## Purpose

The scoring engine ranks symbolic candidates according to configurable rules.

It never determines truth.

It measures coherence with a selected identity profile.

---

# Scoring Philosophy

Every score is:

- deterministic;
- explainable;
- configurable;
- versioned.

No hidden weights.

No implicit bonuses.

Every point awarded must be documented.

---

# Score Components

A score is the sum of independent components.

Example:

Overall Score

=

Numerology Score

+

Symbolism Score

+

Identity Score

+

Custom Bonuses

-

Penalties

---

# Default Components

## Numerology

- Expression
- Soul Urge
- Personality
- Maturity
- Master Numbers

---

## Symbolism

- Meaning
- Origin
- Historical significance
- Archetype

---

## Identity

Compatibility with:

- Constitution
- Values
- Objectives
- Archetype

---

# Configuration

Weights are stored outside the source code.

Example

weights.json

```
{
  "expression": 25,
  "soul": 20,
  "personality": 20,
  "maturity": 10,
  "master_numbers": 15,
  "symbolism": 10
}
```

---

# Explainability

Every recommendation must expose:

- raw values;
- intermediate scores;
- applied bonuses;
- applied penalties;
- final score.

Example

```
Nathan

Expression

8

+25

Soul

6

+20

Personality

4

+18

Master Number

22

+15

Meaning

Gift

+5

Final Score

83
```

---

# Profiles

Different identity profiles may use different scoring configurations.

Example

builder.json

teacher.json

researcher.json

guardian.json

creator.json

Each profile defines its own priorities.

---

# Versioning

Every scoring model has an identifier.

Example

scoring-v1

Future versions must preserve previous implementations.

---

# Goal

The objective of the scoring engine is not to choose.

It is to assist reflection by producing transparent rankings.
