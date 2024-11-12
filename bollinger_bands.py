def bollinger_bands(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, upper_band, middle_band, lower_band,):
    if price > upper_band:
        sell_signal(bought_stocks, sold_stocks, ticker, "(Bollinger Bands)")
    elif price < lower_band:
        buy_signal(bought_stocks, sold_stocks, ticker, "(Bollinger Bands)")