import os
import shutil
from exceptions.exceptions import CustomException

import sys

def save_file(file_path, content):
    """Function to save content to a file."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "w") as file_obj:
            file_obj.write(content)

    except Exception as e:
        raise CustomException(e, sys)

def move_file(src, dest):
    """Function to move a file from source to destination."""
    try:
        shutil.move(src, dest)
    except Exception as e:
        raise CustomException(e, sys)
