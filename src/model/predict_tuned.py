import os
import pickle
import numpy as np
import pandas as pd
from src.log_config.logger import logger
from src.exceptions.exceptions import CustomException


# Function to load the model
def load_model(file_path):
    try:
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
        logger.info(f"Model loaded successfully from {file_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model from {file_path}: {e}")
        raise CustomException(f"Error loading model from {file_path}: {e}", sys)


# Function to make predictions
def make_predictions(input_data, model_file_path, preprocessor_file_path):
    try:
        # Load the preprocessor
        with open(preprocessor_file_path, 'rb') as f:
            preprocessor = pickle.load(f)
        logger.info(f"Preprocessor loaded successfully from {preprocessor_file_path}")

        # Transform the input data
        transformed_data = preprocessor.transform(input_data)

        # Load the trained model
        model = load_model(model_file_path)

        # Make predictions
        predictions = model.predict(transformed_data)
        logger.info(f"Predictions made successfully")
        return predictions
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise CustomException(f"Error during prediction: {e}", sys)


# Main block for the prediction process
if __name__ == "__main__":
    try:
        logger.info("Starting prediction process with the tuned model...")

        # Define paths
        new_data_path = os.path.join("data", "cleaned", "cleaned_students.csv")
        model_path = os.path.join("artifacts", "tuned_model.pkl")  # Tuned model
        preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

        # Check if the new data file exists
        if not os.path.exists(new_data_path):
            raise FileNotFoundError(f"Data file not found at {new_data_path}. Please ensure the file exists.")

        # Read the new data
        new_data = pd.read_csv(new_data_path)
        logger.info(f"New data read successfully from {new_data_path}")

        # Make predictions
        predictions = make_predictions(new_data, model_path, preprocessor_path)
        print("Predictions using the tuned model:", predictions)
        logger.info("Prediction process completed successfully.")
    except FileNotFoundError as fnf_error:
        logger.error(fnf_error)
        print(f"Error: {fnf_error}")
    except Exception as e:
        logger.error(f"Prediction process failed: {e}")
        raise CustomException(f"Prediction process failed: {e}", sys)

# Save predictions to a CSV file
predictions_df = pd.DataFrame(predictions, columns=["Predicted Values"])
predictions_df.to_csv('artifacts/predictions_tuned_model.csv', index=False)

logger.info("Predictions saved to 'artifacts/predictions_tuned_model.csv'")
logger.info("Prediction process completed successfully.")