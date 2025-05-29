from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar

import pytest

if TYPE_CHECKING:
    from _pytest.mark import ParameterSet

from yclientsapi.tests.integration.vars import calculation_id, staff_id


class Parametrize:
    list_calculations: ClassVar[list[ParameterSet]] = [
        pytest.param(
            staff_id,
            date(2021, 4, 1),
            date(2021, 6, 30),
            True,
            id="valid get list of calculations",
        )
    ]

    get_calculation_details: ClassVar[list[ParameterSet]] = [
        pytest.param(
            staff_id,
            calculation_id,
            True,
            id="valid get calculation details",
        )
    ]

    get_balance: ClassVar[list[ParameterSet]] = [
        pytest.param(
            staff_id,
            date(2021, 4, 1),
            date(2021, 6, 30),
            True,
            id="valid get balance",
        )
    ]
