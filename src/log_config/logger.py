import logging
import os
from datetime import datetime

# Define the root directory and logs directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  # Explicitly go two levels up
LOGS_DIR = os.path.join(ROOT_DIR, "logs")  # Define logs directory in the project root
os.makedirs(LOGS_DIR, exist_ok=True)  # Create the logs directory if it doesn't exist

# Generate a dynamic log filename
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode="a"),  # Append logs to the file
        logging.StreamHandler()                       # Log to the console
    ]
)

# Get the logger instance
logger = logging.getLogger("MLProjectLogger")

if __name__ == "__main__":
    logger.info("Logging has been started.")
    logger.warning("This is a warning log.")
    logger.error("This is an error log.")
    logger.critical("This is a critical log.")







"""
if __name__ == "__main__":
    #  logging setup and usage code here
This block ensures that the logging setup and usage code runs only when the script is executed directly,
not when imported as a module.
"""    


# The logger module provides a centralized mechanism for recording log messages in a Python application. 
# By configuring the logging settings, developers can control the log output format, log level, and log file location. 
# This enables the application to generate detailed logs that capture relevant information about its execution, errors, and warnings.

# In this example, we define a logger object that writes log messages to a log file with a filename based on the 
# current date and time.

# The logger object is configured to log messages with different severity levels, such as INFO, WARNING, ERROR, and CRITICAL.

# By using the logger object to record log messages, developers can track the application's behavior, identify issues.
# and monitor its performance. This is particularly useful for debugging, troubleshooting, and maintaining the application.


"""
Explanation:

Imports:

 --logging: Python's built-in module for logging messages.

--os: Provides a way to interact with the operating system, such as file and directory operations.

--datetime: Used to get the current date and time for dynamic log filenames.

Dynamic Log Filename:

LOG_FILE: Creates a log filename based on the current date and time in the format MM_DD_YYYY_HH_MM_SS.log. This ensures that
 each log file is unique and timestamped.

Logs Directory:

logs_path: Defines the path to the logs directory within the current working directory.

os.makedirs(logs_path, exist_ok=True): Creates the logs directory if it doesn't already exist. 
The exist_ok=True parameter prevents an error if the directory already exists.

Log File Path:

LOG_FILE_PATH: Combines the logs_path and LOG_FILE to get the full path to the log file.
Logging Configuration:

logging.basicConfig(): Configures the logging system.

filename=LOG_FILE_PATH: Sets the log file's path.

format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

:Defines the log message format, including the timestamp, line number, logger name, log level, and the actual message.

level=logging.INFO

:Sets the logging level to INFO, meaning all messages at this level and above will be tracked.

"""