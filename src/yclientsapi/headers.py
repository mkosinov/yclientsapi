from __future__ import annotations

from typing import ClassVar, NoReturn

type Headers_Dict = dict[str, str]


class Headers:
    content_type: ClassVar[Headers_Dict] = {"Content-Type": "application/json"}
    accept: ClassVar[Headers_Dict] = {"Accept": "application/vnd.api.v2+json"}

    def __init__(self, partner_token: str, user_token: str = ""):
        self._partner_token = partner_token
        self._user_token = user_token

    @property
    def authorization_partner(self) -> Headers_Dict:
        return {"Authorization": f"Bearer {self._partner_token}"}

    @authorization_partner.setter
    def authorization_partner(self) -> NoReturn:
        raise AttributeError

    @property
    def authorization_partner_user(self) -> Headers_Dict:
        if not self._user_token:
            raise ValueError(
                "User token is not set. Please set it in the YclientsAPI initialization or call later YclientsAPI instance auth.authenticate() method to set it."
            )
        return {
            "Authorization": f"Bearer {self._partner_token}, User {self._user_token}"
        }

    @authorization_partner_user.setter
    def authorization_partner_user(self) -> NoReturn:
        raise AttributeError

    @property
    def base(self) -> Headers_Dict:
        return self.content_type | self.accept | self.authorization_partner

    @base.setter
    def base(self) -> NoReturn:
        raise AttributeError

    @property
    def base_with_user_token(self) -> Headers_Dict:
        return self.content_type | self.accept | self.authorization_partner_user

    @base_with_user_token.setter
    def base_with_user_token(self) -> NoReturn:
        raise AttributeError
