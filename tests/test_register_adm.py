
from api_client.texts.response_texts import ResponseTest
from api_client.models.register import RegisterModel
from api_client.texts.error_texts import ResponseErrorText

class TestRegister_adm:
        """Регистрация нового администратора
            Получить status code 200 OK
            Получить response
        """

        def test_register_new_adm_valid(self, api_client):
                body = RegisterModel().random()
                """Генерация случайного логина и пароля для нового пользователя"""

                response = api_client.register(body=body)
                """Отправляем запрос на регистрацию админа через API"""

                assert response.status_code == 200, f"Check register request, status code is {response.status_code}"
                """Проверяем, что сервер вернул  200 ОК"""

                assert response.json()["status"] == "Successful", f"Registration failed, response: {response.json()}"
                """Проверяем, что в ответе есть ключ "status" со значением "Successful"""

                #assert response.json().get("message") == ResponseTest.CREATE_USER,(f"Expected message '{ResponseTest.CREATE_USER}',"
                                                                                   #f" "f"got '{response.json().get('message')}'")
                 
                """Проверяем текст сообщения об успешном создании пользователя"""

                print(response.json())

        def test_register_with_existing_login(self, api_client, registered_user):
                """Регистрация с уже существующим администратором (логин)
                    Получить status code 400
                    Получить response
                """
                response = api_client.register(body=registered_user)
                assert response.status_code == 400, (
                        f"Expected status code 400, got {response.status_code}. Response: {response.text}"
                )
                error_message = response.json().get("message")

                assert error_message == ResponseErrorText.USER_ALREADY_EXISTS, (
                        f"Expected message '{ResponseErrorText.USER_ALREADY_EXISTS}', got '{error_message}'"
                )



