import logging
import logging.handlers
import sys

class AsciiFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:

        from string import ascii_letters, digits, punctuation, whitespace

        for i in str(record):
            if i not in (ascii_letters + digits + punctuation + whitespace):
                return False
        return True


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
            "datefmt": "%y-%m-%d %H:%M:%S"
        }
    },
    "filters": {
        "ascii_filter": {
            "()": AsciiFilter
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": logging.DEBUG,
            "formatter": "simple",
            "stream": sys.stdout,
        },
        "file": {
            "class": 'logging.FileHandler',
            "level": logging.DEBUG,
            "filters": ["ascii_filter"],
            "formatter": "simple",
            "filename": "calc.log",
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
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False
        }
    }
}



