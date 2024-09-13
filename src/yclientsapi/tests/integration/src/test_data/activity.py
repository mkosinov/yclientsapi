import pytest

from yclientsapi.tests.integration.vars import activity_id


class Parametrize:
    get = [pytest.param(({"activity_id": activity_id}), True, id="valid get")]
    # "empty id", "none existing id", "wrong type"
    search = [
        pytest.param(
            (
                {
                    "from_": "2024-09-01",
                    "till": "2024-10-02",
                    "service_ids": "",
                    "staff_ids": "",
                    "resource_ids": "",
                    "page": "",
                    "count": "",
                }
            ),
            True,
            id="valid search",
        )
    ]
