import orjson

from yclientsapi.schema.activity import ActivityResponse, ActivitySearchListResponse


class Activity:
    """Methods for working with activity."""

    def __init__(self, api):
        self.api = api

    def get(self, activity_id: str | int) -> ActivityResponse:
        """Returns activity.
        :param activity_id: id of activity. Required.
        :return: StaffListResponse
        """
        api_url_suffix = "/activity/{company_id}/{activity_id}"
        url = api_url_suffix.format(
            company_id=self.api.config.company_id, activity_id=activity_id
        )
        response = self.api.client.get(
            url, headers=self.api.headers.basic_with_user_token
        )
        return ActivityResponse(**orjson.loads(response.content))

    # TODO: похоже это не нужно
    # def filters(
    #     self,
    #     service_ids: list[int] | list[str] | None = None,
    #     staff_ids: list[int] | list[str] | None = None,
    #     resource_ids: list[int] | list[str] | None = None,
    # ) -> ActivityFiltersListResponse:
    #     """Returns activity filtered by params.
    #     :param service_ids: list of service ids. Optional.
    #     :param staff_ids: list of staff ids. Optional.
    #     :param resource_ids: list of resource ids. Optional.
    #     :return: ActivityFiltersResponse
    #     """
    #     api_url_suffix = "/activity/{company_id}/filters/"
    #     params = {}
    #     if service_ids:
    #         params["service_ids"] = service_ids
    #     if staff_ids:
    #         params["staff_ids"] = staff_ids
    #     if resource_ids:
    #         params["resource_ids"] = resource_ids
    #     response = self.api.client.get(
    #         api_url_suffix.format(company_id=self.api.config.company_id),
    #         params=params,
    #         headers=self.api.headers.basic_with_partner_token,
    #     )
    #     return ActivityFiltersListResponse(**orjson.loads(response.content))

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
        """Returns activities search results.
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
