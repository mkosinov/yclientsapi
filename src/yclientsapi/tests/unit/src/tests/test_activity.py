from datetime import UTC, datetime, timedelta

import pytest

from yclientsapi.main import YclientsAPI
from yclientsapi.schema.activity import ActivityDeleteResponse, ActivityResponse
from yclientsapi.tests.unit.src.test_data.real.activity import Parametrize
from yclientsapi.tests.unit.vars import resource_id, service_id, staff_id


@pytest.mark.service
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.get,
)
def test_get_activity(lib: YclientsAPI, params, expected_response):
    activity = lib.activity.get(**params)
    assert activity.success == expected_response
    assert isinstance(activity, ActivityResponse)


@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.search,
)
def test_search_activity(lib: YclientsAPI, params, expected_response):
    activity = lib.activity.search(**params)
    assert activity.success == expected_response
    assert isinstance(activity, ActivityResponse)


def test_create_delete_activity(lib: YclientsAPI):
    response = lib.activity.create(
        service_id=service_id,
        staff_id=staff_id,
        resource_id=resource_id,
        start=datetime.now(tz=UTC) + timedelta(days=10),
        end=datetime.now(tz=UTC) + timedelta(days=11),
        comment="yclients api automated integration test.",
    )
    assert response.success
    assert isinstance(response, ActivityResponse)

    response = lib.activity.delete(response.data.id)
    assert response.success
    assert isinstance(response, ActivityDeleteResponse)
