import logging

logger = logging.getLogger(__name__)

def division(a, b):
    logger.debug(f"{a} divided by {b}")  # this message comes only in debug.log
    try:
        return a/b
    except ZeroDivisionError:
        logger.error("Zero division error", exc_info=True) # this message comes in both error.log & debug.log
