from dataclasses import asdict
from http import HTTPMethod

import orjson

from yclientsapi import YclientsAPI
from yclientsapi.logger import log_call
from yclientsapi.schema.activity import (
    ActivityCreate,
    ActivityDatesListResponse,
    ActivityDatesRangeResponse,
    ActivityDeleteResponse,
    ActivityFiltersResponse,
    ActivityGroupServicesResponse,
    ActivityResponse,
    ActivitySearchListResponse,
)
from yclientsapi.tools import build_params


class Activity:
    """Methods for working with activity."""

    def __init__(self, api: YclientsAPI):
        self.__api: YclientsAPI = api

    @log_call
    def get(self, activity_id: str | int) -> ActivityResponse:
        """Returns details of group activity by id.
        :param activity_id: id of activity. Required.
        :return: ActivityResponse
        """
        url_suffix = "/v1/activity/{company_id}/{activity_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={"activity_id": activity_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ActivityResponse(**orjson.loads(response.content))

    @log_call
    def search(
        self,
        from_: str,
        till: str,
        service_ids: list[int] | list[str] | None = None,
        staff_ids: list[int] | list[str] | None = None,
        resource_ids: list[int] | list[str] | None = None,
        page: str | int = "",
        count: str | int = "",
    ) -> ActivitySearchListResponse:
        """Returns activities search results. Can search only in future online activities.
        :param from_: date from in format %Y-%m-%d. Required.
        :param till: date to in format %Y-%m-%d. Required.
        :param service_ids: list of service ids. Optional.
        :param staff_ids: list of staff ids. Optional.
        :param resource_ids: list of resource ids. Optional.
        :return: ActivitySearchListResponse
        """
        params = build_params(locals(), exclude=("self", "from_"))
        params["from"] = from_
        url_suffix = "/v1/activity/{company_id}/search"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ActivitySearchListResponse(**orjson.loads(response.content))

    @log_call
    def create(self, activity: ActivityCreate) -> ActivityResponse:
        """Creates a new activity (group event).
        :param activity: ActivityCreate dataclass with all parameters for the activity creation.
        :return: ActivityResponse
        """
        payload = asdict(activity)
        url_suffix = "/v1/activity/{company_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.POST,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ActivityResponse(**orjson.loads(response.content))

    @log_call
    def update(self, activity_id: int, activity: ActivityCreate) -> ActivityResponse:
        """Updates an existing activity (group event).
        :param activity_id: ID of the activity to update (required)
        :param activity: ActivityCreate dataclass with all parameters for the update
        :return: ActivityResponse
        """
        payload = asdict(activity)
        url_suffix = "/v1/activity/{company_id}/{activity_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.PUT,
            url_suffix=url_suffix,
            url_params={"activity_id": activity_id},
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ActivityResponse(**orjson.loads(response.content))

    @log_call
    def delete(self, activity_id: int) -> ActivityDeleteResponse:
        """Deletes a activity by id.
        :param activity_id: ID of the activity to delete (required)
        :return: ActivityDeleteResponse
        """
        url_suffix = "/v1/activity/{company_id}/{activity_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.DELETE,
            url_suffix=url_suffix,
            url_params={"activity_id": activity_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ActivityDeleteResponse(**orjson.loads(response.content))

    @log_call
    def filters(
        self,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
    ) -> ActivityFiltersResponse:
        """Get filters for activities.
        :param service_ids: List of service IDs (optional)
        :param staff_ids: List of staff IDs (optional)
        :param resource_ids: List of resource IDs (optional)
        :return: ActivityFiltersResponse
        """
        params = build_params(locals(), exclude=("self"))
        url_suffix = "/v1/activity/{company_id}/filters/"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ActivityFiltersResponse(**orjson.loads(response.content))

    @log_call
    def search_dates_range(
        self,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
    ) -> ActivityDatesRangeResponse:
        """Get min and max dates for activities.
        :param service_ids: List of service IDs (optional)
        :param staff_ids: List of staff IDs (optional)
        :param resource_ids: List of resource IDs (optional)
        :return: ActivityDatesRangeResponse
        """
        params = build_params(locals(), exclude=("self"))
        url_suffix = "/v1/activity/{company_id}/search_dates_range/"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ActivityDatesRangeResponse(**orjson.loads(response.content))

    @log_call
    def search_dates(
        self,
        from_: str,
        till: str,
        service_ids: list[int] | None = None,
        staff_ids: list[int] | None = None,
        resource_ids: list[int] | None = None,
    ) -> ActivityDatesListResponse:
        """Get available activity dates in a range.
        :param from_: Start date (YYYY-MM-DD, required)
        :param till: End date (YYYY-MM-DD, required)
        :param service_ids: List of service IDs (optional)
        :param staff_ids: List of staff IDs (optional)
        :param resource_ids: List of resource IDs (optional)
        :return: ActivityDatesListResponse
        """
        params = build_params(locals(), exclude=("self", "from_"))
        params["from"] = from_
        url_suffix = "/v1/activity/{company_id}/search_dates/"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ActivityDatesListResponse(**orjson.loads(response.content))

    @log_call
    def group_services(
        self,
        staff_id: int | None = None,
        term: str | None = None,
    ) -> ActivityGroupServicesResponse:
        """Search for group services.
        :param staff_id: Staff ID for filtering (optional)
        :param term: Search by service name or part of name (optional)
        :return: ActivityGroupServicesResponse
        """
        params = build_params(locals(), exclude=("self"))
        url_suffix = "/v1/activity/{company_id}/services"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ActivityGroupServicesResponse(**orjson.loads(response.content))
