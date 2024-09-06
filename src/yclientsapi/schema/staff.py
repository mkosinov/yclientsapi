from dataclasses import dataclass
from typing import List, Union


@dataclass
class StaffListPosition:
    id: int
    title: str


@dataclass
class StaffListData:
    id: int
    name: str
    company_id: int
    specialization: str
    position: StaffListPosition
    avatar: str
    avatar_big: str
    fired: int
    status: int
    hidden: int
    user_id: int


@dataclass
class StaffListMeta:
    total_count: int


@dataclass
class StaffListMeta404Error:
    message: str


@dataclass
class StaffListMeta404:
    message: str
    errors: List[StaffListMeta404Error]


@dataclass
class StaffListMeta403:
    message: str


@dataclass
class StaffListResponse:
    success: bool
    data: List[StaffListData]
    meta: Union[StaffListMeta, StaffListMeta403, StaffListMeta404]
