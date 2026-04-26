# Program to remove duplicates from list

numbers = [1, 2, 2, 3, 4, 4, 5]
new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print("List after removing duplicates:", new_list)
#Output
"""List after removing duplicates: [1, 2, 3, 4, 5]"""