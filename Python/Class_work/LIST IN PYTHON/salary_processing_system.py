# 4. Salary Processing System

salaries = [25000, 60000, 45000, 80000, 15000]

# Remove below minimum wage (20000)
salaries = [s for s in salaries if s >= 20000]

# Add 5% bonus if salary > 50000
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Updated Salaries:", salaries)
print("Top 3 Salaries:", salaries[:3])
#output
"""Updated Salaries: [84000.0, 63000.0, 45000, 25000]
Top 3 Salaries: [84000.0, 63000.0, 45000]"""