"""
analysis.py

This script loads and displays basic information about the Nifty 50 closing price dataset.

Functionality:
- Dynamically constructs the file path to the dataset
- Loads the CSV into a Pandas DataFrame
- Prints the first few rows of the dataset for quick inspection

Intended for:
- Exploratory data analysis
- Data validation and initial inspection
"""

import os
import pandas as pd
import plotly.graph_objs as go

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "data", "nifty50_closing_prices.csv")

df = pd.read_csv(csv_path)
print(df.head())

# Convert the date column into a datetime data type
df['Date'] = pd.to_datetime(df['Date'])

# Evaluate null values in the dataframe
print(df.isnull().sum())

# Fill null values
df.fillna(method='ffill', inplace=True)

# Create the stock price trends plot
fig = go.Figure()

for company in df.columns[1:]:
    fig.add_trace(go.Scatter(x=df['Date'], y=df[company],
                             mode='lines',
                             name=company,
                             opacity=0.5))

fig.update_layout(
    title='Stock Price Trends of All Indian Companies',
    xaxis_title='Date',
    yaxis_title='Closing Price (INR)',
    xaxis=dict(tickangle=45),
    legend=dict(
        x=1.05,
        y=1,
        traceorder="normal",
        font=dict(size=10),
        orientation="v"
    ),
    margin=dict(l=0, r=0, t=30, b=0),
    hovermode='x',
    template='plotly_white'
)

fig.show()
