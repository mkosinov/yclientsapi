import orjson

from yclientsapi.exceptions import BaseError


class Auth:
    _url_suffix = "auth"

    def get_user_token(self, login: str, password: str) -> str:
        """Send user credentials and return user token or raise HTTPStatusError.
        Raises HTTPStatusError if status code is not ACCEPTED.
        :param login: В качестве логина может быть использован номер телефона пользователя в формате 79161234567 или его Email
        :param password: Пароль пользователя
        """
        api_version = "v1"
        url = "/".join((self.config.api_base_url, api_version, self._url_suffix))
        data: dict[str, str] = {"login": login, "password": password}
        headers = (
            self.headers.content_type
            | self.headers.accept
            | self.headers.authorization_partner
        )
        response = self.client.post(url, json=data, headers=headers)
        response.raise_for_status()
        user_token = (
            orjson.loads(response.content).get("data", {}).get("user_token", None)
        )
        if user_token is None:
            raise BaseError("User token not found")
        return user_token
