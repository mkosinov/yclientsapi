from __future__ import annotations

from dataclasses import field
from enum import IntEnum

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


class RepeatModeId(IntEnum):
    DAILY = 1
    WEEKDAYS = 2
    MON_WED_FRI = 3
    TUE_THU = 4
    WEEKLY = 5
    MONTHLY = 6
    YEARLY = 7


class DuplicateRecords(IntEnum):
    NO = 1
    YES = 2


@dataclass(config=Config.dataclass_config)
class DuplicationStrategyRepeatMode:
    id: int
    title: str


@dataclass(config=Config.dataclass_config)
class DuplicationStrategy:
    """
    Represents a strategy for duplicating activities within a company.
    Attributes:
        id (int): Unique identifier for the duplication strategy.
        company_id (int): Identifier of the company to which the strategy belongs.
        title (str): Name or title of the duplication strategy.
        repeat_mode_id (RepeatModeId): Identifier for the repeat mode.
        repeat_mode (DuplicationStrategyRepeatMode): The repeat mode details.
        days (list[int]): List of days on which the duplication occurs.
            Days of the week are represented as integers: 0 - Sunday, 1 - Monday, ..., 6 - Saturday.
        interval (int): Interval between duplications.
        content_type (int): Type of content being duplicated.
        duplicate_records (int, optional): Duplicate records? 1 - no, 2 - yes
    """

    id: int
    company_id: int
    title: str
    repeat_mode_id: RepeatModeId
    repeat_mode: DuplicationStrategyRepeatMode
    days: list[int]
    interval: int
    content_type: int
    duplicate_records: int = DuplicateRecords.NO


@dataclass(config=Config.dataclass_config)
class ActivityDuplicationStrategyResponse:
    success: bool
    data: list[DuplicationStrategy]
    meta: dict = field(default_factory=dict)


@dataclass(config=Config.dataclass_config)
class DuplicationStrategyCreate:
    title: str
    repeat_mode_id: RepeatModeId
    days: list[int] = field(default_factory=list)
    interval: int = 0
    content_type: DuplicateRecords = DuplicateRecords.NO
    duplicate_records: int = DuplicateRecords.NO


@dataclass(config=Config.dataclass_config)
class ActivityDuplicationStrategyCreateResponse:
    success: bool
    data: DuplicationStrategy
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class DuplicateService:
    id: int
    category_id: int
    title: str
    price_min: int
    price_max: int
    prepaid: str


@dataclass(config=Config.dataclass_config)
class DuplicateResourceInstance:
    id: int
    title: str
    resource_id: int


@dataclass(config=Config.dataclass_config)
class DuplicateMaster:
    id: int
    name: str
    company_id: int
    specialization: str
    rating: int
    show_rating: int
    prepaid: str
    position: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class DuplicateActivity:
    id: int
    service_id: int
    salon_id: int
    master_id: int
    date: int
    length: int
    capacity: int
    records_count: int
    color: str
    instructions: str
    stream_link: str
    font_color: str
    notified: bool
    timestamp: int
    service: DuplicateService
    resource_instances: list[DuplicateResourceInstance]
    master: DuplicateMaster
    records: list = field(default_factory=list)
    labels: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ActivityDuplicateResponse:
    success: bool
    data: list[DuplicateActivity]
    meta: dict = field(default_factory=dict)
