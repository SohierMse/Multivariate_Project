import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data
from utils.analysis import calculate_mahalanobis, run_isolation_forest
from visuals.outlier_plots import mahalanobis_plot

from utils import apply_girly_theme


st.set_page_config(page_title="Outlier Detection", page_icon="⚠️", layout="wide")

apply_girly_theme()  

df = load_data()

st.title("⚠️ Outlier Detection")

st.markdown("""
### Key Findings
- **25 outliers detected** (1.12% of customers)
- **Chi² threshold:** 4.93 (99.9% confidence)
- **Two-tier system:** Mahalanobis (extreme) + Isolation Forest (unusual)
""")

st.markdown("---")

# Features for outlier detection
features = ['Income', 'Total_Spending', 'Age', 'Family_Size',
            'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']

# Mahalanobis Distance
st.subheader("Mahalanobis Distance")

distances, threshold = calculate_mahalanobis(df, features)
outliers = distances > threshold

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(df))
col2.metric("Outliers Detected", outliers.sum())
col3.metric("Outlier %", f"{outliers.mean()*100:.2f}%")

fig = mahalanobis_plot(distances, threshold)
st.plotly_chart(fig, use_container_width=True)

# Isolation Forest
st.subheader("Isolation Forest")

predictions, scores = run_isolation_forest(df, features)
iso_outliers = predictions == -1

col1, col2 = st.columns(2)
col1.metric("Isolation Forest Outliers", iso_outliers.sum())
col2.metric("Agreement Rate", f"{(outliers == iso_outliers).mean()*100:.1f}%")

# Show outliers
if outliers.sum() > 0:
    st.subheader("🚨 Outlier Customers")
    outlier_df = df[outliers][['Income', 'Total_Spending', 'Age', 'Family_Size']].copy()
    outlier_df['Mahalanobis_Distance'] = distances[outliers]
    st.dataframe(outlier_df.sort_values('Mahalanobis_Distance', ascending=False))
    