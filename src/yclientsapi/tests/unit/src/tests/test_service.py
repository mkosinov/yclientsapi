import pytest

from yclientsapi.schema.service import ServiceListResponse
from yclientsapi.tests.unit.vars import service_category_id, service_id, staff_id


@pytest.mark.service
@pytest.mark.parametrize(
    "params",
    [
        {"service_id": service_id},
        {"category_id": service_category_id},
        {"staff_id": staff_id},
        {"service_id": service_id, "staff_id": staff_id},
    ],
    ids=["service_id", "category_id", "staff_id", "service_id, staff_id"],
)
def test_get_service(lib, params):
    service = lib.service.get(**params)
    assert service.success
    assert isinstance(service, ServiceListResponse)


# def test_get_one_service(lib):
#     service = lib.service.get(service_id=os.getenv("SERVICE_ID"))
#     assert service.success
#     assert isinstance(service, ServiceListResponse)


# def test_get_one_category(lib):
#     service = lib.service.get(service_id=os.getenv("SERVICE_CATEGORY_ID"))
#     assert service.success
#     assert isinstance(service, ServiceListResponse)
