import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
from src.log_config.logger import logger
from src.exceptions.exceptions import CustomException

# Load model
def load_model(file_path):
    try:
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
        logger.info(f"Model loaded successfully from {file_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise CustomException(f"Error loading model: {e}", sys)

# Load preprocessor
def load_preprocessor(file_path):
    try:
        with open(file_path, 'rb') as f:
            preprocessor = pickle.load(f)
        logger.info(f"Preprocessor loaded successfully from {file_path}")
        return preprocessor
    except Exception as e:
        logger.error(f"Error loading preprocessor: {e}")
        raise CustomException(f"Error loading preprocessor: {e}", sys)

# Plot feature importance
def plot_ridge_coefficients(model, feature_names, save_path):
    try:
        if hasattr(model, "coef_"):
            coefficients = model.coef_

            # Ensure feature names match the number of coefficients
            if len(coefficients) != len(feature_names):
                raise ValueError(f"Mismatch: {len(coefficients)} coefficients and {len(feature_names)} features.")

            plt.figure(figsize=(10, 6))
            plt.bar(range(len(coefficients)), coefficients, align="center")
            plt.xticks(range(len(coefficients)), feature_names, rotation=90)
            plt.title("Feature Importances (Coefficients)")
            plt.xlabel("Features")
            plt.ylabel("Coefficient Value")
            plt.tight_layout()

            # Save the plot
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
            plt.close()
            logger.info(f"Feature importance plot saved at {save_path}")
        else:
            logger.info("Feature importance not available for this model.")
    except Exception as e:
        logger.error(f"Error plotting feature importance: {e}")
        raise CustomException(f"Error plotting feature importance: {e}", sys)

if __name__ == "__main__":
    try:
        logger.info("Starting feature importance visualization...")
        model_path = os.path.join("artifacts", "best_model.pkl")
        preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
        feature_importance_path = os.path.join("artifacts", "feature_importance.png")

        # Load the model and preprocessor
        best_model = load_model(model_path)
        preprocessor = load_preprocessor(preprocessor_path)

        # Extract feature names from the preprocessor
        numeric_features = ["writing_score", "reading_score"]
        categorical_features = [
            "gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"
        ]
        one_hot_encoded_features = preprocessor.named_transformers_["cat_pipeline"]["one_hot_encoder"].get_feature_names_out(categorical_features)
        feature_names = np.hstack([numeric_features, one_hot_encoded_features])

        # Plot Ridge coefficients as feature importance
        plot_ridge_coefficients(best_model, feature_names, feature_importance_path)
    except Exception as e:
        logger.error(f"Feature importance visualization failed: {e}")


        
