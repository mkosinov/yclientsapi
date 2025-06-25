from datetime import date
from http import HTTPMethod

import orjson

from yclientsapi.logger import log_call
from yclientsapi.schema.salary import (
    SalaryBalanceResponse,
    SalaryCalculationDetailResponse,
    SalaryCalculationListResponse,
)


class Salary:
    """Methods for working with salary."""

    def __init__(self, api):
        self.__api = api

    @log_call
    def list_calculations(
        self,
        staff_id: int,
        date_from: str | date,
        date_to: str | date,
    ) -> SalaryCalculationListResponse:
        """
        Get list of salary calculations for the given staff in the given period.

        :param staff_id: ID of the staff.
        :param date_from: date of start of the period (inclusive). String format: YYYY-MM-DD.
        :param date_to: date of end of the period (inclusive). String format: YYYY-MM-DD.
        :return: SalaryCalculationListResponse
        """
        params = {
            "date_from": date_from.isoformat()
            if isinstance(date_from, date)
            else date_from,
            "date_to": date_to.isoformat() if isinstance(date_to, date) else date_to,
        }
        url_suffix = (
            "/v1/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/"
        )
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={"staff_id": staff_id},
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return SalaryCalculationListResponse(**orjson.loads(response.content))

    @log_call
    def get_calculation_details(
        self, staff_id: int, calculation_id: int
    ) -> SalaryCalculationDetailResponse:
        """
        Get salary calculation details for the given staff and calculation.

        :param staff_id: ID of the staff.
        :param calculation_id: ID of the calculation.
        :return: SalaryCalculationDetailResponse
        """
        url_suffix = "/v1/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/{calculation_id}"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={
                "staff_id": staff_id,
                "calculation_id": calculation_id,
            },
            headers=self.__api._headers.base_with_user_token,
        )
        return SalaryCalculationDetailResponse(**orjson.loads(response.content))

    @log_call
    def get_staff_balance(
        self, staff_id: int, date_from: str | date, date_to: str | date
    ) -> SalaryBalanceResponse:
        """
        Get salary balance for the given staff in the given period.

        :param staff_id: ID of the staff.
        :param date_from: date of start of the period (inclusive). String format: YYYY-MM-DD
        :param date_to: date of end of the period (inclusive). String format: YYYY-MM-DD
        :return: instance of SalaryBalanceResponse
        """
        params = {
            "date_from": date_from.isoformat()
            if isinstance(date_from, date)
            else date_from,
            "date_to": date_to.isoformat() if isinstance(date_to, date) else date_to,
        }
        url_suffix = "/v1/company/{company_id}/salary/calculation/staff/{staff_id}/"
        response = self.__api._sender.send(
            method=HTTPMethod.GET,
            url_suffix=url_suffix,
            url_params={"staff_id": staff_id},
            headers=self.__api._headers.base_with_user_token,
            params=params,
        )
        return SalaryBalanceResponse(**orjson.loads(response.content))
