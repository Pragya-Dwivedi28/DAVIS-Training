# copy() in array in numpy

import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = arr.copy()
arr[0] = 42
print(arr)
print(arr2)
