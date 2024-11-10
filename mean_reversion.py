def mean_reversion(bought_stocks, sold_stocks, ticker, price, short_ma):
    lower_bound = short_ma * 0.95
    upper_bound = short_ma * 1.05
    if price > upper_bound:
        print(f"SELL  {ticker}   (Mean Reversion)")
        sold_stocks.append(ticker)
        if ticker in bought_stocks:
            bought_stocks.remove(ticker)
    elif price < lower_bound:
        print(f"BUY   {ticker}   (Mean Reversion)")
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)