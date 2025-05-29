from collections.abc import Generator
from typing import Any

import pytest

from yclientsapi import YclientsAPI
from yclientsapi.tests.integration.vars import (
    company_id,
    partner_token,
    user_token,
)


@pytest.fixture(scope="session")
def lib() -> Generator[YclientsAPI, Any, None]:
    """Fixture that provides an instance of YclientsAPI for testing.

    The fixture is scoped to the test session and uses context manager
    to ensure proper cleanup of resources.
    """
    with YclientsAPI(
        company_id=company_id,
        partner_token=partner_token,
        user_token=user_token,
    ) as api:
        yield api
