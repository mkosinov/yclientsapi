import pytest

from yclientsapi import YclientsAPI
from yclientsapi.schema.salary import (
    SalaryBalanceResponse,
    SalaryCalculationDetailResponse,
    SalaryCalculationListResponse,
)
from yclientsapi.tests.integration.src.test_data.salary import Parametrize


@pytest.mark.service
@pytest.mark.parametrize(
    ("staff_id", "date_from", "date_to", "expected_response"),
    Parametrize.list_calculations,
)
def test_get_list_calculations(
    lib: YclientsAPI, staff_id, date_from, date_to, expected_response
):
    salary = lib.salary.list_calculations(staff_id, date_from, date_to)
    assert salary.success == expected_response
    assert isinstance(salary, SalaryCalculationListResponse)


@pytest.mark.service
@pytest.mark.parametrize(
    ("staff_id", "calculation_id", "expected_response"),
    Parametrize.get_calculation_details,
)
def test_get_calculation_details(
    lib: YclientsAPI, staff_id, calculation_id, expected_response
):
    calculation = lib.salary.get_calculation_details(staff_id, calculation_id)
    assert calculation.success == expected_response
    assert isinstance(calculation, SalaryCalculationDetailResponse)


@pytest.mark.service
@pytest.mark.parametrize(
    ("staff_id", "date_from", "date_to", "expected_response"),
    Parametrize.get_balance,
)
def test_get_balance(lib: YclientsAPI, staff_id, date_from, date_to, expected_response):
    balance = lib.salary.get_staff_balance(staff_id, date_from, date_to)
    assert balance.success == expected_response
    assert isinstance(balance, SalaryBalanceResponse)
