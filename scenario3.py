import numpy as np

# sales matrix (4 employees × 4 weeks)
sales = np.array([
    [200, 250, 300, 280],
    [150, 180, 200, 220],
    [300, 320, 310, 330],
    [100, 120, 140, 160]
])

# flatten to single row
single_row = sales.reshape(1, -1)

# apply bonus (double sales)
bonus_sales = sales * 2

# highest and lowest sales
highest = sales.max()
lowest = sales.min()

print("Single Row:\n", single_row)
print("Bonus Sales:\n", bonus_sales)
print("Highest:", highest)
print("Lowest:", lowest)