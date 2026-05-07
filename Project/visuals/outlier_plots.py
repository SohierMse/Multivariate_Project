import plotly.graph_objects as go

def mahalanobis_plot(distances, threshold):
    """Plot Mahalanobis distances with threshold"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(len(distances))),
        y=distances,
        mode='markers',
        name='Mahalanobis Distance',
        marker=dict(color='#9b59b6', size=6)
    ))
    
    fig.add_hline(y=threshold, line_dash='dash', line_color='red', 
                  annotation_text=f'Threshold = {threshold:.2f}')
    
    fig.update_layout(
        title='⚠️ Mahalanobis Distance - Outlier Detection',
        xaxis_title='Customer Index',
        yaxis_title='Mahalanobis Distance',
        height=450
    )
    return fig
