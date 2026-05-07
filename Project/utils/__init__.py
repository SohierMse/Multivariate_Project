# utils/__init__.py
import streamlit as st
import os
from pathlib import Path

# Import all utility functions
from .data_loader import load_data, get_dataset_info, get_numeric_columns
from .preprocessing import clean_data, get_preprocessing_summary, apply_log_transformation
from .analysis import run_pca, calculate_mahalanobis, hotelling_t2_one_sample, hotelling_t2_two_sample, run_isolation_forest
from .clustering import perform_kmeans_clustering, perform_hierarchical_clustering, get_cluster_profiles, interpret_clusters
from .insights import generate_recommendations, get_key_insights

def apply_girly_theme():
    """Apply girly theme to all pages (no animations)"""
    try:
        # Try multiple possible paths for the CSS file
        possible_paths = [
            "assets/style.css",
            "../assets/style.css",
            "./assets/style.css",
            "Project/assets/style.css",
            "/mount/src/multivariate_project/Project/assets/style.css",
        ]
        
        css_content = None
        for path in possible_paths:
            if os.path.exists(path):
                with open(path, "r") as f:
                    css_content = f.read()
                break
        
        # If still not found, try using Path
        if css_content is None:
            current_dir = Path(__file__).parent.parent
            css_path = current_dir / "assets" / "style.css"
            if css_path.exists():
                with open(css_path, "r") as f:
                    css_content = f.read()
        
        if css_content:
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
        else:
            # Fallback to inline CSS if file not found
            st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #ffe9f4 0%, #ffe0f0 50%, #ffd6ea 100%);
            }
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #f5e6f3 0%, #fce4ec 100%);
            }
            h1, h2, h3 {
                color: #c44569 !important;
            }
            </style>
            """, unsafe_allow_html=True)
    except Exception as e:
        # Fallback to inline CSS
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #ffe9f4 0%, #ffe0f0 50%, #ffd6ea 100%);
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f5e6f3 0%, #fce4ec 100%);
        }
        h1, h2, h3 {
            color: #c44569 !important;
        }
        p, li {
            color: #4a2a4a !important;
        }
        </style>
        """, unsafe_allow_html=True)

def apply_global_style():
    """Alias for apply_girly_theme()"""
    apply_girly_theme()
