def moving_averages(bought_stocks, sold_stocks, ticker, price, short_ma, long_ma):
    if short_ma > long_ma:
        if price > short_ma:
            print(ticker, "BUY (moving averages)")
            bought_stocks.append(ticker)
            if ticker in sold_stocks:
                sold_stocks.remove(ticker)
    
    elif short_ma < long_ma:
        if price < short_ma:
            print(ticker, "SELL (moving averages)")
            sold_stocks.append(ticker)
            if ticker in bought_stocks:
                bought_stocks.remove(ticker)
                
    if ticker in bought_stocks:
        if price < short_ma or short_ma < long_ma:
            print(ticker, "SELL (moving averages)")
            sold_stocks.append(ticker)
            bought_stocks.remove(ticker)