def moving_averages(bought_stocks, sold_stocks, ticker, price, short_ma, long_ma):
    if short_ma > long_ma:
        if price > short_ma:
            print(ticker, "BUY (moving averages)")
            bought_stocks.append(ticker)
    
    elif short_ma < long_ma:
        if price < short_ma:
            print(ticker, "SELL (moving averages)")
            sold_stocks.append(ticker)