from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def test_logs(request):
    logger.debug("Это DEBUG сообщение")
    logger.info("Это INFO сообщение")
    logger.warning("Это WARNING сообщение")
    logger.error("Это ERROR сообщение")
    logger.critical("Это CRITICAL сообщение")
    return HttpResponse("Проверка логов!")