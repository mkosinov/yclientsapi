from dataclasses import field

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class StorageData:
    id: int
    title: str
    for_service: int
    for_sale: int
    comment: str | None
    weight: int | None


@dataclass(config=Config.dataclass_config)
class StorageListResponse:
    success: bool
    data: list[StorageData]
    meta: list = field(default_factory=list)
