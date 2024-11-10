import yfinance as yf
import pandas as pd
from stocks import *
#import strategy1
#import strategy2
#etc.

for i in list_of_stocks:
    ticker = yf.Ticker(i)
    price = ticker.fast_info['last_price']
    data = ticker.history(period="1y")
    
    # Gets data for moving averages strategy
    data['Short_MA'] = data['Close'].rolling(window=50).mean()  # 50-day SMA
    data['Long_MA'] = data['Close'].rolling(window=200).mean() # 200-day SMA
    short_ma = data['Short_MA'].iloc[-1]
    long_ma = data['Long_MA'].iloc[-1]
    
    print(i, price)
    print(f"50-Day Moving Average (Short): ${short_ma:.2f}")
    print(f"200-Day Moving Average (Long): ${long_ma:.2f}", "\n")
    
    #strategy1.strategy1(current_price, high_price, low_price, open_price, close_price, volume)
    #strategy2.strategy2(current_price, high_price, low_price, open_price, close_price, volume)
    #etc.
    
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