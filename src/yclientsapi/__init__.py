from __future__ import annotations

import logging

from yclientsapi.config import Config
from yclientsapi.exceptions import YclientsApiResponseError  # noqa: F401
from yclientsapi.headers import Headers
from yclientsapi.sender import HttpxSender

__all__ = ["YclientsAPI"]


class YclientsAPI:
    """Class collection of methods for Yclients API.

    :param company_id: company id.
    :param partner_token: partner token.
    :param user_token: user token. Optional. But reqired for many api calls.
    :param logger: logger for logging. Optional. If not provided, default logger will be used.
    :param config_dict: dictionary for changing default dataclass config (extra fields in response). Optional.

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
        logger: logging.Logger | None = None,
        config_dict: dict | None = None,
    ):
        config_dict = config_dict or {}
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger("yclientsapi")
        self._config: Config = Config(company_id, **config_dict)
        self._headers: Headers = Headers(partner_token, user_token)
        self._sender: HttpxSender = HttpxSender(self)
        self.__collect_api_methods()

    def __collect_api_methods(self):
        from yclientsapi.components.activity import Activity
        from yclientsapi.components.auth import Auth
        from yclientsapi.components.duplication import Duplication
        from yclientsapi.components.record import Record
        from yclientsapi.components.salary import Salary
        from yclientsapi.components.service import Service
        from yclientsapi.components.service_category import ServiceCategory
        from yclientsapi.components.staff import Staff
        from yclientsapi.components.storage import Storage

        self.auth = Auth(self)
        self.staff = Staff(self)
        self.service = Service(self)
        self.service_category = ServiceCategory(self)
        self.activity = Activity(self)
        self.record = Record(self)
        self.salary = Salary(self)
        self.storage = Storage(self)
        self.duplication = Duplication(self)

    def __enter__(self):
        self._sender.create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sender.close_session()
