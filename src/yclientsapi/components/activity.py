from __future__ import annotations

import orjson

from yclientsapi import YclientsAPI
from yclientsapi.schema.activity import ActivityResponse, ActivitySearchListResponse


class Activity:
    """Methods for working with activity."""

    def __init__(self, api):
        self.__api: YclientsAPI = api

    def get(self, activity_id: str | int) -> ActivityResponse:
        """Returns details of group activity by id.
        :param activity_id: id of activity. Required.
        :return: ActivityResponse
        """
        url_suffix = "/activity/{company_id}/{activity_id}/"
        response = self.__api._sender.send(
            method="GET",
            url_suffix=url_suffix,
            url_params={"activity_id": activity_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ActivityResponse(**orjson.loads(response.content))

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
        """Returns activities search results. Can search only in future activities.
        :param from: date from in format %Y-%m-%d. Required.
        :param till: date to in format %Y-%m-%d. Required.
        :param service_ids: list of service ids. Optional.
        :param staff_ids: list of staff ids. Optional.
        :param resource_ids: list of resource ids. Optional.
        :return: ActivitySearchListResponse
        """
        params = {}
        for arg, value in locals().items():
            if arg not in ("self", "params") and value:
                params[arg] = value
        url_suffix = "/activity/{company_id}/search/"
        response = self.__api._sender.send(
            method="GET",
            url_suffix=url_suffix,
            url_params={},
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return ActivitySearchListResponse(**orjson.loads(response.content))
