# Program to accept numbers until 0 is entered and print sum

sum = 0

while True:
    num = int(input("Enter number (0 to stop): "))
    
    if num == 0:
        break
    
    sum = sum + num

print("Total Sum =", sum)
#Output
"""Enter number (0 to stop): 5
Enter number (0 to stop): 10
Enter number (0 to stop): 3
Enter number (0 to stop): 0
Total Sum = 18"""