TARGET_COLUMN: str = 'Churn'
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
MODEL_FILENAME: str = 'churn_prediction_model_v1.joblib'
LOG_FILENAME: str = 'churn_model_run_log.json'
MODEL_STORE_DIR: str = 'model_store'
DATA_DIR_NAME: str = 'data'
RAW_DATA_DIR_NAME: str = 'raw'
DATASET_FILENAME = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'