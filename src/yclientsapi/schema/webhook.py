from dataclasses import dataclass
from typing import List, Optional


@dataclass
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


@dataclass
class Staff:
    id: int
    api_id: Optional[str]
    name: str
    specialization: str
    position: dict
    avatar: str
    avatar_big: str
    rating: int
    votes_count: int


@dataclass
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
    custom_fields: List[dict]
    sex: int
    birthday: str
    client_tags: List[dict]


@dataclass
class RecordLabel:
    id: int
    title: str
    color: str
    icon: str
    font_color: str


@dataclass
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


@dataclass
class Data:
    id: int
    company_id: int
    staff_id: int
    services: List[Service]
    goods_transactions: List[dict]
    staff: Staff
    client: Optional[Client]
    comer: Optional[dict]
    clients_count: int
    date: str
    datetime: str
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
    record_labels: List[RecordLabel]
    activity_id: int
    custom_fields: List[dict]
    documents: List[Document]
    sms_remain_hours: int
    email_remain_hours: int
    bookform_id: int
    record_from: str
    is_mobile: int
    short_link: str


@dataclass
class YclientsEvent:
    company_id: int
    resource: str
    resource_id: int
    status: str
    data: Data
