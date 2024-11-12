def bollinger_bands(bought_stocks, sold_stocks, ticker, price, upper_band, middle_band, lower_band):
    if price > upper_band:
        print(f"SELL  {ticker}   (Bollinger Bands)")
        sold_stocks.append(ticker)
        if ticker in bought_stocks:
            bought_stocks.remove(ticker)
    elif price < lower_band:
        print(f"BUY   {ticker}   (Bollinger Bands)")
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)