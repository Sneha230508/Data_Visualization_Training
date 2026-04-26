# 3. Attendance Tracker

attendance = [1, 1, 0, 0, 1, 0, 1]

percentage = (sum(attendance) / len(attendance)) * 100

warning = []
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        warning.append(i)

print("Attendance %:", percentage)
if percentage < 75:
    print("Below 75% Attendance!")

print("Consecutive Absence Index:", warning)

#output
"""Attendance %: 57.14285714285714
Below 75% Attendance!
Consecutive Absence Index: [2]"""