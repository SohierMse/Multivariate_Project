import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data
from utils.preprocessing import clean_data, get_preprocessing_summary

from utils import apply_girly_theme

st.set_page_config(page_title="Preprocessing", page_icon="🧹", layout="wide")


apply_girly_theme()  


df_original = load_data()
df_processed = clean_data(df_original.copy())

st.title("🧹 Data Preprocessing")

st.markdown("""
### 🔧 Preprocessing Steps Applied

Based on the notebook analysis, the following preprocessing steps were performed:
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Before Preprocessing")
    st.write(f"**Shape:** {df_original.shape}")
    st.write(f"**Missing Values:** {df_original.isnull().sum().sum()}")
    st.dataframe(df_original.head(3))

with col2:
    st.subheader("After Preprocessing")
    st.write(f"**Shape:** {df_processed.shape}")
    st.write(f"**Missing Values:** {df_processed.isnull().sum().sum()}")
    st.dataframe(df_processed.head(3))

st.markdown("---")

st.subheader("📋 Preprocessing Steps Detail")

steps = [
    ("1. Remove Constant Columns", "Dropped 'Z_CostContact' and 'Z_Revenue' (constant values, no analytical value)"),
    ("2. Create Age Feature", "Derived 'Age' from 'Year_Birth' (2026 - Year_Birth)"),
    ("3. Filter Invalid Ages", "Removed ages < 18 and > 90 years (data quality)"),
    ("4. Handle Missing Income", "Imputed 24 missing Income values with median (robust to skewness)"),
    ("5. Create Total Spending", "Sum of all product spending (MntWines + MntFruits + ...)"),
    ("6. Create Family Size", "Kidhome + Teenhome + 1 (household structure)"),
    ("7. Clean Marital Status", "Consolidated 'Alone', 'Absurd', 'YOLO' into 'Other'"),
    ("8. Cap Income Outliers", "Capped extreme income at 99th percentile (removed 666,666 outlier)")
]

for step, description in steps:
    with st.expander(step):
        st.write(description)

st.markdown("---")

st.subheader("📊 Missing Values Analysis")
missing_before = df_original.isnull().sum()
missing_after = df_processed.isnull().sum()

missing_df = pd.DataFrame({
    'Column': df_original.columns,
    'Missing Before': missing_before.values,
    'Missing After': [missing_after.get(col, 0) for col in df_original.columns]
})
missing_df = missing_df[missing_df['Missing Before'] > 0]

if len(missing_df) > 0:
    st.dataframe(missing_df)
else:
    st.success("✅ No missing values remaining after preprocessing!")

st.markdown("---")

st.subheader("🔍 New Features Created")

new_features = ['Age', 'Total_Spending', 'Family_Size']
for feature in new_features:
    st.write(f"**{feature}:**")
    st.write(f"  - Mean: {df_processed[feature].mean():.2f}")
    st.write(f"  - Median: {df_processed[feature].median():.2f}")
    st.write(f"  - Range: {df_processed[feature].min():.2f} - {df_processed[feature].max():.2f}")

st.markdown("---")
st.success("✅ Preprocessing complete! Data is ready for analysis.")
