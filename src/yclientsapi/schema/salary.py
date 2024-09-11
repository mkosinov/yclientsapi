from dataclasses import dataclass
from typing import List


@dataclass
class SalaryCalculationData:
    id: int
    company_id: int
    staff_id: int
    amount: int
    status: str
    date_create: str
    date_from: str
    date_to: str
    comment: str


@dataclass
class SalaryCalculationListResponse:
    success: bool
    data: List[SalaryCalculationData]
    meta: dict


@dataclass
class Paid:
    money_sum: str
    discount_sum: str
    bonus_sum: str
    certificate_sum: str
    abonement_sum: str
    deposit_sum: str


@dataclass
class SalaryCalculationInfo:
    criteria_title: str
    param_title: str
    scheme_title: str


@dataclass
class SalaryCalculation:
    type_slug: str
    value: float
    description: str


@dataclass
class SalaryDiscrepancy:
    reason: str
    actual_sum: str
    difference_sum: str


@dataclass
class Currency:
    id: int
    iso: str
    name: str
    symbol: str
    is_symbol_after_amount: bool


@dataclass
class SalaryCalculationDetailTarget:
    target_type_slug: str
    target_id: int
    title: str
    cost: str
    net_cost: str
    salary_sum: str
    salary_promotion_sum: str
    salary_calculation: SalaryCalculation


@dataclass
class SalaryCalculationDetailItem:
    date: str
    time: str
    item_id: int
    item_type_slug: str
    salary_sum: str
    record_id: int
    client_id: int
    cost: str
    paid: Paid
    salary_calculation_info: SalaryCalculationInfo
    targets: List[SalaryCalculationDetailTarget]
    salary_discrepancy: SalaryDiscrepancy


@dataclass
class SalaryCalculationDetailData:
    id: int
    company_id: int
    staff_id: int
    amount: int
    status: str
    date_create: str
    date_from: str
    date_to: str
    comment: str
    salary_items: List[SalaryCalculationDetailItem]
    currency: Currency


@dataclass
class SalaryCalculationDetailResponse:
    success: bool
    data: SalaryCalculationDetailData
    meta: List = None


@dataclass
class SalaryBalance:
    income: str
    expense: str
    balance: str


@dataclass
class SalaryBalanceData:
    total_sum: SalaryBalance
    currency: Currency


@dataclass
class SalaryBalanceResponse:
    success: bool
    data: SalaryBalanceData
    meta: List = None
