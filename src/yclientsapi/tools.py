from collections.abc import Iterable
from typing import Any


def build_params(
    locals_dict: dict[str, Any], exclude: Iterable[str] = ("self")
) -> dict:
    """
    Builds a dictionary of parameters by filtering out specified keys and falsy values from the provided locals dictionary.
    Args:
        locals_dict (dict): Dictionary typically obtained from `locals()`, containing local variables.
    Returns:
        dict: A dictionary containing key-value pairs from `locals_dict` where the key is not in `exclude` and the value is truthy.
    """

    return {k: v for k, v in locals_dict.items() if k not in exclude and v}
