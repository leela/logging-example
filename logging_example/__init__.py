import logging
from logging import FileHandler
from .add import addition
from .div import division

root_logger = logging.getLogger()   # Returns the root logger
root_logger.setLevel(logging.DEBUG) # handles messages of severity DEBUG and above

# create a handler to log all messages of sevirity DEBUG and above.
debug_handler = FileHandler("debug.log")
debug_handler.setLevel(logging.DEBUG)
# We can pass the  message format using setFormatter. Notice that log name is added.
debug_handler.setFormatter(logging.Formatter('%(name)s::%(message)s'))

# create a handler to log all messages of sevirity ERROR and above.
error_handler = FileHandler("error.log")
error_handler.setLevel(logging.ERROR)
# every record in log looks like `logger_name::log_message`
error_handler.setFormatter(logging.Formatter('%(name)s::%(message)s'))

# add handlers to root logger.
# logger sends all the incoming messages to all the handlers.
root_logger.addHandler(debug_handler)
root_logger.addHandler(error_handler)

