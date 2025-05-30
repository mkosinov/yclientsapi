# Poor YclientsAPI

[![codecov](https://codecov.io/gh/mkosinov/yclientsAPI/branch/main/graph/badge.svg)](https://codecov.io/gh/mkosinov/yclientsAPI)

Small set of methods for working with Yclients API. Non official.

## Installation

```bash
pip install poor_yclientsapi
```

## Usage

```python
>>> from yclientsapi import YclientsAPI
>>> with YclientsAPI(COMPANY_ID, PARTNER_TOKEN, USER_TOKEN) as api:
>>>     services = api.service.list(staff_id=MY_STAFF_ID)
```

COMPAMY_ID - client company id from YCLIENTS
PARTNER_TOKEN - general developer token from YCLIENTS
USER_TOKEN - authorization token for client data access in YCLIENTS (Optional)

If you don't have USER_TOKEN, you can call auth.authenticate(USER_LOGIN, USER_PASSWORD) later to retrive and save USER_TOKEN for futher requests

## Tests

Integration tests are located in `/src/yclientsapi/tests/integration/`. See `/src/yclientsapi/tests/README.md` for details on running tests and setup. CRUD operations for service categories are covered by integration tests and use fixtures for setup/cleanup.

## More info

* <https://yclients.com/appstore/developers>
* <https://developers.yclients.com/>
