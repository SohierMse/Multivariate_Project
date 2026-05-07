import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data, get_numeric_columns
from utils.analysis import hotelling_t2_one_sample, hotelling_t2_two_sample

from utils import apply_girly_theme

st.set_page_config(page_title="Statistical Testing", page_icon="📉", layout="wide")
apply_girly_theme()  

df = load_data()
numeric_cols = get_numeric_columns(df)

st.title("📉 Statistical Testing - Hotelling's T²")

st.markdown("""
### 🎯 Hotelling's T² Test

The multivariate extension of the t-test for comparing group means.

**Key Findings:**
- One-Sample: Customer profile differs from benchmark (p < 0.001)
- Two-Sample: Responders vs Non-responders differ significantly (p < 0.001)
- Effect Size: 0.96 (Large)
""")

st.markdown("---")

tab1, tab2 = st.tabs(["📊 One-Sample Test", "🔄 Two-Sample Test"])

# Tab 1: One-Sample Test
with tab1:
    st.subheader("One-Sample Hotelling's T² Test")
    
    features_one = st.multiselect(
        "Select features",
        ['Income', 'Total_Spending', 'Age', 'Family_Size'],
        default=['Income', 'Total_Spending', 'Age', 'Family_Size']
    )
    
    if len(features_one) >= 2:
        st.subheader("Benchmark Values")
        cols = st.columns(len(features_one))
        mu0 = []
        defaults = {'Income': 50000, 'Total_Spending': 600, 'Age': 55, 'Family_Size': 2}
        
        for i, feat in enumerate(features_one):
            with cols[i]:
                val = st.number_input(f"Benchmark {feat}", value=float(defaults.get(feat, 0)))
                mu0.append(val)
        
        if st.button("Run One-Sample Test"):
            result = hotelling_t2_one_sample(df, features_one, np.array(mu0))
            
            col1, col2, col3 = st.columns(3)
            col1.metric("T²", f"{result['T2']:.2f}")
            col2.metric("F", f"{result['F_stat']:.2f}")
            col3.metric("P-Value", f"{result['p_value']:.2e}")
            
            if result['significant']:
                st.error("❌ Reject H₀ - Customer profile differs from benchmark")
            else:
                st.success("✅ Fail to reject H₀ - No significant difference")

# Tab 2: Two-Sample Test
with tab2:
    st.subheader("Two-Sample Hotelling's T² Test")
    
    group_col = st.selectbox("Grouping variable", ['Response', 'Complain', 'Marital_Status'])
    features_two = st.multiselect("Select features", numeric_cols, default=['Income', 'Total_Spending', 'Age', 'Family_Size'])
    
    if len(features_two) >= 2 and group_col:
        unique_vals = df[group_col].dropna().unique()
        
        if len(unique_vals) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                g1 = st.selectbox("Group 1", unique_vals, index=0)
            with col2:
                g2 = st.selectbox("Group 2", unique_vals, index=min(1, len(unique_vals)-1))
            
            group1 = df[df[group_col] == g1][features_two].dropna().values
            group2 = df[df[group_col] == g2][features_two].dropna().values
            
            st.write(f"Group 1 ({g1}): {len(group1)} customers")
            st.write(f"Group 2 ({g2}): {len(group2)} customers")
            
            if st.button("Run Two-Sample Test"):
                result = hotelling_t2_two_sample(group1, group2)
                
                col1, col2, col3 = st.columns(3)
                col1.metric("T²", f"{result['T2']:.2f}")
                col2.metric("F", f"{result['F_stat']:.2f}")
                col3.metric("P-Value", f"{result['p_value']:.2e}")
                
                if result['significant']:
                    st.error(f"❌ Groups '{g1}' and '{g2}' are significantly different")
                else:
                    st.success(f"✅ No significant difference between groups")

st.markdown("---")
st.markdown("### 📊 Summary")
st.info("""
**Conclusion:** Strong evidence for customer segmentation. Groups differ meaningfully 
across multiple dimensions, justifying targeted marketing strategies.
""")
