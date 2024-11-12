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