# Integration tests for yclientapi

This directory contains integration tests for the yclientsapi package.
No functional tests are made, as package functionality is only a wrapper to API calls, and there is no logic to test.

## Stack

* pytest
* httpx
* pydantic

Tests include only "get" method requests to the Yclients API using real account and real data.
No create/update/delete methods are being tested as they will leave an undesirable footprint in real account and also require these methods to be added to the package.

If you want to run tests on your own account, you have to provide both enviroment variables (as in .env.example) and test data (as in /src/yclientsapi/tests/integration/src/test_data/).
