# Alphabet Pyramid

rows = 5

for i in range(rows):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(i+1):
        print(chr(65+k), end=" ")
    print()
#Output
"""A 
    A B
   A B C
  A B C D
 A B C D E"""  