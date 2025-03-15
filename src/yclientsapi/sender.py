from abc import ABC, abstractmethod
from typing import Any

import httpx


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
    def send(self, method, url, headers, **kwargs) -> Any:
        raise NotImplementedError


class httpxSender(AbstractHttpSender):
    def create_session(self):
        self.session = httpx.Client(base_url=self._api._config.api_base_url)

    def close_session(self):
        self.session.close()

    def send(
        self,
        method: str,
        url_suffix: str,
        url_params: dict = None,
        headers: dict = None,
        **kwargs,
    ) -> httpx.Response:
        url_params = url_params or {}
        url = url_suffix.format(company_id=self._api._config.company_id, **url_params)
        headers = headers or {}
        response = self.session.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response
