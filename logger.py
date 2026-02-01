import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok = True)

logger = logging.getLogger("test_task_tests")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, "test.log"), encoding = "utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
