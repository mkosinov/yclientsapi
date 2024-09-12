from yclientsapi.tests.integration.vars import user_login, user_password


def test_auth_user(lib):
    user_token = lib.auth.get_user_token(user_login, user_password)
    assert isinstance(user_token, str)
    assert len(user_token) > 0
