#Normalize (0-1)
import numpy as np
arr = np.array([10,20,30])

# Formula: (x - min) / (max - min)
norm = (arr - arr.min()) / (arr.max() - arr.min())

print(norm)
#output
"""[0.  0.5 1. ]"""