import numpy as np

# 3 × 3 matrix (students × assessments)
marks = np.array([
    [20, 18, 15],
    [16, 19, 17],
    [14, 20, 18]
])

# convert into single row matrix for reporting
single_row = marks.reshape(1, -1)

# double marks of a particular assessment (example: 2nd assessment)
marks[:, 1] = marks[:, 1] * 2

print("Original Marks Matrix:\n", marks)
print("Single Row Matrix:\n", single_row)
print("Updated Marks (Assessment doubled):\n", marks)