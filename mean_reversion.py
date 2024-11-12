def mean_reversion(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, short_ma):
    lower_bound = short_ma * 0.95
    upper_bound = short_ma * 1.05
    if price > upper_bound:
        sell_signal(bought_stocks, sold_stocks, ticker, "(Mean Reversion)")
    elif price < lower_bound:
        buy_signal(bought_stocks, sold_stocks, ticker, "(Mean Reversion)")