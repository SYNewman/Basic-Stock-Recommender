def mean_reversion(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, upper_bound, lower_bound):
    if price > upper_bound:
        sell_signal(bought_stocks, sold_stocks, ticker, "(Mean Reversion)")
    elif price < lower_bound:
        buy_signal(bought_stocks, sold_stocks, ticker, "(Mean Reversion)")