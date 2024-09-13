import orjson

from yclientsapi import YclientsAPI
from yclientsapi.schema.staff import StaffListResponse, StaffResponse


class Staff:
    """Methods for working with staff."""

    def __init__(self, api):
        self.__api: YclientsAPI = api

    def get(self, staff_id: str | int) -> StaffResponse:
        """Returns one staff.

        :param staff_id: id of staff.
        :return: StaffResponse
        """
        url_suffix = "/company/{company_id}/staff/{staff_id}"
        url_params = {"staff_id": staff_id}
        response = self.__api._sender.send(
            "GET",
            url_suffix,
            url_params,
            headers=self.__api._headers.base_with_user_token,
        )
        return StaffResponse(**orjson.loads(response.content))

    def list(self, staff_id: str | int = "") -> StaffListResponse:
        """Returns list of all staff.

        :return: StaffListResponse
        """
        url_suffix = "/company/{company_id}/staff/"
        response = self.__api._sender.send(
            "GET",
            url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return StaffListResponse(**orjson.loads(response.content))
