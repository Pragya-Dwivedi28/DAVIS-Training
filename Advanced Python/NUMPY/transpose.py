#transpose() ---> to swap the rows and columns of an array

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# transpose the array (swap rows and columns)
transposed_arr = np.transpose(arr)
print(transposed_arr)
