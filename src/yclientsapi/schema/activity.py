from __future__ import annotations

from dataclasses import field

from pydantic import ConfigDict
from pydantic.dataclasses import dataclass

from yclientsapi.config import Config

config = ConfigDict(extra=Config.extra_fields_in_response, frozen=True)


@dataclass(config=config)
class RootCategory:
    id: int
    category_id: int
    is_category: bool
    title: str
    category: list = field(default_factory=list)


@dataclass(config=config)
class ServiceCategory:
    title: str
    id: int
    category_id: int
    is_category: bool
    salon_service_id: int
    prepaid: str
    abonement_restriction: int
    category: RootCategory


@dataclass(config=config)
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


@dataclass(config=config)
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


@dataclass(config=config)
class ResourceInstance:
    id: int
    title: str
    resource_id: int


@dataclass(config=config)
class Label:
    id: int
    title: str
    icon: str
    color: str
    font_color: str


@dataclass(config=config)
class Data:
    id: int
    company_id: int
    service_id: int
    staff_id: int
    date: str
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


@dataclass(config=config)
class ActivityResponse:
    success: bool
    data: Data
    meta: list[dict] = field(default_factory=list)


@dataclass(config=config)
class ActivitySearchListResponse:
    success: bool
    data: list[Data]
    meta: dict[str, int] = field(default_factory=lambda: {"count": 0})
