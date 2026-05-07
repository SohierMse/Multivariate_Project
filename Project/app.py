import streamlit as st
import pandas as pd
from utils import apply_girly_theme
from utils.data_loader import load_data, get_dataset_info

# Page configuration must be FIRST 
st.set_page_config(
    page_title="Customer Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply girly theme
apply_girly_theme()

# ========== FIX: Make sidebar navigation text dark purple ==========
st.markdown("""
<style>
/* Make the navigation caption text dark purple */
[data-testid="stSidebar"] .stCaption {
    color: #4a2a4a !important;
    font-weight: 500 !important;
    font-size: 14px !important;
}

/* Make all sidebar text dark purple */
[data-testid="stSidebar"] p {
    color: #4a2a4a !important;
}

/* Keep the headers pink */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #c44569 !important;
}

/* Make metric labels dark */
[data-testid="stSidebar"] .stMetricLabel {
    color: #4a2a4a !important;
}

/* Make metric values pink */
[data-testid="stSidebar"] .stMetricValue {
    color: #c44569 !important;
}

/* Make the about text dark */
[data-testid="stSidebar"] .stMarkdown {
    color: #4a2a4a !important;
}
</style>
""", unsafe_allow_html=True)

# Load data
df = load_data()
info = get_dataset_info(df)

# ==================== CLEAN SIDEBAR ====================
with st.sidebar:
    st.markdown("# 🎯 Customer Analytics")
    st.markdown("### Multivariate Intelligence System")
    st.markdown("---")
    
    # Basic dataset stats
    st.markdown("### 📊 Dataset")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Customers", f"{info['rows']:,}")
    with col2:
        st.metric("Features", info['columns'])
    
    st.markdown("---")
    st.markdown("### 🧭 Navigation")
    st.caption("Use the menu above to explore analyses")  # This text will now be dark purple
    st.markdown("---")
    
    # App description
    st.markdown("### ℹ️ About")
    st.caption("Built with Streamlit | Multivariate Statistics")  # This will also be dark purple
    
    st.markdown("---")
    st.caption("📊 Dashboard v1.0")  # This will also be dark purple

# ==================== MAIN CONTENT ====================
st.title("Customer Analytics Dashboard")
st.markdown("## Multivariate Analysis & Customer Intelligence System")

st.markdown("""
This dashboard provides a comprehensive multivariate analysis of customer behavior based on the **Marketing Campaign Dataset**.
""")

st.markdown("---")

# Key Results Table
st.subheader("📊 Key Results from Analysis")

results_data = {
    "Finding": [
        "Optimal Clusters",
        "Outliers Detected", 
        "Hotelling's T² (2-sample)",
        "Standardized Effect Size",
        "PCA Variance"
    ],
    "Result": [
        "K=2 (Premium vs Budget segments)",
        "25 (1.12%) via Mahalanobis",
        "p < 0.001 - Groups differ significantly",
        "0.96 (Large)",
        "90% with 14 components"
    ]
}

results_df = pd.DataFrame(results_data)
st.table(results_df)

st.markdown("---")

# Available Pages Table
st.subheader("📋 Available Pages")

pages_data = {
    "Page": [
        "🏠 Home",
        "📂 Upload Data", 
        "🧹 Preprocessing",
        "📊 EDA Dashboard",
        "📈 Correlation Analysis",
        "🧠 PCA & Factor Analysis",
        "📉 Statistical Testing",
        "⚠️ Outlier Detection",
        "🧬 Customer Segmentation",
        "💡 Business Recommendations",
        "👥 Team Information"
    ],
    "Description": [
        "Project overview and KPIs",
        "Dataset information",
        "Data cleaning steps",
        "Interactive exploratory analysis",
        "Feature relationships",
        "Dimensionality reduction",
        "Hotelling's T² tests",
        "Mahalanobis + Isolation Forest",
        "K-Means (K=2) + Hierarchical",
        "Actionable insights",
        "Project team details"
    ]
}

pages_df = pd.DataFrame(pages_data)
st.dataframe(pages_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("*Customer Analytics Dashboard | Based on Marketing Campaign Dataset*")