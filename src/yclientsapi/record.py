from datetime import date

import orjson

from yclientsapi.schema.record import RecordListResponse


class Record:
    """Methods for working with records.
    Records are individual and group records.
    Records with activity_id = 0 are individual records.
    """

    def __init__(self, api):
        self.api = api

    def get(
        self,
        page: str | int = "",
        count: str | int = "",
        staff_id: str | int = "",
        client_id: str | int = "",
        created_user_id: str | int = "",
        start_date: str | date = "",
        end_date: str | date = "",
        creation_start_date: str | date = "",
        creation_end_date: str | date = "",
        changed_after: str | date = "",
        changed_before: str | date = "",
        include_consumables: bool | int = False,
        include_finance_transactions: bool | int = False,
        with_deleted: bool | int = False,
    ) -> RecordListResponse:
        """Returns list of records matching search filters.
        :param page: page number
        :param count: number of records per page
        :param staff_id: id of staff
        :param client_id: id of client
        :param created_user_id: id of user that created record
        :param start_date: start date of records
        :param end_date: end date of records
        :param creation_start_date: record creation start date
        :param creation_end_date: record creation end date
        :param changed_after: record changed after date
        :param changed_before: record changed before date
        :param include_consumables: include consumables in results (default: False)
        :param include_finance_transactions: include finance transactions in results (default: False)
        :param with_deleted: with deleted records in results (default: False)
        :return: RecordListResponse
        """
        params = {}
        for arg, value in locals().items():
            if arg not in ("self", "params") and value:
                params[arg] = value
        api_url_suffix = "/records/{company_id}"
        url = api_url_suffix.format(company_id=self.api.config.company_id)
        response = self.api.client.get(
            url,
            params=params,
            headers=self.api.headers.basic_with_user_token,
        )
        return RecordListResponse(**orjson.loads(response.content))
