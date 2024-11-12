def RSI(data,bought_stocks, sold_stocks, ticker, stock, price, RSI_value):
    # Generates buy/sell signal
    if (RSI_value > 70).any():
        print(f"BUY   {ticker}   (RSI)")
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)
    elif (RSI_value < 30).any():
        print(f"SELL  {ticker}   (RSI)")
        sold_stocks.append(ticker)
        if ticker in bought_stocks:
            bought_stocks.remove(ticker)