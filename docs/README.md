# Project North Documentation

## Overview

- [Vision](VISION.md)
- [Philosophy](PHILOSOPHY.md)
- [Architecture](ARCHITECTURE.md)

## Specifications

- [Numerology Specification](NUMEROLOGY_SPECIFICATION.md)
- [Scoring](SCORING.md)

## Examples

- [Calculation Examples](CALCULATION_EXAMPLES.md)
- [Reference Profiles](REFERENCE_PROFILES.md)

## Development

- [API](API.md)
- [Changelog](CHANGELOG.md)

# Project North

An open-source numerology research engine written in Python.

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## Features

- Expression Number
- Soul Number
- Personality Number
- Life Path Number
- Interpretation Engine
- CLI
- JSON Export
- Markdown Export

## Installation

```bash
git clone <repository>

cd project-north

make install
```

## Usage

```bash
make run
```

ou

```bash
python src/project_north/cli/main.py "Benjamin Lebrun" 12 11 1997
```

## Tests

```bash
make test
```

## Documentation

See the `docs/` directory.

## Project Structure

```text
src/
tests/
docs/
├── API.md
├── ARCHITECTURE.md
├── CALCULATION_EXAMPLES.md
├── CHANGELOG.md
├── NUMEROLOGY_SPECIFICATION.md
├── PHILOSOPHY.md
├── REFERENCE_PROFILES.md
├── SCORING.md
└── VISION.md
research/
```

## License

MIT License

Copyright (c) 2026 Benjamin Lebrun

Permission is hereby granted, free of charge, to any person obtaining a copy...