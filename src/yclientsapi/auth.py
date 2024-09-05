class Authentication:
    def auth_user(self, login: str, password) -> str:
        """Send user credentials and get user token.
        :param login: В качестве логина может быть использован номер телефона пользователя в формате 79161234567 или его Email
        :param password: Пароль пользователя
        :return: User token
        """

        respone = self.config.client.post()
        self.config.user_token = partner_token
