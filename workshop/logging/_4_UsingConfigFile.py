import logging
import logging.config
class LoggerDemoConfig:

    def testLog(self):
        #Create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConfig.__name__)

        logger.debug("This is a good logging:")
        logger.info("This is info message:")
        logger.warning("This is warning message:")
        logger.error("This is error message:")
        logger.critical("This is critical message:")


demo = LoggerDemoConfig()
demo.testLog()

"""
Check more exmaple from refrence
https://github.com/amilstead/python-logging-examples

"""