#Sort tuples using lambda
data = [("A", 80), ("B", 70), ("C", 90)]

# Sort based on marks (index 1)
data.sort(key=lambda x: x[1])

print(data)
#Output
[('B', 70), ('A', 80), ('C', 90)]