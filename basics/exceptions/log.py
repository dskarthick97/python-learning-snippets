""" Log module """

import sys
import logging

FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = logging.FileHandler("exceptions.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name, handler):
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    logger.propagate = False
    return logger
