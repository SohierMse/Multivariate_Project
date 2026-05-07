import pandas as pd
import streamlit as st
import numpy as np
import os
from pathlib import Path

@st.cache_data
def load_data():
    """Load the marketing campaign dataset with all preprocessing"""
    
    # Try multiple possible file paths
    possible_paths = [
        "data/marketing_campaign.csv",
        "../data/marketing_campaign.csv",
        "./data/marketing_campaign.csv",
        "marketing_campaign.csv",
        "../marketing_campaign.csv",
    ]
    
    df = None
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path, sep="\t")
            break
    
    # If still not found, try to get the directory of the current file
    if df is None:
        current_dir = Path(__file__).parent.parent
        file_path = current_dir / "data" / "marketing_campaign.csv"
        if file_path.exists():
            df = pd.read_csv(file_path, sep="\t")
    
    if df is None:
        st.error("Could not find marketing_campaign.csv file. Please check the file path.")
        return None
    
    # Remove constant columns
    df = df.drop(['Z_CostContact', 'Z_Revenue'], axis=1)
    
    # Fix date format
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], format="%d-%m-%Y")
    
    # Create Age feature
    df["Age"] = 2026 - df["Year_Birth"]
    df = df[(df["Age"] >= 18) & (df["Age"] <= 90)]
    df = df.drop("Year_Birth", axis=1)
    
    # Handle missing Income values (24 nulls) - using median
    df["Income"] = df["Income"].fillna(df["Income"].median())
    
    # Create Total Spending feature
    df["Total_Spending"] = (
        df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
        df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
    )
    
    # Create Family Size feature
    df["Family_Size"] = df["Kidhome"] + df["Teenhome"] + 1
    
    # Fix marital status
    df['Marital_Status'] = df['Marital_Status'].replace(
        ['Alone', 'Absurd', 'YOLO'], 'Other'
    )
    
    # Cap extreme income outlier
    income_cap = df["Income"].quantile(0.99)
    df["Income"] = df["Income"].clip(upper=income_cap)
    
    return df

def get_dataset_info(df):
    """Return dataset information"""
    if df is None:
        return {'rows': 0, 'columns': 0, 'memory': '0 MB', 'missing': 0}
    
    return {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'memory': f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
        'missing': df.isnull().sum().sum()
    }

def get_numeric_columns(df):
    """Get numeric columns excluding ID"""
    if df is None:
        return []
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if 'ID' in numeric_cols:
        numeric_cols.remove('ID')
    return numeric_cols
