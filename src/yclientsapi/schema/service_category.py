from dataclasses import field

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class ServiceCategoryCreateRequest:
    title: str
    api_id: str
    weight: int
    booking_title: str
    staff: list[int] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceCategoryUpdateRequest:
    title: str
    weight: int
    staff: list[int] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class _ServiceCategoryCreateResponseData:
    id: int
    salon_service_id: int
    title: str
    weight: int
    api_id: str
    is_chain: bool
    staff: list[int] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class _ServiceCategoryGetResponseData:
    id: int
    salon_service_id: int
    title: str
    weight: int
    api_id: str
    staff: list[int] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceCategoryCreateResponse:
    success: bool
    data: _ServiceCategoryCreateResponseData
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceCategoryGetResponse:
    success: bool
    data: _ServiceCategoryGetResponseData
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceCategoryListResponse:
    success: bool
    meta: dict[str, int]
    data: list[_ServiceCategoryGetResponseData] = field(default_factory=list)
