#concatenate() --> to join the values of 2 matrices 


import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
#concatenation along columns(vertical)(axis=1)
result = np.concatenate((arr1,arr2),axis=1)
print(result)

#concatenation along rows(horizontal)(axis=0)
result1 = np.concatenate((arr1,arr2),axis=0)
print(result1)
