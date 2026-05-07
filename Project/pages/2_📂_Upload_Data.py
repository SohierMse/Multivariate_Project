import streamlit as st
import pandas as pd
from utils.data_loader import load_data, get_dataset_info

from utils import apply_girly_theme

st.set_page_config(page_title="Upload Data", page_icon="📂", layout="wide")

apply_girly_theme()  


df = load_data()
info = get_dataset_info(df)

st.title("📂 Dataset Information")

st.info("📌 This dashboard uses the **Marketing Campaign Dataset** (fixed dataset for analysis)")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(10))

with col2:
    st.subheader("ℹ️ Dataset Info")
    st.write(f"**Rows:** {info['rows']:,}")
    st.write(f"**Columns:** {info['columns']}")
    st.write(f"**Memory:** {info['memory']}")
    st.write(f"**Missing Values:** {info['missing']}")

st.markdown("---")

st.subheader("🔍 Column Types")
dtype_df = pd.DataFrame({
    'Column': df.columns,
    'Type': df.dtypes.astype(str),
    'Non-Null': df.count().values,
    'Null %': (df.isnull().sum() / len(df) * 100).round(2).values
})
st.dataframe(dtype_df)

st.markdown("---")

st.subheader("📊 Basic Statistics")
st.dataframe(df.describe())

st.markdown("---")

st.subheader("📈 Data Quality Report")
col1, col2, col3 = st.columns(3)

with col1:
    complete_rows = (df.notnull().all(axis=1)).sum()
    st.metric("Complete Rows", f"{complete_rows} ({complete_rows/len(df)*100:.1f}%)")

with col2:
    duplicate_rows = df.duplicated().sum()
    st.metric("Duplicate Rows", duplicate_rows)

with col3:
    unique_ids = df['ID'].nunique() if 'ID' in df.columns else len(df)
    st.metric("Unique Customers", unique_ids)
    