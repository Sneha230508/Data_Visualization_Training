# Program to print multiplication table using while loop

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1
#Output
"""Enter a number: 5
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50"""