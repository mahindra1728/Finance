# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:11:37 2021

@author: mahindra.choudhary
"""

#############################
# Futures and Options Data
#############################

# If you are looking to get Options chain data then you can refer to the FREE course on Getting Market Data on Quantra.

# NSEpy
# The nsepy package is used to get the stock market data for the futures and options for Indian stocks and indices.

pip install nsepy

from datetime import date
from nsepy import get_history
stock_opt = get_history(symbol="nifty bank",
  start=date(2015, 8, 5),
  end=date(2021, 8, 9),
  # option_type="CE",
  # strike_price=17500,
  # expiry_date=date(2021, 9, 30)
 )
stock_opt.head()


import matplotlib.pyplot as plt
stock_opt.Close.plot(figsize=(10, 5))
# Define the label for the title of the figure
plt.title("Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


################################################
# Stock Market Data Visualization and Analysis
################################################

# After you have the stock market data, the next step is to create trading strategies and analyse the performance. 
# The ease of analysing the performance is the key advantage of the Python.

# We will analyse the cumulative returns, drawdown plot, different ratios such as

# Sharpe ratio,
# Sortino ratio, and
# Calmar ratio.

# I have created a simple buy and hold strategy for illustration purpose with four stocks namely:

# Apple
# Amazon
# Microsoft
# Walmart
# To analyse the performance, you can use the pyfolio tear sheet as shown below.

# Install pyfolio if not already installed, as follows:

!pip install pyfolio

# Define the ticker list
tickers_list = ['AAPL', 'AMZN', 'MSFT', 'WMT']

# Import pandas and create a placeholder for the data
import pandas as pd
data = pd.DataFrame(columns=tickers_list)

# Fetch the data
import yfinance as yf
for ticker in tickers_list:
     data[ticker] = yf.download(ticker, period='5y',)['Adj Close']
        
# Compute the returns of individual stocks and then compute the daily mean returns.
# The mean return is the daily portfolio returns with the above four stocks.
data = data.pct_change().dropna().mean(axis=1)

# Import Pyfolio
import pyfolio as pf

# Get the full tear sheet
pf.create_simple_tear_sheet(data)


# Suggested reads on Data Visualization using Python

# Seaborn for Python Data Visualization
# Plotly Python for an interactive Data Visualization
# Bokeh for Data Visualization in Python
