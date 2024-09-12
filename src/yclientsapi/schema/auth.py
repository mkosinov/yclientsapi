from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AuthResponse:
    id: int
    user_token: str
    name: str
    phone: str
    login: str
    email: str
    avatar: str
    is_approved: bool
