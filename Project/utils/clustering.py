import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import silhouette_score
import streamlit as st

@st.cache_resource
def perform_kmeans_clustering(df, features, n_clusters=2):
    """Perform KMeans clustering"""
    X = df[features].dropna()
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    
    silhouette = silhouette_score(X_scaled, clusters)
    
    return clusters, silhouette, scaler

@st.cache_resource
def perform_hierarchical_clustering(df, features, n_clusters=2, linkage='complete'):
    """Perform Hierarchical Clustering"""
    X = df[features].dropna()
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    
    hier = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    clusters = hier.fit_predict(X_scaled)
    
    silhouette = silhouette_score(X_scaled, clusters)
    
    return clusters, silhouette, scaler

def get_cluster_profiles(df, features, clusters):
    """Get cluster profiles/means"""
    df_clustered = df[features].copy()
    df_clustered['Cluster'] = clusters
    profiles = df_clustered.groupby('Cluster')[features].mean()
    sizes = df_clustered['Cluster'].value_counts()
    
    return profiles, sizes

def interpret_clusters(profiles):
    """Interpret clusters based on income and spending patterns"""
    interpretations = {}
    
    for idx in profiles.index:
        income = profiles.loc[idx, 'Income'] if 'Income' in profiles.columns else 0
        spending = profiles.loc[idx, 'Total_Spending'] if 'Total_Spending' in profiles.columns else 0
        
        if income > 70000 and spending > 1000:
            interpretations[idx] = "💰 Premium High-Value Customers"
        elif income > 50000 and spending > 500:
            interpretations[idx] = "🛍️ Mid-Tier Active Shoppers"
        elif income < 40000 and spending < 200:
            interpretations[idx] = "👨‍👩‍👧 Budget-Conscious Families"
        else:
            interpretations[idx] = "📊 Standard Customers"
    
    return interpretations