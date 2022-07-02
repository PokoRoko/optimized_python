import datetime

from loguru import logger


def def_time(func) -> ():
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        logger.debug(f"def '{func.__name__}' execute: {end - start}")
    return wrapper
