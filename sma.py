# Code to run the SMA (simple moving average) strategy
# This is a much simpler version of the strategy which is much more likely to generate a buy/sell signal
def SMA(bought_stocks, sold_stocks, ticker, short_ma, long_ma):
    
    # Code to generate a buy signal
    if short_ma > long_ma:
        print("BUY (SMA)")
        # Code to add/remove the stock from the list of bought/sold stocks
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)
        
    # Code to generate a sell signal
    elif short_ma < long_ma:
        print("SELL (SMA)")
        bought_stocks.remove(ticker)
        if ticker in sold_stocks:
            sold_stocks.append(ticker)
        
    # Code to run if neither a buy or sell signal is generated
    else:
        bought_stocks.remove(ticker)
        sold_stocks.remove(ticker)