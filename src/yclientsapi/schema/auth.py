from dataclasses import field

from pydantic import ConfigDict
from pydantic.dataclasses import dataclass

from yclientsapi.config import Config

config = ConfigDict(extra=Config.extra_fields_in_response, frozen=True)


@dataclass(config=config)
class Data:
    id: int
    user_token: str
    name: str
    phone: str
    login: str
    email: str
    avatar: str
    is_approved: bool
    is_email_confirmed: bool
    _: str | None = field(default=None, metadata={"alias": "0"})


@dataclass(config=config)
class AuthResponse:
    success: bool
    data: Data
    meta: list = field(default_factory=list)
