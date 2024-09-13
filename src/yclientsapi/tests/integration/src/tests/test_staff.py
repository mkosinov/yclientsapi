from yclientsapi.schema.staff import StaffListResponse, StaffResponse
from yclientsapi.tests.integration.vars import staff_id


def test_get_all_staff(lib):
    response = lib.staff.list()
    assert response.success
    assert isinstance(response, StaffListResponse)


def test_get_one_staff_by_id(lib):
    response = lib.staff.get(staff_id=staff_id)
    assert response.success
    assert isinstance(response, StaffResponse)
