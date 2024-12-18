import numpy as np

# Given code
f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices = [float(price) for price in listItems]

def find_max_profit(prices):
    current_max_val = float('-inf')     # Start with a very low value, useful in findMax algorithims
    max_profit_val = 0  		# Starting point for our maximum

    for price in reversed(prices):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

# Output
largest_profit = find_max_profit(appleprices)
print(f"Largest Possible Profit: ${largest_profit:.2f}")
