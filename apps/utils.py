import json
import tomllib
import os

from datetime import datetime as dt
from pathlib import Path
from typing import Optional, Union

def resolve_path(path_str):
    """
    RESOLVE PATH
    """
    path = Path(path_str)
    if path_str.startswith('~/'):
        return path.expanduser().resolve()
    elif not path.is_absolute():
        base_dir = Path(__file__).resolve().parent
        return (base_dir / path).resolve()
    else:
        return path.resolve()

def load_data(path_str: str | Path, ext: str) -> dict:
    """
    LOADED DATA JSON or TOML
    """
    try:
        path = resolve_path(path_str)

        if ext == "json":
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        elif ext == "toml":
            with open(path, "rb") as f:
                return tomllib.load(f)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

    except Exception as e:
        print("Error loading file:", e)
        return {}

def cln_screen():
    """
    CLEAR SCREEN
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        print(f"Don't Know How to clean screen on {nm} System")

def date(fmt: str = "simple", when: Optional[Union[dt, str]] = None) -> str:
    """
    DATE TIME
    """
    try:
        # Handle waktu
        if not when:
            now = dt.now()
        elif isinstance(when, str):
            now = dt.fromisoformat(when)
        elif isinstance(when, dt):
            now = when
        else:
            return "[invalid datetime]"

        # Handle format
        if fmt == "iso":
            return now.astimezone().replace(microsecond=0).isoformat()
        elif fmt == "simple":
            return now.strftime("%Y-%m-%d")
        else:
            return now.strftime(fmt)
    except Exception:
        return "[invalid format]"

