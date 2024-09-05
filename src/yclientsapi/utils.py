from typing import Sequence

from yclientsapi.config import config


def compose_url(
    api_url_suffix: str,
    *args: Sequence[str],
    api_base_url: str = config.api_base_url,
    api_version: str = config.api_version,
) -> str:
    return "/".join([api_base_url, api_version, api_url_suffix, *args])
