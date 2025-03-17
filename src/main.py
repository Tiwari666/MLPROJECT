import sys
import os
import logging
from datetime import datetime

# Add the src directory to the path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Generate a dynamic log filename based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Define the root directory and logs directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root directory of the project
LOGS_DIR = os.path.join(ROOT_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # Create the logs directory if it doesn't exist

# File path for the log file
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# FileHandler for writing logs to a file
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode="a"),  # Append logs to the file
        logging.StreamHandler()                       # Log to the console
    ]
)

# Create and return a logger instance
logger = logging.getLogger("MLProjectLogger")

# Import other modules
from exceptions.exceptions import CustomException  
from data_ingestion import load_data
from data_transformation import transform_data
from hyperparameter_tuning import tune_parameters
from model.train_model import train
from model.model_evaluation import evaluate
from model.feature_importance import calculate
from api.app import run


def main():
    """Main function to execute the application flow."""
    try:
        # Example usage of the imported modules
        logger.info("Starting the application workflow.")
        load_data()
        transform_data()
        tune_parameters()
        train()
        evaluate()
        calculate()
        run()
        logger.info("Application workflow completed successfully.")
    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    # Run the main application
    main()

    # Additional logging examples
    logger.info("Logging has been started.")
    logger.warning("Logging warning: look at it.")
    logger.error("Logging error: please fix it.")
    logger.critical("Logging critical message: the serious message.")

