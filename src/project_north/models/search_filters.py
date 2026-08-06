from dataclasses import dataclass


@dataclass
class SearchFilters:
    gender: str | None = None

    expression_values: list[int] | None = None
    soul_values: list[int] | None = None
    personality_values: list[int] | None = None

    expression: int | None = None
    soul: int | None = None
    personality: int | None = None