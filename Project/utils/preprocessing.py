import pandas as pd
import numpy as np

def clean_data(df):
    """Clean the dataset"""
    df_clean = df.copy()
    
    # Handle missing values
    df_clean["Income"] = df_clean["Income"].fillna(df_clean["Income"].median())
    
    # Remove unrealistic ages
    df_clean = df_clean[(df_clean["Age"] >= 18) & (df_clean["Age"] <= 90)]
    
    # Cap extreme income outliers
    income_cap = df_clean["Income"].quantile(0.99)
    df_clean["Income"] = df_clean["Income"].clip(upper=income_cap)
    
    return df_clean

def get_preprocessing_summary(df_original, df_processed):
    """Get summary of preprocessing steps"""
    return {
        'original_shape': df_original.shape,
        'processed_shape': df_processed.shape,
        'missing_values_removed': df_original.isnull().sum().sum() - df_processed.isnull().sum().sum(),
        'columns_removed': ['Z_CostContact', 'Z_Revenue', 'Year_Birth'],
        'new_features': ['Age', 'Total_Spending', 'Family_Size']
    }

def apply_log_transformation(df, columns):
    """Apply log transformation to skewed columns"""
    df_log = df.copy()
    for col in columns:
        if col in df_log.columns:
            df_log[col] = np.log1p(df_log[col])
    return df_log
