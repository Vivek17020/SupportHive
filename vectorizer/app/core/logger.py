import logging
import os

# Create a custom logger
logger = logging.getLogger("ta-vectordb")
logger.setLevel(logging.DEBUG)  # Set root level; handlers will filter what to show

# Prevent adding duplicate handlers if this script is imported multiple times
if not logger.handlers:
    # Create console handler (INFO and above)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)

    # Create file handler (ERROR and above)
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    f_handler = logging.FileHandler(os.path.join(log_dir, "ta-vectordb.log"))
    f_handler.setLevel(logging.ERROR)

    # Create formatters and set them
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
