# Architecture

## Purpose

Project North is organized around the concept of Identity.

Identity is the core domain.

Every symbolic system is implemented as an independent module.

---

# Layers

```
Application
    │
    ▼
Identity Engine
    │
    ├── Constitution
    ├── Values
    ├── Archetypes
    ├── Objectives
    │
    ▼
Symbolic Modules
    ├── Pythagorean Numerology
    ├── Chaldean Numerology
    ├── Name Symbolism
    ├── Future Modules...
    │
    ▼
Scoring Engine
    │
    ▼
Reports
```

---

# Domain

The domain language is shared across the entire project.

Core entities:

- Person
- Identity
- Constitution
- Value
- Principle
- Archetype
- Symbolic Model
- Analysis
- Recommendation
- Score
- Report

---

# Design Principles

- Composition over inheritance.
- Pure functions whenever possible.
- Immutable value objects.
- Explicit dependencies.
- Reproducible calculations.
- Versioned algorithms.

---

# Modules

The framework is divided into independent packages.

Example:

```
project_north/

core/

identity/

schools/

datasets/

scoring/

reports/

cli/
```

Every symbolic system lives inside the `schools` package.

---

# Dependency Rule

Dependencies always point inward.

```
CLI

↓

Application

↓

Identity Engine

↓

Schools

↓

Core
```

Core never depends on higher layers.

Schools never know the CLI.

Reports never perform calculations.

---

# Configuration

No hard-coded weights.

No hard-coded scoring.

Everything configurable through dedicated configuration files.

---

# Testing

Every public calculation must have unit tests.

Every documented example should become an automated test whenever possible.

---

# Future

Project North is designed as a framework.

New symbolic systems should be installable without modifying the core engine.
