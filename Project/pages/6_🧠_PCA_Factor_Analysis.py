import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data, get_numeric_columns
from utils.analysis import run_pca
from visuals.pca_plots import scree_plot, pca_loadings_heatmap
from utils import apply_girly_theme


st.set_page_config(page_title="PCA & Factor Analysis", page_icon="🧠", layout="wide")

apply_girly_theme()  

df = load_data()
numeric_cols = get_numeric_columns(df)

st.title("🧠 Principal Component Analysis")

st.markdown("""
### Key Findings

| Metric | Value |
|--------|-------|
| **Total Features** | 22 |
| **Components for 90% Variance** | 14 |
| **PC1 Variance Explained** | ~32% |
| **Primary PC1 Drivers** | Meat Products, Wines, Income |
| **Strongest Negative PC1** | Kidhome, NumWebVisitsMonth |
""")

st.markdown("---")

# Select features for PCA (excluding ID)
pca_cols = [col for col in numeric_cols if col not in ['ID']]
selected_pca_cols = st.multiselect(
    "Select features for PCA",
    pca_cols,
    default=pca_cols[:min(15, len(pca_cols))]
)

n_components = st.slider(
    "Number of components to display",
    min_value=2,
    max_value=min(10, len(selected_pca_cols)),
    value=min(5, len(selected_pca_cols))
)

if len(selected_pca_cols) >= 3:
    with st.spinner("Running PCA..."):
        pca, pca_result, loadings, scaler = run_pca(df, selected_pca_cols, n_components)
    
    # Scree Plot
    st.subheader("📉 Scree Plot - Explained Variance")
    fig_scree = scree_plot(pca)
    st.plotly_chart(fig_scree, use_container_width=True)
    
    # Explained variance table
    st.subheader("📊 Explained Variance")
    var_df = pd.DataFrame({
        'Component': [f'PC{i+1}' for i in range(pca.n_components_)],
        'Variance Ratio': pca.explained_variance_ratio_,
        'Cumulative': np.cumsum(pca.explained_variance_ratio_)
    })
    st.dataframe(var_df.style.format({'Variance Ratio': '{:.2%}', 'Cumulative': '{:.2%}'}))
    
    # Loadings Heatmap
    st.subheader("📌 PCA Loadings Matrix")
    fig_loadings = pca_loadings_heatmap(loadings.iloc[:, :n_components])
    st.plotly_chart(fig_loadings, use_container_width=True)
    
    # Feature importance for PC1
    st.subheader("🎯 Feature Importance - PC1 (Loyalty/Spending Axis)")
    pc1_loadings = loadings['PC1'].sort_values(ascending=False)
    
    importance_df = pd.DataFrame({
        'Feature': pc1_loadings.index,
        'Loading': pc1_loadings.values
    })
    st.dataframe(importance_df.style.format({'Loading': '{:.3f}'}))
    
    st.markdown("---")
    st.markdown("""
    ### 📝 PCA Interpretation
    
    **PC1 - "Spending Power & Loyalty":**
    - Positive loadings: Meat Products, Wines, Income, Catalog Purchases
    - Negative loadings: Kidhome, NumWebVisitsMonth
    - Represents customers with high spending vs budget-constrained families
    
    **PC2 - "Demographics":**
    - Captures age and education impacts
    
    **PC3 - "Digital Behavior":**
    - Web visits vs deal purchases
    
    **Global Importance:** Kidhome is the most important feature overall, 
    even more influential than income for segmentation!
    """)

else:
    st.warning("Please select at least 3 features for PCA analysis.")
    