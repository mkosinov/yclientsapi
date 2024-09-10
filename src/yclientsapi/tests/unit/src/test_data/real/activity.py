import pytest


class Parametrize:
    get = [pytest.param(({"activity_id": 54321}), True, id="valid get")]
    # "empty id", "none existing id", "wrong type"
    search = [
        pytest.param(
            (
                {
                    "from_": "2020-01-01",
                    "till": "2024-01-02",
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
