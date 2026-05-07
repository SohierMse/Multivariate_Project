# utils/__init__.py
import streamlit as st

# Import all utility functions
from .data_loader import load_data, get_dataset_info, get_numeric_columns
from .preprocessing import clean_data, get_preprocessing_summary, apply_log_transformation
from .analysis import run_pca, calculate_mahalanobis, hotelling_t2_one_sample, hotelling_t2_two_sample, run_isolation_forest
from .clustering import perform_kmeans_clustering, perform_hierarchical_clustering, get_cluster_profiles, interpret_clusters
from .insights import generate_recommendations, get_key_insights

def apply_girly_theme():
    """Apply girly theme to all pages (no animations)"""
    try:
        with open("assets/style.css", "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # If CSS file doesn't exist, don't crash
        pass

def apply_global_style():
    """Alias for apply_girly_theme()"""
    apply_girly_theme()
    