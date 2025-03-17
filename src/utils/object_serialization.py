import pickle
import os
from src.exception import CustomException
import sys

def save_object(file_path, obj):
    """Function to save a Python object to a file."""
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    """Function to load a Python object from a file."""
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise CustomException(e, sys)
