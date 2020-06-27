"""
Logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""


import logging

#This is provided by logging to do changes to loggin,
#Default level is warn.
logging.basicConfig(filename="sample.log",level=logging.DEBUG)

logging.debug("This is a good logging")
logging.info("This is info message:")
logging.warning("This is warning message:")
logging.error("This is error message:")
logging.critical("This is critical message:")



