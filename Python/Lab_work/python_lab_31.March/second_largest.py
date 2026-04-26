 List of numbers
lst = [10, 20, 4, 45, 99]

# Initialize largest and second largest
largest = second = float('-inf')

# Loop through list
for num in lst:
    if num > largest:
        second = largest      # update second largest
        largest = num         # update largest
    elif num > second and num != largest:
        second = num          # update second largest

print(second)  # Output second largest
45