# src/data_transformation/data_transformation.py

import os
import sys
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from dataclasses import dataclass

# Add the project root to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.log_config.logger import logger
from src.utils.common_utils import save_object
from src.model.model_evaluation import evaluate_regression_models

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "preprocessor.pkl")
    transformed_train_data_path: str = os.path.join('artifacts', 'transformed_train_data.csv')
    transformed_test_data_path: str = os.path.join('artifacts', 'transformed_test_data.csv')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        logger.info("DataTransformation object initialized.")

    def get_data_transformer_object(self):
        """Creates and returns the data preprocessing object."""
        try:
            logger.info("Creating data transformation pipelines.")

            # Define pipelines
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore", sparse=False)),
                ("scaler", StandardScaler(with_mean=False))
            ])

            # Combine pipelines
            preprocessor = ColumnTransformer(transformers=[
                ("num_pipeline", num_pipeline, ["writing_score", "reading_score"]),
                ("cat_pipeline", cat_pipeline, [
                    "gender",
                    "race_ethnicity",
                    "parental_level_of_education",
                    "lunch",
                    "test_preparation_course"
                ])
            ])
            logger.info("Data transformation pipelines created successfully.")
            return preprocessor
        except Exception as e:
            # Import inside the function to avoid circular dependency
            from src.exceptions.exceptions import CustomException
            raise CustomException(f"Error in creating data transformer object: {e}", sys)

    def initiate_data_transformation(self, train_path, test_path):
        """Transforms train and test datasets and saves the preprocessor object."""
        try:
            logger.info(f"Checking existence of train and test files.")
            if not os.path.exists(train_path) or not os.path.exists(test_path):
                raise FileNotFoundError(f"Train or test file does not exist: {train_path}, {test_path}")

            logger.info(f"Reading train data from {train_path}")
            train_df = pd.read_csv(train_path)
            logger.info(f"Reading test data from {test_path}")
            test_df = pd.read_csv(test_path)

            logger.info(f"Train dataset shape: {train_df.shape}")
            logger.info(f"Test dataset shape: {test_df.shape}")

            # Validate required columns
            required_columns = ["writing_score", "reading_score", "gender", "race_ethnicity",
                                "parental_level_of_education", "lunch", "test_preparation_course", "math_score"]
            for col in required_columns:
                if col not in train_df.columns or col not in test_df.columns:
                    raise ValueError(f"Missing required column '{col}' in train or test data.")

            logger.info("Preparing preprocessing object.")
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"

            # Split data into features and target
            input_features_train = train_df.drop(columns=[target_column_name])
            target_feature_train = train_df[target_column_name]

            input_features_test = test_df.drop(columns=[target_column_name])
            target_feature_test = test_df[target_column_name]

            logger.info("Applying transformations.")
            input_features_train_transformed = preprocessing_obj.fit_transform(input_features_train)
            input_features_test_transformed = preprocessing_obj.transform(input_features_test)

            # Combine transformed data with the target variable
            train_data = np.c_[input_features_train_transformed, target_feature_train.to_numpy()]
            test_data = np.c_[input_features_test_transformed, target_feature_test.to_numpy()]

            # Save transformed data
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_data_path), exist_ok=True)
            pd.DataFrame(train_data).to_csv(self.data_transformation_config.transformed_train_data_path, index=False)
            pd.DataFrame(test_data).to_csv(self.data_transformation_config.transformed_test_data_path, index=False)

            logger.info(f"Transformed train data saved at {self.data_transformation_config.transformed_train_data_path}")
            logger.info(f"Transformed test data saved at {self.data_transformation_config.transformed_test_data_path}")

            # Save preprocessor object
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            logger.info(f"Preprocessor object saved at {self.data_transformation_config.preprocessor_obj_file_path}")

            # Perform model evaluation (if needed)
            logger.info("Starting model evaluation with transformed data.")
            evaluate_regression_models(
                input_features_train_transformed,
                target_feature_train,
                input_features_test_transformed,
                target_feature_test
            )

            return (
                self.data_transformation_config.transformed_train_data_path,
                self.data_transformation_config.transformed_test_data_path,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            # Import inside the function to avoid circular dependency
            from src.exceptions.exceptions import CustomException
            raise CustomException(f"Error in data transformation process: {e}", sys)


if __name__ == "__main__":
    train_file_path = os.path.join('data', 'cleaned', 'train.csv')
    test_file_path = os.path.join('data', 'cleaned', 'test.csv')

    try:
        logger.info("Starting the data transformation process.")
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_path=train_file_path, test_path=test_file_path)
        logger.info("Data transformation process completed successfully.")
    except Exception as e:
        logger.error(f"Data transformation failed: {e}")
