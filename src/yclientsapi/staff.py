from yclientsapi.config import config
from yclientsapi.utils import compose_url


class Staff:
    _api_url_suffix = "staff"

    def get_staff(self):
        full_url = compose_url(self._api_url_suffix, config.yclients_company_id)
        response = self.client.get(full_url, headers=config.headers.basic, timeout=1)
        print(response.json())
