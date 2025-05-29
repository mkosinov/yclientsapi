from __future__ import annotations

from datetime import datetime, timedelta
from random import randint
from typing import TYPE_CHECKING, ClassVar

import pytest

from yclientsapi.schema.duplication import (
    DuplicateRecords,
    DuplicationStrategyCreate,
    RepeatModeId,
)

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
    list_duplication_strategies: ClassVar[list[ParameterSet]] = [
        pytest.param({}, True, id="valid list_duplication_strategies")
    ]

    create_duplication_strategy: ClassVar[list[ParameterSet]] = [
        pytest.param(
            {
                "strategy": DuplicationStrategyCreate(
                    title="Test Strategy",
                    repeat_mode_id=RepeatModeId.WEEKLY,
                    days=[1, 3, 5],
                    interval=1,
                    content_type=DuplicateRecords.NO,
                )
            },
            True,
            id="valid create_duplication_strategy",
        )
    ]

    update_duplication_strategy: ClassVar[list[ParameterSet]] = [
        pytest.param(
            {
                "strategy": DuplicationStrategyCreate(
                    title="Updated Test Strategy",
                    repeat_mode_id=RepeatModeId.WEEKLY,
                    days=[2, 4],
                    interval=2,
                    content_type=DuplicateRecords.NO,
                )
            },
            True,
            id="valid update_duplication_strategy",
        )
    ]

    duplicate: ClassVar[list[ParameterSet]] = [
        pytest.param(
            {
                "activity_id": None,
                "payload": {
                    "dates": [future_date, future_date2],
                    "content_type": DuplicateRecords.NO,
                    "force": False,
                },
            },
            True,
            id="valid duplicate",
        )
    ]
