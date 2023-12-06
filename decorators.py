"""decorators.py
This module contains all the decorators used in the application."""
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def input_is_valid(f):
    """Validates the input
    Rules:
        - should be an integer and greater than 0 and lower than 1000
    """
    def validate(*args, **kwargs):
        value = args[1]
        if not isinstance(value, int):
            logger.error(f"'{value}' should be integer")
            return None
        elif value <= 0 or value >= 1000:
            logger.error(f"'{value}' should be greater than 0 and lower than 1000")
            return None
        return f(*args, **kwargs)

    return validate


def range_is_valid(f):
    """Validates the input
    Rules:
        - gte arg should be integer and greater than 0 and lower than 1000
        - lte arg should be integer and greater than 0 and lower than 1000
        - gte should be lower than lte
    """

    def validate(*args, **kwargs):
        gte = args[1]
        lte = args[2]

        if not isinstance(gte, int) or not isinstance(lte, int):
            logger.error("Range values should be type: Integer")
            return None
        elif min([lte, gte]) <= 0 or max([lte, gte]) >= 1000:
            logger.error("Both arguments should be greater than 0")
            return None
        elif lte < gte:
            logger.error("gte should be lower than lte")
            return None
        return f(*args, **kwargs)

    return validate
