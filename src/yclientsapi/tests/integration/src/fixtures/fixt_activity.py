import logging

import httpx
import pytest

from yclientsapi import YclientsAPI
from yclientsapi.tests.integration.src.test_data.activity import Parametrize


def _default_activity_payload():
    return Parametrize.create[0].values[0]["activity"]


@pytest.fixture
def activity_create_fixt(lib: YclientsAPI):
    """
    Fixture that creates an activity for testing.
    Yields the activity ID for the test to use.
    """
    activity = lib.activity.create(activity=_default_activity_payload())
    return activity.data.id


@pytest.fixture
def activity_create_and_cleanup_fixt(lib: YclientsAPI):
    """
    Fixture that creates an activity for testing.
    Yields the activity ID for the test to use, and then cleans up by deleting the activity.
    """
    activity = lib.activity.create(activity=_default_activity_payload())
    yield activity.data.id
    try:
        lib.activity.delete(activity_id=activity.data.id)
    except httpx.HTTPStatusError as err:
        logging.critical(f"Failed to clean up activity {activity.data.id}: {err!s}")
