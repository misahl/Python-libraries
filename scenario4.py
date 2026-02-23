import numpy as np

temp = np.array([
    [30, 32, 31, 29],
    [28, 27, 30, 31]
])

# increase temperature
new_temp = temp + 2

# maximum temperature
max_temp = temp.max()

print("Updated Temperature:\n", new_temp)
print("Maximum Temperature:", max_temp)