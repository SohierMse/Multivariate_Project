import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import RobustScaler
from scipy.spatial.distance import mahalanobis
from scipy.stats import chi2, f
from sklearn.ensemble import IsolationForest
import streamlit as st

@st.cache_resource
def run_pca(df, numeric_cols, n_components=14):
    """Run PCA on numeric columns"""
    scaler = RobustScaler()
    scaled_data = scaler.fit_transform(df[numeric_cols].dropna())
    
    pca = PCA(n_components=min(n_components, len(numeric_cols)))
    pca_result = pca.fit_transform(scaled_data)
    
    loadings = pd.DataFrame(
        pca.components_.T,
        columns=[f'PC{i+1}' for i in range(pca.n_components_)],
        index=numeric_cols
    )
    
    return pca, pca_result, loadings, scaler

def calculate_mahalanobis(df, features):
    """Calculate Mahalanobis distance for outlier detection"""
    data = df[features].values
    mean = np.mean(data, axis=0)
    cov = np.cov(data, rowvar=False)
    inv_cov = np.linalg.pinv(cov)
    
    distances = np.array([mahalanobis(row, mean, inv_cov) for row in data])
    threshold = np.sqrt(chi2.ppf(0.999, df=len(features)))
    
    return distances, threshold

def run_isolation_forest(df, features):
    """Run Isolation Forest for anomaly detection"""
    from sklearn.preprocessing import RobustScaler
    
    X = df[features].values
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    
    iso_forest = IsolationForest(
        n_estimators=200,
        contamination='auto',
        random_state=42
    )
    
    predictions = iso_forest.fit_predict(X_scaled)
    scores = iso_forest.decision_function(X_scaled)
    
    return predictions, scores

def hotelling_t2_one_sample(df, features, mu0):
    """One-sample Hotelling's T² test"""
    X = df[features].values
    mean_vector = np.mean(X, axis=0)
    S = np.cov(X, rowvar=False)
    n, p = X.shape
    
    T2 = n * (mean_vector - mu0).T @ np.linalg.inv(S) @ (mean_vector - mu0)
    F_stat = ((n - p) / (p * (n - 1))) * T2
    p_value = 1 - f.cdf(F_stat, p, n - p)
    
    return {'T2': T2, 'F_stat': F_stat, 'p_value': p_value, 'significant': p_value < 0.05}

def hotelling_t2_two_sample(group1, group2):
    """Two-sample Hotelling's T² test"""
    n1, p = group1.shape
    n2, _ = group2.shape
    
    mean1 = np.mean(group1, axis=0)
    mean2 = np.mean(group2, axis=0)
    
    S1 = np.cov(group1, rowvar=False)
    S2 = np.cov(group2, rowvar=False)
    Sp = ((n1 - 1) * S1 + (n2 - 1) * S2) / (n1 + n2 - 2)
    
    T2 = (n1 * n2) / (n1 + n2) * (mean1 - mean2).T @ np.linalg.pinv(Sp) @ (mean1 - mean2)
    F_stat = ((n1 + n2 - p - 1) / (p * (n1 + n2 - 2))) * T2
    p_value = 1 - f.cdf(F_stat, p, n1 + n2 - p - 1)
    
    return {'T2': T2, 'F_stat': F_stat, 'p_value': p_value, 'significant': p_value < 0.05}
