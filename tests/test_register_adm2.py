

from api_client.models.register import RegisterModel

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


