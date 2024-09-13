from typing import NoReturn

from httpx import HTTPError


class YclientsApiResponseError(HTTPError):
    def __init__(self, message: str) -> NoReturn:
        super().__init__(message)
