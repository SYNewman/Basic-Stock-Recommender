# This code runs the logic for the moving averages strategy
def moving_averages(buy_signal, sell_signal, bought_stocks, sold_stocks, ticker, price, short_ma, long_ma):
    if short_ma > long_ma: # Code to generate a buy signal
        if price > short_ma:
            buy_signal(bought_stocks, sold_stocks, ticker, "(Moving Averages)")
    elif short_ma < long_ma: # Code to generate a sell signal
        if price < short_ma:
            sell_signal(bought_stocks, sold_stocks, ticker, "(Moving Averages)")