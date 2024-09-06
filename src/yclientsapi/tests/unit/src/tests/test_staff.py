from yclientsapi.schema.staff import StaffListResponse


def test_get_staff(init_lib):
    staff = init_lib.get_staff()
    assert staff.success
    assert isinstance(staff, StaffListResponse)
