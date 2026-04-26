a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

# Check each element of list a
for i in a:
    if i in b and i not in common:  # avoid duplicates
        common.append(i)

print(common)
#Output
[3, 4]