from dataclasses import field

from pydantic import ConfigDict
from pydantic.dataclasses import dataclass

from yclientsapi.config import Config

config = ConfigDict(extra=Config.extra_fields_in_response, frozen=True)


@dataclass(config=config)
class ServiceCategoryData:
    id: int
    category_id: int
    salon_service_id: int
    title: str
    weight: int
    api_id: str
    booking_title: str
    price_min: int
    price_max: int
    sex: int
    is_chain: bool
    staff: list[int] = field(default_factory=list)


@dataclass(config=config)
class ServiceCategoryListResponse:
    success: bool
    meta: dict[str, int]
    data: list[ServiceCategoryData] = field(default_factory=list)


@dataclass(config=config)
class ServiceCategoryResponse:
    success: bool
    data: ServiceCategoryData
    meta: list = field(default_factory=list)
