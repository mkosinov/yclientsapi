from dataclasses import asdict
from http import HTTPMethod

import orjson

from yclientsapi.logger import log_call
from yclientsapi.schema.service_category import (
    ServiceCategoryCreateRequest,
    ServiceCategoryCreateResponse,
    ServiceCategoryGetResponse,
    ServiceCategoryListResponse,
    ServiceCategoryUpdateRequest,
)


class ServiceCategory:
    """Methods for working with ServiceCategory."""

    def __init__(self, api):
        self.__api = api

    @log_call
    def list(
        self,
    ) -> ServiceCategoryListResponse:
        """Returns list of all service categories.

        :return: ServiceCategoryListResponse
        """
        url_suffix = "/v1/company/{company_id}/service_categories/"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return ServiceCategoryListResponse(**orjson.loads(response.content))

    @log_call
    def get(
        self,
        category_id: str | int,
    ) -> ServiceCategoryGetResponse:
        """Return a single service category by its ID.

        :param category_id: ID of the service category
        :return: ServiceCategoryGetResponse
        """
        url_suffix = "/v1/service_category/{company_id}/{category_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={"category_id": category_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ServiceCategoryGetResponse(**orjson.loads(response.content))

    @log_call
    def create(
        self,
        service_category: ServiceCategoryCreateRequest,
    ) -> ServiceCategoryCreateResponse:
        """Create a new service category.

        :param service_category: Data for the new service category
        :return: ServiceCategoryCreateResponse
        """
        url_suffix = "/v1/service_categories/{company_id}"
        payload = asdict(service_category)
        response = self.__api._sender.send(
            method=HTTPMethod.POST,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ServiceCategoryCreateResponse(**orjson.loads(response.content))

    @log_call
    def update(
        self,
        category_id: str | int,
        service_category: ServiceCategoryUpdateRequest,
    ) -> ServiceCategoryGetResponse:
        """Update an existing service category by its ID.

        :param category_id: ID of the service category to update
        :param service_category: Updated data for the service category
        :return: ServiceCategoryGetResponse
        """
        url_suffix = "/v1/service_category/{company_id}/{category_id}"
        payload = asdict(service_category)
        response = self.__api._sender.send(
            method=HTTPMethod.PUT,
            url_suffix=url_suffix,
            url_params={"category_id": category_id},
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ServiceCategoryGetResponse(**orjson.loads(response.content))

    @log_call
    def delete(
        self,
        category_id: str | int,
    ) -> None:
        """Delete a service category by its ID.

        :param category_id: ID of the service category to delete
        """
        url_suffix = "/v1/service_category/{company_id}/{category_id}"
        self.__api._sender.send(
            method=HTTPMethod.DELETE,
            url_suffix=url_suffix,
            url_params={"category_id": category_id},
            headers=self.__api._headers.base_with_user_token,
        )
