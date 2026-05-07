import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def scree_plot(pca_model):
    """Scree plot from fitted PCA"""
    explained_variance = pca_model.explained_variance_ratio_
    cumulative = np.cumsum(explained_variance)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[f'PC{i+1}' for i in range(len(explained_variance))],
        y=explained_variance,
        name='Individual',
        marker_color='#9b59b6'
    ))
    fig.add_trace(go.Scatter(
        x=[f'PC{i+1}' for i in range(len(explained_variance))],
        y=cumulative,
        name='Cumulative',
        marker_color='#e74c3c',
        mode='lines+markers',
        yaxis='y2'
    ))
    fig.update_layout(
        title='📉 Scree Plot - Explained Variance',
        xaxis_title='Principal Components',
        yaxis_title='Individual Variance',
        yaxis2=dict(title='Cumulative Variance', overlaying='y', side='right'),
        height=500
    )
    return fig

def pca_loadings_heatmap(loadings_df):
    """Factor loadings heatmap"""
    fig = px.imshow(
        loadings_df,
        title='🧠 PCA Loadings Matrix',
        color_continuous_scale='RdBu',
        aspect='auto',
        text_auto='.2f'
    )
    fig.update_layout(height=500)
    return fig
