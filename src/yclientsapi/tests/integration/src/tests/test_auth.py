from yclientsapi.schema.auth import AuthResponse
from yclientsapi.tests.integration.vars import user_login, user_password


def test_auth_user(lib):
    response = lib.auth.authenticate(user_login, user_password)

    assert response.success
    assert isinstance(response, AuthResponse)
