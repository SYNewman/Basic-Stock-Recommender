# Code to run the SMA (simple moving average) strategy
# This is a much simpler version of the strategy which is much more likely to generate a buy/sell signal
def SMA(bought_stocks, sold_stocks, ticker, short_ma, long_ma):
    if short_ma > long_ma:
        print(f"BUY {ticker}   (SMA)")
        # Code to add/remove the stock from the list of bought/sold stocks
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)
    else:
        print(f"SELL {ticker}   (SMA)")
        bought_stocks.remove(ticker)
        if ticker in sold_stocks:
            sold_stocks.append(ticker)