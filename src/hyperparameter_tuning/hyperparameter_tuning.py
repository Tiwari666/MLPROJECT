import os
import sys
import pickle
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.exceptions import NotFittedError
from src.log_config.logger import logger
from src.exceptions.exceptions import CustomException

def hyperparameter_tuning(X_train, y_train):
    """
    Perform hyperparameter tuning for Ridge Regression.
    """
    try:
        logger.info("Starting hyperparameter tuning for Ridge Regression...")
        
        # Define hyperparameter grid
        param_grid = {
            'alpha': [0.01, 0.1, 1, 10, 100],
            'solver': ['auto', 'svd', 'cholesky', 'lsqr']
        }
        
        # Initialize Ridge model
        ridge = Ridge()
        
        # GridSearchCV for hyperparameter tuning
        grid_search = GridSearchCV(
            estimator=ridge,
            param_grid=param_grid,
            scoring='r2',
            cv=5,
            verbose=2
        )
        
        # Fit GridSearchCV
        grid_search.fit(X_train, y_train)
        logger.info(f"Best parameters: {grid_search.best_params_}")
        logger.info(f"Best R2 score: {grid_search.best_score_}")

        # Save the tuned model
        tuned_model_path = os.path.join("artifacts", "tuned_model.pkl")
        with open(tuned_model_path, 'wb') as f:
            pickle.dump(grid_search.best_estimator_, f)
        logger.info(f"Tuned model saved at {tuned_model_path}")

    except Exception as e:
        logger.error(f"Error during hyperparameter tuning: {e}")
        raise CustomException(f"Error during hyperparameter tuning: {e}", sys)


if __name__ == "__main__":
    try:
        logger.info("Loading transformed training data for hyperparameter tuning...")
        
        # Load transformed train data
        train_data_path = os.path.join("artifacts", "transformed_train_data.csv")
        train_data = np.loadtxt(train_data_path, delimiter=',', skiprows=1)
        
        # Separate features and target
        X_train = train_data[:, :-1]
        y_train = train_data[:, -1]
        
        logger.info("Data loaded successfully. Initiating hyperparameter tuning...")
        hyperparameter_tuning(X_train, y_train)
        logger.info("Hyperparameter tuning completed successfully.")
    except Exception as e:
        logger.error(f"Failed during hyperparameter tuning: {e}")
        raise CustomException(e, sys)
