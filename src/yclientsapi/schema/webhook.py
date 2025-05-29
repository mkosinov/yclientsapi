from datetime import datetime

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class Service:
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
class Staff:
    id: int
    api_id: str | None
    name: str
    specialization: str
    position: dict  # TODO: add nested schema
    avatar: str
    avatar_big: str
    rating: int
    votes_count: int


@dataclass(config=Config.dataclass_config)
class Client:
    id: int
    name: str
    surname: str
    patronymic: str
    display_name: str
    comment: str
    phone: str
    card: str
    email: str
    success_visits_count: int
    fail_visits_count: int
    discount: int
    custom_fields: list[dict]  # TODO: add nested schema
    sex: int
    birthday: str
    client_tags: list[dict]  # TODO: add nested schema


@dataclass(config=Config.dataclass_config)
class RecordLabel:
    id: int
    title: str
    color: str
    icon: str
    font_color: str


@dataclass(config=Config.dataclass_config)
class Document:
    id: int
    type_id: int
    storage_id: int
    user_id: int
    company_id: int
    number: int
    comment: str
    date_created: str
    category_id: int
    visit_id: int
    record_id: int
    type_title: str
    is_sale_bill_printed: bool


@dataclass(config=Config.dataclass_config)
class Webhook:
    id: int
    company_id: int
    staff_id: int
    services: list[Service]
    goods_transactions: list[dict]  # TODO: add nested schema
    staff: Staff
    client: Client | None
    comer: dict | None  # TODO: add nested schema
    clients_count: int
    date: datetime
    datetime: datetime
    create_date: str
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
    prepaid: bool
    prepaid_confirmed: bool
    is_update_blocked: bool
    last_change_date: str
    custom_color: str
    custom_font_color: str
    record_labels: list[RecordLabel]
    activity_id: int
    custom_fields: list[dict]  # TODO: add nested schema
    documents: list[Document]
    sms_remain_hours: int
    email_remain_hours: int
    bookform_id: int
    record_from: str
    is_mobile: int
    short_link: str


@dataclass(config=Config.dataclass_config)
class YclientsEvent:
    company_id: int
    resource: str
    resource_id: int
    status: str
    data: Webhook
