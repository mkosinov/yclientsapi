from dataclasses import field
from datetime import datetime

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
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


@dataclass(config=Config.dataclass_config)
class SalaryCalculationListResponse:
    success: bool
    meta: dict
    data: list[SalaryCalculationData] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class Paid:
    money_sum: str
    discount_sum: str
    bonus_sum: str
    certificate_sum: str
    abonement_sum: str
    deposit_sum: str


@dataclass(config=Config.dataclass_config)
class SalaryCalculationInfo:
    criteria_title: str
    param_title: str
    scheme_title: str


@dataclass(config=Config.dataclass_config)
class SalaryCalculation:
    type_slug: str
    value: float
    description: str


@dataclass(config=Config.dataclass_config)
class SalaryDiscrepancy:
    reason: str
    actual_sum: str
    difference_sum: str


@dataclass(config=Config.dataclass_config)
class Currency:
    id: int
    iso: str
    name: str
    symbol: str
    is_symbol_after_amount: bool


@dataclass(config=Config.dataclass_config)
class CurrencyShort:
    symbol: str


@dataclass(config=Config.dataclass_config)
class SalaryCalculationDetailTarget:
    target_type_slug: str
    target_id: int
    title: str
    cost: str
    net_cost: str
    salary_sum: str
    salary_promotion_sum: str
    salary_calculation: SalaryCalculation


@dataclass(config=Config.dataclass_config)
class SalaryCalculationDetailItem:
    date: datetime
    time: str
    item_id: int
    item_type_slug: str
    salary_sum: str
    record_id: int
    client_id: int
    cost: str
    paid: Paid
    salary_calculation_info: SalaryCalculationInfo
    salary_discrepancy: SalaryDiscrepancy
    targets: list[SalaryCalculationDetailTarget] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
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
    currency: Currency
    salary_items: list[SalaryCalculationDetailItem] = field(
        default_factory=list
    )


@dataclass(config=Config.dataclass_config)
class SalaryCalculationDetailResponse:
    success: bool
    data: SalaryCalculationDetailData
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class SalaryBalance:
    income: str
    expense: str
    balance: str


@dataclass(config=Config.dataclass_config)
class SalaryBalanceData:
    total_sum: SalaryBalance
    currency: CurrencyShort


@dataclass(config=Config.dataclass_config)
class SalaryBalanceResponse:
    success: bool
    data: SalaryBalanceData
    meta: list = field(default_factory=list)
