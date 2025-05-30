import pytest

from yclientsapi.tests.integration.src.test_data.service_category import Parametrize


def _default_service_category_payload():
    return Parametrize.create[0].values[0]["service_category"]


@pytest.fixture
def service_category_fixt_create_cleanup(lib):
    response = lib.service_category.create(
        service_category=_default_service_category_payload()
    )
    category_id = response.data.id
    yield category_id
    lib.service_category.delete(category_id)


@pytest.fixture
def service_category_create_fixt(lib):
    response = lib.service_category.create(
        service_category=_default_service_category_payload()
    )
    category_id = response.data.id
    yield category_id
