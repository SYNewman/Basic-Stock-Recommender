# This code runs the logic for the RSI strategy
def RSI(bought_stocks, sold_stocks, ticker, stock, price):
    # Code to calculate the RSI
    # ---------- put code to calculate RSI here ----------
    
    # Generates buy/sell signal
    if RSI > 70:
        print(f"BUY   {ticker}   (RSI)")
        bought_stocks.append(ticker)
        if ticker in sold_stocks:
            sold_stocks.remove(ticker)
    elif RSI < 30:
        print(f"SELL  {ticker}   (RSI)")
        sold_stocks.append(ticker)
        if ticker in bought_stocks:
            bought_stocks.remove(ticker)