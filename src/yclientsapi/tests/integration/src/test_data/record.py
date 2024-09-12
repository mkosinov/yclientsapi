import pytest

count = 3


class Parametrize:
    list = [
        pytest.param(
            {
                "page": None,
                "count": count,
                "staff_id": None,
                "client_id": None,
                "created_user_id": None,
                "start_date": "2020-09-10",
                "end_date": "2020-09-12",
                "creation_start_date": None,
                "creation_end_date": None,
                "changed_after": None,
                "changed_before": None,
                "include_consumables": None,
                "include_finance_transactions": None,
                "with_deleted": None,
            },
            {
                "success": True,
                "count": count,
            },
            id="valid list",
        )
    ]
