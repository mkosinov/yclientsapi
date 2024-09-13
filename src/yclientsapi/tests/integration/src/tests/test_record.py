import pytest

from yclientsapi import YclientsAPI
from yclientsapi.schema.record import RecordListResponse
from yclientsapi.tests.integration.src.test_data.record import Parametrize


@pytest.mark.parametrize(
    ("params", "expected_response"),
    Parametrize.list,
)
def test_list_records(lib: YclientsAPI, params, expected_response):
    records = lib.record.list(**params)
    assert records.success == expected_response["success"]
    assert isinstance(records, RecordListResponse)
    assert len(records.data) == expected_response["count"]
