import yfinance as yf
import pandas as pd
from datetime import datetime
from stocks import *
import moving_averages
import sma


bought_stocks = []
sold_stocks = []
time = datetime.now() # Calculates the exact time


for i in list_of_stocks: # Main program
    
    # Gets main data for each stock
    stock = yf.Ticker(i)
    ticker = stock.info['symbol']
    price = stock.fast_info['last_price']
    data = stock.history(period="1y")
    
    # Gets data for moving averages strategy
    data['Short_MA'] = data['Close'].rolling(window=50).mean()  # Calculates the 50-day SMA
    data['Long_MA'] = data['Close'].rolling(window=200).mean() # Calculates the 200-day SMA
    short_ma = data['Short_MA'].iloc[-1]
    long_ma = data['Long_MA'].iloc[-1]
    
    # Runs each strategy
    moving_averages.moving_averages(bought_stocks, sold_stocks, ticker, price, short_ma, long_ma)
    sma.SMA(bought_stocks, sold_stocks, ticker, short_ma, long_ma)
    
print("\n\n", "Buy these stocks: ", bought_stocks, "\n") # Prints the list of bought stocks
print(" Sell these stocks: ", sold_stocks, "\n\n") # Prints the list of sold stocks
print("Run at: ", time) # Prints the time which the programme was run at


'''
next steps:
- main app
    - add more stocks
    - add strategies
    - edit for loop so that it actually gets the data for each stock
    - make sure that this data is relevant for the strategies being implemented
- List of strategies to implement:
    - strategy1
    - strategy2
    - etc.
- test
- make more advanced
    - add oop
    - add data structures
- put together with the django app
    - put data in database and do other jobs relevant for the job
    - during this stage, keep adding strategies etc. in this app
'''