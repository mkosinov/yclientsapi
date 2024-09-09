from typing import Sequence


def compose_url(
    api_base_url: str,
    api_version: str,
    api_url_suffix: str,
    *args: Sequence[str],
) -> str:
    return "/".join([api_base_url, api_version, api_url_suffix, *args])


class QueryDict(dict):
    """Dictionary that drops keys without values."""

    def __init__(self, d: dict):
        super().__init__({k: v for k, v in d.items() if v})
