import os
import pandas as pd
from src.log_config.logger import logger
from src.model.predict import make_predictions
from sklearn.metrics import r2_score

def compare_r2_scores():
    try:
        # Paths for models and preprocessor
        model_path_before_tuning = os.path.join("artifacts", "best_model.pkl")
        model_path_after_tuning = os.path.join("artifacts", "tuned_model.pkl")
        preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
        
        # Read the data
        new_data_path = os.path.join("data", "cleaned", "cleaned_students.csv")
        new_data = pd.read_csv(new_data_path)

        # Make predictions for the original model
        logger.info("Making predictions using the original model...")
        predictions_before_tuning = make_predictions(new_data, model_path_before_tuning, preprocessor_path)
        
        # Make predictions for the tuned model
        logger.info("Making predictions using the tuned model...")
        predictions_after_tuning = make_predictions(new_data, model_path_after_tuning, preprocessor_path)

        # Actual values (target) - Adjust this to your dataset
        y_actual = new_data["math_score"]  # Replace with the actual column name

        # Calculate R2 scores for both models
        r2_before = r2_score(y_actual, predictions_before_tuning)
        r2_after = r2_score(y_actual, predictions_after_tuning)

        # Logging the R2 scores
        logger.info(f"R2 Score before tuning: {r2_before}")
        logger.info(f"R2 Score after tuning: {r2_after}")

        # Compare and save results
        with open(os.path.join("artifacts", "r2_comparison.txt"), "w") as file:
            file.write(f"R2 Score before tuning: {r2_before}\n")
            file.write(f"R2 Score after tuning: {r2_after}\n")

        logger.info("R2 comparison saved successfully.")

    except Exception as e:
        logger.error(f"Error in comparing R2 scores: {e}")

# Call the comparison function
if __name__ == "__main__":
    compare_r2_scores()
