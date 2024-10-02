import logging
from logging.handlers import RotatingFileHandler

# Configure logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# File handler (rotating logs after 5MB, keeping last 5 logs)
file_handler = RotatingFileHandler("logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=5)
file_handler.setFormatter(formatter)

# Stream handler (console logs)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Adding handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)

def log_debug(message: str):
    logger.debug(message)
