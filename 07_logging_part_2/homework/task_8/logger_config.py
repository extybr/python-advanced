import logging
import logging.handlers
import sys

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
            "class": 'logging.FileHandler',
            "level": logging.DEBUG,
            "formatter": "simple",
            "filename": "calc.log",
            "mode": "a"
        },
        "httpserver": {
            "()": "logging.handlers.HTTPHandler",
            "level": logging.DEBUG,
            "host": "127.0.0.1:5000",
            "url": "/log",
            "method": "POST"
        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console", "file", "httpserver"],
            "propagate": False
        },
        "utils": {
            "level": "DEBUG",
            "handlers": ["console", "file", "httpserver"],
            "propagate": False
        }
    },
}



