import pytest

from yclientsapi import YclientsAPI
from yclientsapi.schema.activity import ActivityResponse, ActivitySearchListResponse
from yclientsapi.tests.integration.src.test_data.activity import Parametrize


@pytest.mark.service
@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.get,
)
def test_get_activity(lib, params, expected_response):
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
    assert isinstance(activity, ActivitySearchListResponse)
