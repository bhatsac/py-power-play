import logging
class ConsoleLogger:
    def testLog(self):
        #Create Logger
        logger = logging.getLogger(ConsoleLogger.__name__)
        logger.setLevel(logging.INFO)

        #Create handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #Create formatter
        formatter = logging.Formatter("%(asctime)s: - %(name)s %(levelname)s:  %(message)s"
                    ,datefmt='%m/%d/%Y %I:%M:%S %p')

        #Add the formatter to console handler
        chandler.setFormatter(formatter)

        #Add handler to logger
        logger.addHandler(chandler)

        #Now log messages
        logger.debug("This is a good logging:")
        logger.info("This is info message:")
        logger.warning("This is warning message:")
        logger.error("This is error message:")
        logger.critical("This is critical message:")

if __name__=="__main__":
    ConsoleLogger().testLog()