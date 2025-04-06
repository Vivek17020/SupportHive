# customer_support_chat/app/core/logger.py
import logging
from .settings import get_settings

config = get_settings()

logger = logging.getLogger("customer_support_chat")

# Prevent adding multiple handlers if logger is reused (e.g., during hot-reloading or testing)
if not logger.handlers:
    logger.setLevel(getattr(logging, config.LOG_LEVEL, "DEBUG"))

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(getattr(logging, config.LOG_LEVEL, "DEBUG"))

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"
    )
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    # Optional: Enable file logging
    # file_handler = logging.FileHandler("app.log")
    # file_handler.setLevel(getattr(logging, config.LOG_LEVEL, "DEBUG"))
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)
