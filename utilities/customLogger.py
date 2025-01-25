import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_path = ".\\Logs\\automation.log"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)  # Create directory if not exists

        logger = logging.getLogger("AutomationLogger")
        if not logger.hasHandlers():
            logging.basicConfig(
                filename=log_path,
                format='%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p',
                level=logging.INFO
            )
        return logger
