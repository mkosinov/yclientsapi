from http import HTTPMethod

import orjson

from yclientsapi.logger import log_call
from yclientsapi.schema.service import ServiceListResponse, ServiceResponse


class Service:
    """Methods for working with services."""

    def __init__(self, api):
        self.__api = api

    @log_call
    def list(
        self,
        category_id: str | int = "",
        staff_id: str | int = "",
    ) -> ServiceListResponse:
        """Returns list of services.

        :param category_id: id of service category
        :param staff_id: id of staff
        :return: ServiceListResponse
        """
        url_suffix = "/v1/company/{company_id}/services/"
        params = {}
        if staff_id:
            params["staff_id"] = staff_id
        if category_id:
            params["category_id"] = category_id
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={},
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ServiceListResponse(**orjson.loads(response.content))

    @log_call
    def get(
        self,
        service_id: str | int,
    ) -> ServiceResponse:
        """Returns single service.

        :param service_id: id of service
        :return: ServiceResponse
        """
        url_suffix = "/v1/company/{company_id}/services/{service_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={"service_id": service_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ServiceResponse(**orjson.loads(response.content))
