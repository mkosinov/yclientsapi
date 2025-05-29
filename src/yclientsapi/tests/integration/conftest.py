pytest_plugins = [
    "src.yclientsapi.tests.integration.src.fixtures.fixt_lib",
    "src.yclientsapi.tests.integration.src.fixtures.fixt_activity",
    "src.yclientsapi.tests.integration.src.fixtures.fixt_duplication",
]


def pytest_configure(config):
    """Register custom pytest markers to avoid warnings."""
    config.addinivalue_line(
        "markers", "activity: mark tests related to activities"
    )
    config.addinivalue_line(
        "markers",
        "duplication: mark tests related to activity duplication",
    )
