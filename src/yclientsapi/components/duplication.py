from dataclasses import asdict
from http import HTTPMethod

import orjson

from yclientsapi import YclientsAPI
from yclientsapi.logger import log_call
from yclientsapi.schema.activity import ActivityDeleteResponse
from yclientsapi.schema.duplication import (
    ActivityDuplicateResponse,
    ActivityDuplicationStrategyCreateResponse,
    ActivityDuplicationStrategyResponse,
    DuplicationStrategyCreate,
)


class Duplication:
    """Handles duplication-related operations for activities."""

    def __init__(self, api: YclientsAPI):
        self.__api = api

    @log_call
    def list_duplication_strategies(
        self,
    ) -> ActivityDuplicationStrategyResponse:
        """List all duplication strategies for activities.
        :return: ActivityDuplicationStrategyResponse
        """
        url_suffix = "/v1/activity/{company_id}/duplication_strategy"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
        )
        return ActivityDuplicationStrategyResponse(**orjson.loads(response.content))

    @log_call
    def create_duplication_strategy(
        self, strategy: DuplicationStrategyCreate
    ) -> ActivityDuplicationStrategyCreateResponse:
        """Create a duplication strategy for activities.
        :param strategy: DuplicationStrategyCreate dataclass with all parameters for the strategy
        :return: ActivityDuplicationStrategyCreateResponse
        """
        payload = asdict(strategy)
        url_suffix = "/v1/activity/{company_id}/duplication_strategy"
        response = self.__api._sender.send(
            method=HTTPMethod.POST,
            url_suffix=url_suffix,
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ActivityDuplicationStrategyCreateResponse(
            **orjson.loads(response.content)
        )

    @log_call
    def update_duplication_strategy(
        self, strategy_id: int, strategy: DuplicationStrategyCreate
    ) -> ActivityDuplicationStrategyCreateResponse:
        """Update an existing duplication strategy.
        :param strategy_id: ID of the strategy to update
        :param strategy: DuplicationStrategyCreate dataclass with updated parameters
        :return: ActivityDuplicationStrategyCreateResponse
        """
        payload = asdict(strategy)
        url_suffix = "/v1/activity/{company_id}/duplication_strategy/{strategy_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.POST,
            url_suffix=url_suffix,
            url_params={"strategy_id": strategy_id},
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ActivityDuplicationStrategyCreateResponse(
            **orjson.loads(response.content)
        )

    @log_call
    def delete_duplication_strategy(self, strategy_id: int) -> ActivityDeleteResponse:
        """Delete a duplication strategy.
        :param strategy_id: ID of the strategy to delete
        :return: ActivityDeleteResponse
        """
        url_suffix = "/v1/activity/{company_id}/duplication_strategy/{strategy_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.DELETE,
            url_suffix=url_suffix,
            url_params={"strategy_id": strategy_id},
            headers=self.__api._headers.base_with_user_token,
        )
        return ActivityDeleteResponse(**orjson.loads(response.content))

    @log_call
    def duplicate(self, activity_id: int, payload: dict) -> ActivityDuplicateResponse:
        """
        Duplicate an activity using the duplication API endpoint.
        NOTE: The correct input JSON format for this API call is currently unknown.
        This function may not work as expected until the correct payload structure is determined.
        """
        url_suffix = "/v1/activity/{company_id}/{activity_id}/duplicate"
        response = self.__api._sender.send(
            method=HTTPMethod.POST,
            url_suffix=url_suffix,
            url_params={"activity_id": activity_id},
            headers=self.__api._headers.base_with_user_token,
            json=payload,
        )
        return ActivityDuplicateResponse(**orjson.loads(response.content))
