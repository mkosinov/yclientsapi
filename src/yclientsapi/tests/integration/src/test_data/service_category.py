# Test data for service_category integration tests

from typing import ClassVar

import pytest

from yclientsapi.schema.service_category import (
    ServiceCategoryCreateRequest,
    ServiceCategoryUpdateRequest,
)


class Parametrize:
    create: ClassVar[list] = [
        pytest.param(
            {
                "service_category": ServiceCategoryCreateRequest(
                    title="Test Category",
                    booking_title="Test Category",
                    api_id="test_api_id",
                    weight=1,
                    staff=[],
                )
            },
            True,
            id="valid create",
        ),
    ]

    update: ClassVar[list] = [
        pytest.param(
            {
                "service_category": ServiceCategoryUpdateRequest(
                    title="Updated Category",
                    booking_title="Updated Category",
                    weight=2,
                    staff=[],
                )
            },
            True,
            id="valid update",
        ),
    ]


# Add more edge cases as needed, e.g. missing fields, long titles, etc.
