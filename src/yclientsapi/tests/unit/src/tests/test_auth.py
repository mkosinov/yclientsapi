def test_auth_user(init_lib):
    user_token = init_lib.get_user_token("info@colourmountains.ru", "Oblomist!1")
    assert isinstance(user_token, str)
    assert len(user_token) > 0
