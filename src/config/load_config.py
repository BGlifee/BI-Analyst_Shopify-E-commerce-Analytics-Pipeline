from pathlib import Path
import toml


def load_config(path: str | None = None) -> dict:
    if path is None:
        path = Path(__file__).resolve().parents[2] / "config.toml"
    return toml.load(path)