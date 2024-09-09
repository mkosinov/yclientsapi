from dataclasses import dataclass, field


@dataclass
class Service:
    id: int
    title: str
    category_id: int


@dataclass
class Staff:
    id: int
    name: str
    company_id: int
    specialization: str


@dataclass
class ResourceInstance:
    id: int
    title: str
    resource_id: int


@dataclass
class Label:
    id: int
    title: str
    icon: str
    color: str
    font_color: str


@dataclass
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
    comment: str
    records_count: int
    font_color: str
    service: Service
    staff: Staff
    resource_instances: list[ResourceInstance]
    labels: list[Label]


@dataclass
class ActivityResponse:
    success: bool
    data: Data
    meta: list[dict] = field(default_factory=list)


@dataclass
class ActivityFiltersListData:
    id: int
    title: str
    is_disabled: bool


@dataclass
class ActivityFiltersListResponse:
    success: bool
    data: list[tuple[Service, list[ActivityFiltersListData]]]
    meta: dict[str, int] = field(default_factory=lambda: {"count": 0})


@dataclass
class ActivitySearchListResponse:
    success: bool
    data: list[Data]
    meta: dict[str, int] = field(default_factory=lambda: {"count": 0})
