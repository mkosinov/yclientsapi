import orjson

from yclientsapi.exceptions import BaseError


class Auth:
    api_url_suffix = "/auth"

    def __init__(self, api):
        self.__api = api

    def get_user_token(self, login: str, password: str) -> str:
        """Send user credentials and return user token or raise HTTPStatusError.
        Raises HTTPStatusError if status code is not OK.
        :param login: В качестве логина может быть использован номер телефона пользователя в формате 79161234567 или его Email
        :param password: Пароль пользователя
        """
        url = self.api_url_suffix
        data: dict[str, str] = {"login": login, "password": password}
        headers = (
            self.__api.headers.content_type
            | self.__api.headers.accept
            | self.__api.headers.authorization_partner
        )
        response = self.__api.client.post(url, json=data, headers=headers)
        response.raise_for_status()
        user_token = (
            orjson.loads(response.content).get("data", {}).get("user_token", None)
        )
        if user_token is None:
            raise BaseError("No user token returned in response from yclients")
        return user_token
