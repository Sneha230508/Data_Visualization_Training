# Program to safely remove a key from dictionary

data = {"a": 1, "b": 2, "c": 3}

key = input("Enter key to remove: ")

if key in data:
    del data[key]
    print("Key removed")
else:
    print("Key not found")

print("Updated dictionary:", data)
#Output
"""Enter key to remove: a
Key removed
Updated dictionary: {'b': 2, 'c': 3}"""