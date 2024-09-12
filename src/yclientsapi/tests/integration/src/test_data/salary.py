from datetime import date

import pytest

from yclientsapi.tests.integration.vars import calculation_id, staff_id


class Parametrize:
    list_calculations = [
        pytest.param(
            staff_id,
            date(2021, 4, 1),
            date(2021, 6, 30),
            True,
            id="valid get list of calculations",
        )
    ]

    get_calculation_details = [
        pytest.param(
            staff_id,
            calculation_id,
            True,
            id="valid get calculation details",
        )
    ]

    get_balance = [
        pytest.param(
            staff_id,
            date(2021, 4, 1),
            date(2021, 6, 30),
            True,
            id="valid get balance",
        )
    ]
