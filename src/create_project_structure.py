import os

# Define the base directory for the current project
base_dir = r'C:\Users\naren\Desktop\DS\Projects\MLPROJECT\src'

# Define the subdirectories and their corresponding files
subdirectories = {
    'data_ingestion': ['data_ingestion.py'],
    'data_transformation': ['data_transformation.py'],
    'hyperparameter_tuning': ['hyperparameter_tuning.py'],
    'model': ['train_model.py', 'model_evaluation.py', 'feature_importance.py', 'predict.py'],
    'api': ['app.py', 'routes.py'],
    'utils': ['helper_functions.py', 'config.py'],
    'logging': ['logger.py'],
    'exceptions': ['exceptions.py']
}

# Create subdirectories and files
for subdir, files in subdirectories.items():
    subdir_path = os.path.join(base_dir, subdir)
    os.makedirs(subdir_path, exist_ok=True)  # Create subdirectory if it doesn't exist
    for file in files:
        file_path = os.path.join(subdir_path, file)
        with open(file_path, 'w') as f:
            pass  # Create an empty file
