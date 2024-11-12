import time
import yfinance as yf
import pandas as pd
from datetime import datetime
from functions import *
from stocks import *
import SMA
import RSI
import moving_averages
import mean_reversion
import bollinger_bands

# Function to recommend stocks
def recommend(buy_signal, sell_signal, bought_stocks, sold_stocks, list_of_stocks, remove_duplicates, remove_stocks_in_both_lists):
    for i in list_of_stocks: # Main program
        # Gets main data for each stock
        stock = yf.Ticker(i)
        ticker = stock.info['symbol']
        price = stock.fast_info['last_price']
        data = stock.history(period="1y")
        
        # Gets data for moving averages (and mean reversion) strategies
        data['Short_MA'] = data['Close'].rolling(window=50).mean()  # Calculates the 50-day SMA
        data['Long_MA'] = data['Close'].rolling(window=200).mean() # Calculates the 200-day SMA
        short_ma = data['Short_MA'].iloc[-1]
        long_ma = data['Long_MA'].iloc[-1]
        
        # Code to get data for mean reversion strategy
        lower_bound = short_ma * 0.95
        upper_bound = short_ma * 1.05
        
        # Code to calculate the RSI
        delta = data['Close'].diff()
        average_gains = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        average_losses = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        RS_value = average_gains / average_losses
        RSI_value = 100 - (100 / (1 + RS_value))
        
        # Gets the data needed for the bollinger bands strategy
        data['Middle_band'] = data['Close'].rolling(window=20).mean()
        data['Upper_band'] = data['Middle_band'] + (data['Close'].rolling(window=20).std() * 2)
        data['Lower_band'] = data['Middle_band'] - (data['Close'].rolling(window=20).std() * 2)
        upper_band = data['Upper_band'].iloc[-1]
        middle_band = data['Middle_band'].iloc[-1]
        lower_band = data['Lower_band'].iloc[-1]
        
        # Runs each strategy
        moving_averages.moving_averages(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, short_ma, long_ma)
        SMA.SMA(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, short_ma, long_ma)
        #mean_reversion.mean_reversion(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, upper_bound, lower_bound)
        RSI.RSI(buy_signal, sell_signal, data, bought_stocks, sold_stocks, ticker, stock, price, RSI_value)
        bollinger_bands.bollinger_bands(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, upper_band, middle_band, lower_band)
    
    remove_duplicates(bought_stocks)
    remove_duplicates(sold_stocks)

    remove_stocks_in_both_lists(bought_stocks, sold_stocks)
    
    print("\n", "Buy: ", bought_stocks) # Prints the list of bought stocks
    print(" Sell:", sold_stocks, "\n") # Prints the list of sold stocks
    print("Run at: ", time) # Prints the time which the programme was run at