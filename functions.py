def remove_duplicates(list): # Function to remove duplicates from the list
    for i in list:
        amount = list.count(i)
        if amount > 1:
            while amount > 1:
                list.remove(i)
                amount = list.count(i)

def remove_stocks_in_both_lists(bought_stocks, sold_stocks): # Function to remove stocks which appear in both lists
    for i in bought_stocks:
        if i in sold_stocks:
            bought_stocks.remove(i)
            sold_stocks.remove(i)
            
def find_stock(bought_stocks, sold_stocks): # Function to find a stock
    stock = input("Enter a stock name: ").upper()
    if stock in bought_stocks:
        print(f"{stock} is in the list of bought stocks")
    elif stock in sold_stocks:
        print(f"{stock} is in the list of sold stocks")
    else:
        print(f"{stock} is not in either list")

def sort_stocks(bought_stocks, sold_stocks): # Function to sort stocks
    print(f"Bought stocks: {bought_stocks}\nSold stocks: {sold_stocks}")
    bought_stocks.sort()
    sold_stocks.sort()
    print(f"Bought stocks: {bought_stocks}\nSold stocks: {sold_stocks}")