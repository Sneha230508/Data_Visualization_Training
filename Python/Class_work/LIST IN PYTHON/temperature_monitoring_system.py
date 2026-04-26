# 8. Temperature Monitoring System

temps = [35, 42, 39, 46, 30, 41]

hottest = max(temps)
coldest = min(temps)

extreme_days = len([t for t in temps if t > 40])

for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

print("Hottest:", hottest)
print("Coldest:", coldest)
print("Extreme Days (>40):", extreme_days)
print("Updated Temps:", temps)
#output
"""Hottest : 46
Coldest : 30
Extreme Days (>40): 3
Updated Temps:[35,42,39, 'heat alert', 30,41]"""