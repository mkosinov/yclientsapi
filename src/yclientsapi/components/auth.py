from http import HTTPMethod
from typing import TYPE_CHECKING

import orjson

if TYPE_CHECKING:
    from yclientsapi import YclientsAPI

from yclientsapi.exceptions import YclientsApiResponseError
from yclientsapi.logger import log_call
from yclientsapi.schema.auth import AuthResponse


class Auth:
    def __init__(self, api):
        self.__api: YclientsAPI = api

    @log_call
    def authenticate(self, login: str, password: str) -> AuthResponse:
        """Send user login and password and save user token for further requests.
        Raises HTTPStatusError if status code is not 2xx.

        :param login: User's login can be a phone number in the format 79161234567 or an email
        :param password: User's password
        :return: AuthResponse
        """
        if not login or not password:
            raise ValueError("Login and password are required")
        url_suffix = "/v1/auth"
        data: dict[str, str] = {"login": login, "password": password}
        response = self.__api._sender.send(
            method=HTTPMethod.POST,
            url_suffix=url_suffix,
            headers=self.__api._headers.base,
            json=data,
        )
        result = AuthResponse(**orjson.loads(response.content))
        if result.success:
            self.__api._headers._user_token = result.data.user_token
            return result
        else:
            raise YclientsApiResponseError("No user token in response")
