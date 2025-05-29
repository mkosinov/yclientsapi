from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

import pytest

if TYPE_CHECKING:
    from _pytest.mark import ParameterSet

count = 3


class Parametrize:
    list: ClassVar[list[ParameterSet]] = [
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
