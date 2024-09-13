from typing import NoReturn


class Headers:
    content_type = {"Content-Type": "application/json"}
    accept = {"Accept": "application/vnd.api.v2+json"}

    def __init__(self, partner_token: str, user_token: str = ""):
        self._partner_token = partner_token
        self._user_token = user_token

    @property
    def authorization_partner(self) -> str:
        return {"Authorization": "Bearer {bearer}".format(bearer=self._partner_token)}

    @authorization_partner.setter
    def authorization_partner(self) -> NoReturn:
        raise AttributeError

    @property
    def authorization_partner_user(self) -> str:
        return {
            "Authorization": "Bearer {bearer}, User {user_token}".format(
                bearer=self._partner_token, user_token=self._user_token
            )
        }

    @authorization_partner_user.setter
    def authorization_partner_user(self) -> NoReturn:
        raise AttributeError

    @property
    def base(self) -> dict[str, str]:
        return self.content_type | self.accept | self.authorization_partner

    @base.setter
    def base(self) -> NoReturn:
        raise AttributeError

    @property
    def base_with_user_token(self) -> dict[str, str]:
        return self.content_type | self.accept | self.authorization_partner_user

    @base_with_user_token.setter
    def base_with_user_token(self) -> NoReturn:
        raise AttributeError
