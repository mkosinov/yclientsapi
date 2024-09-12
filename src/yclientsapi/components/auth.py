import orjson

from yclientsapi.schema.auth import AuthResponse


class Auth:
    def __init__(self, api):
        self.api = api

    def authenticate(self, login: str, password: str) -> AuthResponse:
        """Send user credentials and return user token.
        Raises HTTPStatusError if status code is not 2xx.

        :param login: User's login can be a phone number in the format 79161234567 or an email
        :param password: User's password
        :return: AuthResponse
        """
        url = "/auth"
        data: dict[str, str] = {"login": login, "password": password}
        headers = self.api.headers.base
        response = self.api.client.post(url, json=data, headers=headers)
        response.raise_for_status()
        return AuthResponse(**orjson.loads(response.content))
