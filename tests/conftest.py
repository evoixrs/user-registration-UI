import logging

import pytest
from api_client.client import StoreClient
from api_client.models.register import RegisterModel

logger = logging.getLogger("api_tests")

def pytest_addoption(parser):
     parser.addoption("--api-url", action="store", default="http://158.160.87.146:5000",
                      help="foo: bar or baz")

@pytest.fixture(scope="session")
def api_client(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start app on address {url}")
    """Логи, на какой адрес будет отправляться запрос"""

    client = StoreClient(url=url)
    """Экземпляр StoreClient с этим url для общения с API"""

    return client
    """Возвращаем экземпляр, чтобы использовать его в тестах"""


@pytest.fixture
def registered_user(api_client):
    body = RegisterModel().random()
    """Генерация случайного логина и пароля для нового пользователя"""

    reg_response = api_client.register(body=body)
    """Регистрируем пользователя через API с помощью клиента"""

    assert reg_response.status_code == 200
    """Проверка на успешную регистрацию"""

    return body
    """Возвращает логин и пароль"""

