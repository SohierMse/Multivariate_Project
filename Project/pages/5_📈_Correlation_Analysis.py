import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.data_loader import load_data, get_numeric_columns
from visuals.correlation_plots import correlation_heatmap

from utils import apply_girly_theme

st.set_page_config(page_title="Correlation Analysis", page_icon="📈", layout="wide")

apply_girly_theme()  


df = load_data()
numeric_cols = get_numeric_columns(df)

st.title("📈 Correlation Analysis")

st.markdown("""
### Key Findings from Analysis

| Correlation Pair | Strength | Interpretation |
|-----------------|----------|----------------|
| MntWines ↔ Total_Spending | 0.89 | Wine is the strongest spending driver |
| MntMeatProducts ↔ Total_Spending | 0.84 | Meat is second major driver |
| NumCatalogPurchases ↔ Total_Spending | 0.78 | Catalog users are high spenders |
| Income ↔ Total_Spending | 0.66 | Moderate correlation |
| Kidhome ↔ Family_Size | 0.70 | Expected structural relationship |
""")

st.markdown("---")

# Select columns for correlation
available_cols = [col for col in numeric_cols if col not in ['ID']]
selected_cols = st.multiselect(
    "Select columns for correlation analysis",
    available_cols,
    default=available_cols[:min(10, len(available_cols))]
)

if len(selected_cols) >= 2:
    fig = correlation_heatmap(df, selected_cols)
    st.plotly_chart(fig, use_container_width=True)
    
    # Strongest correlations
    st.subheader("🔍 Strongest Correlations")
    corr_matrix = df[selected_cols].corr()
    
    # Get upper triangle
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    strong_corr = upper.unstack().dropna().sort_values(ascending=False).head(10)
    
    strong_df = pd.DataFrame({
        'Variable 1': [x[0] for x in strong_corr.index],
        'Variable 2': [x[1] for x in strong_corr.index],
        'Correlation': strong_corr.values
    })
    st.dataframe(strong_df.style.format({'Correlation': '{:.3f}'}))

else:
    st.warning("Please select at least 2 columns for correlation analysis.")

st.markdown("---")

st.markdown("""
### 📝 Interpretation Guide

**Strong Correlations (|r| > 0.7):**
- Indicates strong linear relationship
- Variables tend to move together

**Moderate Correlations (0.5 < |r| < 0.7):**
- Meaningful relationship but not deterministic
- Other factors also influence the variables

**Weak Correlations (|r| < 0.3):**
- Little to no linear relationship
- Variables behave independently

**Important Note:** Correlation does not imply causation!
""")
