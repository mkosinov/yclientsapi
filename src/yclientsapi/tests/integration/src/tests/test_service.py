import pytest

from yclientsapi.schema.service import ServiceListResponse, ServiceResponse
from yclientsapi.tests.integration.vars import service_category_id, service_id, staff_id


@pytest.mark.service
@pytest.mark.parametrize(
    "params",
    [
        {"category_id": service_category_id},
        {"staff_id": staff_id},
        {"category_id": service_category_id, "staff_id": staff_id},
    ],
    ids=["category_id", "staff_id", "category_id, staff_id"],
)
def test_list_service(lib, params):
    service = lib.service.list(**params)
    assert service.success
    assert isinstance(service, ServiceListResponse)


@pytest.mark.service
@pytest.mark.parametrize(
    "params",
    [
        {"service_id": service_id},
    ],
    ids=["service_id"],
)
def test_get_service(lib, params):
    service = lib.service.get(**params)
    assert service.success
    assert isinstance(service, ServiceResponse)
