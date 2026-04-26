# Program to merge two lists and remove duplicates

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged = list1 + list2
final_list = []

for item in merged:
    if item not in final_list:
        final_list.append(item)

print("Merged list without duplicates:", final_list)
#Output
"""Merged list without duplicates: [1, 2, 3, 4, 5, 6]"""