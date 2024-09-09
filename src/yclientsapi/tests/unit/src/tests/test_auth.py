import os


def test_auth_user(lib):
    user_token = lib.auth.get_user_token(
        os.getenv("YCLIENTS_USER_LOGIN"), os.getenv("YCLIENTS_USER_PASSWORD")
    )
    assert isinstance(user_token, str)
    assert len(user_token) > 0
