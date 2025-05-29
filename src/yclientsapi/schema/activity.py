from __future__ import annotations

from dataclasses import field
from datetime import datetime  # noqa: TC003

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class RootCategory:
    id: int
    category_id: int
    is_category: bool
    title: str
    category: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceCategory:
    title: str
    id: int
    category_id: int
    is_category: bool
    salon_service_id: int
    prepaid: str
    abonement_restriction: int
    category: RootCategory


@dataclass(config=Config.dataclass_config)
class Service:
    id: int
    title: str
    category_id: int
    image_url: str
    category_id: int
    is_category: bool
    salon_service_id: int
    comment: str
    price_min: int
    price_max: int
    prepaid: str
    abonement_restriction: int
    category: ServiceCategory


@dataclass(config=Config.dataclass_config)
class Staff:
    id: int
    name: str
    company_id: int
    specialization: str
    api_id: str | None
    user_id: int
    rating: float
    prepaid: str
    show_rating: int
    comments_count: int
    votes_count: int
    average_score: float
    avatar: str
    avatar_big: str
    position: dict[str, int | str] = field(default_factory=dict)


@dataclass(config=Config.dataclass_config)
class ResourceInstance:
    id: int
    title: str
    resource_id: int


@dataclass(config=Config.dataclass_config)
class Label:
    id: int
    title: str
    icon: str
    color: str
    font_color: str


@dataclass(config=Config.dataclass_config)
class ActivityData:
    id: int
    company_id: int
    service_id: int
    staff_id: int
    date: datetime
    timestamp: int
    length: int
    capacity: int
    color: str
    instructions: str
    stream_link: str
    notified: bool
    comment: str | None
    records_count: int
    font_color: str
    service: Service
    staff: Staff
    prepaid: str
    resource_instances: list[ResourceInstance] = field(default_factory=list)
    labels: list[Label] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ActivityResponse:
    success: bool
    data: ActivityData
    meta: list[dict] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ActivitySearchListResponse:
    success: bool
    data: list[ActivityData]
    meta: dict[str, int] = field(default_factory=lambda: {"count": 0})


@dataclass(config=Config.dataclass_config)
class ActivityCreate:
    date: str
    service_id: int
    staff_id: int
    capacity: int
    force: bool
    resource_instance_ids: list[int] | None = None
    length: int | None = None
    color: str | None = None
    label_ids: list[int] | None = None
    comment: str | None = None
    stream_link: str | None = None
    instructions: str | None = None


@dataclass(config=Config.dataclass_config)
class ActivityDeleteResponse:
    success: bool
    meta: dict


@dataclass(config=Config.dataclass_config)
class FilterItem:
    id: int
    title: str
    is_disabled: bool


@dataclass(config=Config.dataclass_config)
class FilterBlock:
    code: str
    title: str
    data: list[FilterItem]


@dataclass(config=Config.dataclass_config)
class ActivityFiltersResponse:
    success: bool
    data: list[FilterBlock]
    meta: dict


@dataclass(config=Config.dataclass_config)
class ActivityDatesRangeData:
    min_date: str
    max_date: str


@dataclass(config=Config.dataclass_config)
class ActivityDatesRangeResponse:
    success: bool
    data: ActivityDatesRangeData
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ActivityDatesListResponse:
    success: bool
    data: list[str]
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class GroupServiceCategory:
    id: int
    title: str


@dataclass(config=Config.dataclass_config)
class GroupServiceStaff:
    id: int
    name: str
    length: int


@dataclass(config=Config.dataclass_config)
class GroupServiceResource:
    id: int
    title: str
    salon_id: int


@dataclass(config=Config.dataclass_config)
class GroupService:
    id: int
    title: str
    capacity: int
    price_min: int
    price_max: int
    is_multi: bool
    category: GroupServiceCategory
    staff: list[GroupServiceStaff]
    resources: list[GroupServiceResource]


@dataclass(config=Config.dataclass_config)
class ActivityGroupServicesResponse:
    success: bool
    data: list[GroupService]
    meta: dict = field(default_factory=dict)
