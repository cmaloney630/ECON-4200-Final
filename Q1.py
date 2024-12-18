import numpy as np

# Given code
f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])


#Convert to array
appleprices = np.array(appleprices)

# Calculations
mean_price = np.mean(appleprices)
std_deviation = np.std(appleprices)


print(f"Mean Price: {mean_price}")
print(f"Standard Deviation: {std_deviation}")
