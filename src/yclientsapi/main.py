import httpx

from yclientsapi.config import Config
from yclientsapi.staff import Staff


class YclientsAPI(Staff):
    """Send requests to Yclients API.
    Use with context manager:
    with YclientsAPI(company_id, bearer, user_token) as api:
        api.get_staff()

    """

    def __init__(self, company_id: str, bearer: str, user_token: str):
        self.config: Config = Config(company_id, bearer, user_token)
        self.client = httpx.Client(base_url=self.config.api_base_url)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
