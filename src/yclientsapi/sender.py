from abc import ABC, abstractmethod
from http import HTTPMethod
from typing import Any

import httpx

from yclientsapi.exceptions import YclientsApiResponseError


class AbstractHttpSender(ABC):
    def __init__(self, api, **kwargs):
        self._api = api

    @abstractmethod
    def create_session(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def close_session(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def send(
        self,
        method: HTTPMethod,
        url_suffix: str,
        url_params: dict | None = None,
        headers: dict | None = None,
        **kwargs,
    ) -> Any:
        raise NotImplementedError


class HttpxSender(AbstractHttpSender):
    def create_session(self):
        self.session = httpx.Client(base_url=self._api._config.api_base_url)

    def close_session(self):
        self.session.close()

    def send(
        self,
        method: HTTPMethod,
        url_suffix: str,
        url_params: dict | None = None,
        headers: dict | None = None,
        **kwargs,
    ) -> httpx.Response:
        url_params = url_params or {}
        url = url_suffix.format(company_id=self._api._config.company_id, **url_params)
        headers = headers or {}
        self._api.logger.info(f"Sending {method.value} request to {url}")
        self._api.logger.debug(f"Request headers: {headers}")
        if "json" in kwargs:
            self._api.logger.debug(f"Request JSON body: {kwargs['json']}")
        elif "data" in kwargs:
            self._api.logger.debug(f"Request data body: {kwargs['data']}")
        response = self.session.request(method.value, url, headers=headers, **kwargs)
        self._api.logger.debug(f"Response status: {response.status_code}")
        self._api.logger.debug(f"Response content: {response.content}")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as err:
            response_content = response.content.decode("utf-8", errors="replace")
            request_url = str(response.request.url)
            request_method = response.request.method
            request_headers = dict(response.request.headers)
            request_body = (
                response.request.content.decode("utf-8", errors="replace")
                if response.request.content
                else None
            )
            message = (
                f"HTTP error response: {response.status_code}\n"
                f"Error response content: {response_content}\n"
                f"Request URL: {request_url}\n"
                f"Request method: {request_method}\n"
                f"Request headers: {request_headers}\n"
                f"Request body: {request_body}"
            )
            self._api.logger.error(message)
            raise YclientsApiResponseError(message) from err
        return response
