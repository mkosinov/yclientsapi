from yclientsapi.schema.staff import StaffListResponse
from yclientsapi.tests.integration.vars import staff_id


def test_get_all_staff(lib):
    staff = lib.staff.get()
    assert staff.success
    assert isinstance(staff, StaffListResponse)


def test_get_one_staff_by_id(lib):
    staff = lib.staff.get(staff_id=staff_id)
    assert staff.success
    assert isinstance(staff, StaffListResponse)
