from typing import List

from pydantic import BaseModel, ConfigDict
from pydantic.dataclasses import dataclass

from yclientsapi.config import Config

config = ConfigDict(extra=Config.extra_fields_in_response, frozen=True)


@dataclass(config=config)
class StorageData(BaseModel):
    id: int
    title: str
    for_service: int
    for_sale: int
    comment: str | None
    weight: int | None


@dataclass(config=config)
class StorageListResponse(BaseModel):
    success: bool
    data: List[StorageData]
    meta: List
