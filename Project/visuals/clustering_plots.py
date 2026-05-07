import plotly.express as px
import plotly.graph_objects as go

def cluster_scatter(df, x_col, y_col, cluster_col='Cluster'):
    """2D scatter plot of clusters"""
    fig = px.scatter(
        df, x=x_col, y=y_col,
        color=cluster_col,
        title='🧬 Customer Segments',
        color_continuous_scale='Viridis',
        labels={x_col: x_col.replace('_', ' ').title(), 
                y_col: y_col.replace('_', ' ').title()},
        opacity=0.7
    )
    return fig

def cluster_radar(df_cluster_means, features):
    """Radar chart for cluster profiles"""
    fig = go.Figure()
    
    for cluster in df_cluster_means.index:
        fig.add_trace(go.Scatterpolar(
            r=df_cluster_means.loc[cluster, features].values,
            theta=features,
            fill='toself',
            name=f'Cluster {cluster}'
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title='Cluster Profiles Comparison',
        height=500
    )
    return fig
