from dataclasses import field

from pydantic.dataclasses import dataclass

from yclientsapi.config import Config


@dataclass(config=Config.dataclass_config)
class Auth:
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


@dataclass(config=Config.dataclass_config)
class AuthResponse:
    success: bool
    data: Auth
    meta: list = field(default_factory=list)
