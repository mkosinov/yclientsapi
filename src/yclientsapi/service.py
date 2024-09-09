from typing import Union

import orjson

from yclientsapi.schema.service import ServiceListResponse


class Service:
    """Methods for working with services."""

    api_url_suffix = "/company/{company_id}/services/{service_id}"

    def __init__(self, api):
        self.api = api

    def get(
        self,
        service_id: Union[str, int] = "",
        category_id: Union[str, int] = "",
        staff_id: Union[str, int] = "",
    ) -> ServiceListResponse:
        """Returns list of all services or one certain service.
        :param service_id: id of service
        :param category_id: id of service category
        :param staff_id: id of staff
        :return: ServiceListResponse
        """
        url = self.api_url_suffix.format(
            company_id=self.api.config.company_id, service_id=service_id
        )
        params = {}
        if staff_id:
            params["staff_id"] = staff_id
        if category_id:
            params["category_id"] = category_id
        response = self.api.client.get(
            url,
            params=params,
            headers=self.api.headers.basic_with_user_token,
        )
        return ServiceListResponse(**orjson.loads(response.content))


class ServiceCategory:
    """Methods for working with ServiceCategory."""

    api_url_suffix = "/company/{company_id}/service_categories/{category_id}"

    def __init__(self, api):
        self.api = api

    def get(
        self,
        category_id: Union[str, int] = "",
        staff_id: Union[str, int] = "",
    ) -> ServiceListResponse:
        """Returns list of all service_categories or one certain service_category.
        :param category_id: id of service category
        :param staff_id: id of staff
        :return: ServiceListResponse
        """
        url = self.api_url_suffix.format(
            company_id=self.api.config.company_id, category_id=category_id
        )
        params = {}
        if staff_id:
            params["staff_id"] = staff_id
        if category_id:
            params["category_id"] = category_id
        response = self.api.client.get(
            url,
            params=params,
            headers=self.api.headers.basic_with_user_token,
        )
        return ServiceListResponse(**orjson.loads(response.content))
