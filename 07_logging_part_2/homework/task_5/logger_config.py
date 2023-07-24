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
        "rotate": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": logging.DEBUG,
            "formatter": "simple",
            "filename": "utils.log",
            "when": "h",
            "interval": 10,
            "backupCount": 0,
            "encoding": None,
            "delay": False,
            "utc": False,
            "atTime": None
        }
    },
    "loggers": {
        # "app": {
        #     "level": 10,
        #     "handlers": ["console", "file"],
        #     "propagate": False
        # },
        "utils": {
            "level": "INFO",
            "handlers": ["console", "rotate"],
            "propagate": False
        }
    },
}



