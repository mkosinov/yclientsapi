from dataclasses import field

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class Price:
    min: int
    max: int


@dataclass(config=Config.dataclass_config)
class ServiceStaffData:
    id: int
    seance_length: int
    technological_card_id: int
    image_url: str
    price: Price | None
    name: str


@dataclass(config=Config.dataclass_config)
class ImageGroupImagesBasic:
    id: int
    path: str
    width: str
    height: str
    type: str
    image_group_id: int
    version: str


@dataclass(config=Config.dataclass_config)
class ImageGroupImages:
    basic: ImageGroupImagesBasic | None


@dataclass(config=Config.dataclass_config)
class ImageGroup:
    id: int
    entity: str
    entity_id: str
    images: ImageGroupImages


@dataclass(config=Config.dataclass_config)
class ServiceData:
    booking_title: str
    tax_variant: int | None
    vat_id: int | None
    print_title: str
    service_type: int
    api_service_id: int
    repeat_visit_days_step: int | None
    seance_search_start: int
    seance_search_finish: int
    seance_search_step: int
    step: int
    is_need_limit_date: bool
    date_from: str
    date_to: str
    schedule_template_type: int
    online_invoicing_status: int
    is_abonement_autopayment_enabled: int
    autopayment_before_visit_time: int
    abonement_restriction_value: int
    is_chain: bool
    is_price_managed_only_in_chain: bool
    is_comment_managed_only_in_chain: bool
    price_prepaid_amount: int
    price_prepaid_percent: int
    id: int
    salon_service_id: int
    title: str
    category_id: int
    price_min: int
    price_max: int
    discount: int
    comment: str
    weight: int
    active: int
    api_id: str
    prepaid: str
    is_multi: bool
    capacity: int
    duration: int
    is_online: bool
    image_group: ImageGroup | list[ImageGroup] = field(default_factory=list)
    staff: list[ServiceStaffData] = field(default_factory=list)
    dates: list = field(default_factory=list)
    resources: list[int] = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceResponse:
    success: bool
    data: ServiceData
    meta: list = field(default_factory=list)


@dataclass(config=Config.dataclass_config)
class ServiceListResponse:
    success: bool
    data: list[ServiceData]
    meta: dict[str, int] = field(default_factory=dict)
