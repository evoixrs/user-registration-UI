class ResponseErrorText:
    USERNAME_PASSWORD = "Username and password are required fields"
    """Ошибка, нужны оба поля: и логин, и пароль."""

    BAD_REQUEST = "Bad Request"
    """некорректный или неправильно составленный запрос."""

    INVALID_CREDENTIALS = "Invalid credentials"
    """неверные логин или пароль"""

    USER_ALREADY_EXISTS = "User already exists"
    """Пользователь уже существует"""