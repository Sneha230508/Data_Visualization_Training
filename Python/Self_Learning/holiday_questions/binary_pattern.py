# Binary Pattern

for i in range(1,6):
    for j in range(1,i+1):
        print((i+j)%2, end=" ")
    print()
#Output
"""0 
1 0
0 1 0
1 0 1 0
0 1 0 1 0"""