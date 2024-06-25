"""custom logger for logging"""
import logging

class CustomeLogging:
    """
    class for Custom logging
    """
    def __init__(self):
        self.format = '%(levelname)s - %(asctime)s - %(message)s'
        self.level = logging.INFO

    def logger(self, name):
        """
        Logger method
        """ 
        file = name + '.log'
        logger = logging.getLogger()
        logging.basicConfig(level=self.level, format = self.format, filename=file)
        return logger
