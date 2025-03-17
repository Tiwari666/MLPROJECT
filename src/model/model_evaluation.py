import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from src.log_config.logger import logger  # Global import for logger
import sys
import os


def evaluate_model(model, X_test, y_test):
    """
    Evaluates the performance of a regression model on a test set.
    Returns MAE, RMSE, and R2 Score.
    """
    from src.utils.common_utils import CustomException  # Local import for CustomException
    try:
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2_score_value = r2_score(y_test, y_pred)

        logger.info(f"Evaluation metrics for model {model.__class__.__name__}:")
        logger.info(f"Mean Absolute Error (MAE): {mae}")
        logger.info(f"Root Mean Squared Error (RMSE): {rmse}")
        logger.info(f"R2 Score: {r2_score_value}")

        return mae, rmse, r2_score_value
    except Exception as e:
        raise CustomException("Error in model evaluation.", sys)


def evaluate_regression_models(X_train, y_train, X_test, y_test):
    """
    Trains and evaluates multiple regression models and logs their performance.
    """
    from src.utils.common_utils import save_object, CustomException  # Local imports for circular import handling
    try:
        models = {
            "Linear Regression": LinearRegression(),
            "Lasso": Lasso(),
            "Ridge": Ridge(),
            "K-Neighbors Regressor": KNeighborsRegressor(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest Regressor": RandomForestRegressor(),
            "XGBRegressor": XGBRegressor(),
            "CatBoost Regressor": CatBoostRegressor(verbose=False),
            "AdaBoost Regressor": AdaBoostRegressor()
        }

        best_model = None
        best_r2_score = float("-inf")
        best_model_name = None

        for model_name, model in models.items():
            logger.info(f"Training model: {model_name}")
            model.fit(X_train, y_train)

            # Evaluate the model
            mae, rmse, r2_score_value = evaluate_model(model, X_test, y_test)

            # Update the best model if current model has a better R2 score
            if r2_score_value > best_r2_score:
                best_r2_score = r2_score_value
                best_model = model
                best_model_name = model_name

            logger.info("=" * 35)

        # Save the best model
        best_model_path = os.path.join("artifacts", "best_model.pkl")
        save_object(best_model_path, best_model)
        logger.info(f"Best Model: {best_model_name} with R2 Score: {best_r2_score}")
        logger.info(f"Best Model saved at: {best_model_path}")

        return best_model_name, best_r2_score, best_model_path

    except Exception as e:
        raise CustomException("Error in evaluate_regression_models.", sys)
