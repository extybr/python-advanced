import logging
import logging.handlers
import sys
from logging_tree import format

class CustomHandler(logging.Handler):
    def __init__(self, file_name='', mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        with open(self.file_name, mode=self.mode) as log:
            log.write(message + '\n')

        with open("logging_tree.txt", mode="w") as log:
            log.write(format.build_description())


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
            "datefmt": "%y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": logging.DEBUG,
            "formatter": "simple",
            "stream": sys.stdout
        },
        "file": {
            "()": CustomHandler,
            "level": logging.DEBUG,
            "formatter": "simple",
            "file_name": "calc.log",
            "mode": "a"
        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "utils": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        }
    },
}



