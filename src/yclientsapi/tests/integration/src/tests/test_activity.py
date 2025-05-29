import logging

import pytest

from yclientsapi import YclientsAPI
from yclientsapi.schema.activity import (
    ActivityDatesListResponse,
    ActivityDatesRangeResponse,
    ActivityDeleteResponse,
    ActivityFiltersResponse,
    ActivityGroupServicesResponse,
    ActivityResponse,
    ActivitySearchListResponse,
)
from yclientsapi.tests.integration.src.test_data.activity import Parametrize

pytest_plugins = [
    "src.yclientsapi.tests.integration.src.fixtures.fixt_activity",
]


@pytest.mark.activity
def test_get_activity(lib, activity_create_and_cleanup_fixt):
    activity_id = activity_create_and_cleanup_fixt
    activity = lib.activity.get(activity_id=activity_id)
    assert activity.success is True
    assert isinstance(activity, ActivityResponse)


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.search,
)
def test_search_activity(
    lib: YclientsAPI,
    params,
    expected_response,
    activity_create_and_cleanup_fixt,
):
    activity_id = activity_create_and_cleanup_fixt
    created_activity = lib.activity.get(activity_id=activity_id)
    activity_date = created_activity.data.date.strftime("%Y-%m-%d")

    search_params = {
        "from_": activity_date,
        "till": activity_date,
    }

    search_results = lib.activity.search(**search_params)

    assert search_results.success == expected_response
    assert isinstance(search_results, ActivitySearchListResponse)

    found = False
    for activity in search_results.data:
        if activity.id == activity_id:
            found = True
            break

    assert found


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.create,
)
def test_create_activity(lib: YclientsAPI, params, expected_response, request):
    activity = lib.activity.create(**params)
    activity_id = activity.data.id

    def cleanup():
        try:
            lib.activity.delete(activity_id=activity_id)
        except Exception as e:
            logging.critical(f"Failed to clean up activity {activity_id}: {e!s}")

    request.addfinalizer(cleanup)

    assert activity.success == expected_response
    assert isinstance(activity, ActivityResponse)


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.create,
)
def test_update_activity(
    lib: YclientsAPI,
    params,
    expected_response,
    activity_create_and_cleanup_fixt,
):
    activity_id = activity_create_and_cleanup_fixt

    activity = lib.activity.update(activity_id=activity_id, **params)
    assert activity.success == expected_response
    assert isinstance(activity, ActivityResponse)


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.filters,
)
def test_filters(lib: YclientsAPI, params, expected_response):
    response = lib.activity.filters(**params)
    assert response.success == expected_response
    assert isinstance(response, ActivityFiltersResponse)


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.search_dates_range,
)
def test_search_dates_range(lib: YclientsAPI, params, expected_response):
    response = lib.activity.search_dates_range(**params)
    assert response.success == expected_response
    assert isinstance(response, ActivityDatesRangeResponse)


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.search_dates,
)
def test_search_dates(lib: YclientsAPI, params, expected_response):
    response = lib.activity.search_dates(**params)
    assert response.success == expected_response
    assert isinstance(response, ActivityDatesListResponse)


@pytest.mark.activity
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.group_services,
)
def test_group_services(lib: YclientsAPI, params, expected_response):
    response = lib.activity.group_services(**params)
    assert response.success == expected_response
    assert isinstance(response, ActivityGroupServicesResponse)


@pytest.mark.activity
def test_delete_activity(lib: YclientsAPI, activity_create_fixt):
    """Test deleting an activity."""
    activity_id = activity_create_fixt

    response = lib.activity.delete(activity_id=activity_id)
    assert response.success is True
    assert isinstance(response, ActivityDeleteResponse)
