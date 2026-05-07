import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from visuals.eda_plots import (
    age_distribution, income_distribution, spending_distribution,
    marital_status_pie, education_bar, spending_by_family_size
)
from utils import apply_girly_theme


st.set_page_config(page_title="EDA Dashboard", page_icon="📊", layout="wide")

apply_girly_theme()  

df = load_data()

st.title("📊 Exploratory Data Analysis Dashboard")

st.markdown("""
### Interactive Visualizations
Explore customer demographics, spending patterns, and behavioral distributions.
""")

st.markdown("---")

# Filters in sidebar
st.sidebar.subheader("🔍 Filters")
education_filter = st.sidebar.multiselect(
    "Education Level",
    df['Education'].unique(),
    default=df['Education'].unique()
)

marital_filter = st.sidebar.multiselect(
    "Marital Status",
    df['Marital_Status'].unique(),
    default=df['Marital_Status'].unique()
)

# Apply filters
filtered_df = df[
    df['Education'].isin(education_filter) & 
    df['Marital_Status'].isin(marital_filter)
]

st.write(f"**Showing {len(filtered_df):,} customers** (out of {len(df):,})")

st.markdown("---")

# Row 1: Distributions
col1, col2 = st.columns(2)

with col1:
    fig_age = age_distribution(filtered_df)
    st.plotly_chart(fig_age, use_container_width=True)
    
    fig_spending = spending_distribution(filtered_df)
    st.plotly_chart(fig_spending, use_container_width=True)

with col2:
    fig_income = income_distribution(filtered_df)
    st.plotly_chart(fig_income, use_container_width=True)
    
    fig_marital = marital_status_pie(filtered_df)
    st.plotly_chart(fig_marital, use_container_width=True)

# Row 2
col1, col2 = st.columns(2)

with col1:
    fig_edu = education_bar(filtered_df)
    st.plotly_chart(fig_edu, use_container_width=True)

with col2:
    fig_family = spending_by_family_size(filtered_df)
    st.plotly_chart(fig_family, use_container_width=True)

st.markdown("---")

# Summary Statistics
st.subheader("📊 Summary Statistics by Category")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**By Education Level**")
    edu_stats = filtered_df.groupby('Education')['Total_Spending'].agg(['mean', 'median', 'count']).round(2)
    st.dataframe(edu_stats)

with col2:
    st.markdown("**By Marital Status**")
    marital_stats = filtered_df.groupby('Marital_Status')['Total_Spending'].agg(['mean', 'median', 'count']).round(2)
    st.dataframe(marital_stats)

st.markdown("---")
st.info("""
**Key Insights from EDA:**
- Customer age is primarily 45-75 years (bimodal distribution)
- Income is right-skewed with most customers earning $30k-70k
- Spending is highly skewed - most customers spend < $500
- Single-person households spend the most (~$1,100)
- Presence of children significantly reduces spending
""")
