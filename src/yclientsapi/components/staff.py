from __future__ import annotations

from http import HTTPMethod
from typing import TYPE_CHECKING

import orjson

from yclientsapi.logger import log_call
from yclientsapi.schema.staff import StaffListResponse, StaffResponse

if TYPE_CHECKING:
    from yclientsapi import YclientsAPI


class Staff:
    """Methods for working with staff."""

    def __init__(self, api):
        self.__api: YclientsAPI = api

    @log_call
    def get(self, staff_id: str | int) -> StaffResponse:
        """Returns one staff.

        :param staff_id: id of staff.
        :return: StaffResponse
        """
        url_suffix = "/v1/company/{company_id}/staff/{staff_id}"
        url_params = {"staff_id": staff_id}
        response = self.__api._sender.send(
            HTTPMethod.GET,
            url_suffix,
            url_params,
            headers=self.__api._headers.base_with_user_token,
        )
        return StaffResponse(**orjson.loads(response.content))

    @log_call
    def list(self, staff_id: str | int = "") -> StaffListResponse:
        """Returns list of all staff.

        :return: StaffListResponse
        """
        url_suffix = "/v1/company/{company_id}/staff/"
        response = self.__api._sender.send(
            HTTPMethod.GET,
            url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return StaffListResponse(**orjson.loads(response.content))
