import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Define paths
cleaned_file_path = os.path.join('data', 'cleaned', 'cleaned_students.csv')
train_file_path = os.path.join('data', 'cleaned', 'train.csv')
test_file_path = os.path.join('data', 'cleaned', 'test.csv')

# Ensure the directory exists
os.makedirs(os.path.dirname(train_file_path), exist_ok=True)

try:
    # Load the cleaned data
    data = pd.read_csv(cleaned_file_path)

    # Split the data into train and test sets
    train, test = train_test_split(data, test_size=0.2, random_state=42)

    # Save the train and test sets
    train.to_csv(train_file_path, index=False)
    test.to_csv(test_file_path, index=False)

    print(f"Train and test datasets created successfully:")
    print(f"Train: {train_file_path}")
    print(f"Test: {test_file_path}")
except FileNotFoundError:
    print(f"File not found: {cleaned_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

