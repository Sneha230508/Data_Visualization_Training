#Flatten List
nested = [[1, 2], [3, 4], [5]]
flat = []

# Loop through sublists
for sub in nested:
    for i in sub:
        flat.append(i)   # add elements to flat list

print(flat)
#Output
"""[1, 2, 3, 4, 5]"""