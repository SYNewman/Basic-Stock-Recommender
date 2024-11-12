from datetime import datetime
from functions import *
import stock_recommender
from stocks import *

bought_stocks = []
sold_stocks = []
time = datetime.now() # Calculates the exact time

def buy_signal(bought_stocks, sold_stocks, ticker, strategy): # Function to generate buy signals
    print(f"BUY   {ticker}   {strategy}")
    bought_stocks.append(ticker)
    if ticker in sold_stocks:
        sold_stocks.remove(ticker)

def sell_signal(bought_stocks, sold_stocks, ticker, strategy): # Function to generate sell signals
    print(f"SELL  {ticker}   {strategy}")
    sold_stocks.append(ticker)
    if ticker in bought_stocks:
        bought_stocks.remove(ticker)
        
stock_recommender.recommend(
    buy_signal, sell_signal, bought_stocks, sold_stocks, list_of_stocks,
    remove_duplicates, remove_stocks_in_both_lists)

# next steps:
# - add more stocks
# - add oop
# - add data structures (2/3)
# - make trading algorithms myself
# - add searching / sorting algorithms
# - put together with the django app
#     - put data in database and do other jobs relevant for the job
#     - add a hashed password to the database
#     - make GUI for different web pages
# - Optional other jobs
#     - add more strategies
#     - test

# Options to add:
# - run stock recommender
# - run specific strategy
# - look for specific stocks (and get their data)
# - sort stocks (by price, ABC, strategy, etc.)
# - Information about strategies