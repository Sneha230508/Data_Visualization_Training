#Pairs with target sum
lst = [1, 2, 3, 4, 5]
target = 5

pairs = []

# Check all pairs
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))

print(pairs)
#Output
"""[(1, 4), (2, 3)]"""