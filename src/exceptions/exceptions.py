import sys
from src.log_config.logger import logger


def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message with the file name, line number, and error details.
    """
    try:
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}]: {str(error)}"
        return error_message
    except Exception as e:
        logger.error(f"Error in error_message_detail function: {e}")
        return f"Error message could not be generated due to: {e}"


class CustomException(Exception):
    """
    Custom exception class that logs detailed error information.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        try:
            self.error_message = error_message_detail(error_message, error_detail)
            logger.error(self.error_message)
        except Exception as e:
            logger.error(f"Failed to initialize CustomException: {e}")
            self.error_message = f"Failed to log error details: {e}"

    def __str__(self):
        return self.error_message


# Optional: Usage Example for Debugging (Remove in Production)
if __name__ == "__main__":
    try:
        # Simulating a division by zero error
        result = 10 / 0
    except Exception as e:
        # Example of using CustomException
        raise CustomException("An error occurred during the operation.", sys)




""" 
This script enhances error handling by defining a CustomException class that captures detailed information about errors, 
including the file name and line number where the error occurred. This is achieved through the error_message_detail function, 
which utilizes Python's sys module to access the current exception's traceback. 
By integrating this with the application's logging system, the custom exception provides a clear and informative message when raised,
facilitating easier debugging and maintenance.

"""


"""
In Python, the sys module provides access to system-specific parameters and functions that interact closely with 
the Python interpreter. It allows us to manipulate various aspects of the runtime environment, such as command-line arguments, 
standard input/output streams, and exception handling.

In this code, sys is used to access the current exception information within the error_message_detail function and 

interact with the command-line environment in Python.

For example, sys.argv can be used to retrieve command-line arguments passed to a script, allowing for dynamic input handling.
 Additionally, sys.exit() can be used to terminate a script with a specific exit status, which is useful for signaling 
 success or failure to the operating system or calling process.
"""


"""
In Python, exc_tb refers to the traceback object associated with the most recent exception. 
A traceback provides a detailed report of the active stack frames at a particular point in time during the execution of a program, 
especially when an exception is raised. It helps developers trace the sequence of function calls that led to the error,
making it easier to identify and fix issues in the code.

Example:

import sys

try:
    # Code that may raise an exception
    result = 10 / 0
except Exception:
    exc_type, exc_value, exc_tb = sys.exc_info()
    # Now, exc_tb contains the traceback object

"""


"""
Understanding and utilizing traceback objects in Python is essential for effective debugging.
 They provide a clear view of the program's execution path leading up to an error, enabling developers to identify 
 and resolve issues more efficiently.
"""