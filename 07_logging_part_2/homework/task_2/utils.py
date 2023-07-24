import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add
from logger_config import stream

logger = logging.getLogger('utils')
logger.setLevel('DEBUG')
logger.propagate = False
stream_handler = stream()
logger.addHandler(stream_handler)

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    logger.info(f"Operator: {value}")
    if not isinstance(value, str):
        print("wrong operator type", value)
        logger.error(value + 'is not str')
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        print("wrong operator value", value)
        logger.error(value + 'not in operators')
        raise ValueError("wrong operator value")

    return OPERATORS[value]
