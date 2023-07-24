# import logging
import logging.config
from typing import Union, Callable
from operator import sub, mul, truediv, add
from logger_config import dict_config


logging.config.dictConfig(dict_config)
logger = logging.getLogger('utils')
logger.setLevel('DEBUG')

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
