import yfinance as yf
from stocks import *
#import strategy1
#import strategy2
#etc.

for i in list_of_stocks:
    ticker = yf.Ticker(i)
    current_price = ticker.info["regularMarketPrice"]
    high_price = ticker.info["regularMarketDayHigh"]
    low_price = ticker.info["regularMarketDayLow"]
    open_price = ticker.info["regularMarketOpen"]
    close_price = ticker.info["regularMarketPreviousClose"]
    volume = ticker.info["regularMarketVolume"]
    
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