import os
import pickle
import numpy as np
import pandas as pd
from src.log_config.logger import logger
from src.exceptions.exceptions import CustomException

# Load the best model
def load_model(file_path):
    try:
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
        logger.info(f"Model loaded successfully from {file_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise CustomException(f"Error loading model: {e}", sys)

# Predict with the model
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

# Example usage
if __name__ == "__main__":
    try:
        logger.info("Starting prediction process...")
        # Use the cleaned_students.csv as new data
        new_data_path = os.path.join("data", "cleaned", "cleaned_students.csv")
        model_path = os.path.join("artifacts", "best_model.pkl")
        preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
        
        # Read the cleaned data
        new_data = pd.read_csv(new_data_path)
        logger.info(f"New data read successfully from {new_data_path}")

        # Drop the target column 'math_score'
        if "math_score" in new_data.columns:
            new_data = new_data.drop(columns=["math_score"])
            logger.info("Dropped the target column 'math_score' from new data")

        # Make predictions
        predictions = make_predictions(new_data, model_path, preprocessor_path)
        print("Predictions:", predictions)
        logger.info("Prediction process completed successfully.")
    except Exception as e:
        logger.error(f"Prediction process failed: {e}")
