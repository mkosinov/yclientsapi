__all__ = ["YclientsAPI"]

import httpx

from yclientsapi.components.activity import Activity
from yclientsapi.components.auth import Auth
from yclientsapi.components.record import Record
from yclientsapi.components.salary import Salary
from yclientsapi.components.service import Service
from yclientsapi.components.staff import Staff
from yclientsapi.config import Config
from yclientsapi.headers import Headers


class YclientsAPI:
    """Class collection of methods for Yclients API.

    :param company_id: company id. Required.
    :param partner_token: partner token. Required.
    :param user_token: user token (leave empty if you want to supply user login and password)
    :param user_login: user login (can be phone number or email. leave empty if you supply user token)
    :param user_password: user password (leave empty if you supply user token)

    Use with context manager:
    with YclientsAPI(*args, **kwargs) as api:
        api.staff.get()

    README https://github.com/mkosinov/yclientsapi
    """

    def __init__(
        self,
        company_id: int | str,
        partner_token: str,
        user_token: str = "",
        user_login: str = "",
        user_password: str = "",
    ):
        self.config: Config = Config(company_id)
        self.client = httpx.Client(base_url=self.config.api_base_url)
        self.collect_api_methods()
        self.headers = Headers(partner_token, user_token)
        if not user_token:
            self.headers._user_token = self.auth.authenticate(
                user_login, user_password
            ).user_token

    def collect_api_methods(self):
        self.auth = Auth(self)
        self.staff = Staff(self)
        self.service = Service(self)
        self.activity = Activity(self)
        self.record = Record(self)
        self.salary = Salary(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
