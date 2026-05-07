import plotly.graph_objects as go
import plotly.express as px

def correlation_heatmap(df, numeric_cols):
    """Interactive correlation heatmap"""
    corr_matrix = df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmin=-1, zmax=1,
        text=corr_matrix.round(2),
        texttemplate='%{text}',
        textfont={"size": 10}
    ))
    fig.update_layout(
        title='📈 Correlation Heatmap',
        height=600,
        width=700
    )
    return fig

