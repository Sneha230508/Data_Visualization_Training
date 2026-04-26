# Program to count frequency of elements in list

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1

print("Frequency of elements:")
for key in freq:
    print(key, "->", freq[key])
#Output
"""Frequency of elements:
1 -> 1
2 -> 2
3 -> 1
4 -> 3
5 -> 1"""