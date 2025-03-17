import pandas as pd
import os

def load_and_print_data():
    # Construct the path to the file relative to the current script
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'uncleaned', 'students.csv')
import os
import pandas as pd

def load_data(file_path):
    """Load the data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        print("Displaying the first few rows of the dataset:")
        print(data.head())
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

def clean_data(data):
    """Clean the data by removing duplicates and handling missing values."""
    # Remove duplicate rows
    data = data.drop_duplicates()
    print("Duplicates removed.")
    
    # Replace missing values in numerical columns with the median
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        data[col].fillna(data[col].median(), inplace=True)
    
    # Replace missing values in categorical columns with the mode
    for col in data.select_dtypes(include=['object']).columns:
        data[col].fillna(data[col].mode()[0], inplace=True)
    
    print("Missing values handled.")
    return data

def save_data(data, file_path):
    """Save the cleaned data to a CSV file."""
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Save the cleaned data
        data.to_csv(file_path, index=False)
        print(f"Cleaned data saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")

if __name__ == "__main__":
    # File paths
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'uncleaned', 'students.csv')
    cleaned_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned', 'cleaned_students.csv')

    # Load the data
    data = load_data(file_path)
    if data is not None:
        # Clean the data
        cleaned_data = clean_data(data)
        
        # Save the cleaned data
        save_data(cleaned_data, cleaned_file_path)



