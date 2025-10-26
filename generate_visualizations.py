"""
Generate Interactive Plotly Visualizations for MultimodalICU

This script creates sample interactive HTML visualizations using Python and Plotly.
These can be embedded in a GitHub Pages site.

Requirements:
    pip install plotly pandas numpy
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)


def generate_timeseries_visualization():
    """Generate an interactive time series visualization of ICU vital signs."""
    
    # Generate sample time series data
    hours = 72
    timestamps = [datetime.now() - timedelta(hours=hours-i) for i in range(hours)]
    
    # Simulate vital signs data
    heart_rate = 70 + np.cumsum(np.random.randn(hours)) + 10 * np.sin(np.arange(hours) * 2 * np.pi / 24)
    blood_pressure_sys = 120 + np.cumsum(np.random.randn(hours) * 0.5)
    spo2 = 95 + np.random.randn(hours) * 2
    spo2 = np.clip(spo2, 90, 100)  # Keep realistic range
    
    # Create figure with secondary y-axis
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=heart_rate,
        name='Heart Rate (bpm)',
        mode='lines',
        line=dict(color='#FF6B6B', width=2),
        hovertemplate='<b>Heart Rate</b><br>%{y:.1f} bpm<br>%{x}<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=blood_pressure_sys,
        name='Systolic BP (mmHg)',
        mode='lines',
        line=dict(color='#4ECDC4', width=2),
        hovertemplate='<b>Systolic BP</b><br>%{y:.1f} mmHg<br>%{x}<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=spo2,
        name='SpO2 (%)',
        mode='lines',
        line=dict(color='#95E1D3', width=2),
        hovertemplate='<b>SpO2</b><br>%{y:.1f}%<br>%{x}<extra></extra>'
    ))
    
    fig.update_layout(
        title='ICU Patient Vital Signs - Time Series Analysis',
        xaxis_title='Time',
        yaxis_title='Value',
        hovermode='x unified',
        template='plotly_white',
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Save as standalone HTML
    fig.write_html('visualizations/timeseries.html', include_plotlyjs='cdn')
    print("✓ Generated timeseries.html")


def generate_demographics_visualization():
    """Generate an interactive demographics visualization."""
    
    # Generate sample demographic data
    age_groups = ['18-30', '31-45', '46-60', '61-75', '76+']
    outcomes = ['Discharged', 'Transferred', 'ICU Stay']
    
    data = []
    for age in age_groups:
        for outcome in outcomes:
            count = np.random.randint(10, 100)
            data.append({'Age Group': age, 'Outcome': outcome, 'Count': count})
    
    df = pd.DataFrame(data)
    
    # Create stacked bar chart
    fig = px.bar(df, 
                 x='Age Group', 
                 y='Count', 
                 color='Outcome',
                 title='Patient Demographics and Outcomes',
                 labels={'Count': 'Number of Patients'},
                 color_discrete_sequence=['#667eea', '#764ba2', '#f093fb'],
                 barmode='group')
    
    fig.update_layout(
        template='plotly_white',
        height=600,
        hovermode='x unified',
        legend=dict(
            title='Outcome',
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )
    
    fig.update_traces(hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>')
    
    # Save as standalone HTML
    fig.write_html('visualizations/demographics.html', include_plotlyjs='cdn')
    print("✓ Generated demographics.html")


def generate_correlation_visualization():
    """Generate an interactive correlation matrix heatmap."""
    
    # Generate sample clinical variables
    variables = ['Heart Rate', 'Blood Pressure', 'SpO2', 'Temperature', 
                 'Respiratory Rate', 'GCS Score', 'SOFA Score', 'WBC Count']
    
    # Generate random correlation matrix
    n_vars = len(variables)
    correlation_matrix = np.random.randn(n_vars, n_vars)
    correlation_matrix = (correlation_matrix + correlation_matrix.T) / 2  # Make symmetric
    np.fill_diagonal(correlation_matrix, 1)  # Diagonal is 1
    
    # Normalize to [-1, 1]
    correlation_matrix = correlation_matrix / np.max(np.abs(correlation_matrix))
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix,
        x=variables,
        y=variables,
        colorscale='RdBu',
        zmid=0,
        text=np.round(correlation_matrix, 2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation"),
        hovertemplate='<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z:.3f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Clinical Variables Correlation Matrix',
        xaxis_title='',
        yaxis_title='',
        template='plotly_white',
        height=700,
        width=800,
        xaxis={'side': 'bottom'},
        yaxis={'autorange': 'reversed'}
    )
    
    fig.update_xaxes(tickangle=-45)
    
    # Save as standalone HTML
    fig.write_html('visualizations/correlation.html', include_plotlyjs='cdn')
    print("✓ Generated correlation.html")


def main():
    """Generate all visualizations."""
    print("Generating interactive Plotly visualizations...")
    print("-" * 50)
    
    generate_timeseries_visualization()
    generate_demographics_visualization()
    generate_correlation_visualization()
    
    print("-" * 50)
    print("All visualizations generated successfully!")
    print("\nTo view the visualizations:")
    print("1. Open index.html in a web browser")
    print("2. Or deploy to GitHub Pages")


if __name__ == "__main__":
    main()
