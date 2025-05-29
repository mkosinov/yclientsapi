import logging

import httpx
import pytest

from yclientsapi import YclientsAPI
from yclientsapi.tests.integration.src.test_data.duplication import Parametrize


def _default_duplication_strategy_payload():
    return Parametrize.create_duplication_strategy[0].values[0]["strategy"]


@pytest.fixture
def duplication_strategy_create(lib: YclientsAPI, request):
    """
    Fixture that creates a duplication strategy.

    Creates a strategy using the parameters from the _default_duplication_strategy_payload,
    returns the strategy ID for the test to use.
    """

    response = lib.duplication.create_duplication_strategy(
        strategy=_default_duplication_strategy_payload()
    )
    strategy_id = response.data.id

    return strategy_id


@pytest.fixture
def duplication_strategy_create_cleanup_fixt(lib: YclientsAPI, request):
    """
    Fixture that creates a duplication strategy for testing.

    Creates a strategy using the parameters from _default_duplication_strategy_payload,
    yields the strategy ID for the test to use,
    and then cleans up by deleting the strategy.
    """

    response = lib.duplication.create_duplication_strategy(
        strategy=_default_duplication_strategy_payload()
    )
    strategy_id = response.data.id
    yield strategy_id
    try:
        lib.duplication.delete_duplication_strategy(strategy_id=strategy_id)
    except httpx.HTTPStatusError as err:
        logging.critical(
            f"Failed to clean up duplication strategy {strategy_id}: {err!s}"
        )
