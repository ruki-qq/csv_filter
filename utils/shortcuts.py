from typing import Any


def is_integer(value: Any) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
