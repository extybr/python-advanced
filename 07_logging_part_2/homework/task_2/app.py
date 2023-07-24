import sys
import logging
from utils import string_to_operator
from logger_config import stream

logger = logging.getLogger('app')
logger.setLevel('DEBUG')
logger.propagate = False
stream_handler = stream()
logger.addHandler(stream_handler)


def calc(args: list) -> None:
    logger.info(f"Arguments: {args}")
    print("Arguments: ", args)

    number_1 = args[0]
    operator = args[1]
    number_2 = args[2]

    try:
        number_1 = float(number_1)
    except ValueError as error:
        logger.error(error)
        print("Error while converting number 1")
        print(error)

    try:
        number_2 = float(number_2)
    except ValueError as error:
        logger.error(error)
        print("Error while converting number 1")
        print(error)

    operator_func = string_to_operator(operator)

    result = operator_func(number_1, number_2)

    print("Result: ", result)
    print(f"{number_1} {operator} {number_2} = {result}")
    logger.info(f"Result: {result}")


if __name__ == '__main__':
    calc(sys.argv[1:])
