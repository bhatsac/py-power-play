
import logging

# Changing the Format Of Logs
logging.basicConfig(format="%(asctime)s: %(levelname)s:  %(message)s"
                    , datefmt='%m/%d/%Y %I:%M:%S %p'
                    , level=logging.DEBUG)
logging.debug("This is a good logging:")
logging.info("This is info message:")
logging.warning("This is warning message:")
logging.error("This is error message:")
logging.critical("This is critical message:")