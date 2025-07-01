import logging

from requests import Response

logger = logging.getLogger("api_tests")


def log_response(response: Response, request_body: dict = None):
    method = response.request.method
    url = response.url
    status_code = response.status_code
    """Получаем метод, URL и статус-код из объекта ответа"""

    logger.info(f"HTTP {method}, request to URL {url}")
    """Выводит в лог, какой метод и по какому адресу был запрос"""

    if request_body is not None:
        logger.info(f"Request body: {request_body}")
    """Если был передан request_body, пишет его в лог"""

    logger.info(f"Status code is {status_code}")
    """Пишет в лог статус-код ответа"""

    try:
        logger.info(f"Response body: {response.json()}")
    except ValueError:
        logger.info(f"Response is not JSON, {response.text}")
        """Вывести тело ответа как JSON"""