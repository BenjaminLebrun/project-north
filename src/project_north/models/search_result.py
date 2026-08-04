from dataclasses import dataclass


@dataclass
class SearchResult:

    rank: int

    name: str

    expression: int

    soul: int

    personality: int

    score: int

    details: list[str]