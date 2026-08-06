from dataclasses import dataclass, field


@dataclass
class CompatibilitySettings:

    # Activation des critères numérologiques
    use_expression: bool = True
    use_soul: bool = True
    use_personality: bool = True

    # Activation des bonus
    use_biblical: bool = True
    use_historical: bool = True
    use_royal: bool = True
    use_meaning: bool = True

    # Poids de la numérologie
    expression_weight: int = 30
    soul_weight: int = 25
    personality_weight: int = 20

    # Poids des bonus
    biblical_weight: int = 10
    historical_weight: int = 5
    royal_weight: int = 5

    @classmethod
    def numerology_only(cls):
        return cls(
            use_biblical=False,
            use_historical=False,
            use_royal=False,
            use_meaning=False,
        )

    @classmethod
    def full(cls):
        return cls()

    meaning_weights: dict = field(
        default_factory=lambda: {
            "force": 10,
            "sagesse": 10,
            "protection": 10,
        }
    )