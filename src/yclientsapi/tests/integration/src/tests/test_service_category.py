import pytest

from yclientsapi.schema.service_category import (
    ServiceCategoryCreateResponse,
    ServiceCategoryGetResponse,
    ServiceCategoryListResponse,
)
from yclientsapi.tests.integration.src.test_data.service_category import Parametrize

pytest_plugins = [
    "src.yclientsapi.tests.integration.src.fixtures.fixt_service_category",
]


@pytest.mark.service
def test_list_service_categories(lib):
    response = lib.service_category.list()
    assert response.success
    assert isinstance(response, ServiceCategoryListResponse)


@pytest.mark.service
@pytest.mark.parametrize(("params", "expected_response"), Parametrize.create)
def test_create_service_category(lib, params, expected_response, request):
    response = lib.service_category.create(**params)
    category_id = response.data.id

    def cleanup():
        lib.service_category.delete(category_id)

    request.addfinalizer(cleanup)
    assert response.success == expected_response
    assert response.data.title == params["service_category"].title
    assert isinstance(response, ServiceCategoryCreateResponse)


@pytest.mark.service
def test_get_service_category(lib, service_category_fixt_create_cleanup):
    category_id = service_category_fixt_create_cleanup
    response = lib.service_category.get(category_id)
    assert response.success
    assert response.data.id == category_id
    assert isinstance(response, ServiceCategoryGetResponse)


@pytest.mark.service
@pytest.mark.parametrize(("params", "expected_response"), Parametrize.update)
def test_update_service_category(
    lib, service_category_fixt_create_cleanup, params, expected_response
):
    category_id = service_category_fixt_create_cleanup
    response = lib.service_category.update(category_id, **params)
    assert response.success == expected_response
    assert response.data.title == params["service_category"].title
    assert isinstance(response, ServiceCategoryGetResponse)


@pytest.mark.service
def test_delete_service_category(lib, service_category_create_fixt):
    category_id = service_category_create_fixt
    response = lib.service_category.delete(category_id)
    assert response is None
