#swap dictionary
d = {"a": 1, "b": 2}

# Swap keys and values using dictionary comprehension
swapped = {v: k for k, v in d.items()}

print(swapped)
#Output
"""{1: 'a', 2: 'b'}"""