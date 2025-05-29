from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class Price:
    min: int
    max: int


@dataclass(config=Config.dataclass_config)
class GridSetting:
    grid_first_timeslot: int
    grid_last_timeslot: int
    grid_display_step: int
    grid_nearest_timeslot_delay: int
    grid_base_type: str
    is_grid_flexible: bool


@dataclass(config=Config.dataclass_config)
class WeekdaySetting:
    weekday: int
    timeslots: list
    setting: GridSetting


@dataclass(config=Config.dataclass_config)
class GridSettings:
    is_enabled: bool
    weekdays_settings: list[WeekdaySetting]
    dates_settings: list


@dataclass(config=Config.dataclass_config)
class Chain:
    id: int
    title: str


@dataclass(config=Config.dataclass_config)
class Employee:
    id: int
    phone: str
    name: str
    firstname: str
    surname: str
    patronymic: str
    date_admission: str
    date_registration_end: str
    citizenship: str
    sex: str
    gender: int
    passport_data: str
    personal_tax_reference_number: str
    number_insurance_certificates: str


@dataclass(config=Config.dataclass_config)
class ServiceLink:
    service_id: int
    master_id: int
    length: int
    technological_card_id: int
    api_id: str
    is_online: bool
    is_offline_records_allowed: bool
    price: Price | None


@dataclass(config=Config.dataclass_config)
class Position:
    id: int
    chain_id: int
    title: str
    description: str
    services_binding_type: int
    rules_required_fields: list
    only_chain_appointment: bool


@dataclass(config=Config.dataclass_config)
class User:
    id: int
    name: str
    phone: str
    email: str
    avatar: str
    is_approved: bool


@dataclass(config=Config.dataclass_config)
class StaffData:
    id: int
    api_id: str | None
    name: str
    specialization: str
    company_id: int
    information: str
    fired: int
    is_fired: bool
    dismissal_date: str | None
    dismissal_reason: str | None
    hidden: int
    is_online: bool
    status: int
    is_deleted: bool
    user_id: int | None
    rating: float
    prepaid: str
    is_chain: bool
    weight: int
    is_rating_shown: bool
    is_online_random_choice_allowed: bool
    seance_step: int
    seance_search_step: int
    seance_search_start: int
    seance_search_finish: int
    is_timetable_off: bool
    is_fullness_accounting: bool
    google_clients: bool
    timetable_markup_divider_interval: int | None
    avatar: str
    avatar_big: str
    position: Position
    user: User | None
    is_bookable: bool
    services_links: list[ServiceLink]
    schedule_till: str
    employee: Employee
    chain: Chain | None
    grid_settings: GridSettings
    domain: str | None
    google_link: str


@dataclass(config=Config.dataclass_config)
class StaffResponse:
    success: bool
    data: StaffData
    meta: list


@dataclass(config=Config.dataclass_config)
class StaffListMeta:
    count: int


@dataclass(config=Config.dataclass_config)
class StaffListResponse:
    success: bool
    meta: StaffListMeta
    data: list[StaffData]
