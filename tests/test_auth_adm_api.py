

class TestAuth_adm:
        """Авторизация под новым пользователем
            Получить status code 200 OK
            Получить response
        """


def test_auth_new_adm(api_client, registered_user):
    auth_response = api_client.auth(body=registered_user)
    """Отправляем POST на авторизацию с зарегистрированным логином и паролем
       Фикстура registered_user возвращает пароль и логин"""

    assert auth_response.status_code == 200, (f"Check auth request, status code is {auth_response.status_code}. "
                                              f"Response: {auth_response.text}")
    """Проверяем, что сервер вернул 200 ОК, авторизировались"""

    response_json = auth_response.json()
    assert "token" in response_json, f"No token in response: {response_json}"
    assert response_json["token"], "Token is empty"
    """Проверяем, что в ответе есть token и он не пустой"""


