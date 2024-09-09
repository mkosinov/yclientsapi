import pytest

from yclientsapi.main import YclientsAPI
from yclientsapi.schema.activity import ActivityResponse
from yclientsapi.tests.unit.vars import activity_id


@pytest.mark.service
@pytest.mark.parametrize(
    ("params", "expected_response"),
    [({"activity_id": activity_id}, True)],
    ids=["existing_id"],
    # , "empty id", "none existing id", "wrong type"
)
def test_get_activity(lib: YclientsAPI, params, expected_response):
    activity = lib.activity.get(**params)
    assert activity.success == expected_response
    assert isinstance(activity, ActivityResponse)


def test_search_activity(lib: YclientsAPI, params, expected_response):
    activity = lib.activity.get(**params)
    assert activity.success == expected_response
    assert isinstance(activity, ActivityResponse)
