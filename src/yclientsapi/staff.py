import orjson

from yclientsapi.schema.staff import StaffListResponse


class Staff:
    """Methods for working with staff."""

    _api_url_suffix = "/company/{company_id}/staff/{staff_id}"

    def get_staff(self, staff_id="") -> StaffListResponse:
        """Returns list of all staff or one certain staff.
        :param staff_id: id of staff. If not specified, returns list of all staff.
        :return: StaffListResponse
        """
        url = self._api_url_suffix.format(
            company_id=self.config.company_id, staff_id=staff_id
        )
        response = self.client.get(url, headers=self.headers.basic_with_user_token)
        return StaffListResponse(**orjson.loads(response.content))
