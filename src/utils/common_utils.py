import pickle
import os
from src.log_config.logger import logger


class CustomException(Exception):
    """Custom exception class that logs detailed error information."""
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message


def save_object(file_path, obj):
    """Save a Python object to a file using pickle."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump(obj, f)
        logger.info(f"Object saved successfully at {file_path}")
    except Exception as e:
        logger.error(f"Error occurred while saving object: {e}")
        raise CustomException(e, sys)
