# Program to rotate list by K positions

numbers = [1, 2, 3, 4, 5]
k = int(input("Enter value of K: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Rotated list:", rotated)
#Output
"""Enter value of K: 4
Rotated list: [5, 1, 2, 3, 4]"""