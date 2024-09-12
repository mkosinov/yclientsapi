import orjson

from yclientsapi.schema.staff import StaffListResponse


class Staff:
    """Methods for working with staff."""

    _api_url_suffix = "/company/{company_id}/staff/{staff_id}"

    def __init__(self, api):
        self.api = api

    def get(self, staff_id: str | int = "") -> StaffListResponse:
        """Returns list of all staff or one certain staff.
        Raises HTTPStatusError if status code is not OK.
        :param staff_id: id of staff. If not specified, returns list of all staff.
        :return: StaffListResponse
        """
        url = self._api_url_suffix.format(
            company_id=self.api.config.company_id, staff_id=staff_id
        )
        response = self.api.client.get(
            url, headers=self.api.headers.basic_with_user_token
        )
        response.raise_for_status()
        return StaffListResponse(**orjson.loads(response.content))
