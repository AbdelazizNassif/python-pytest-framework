import time
import pytest
import inspect
import logging


# this class to contain common utilities
# this class will have knowledge of the set_up variables and the class that will inherit from it
# this class is basically made to remove redundunt usefixure in other classes
@pytest.mark.usefixtures("set_up")
class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

