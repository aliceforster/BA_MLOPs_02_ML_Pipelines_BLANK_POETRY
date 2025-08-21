"""
config.py 
 
This script stores configuration variables and constants used across the ML project.
It includes definitions for column names, test sizes, random states, and file names
for models and logs, and paths to datasets.
"""
import os

 
# Define column structure based on the churn dataset
TARGET_COLUMN: str = 'Churn'  # Target variable
NUMERIC_COLUMNS: list[str] = ['tenure', 'MonthlyCharges', 'TotalCharges']
CATEGORICAL_COLUMNS: list[str] = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod'
]
 
 
TEST_SIZE: float = 0.25
RANDOM_STATE: int = 42
 
# Define file and directory names
MODEL_FILENAME: str = "churn_prediction_model_v1.joblib"
LOG_FILENAME: str = "churn_model_run_log.json"
MODEL_STORE_DIR: str = "model_store"
 
# Define data paths (relative to the project root, assuming config.py is in src/)
DATA_DIR_NAME: str = "data"
RAW_DATA_DIR_NAME: str = "raw"
DATASET_FILENAME: str = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
 