from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
from src.exceptions.exceptions import CustomException
import sys

def evaluate_regression_model(X_train, y_train, X_test, y_test, models, param):
    """
    Function to evaluate regression model performance.
    Performs grid search for hyperparameter tuning and evaluates models.

    Parameters:
    - X_train, y_train: Training data
    - X_test, y_test: Testing data
    - models: Dictionary of models to evaluate
    - param: Dictionary of hyperparameters for each model

    Returns:
    - report: Dictionary containing evaluation metrics for each model
    """
    try:
        report = {}

        # Iterate through the models and their corresponding parameters
        for model_name, model in models.items():
            logger.info(f"Evaluating model: {model_name}")

            # Retrieve hyperparameters for the current model
            params = param.get(model_name, {})

            # Perform GridSearchCV for hyperparameter tuning
            gs = GridSearchCV(estimator=model, param_grid=params, cv=3, scoring='r2', n_jobs=-1)
            gs.fit(X_train, y_train)

            # Set the best parameters to the model
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Make predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate evaluation metrics
            train_rmse = mean_squared_error(y_train, y_train_pred, squared=False)
            test_rmse = mean_squared_error(y_test, y_test_pred, squared=False)
            train_mae = mean_absolute_error(y_train, y_train_pred)
            test_mae = mean_absolute_error(y_test, y_test_pred)
            train_r2 = r2_score(y_train, y_train_pred)
            test_r2 = r2_score(y_test, y_test_pred)

            # Log metrics
            logger.info(f"Model: {model_name}")
            logger.info(f"Train RMSE: {train_rmse}, Test RMSE: {test_rmse}")
            logger.info(f"Train MAE: {train_mae}, Test MAE: {test_mae}")
            logger.info(f"Train R2: {train_r2}, Test R2: {test_r2}")

            # Store metrics in the report
            report[model_name] = {
                'train_rmse': train_rmse,
                'test_rmse': test_rmse,
                'train_mae': train_mae,
                'test_mae': test_mae,
                'train_r2': train_r2,
                'test_r2': test_r2
            }

        return report

    except Exception as e:
        logger.error(f"Error during model evaluation: {e}")
        raise CustomException(e, sys)

# Example Usage
if __name__ == "__main__":
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.datasets import make_regression
    from sklearn.model_selection import train_test_split

    # Generate synthetic regression data
    X, y = make_regression(n_samples=1000, n_features=10, noise=0.1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define models and hyperparameters
    models = {
        "LinearRegression": LinearRegression(),
        "RandomForestRegressor": RandomForestRegressor()
    }

    params = {
        "LinearRegression": {},
        "RandomForestRegressor": {
            "n_estimators": [10, 50, 100],
            "max_depth": [None, 10, 20]
        }
    }

    # Evaluate models
    try:
        results = evaluate_regression_model(X_train, y_train, X_test, y_test, models, params)
        print(results)
    except Exception as e:
        print(f"Error: {e}")
