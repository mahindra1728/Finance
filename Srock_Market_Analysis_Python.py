# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:00:23 2021

@author: mahindra.choudhary
"""
###########################################
# Stock Market Data And Analysis In Python
###########################################



# Are you looking to get stock market data and analyse the historical data in Python? You have come to right place.

# After reading this, you will be able to:

# Get historical data for stocks
# Plot the stock market data and analyse the performance
# Get the fundamental, futures and options data

# How to get Stock Market Data in Python?
# Yahoo Finance
# One of the first sources from which you can get historical daily price-volume stock market data is Yahoo finance. 
# You can use pandas_datareader or yfinance module to get the data and then can download or store in a csv file by using pandas.to_csv method.

# If yfinance is not installed on your computer, then run the below line of code from your Jupyter Notebook to install yfinance

!pip install yfinance


# Import yfinance package
import yfinance as yf

# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Set the ticker
ticker = 'AMZN'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()
data.head()


# To visualize the adjusted close price data, you can use the matplotlib library and plot method as shown below.

# Import matplotlib for plotting
import matplotlib.pyplot as plt
%matplotlib inline

# Plot adjusted close price data
data['Adj Close'].plot()
plt.show()

# Let us improve the plot by resizing, giving appropriate labels and adding grid lines for better readability.

# Plot the adjusted close price
data['Adj Close'].plot(figsize=(10, 7))

# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()



###########################################################
# How to get Stock Market Data for different geographies?
###########################################################

# To get stock market data for different geographies, search the ticker symbol on Yahoo finance and use that as the ticker

# Get stock market data for multiple tickers

# To get the stock market data of multiple stock tickers, you can create a list of tickers and call the yfinance download method for 
# each stock ticker.

# For simplicity, I have created a dataframe data to store the adjusted close price of the stocks.


# Import packages
import yfinance as yf
import pandas as pd

# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Define the ticker list
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)

# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker, 
                               start_date,
                               end_date)['Adj Close']
    
# Print first 5 rows of the data
data.head()

############################
# Plot all the close prices
###########################

data.plot(figsize=(10, 7))

# Show the legend
plt.legend()

# Define the label for the title of the figure
plt.title("Adjusted Close Price", fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()



########################
# S&P 500 Stock Tickers
########################

# If you want to analyse the stock market data for all the stocks which make up S&P 500 then below code will help you. 
# It gets the list of stocks from the wikipedia page and then fetches the stock market data from yahoo finance.

# Import packages
import yfinance as yf
import pandas as pd

# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(tickers.head())

# Get the data for this tickers from yahoo finance
data = yf.download(tickers.Symbol.to_list(),'2021-1-1','2021-7-12', auto_adjust=True)['Close']
print(data.head())


##########################################
# Intraday or Minute Frequency Stock Data
##########################################

# yfinance module can be used to fetch the minute level stock market data. It returns the stock market data for the last 7 days.

# If yfinance is not installed on your computer, then run the below line of code from your Jupyter Notebook to install yfinance.


# The yfinance module has the download method which can be used to download the stock market data.

# It takes the following parameters:

# ticker: The name of the tickers you want the stock market data for. If you want stock market data for multiple tickers then separate 
# them by space
# period: The number of days/month of stock market data required. The valid frequencies are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
# interval: The frequency of the stock market data. The valid intervals are 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

import yfinance as yf
intraday_data = yf.download(tickers="MSFT",
                            period="5d",
                            interval="1m",
                            auto_adjust=True)
intraday_data.head()


# Resample Stock Data
# Convert 1-minute data to 1-hour data or Resample Stock Data

# During strategy modelling, you might be required to work with a custom frequency of stock market data such as 15 minutes or 1 hour or 
# even 1 month.

# If you have minute level data, then you can easily construct the 15 minutes, 1 hour or daily candles by resampling them. 
# Thus, you don't have to buy them separately.

# In this case, you can use the pandas resample method to convert the stock market data to the frequency of your choice. 
# The implementation of these is shown below where a 1-minute frequency data is converted to 10-minute frequency data.

# The first step is to define the dictionary with the conversion logic. For example, to get the open value the first value will be used, 
# to get the high value the maximum value will be used and so on.

# The name Open, High, Low, Close and Volume should match the column names in your dataframe.

ohlcv_dict = {
 'Open': 'first',
 'High': 'max',
 'Low': 'min',
 'Close': 'last',
 'Volume': 'sum'
}

# Convert the index to datetime timestamp as by default string is returned. Then call the resample method with the frequency such as:

# 10T for 10 minutes,
# D for 1 day and
# M for 1 month

# Import package & get the data
import yfinance as yf
intraday_data = yf.download(tickers="MSFT",
                            period="5d",
                            interval="1m",
                            auto_adjust=True)

# Define the resampling logic
ohlcv_dict = {
     'Open': 'first',
     'High': 'max',
     'Low': 'min',
     'Close': 'last',
     'Volume': 'sum'
}

# Resample the data
intraday_data_10 = intraday_data.resample('10T').agg(ohlcv_dict)
intraday_data_10.head()

# Yahoo finance has limited set of minute level data. if you need the stock market data for higher range then you can get the data from 
# data vendors such as Quandl, AlgoSeek or your broker.

# Using Quandl to get Stock Market Data (Optional)

# Quandl has many data sources to get different types of stock market data. However, some are free and some are paid. 
# Wiki is the free data source of Quandl to get the data of the end of the day prices of 3000+ US equities. 
# It is curated by Quandl community and also provides information about the dividends and split.

# Quandl also provides paid data source of minute and lower frequencies.

# To get the stock market data, you need to first install the quandl module if it is not already installed using the pip command as shown below.


!pip install quandl

# You need to get your own API Key from quandl to get the stock market data using the below code. If you are facing issue in getting the API key
 # then you can refer to this link.

# After you get your key, assign the variable QUANDL_API_KEY with that key. Then set the start date, end date and the ticker of the asset whose 
# stock market data you want to fetch.

# The quandl get method takes this stock market data as input and returns the open, high, low, close, volume, adjusted values and other information.

########################
# Import quandl package
########################
import quandl

# To get your API key, sign up for a free Quandl account.
# Then, you can find your API key on Quandl account settings page.
QUANDL_API_KEY = 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY'

# This is to prompt you to change the Quandl Key
if QUANDL_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
    raise Exception("Please provide a valid Quandl API key!")
 
# Set the start and end date
start_date = '1990-01-01'
end_date = '2018-03-01'

# Set the ticker name
ticker = 'AMZN'

# Feth the data
data = quandl.get('WIKI/'+ticker, 
                  start_date=start_date, 
                  end_date=end_date, 
                  api_key=QUANDL_API_KEY)

# Print the first 5 rows of the dataframe
data.head()

####################
# Fundamental Data
####################

# We have used yfinance to get the fundamental data.

# The first step is to set the ticker and then call the appropriate properties to get the right stock market data.

# If yfinance is not installed on your computer, then run the below line of code from your Jupyter Notebook to install yfinance.

!pip install yfinance

# Import yfinance
import yfinance as yf

# Set the ticker as MSFT
msft = yf.Ticker("MSFT")

# Key Ratios
###############
# You can fetch the latest price to book ratio and price to earnings ratio as shown below.

# get price to book
pb = msft.info['priceToBook']
pe = msft.info['regularMarketPrice']/msft.info['epsTrailingTwelveMonths']
print('Price to Book Ratio is: %.2f' % pb)
print('Price to Earnings Ratio is: %.2f' % pe)

# Revenues
###########
# show revenues

revenue = msft.financials.loc['Total Revenue']
plt.bar(revenue.index, revenue.values)
plt.ylabel("Total Revenues")
plt.show()


# Earnings Before Interest and Taxes (EBIT)
############################################

EBIT = msft.financials.loc['Earnings Before Interest and Taxes']
plt.bar(EBIT.index, EBIT.values)
plt.ylabel("EBIT")
plt.show()


# Balance sheet, cash flows and other information
##################################################

# show income statement
msft.financials
# show balance heet
msft.balance_sheet
# show cashflow
msft.cashflow
# show other info
msft.info















