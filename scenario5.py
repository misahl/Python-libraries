import numpy as np

# travel expenses matrix
expenses = np.array([
    [500, 300, 200],
    [400, 350, 250],
    [450, 320, 280]
])

# convert to single row
single_row = expenses.reshape(1, -1)

# total expense
total = expenses.sum()

print("Single Row:", single_row)
print("Total Expense:", total)