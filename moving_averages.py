def moving_averages(ticker, price, short_ma, long_ma):
    if short_ma > long_ma:
        if price > short_ma:
            print(ticker, "BUY (moving averages)")
    
    elif short_ma < long_ma:
        if price < short_ma:
            print(ticker, "SELL (moving averages)")