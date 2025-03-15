from __future__ import annotations

from yclientsapi.config import Config
from yclientsapi.headers import Headers
from yclientsapi.sender import httpxSender

__all__ = ["YclientsAPI"]


class YclientsAPI:
    """Class collection of methods for Yclients API.

    :param company_id: company id.
    :param partner_token: partner token.
    :param user_token: user token. Optional. But reqired for many api calls.
    :param ConfigDict: dictionary for changing default config. Optional.

    If no user_token is provided, you can call auth.authenticate() later to retrive and save user_token for futher requests.

    Usage:

    ```python
    >>> from yclientsapi import YclientsAPI
    >>> with YclientsAPI(12345, "partner_token_12345") as api:
    >>>     api.auth.authenticate("user_login", "user_password")
    >>>     staff_obj = api.staff.get(123)
    ```

    README https://github.com/mkosinov/yclientsapi
    """

    def __init__(
        self,
        company_id: int | str,
        partner_token: str,
        user_token: str = "",
        ConfigDict: dict | None = None,
    ):
        ConfigDict = ConfigDict or {}
        self._config: Config = Config(company_id, **ConfigDict)
        self._headers: Headers = Headers(partner_token, user_token)
        self._sender: httpxSender = httpxSender(self)
        self.__collect_api_methods()

    def __collect_api_methods(self):
        from yclientsapi.components.activity import Activity
        from yclientsapi.components.auth import Auth
        from yclientsapi.components.record import Record
        from yclientsapi.components.salary import Salary
        from yclientsapi.components.service import Service
        from yclientsapi.components.service_category import ServiceCategory
        from yclientsapi.components.staff import Staff

        self.auth = Auth(self)
        self.staff = Staff(self)
        self.service = Service(self)
        self.service_category = ServiceCategory(self)
        self.activity = Activity(self)
        self.record = Record(self)
        self.salary = Salary(self)

    def __enter__(self):
        self._sender.create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sender.close_session()
