from dataclasses import field
from datetime import datetime

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class RecordStaff:
    id: int
    api_id: str | None
    name: str
    specialization: str
    position: dict
    avatar: str
    avatar_big: str
    rating: int
    votes_count: int


@dataclass(config=Config.dataclass_config)
class RecordService:
    id: int
    title: str
    cost: int
    cost_to_pay: int
    manual_cost: int
    cost_per_unit: int
    discount: int
    first_cost: int
    amount: int


@dataclass(config=Config.dataclass_config)
class RecordClient:
    id: int
    name: str
    surname: str
    patronymic: str
    display_name: str
    phone: str
    card: str
    email: str
    success_visits_count: int
    fail_visits_count: int
    discount: int
    custom_fields: list[dict]
    client_tags: list[dict]
    is_new: bool


@dataclass(config=Config.dataclass_config)
class RecordLabel:
    id: str
    title: str
    color: str
    icon: str
    font_color: str


@dataclass(config=Config.dataclass_config)
class RecordDocument:
    id: int
    type_id: int
    storage_id: int
    user_id: int
    company_id: int
    number: int
    comment: str | None
    date_created: datetime
    category_id: int
    visit_id: int
    record_id: int
    type_title: str
    is_sale_bill_printed: bool | None


@dataclass(config=Config.dataclass_config)
class Record:
    id: int
    company_id: int
    staff_id: int
    services: list[RecordService]
    goods_transactions: list[dict]
    staff: RecordStaff
    client: RecordClient | None
    comer: dict | None
    clients_count: int
    date: datetime
    datetime_: datetime = field(metadata={"alias": "datetime"})
    create_date: datetime
    comment: str
    online: bool
    visit_attendance: int
    attendance: int
    confirmed: int
    seance_length: int
    length: int
    sms_before: int
    sms_now: int
    sms_now_text: str
    email_now: int
    notified: int
    master_request: int
    api_id: str
    from_url: str
    review_requested: int
    visit_id: int
    created_user_id: int
    deleted: bool
    paid_full: int
    payment_status: int
    prepaid: bool
    prepaid_confirmed: bool
    last_change_date: datetime
    custom_color: str
    custom_font_color: str
    record_labels: list[RecordLabel]
    activity_id: int
    custom_fields: list[dict]
    documents: list[RecordDocument]
    sms_remain_hours: int
    email_remain_hours: int
    bookform_id: int
    record_from: str
    is_mobile: int
    is_update_blocked: bool
    is_sale_bill_printed: bool
    resource_instance_ids: list[int]
    short_link: str
    acceptance_free: str | None


@dataclass(config=Config.dataclass_config)
class RecordListMeta:
    page: int
    total_count: int


@dataclass(config=Config.dataclass_config)
class RecordListResponse:
    success: bool
    data: list[Record]
    meta: RecordListMeta
