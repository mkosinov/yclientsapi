import os

from pydantic import ConfigDict
from pydantic.config import ExtraValues


class Config:
    api_base_url = os.getenv("YCLIENTS_API_BASE_URL", "https://api.yclients.com/api")
    _extra_value = os.getenv("EXTRA_FIELDS_IN_RESPONSE")
    _validated_extra: ExtraValues = (
        _extra_value if _extra_value in ("allow", "ignore", "forbid") else "ignore"
    )
    dataclass_config = ConfigDict(extra=_validated_extra, frozen=True)

    def __init__(self, company_id: int | str, **kwargs):
        self.company_id = company_id
        for key, value in kwargs.items():
            setattr(self, key, value)
