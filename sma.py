# Code to run the SMA (simple moving average) strategy
# This is a much simpler version of the strategy which is much more likely to generate a buy/sell signal
def SMA(short_ma, long_ma):
    
    # Code to generate a buy signal
    if short_ma > long_ma:
        print("BUY (SMA)")
        
    # Code to generate a sell signal
    elif short_ma < long_ma:
        print("SELL (SMA)")