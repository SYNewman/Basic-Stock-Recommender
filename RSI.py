def RSI(buy_signal, sell_signal, data, bought_stocks, sold_stocks, ticker, stock, price, RSI_value):
    # Generates buy/sell signal
    if (RSI_value > 70).any():
        buy_signal(bought_stocks, sold_stocks, ticker, "(RSI)")
    elif (RSI_value < 30).any():
        sell_signal(bought_stocks, sold_stocks, ticker, "(RSI)")