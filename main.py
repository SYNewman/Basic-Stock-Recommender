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