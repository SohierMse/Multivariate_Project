import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data
from utils.clustering import perform_kmeans_clustering, get_cluster_profiles, interpret_clusters
from visuals.clustering_plots import cluster_scatter
from utils import apply_girly_theme

st.set_page_config(page_title="Customer Segmentation", page_icon="🧬", layout="wide")
apply_girly_theme()  
df = load_data()

st.title("🧬 Customer Segmentation")

st.markdown("""
### Key Findings
- **Optimal clusters: K=2** (Premium vs Budget segments)
- **Silhouette score:** 0.33
- **Premium segment:** 1,011 customers (Higher income & spending)
- **Budget segment:** 1,226 customers (Lower income, larger families)
""")

st.markdown("---")

# Features for clustering
features = ['Income', 'Total_Spending', 'Age', 'Family_Size',
            'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'Recency']

# Run clustering
clusters, silhouette, _ = perform_kmeans_clustering(df, features, n_clusters=2)
profiles, sizes = get_cluster_profiles(df, features, clusters)
interpretations = interpret_clusters(profiles)

# Display results
col1, col2 = st.columns(2)
col1.metric("Silhouette Score", f"{silhouette:.3f}")
col2.metric("Total Segments", "2")

st.subheader("Cluster Profiles")
st.dataframe(profiles.style.background_gradient(cmap='RdYlGn'))

st.subheader("Cluster Sizes")
for cluster in sorted(sizes.index):
    st.write(f"**{interpretations[cluster]}:** {sizes[cluster]:,} customers")

# Visualization
df_clustered = df[features].copy()
df_clustered['Cluster'] = clusters
df_clustered['Interpretation'] = df_clustered['Cluster'].map(interpretations)

fig = cluster_scatter(df_clustered, 'Income', 'Total_Spending', 'Interpretation')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("""
**Business Implications:**
- **Premium Segment:** Priority for retention, loyalty programs, premium products
- **Budget Segment:** Value deals, digital touchpoints, family-oriented promotions
""")