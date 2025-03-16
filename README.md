# Poor YclientsAPI

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

/src/yclientsapi/tests/integration/README.md

## More info

* <https://yclients.com/appstore/developers>
* <https://developers.yclients.com/>
