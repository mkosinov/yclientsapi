from http import HTTPMethod
from typing import TYPE_CHECKING

import orjson

from yclientsapi.logger import log_call

if TYPE_CHECKING:
    from yclientsapi import YclientsAPI
from yclientsapi.schema.storage import StorageListResponse


class Storage:
    """Methods for working with storage."""

    def __init__(self, api):
        self.__api: YclientsAPI = api

    @log_call
    def list(self) -> StorageListResponse:
        """Returns list of all storages.

        :return: StorageListResponse
        """
        url_suffix = "/v1/storages/{company_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return StorageListResponse(**orjson.loads(response.content))
