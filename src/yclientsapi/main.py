import httpx

from yclientsapi.activity import Activity
from yclientsapi.auth import Auth
from yclientsapi.config import Config
from yclientsapi.headers import Headers
from yclientsapi.record import Record
from yclientsapi.salary import Salary
from yclientsapi.service import Service
from yclientsapi.staff import Staff


class YclientsAPI:
    """Send requests to Yclients API.
    Use with context manager:
    with YclientsAPI(*args, **kwargs) as api:
        api.staff.get()

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
        self.headers = Headers(partner_token, user_token)
        if not user_token:
            self.headers._user_token = self.get_user_token(user_login, user_password)
        self.compose_api_methods()

    def compose_api_methods(self):
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
