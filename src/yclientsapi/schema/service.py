from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ServiceStaff:
    id: int
    seance_length: int


@dataclass
class ServiceImage:
    id: int
    path: str
    width: int
    height: int
    type: str
    image_group_id: int
    version: str


@dataclass
class ServiceImageGroup:
    id: int
    entity: str
    entity_id: int
    images: List[ServiceImage]


@dataclass
class ServiceData:
    id: str
    title: str
    category_id: str
    price_min: str
    price_max: str
    discount: str
    comment: str
    weight: str
    active: str
    api_id: str
    staff: List[ServiceStaff]
    image_group: Optional[ServiceImageGroup]


@dataclass
class ServiceMeta:
    total_count: int


@dataclass
class ServiceListResponse:
    success: bool
    data: List[ServiceData]
    meta: ServiceMeta
