# This code runs the logic for the moving averages strategy
def moving_averages(bought_stocks, sold_stocks, ticker, price, short_ma, long_ma):
    
    # Code to generate a buy signal
    if short_ma > long_ma:
        if price > short_ma:
            print(f"BUY {ticker}   (Moving Averages)")
            # Adds the stock to the list of bought stocks
            bought_stocks.append(ticker)
            # Removes the stock from the list of sold stocks if is in it
            if ticker in sold_stocks:
                sold_stocks.remove(ticker)
    
    # Code to generate a sell signal
    elif short_ma < long_ma:
        if price < short_ma:
            print(f"SELL {ticker}   (Moving Averages)")
            sold_stocks.append(ticker)
            if ticker in bought_stocks:
                bought_stocks.remove(ticker)
                
    # Code to check if it is time to sell a stock which was previously bought
    if ticker in bought_stocks:
        if price < short_ma or short_ma < long_ma:
            print(f"SELL {ticker}   (Moving Averages)")
            sold_stocks.append(ticker)
            bought_stocks.remove(ticker)