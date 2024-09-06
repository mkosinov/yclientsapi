import os

import httpx
import pytest
from dotenv import load_dotenv

from yclientsapi import YclientsAPI

load_dotenv()


@pytest.fixture(scope="session")
def get_httpx_client() -> httpx.Client:
    print("Creating HTTPX client in pytest session")
    base_url = "https://api.yclients.com/api/"
    version = "v1/"
    return httpx.Client(base_url=base_url + version)


@pytest.fixture
def init_lib() -> YclientsAPI:
    return YclientsAPI(
        company_id=int(os.getenv("company_id")),
        partner_token=os.getenv("partner_token"),
        user_login=os.getenv("user_login"),
        user_password=os.getenv("user_password"),
    )
