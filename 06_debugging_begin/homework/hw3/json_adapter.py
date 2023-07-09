"""
Удобно сохранять логи в определённом формате, чтобы затем их можно было фильтровать и анализировать. 
Сконфигурируйте логгер так, чтобы он писал логи в файл skillbox_json_messages.log в следующем формате:

{"time": "<время>", "level": "<уровень лога>", "message": "<сообщение>"}

Но есть проблема: если в message передать двойную кавычку, то лог перестанет быть валидной JSON-строкой:

{"time": "21:54:15", "level": "INFO", "message": "“"}

Чтобы этого избежать, потребуется LoggerAdapter. Это класс из модуля logging,
который позволяет модифицировать логи перед тем, как они выводятся.
У него есть единственный метод — process, который изменяет сообщение или именованные аргументы, переданные на вход.

class JsonAdapter(logging.LoggerAdapter):
  def process(self, msg, kwargs):
    # меняем msg
    return msg, kwargs

Использовать можно так:

logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Сообщение')

Вам нужно дописать метод process так, чтобы в логах была всегда JSON-валидная строка.
"""

import logging
import json
from datetime import datetime

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        message = json.dumps({"time": datetime.now().strftime("%H:%M:%S"),
                              "level": kwargs.get("extra")["level"],
                              "message": msg},
                             ensure_ascii=False)
        # with open("skillbox_json_messages.log", "a") as log:
        #     log.write(message + "\n")
        return message, kwargs


if __name__ == '__main__':
    # format = '{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
    logging.basicConfig(level=logging.DEBUG, format="%(message)s",
                        filename="skillbox_json_messages.log")
    logger = JsonAdapter(logging.getLogger(__name__), extra={"level": None})
    logger.setLevel(logging.DEBUG)
    logger.info('Сообщение', extra={"level": "INFO"})
    logger.info('"', extra={"level": "INFO"})
    logger.error('Кавычка)"', extra={"level": "ERROR"})
    logger.debug("Еще одно сообщение", extra={"level": "DEBUG"})
