#Remove Duplicates
lst = [1, 2, 2, 3, 4, 3]
res = []

# Add only unique elements
for i in lst:
    if i not in res:
        res.append(i)

print(res)
#Output
"""[1, 2, 3, 4]"""