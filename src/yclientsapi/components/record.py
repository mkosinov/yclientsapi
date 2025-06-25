from __future__ import annotations

from http import HTTPMethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import date

import orjson

from yclientsapi.logger import log_call
from yclientsapi.schema.record import RecordListResponse

if TYPE_CHECKING:
    from yclientsapi import YclientsAPI


class Record:
    """Methods for working with records.
    Records are individual and group records.
    Records with activity_id = 0 are individual records.
    """

    def __init__(self, api):
        self.__api: YclientsAPI = api

    @log_call
    def list(
        self,
        page: int | None = None,
        count: int | None = None,
        staff_id: int | None = None,
        client_id: int | None = None,
        created_user_id: int | None = None,
        start_date: str | date | None = None,
        end_date: str | date | None = None,
        creation_start_date: str | date | None = None,
        creation_end_date: str | date | None = None,
        changed_after: str | date | None = None,
        changed_before: str | date | None = None,
        include_consumables: int | None = None,
        include_finance_transactions: int | None = None,
        with_deleted: bool | None = None,
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
        :param include_consumables: include consumables in results
        :param include_finance_transactions: include finance transactions in results
        :param with_deleted: with deleted records in results
        :return: RecordListResponse
        """
        params = {}
        for arg, value in locals().items():
            if arg not in ("self", "params") and value:
                params[arg] = value
        url_suffix = "/v1/records/{company_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={},
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return RecordListResponse(**orjson.loads(response.content))
