import numpy as np
import matplotlib.pyplot as plt

# Given code
f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])


appleprices = np.array(appleprices)

# Generating the graph
x_values = np.arange(1, len(appleprices) + 1)  # Days from 1 to 252

# Formatting
plt.plot(x_values, appleprices, label="Daily Price", color="blue", linewidth=1.5)
plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
plt.xlabel("Day")
plt.ylabel("Trading price")

# Output
plt.grid(True)  # Showing gridlines to make it easier to read
plt.show()
