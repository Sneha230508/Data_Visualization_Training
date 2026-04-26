#pattern

n = int(input("Enter rows: "))

if n > 0:
    # Upper half
    for rows in range(1, n + 1):
        print(" " * (n - rows) + "*" * (2 * rows - 1))

    # Lower half
    for rows in range(n - 1, 0, -1):
        print(" " * (n - rows) + "*" * (2 * rows - 1))

else:
    print("Not possible")
    #Output
    """Enter rows: 3
  *
 ***
*****
 ***
  *"""
