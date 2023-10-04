import logging.handlers
import sys


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "<%(message)s> <%(asctime)s>",
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
            "class": 'logging.FileHandler',
            "level": logging.DEBUG,
            "formatter": "simple",
            "filename": "timestamp.log",
            "mode": "a"
        }
    },
    "loggers": {
        "server": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False
        }
    },
}



