import logging
import os
from datetime import datetime


def create_log_directory(log_dir_path="logs"):
    

    try:
        os.makedirs(log_dir_path, exist_ok=True)
        return os.path.abspath(log_dir_path)
    except OSError as e:
        raise OSError(f"Error creating log directory: {e}") from e


LOG_DIR_PATH = create_log_directory()  # Handle potential directory creation errors

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)  # Get a logger for this module
    logger.info('File executed successfully')
