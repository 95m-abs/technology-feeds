from pathlib import Path

from dotenv import dotenv_values

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"

_config = dotenv_values(ENV_FILE)

def get_setting(name: str) -> str:
    value = _config.get(name)

    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"Missing required setting: {name}")

    return value.strip()
