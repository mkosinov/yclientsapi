import pytest

from yclientsapi.schema.service_category import (
    ServiceCategoryListResponse,
    ServiceCategoryResponse,
)
from yclientsapi.tests.integration.vars import service_category_id


@pytest.mark.service
def test_list_service_categories(lib):
    response = lib.service_category.list()
    assert response.success
    assert isinstance(response, ServiceCategoryListResponse)


@pytest.mark.service
@pytest.mark.parametrize(
    "params",
    [
        {"category_id": service_category_id},
    ],
    ids=["valid service_category_id"],
)
def test_get_service_category(lib, params):
    response = lib.service_category.get(**params)
    assert response.success
    assert isinstance(response, ServiceCategoryResponse)
