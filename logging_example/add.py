import logging

logger = logging.getLogger(__name__)

def addition(a, b):
    logger.debug(f"Adding {a} and {b}")  # this message comes only in debug.log
    return a+b