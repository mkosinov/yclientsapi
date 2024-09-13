import orjson

from yclientsapi.schema.service_category import (
    ServiceCategoryListResponse,
    ServiceCategoryResponse,
)


class ServiceCategory:
    """Methods for working with ServiceCategory."""

    def __init__(self, api):
        self.__api = api

    def list(
        self,
    ) -> ServiceCategoryListResponse:
        """Returns list of all service categories.

        :return: ServiceCategoryListResponse
        """
        url_suffix = "/company/{company_id}/service_categories/"
        response = self.__api._sender.send(
            method="GET",
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return ServiceCategoryListResponse(**orjson.loads(response.content))

    def get(
        self,
        category_id: str | int,
    ) -> ServiceCategoryResponse:
        """Returns service category.

        :param category_id: id of service category
        :return: ServiceCategoryResponse
        """
        url_suffix = "/company/{company_id}/service_categories/{category_id}"
        response = self.__api._sender.send(
            method="GET",
            url_suffix=url_suffix,
            url_params={"category_id": category_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ServiceCategoryResponse(**orjson.loads(response.content))
