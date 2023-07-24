import logging
import logging.handlers
import sys

import configparser


def convert_to_dict():
    js = {"version": 1}
    config = configparser.RawConfigParser()
    config.read('logging_conf.ini')
    for section in config.sections():
        json_data = {section: value for key, value in config.items(section)}
        js.update(json_data)
    return js


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
            "filename": "logfile.log",
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
    },
}



