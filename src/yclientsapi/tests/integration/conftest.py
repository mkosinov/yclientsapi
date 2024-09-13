from typing import Any, Generator

import pytest

from yclientsapi import YclientsAPI
from yclientsapi.tests.integration.vars import company_id, partner_token, user_token

# @pytest.fixture(scope="session")
# def get_httpx_client() -> httpx.Client:
#     print("Creating HTTPX client in pytest session")
#     base_url = "https://api.yclients.com/api/"
#     version = "v1/"
#     return httpx.Client(base_url=base_url + version)


@pytest.fixture(scope="session")
def lib() -> Generator[YclientsAPI, Any, None]:
    with YclientsAPI(
        company_id=company_id, partner_token=partner_token, user_token=user_token
    ) as api:
        yield api
