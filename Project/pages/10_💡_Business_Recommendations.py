import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.insights import generate_recommendations, get_key_insights
from utils.clustering import perform_kmeans_clustering, get_cluster_profiles, interpret_clusters
from utils import apply_girly_theme

st.set_page_config(page_title="Business Recommendations", page_icon="💡", layout="wide")

apply_girly_theme()  
df = load_data()

st.title("💡 Business Recommendations")

st.markdown("""
### 🎯 Data-Driven Strategic Recommendations

Based on the multivariate analysis of customer behavior, here are actionable recommendations:
""")

st.markdown("---")

# Run clustering for recommendations
features = ['Income', 'Total_Spending', 'Age', 'Family_Size',
            'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'Recency']

clusters, _, _ = perform_kmeans_clustering(df, features, n_clusters=2)
profiles, sizes = get_cluster_profiles(df, features, clusters)
interpretations = interpret_clusters(profiles)

# Cluster-based recommendations
st.subheader("📊 Segment-Based Strategies")

for cluster in sorted(profiles.index):
    with st.expander(f"{interpretations[cluster]} ({sizes[cluster]:,} customers)"):
        if cluster == 0:  # Budget segment based on notebook
            st.markdown("""
            **Profile Characteristics:**
            - Lower income (~$37,340)
            - Very low spending (~$146)
            - Larger family size (2.26)
            - Low engagement across all channels
            
            **Recommendations:**
            - 🎯 Target with value deals and family-oriented promotions
            - 📱 Focus on cost-effective digital touchpoints
            - 🛍️ Create bundle offers for larger households
            - 💰 Avoid expensive catalog campaigns (ROI will be low)
            """)
        else:  # Premium segment
            st.markdown("""
            **Profile Characteristics:**
            - Higher income (~$70,281)
            - High spending (~$1,163)
            - Smaller family size (1.57)
            - Heavy catalog and store users
            
            **Recommendations:**
            - ⭐ **Priority #1:** Retain at all costs (highest revenue contributors)
            - 💎 Launch exclusive loyalty program with premium benefits
            - 📖 Maintain catalog investment (this channel works for them)
            - 🍷 Focus premium product promotions (Wine, Meat)
            """)

st.markdown("---")

# Automated recommendations
st.subheader("🤖 Automated Insights")
recommendations_df = generate_recommendations(df)

if len(recommendations_df) > 0:
    for _, rec in recommendations_df.iterrows():
        if rec['priority'] == 'High':
            st.warning(f"### {rec['type']}\n{rec['recommendation']}")
        elif rec['priority'] == 'Medium':
            st.info(f"### {rec['type']}\n{rec['recommendation']}")
        else:
            st.success(f"### {rec['type']}\n{rec['recommendation']}")
else:
    st.info("No automated recommendations at this time.")

st.markdown("---")

# Strategic action plan
st.subheader("📋 Strategic Action Plan")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ⚡ Immediate (Next Week)
    1. Flag 25 outlier customers for manual review
    2. Launch re-engagement campaign for high-income low-spending customers
    3. Adjust catalog budget allocation toward Premium segment
    
    ### 📅 Short-term (Next Month)
    1. Implement segment-specific email campaigns
    2. Test value bundles for Budget segment
    3. Optimize web experience for Mid-Tier customers
    """)

with col2:
    st.markdown("""
    ### 🎯 Medium-term (Quarter)
    1. Develop loyalty program based on cluster behavior
    2. Create predictive model for customer lifetime value
    3. A/B test premium offers on Cluster 1
    
    ### 🚀 Long-term (Year)
    1. Build real-time segmentation system
    2. Automate personalized recommendations
    3. Integrate with CRM for campaign automation
    """)

st.markdown("---")

# Key metrics to monitor
st.subheader("📊 KPIs to Monitor")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Premium Segment Size", f"{sizes[1]:,}" if 1 in sizes else "N/A")
with col2:
    st.metric("Average Spending Gap", f"${profiles.loc[1, 'Total_Spending'] - profiles.loc[0, 'Total_Spending']:.0f}" if 0 in profiles.index and 1 in profiles.index else "N/A")
with col3:
    outlier_count = len(df[df['Income'] > df['Income'].quantile(0.99)])
    st.metric("High-Income Outliers", outlier_count)
with col4:
    st.metric("Campaign Response", f"{df['Response'].mean()*100:.1f}%")

st.markdown("---")
st.success("""
**Conclusion:** The analysis confirms that customers form two distinct segments 
(Premium vs Budget). Implementing differentiated strategies for each segment 
will maximize ROI and improve customer satisfaction.
""")
