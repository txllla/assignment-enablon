import logging

from utils.config_util import ConfigUtil


class Logger:
    __logger = logging.getLogger("Logger")

    __logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(ConfigUtil.get_logger_config()["logging-location"])
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')

    file_handler.setFormatter(formatter)
    __logger.addHandler(file_handler)

    @staticmethod
    def set_level(level):
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message):
        Logger.__logger.info(msg=message)

    @staticmethod
    def debug(message):
        Logger.__logger.debug(msg=message)

    @staticmethod
    def warning(message):
        Logger.__logger.warning(msg=message)

    @staticmethod
    def error(message):
        Logger.__logger.error(msg=message)

    @staticmethod
    def fatal(message):
        Logger.__logger.fatal(msg=message)

    @staticmethod
    def step(message):
        Logger.__logger.info(msg=message)
