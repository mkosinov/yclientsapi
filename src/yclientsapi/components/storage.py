import orjson

from yclientsapi import YclientsAPI
from yclientsapi.schema.storage import StorageListResponse


class Storage:
    """Methods for working with storage."""

    def __init__(self, api):
        self.__api: YclientsAPI = api

    def list(self) -> StorageListResponse:
        """Returns list of all storages.

        :return: StorageListResponse
        """
        url_suffix = "/storages/{company_id}"
        response = self.__api._sender.send(
            "GET",
            url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return StorageListResponse(**orjson.loads(response.content))
