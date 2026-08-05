from dataclasses import dataclass


@dataclass
class CompatibilitySettings:
    use_expression: bool = True
    use_soul: bool = True
    use_personality: bool = True

    use_biblical: bool = True
    use_historical: bool = True
    use_royal: bool = True

    use_meaning: bool = True