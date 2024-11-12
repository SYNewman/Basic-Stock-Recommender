def SMA(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, short_ma, long_ma):
    if short_ma > long_ma:
        buy_signal(bought_stocks, sold_stocks, ticker, "(SMA)")
    else:
        sell_signal(bought_stocks, sold_stocks, ticker, "(SMA)")