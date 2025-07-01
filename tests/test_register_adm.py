

import requests
from faker import Faker

URL = "http://158.160.87.146:5000/"
fake = Faker()


class TestRegister_adm:
    """Регистрация нового администратора
       Получить status code 200 OK
       Получить response
    """
    def test_register_new_adm_valid(self):
        body = {"login": fake.name(), "password": fake.password()}
        response = requests.post(url=f"{URL}/api/register", json=body)
        assert response.status_code == 200, f"Check register request, status code is {response.status_code}"
        assert response.json()["status"] == "Successful", f"Registration failed, response: {response.json()}"







