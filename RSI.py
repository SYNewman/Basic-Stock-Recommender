# This code runs the logic for the RSI strategy

import yfinance as yf
import pandas as pd

def RSI(data,bought_stocks, sold_stocks, ticker, stock, price):
    # Code to calculate the RSI
    delta = data['Close'].diff()
    average_gains = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    average_losses = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    RS = average_gains / average_losses
    RSI = 100 - (100 / (1 + RS))
    print(RSI)
    
    # Generates buy/sell signal
    if RSI > 70:
        print(f"BUY   {ticker}   (RSI)")
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)
    elif RSI < 30:
        print(f"SELL  {ticker}   (RSI)")
        sold_stocks.append(ticker)
        if ticker in bought_stocks:
            bought_stocks.remove(ticker)