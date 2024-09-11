from datetime import datetime

import orjson

from yclientsapi.schema.activity import (
    ActivityDeleteResponse,
    ActivityResponse,
    ActivitySearchListResponse,
)


class Activity:
    """Methods for working with activity."""

    def __init__(self, api):
        self.api = api

    def create(
        self,
        date: datetime,
        service_id: int,
        staff_id: int,
        capacity: int,
        resource_instance_ids: list[int] | None = None,
        force: bool = False,
        length: int | None = None,
        color: str | None = None,
        label_ids: list[int] | None = None,
        comment: str | None = None,
        stream_link: str | None = None,
        instructions: str | None = None,
    ) -> ActivityResponse:
        """Create activity.
        :param date: date and time. Required.
        :param service_id: id of service. Required.
        :param staff_id: id of staff. Required.
        :param capacity: capacity of activity. Required.
        :param resource_instance_ids: list of resource instance ids. Optional.
        :param force: ignore errors (staff/resource busy, etc.). Required.
        :param length: length of activity in seconds. Optional.
        :param color: color of activity. Optional.
        :param label_ids: list of label ids. Optional.
        :param comment: comment for activity. Optional.
        :param stream_link: link to online activity. Optional.
        :param instructions: instructions for activity. Optional.
        :return: ActivityResponse
        """
        api_url_suffix = "/activity/{company_id}"
        url = api_url_suffix.format(company_id=self.api.config.company_id)
        body = {
            "date": date,
            "service_id": service_id,
            "staff_id": staff_id,
            "capacity": capacity,
            "resource_instance_ids": resource_instance_ids,
            "force": force,
            "length": length,
            "color": color,
            "label_ids": label_ids,
            "comment": comment,
            "stream_link": stream_link,
            "instructions": instructions,
        }
        response = self.api.client.post(
            url, json=body, headers=self.api.headers.basic_with_user_token
        )
        return ActivityResponse(**orjson.loads(response.content))

    def delete(self, activity_id: str | int) -> ActivityDeleteResponse:
        """Delete activity.
        :param activity_id: id of activity. Required.
        :return: ActivityDeleteResponse
        """
        api_url_suffix = "/activity/{company_id}/{activity_id}"
        url = api_url_suffix.format(
            company_id=self.api.config.company_id, activity_id=activity_id
        )
        response = self.api.client.delete(
            url, headers=self.api.headers.basic_with_user_token
        )
        return ActivityDeleteResponse(**orjson.loads(response.content))

    def get(self, activity_id: str | int) -> ActivityResponse:
        """Returns activity.
        :param activity_id: id of activity. Required.
        :return: StaffListResponse
        """
        url_suffix = "/activity/{company_id}/{activity_id}".format(
            company_id=self.api.config.company_id, activity_id=activity_id
        )
        response = self.api.client.get(
            url_suffix, headers=self.api.headers.basic_with_user_token
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
        api_url_suffix = "/activity/{company_id}/search/"
        response = self.api.client.get(
            api_url_suffix.format(company_id=self.api.config.company_id),
            params=params,
            headers=self.api.headers.basic_with_partner_token,
        )
        return ActivitySearchListResponse(**orjson.loads(response.content))
