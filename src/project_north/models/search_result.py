from dataclasses import dataclass, field


@dataclass
class SearchResult:
    rank: int
    name: str

    expression: int
    soul: int
    personality: int

    score: int

    base_score: int = 0
    bonus_score: int = 0

    details: list[str] = field(default_factory=list)
    interpretation: str = ""