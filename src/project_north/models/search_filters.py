from dataclasses import dataclass


@dataclass
class SearchFilters:
    gender: str | None = None