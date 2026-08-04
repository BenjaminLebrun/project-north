from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[3]


def load_yaml(filename):

    with open(ROOT / "config" / filename, encoding="utf-8") as f:
        return yaml.safe_load(f)