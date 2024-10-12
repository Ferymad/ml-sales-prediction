import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

def import_data():
    # Step 1: Import Data
    data_path = 'backend/data/sales_data.csv'
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        return df
    else:
        raise FileNotFoundError("sales_data.csv not found in data directory")

def clean_data(df):
    # Step 2: Data Cleaning
    df.dropna(inplace=True)
    return df

def transform_data(df):
    # Step 3: Data Transformation
    # Encode categorical variables
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col])
    
    # Perform feature engineering as needed
    # (Add your feature engineering code here)
    
    return df

if __name__ == "__main__":
    df = import_data()
    df = clean_data(df)
    df = transform_data(df)
    print(df.head())
