import streamlit as st
from utils import apply_girly_theme

st.set_page_config(
    page_title="Team Information",
    page_icon="👥",
    layout="wide"
)

apply_girly_theme()

st.title("👥 Team Information")

st.markdown("""
### 📊 Project Team - Customer Personality Analysis

This project was completed as part of the **Multivariate Statistics & Data Science** course.
""")

st.markdown("---")

# Team Members - As bullet list (NO TABLE)
st.subheader("👨‍💻 Team Members")

st.markdown("""
**Member 1 - Sohier Mohamed Salah Eldin Mohamed** (ID: 23010158)
- **Role:** Data Engineering & Deployment Specialist
- **Key Contributions:** Data Cleaning, Correlation Analysis, Streamlit Dashboard

**Member 2 - Sondos Yasser Mohamed Fahmy Hashem** (ID: 23010132)
- **Role:** Exploratory Analytics & Structure Discovery Specialist
- **Key Contributions:** PCA, Factor Analysis, Mean Vector Analysis

**Member 3 - Rowan Ali Ibrahim Ali** (ID: 23010142)
- **Role:** Statistical Inference Specialist
- **Key Contributions:** Hotelling's T² Tests, Effect Size, Statistical Validation

**Member 4 - Samah Mohamed Saad** (ID: 23011287)
- **Role:** Risk, Outlier & Intelligence Modeling Specialist
- **Key Contributions:** Mahalanobis Distance, Customer Segmentation, Confidence Intervals
""")

st.markdown("---")

# Technologies Used - As bullet list
st.subheader("🛠️ Technologies Used")

st.markdown("""
**Frontend & Visualization**
- Streamlit
- Plotly
- Matplotlib
- Seaborn

**Machine Learning & Statistics**
- Scikit-learn
- SciPy
- FactorAnalyzer
- Statsmodels

**Data Processing**
- Pandas
- NumPy
- Python 3.x
""")

st.markdown("---")

# Course Information
st.subheader("📚 Course Information")

st.markdown("""
- **Course:** Multivariate Statistics & Data Science
- **Project:** Customer Personality Analysis
- **Dataset:** Marketing Campaign Dataset
- **Semester:** Spring 2026
""")

st.markdown("---")

# Resources
st.subheader("🔗 Resources")

st.markdown("""
- **Presentation Link:** [Canva Presentation](https://canva.link/e9qie44ywfz0w6n)
- **Dataset Source:** [Kaggle - Customer Personality Analysis](https://www.kaggle.com/code/amiraadel21000/customer-personality-analysis)
- **Analysis Notebook:** [Google Colab Notebook](https://colab.research.google.com/drive/1DaotVCErZ5nMcBNBUjtiEOD7omnTiraW?usp=sharing)
""")

st.markdown("---")

# Acknowledgments
st.subheader("🙏 Acknowledgments")

st.markdown("""
Special thanks to our course instructors for guidance on multivariate statistical methods including:
- Principal Component Analysis (PCA)
- Factor Analysis with Varimax rotation
- Hotelling's T² tests (one-sample, two-sample)
- Mahalanobis distance for outlier detection
- K-Means and Hierarchical clustering
- Confidence regions and intervals
""")

st.markdown("---")
st.caption("*Project completed as part of academic requirements for Multivariate Statistics course*")