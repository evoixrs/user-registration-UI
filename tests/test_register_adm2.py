
import requests
from api_client.models.register import RegisterModel
#from api_client.texts.error_texts import ResponseErrorText

class TestRegister_adm2:
        """Регистрация нового администратора
            Получить status code 200 OK
            Получить response
        """

        def test_register_new_adm_valid2(self, api_client):
                body = RegisterModel().random()
                response = api_client.register(body=body)
                assert response.status_code == 200, f"Check register request, status code is {response.status_code}"
                assert response.json()["status"] == "Successful", f"Registration failed, response: {response.json()}"


