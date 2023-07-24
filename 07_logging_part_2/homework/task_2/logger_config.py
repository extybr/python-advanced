import logging
import sys


def stream():
    formatter = logging.Formatter(
        fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
        datefmt="%y-%m-%d %H:%M:%S"
    )
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)
    return stream_handler
