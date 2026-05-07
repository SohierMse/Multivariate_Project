import streamlit as st
from utils.data_loader import load_data
from utils.insights import get_key_insights
from utils import apply_girly_theme


st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

apply_girly_theme()  



# Rest of your page code...

df = load_data()

st.title("🏠 Customer Analytics Dashboard")
st.markdown("## Multivariate Analysis & Customer Intelligence System")

# KPI Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Customers", f"{len(df):,}")

with col2:
    avg_income = df['Income'].mean()
    st.metric("💰 Average Income", f"${avg_income:,.0f}")

with col3:
    avg_spending = df['Total_Spending'].mean()
    st.metric("🛍️ Average Spending", f"${avg_spending:,.0f}")

with col4:
    response_rate = df['Response'].mean() * 100
    st.metric("📧 Campaign Response", f"{response_rate:.1f}%")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎯 Project Overview
    
    This platform provides deep insights into customer behavior using multivariate statistical techniques.
    
    **Key Objectives:**
    - Identify customer segments through clustering
    - Analyze spending patterns and correlations
    - Detect anomalies using Mahalanobis distance
    - Generate actionable business recommendations
    
    **Dataset:** Marketing Campaign (2,237 customers, 29 features)
    """)

with col2:
    st.markdown("### 📊 Key Insights")
    insights = get_key_insights(df)
    for insight in insights:
        st.info(insight)

st.markdown("---")
st.markdown("### 📈 Quick Stats")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Age")
    st.write(f"Min: {df['Age'].min():.0f} | Max: {df['Age'].max():.0f}")
    st.write(f"Mean: {df['Age'].mean():.1f} | Median: {df['Age'].median():.0f}")

with col2:
    st.subheader("Income")
    st.write(f"Min: ${df['Income'].min():,.0f} | Max: ${df['Income'].max():,.0f}")
    st.write(f"Mean: ${df['Income'].mean():,.0f} | Median: ${df['Income'].median():,.0f}")

with col3:
    st.subheader("Spending")
    st.write(f"Min: ${df['Total_Spending'].min():,.0f} | Max: ${df['Total_Spending'].max():,.0f}")
    st.write(f"Mean: ${df['Total_Spending'].mean():,.0f} | Median: ${df['Total_Spending'].median():,.0f}")


    