from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class RecordStaff:
    id: int
    name: str
    specialization: str
    avatar: str
    avatar_big: str
    rating: int
    votes_count: int


@dataclass
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


@dataclass
class RecordClient:
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
    birthday: datetime
    client_tags: List[dict]


@dataclass
class RecordLabel:
    id: str
    color: str
    icon: str
    font_color: str


@dataclass
class RecordDocument:
    type_id: int
    storage_id: int
    user_id: int
    company_id: int
    number: int
    comment: str
    date_created: datetime
    category_id: int
    visit_id: int
    record_id: int
    type_title: str
    is_sale_bill_printed: bool


@dataclass
class Record:
    id: int
    company_id: int
    staff_id: int
    services: List[RecordService]
    goods_transactions: List[dict]
    staff: RecordStaff
    client: Optional[RecordClient]
    comer: Optional[dict]
    clients_count: int
    date: datetime
    datetime: datetime
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
    visit_id: str
    created_user_id: int
    deleted: bool
    paid_full: int
    prepaid: bool
    prepaid_confirmed: bool
    last_change_date: datetime
    custom_color: str
    custom_font_color: str
    record_labels: List[RecordLabel]
    activity_id: int
    custom_fields: List[dict]
    documents: List[RecordDocument]
    sms_remain_hours: int
    email_remain_hours: int
    bookform_id: int
    record_from: str
    is_mobile: int
    is_sale_bill_printed: bool
    consumables: List[dict]
    finance_transactions: List[dict]


@dataclass
class RecordListMeta:
    page: int
    total_count: int


@dataclass
class RecordListResponse:
    success: bool
    data: List[Record]
    meta: RecordListMeta
