#reshape() to change the shape of an array and returns a new array

import numpy as np

arr = np.array([1,2,3,4,5,50])
print(arr)
arr1 = arr.reshape(3,2)
print(arr1)


arr2= np.random.randint(0,100,12)
print(arr2)
arr2 = arr2.reshape(4,3)
print(arr2)
print("Array value is :", arr2[0][1])
print("Array value is :", arr2[1][0])
print(arr2.shape)
arr2= arr2.reshape(-1,4)
print(arr2)
arr2 = arr2.reshape(2,-1)
print(arr2)
