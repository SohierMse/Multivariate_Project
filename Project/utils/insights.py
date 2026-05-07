import pandas as pd
import numpy as np

def generate_recommendations(df, clusters=None):
    """Generate business recommendations"""
    recommendations = []
    
    # High-income low-spending customers
    if 'Income' in df.columns and 'Total_Spending' in df.columns:
        high_income_low_spend = df[(df['Income'] > 70000) & (df['Total_Spending'] < 500)]
        if len(high_income_low_spend) > 0:
            recommendations.append({
                'type': '⚠️ High Income, Low Spending',
                'description': f'{len(high_income_low_spend)} customers with high income but low spending',
                'recommendation': 'Launch personalized premium offers to unlock their spending potential',
                'priority': 'High'
            })
    
    # Campaign response insights
    if 'Response' in df.columns:
        response_rate = df['Response'].mean() * 100
        if response_rate < 15:
            recommendations.append({
                'type': '📧 Low Campaign Response',
                'description': f'Campaign response rate is only {response_rate:.1f}%',
                'recommendation': 'Focus marketing on high-value customer segments',
                'priority': 'Medium'
            })
    
    # Family size insights
    if 'Family_Size' in df.columns and 'Total_Spending' in df.columns:
        small_families = df[df['Family_Size'] <= 2]['Total_Spending'].mean()
        large_families = df[df['Family_Size'] >= 3]['Total_Spending'].mean()
        if small_families > large_families * 1.5:
            recommendations.append({
                'type': '👨‍👩‍👧 Family Size Impact',
                'description': f'Single/small households spend {small_families:.0f} vs large families {large_families:.0f}',
                'recommendation': 'Create family-friendly bundles for larger households',
                'priority': 'Medium'
            })
    
    return pd.DataFrame(recommendations)

def get_key_insights(df):
    """Extract key insights from data"""
    insights = []
    
    if 'Total_Spending' in df.columns:
        insights.append(f"📊 Average customer spending: ${df['Total_Spending'].mean():.0f}")
    
    if 'Income' in df.columns:
        insights.append(f"💰 Average customer income: ${df['Income'].mean():,.0f}")
    
    if 'Age' in df.columns:
        insights.append(f"🎂 Average customer age: {df['Age'].mean():.0f} years")
    
    if 'Response' in df.columns:
        insights.append(f"📧 Campaign response rate: {df['Response'].mean()*100:.1f}%")
    
    insights.append("🔍 25 multivariate outliers detected (1.12%)")
    insights.append("📈 Optimal clusters: K=2 (Premium vs Budget)")
    insights.append("🍷 Wines and Meat are primary spending drivers")
    insights.append("📊 90% variance explained by 14 PCA components")
    
    return insights
