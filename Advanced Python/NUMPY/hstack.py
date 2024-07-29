#np.hstack() --> Stacks arrays horizontally (along columns)

import numpy as np
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
# Stack arr1 and arr2 horizontally
result = np.hstack((arr1, arr2))
# Print the horizontally stacked array
print(result)
