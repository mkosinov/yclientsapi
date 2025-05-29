import logging

import pytest

from yclientsapi import YclientsAPI
from yclientsapi.schema.activity import ActivityDeleteResponse
from yclientsapi.schema.duplication import (
    ActivityDuplicationStrategyCreateResponse,
    ActivityDuplicationStrategyResponse,
)
from yclientsapi.tests.integration.src.test_data.duplication import Parametrize

pytest_plugins = [
    "src.yclientsapi.tests.integration.src.fixtures.fixt_activity",
    "src.yclientsapi.tests.integration.src.fixtures.fixt_duplication",
]


@pytest.mark.duplication
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.list_duplication_strategies,
)
def test_list_duplication_strategies(lib: YclientsAPI, params, expected_response):
    response = lib.duplication.list_duplication_strategies()
    assert response.success == expected_response
    assert isinstance(response, ActivityDuplicationStrategyResponse)


@pytest.mark.duplication
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.create_duplication_strategy,
)
def test_create_duplication_strategy(
    lib: YclientsAPI,
    params,
    expected_response,
    request,
):
    response = lib.duplication.create_duplication_strategy(**params)

    def cleanup():
        try:
            lib.duplication.delete_duplication_strategy(strategy_id=response.data.id)
        except Exception as e:
            logging.critical(
                f"Failed to clean up duplication strategy {response.data.id}: {e!s}"
            )

    request.addfinalizer(cleanup)

    assert response.success == expected_response
    assert isinstance(response, ActivityDuplicationStrategyCreateResponse)


@pytest.mark.duplication
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.update_duplication_strategy,
)
def test_update_duplication_strategy(
    lib: YclientsAPI,
    params,
    expected_response,
    duplication_strategy_create_cleanup_fixt,
):
    strategy_id = duplication_strategy_create_cleanup_fixt
    update_response = lib.duplication.update_duplication_strategy(
        strategy_id=strategy_id, **params
    )
    assert update_response.success == expected_response
    assert isinstance(update_response, ActivityDuplicationStrategyCreateResponse)

    strategies = lib.duplication.list_duplication_strategies()
    updated_strategy = next(s for s in strategies.data if s.id == strategy_id)
    expected_strategy = params["strategy"]
    assert updated_strategy.title == expected_strategy.title
    assert updated_strategy.repeat_mode_id == expected_strategy.repeat_mode_id
    assert updated_strategy.days == expected_strategy.days
    assert updated_strategy.interval == expected_strategy.interval
    assert updated_strategy.content_type == expected_strategy.content_type


@pytest.mark.duplication
def test_delete_duplication_strategy(lib: YclientsAPI, duplication_strategy_create):
    strategy_id = duplication_strategy_create
    delete_response = lib.duplication.delete_duplication_strategy(
        strategy_id=strategy_id
    )
    assert delete_response.success is True
    assert isinstance(delete_response, ActivityDeleteResponse)


@pytest.mark.duplication
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.duplicate,
)
def test_duplicate(
    lib: YclientsAPI,
    params,
    expected_response,
    activity_create_and_cleanup_fixt,
    request,
):
    """
    Skipped: The correct input JSON format for the duplication API call is unknown.
    This test will be enabled once the correct payload structure is determined.
    """
    pytest.skip("Skipping: unknown correct input JSON format for duplication API call.")
    # The rest of the test logic is left for future implementation.
