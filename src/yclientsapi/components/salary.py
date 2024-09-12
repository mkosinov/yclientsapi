from datetime import date

import orjson

from yclientsapi.schema.salary import (
    SalaryBalanceResponse,
    SalaryCalculationDetailResponse,
    SalaryCalculationListResponse,
)


class Salary:
    """Methods for working with salary."""

    def __init__(self, api):
        self.api = api

    def list_calculations(
        self,
        staff_id: int,
        date_from: str | date,
        date_to: str | date,
    ) -> SalaryCalculationListResponse:
        """
        Get list of salary calculations for the given staff in the given period.

        :param staff_id: ID of the staff.
        :param date_from: date of start of the period (inclusive).String format: YYYY-MM-DD
        :param date_to: date of end of the period (inclusive). String format: YYYY-MM-DD
        :return: instance of SalaryCalculationListResponse
        """
        url = (
            "/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/".format(
                company_id=self.api.config.company_id, staff_id=staff_id
            )
        )
        params = {
            "date_from": date_from.isoformat()
            if isinstance(date_from, date)
            else date_from,
            "date_to": date_to.isoformat() if isinstance(date_to, date) else date_to,
        }
        response = self.api.client.get(
            url, params=params, headers=self.api.headers.basic_with_user_token
        )
        return SalaryCalculationListResponse(**orjson.loads(response.content))

    def get_calculation_details(
        self, staff_id: int, calculation_id: int
    ) -> SalaryCalculationDetailResponse:
        """
        Get salary calculation details for the given staff and calculation.

        :param staff_id: ID of the staff.
        :param calculation_id: ID of the calculation.
        :return: instance of SalaryCalculationDetailResponse
        """
        url = "/company/{company_id}/salary/payroll/staff/{staff_id}/calculation/{calculation_id}".format(
            company_id=self.api.config.company_id,
            staff_id=staff_id,
            calculation_id=calculation_id,
        )
        response = self.api.client.get(
            url, headers=self.api.headers.basic_with_user_token
        )
        return SalaryCalculationDetailResponse(**orjson.loads(response.content))

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
        url = "/company/{company_id}/salary/calculation/staff/{staff_id}/".format(
            company_id=self.api.config.company_id, staff_id=staff_id
        )
        params = {
            "date_from": date_from.isoformat()
            if isinstance(date_from, date)
            else date_from,
            "date_to": date_to.isoformat() if isinstance(date_to, date) else date_to,
        }
        response = self.api.client.get(
            url, params=params, headers=self.api.headers.basic_with_user_token
        )
        return SalaryBalanceResponse(**orjson.loads(response.content))
