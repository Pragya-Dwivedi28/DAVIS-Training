#slicing of array in numpy

import numpy as np

arr = np.array([1,2,3,4,5,6,7])
sarr = arr[1:5]
print(arr)
print(sarr)
sarr[2] = 100   #insert 100 in the array
print(arr)
print(sarr)
