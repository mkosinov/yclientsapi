from typing import NoReturn


class Headers:
    _content_type_json = "application/json"
    _accept_json = "application/vnd.api.v2+json"
    _authorization = "Bearer {bearer},User {bearer}"

    @property
    def basic(self, bearer: str, user_token: str) -> dict[str, str]:
        return {
            "Content-Type": self._content_type_json,
            "Accept": self._accept_json,
            "Authorization": self._authorization.format(bearer, user_token),
        }

    @basic.setter
    def basic(self) -> NoReturn:
        raise AttributeError


class Config:
    api_base_url = "https://api.yclients.com/api/"
    api_version = "v1"
    headers = Headers()

    def __init__(self, company_id: str, bearer: str, user_token: str):
        self.company_id = company_id
        self.bearer = bearer
        self.user_token = user_token
