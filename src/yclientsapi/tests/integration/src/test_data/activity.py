from __future__ import annotations

from datetime import datetime, timedelta
from random import randint
from typing import TYPE_CHECKING, ClassVar

import pytest

from yclientsapi.schema.activity import ActivityCreate
from yclientsapi.tests.integration.vars import service_id, staff_id

if TYPE_CHECKING:
    from _pytest.mark import ParameterSet

today = datetime.now()
future_date_base = today + timedelta(days=7)
future_date = future_date_base.replace(
    hour=randint(10, 18), minute=0, second=0
).strftime("%Y-%m-%d %H:%M:%S")
future_date2 = (
    (today + timedelta(days=14))
    .replace(hour=randint(10, 17), minute=30, second=0)
    .strftime("%Y-%m-%d %H:%M:%S")
)


class Parametrize:
    search: ClassVar[list[ParameterSet]] = [
        pytest.param(
            {
                "from_": future_date.split()[0],
                "till": future_date2.split()[0],
                "service_ids": "",
                "staff_ids": "",
                "resource_ids": "",
                "page": "",
                "count": "",
            },
            True,
            id="valid search",
        )
    ]

    create: ClassVar[list[ParameterSet]] = [
        pytest.param(
            {
                "activity": ActivityCreate(
                    date=future_date,
                    service_id=int(service_id),
                    staff_id=int(staff_id),
                    capacity=5,
                    force=True,
                    length=7200,
                    color="#FF5733",
                    comment="Test activity at working hours with 2 hour duration",
                )
            },
            True,
            id="valid create",
        ),
    ]

    filters: ClassVar[list[ParameterSet]] = [pytest.param({}, True, id="valid filters")]

    search_dates_range: ClassVar[list[ParameterSet]] = [
        pytest.param({}, True, id="valid search_dates_range")
    ]

    search_dates: ClassVar[list[ParameterSet]] = [
        pytest.param(
            {
                "from_": future_date.split()[0],
                "till": future_date2.split()[0],
            },
            True,
            id="valid search_dates",
        )
    ]

    group_services: ClassVar[list[ParameterSet]] = [
        pytest.param({}, True, id="valid group_services")
    ]
