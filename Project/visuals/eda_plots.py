import plotly.express as px
import plotly.graph_objects as go

def age_distribution(df):
    fig = px.histogram(
        df, x='Age', 
        title='📊 Age Distribution',
        color_discrete_sequence=['#9b59b6'],
        nbins=25,
        labels={'Age': 'Customer Age', 'count': 'Number of Customers'}
    )
    fig.update_layout(showlegend=False, height=400)
    return fig

def income_distribution(df):
    fig = px.histogram(
        df, x='Income',
        title='💰 Income Distribution',
        color_discrete_sequence=['#9b59b6'],
        nbins=40,
        labels={'Income': 'Annual Income ($)', 'count': 'Number of Customers'}
    )
    return fig

def spending_distribution(df):
    fig = px.histogram(
        df, x='Total_Spending',
        title='🛍️ Total Spending Distribution',
        color_discrete_sequence=['#9b59b6'],
        nbins=30,
        labels={'Total_Spending': 'Total Spending ($)', 'count': 'Customers'}
    )
    return fig

def marital_status_pie(df):
    marital_counts = df['Marital_Status'].value_counts()
    fig = px.pie(
        values=marital_counts.values, names=marital_counts.index,
        title='💍 Marital Status Distribution',
        hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def education_bar(df):
    edu_counts = df['Education'].value_counts()
    fig = px.bar(
        x=edu_counts.index, y=edu_counts.values,
        title='🎓 Education Level',
        labels={'x': 'Education', 'y': 'Number of Customers'},
        color=edu_counts.values,
        color_continuous_scale='Purples'
    )
    return fig

def spending_by_family_size(df):
    family_spending = df.groupby('Family_Size')['Total_Spending'].mean().reset_index()
    fig = px.bar(
        family_spending, x='Family_Size', y='Total_Spending',
        title='Average Spending by Family Size',
        color='Total_Spending',
        color_continuous_scale='Purples'
    )
    return fig

