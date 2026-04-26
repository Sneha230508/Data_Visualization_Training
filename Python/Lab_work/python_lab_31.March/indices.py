#indices greater than value
import numpy as np
arr = np.array([1,5,8,2])

# Get indices where condition is true
print(np.where(arr > 4))
#Output
"""(array([1, 2]),)"""