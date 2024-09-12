from httpx import HTTPError


class YclientsApiResponseError(HTTPError):
    def __init__(self, message: str):
        super().__init__(message)
