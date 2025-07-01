import logging

import requests
from requests import Response

from utils.logger_api import log_response

logger = logging.getLogger("api_tests")

class StoreClient:
    _REGISTER = "/api/register"
    """Константа с путем для регистрации"""

    _AUTH = "/api/auth"
    """Константа с путем для авторизации"""

    def __init__(self, url: str):
        self.url = url
    """Сохраняем базовый URL сервера"""

    def register(self, body: dict) -> Response:

        res = requests.post(url=f'{self.url}{self._REGISTER}', json=body)
        """POST запрос на ручку /api register с телом запроса(body) в JSON."""

        log_response(response=res, request_body=body)
        """Логирование отправленного запроса и ответа"""

        return res

    def auth(self, body: dict) -> Response:

        res = requests.post(url=f'{self.url}{self._AUTH}', json=body)
        """POST запрос на ручку /api auth с телом запроса(body) в JSON,
        передавая логин и пароль"""

        log_response(response=res, request_body=body)
        """Логирование отправленного запроса и ответа"""

        return res