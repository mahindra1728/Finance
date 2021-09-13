# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:20:05 2021

@author: mahindra.choudhary
"""
cd D:/From_82/Mahendra/My_Scripts/Yahoo_finance

pip install yfinance
pip install plotly

""" 
I. Import package
The first step will consist of importing the necessary packages.
You will start by importing your packages previously installed by using the following lines of code:
""" 


# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

# II. Get connected to the market
# Now that the different packages needed have been uploaded. We are going to use UBER as an example to set up our import through Yahoo Finance API.

# Yahoo Finance API will need 3 mandatory arguments in this order:
# Tickers (1)
# Start date + End date or Period (2)
# Interval (3)

# For our case, the ticker(argument 1) will be UBER. Furthermore, we are going to choose for this example the 5 last days period(argument 2)
# instead of defining a Start and End date. And we will set up an interval(argument 3) of 5 minutes. 
# As a quick reminder, UBER’s ticker is UBER.

# To call your data, you will have to use the following structure:
    
"""
yf.download(tickers = arrument1, period = argument 2, interval = argument 3)

"""
    

# Before to go further, I am going to bring some details on the third argument (interval).

# A quick lookup on interval
# I want to give you a quick shot on the different interval you can set up using yahoo finance API.
# Detailed below the full list of interval possibilities which can be required:

""" 
             Periods                              Arguments  
--------------------------------------------------------------------------------- """
#             1 minute                     |        1m                        |
#             2 minute                     |        2m                        |
#             n minute                     |        nm                        |
#             1 hour                       |        1h                        |
#             2 hour                       |        2h                        |
#             1 day                        |        1d                        |
#             2 days                       |        2d                        |
#             1 week                       |        1wk                       |
#             2 weeks                      |        2wk                       |
#             1 month                      |        1mo                       |

"""
-----------------------------------------------------------------------------------
"""


#################
# Import tickers 
#################

pip install get-all-tickers
from get_all_tickers import get_tickers as gt

list_of_tickers = gt.get_tickers()
# or if you want to save them to a CSV file
get.save_tickers()





#Interval required 5 minutes
data = yf.download(tickers='UBER', period='5d', interval = '1m')
#Print data
data

##############################################################
pfizer = yf.Ticker('PFE')
pfizer.info
old  =  pfizer.history(start="2010-01-01",  end="2020-07-21")
old.head()

# ------------------------------------------------------------

nifty = yf.Ticker('NSEI')

nifty.info

type(data)
data.shape
data.size
data.ndim

# Live test
# At the time when I am executing the line below, we are the 23rd October 2020, and it is actually 5:13 PM in 
# London which means that the market is open.
# For your information: 5:13 PM UK time correspond to 1:13 PM New York time.

# We have defined our 3 arguments, let’s execute the code below:

    
# For a recap, the following line of code is calling Yahoo finance API and 
# requesting to get data for the last 5 days, with an interval of 5 minutes.
# And here is the output:




































































































































































































































