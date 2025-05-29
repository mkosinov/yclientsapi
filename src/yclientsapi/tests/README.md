# Integration tests for yclientapi

This directory contains integration tests for the yclientsapi package.
No functional tests are made, as package functionality is only a wrapper to API calls, and there is no logic to test.

## Stack

* pytest
* httpx
* pydantic

## Running Tests

To run the integration tests, use:

```bash
pytest src/yclientsapi/tests/integration/src/tests/test_activity.py
```

Some tests will create data in your account but should cleanup after tests finish.

## Coverage

To measure test coverage, run:

```bash
pytest --cov=src
```

This will display a coverage summary in the terminal. For a detailed HTML report, run:

```bash
pytest --cov=src --cov-report=html
```

The HTML report will be generated in the `htmlcov` directory.

## Setup

If you want to run tests on your own account, you have to provide both environment variables (as in .env.example) and test data (as in /src/yclientsapi/tests/integration/src/test_data/).
