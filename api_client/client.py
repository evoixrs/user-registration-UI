import logging

import requests
from requests import Response

logger = logging.getLogger("api_tests")

class StoreClient:
    _REGISTER = "/api/register"
    """Константа с путем для регистрации"""

    def __init__(self, url: str):
        self.url = url
    """Сохраняем базовый URL сервера"""

    def register(self, body: dict) -> Response:
        logger.info(f'Register new user, with body {body}')
        """Логируем инф. о регистрации пользователя"""

        res = requests.post(url=f'{self.url}{self._REGISTER}', json=body)
        """POST запрос на ручку /api register с телом запроса(body) в JSON."""

        logger.info(f'Status code is {res.status_code}, response body is {res.json()}')
        """Логируем статус-код и тело ответа в формате JSON"""

        return res