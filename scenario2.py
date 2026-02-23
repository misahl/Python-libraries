import numpy as np

# attendance matrix (5 students × 7 days)
attendance = np.array([
    [1,1,0,1,1,1,0],
    [1,0,1,1,1,0,1],
    [1,1,1,1,0,1,1],
    [0,1,1,0,1,1,1],
    [1,1,0,1,1,0,1]
])

# convert to single column
single_col = attendance.reshape(-1, 1)

# attendance percentage per student
percentage = attendance.mean(axis=1) * 100

# students below 75%
low_attendance = percentage < 75

print("Single Column:\n", single_col)
print("Attendance %:", percentage)
print("Low Attendance:", low_attendance)