import os
from enum import StrEnum


class ExtraFieldsInResponse(StrEnum):
    ALLOW = "allow"
    FORBID = "forbid"
    IGNORE = "ignore"


class Config:
    api_base_url = os.getenv("YCLIENTS_API_BASE_URL", "https://api.yclients.com/api/v1")
    extra_fields_in_response = os.getenv(
        "EXTRA_FIELDS_IN_RESPONSE", ExtraFieldsInResponse.IGNORE.value
    )

    def __init__(self, company_id: int | str, **kwargs):
        self.company_id = company_id
        for key, value in kwargs.items():
            setattr(self, key, value)
